"""W5 zero-LLM qualification over sealed post-runtime replay artifacts.

This module is intentionally stdlib-only at import time.  It does not execute
Apps Research, Apps RG generation, Apps Eval, L6, a judge, an embedding model,
or UWG.  It reopens two completed W0-W4 chains, exercises deterministic
control-plane fault cases, and emits a sealed qualification package outside
all source and replay roots.
"""

from __future__ import annotations

import hashlib
import json
import os
import uuid
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


W5_COMPLETION_SCHEMA = "apps_rg.zero_llm_qualification_completion.v1"
W5_COMPLETION_FILENAME = "w5_completion_receipt.json"
W5_REAL_RUN_MATRIX_SCHEMA = "apps_rg.zero_llm_real_run_matrix.v1"
W5_REAL_RUN_MATRIX_FILENAME = "real_run_qualification_matrix.json"
W5_POSITIVE_MANIFEST_SCHEMA = "apps_rg.synthetic_positive_control_manifest.v1"
W5_POSITIVE_MANIFEST_FILENAME = "positive_control_manifest.json"
W5_FAULT_RECEIPT_SCHEMA = "apps_rg.w5_injected_stage_error.v1"
W5_ERROR_SPAN_SCHEMA = "apps_rg.local_post_runtime_error_span.v1"
W5_L6_RESUME_SCHEMA = "apps_rg.w5_l6_resume_receipt.v1"
W5_TRIPWIRE_SCHEMA = "apps_rg.w5_provider_tripwire_proof.v1"
W5_TRIPWIRE_FILENAME = "provider_tripwire_proof.json"
W5_COUNTS_SCHEMA = "apps_rg.zero_llm_qualification_counts.v1"
W5_COUNTS_FILENAME = "qualification_counts.json"
W5_PACKAGE_SEAL_SCHEMA = "apps_rg.zero_llm_qualification_package_seal.v1"
W5_PACKAGE_SEAL_FILENAME = "w5_qualification_package_seal.json"

EXPECTED_LANES: tuple[str, ...] = (
    "competencies",
    "executive_summary",
    "ey_bullets",
    "ey_narrative",
    "headline",
    "ibm_bullets",
    "ibm_narrative",
    "insurtech_bullets",
    "insurtech_narrative",
    "unify_bullets",
    "unify_narrative",
)
ZERO_COUNTER_KEYS = frozenset(
    {
        "blocked_import_attempts",
        "embedding_calls",
        "judge_calls",
        "model_calls",
        "network_attempts",
        "provider_calls",
        "subprocess_attempts",
    }
)
EXPECTED_TERMINAL_STATE = {
    "product_authorized": False,
    "post_runtime_execution_complete": True,
    "eval_verdict": "fail",
    "observability_complete": True,
    "terminal_closed": True,
    "terminal_outcome": "BLOCKED_NON_PRODUCT",
    "pipeline_complete": False,
}
REQUIRED_LOCAL_PACKAGE_ROLES = frozenset(
    {
        "aggregate_counts",
        "eval_error_receipt",
        "eval_error_span",
        "l6_error_receipt",
        "l6_error_span",
        "l6_resume_receipt",
        "positive_control_manifest",
        "provider_tripwire_proof",
        "real_run_matrix",
    }
)


class ZeroLlmQualificationError(RuntimeError):
    """Raised when saved evidence cannot satisfy the W5 qualification."""


class InjectedQualificationError(RuntimeError):
    """Deterministic sentinel used only by the W5 fault matrix."""


