"""Fail-closed compatibility adapter for the pinned core W2 producer.

The standalone app pins ``agentic_core`` as an external dependency.  The
currently pinned runner emits several mutually contradictory W2 fields (for
example a failed L2 witness alongside a successful spine proof).  This module
adapts the producer call in-process without editing the pinned checkout.  All
derived fields come from the emitted execution witness and governed X3 receipt.
"""

from __future__ import annotations

import hashlib
import json
import shutil
from contextlib import contextmanager
from pathlib import Path
from threading import RLock
from typing import Any, Iterator, Mapping

from apps_rg.runtime.failure_evidence import atomic_write_json


ADAPTER_SCHEMA = "apps_rg.core_runtime_producer_adapter.v1"
L2_SEALED_ARTIFACT = "l2_sealed_artifact.json"
_PATCH_LOCK = RLock()
_CANONICAL_X3 = {
    "X3A": "X3A_DENY_REROUTE",
    "X3B": "X3B_ESCALATE_HITL",
    "X3C": "X3C_COMMIT_REQUEST_TO_UWG",
    "X3D": "X3D_ALLOW_FINISH",
    "X3E": "X3E_SAFE_ABSTAIN",
}


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _digest(value: Any) -> str:
    return f"sha256:{hashlib.sha256(_canonical_json(value).encode('utf-8')).hexdigest()}"


def _load_payload(root: Path, filename: str) -> dict[str, Any]:
    try:
        value = json.loads((root / filename).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError):
        return {}
    if not isinstance(value, Mapping):
        return {}
    payload = value.get("payload")
    return dict(payload) if isinstance(payload, Mapping) else {}


def _canonical_x3(value: Any) -> str:
    raw = str(value or "").strip()
    if raw in _CANONICAL_X3.values():
        return raw
    return _CANONICAL_X3.get(raw, "")


def _witness_outcome(root: Path) -> dict[str, Any]:
    witness = _load_payload(root, "runtime_execution_witness.json")
    exhaust = _load_payload(root, "runtime_exhaust_bundle.json")
    x3_receipt = _load_payload(root, "x3_disposition_receipt.json")
    l2 = witness.get("l2") if isinstance(witness.get("l2"), Mapping) else {}
    sub_stages = l2.get("sub_stages") if isinstance(l2.get("sub_stages"), list) else []
    failed_sub_stages = [
        str(row.get("sub_stage_id") or "")
        for row in sub_stages
        if isinstance(row, Mapping)
        and str(row.get("status") or "").upper() in {"FAIL", "FAILED", "ERROR"}
    ]
    fault = str(l2.get("fault") or exhaust.get("l2_fault") or "")
    l2_failed = bool(
        fault
        or str(l2.get("status") or "").upper() in {"FAIL", "FAILED", "ERROR"}
        or failed_sub_stages
    )
    x3 = _canonical_x3(
        x3_receipt.get("x3_disposition") or x3_receipt.get("disposition")
    )
    blockers: list[str] = []
    if l2_failed:
        blockers.append(f"L2_EXECUTION_FAILED:{fault or 'witness_status'}")
    blockers.extend(f"L2_SUB_STAGE_FAILED:{stage}" for stage in failed_sub_stages)
    if x3 != "X3D_ALLOW_FINISH":
        blockers.append(f"GOVERNED_EXIT_NOT_ALLOW_FINISH:{x3 or 'missing'}")
    runtime_mode = str(exhaust.get("runtime_mode") or "").strip()
    if l2_failed:
        runtime_mode = "fault"
    return {
        "witness": witness,
        "runtime_mode": runtime_mode or "unknown",
        "l2_failed": l2_failed,
        "fault": fault,
        "failed_sub_stages": failed_sub_stages,
        "x3_disposition": x3,
        "blocking_gaps": list(dict.fromkeys(blockers)),
        "success": not blockers,
    }


def _write_l2_sealed_projection(root: Path, witness: Mapping[str, Any]) -> str:
    l2 = witness.get("l2") if isinstance(witness.get("l2"), Mapping) else {}
    witness_envelope = json.loads(
        (root / "runtime_execution_witness.json").read_text(encoding="utf-8")
    )
    witness_hash = str(witness_envelope.get("artifact_hash") or "")
    payload = {
        "schema_version": "apps_rg.core_l2_sealed_projection.v1",
        "producer_adapter": ADAPTER_SCHEMA,
        "run_id": str(witness.get("run_id") or ""),
        "request_id": str(witness.get("request_id") or ""),
        "trace_root": str(witness.get("trace_root") or ""),
        "route_id": str(witness.get("route_id") or ""),
        "executed": bool(l2.get("executed")),
        "status": str(l2.get("status") or "UNKNOWN"),
        "fault": str(l2.get("fault") or ""),
        "sub_stages": list(l2.get("sub_stages") or []),
        "source_witness_ref": "runtime_execution_witness.json",
        "source_witness_sha256": witness_hash,
    }
    artifact_hash = _digest(payload)
    atomic_write_json(
        root / L2_SEALED_ARTIFACT,
        {
            "producer_component": (
                "apps_rg.runtime.orchestration.core_runtime_producer_adapter"
            ),
            "producer_module": "core_runtime_producer_adapter",
            "producer_function_or_class": "_write_l2_sealed_projection",
            "artifact_hash": artifact_hash,
            "upstream_artifact_ref": witness_hash,
            "payload": payload,
        },
    )
    return artifact_hash


class _HowTraceDocument:
    """Minimal proxy used by the pinned runner's ``to_dict`` call."""

    def __init__(self, payload: Mapping[str, Any]) -> None:
        self._payload = dict(payload)

    def to_dict(self) -> dict[str, Any]:
        return dict(self._payload)