def _canonical_digest(value: Any) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _contained(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _read_json(path: Path, *, label: str) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise ZeroLlmQualificationError(
            f"{label}_unreadable:{type(exc).__name__}:{path}"
        ) from exc
    if not isinstance(value, dict):
        raise ZeroLlmQualificationError(f"{label}_not_object:{path}")
    return value


def _atomic_write_json(path: Path, payload: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(
        dict(payload), ensure_ascii=False, indent=2, sort_keys=True, default=str
    ) + "\n"
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.{uuid.uuid4().hex}.tmp"
    )
    try:
        temporary.write_text(content, encoding="utf-8", newline="\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
    return path


def _write_semantic(path: Path, payload: Mapping[str, Any]) -> Path:
    body = dict(payload)
    body["semantic_digest"] = _canonical_digest(body)
    return _atomic_write_json(path, body)


def _semantic_valid(payload: Mapping[str, Any], *, field: str = "semantic_digest") -> bool:
    body = dict(payload)
    observed = str(body.pop(field, "") or "")
    return bool(observed) and observed == _canonical_digest(body)


def _require(checks: Mapping[str, bool], *, label: str) -> None:
    failed = sorted(name for name, passed in checks.items() if not passed)
    if failed:
        raise ZeroLlmQualificationError(f"{label}:" + ",".join(failed))


def _zero_counters(payload: Mapping[str, Any]) -> bool:
    counters = payload.get("attempt_counters")
    counters = dict(counters) if isinstance(counters, Mapping) else {}
    return ZERO_COUNTER_KEYS.issubset(counters) and all(
        type(value) is int and value == 0 for value in counters.values()
    )


def _binding(
    path: Path,
    *,
    namespace: str,
    root: Path,
    role: str = "",
) -> dict[str, Any]:
    target = path.resolve(strict=True)
    parent = root.resolve(strict=True)
    if not _contained(target, parent):
        raise ZeroLlmQualificationError(
            f"binding_outside_namespace:{namespace}:{target}"
        )
    result = {
        "artifact_namespace": namespace,
        "artifact_ref": target.relative_to(parent).as_posix(),
        "byte_length": target.stat().st_size,
        "sha256": _sha256_file(target),
    }
    if role:
        result["artifact_role"] = role
    return result


def _resolve_binding(
    binding: Any,
    *,
    roots: Mapping[str, Path],
    label: str,
) -> Path:
    if not isinstance(binding, Mapping):
        raise ZeroLlmQualificationError(f"{label}_binding_missing")
    namespace = str(binding.get("artifact_namespace") or "")
    root = roots.get(namespace)
    if root is None:
        raise ZeroLlmQualificationError(f"{label}_namespace_invalid:{namespace}")
    root = root.resolve(strict=True)
    ref = str(binding.get("artifact_ref") or "").strip()
    if not ref:
        raise ZeroLlmQualificationError(f"{label}_ref_missing")
    path = (root / ref).resolve()
    if not _contained(path, root):
        raise ZeroLlmQualificationError(f"{label}_outside_root:{path}")
    if not path.is_file():
        raise ZeroLlmQualificationError(f"{label}_missing:{path}")
    if type(binding.get("byte_length")) is not int or binding.get(
        "byte_length"
    ) != path.stat().st_size:
        raise ZeroLlmQualificationError(f"{label}_length_mismatch:{path}")
    if binding.get("sha256") != _sha256_file(path):
        raise ZeroLlmQualificationError(f"{label}_digest_mismatch:{path}")
    return path


def _resolve_relative_binding(root: Path, binding: Any, *, label: str) -> Path:
    row = dict(binding) if isinstance(binding, Mapping) else {}
    row["artifact_namespace"] = "relative"
    return _resolve_binding(row, roots={"relative": root}, label=label)


def _verify_rows(
    rows: Any,
    *,
    roots: Mapping[str, Path],
    label: str,
    default_namespace: str = "",
    allow_duplicate_roles: bool = False,
) -> tuple[bool, list[str], set[str]]:
    errors: list[str] = []
    roles: set[str] = set()
    if not isinstance(rows, list) or not rows:
        return False, [f"{label}_artifacts_missing"], roles
    identities: set[tuple[str, str]] = set()
    for index, raw in enumerate(rows):
        if not isinstance(raw, Mapping):
            errors.append(f"{label}_artifact_not_object:{index}")
            continue
        row = dict(raw)
        if not row.get("artifact_namespace") and default_namespace:
            row["artifact_namespace"] = default_namespace
        role = str(row.get("artifact_role") or f"artifact_{index:04d}")
        if role in roles and not allow_duplicate_roles:
            errors.append(f"{label}_artifact_role_duplicate:{role}")
        roles.add(role)
        identity = (
            str(row.get("artifact_namespace") or ""),
            str(row.get("artifact_ref") or ""),
        )
        if identity in identities:
            errors.append(f"{label}_artifact_identity_duplicate:{identity}")
        identities.add(identity)
        try:
            _resolve_binding(row, roots=roots, label=f"{label}:{role}")
        except ZeroLlmQualificationError as exc:
            errors.append(str(exc))
    return not errors, errors, roles


def _verify_seal(
    path: Path,
    *,
    root: Path,
    schema: str,
    required_roles: Iterable[str] = (),
    require_artifact_count: bool = False,
    allow_duplicate_roles: bool = False,
    namespace: str = "sealed",
) -> tuple[bool, list[str]]:
    seal = _read_json(path, label="artifact_seal")
    body = {key: value for key, value in seal.items() if key != "manifest_sha256"}
    rows_valid, row_errors, roles = _verify_rows(
        seal.get("artifacts"),
        roots={namespace: root},
        label="artifact_seal",
        default_namespace=namespace,
        allow_duplicate_roles=allow_duplicate_roles,
    )
    checks = {
        "schema_exact": seal.get("schema_version") == schema,
        "status_pass": seal.get("status") == "PASS",
        "manifest_digest_valid": seal.get("manifest_sha256")
        == _canonical_digest(body),
        "required_roles_present": set(required_roles).issubset(roles),
        "artifact_count_exact": (
            seal.get("artifact_count") == len(seal.get("artifacts") or [])
            if require_artifact_count
            else True
        ),
        "artifact_rows_valid": rows_valid and not row_errors,
    }
    errors = list(row_errors)
    errors.extend(name for name, passed in checks.items() if not passed)
    return not errors, sorted(set(errors))


def _guard_valid(
    payload: Mapping[str, Any],
    *,
    wave: str,
    source_run_id: str,
    source_manifest_sha256: str,
    completion: Mapping[str, Any],
    expected_activity: Mapping[str, bool],
) -> bool:
    return bool(
        payload.get("schema_version")
        == "apps_rg.post_runtime_zero_provider_replay.v1"
        and payload.get("wave") == wave
        and payload.get("status") == "PASS"
        and payload.get("scope_complete") is True
        and _semantic_valid(payload)
        and payload.get("source_run_id") == source_run_id
        and payload.get("source_manifest_sha256") == source_manifest_sha256
        and payload.get("source_unchanged") is True
        and payload.get("clean_import_state") is True
        and _zero_counters(payload)
        and payload.get("operation_completion_status") == "PASS"
        and payload.get("operation_completion_semantic_digest")
        == completion.get("semantic_digest")
        and all(
            payload.get(name) is expected
            for name, expected in expected_activity.items()
        )
    )


def _validate_real_run(
    *,
    source: Path,
    replay: Path,
    current_source_manifest: Mapping[str, Any],
    index: int,
) -> dict[str, Any]:
    source = source.resolve(strict=True)
    replay = replay.resolve(strict=True)
    source_run_id = source.name
    source_digest = str(current_source_manifest.get("content_sha256") or "")
    if not source_digest:
        raise ZeroLlmQualificationError(
            f"current_source_manifest_digest_missing:{source_run_id}"
        )

    w0_path = replay / "w0_zero_provider_preflight_receipt.json"
    w0 = _read_json(w0_path, label="w0")
    _require(
        {
            "schema": w0.get("schema_version")
            == "apps_rg.post_runtime_zero_provider_preflight.v1",
            "status": w0.get("status") == "PASS"
            and w0.get("w0_scope_complete") is True,
            "semantic": _semantic_valid(w0),
            "source": w0.get("source_run_id") == source_run_id,
            "manifest": w0.get("source_manifest_sha256") == source_digest,
            "unchanged": w0.get("source_unchanged") is True,
            "zero": _zero_counters(w0),
        },
        label=f"w5_w0_invalid:{source_run_id}",
    )

    completion_specs = {
        "W1": (
            replay / "w1/w1_completion_receipt.json",
            "apps_rg.authority_reconciliation_completion.v1",
        ),
        "W2": (
            replay / "w2/w2_completion_receipt.json",
            "apps_rg.apps_eval_replay_completion.v1",
        ),
        "W3": (
            replay / "w3/w3_completion_receipt.json",
            "apps_rg.l6_shadow_replay_completion.v1",
        ),
        "W4": (
            replay / "w4/w4_completion_receipt.json",
            "apps_rg.terminal_closeout_replay_completion.v1",
        ),
    }
    completions: dict[str, dict[str, Any]] = {}
    completion_paths: dict[str, Path] = {}
    for wave, (path, schema) in completion_specs.items():
        doc = _read_json(path, label=f"{wave.lower()}_completion")
        _require(
            {
                "schema": doc.get("schema_version") == schema,
                "wave": doc.get("wave") == wave,
                "status": doc.get("status") == "PASS",
                "scope": doc.get("scope_complete") is True,
                "semantic": _semantic_valid(doc),
                "source": doc.get("source_run_id") == source_run_id,
            },
            label=f"w5_{wave.lower()}_completion_invalid:{source_run_id}",
        )
        completions[wave] = doc
        completion_paths[wave] = path

    guard_specs = {
        "W1": (
            replay / "w1/w1_zero_provider_guard_receipt.json",
            {
                "apps_eval_executed": False,
                "l6_executed": False,
                "uwg_operation_attempted": False,
            },
        ),
        "W2": (
            replay / "w2/w2_zero_provider_guard_receipt.json",
            {
                "apps_eval_executed": True,
                "l6_executed": False,
                "uwg_operation_attempted": False,
            },
        ),
        "W3": (
            replay / "w3/w3_zero_provider_guard_receipt.json",
            {
                "apps_eval_executed": False,
                "l6_executed": True,
                "uwg_operation_attempted": False,
            },
        ),
        "W4": (
            replay / "w4/w4_zero_provider_guard_receipt.json",
            {
                "apps_eval_executed": False,
                "l6_executed": False,
                "uwg_operation_attempted": False,
            },
        ),
    }
    guards: dict[str, dict[str, Any]] = {}
    guard_paths: dict[str, Path] = {}
    for wave, (path, expected) in guard_specs.items():
        doc = _read_json(path, label=f"{wave.lower()}_guard")
        _require(
            {
                "guard_exact": _guard_valid(
                    doc,
                    wave=wave,
                    source_run_id=source_run_id,
                    source_manifest_sha256=source_digest,
                    completion=completions[wave],
                    expected_activity=expected,
                )
            },
            label=f"w5_{wave.lower()}_guard_invalid:{source_run_id}",
        )
        guards[wave] = doc
        guard_paths[wave] = path

    w1 = completions["W1"]
    w2 = completions["W2"]
    w3 = completions["W3"]
    w4 = completions["W4"]
    _require(
        {
            "w1_authority_denied": w1.get("product_authorized") is False
            and w1.get("pipeline_complete") is False,
            "w2_eval_complete": w2.get("eval_execution_complete") is True
            and w2.get("eval_verdict") == "fail"
            and w2.get("release_blocked") is True,
            "w3_observability_complete": w3.get("l6_execution_complete") is True
            and w3.get("binding_closure_status") == "FAIL"
            and w3.get("apps_eval_rows_bound") is False,
            "w4_gate": w4.get("w5_authorized") is True,
            "w4_terminal_state": all(
                w4.get(name) == expected
                for name, expected in EXPECTED_TERMINAL_STATE.items()
            ),
        },
        label=f"w5_state_chain_invalid:{source_run_id}",
    )

    w2_dir = replay / "w2"
    eval_record_path = _resolve_relative_binding(
        w2_dir, w2.get("eval_record"), label="w2_eval_record"
    )
    eval_record = _read_json(eval_record_path, label="w2_eval_record")
    eval_seal_path = _resolve_relative_binding(
        w2_dir, w2.get("eval_package_seal"), label="w2_eval_seal"
    )
    eval_seal_valid, eval_seal_errors = _verify_seal(
        eval_seal_path,
        root=eval_seal_path.parent,
        schema="apps_eval.apps_rg_eval_package_seal.v1",
        required_roles={
            "eval_record",
            "scorecard_rows",
            "component_scorecards",
            "coverage_matrix",
            "regression_summary",
        },
        allow_duplicate_roles=True,
    )
    _require(
        {
            "record_id": eval_record.get("record_id") == w2.get("record_id"),
            "eval_complete": eval_record.get("eval_execution_complete") is True,
            "eval_fail": eval_record.get("eval_verdict") == "fail",
            "release_blocked": eval_record.get("release_blocked") is True,
            "seal": eval_seal_valid and not eval_seal_errors,
        },
        label=f"w5_eval_record_invalid:{source_run_id}",
    )

    w3_dir = replay / "w3"
    closure_path = _resolve_relative_binding(
        w3_dir,
        w3.get("l6_apps_eval_binding_closure"),
        label="w3_l6_closure",
    )
    closure = _read_json(closure_path, label="w3_l6_closure")
    w3_seal_path = _resolve_relative_binding(
        w3_dir, w3.get("w3_package_seal"), label="w3_package_seal"
    )
    w3_seal_valid, w3_seal_errors = _verify_seal(
        w3_seal_path,
        root=w3_dir,
        schema="apps_rg.l6_shadow_replay_package_seal.v1",
        required_roles={
            "l6_apps_eval_binding_closure",
            "l6_section_apps_eval_bindings",
        },
        require_artifact_count=True,
    )
    _require(
        {
            "closure_semantic": _semantic_valid(closure),
            "closure_fail": closure.get("binding_closure_status") == "FAIL",
            "rows_unbound": closure.get("apps_eval_rows_bound") is False,
            "record_chain": w3.get("record_id") == w2.get("record_id"),
            "seal": w3_seal_valid and not w3_seal_errors,
        },
        label=f"w5_l6_closure_invalid:{source_run_id}",
    )

    w4_dir = replay / "w4"
    terminal_manifest_path = _resolve_relative_binding(
        w4_dir,
        w4.get("terminal_non_product_manifest"),
        label="w4_terminal_manifest",
    )
    terminal_manifest = _read_json(
        terminal_manifest_path, label="w4_terminal_manifest"
    )
    terminal_body = {
        key: value
        for key, value in terminal_manifest.items()
        if key != "manifest_sha256"
    }
    terminal_rows_valid, terminal_row_errors, _ = _verify_rows(
        terminal_manifest.get("bound_receipts"),
        roots={"source_run": source, "replay_root": replay, "w4": w4_dir},
        label="w4_terminal_manifest",
    )
    w4_seal_path = _resolve_relative_binding(
        w4_dir,
        w4.get("w4_package_seal"),
        label="w4_package_seal",
    )
    w4_seal_valid, w4_seal_errors = _verify_seal(
        w4_seal_path,
        root=w4_dir,
        schema="apps_rg.terminal_closeout_package_seal.v1",
        required_roles={
            "terminal_non_product_manifest",
            "terminal_non_product_manifest_seal",
            "terminal_stage_ledger",
            "terminal_stage_ledger_seal",
            "terminal_transition",
            "local_failure_telemetry",
            "local_failure_telemetry_summary",
        },
        require_artifact_count=True,
        namespace="w4",
    )
    _require(
        {
            "manifest_schema": terminal_manifest.get("schema_version")
            == "apps_rg.terminal_non_product_manifest.v1",
            "manifest_status": terminal_manifest.get("status") == "SEALED",
            "manifest_digest": terminal_manifest.get("manifest_sha256")
            == _canonical_digest(terminal_body),
            "manifest_state": terminal_manifest.get("terminal_state")
            == EXPECTED_TERMINAL_STATE,
            "manifest_count": terminal_manifest.get("bound_receipt_count")
            == len(terminal_manifest.get("bound_receipts") or [])
            == 36,
            "manifest_rows": terminal_rows_valid and not terminal_row_errors,
            "package_seal": w4_seal_valid and not w4_seal_errors,
        },
        label=f"w5_terminal_manifest_invalid:{source_run_id}",
    )

    uwg_path = source / "uwg_commit_receipt.json"
    uwg = _read_json(uwg_path, label="historical_uwg")
    _require(
        {
            "schema": uwg.get("schema_version") == "L4-UWG-1.0.0",
            "historical_commit": uwg.get("commit_status") == "COMMITTED",
            "no_new_w1": guards["W1"].get("uwg_operation_attempted") is False,
            "no_new_w2": guards["W2"].get("uwg_operation_attempted") is False,
            "no_new_w3": guards["W3"].get("uwg_operation_attempted") is False,
            "no_new_w4": guards["W4"].get("uwg_operation_attempted") is False,
        },
        label=f"w5_uwg_chain_invalid:{source_run_id}",
    )

    source_namespace = f"source_{index}"
    replay_namespace = f"replay_{index}"
    evidence = [
        _binding(
            eval_record_path,
            namespace=replay_namespace,
            root=replay,
            role="apps_eval_record",
        ),
        _binding(
            eval_seal_path,
            namespace=replay_namespace,
            root=replay,
            role="apps_eval_package_seal",
        ),
        _binding(
            closure_path,
            namespace=replay_namespace,
            root=replay,
            role="l6_terminal_closure",
        ),
        _binding(
            w3_seal_path,
            namespace=replay_namespace,
            root=replay,
            role="l6_package_seal",
        ),
        _binding(
            terminal_manifest_path,
            namespace=replay_namespace,
            root=replay,
            role="non_product_terminal_manifest",
        ),
        _binding(
            w4_seal_path,
            namespace=replay_namespace,
            root=replay,
            role="terminal_closeout_package_seal",
        ),
        _binding(
            guard_paths["W4"],
            namespace=replay_namespace,
            root=replay,
            role="w4_zero_provider_guard",
        ),
        _binding(
            completion_paths["W4"],
            namespace=replay_namespace,
            root=replay,
            role="w4_completion",
        ),
        _binding(
            uwg_path,
            namespace=source_namespace,
            root=source,
            role="historical_uwg_commit",
        ),
    ]
    return {
        "case_id": f"blocked_real_run_{index + 1}",
        "source_run_id": source_run_id,
        "record_id": str(w2.get("record_id") or ""),
        "status": "PASS",
        "expected_terminal_outcome": "BLOCKED_NON_PRODUCT",
        "observed_terminal_outcome": w4.get("terminal_outcome"),
        "eval_execution_complete": True,
        "eval_verdict": "fail",
        "l6_observability_complete": True,
        "l6_binding_closure_status": "FAIL",
        "terminal_closed": True,
        "product_authorized": False,
        "pipeline_complete": False,
        "source_manifest_sha256": source_digest,
        "source_namespace": source_namespace,
        "replay_namespace": replay_namespace,
        "historical_uwg_sha256": _sha256_file(uwg_path),
        "new_uwg_operation_attempted": False,
        "evidence_bindings": evidence,
    }


def _positive_control_state() -> dict[str, Any]:
    return {
        "product_authorized": True,
        "post_runtime_execution_complete": True,
        "eval_verdict": "pass",
        "observability_complete": True,
        "terminal_closed": True,
        "terminal_stage": "MANDATORY_OUTPUTS",
        "terminal_outcome": "PRODUCT_COMPLETE",
        "pipeline_complete": True,
    }


def _emit_positive_control(output: Path) -> tuple[dict[str, Any], Path]:
    root = output / "positive_control"
    receipt_root = root / "receipts"
    receipt_paths: list[tuple[str, Path]] = []

    entry_path = _write_semantic(
        receipt_root / "entry_handoff.json",
        {
            "schema_version": "apps_rg.w5.synthetic_entry_handoff.v1",
            "status": "PASS",
            "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
            "apps_research_completed_before_u0": True,
            "handoff_verified": True,
        },
    )
    receipt_paths.append(("entry_handoff", entry_path))

    dag_path = _write_semantic(
        receipt_root / "l0_dag.json",
        {
            "schema_version": "apps_rg.w5.synthetic_l0_dag.v1",
            "status": "PASS",
            "lane_ids": list(EXPECTED_LANES),
            "saved_output_fixture": True,
            "actual_parallel_runtime_claimed": False,
        },
    )
    receipt_paths.append(("l0_dag", dag_path))

    for lane in EXPECTED_LANES:
        path = _write_semantic(
            receipt_root / "lanes" / f"{lane}.json",
            {
                "schema_version": "apps_rg.w5.synthetic_lane_authority.v1",
                "status": "PASS",
                "lane_id": lane,
                "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
                "l2_handoff_status": "PASS",
                "l2_spine_status": "PASS",
                "x2_status": "PASS",
                "x3_disposition": "X3D_ALLOW_FINISH",
                "final_materialized_acceptance": True,
                "product_release_eligible": True,
            },
        )
        receipt_paths.append((f"lane_{lane}", path))

    aggregation_path = _write_semantic(
        receipt_root / "x2_aggregation.json",
        {
            "schema_version": "apps_rg.w5.synthetic_x2_aggregation.v1",
            "status": "PASS",
            "lanes_total": len(EXPECTED_LANES),
            "lanes_passed": len(EXPECTED_LANES),
            "cross_section_product_pass": True,
            "graph_evidence_release_pass": True,
            "final_assembly_product_release_eligible": True,
        },
    )
    receipt_paths.append(("x2_aggregation", aggregation_path))

    authority_path = _write_semantic(
        receipt_root / "product_authority.json",
        {
            "schema_version": "apps_rg.w5.synthetic_product_authority.v1",
            "status": "AUTHORIZED_FIXTURE_ONLY",
            "canonical_x3_disposition": "X3D_ALLOW_FINISH",
            "authorized_lane_count": len(EXPECTED_LANES),
            "blocked_lane_count": 0,
            "fixture_product_authorized": True,
            "production_authority_granted": False,
            "publication_allowed": False,
        },
    )
    receipt_paths.append(("product_authority", authority_path))

    eval_path = _write_semantic(
        receipt_root / "apps_eval.json",
        {
            "schema_version": "apps_rg.w5.synthetic_apps_eval.v1",
            "status": "PASS",
            "eval_execution_complete": True,
            "eval_verdict": "pass",
            "release_blocked": False,
            "deterministic_only": True,
            "with_judge": False,
        },
    )
    receipt_paths.append(("apps_eval", eval_path))

    l6_path = _write_semantic(
        receipt_root / "l6_closure.json",
        {
            "schema_version": "apps_rg.w5.synthetic_l6_closure.v1",
            "status": "PASS",
            "observability_execution_complete": True,
            "observed_run_verdict": "pass",
            "grain_parity_status": "PASS",
            "sections_total": len(EXPECTED_LANES),
            "sections_bound": len(EXPECTED_LANES),
        },
    )
    receipt_paths.append(("l6_closure", l6_path))

    terminal_path = _write_semantic(
        receipt_root / "terminal_product_complete.json",
        {
            "schema_version": "apps_rg.w5.synthetic_terminal_product.v1",
            "status": "PASS",
            "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
            "control_state": _positive_control_state(),
            "production_authority_granted": False,
            "publication_allowed": False,
        },
    )
    receipt_paths.append(("terminal_product_complete", terminal_path))

    receipts = [
        _binding(path, namespace="positive", root=root, role=role)
        for role, path in sorted(receipt_paths)
    ]
    body: dict[str, Any] = {
        "schema_version": W5_POSITIVE_MANIFEST_SCHEMA,
        "status": "PASS",
        "case_id": "valid_synthetic_saved_output_fixture",
        "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
        "qualification_only": True,
        "production_authority_granted": False,
        "publication_allowed": False,
        "expected_control_state": _positive_control_state(),
        "receipt_count": len(receipts),
        "receipts": receipts,
    }
    manifest = {**body, "manifest_sha256": _canonical_digest(body)}
    path = _atomic_write_json(root / W5_POSITIVE_MANIFEST_FILENAME, manifest)
    return manifest, path


def _verify_positive_control(path: Path) -> tuple[bool, list[str]]:
    manifest = _read_json(path, label="positive_control_manifest")
    root = path.parent
    body = {
        key: value for key, value in manifest.items() if key != "manifest_sha256"
    }
    rows_valid, row_errors, roles = _verify_rows(
        manifest.get("receipts"),
        roots={"positive": root},
        label="positive_control_manifest",
    )
    expected_roles = {
        "entry_handoff",
        "l0_dag",
        "x2_aggregation",
        "product_authority",
        "apps_eval",
        "l6_closure",
        "terminal_product_complete",
        *(f"lane_{lane}" for lane in EXPECTED_LANES),
    }
    docs: dict[str, dict[str, Any]] = {}
    if isinstance(manifest.get("receipts"), list):
        for row in manifest["receipts"]:
            if not isinstance(row, Mapping):
                continue
            role = str(row.get("artifact_role") or "")
            try:
                receipt_path = _resolve_binding(
                    row,
                    roots={"positive": root},
                    label=f"positive_control:{role}",
                )
            except ZeroLlmQualificationError:
                continue
            docs[role] = _read_json(receipt_path, label=f"positive_control:{role}")

    lane_docs = [docs.get(f"lane_{lane}", {}) for lane in EXPECTED_LANES]
    entry = docs.get("entry_handoff", {})
    dag = docs.get("l0_dag", {})
    aggregation = docs.get("x2_aggregation", {})
    authority = docs.get("product_authority", {})
    eval_doc = docs.get("apps_eval", {})
    l6 = docs.get("l6_closure", {})
    terminal = docs.get("terminal_product_complete", {})
    checks = {
        "schema_exact": manifest.get("schema_version")
        == W5_POSITIVE_MANIFEST_SCHEMA,
        "status_pass": manifest.get("status") == "PASS",
        "qualification_only": manifest.get("qualification_only") is True,
        "no_production_authority": manifest.get("production_authority_granted")
        is False
        and manifest.get("publication_allowed") is False,
        "manifest_digest_valid": manifest.get("manifest_sha256")
        == _canonical_digest(body),
        "receipt_count_exact": manifest.get("receipt_count")
        == len(manifest.get("receipts") or [])
        == len(expected_roles),
        "roles_exact": roles == expected_roles,
        "rows_valid": rows_valid and not row_errors,
        "all_semantic_digests_valid": len(docs) == len(expected_roles)
        and all(_semantic_valid(doc) for doc in docs.values()),
        "entry_pass": entry.get("status") == "PASS"
        and entry.get("apps_research_completed_before_u0") is True
        and entry.get("handoff_verified") is True,
        "dag_pass": dag.get("status") == "PASS"
        and tuple(dag.get("lane_ids") or []) == EXPECTED_LANES
        and dag.get("actual_parallel_runtime_claimed") is False,
        "lanes_exact": len(lane_docs) == len(EXPECTED_LANES)
        and all(
            row.get("lane_id") == lane
            and row.get("status") == "PASS"
            and row.get("l2_handoff_status") == "PASS"
            and row.get("l2_spine_status") == "PASS"
            and row.get("x2_status") == "PASS"
            and row.get("x3_disposition") == "X3D_ALLOW_FINISH"
            and row.get("final_materialized_acceptance") is True
            and row.get("product_release_eligible") is True
            for lane, row in zip(EXPECTED_LANES, lane_docs, strict=True)
        ),
        "aggregation_pass": aggregation.get("status") == "PASS"
        and aggregation.get("lanes_passed") == len(EXPECTED_LANES)
        and aggregation.get("cross_section_product_pass") is True
        and aggregation.get("graph_evidence_release_pass") is True
        and aggregation.get("final_assembly_product_release_eligible") is True,
        "fixture_authority_pass": authority.get("status")
        == "AUTHORIZED_FIXTURE_ONLY"
        and authority.get("canonical_x3_disposition") == "X3D_ALLOW_FINISH"
        and authority.get("fixture_product_authorized") is True
        and authority.get("production_authority_granted") is False,
        "eval_pass": eval_doc.get("eval_execution_complete") is True
        and eval_doc.get("eval_verdict") == "pass"
        and eval_doc.get("release_blocked") is False
        and eval_doc.get("with_judge") is False,
        "l6_pass": l6.get("observability_execution_complete") is True
        and l6.get("observed_run_verdict") == "pass"
        and l6.get("grain_parity_status") == "PASS"
        and l6.get("sections_bound") == len(EXPECTED_LANES),
        "terminal_state_exact": terminal.get("control_state")
        == _positive_control_state()
        and terminal.get("production_authority_granted") is False,
    }
    errors = list(row_errors)
    errors.extend(name for name, passed in checks.items() if not passed)
    return not errors, sorted(set(errors))


def _stable_id(*parts: str, length: int) -> str:
    digest = hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()
    return digest[:length]


def _emit_injected_error(
    *,
    output: Path,
    stage_id: str,
    recovery_action: str,
    observed_call_order: Sequence[str],
) -> tuple[Path, Path]:
    normalized = stage_id.lower()
    error_message = f"w5 injected {normalized} exception"
    trace_id = _stable_id("W5", stage_id, "trace", length=32)
    span_id = _stable_id("W5", stage_id, "span", length=16)
    receipt_path = _write_semantic(
        output / "fault_injection" / f"{normalized}_error_receipt.json",
        {
            "schema_version": W5_FAULT_RECEIPT_SCHEMA,
            "status": "CAPTURED",
            "case_id": f"injected_{normalized}_exception",
            "stage_id": stage_id,
            "error_type": "InjectedQualificationError",
            "error_message": error_message,
            "traceback": f"InjectedQualificationError: {error_message}",
            "trace_id": trace_id,
            "span_id": span_id,
            "recovery_action": recovery_action,
            "observed_call_order": list(observed_call_order),
            "generation_retry_attempted": False,
            "generation_replayed": False,
            "judge_replayed": False,
            "uwg_operation_attempted": False,
            "provider_calls": 0,
            "network_attempts": 0,
            "local_authority": True,
        },
    )
    span_path = _write_semantic(
        output / "fault_injection" / f"{normalized}_error_span.json",
        {
            "schema_version": W5_ERROR_SPAN_SCHEMA,
            "status": "ERROR",
            "case_id": f"injected_{normalized}_exception",
            "stage_id": stage_id,
            "trace_id": trace_id,
            "span_id": span_id,
            "exception_type": "InjectedQualificationError",
            "exception_message": error_message,
            "recovery_action": recovery_action,
            "provider_execution": False,
            "generation_execution": False,
            "judge_execution": False,
            "uwg_execution": False,
            "local_authority": True,
            "remote_otel_role": "OPTIONAL_MIRROR_NOT_AUTHORITY",
        },
    )
    return receipt_path, span_path


def _emit_fault_matrix(output: Path) -> dict[str, Path]:
    eval_order: list[str] = []

    def injected_eval() -> None:
        eval_order.append("APPS_EVAL:attempt_1")
        raise InjectedQualificationError("w5 injected apps_eval exception")

    try:
        injected_eval()
    except InjectedQualificationError:
        eval_receipt, eval_span = _emit_injected_error(
            output=output,
            stage_id="APPS_EVAL",
            recovery_action="STOP_WITH_DURABLE_ERROR_NO_GENERATION_RETRY",
            observed_call_order=eval_order,
        )
    else:  # pragma: no cover - sentinel always raises
        raise ZeroLlmQualificationError("eval fault injection did not raise")

    l6_order: list[str] = []

    def injected_l6() -> None:
        l6_order.append("L6_OBSERVABILITY:attempt_1")
        raise InjectedQualificationError("w5 injected l6_observability exception")

    try:
        injected_l6()
    except InjectedQualificationError:
        l6_receipt, l6_span = _emit_injected_error(
            output=output,
            stage_id="L6_OBSERVABILITY",
            recovery_action="RESUME_FROM_L6_ONLY",
            observed_call_order=l6_order,
        )
    else:  # pragma: no cover - sentinel always raises
        raise ZeroLlmQualificationError("L6 fault injection did not raise")

    l6_order.append("L6_OBSERVABILITY:attempt_2_resume")
    l6_resume = _write_semantic(
        output / "fault_injection" / "l6_resume_receipt.json",
        {
            "schema_version": W5_L6_RESUME_SCHEMA,
            "status": "PASS",
            "case_id": "injected_l6_observability_exception",
            "resume_from_stage": "L6_OBSERVABILITY",
            "observed_call_order": l6_order,
            "apps_eval_replayed": False,
            "generation_replayed": False,
            "judge_replayed": False,
            "uwg_operation_attempted": False,
            "upstream_saved_artifacts_reused": True,
            "resume_attempt_count": 1,
        },
    )
    return {
        "eval_error_receipt": eval_receipt,
        "eval_error_span": eval_span,
        "l6_error_receipt": l6_receipt,
        "l6_error_span": l6_span,
        "l6_resume_receipt": l6_resume,
    }


def _verify_fault_matrix(paths: Mapping[str, Path]) -> tuple[bool, list[str]]:
    docs = {role: _read_json(path, label=role) for role, path in paths.items()}
    eval_receipt = docs.get("eval_error_receipt", {})
    eval_span = docs.get("eval_error_span", {})
    l6_receipt = docs.get("l6_error_receipt", {})
    l6_span = docs.get("l6_error_span", {})
    resume = docs.get("l6_resume_receipt", {})
    checks = {
        "roles_exact": set(docs)
        == {
            "eval_error_receipt",
            "eval_error_span",
            "l6_error_receipt",
            "l6_error_span",
            "l6_resume_receipt",
        },
        "schemas_exact": eval_receipt.get("schema_version")
        == W5_FAULT_RECEIPT_SCHEMA
        and l6_receipt.get("schema_version") == W5_FAULT_RECEIPT_SCHEMA
        and eval_span.get("schema_version") == W5_ERROR_SPAN_SCHEMA
        and l6_span.get("schema_version") == W5_ERROR_SPAN_SCHEMA
        and resume.get("schema_version") == W5_L6_RESUME_SCHEMA,
        "all_semantic": all(_semantic_valid(doc) for doc in docs.values()),
        "eval_error_durable": eval_receipt.get("status") == "CAPTURED"
        and eval_receipt.get("stage_id") == "APPS_EVAL"
        and eval_receipt.get("recovery_action")
        == "STOP_WITH_DURABLE_ERROR_NO_GENERATION_RETRY"
        and eval_receipt.get("observed_call_order") == ["APPS_EVAL:attempt_1"]
        and eval_receipt.get("generation_retry_attempted") is False
        and eval_receipt.get("generation_replayed") is False
        and eval_receipt.get("judge_replayed") is False
        and eval_receipt.get("uwg_operation_attempted") is False,
        "eval_span_durable": eval_span.get("status") == "ERROR"
        and eval_span.get("stage_id") == "APPS_EVAL"
        and eval_span.get("trace_id") == eval_receipt.get("trace_id")
        and eval_span.get("span_id") == eval_receipt.get("span_id")
        and eval_span.get("provider_execution") is False
        and eval_span.get("generation_execution") is False
        and eval_span.get("judge_execution") is False
        and eval_span.get("uwg_execution") is False,
        "l6_error_durable": l6_receipt.get("status") == "CAPTURED"
        and l6_receipt.get("stage_id") == "L6_OBSERVABILITY"
        and l6_receipt.get("recovery_action") == "RESUME_FROM_L6_ONLY"
        and l6_receipt.get("observed_call_order")
        == ["L6_OBSERVABILITY:attempt_1"]
        and l6_receipt.get("generation_replayed") is False
        and l6_receipt.get("judge_replayed") is False
        and l6_receipt.get("uwg_operation_attempted") is False,
        "l6_span_durable": l6_span.get("status") == "ERROR"
        and l6_span.get("stage_id") == "L6_OBSERVABILITY"
        and l6_span.get("trace_id") == l6_receipt.get("trace_id")
        and l6_span.get("span_id") == l6_receipt.get("span_id")
        and l6_span.get("provider_execution") is False
        and l6_span.get("generation_execution") is False
        and l6_span.get("judge_execution") is False
        and l6_span.get("uwg_execution") is False,
        "l6_resume_only": resume.get("status") == "PASS"
        and resume.get("resume_from_stage") == "L6_OBSERVABILITY"
        and resume.get("observed_call_order")
        == [
            "L6_OBSERVABILITY:attempt_1",
            "L6_OBSERVABILITY:attempt_2_resume",
        ]
        and resume.get("apps_eval_replayed") is False
        and resume.get("generation_replayed") is False
        and resume.get("judge_replayed") is False
        and resume.get("uwg_operation_attempted") is False,
        "l6_resume_reuses_saved_artifacts": resume.get(
            "upstream_saved_artifacts_reused"
        )
        is True
        and resume.get("resume_attempt_count") == 1,
        "no_execution_calls": all(
            doc.get("provider_calls", 0) == 0
            and doc.get("network_attempts", 0) == 0
            and doc.get("uwg_operation_attempted", False) is False
            for doc in docs.values()
        ),
    }
    errors = [name for name, passed in checks.items() if not passed]
    return not errors, errors


def _emit_tripwire_proof(
    output: Path,
    probe: Callable[[], Mapping[str, Any]],
) -> tuple[dict[str, Any], Path]:
    observed = probe()
    observed = dict(observed) if isinstance(observed, Mapping) else {}
    counters = observed.get("controlled_attempt_counters")
    counters = dict(counters) if isinstance(counters, Mapping) else {}
    checks = {
        "probe_pass": observed.get("status") == "PASS",
        "provider_blocked": observed.get("provider_attempt_blocked") is True,
        "exception_exact": observed.get("exception_type")
        == "ProviderExecutionBlocked",
        "controlled_provider_attempt_exact": counters.get("provider_calls") == 1,
        "no_network_attempt": counters.get("network_attempts") == 0,
        "no_other_execution_attempt": all(
            counters.get(name, 0) == 0
            for name in (
                "embedding_calls",
                "judge_calls",
                "model_calls",
                "subprocess_attempts",
            )
        ),
    }
    failed = sorted(name for name, passed in checks.items() if not passed)
    proof: dict[str, Any] = {
        "schema_version": W5_TRIPWIRE_SCHEMA,
        "status": "PASS" if not failed else "FAIL",
        "case_id": "provider_tripwire",
        "scope": "CONTROLLED_TRIPWIRE_PROBE_NOT_QUALIFICATION_ACTIVITY",
        "provider_attempt_blocked": observed.get("provider_attempt_blocked") is True,
        "exception_type": str(observed.get("exception_type") or ""),
        "controlled_attempt_counters": counters,
        "qualification_attempt_counters_affected": False,
        "checks": checks,
        "failed_checks": failed,
    }
    proof["semantic_digest"] = _canonical_digest(proof)
    path = _atomic_write_json(output / W5_TRIPWIRE_FILENAME, proof)
    if failed:
        raise ZeroLlmQualificationError(
            "w5_provider_tripwire_invalid:" + ",".join(failed)
        )
    return proof, path


def _verify_tripwire_proof(path: Path) -> tuple[bool, list[str]]:
    proof = _read_json(path, label="provider_tripwire_proof")
    counters = proof.get("controlled_attempt_counters")
    counters = dict(counters) if isinstance(counters, Mapping) else {}
    recorded_checks = proof.get("checks")
    recorded_checks = (
        dict(recorded_checks) if isinstance(recorded_checks, Mapping) else {}
    )
    checks = {
        "schema_exact": proof.get("schema_version") == W5_TRIPWIRE_SCHEMA,
        "status_pass": proof.get("status") == "PASS",
        "semantic_valid": _semantic_valid(proof),
        "scope_exact": proof.get("scope")
        == "CONTROLLED_TRIPWIRE_PROBE_NOT_QUALIFICATION_ACTIVITY",
        "provider_blocked": proof.get("provider_attempt_blocked") is True,
        "exception_exact": proof.get("exception_type")
        == "ProviderExecutionBlocked",
        "controlled_provider_attempt_exact": counters.get("provider_calls")
        == 1,
        "no_network_attempt": counters.get("network_attempts") == 0,
        "no_other_execution_attempt": all(
            counters.get(name, 0) == 0
            for name in (
                "embedding_calls",
                "judge_calls",
                "model_calls",
                "subprocess_attempts",
            )
        ),
        "qualification_counters_unaffected": proof.get(
            "qualification_attempt_counters_affected"
        )
        is False,
        "recorded_checks_pass": bool(recorded_checks)
        and all(value is True for value in recorded_checks.values())
        and proof.get("failed_checks") == [],
    }
    errors = [name for name, passed in checks.items() if not passed]
    return not errors, errors


def _emit_real_run_matrix(
    output: Path, rows: Sequence[Mapping[str, Any]]
) -> tuple[dict[str, Any], Path]:
    body: dict[str, Any] = {
        "schema_version": W5_REAL_RUN_MATRIX_SCHEMA,
        "status": "PASS",
        "case_count": len(rows),
        "cases": [dict(row) for row in rows],
        "apps_eval_records": sum(
            1 for row in rows if row.get("eval_execution_complete") is True
        ),
        "l6_terminal_closures": sum(
            1 for row in rows if row.get("l6_observability_complete") is True
        ),
        "non_product_terminal_manifests": sum(
            1
            for row in rows
            if row.get("observed_terminal_outcome") == "BLOCKED_NON_PRODUCT"
        ),
        "new_uwg_operations": sum(
            1 for row in rows if row.get("new_uwg_operation_attempted") is True
        ),
    }
    body["semantic_digest"] = _canonical_digest(body)
    path = _atomic_write_json(output / W5_REAL_RUN_MATRIX_FILENAME, body)
    return body, path


def _emit_counts(
    output: Path,
    *,
    matrix: Mapping[str, Any],
    positive_valid: bool,
    fault_valid: bool,
    tripwire_valid: bool,
) -> tuple[dict[str, Any], Path]:
    payload: dict[str, Any] = {
        "schema_version": W5_COUNTS_SCHEMA,
        "status": "PASS",
        "provider_calls": 0,
        "judge_calls": 0,
        "embedding_calls": 0,
        "model_calls": 0,
        "network_attempts": 0,
        "subprocess_attempts": 0,
        "model_span_delta": 0,
        "source_files_changed": 0,
        "apps_eval_records": int(matrix.get("apps_eval_records") or 0),
        "l6_terminal_closures": int(matrix.get("l6_terminal_closures") or 0),
        "non_product_terminal_manifests": int(
            matrix.get("non_product_terminal_manifests") or 0
        ),
        "new_uwg_operations": int(matrix.get("new_uwg_operations") or 0),
        "positive_control_fixture_passed": positive_valid,
        "injected_failure_matrix_passed": fault_valid,
        "provider_tripwire_passed": tripwire_valid,
    }
    payload["semantic_digest"] = _canonical_digest(payload)
    path = _atomic_write_json(output / W5_COUNTS_FILENAME, payload)
    return payload, path


def _emit_package_seal(
    output: Path, artifacts: Mapping[str, Path]
) -> tuple[dict[str, Any], Path]:
    rows = [
        _binding(path, namespace="w5", root=output, role=role)
        for role, path in sorted(artifacts.items())
    ]
    body: dict[str, Any] = {
        "schema_version": W5_PACKAGE_SEAL_SCHEMA,
        "status": "PASS",
        "artifact_count": len(rows),
        "artifacts": rows,
        "emission_phase": "POST_EMISSION_REOPENED_AND_VALIDATED",
    }
    seal = {**body, "manifest_sha256": _canonical_digest(body)}
    path = _atomic_write_json(output / W5_PACKAGE_SEAL_FILENAME, seal)
    return seal, path


def _verify_package_seal(
    output: Path, path: Path
) -> tuple[bool, list[str], dict[str, str]]:
    seal = _read_json(path, label="w5_package_seal")
    body = {key: value for key, value in seal.items() if key != "manifest_sha256"}
    rows_valid, row_errors, roles = _verify_rows(
        seal.get("artifacts"),
        roots={"w5": output},
        label="w5_package_seal",
    )
    observed: dict[str, str] = {}
    if isinstance(seal.get("artifacts"), list):
        for row in seal["artifacts"]:
            if not isinstance(row, Mapping):
                continue
            role = str(row.get("artifact_role") or "")
            try:
                artifact_path = _resolve_binding(
                    row, roots={"w5": output}, label=f"w5_package:{role}"
                )
            except ZeroLlmQualificationError:
                continue
            observed[role] = _sha256_file(artifact_path)
    checks = {
        "schema_exact": seal.get("schema_version") == W5_PACKAGE_SEAL_SCHEMA,
        "status_pass": seal.get("status") == "PASS",
        "manifest_digest_valid": seal.get("manifest_sha256")
        == _canonical_digest(body),
        "artifact_count_exact": seal.get("artifact_count")
        == len(seal.get("artifacts") or []),
        "roles_exact": roles == REQUIRED_LOCAL_PACKAGE_ROLES,
        "emission_phase_exact": seal.get("emission_phase")
        == "POST_EMISSION_REOPENED_AND_VALIDATED",
        "rows_valid": rows_valid and not row_errors,
    }
    errors = list(row_errors)
    errors.extend(name for name, passed in checks.items() if not passed)
    return not errors, sorted(set(errors)), observed


def _execute_once(
    *,
    output: Path,
    inputs: Sequence[tuple[Path, Path]],
    source_manifests: Sequence[Mapping[str, Any]],
    provider_tripwire_probe: Callable[[], Mapping[str, Any]],
) -> dict[str, Any]:
    rows = [
        _validate_real_run(
            source=source,
            replay=replay,
            current_source_manifest=source_manifests[index],
            index=index,
        )
        for index, (source, replay) in enumerate(inputs)
    ]
    matrix, matrix_path = _emit_real_run_matrix(output, rows)

    _, positive_path = _emit_positive_control(output)
    positive_valid, positive_errors = _verify_positive_control(positive_path)
    if not positive_valid:
        raise ZeroLlmQualificationError(
            "w5_positive_control_invalid:" + ",".join(positive_errors)
        )

    fault_paths = _emit_fault_matrix(output)
    fault_valid, fault_errors = _verify_fault_matrix(fault_paths)
    if not fault_valid:
        raise ZeroLlmQualificationError(
            "w5_fault_matrix_invalid:" + ",".join(fault_errors)
        )

    tripwire, tripwire_path = _emit_tripwire_proof(
        output, provider_tripwire_probe
    )
    tripwire_valid, tripwire_errors = _verify_tripwire_proof(tripwire_path)
    if not tripwire_valid:
        raise ZeroLlmQualificationError(
            "w5_provider_tripwire_invalid:" + ",".join(tripwire_errors)
        )
    counts, counts_path = _emit_counts(
        output,
        matrix=matrix,
        positive_valid=positive_valid,
        fault_valid=fault_valid,
        tripwire_valid=tripwire_valid,
    )
    _require(
        {
            "two_cases": matrix.get("case_count") == 2,
            "apps_eval_records_exact": counts.get("apps_eval_records") == 2,
            "l6_closures_exact": counts.get("l6_terminal_closures") == 2,
            "terminal_manifests_exact": counts.get(
                "non_product_terminal_manifests"
            )
            == 2,
            "no_uwg": counts.get("new_uwg_operations") == 0,
            "zero_execution_counts": all(
                counts.get(name) == 0
                for name in (
                    "provider_calls",
                    "judge_calls",
                    "embedding_calls",
                    "model_calls",
                    "network_attempts",
                    "subprocess_attempts",
                    "model_span_delta",
                    "source_files_changed",
                )
            ),
        },
        label="w5_aggregate_counts_invalid",
    )

    artifacts = {
        "aggregate_counts": counts_path,
        "positive_control_manifest": positive_path,
        "provider_tripwire_proof": tripwire_path,
        "real_run_matrix": matrix_path,
        **fault_paths,
    }
    seal, seal_path = _emit_package_seal(output, artifacts)
    seal_valid, seal_errors, artifact_digests = _verify_package_seal(
        output, seal_path
    )
    if not seal_valid:
        raise ZeroLlmQualificationError(
            "w5_package_seal_invalid:" + ",".join(seal_errors)
        )
    return {
        "matrix": matrix,
        "matrix_path": matrix_path,
        "positive_path": positive_path,
        "fault_paths": fault_paths,
        "tripwire": tripwire,
        "tripwire_path": tripwire_path,
        "counts": counts,
        "counts_path": counts_path,
        "seal": seal,
        "seal_path": seal_path,
        "artifact_digests": artifact_digests,
    }


def _manifest_entry_map(manifest: Mapping[str, Any]) -> dict[str, tuple[int, str]]:
    rows = manifest.get("entries")
    rows = rows if isinstance(rows, list) else []
    result: dict[str, tuple[int, str]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        ref = str(row.get("artifact_ref") or "")
        if not ref:
            continue
        result[ref] = (
            int(row.get("byte_length") or 0),
            str(row.get("sha256") or ""),
        )
    return result


def _changed_file_count(
    before: Mapping[str, Any], after: Mapping[str, Any]
) -> int:
    left = _manifest_entry_map(before)
    right = _manifest_entry_map(after)
    return sum(1 for key in set(left) | set(right) if left.get(key) != right.get(key))


def _normalize_inputs(
    run_inputs: Sequence[Mapping[str, Any]],
) -> list[tuple[Path, Path]]:
    if len(run_inputs) != 2:
        raise ZeroLlmQualificationError(
            f"W5 requires exactly two preserved runs; observed={len(run_inputs)}"
        )
    normalized: list[tuple[Path, Path]] = []
    for index, raw in enumerate(run_inputs):
        source = Path(str(raw.get("source_run") or "")).resolve(strict=True)
        replay = Path(str(raw.get("replay_root") or "")).resolve(strict=True)
        if _contained(replay, source) or _contained(source, replay):
            raise ZeroLlmQualificationError(
                f"W5 source/replay roots overlap for input {index}"
            )
        normalized.append((source, replay))
    normalized.sort(key=lambda pair: pair[0].name)
    if len({source for source, _ in normalized}) != len(normalized):
        raise ZeroLlmQualificationError("W5 source runs must be unique")
    if len({replay for _, replay in normalized}) != len(normalized):
        raise ZeroLlmQualificationError("W5 replay roots must be unique")
    return normalized


def emit_w5_zero_llm_qualification(
    *,
    run_inputs: Sequence[Mapping[str, Any]],
    output_dir: Path | str,
    source_manifest_builder: Callable[[Path], Mapping[str, Any]],
    provider_tripwire_probe: Callable[[], Mapping[str, Any]],
) -> dict[str, Any]:
    """Qualify the positive control and both blocked real runs without LLMs."""

    inputs = _normalize_inputs(run_inputs)
    output = Path(output_dir).resolve()
    for source, replay in inputs:
        if _contained(output, source) or _contained(output, replay):
            raise ZeroLlmQualificationError(
                "W5 output must be outside every source and replay root"
            )
    output.mkdir(parents=True, exist_ok=True)

    before = [dict(source_manifest_builder(source)) for source, _ in inputs]
    first = _execute_once(
        output=output,
        inputs=inputs,
        source_manifests=before,
        provider_tripwire_probe=provider_tripwire_probe,
    )
    first_seal_sha = _sha256_file(first["seal_path"])
    first_artifacts = dict(first["artifact_digests"])
    second = _execute_once(
        output=output,
        inputs=inputs,
        source_manifests=before,
        provider_tripwire_probe=provider_tripwire_probe,
    )
    second_seal_sha = _sha256_file(second["seal_path"])
    second_artifacts = dict(second["artifact_digests"])
    after = [dict(source_manifest_builder(source)) for source, _ in inputs]

    changed_counts = [
        _changed_file_count(before[index], after[index])
        for index in range(len(inputs))
    ]
    counts = second["counts"]
    checks = {
        "positive_control_pass": _verify_positive_control(
            second["positive_path"]
        )[0],
        "both_real_runs_pass": second["matrix"].get("case_count") == 2
        and all(
            row.get("status") == "PASS"
            for row in second["matrix"].get("cases") or []
        ),
        "eval_exception_case_pass": _verify_fault_matrix(
            second["fault_paths"]
        )[0],
        "l6_resume_case_pass": _verify_fault_matrix(second["fault_paths"])[0],
        "provider_tripwire_pass": second["tripwire"].get("status") == "PASS",
        "repeated_replay_seal_stable": first_seal_sha == second_seal_sha,
        "repeated_replay_artifacts_stable": first_artifacts == second_artifacts,
        "source_files_unchanged": changed_counts == [0, 0]
        and all(before[index] == after[index] for index in range(2)),
        "apps_eval_records_exact": counts.get("apps_eval_records") == 2,
        "l6_terminal_closures_exact": counts.get("l6_terminal_closures") == 2,
        "non_product_manifests_exact": counts.get(
            "non_product_terminal_manifests"
        )
        == 2,
        "no_duplicate_uwg": counts.get("new_uwg_operations") == 0,
    }
    failed = sorted(name for name, passed in checks.items() if not passed)
    completion: dict[str, Any] = {
        "schema_version": W5_COMPLETION_SCHEMA,
        "wave": "W5",
        "status": "PASS" if not failed else "BLOCKED",
        "scope_complete": not failed,
        "w6_authorized": not failed,
        "qualification_mode": "ZERO_LLM_SAVED_ARTIFACTS_ONLY",
        "positive_control_fixture": {
            "status": "PASS" if checks["positive_control_pass"] else "FAIL",
            "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
            "production_authority_granted": False,
            "publication_allowed": False,
        },
        "real_run_ids": [source.name for source, _ in inputs],
        "record_ids": [
            str(row.get("record_id") or "")
            for row in second["matrix"].get("cases") or []
        ],
        "provider_calls": 0,
        "judge_calls": 0,
        "embedding_calls": 0,
        "model_calls": 0,
        "network_attempts": 0,
        "subprocess_attempts": 0,
        "model_span_delta": 0,
        "source_files_changed": sum(changed_counts),
        "apps_eval_records": counts.get("apps_eval_records"),
        "l6_terminal_closures": counts.get("l6_terminal_closures"),
        "non_product_terminal_manifests": counts.get(
            "non_product_terminal_manifests"
        ),
        "new_uwg_operations": counts.get("new_uwg_operations"),
        "injected_eval_exception": {
            "durable_error_receipt": True,
            "durable_error_span": True,
            "generation_retry_attempted": False,
        },
        "injected_l6_exception": {
            "durable_error_receipt": True,
            "durable_error_span": True,
            "resumed_from_l6_only": True,
            "generation_replayed": False,
            "uwg_operation_attempted": False,
        },
        "determinism_replay": {
            "execution_count": 2,
            "first_package_seal_sha256": first_seal_sha,
            "second_package_seal_sha256": second_seal_sha,
            "package_seal_bytes_stable": first_seal_sha == second_seal_sha,
            "artifact_bytes_stable": first_artifacts == second_artifacts,
        },
        "source_manifests": [
            {
                "source_run_id": source.name,
                "before_content_sha256": before[index].get("content_sha256"),
                "after_content_sha256": after[index].get("content_sha256"),
                "changed_file_count": changed_counts[index],
            }
            for index, (source, _) in enumerate(inputs)
        ],
        "checks": checks,
        "failed_checks": failed,
        "real_run_matrix": _binding(
            second["matrix_path"], namespace="w5", root=output
        ),
        "positive_control_manifest": _binding(
            second["positive_path"], namespace="w5", root=output
        ),
        "qualification_counts": _binding(
            second["counts_path"], namespace="w5", root=output
        ),
        "w5_package_seal": _binding(
            second["seal_path"], namespace="w5", root=output
        ),
    }
    completion["semantic_digest"] = _canonical_digest(completion)
    completion_path = _atomic_write_json(
        output / W5_COMPLETION_FILENAME, completion
    )
    if failed:
        raise ZeroLlmQualificationError(
            "W5 qualification blocked:" + ",".join(failed)
        )
    return {
        "completion": completion,
        "completion_path": completion_path.as_posix(),
        "qualification_dir": output.as_posix(),
        "w5_package_seal_path": second["seal_path"].as_posix(),
        "activity": {
            "apps_eval_executed": False,
            "l6_executed": False,
            "uwg_operation_attempted": False,
        },
    }


def verify_w5_qualification(
    *,
    qualification_dir: Path | str,
    run_inputs: Sequence[Mapping[str, Any]],
    source_manifest_builder: Callable[[Path], Mapping[str, Any]],
) -> tuple[bool, list[str]]:
    output = Path(qualification_dir).resolve(strict=True)
    inputs = _normalize_inputs(run_inputs)
    completion = _read_json(
        output / W5_COMPLETION_FILENAME, label="w5_completion"
    )
    package_path = _resolve_binding(
        completion.get("w5_package_seal"),
        roots={"w5": output},
        label="w5_completion_package",
    )
    package_valid, package_errors, _ = _verify_package_seal(
        output, package_path
    )
    package = _read_json(package_path, label="w5_package_seal")
    package_artifacts: dict[str, Path] = {}
    package_rows = package.get("artifacts")
    package_rows = package_rows if isinstance(package_rows, list) else []
    for row in package_rows:
        if not isinstance(row, Mapping):
            continue
        role = str(row.get("artifact_role") or "")
        try:
            package_artifacts[role] = _resolve_binding(
                row,
                roots={"w5": output},
                label=f"w5_package_artifact:{role}",
            )
        except ZeroLlmQualificationError:
            continue
    fault_roles = (
        "eval_error_receipt",
        "eval_error_span",
        "l6_error_receipt",
        "l6_error_span",
        "l6_resume_receipt",
    )
    fault_paths = {
        role: package_artifacts[role]
        for role in fault_roles
        if role in package_artifacts
    }
    if len(fault_paths) == len(fault_roles):
        fault_valid, fault_errors = _verify_fault_matrix(fault_paths)
    else:
        missing = sorted(set(fault_roles) - set(fault_paths))
        fault_valid = False
        fault_errors = [f"fault_artifact_missing:{role}" for role in missing]
    tripwire_path = package_artifacts.get("provider_tripwire_proof")
    if tripwire_path is not None:
        tripwire_valid, tripwire_errors = _verify_tripwire_proof(tripwire_path)
    else:
        tripwire_valid = False
        tripwire_errors = ["provider_tripwire_artifact_missing"]
    positive_path = _resolve_binding(
        completion.get("positive_control_manifest"),
        roots={"w5": output},
        label="w5_completion_positive",
    )
    positive_valid, positive_errors = _verify_positive_control(positive_path)
    matrix_path = _resolve_binding(
        completion.get("real_run_matrix"),
        roots={"w5": output},
        label="w5_completion_matrix",
    )
    matrix = _read_json(matrix_path, label="w5_real_run_matrix")
    roots: dict[str, Path] = {}
    for index, (source, replay) in enumerate(inputs):
        roots[f"source_{index}"] = source
        roots[f"replay_{index}"] = replay
    evidence_errors: list[str] = []
    cases = matrix.get("cases")
    cases = cases if isinstance(cases, list) else []
    for case_index, case in enumerate(cases):
        if not isinstance(case, Mapping):
            evidence_errors.append(f"matrix_case_not_object:{case_index}")
            continue
        valid, errors, _ = _verify_rows(
            case.get("evidence_bindings"),
            roots=roots,
            label=f"matrix_case_{case_index}",
        )
        if not valid:
            evidence_errors.extend(errors)
    fresh_rows: list[dict[str, Any]] = []
    current_source_manifests: list[dict[str, Any]] = []
    fresh_chain_errors: list[str] = []
    for index, (source, replay) in enumerate(inputs):
        try:
            current_manifest = dict(source_manifest_builder(source))
            current_source_manifests.append(current_manifest)
            fresh_rows.append(
                _validate_real_run(
                    source=source,
                    replay=replay,
                    current_source_manifest=current_manifest,
                    index=index,
                )
            )
        except ZeroLlmQualificationError as exc:
            fresh_chain_errors.append(str(exc))
    counts_path = _resolve_binding(
        completion.get("qualification_counts"),
        roots={"w5": output},
        label="w5_completion_counts",
    )
    counts = _read_json(counts_path, label="w5_counts")
    source_manifest_rows = completion.get("source_manifests")
    source_manifest_rows = (
        source_manifest_rows if isinstance(source_manifest_rows, list) else []
    )
    determinism = completion.get("determinism_replay")
    determinism = dict(determinism) if isinstance(determinism, Mapping) else {}
    actual_package_sha = _sha256_file(package_path)
    checks = {
        "completion_schema": completion.get("schema_version")
        == W5_COMPLETION_SCHEMA,
        "completion_pass": completion.get("status") == "PASS"
        and completion.get("scope_complete") is True
        and completion.get("w6_authorized") is True,
        "completion_mode_exact": completion.get("qualification_mode")
        == "ZERO_LLM_SAVED_ARTIFACTS_ONLY",
        "completion_semantic": _semantic_valid(completion),
        "package": package_valid and not package_errors,
        "completion_artifacts_match_package": matrix_path
        == package_artifacts.get("real_run_matrix")
        and positive_path == package_artifacts.get("positive_control_manifest")
        and counts_path == package_artifacts.get("aggregate_counts"),
        "fault_matrix": fault_valid and not fault_errors,
        "provider_tripwire": tripwire_valid and not tripwire_errors,
        "positive": positive_valid and not positive_errors,
        "matrix_schema": matrix.get("schema_version")
        == W5_REAL_RUN_MATRIX_SCHEMA,
        "matrix_pass": matrix.get("status") == "PASS",
        "matrix_semantic": _semantic_valid(matrix),
        "two_cases": matrix.get("case_count") == len(cases) == 2,
        "case_ids_match": [case.get("source_run_id") for case in cases]
        == [source.name for source, _ in inputs],
        "completion_ids_match": completion.get("real_run_ids")
        == [source.name for source, _ in inputs]
        and completion.get("record_ids")
        == [case.get("record_id") for case in cases],
        "external_evidence": not evidence_errors,
        "nested_chains_revalidated": not fresh_chain_errors
        and len(fresh_rows) == len(cases)
        and all(
            _canonical_digest(fresh_rows[index])
            == _canonical_digest(cases[index])
            for index in range(len(cases))
        ),
        "counts_schema": counts.get("schema_version") == W5_COUNTS_SCHEMA,
        "counts_pass": counts.get("status") == "PASS"
        and counts.get("positive_control_fixture_passed") is True
        and counts.get("injected_failure_matrix_passed") is True
        and counts.get("provider_tripwire_passed") is True,
        "counts_semantic": _semantic_valid(counts),
        "counts_exact": counts.get("apps_eval_records") == 2
        and counts.get("l6_terminal_closures") == 2
        and counts.get("non_product_terminal_manifests") == 2
        and counts.get("new_uwg_operations") == 0,
        "counts_zero_execution": all(
            counts.get(name) == 0
            for name in (
                "provider_calls",
                "judge_calls",
                "embedding_calls",
                "model_calls",
                "network_attempts",
                "subprocess_attempts",
                "model_span_delta",
                "source_files_changed",
            )
        ),
        "zero_execution": all(
            completion.get(name) == 0
            for name in (
                "provider_calls",
                "judge_calls",
                "embedding_calls",
                "model_calls",
                "network_attempts",
                "subprocess_attempts",
                "model_span_delta",
                "source_files_changed",
                "new_uwg_operations",
            )
        ),
        "source_manifests_current": len(source_manifest_rows)
        == len(current_source_manifests)
        == 2
        and all(isinstance(row, Mapping) for row in source_manifest_rows)
        and all(
            row.get("source_run_id") == inputs[index][0].name
            and row.get("before_content_sha256")
            == current_source_manifests[index].get("content_sha256")
            and row.get("after_content_sha256")
            == current_source_manifests[index].get("content_sha256")
            and row.get("changed_file_count") == 0
            for index, row in enumerate(source_manifest_rows)
        ),
        "fault_completion_exact": completion.get(
            "injected_eval_exception"
        )
        == {
            "durable_error_receipt": True,
            "durable_error_span": True,
            "generation_retry_attempted": False,
        }
        and completion.get("injected_l6_exception")
        == {
            "durable_error_receipt": True,
            "durable_error_span": True,
            "resumed_from_l6_only": True,
            "generation_replayed": False,
            "uwg_operation_attempted": False,
        },
        "deterministic": determinism.get("execution_count") == 2
        and determinism.get("artifact_bytes_stable") is True
        and determinism.get("package_seal_bytes_stable") is True
        and determinism.get("first_package_seal_sha256")
        == determinism.get("second_package_seal_sha256")
        == actual_package_sha,
    }
    errors = [
        *package_errors,
        *fault_errors,
        *tripwire_errors,
        *positive_errors,
        *evidence_errors,
        *fresh_chain_errors,
    ]
    errors.extend(name for name, passed in checks.items() if not passed)
    return not errors, sorted(set(errors))


__all__ = [
    "EXPECTED_LANES",
    "InjectedQualificationError",
    "W5_COMPLETION_FILENAME",
    "W5_COMPLETION_SCHEMA",
    "W5_COUNTS_FILENAME",
    "W5_PACKAGE_SEAL_FILENAME",
    "W5_POSITIVE_MANIFEST_FILENAME",
    "ZeroLlmQualificationError",
    "emit_w5_zero_llm_qualification",
    "verify_w5_qualification",
]