@contextmanager
def adapt_pinned_core_w2_producer(
    core_entrypoint_module: Any,
    *,
    requested_runtime_mode: str,
) -> Iterator[None]:
    """Temporarily make the pinned W2 producer derive one terminal outcome."""

    from agentic_core.L7_auditability import how_trace as how_trace_module
    from agentic_core.L7_auditability.contracts.how_trace import (
        compute_how_trace_digest,
    )
    from agentic_core.runtime.artifacts import spine_proof_bundle as spine_module

    with _PATCH_LOCK:
        original_emit = core_entrypoint_module.emit_artifact
        original_how = how_trace_module.build_how_trace
        original_spine = spine_module.build_spine_proof_payload
        sealed_hash_by_root: dict[Path, str] = {}

        def adapted_emit(
            artifact_dir: Path,
            filename: str,
            payload: Any,
            **kwargs: Any,
        ) -> tuple[Path, str]:
            root = Path(artifact_dir).resolve()
            # The pinned core reuses several filenames that the app-owned
            # section lane has already sealed (Exit and RuntimeExhaust in
            # particular).  Preserve the exact app bytes under the taxonomy's
            # preferred names before core emits its own envelope.  Deferred L6
            # can then consume both authorities without either producer
            # overwriting the other.
            from apps_rg.runtime.section_binding_taxonomy import (
                APPS_RG_SECTION_SHIM_PREFERRED_NAMES,
            )

            preferred_name = APPS_RG_SECTION_SHIM_PREFERRED_NAMES.get(filename)
            existing = root / filename
            if preferred_name and existing.is_file():
                preferred = root / preferred_name
                if not preferred.exists():
                    shutil.copyfile(existing, preferred)
            doc = dict(payload) if isinstance(payload, Mapping) else payload
            if isinstance(doc, dict):
                if filename == "route_contract.json":
                    # The app recipe arrives with preloaded grounding.  The core
                    # shell therefore bypasses its own C0 and must not claim that
                    # its own FinalEvidenceContract is required.
                    doc["grounding_required"] = False
                    doc["producer_adapter"] = ADAPTER_SCHEMA
                elif filename == "x3_disposition_receipt.json":
                    doc["x3_disposition"] = _canonical_x3(
                        doc.get("x3_disposition") or doc.get("disposition")
                    )
                    doc["producer_adapter"] = ADAPTER_SCHEMA
                elif filename == "runtime_execution_witness.json":
                    nested_x2 = doc.get("x2")
                    if isinstance(nested_x2, Mapping):
                        nested_x2 = dict(nested_x2)
                        nested_x2["x3_disposition"] = _canonical_x3(
                            nested_x2.get("x3_disposition")
                            or nested_x2.get("disposition")
                        )
                        doc["x2"] = nested_x2
                    nested_x3 = doc.get("x3")
                    if isinstance(nested_x3, Mapping):
                        nested_x3 = dict(nested_x3)
                        nested_x3["x3_disposition"] = _canonical_x3(
                            nested_x3.get("x3_disposition")
                            or nested_x3.get("disposition")
                        )
                    doc["x3"] = nested_x3
                    doc["producer_adapter"] = ADAPTER_SCHEMA
                elif filename == "exit_review_packet.json":
                    doc["x3_disposition"] = _canonical_x3(
                        doc.get("x3_disposition") or doc.get("disposition")
                    )
                    doc["producer_adapter"] = ADAPTER_SCHEMA
                elif filename == "runtime_exhaust_bundle.json":
                    doc["runtime_mode"] = (
                        "fault"
                        if str(doc.get("l2_fault") or "")
                        else requested_runtime_mode
                    )
                    doc["x3_disposition"] = _canonical_x3(
                        doc.get("x3_disposition")
                    )
                    doc["producer_adapter"] = ADAPTER_SCHEMA
                elif filename == "integrated_runtime_artifact_manifest.json":
                    sealed_hash = sealed_hash_by_root.get(root, "")
                    if sealed_hash:
                        names = list(doc.get("artifact_filenames") or [])
                        if L2_SEALED_ARTIFACT not in names:
                            names.append(L2_SEALED_ARTIFACT)
                        doc["artifact_filenames"] = names
                        hashes = dict(doc.get("artifact_hashes") or {})
                        hashes[L2_SEALED_ARTIFACT] = sealed_hash
                        doc["artifact_hashes"] = hashes
                    doc["producer_adapter"] = ADAPTER_SCHEMA
            written = original_emit(
                artifact_dir,
                filename,
                doc,
                **kwargs,
            )
            if filename == "runtime_execution_witness.json" and isinstance(doc, Mapping):
                sealed_hash_by_root[root] = _write_l2_sealed_projection(root, doc)
            return written

        def adapted_how(artifact_dir: Path, **kwargs: Any) -> _HowTraceDocument:
            root = Path(artifact_dir).resolve()
            trace = original_how(artifact_dir, **kwargs)
            outcome = _witness_outcome(root)
            payload = dict(trace.to_dict())
            payload["runtime_mode"] = outcome["runtime_mode"]
            payload["producer_component"] = (
                "agentic_core.runtime.entrypoints.integrated_single_action_spine_run"
            )
            payload["producer_adapter"] = ADAPTER_SCHEMA
            gaps = [
                str(value)
                for value in payload.get("blocking_gaps", [])
                if str(value)
                not in {
                    "artifact_manifest_missing_at_how_trace_emit_time",
                    "spine_proof_bundle_missing_at_how_trace_emit_time",
                }
            ]
            gaps.extend(outcome["blocking_gaps"])
            payload["blocking_gaps"] = list(dict.fromkeys(gaps))
            payload["success"] = bool(
                outcome["success"]
                and not any(
                    str(stage.get("status") or "").upper() == "FAILED"
                    for stage in payload.get("stages", [])
                    if isinstance(stage, Mapping)
                )
            )
            payload["deterministic_digest"] = compute_how_trace_digest(payload)
            return _HowTraceDocument(payload)

        def adapted_spine(**kwargs: Any) -> dict[str, Any]:
            root = Path(kwargs["artifact_dir"]).resolve()
            outcome = _witness_outcome(root)
            gaps = list(kwargs.get("extra_blocking_gaps") or [])
            gaps.extend(outcome["blocking_gaps"])
            how = _load_payload(root, "agentic_core_how_trace.json")
            if how.get("success") is not True:
                gaps.append("HOW_TRACE_BLOCKED")
            artifact_hashes = dict(kwargs.get("artifact_hashes") or {})
            sealed_hash = sealed_hash_by_root.get(root, "")
            if sealed_hash:
                artifact_hashes[L2_SEALED_ARTIFACT] = sealed_hash
            call = dict(kwargs)
            call["artifact_hashes"] = artifact_hashes
            call["runtime_mode"] = outcome["runtime_mode"]
            call["exit_code"] = 0 if not gaps else 1
            call["extra_blocking_gaps"] = list(dict.fromkeys(gaps))
            payload = original_spine(**call)
            if sealed_hash:
                # The pinned builder overwrites this ref with
                # terminal_ret_packet.json whenever L2 executed.  The shipped
                # verifier, however, resolves the field only against the
                # canonical l2_sealed_artifact.json filename.
                payload["runtime_l2_artifact_ref"] = sealed_hash
            payload["producer_adapter"] = ADAPTER_SCHEMA
            return payload

        core_entrypoint_module.emit_artifact = adapted_emit
        how_trace_module.build_how_trace = adapted_how
        spine_module.build_spine_proof_payload = adapted_spine
        try:
            yield
        finally:
            core_entrypoint_module.emit_artifact = original_emit
            how_trace_module.build_how_trace = original_how
            spine_module.build_spine_proof_payload = original_spine


__all__ = [
    "ADAPTER_SCHEMA",
    "L2_SEALED_ARTIFACT",
    "adapt_pinned_core_w2_producer",
]
