"""Deterministic W2 Apps Eval replay over immutable historical run artifacts.

The module is stdlib-only at import time so the caller can install the
zero-provider guard before importing Apps Eval.  W2 consumes the additive W1
authority correction, emits a sealed deterministic FAIL record, and stops at
the L6 handoff boundary.  Independent L6 shadow execution belongs to W3.
"""

from __future__ import annotations

import hashlib
import json
import os
import uuid
from dataclasses import replace
from pathlib import Path
from typing import Any, Mapping


W2_COMPLETION_SCHEMA = "apps_rg.apps_eval_replay_completion.v1"
W2_COMPLETION_FILENAME = "w2_completion_receipt.json"

W1_RECONCILIATION_FILENAME = "w1_authoritative_reconciliation.json"
W1_CORRECTION_FILENAME = "w1_authorization_correction_receipt.json"
W1_COMPLETION_FILENAME = "w1_completion_receipt.json"
W1_GUARD_FILENAME = "w1_zero_provider_guard_receipt.json"

MANDATORY_RUN_OUTPUT = "APPS_RG_MANDATORY_RUN_OUTPUT.json"


class AppsEvalReplayError(RuntimeError):
    """Raised when W1 authority or W2 deterministic evidence is invalid."""


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


def _read_json(path: Path, *, label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise AppsEvalReplayError(f"{label}_unreadable:{path}") from exc
    if not isinstance(payload, dict):
        raise AppsEvalReplayError(f"{label}_not_object:{path}")
    return payload


def _semantic_digest_valid(payload: Mapping[str, Any]) -> bool:
    body = dict(payload)
    observed = str(body.pop("semantic_digest", "") or "")
    return bool(observed) and observed == _canonical_digest(body)


def _failed_checks(checks: Mapping[str, bool]) -> list[str]:
    return sorted(name for name, passed in checks.items() if not passed)


def _file_binding(path: Path, *, relative_to: Path) -> dict[str, Any]:
    target = path.resolve(strict=True)
    root = relative_to.resolve()
    try:
        artifact_ref = target.relative_to(root).as_posix()
    except ValueError:
        artifact_ref = target.as_posix()
    return {
        "artifact_ref": artifact_ref,
        "byte_length": target.stat().st_size,
        "sha256": _sha256_file(target),
    }


def _source_binding_valid(source: Path, binding: Any) -> bool:
    if not isinstance(binding, Mapping):
        return False
    ref = str(binding.get("artifact_ref") or "").strip()
    if not ref:
        return False
    candidate = (source / ref).resolve()
    try:
        candidate.relative_to(source)
    except ValueError:
        return False
    return bool(
        candidate.is_file()
        and binding.get("byte_length") == candidate.stat().st_size
        and binding.get("sha256") == _sha256_file(candidate)
    )


def _validate_w1_authority(
    *,
    source: Path,
    output_dir: Path,
) -> dict[str, Any]:
    w1_dir = output_dir.parent / "w1"
    paths = {
        "reconciliation": w1_dir / W1_RECONCILIATION_FILENAME,
        "correction": w1_dir / W1_CORRECTION_FILENAME,
        "completion": w1_dir / W1_COMPLETION_FILENAME,
        "guard": w1_dir / W1_GUARD_FILENAME,
    }
    docs = {
        name: _read_json(path, label=f"w1_{name}")
        for name, path in paths.items()
    }
    reconciliation = docs["reconciliation"]
    correction = docs["correction"]
    completion = docs["completion"]
    guard = docs["guard"]
    guard_counters = guard.get("attempt_counters")
    guard_counters = (
        dict(guard_counters) if isinstance(guard_counters, Mapping) else {}
    )
    checks = {
        "reconciliation_schema_exact": reconciliation.get("schema_version")
        == "apps_rg.authority_reconciliation.v1",
        "reconciliation_digest_valid": _semantic_digest_valid(reconciliation),
        "reconciliation_source_bound": reconciliation.get("source_run_id")
        == source.name,
        "reconciliation_product_denied": reconciliation.get("product_authorized")
        is False
        and reconciliation.get("publish_allowed") is False,
        "reconciliation_entry_pass": (
            isinstance(reconciliation.get("entry_authority"), Mapping)
            and reconciliation["entry_authority"].get("status") == "PASS"
        ),
        "reconciliation_lanes_blocked": int(
            reconciliation.get("blocked_lane_count") or 0
        )
        > 0
        and int(reconciliation.get("authorized_lane_count") or 0) == 0,
        "correction_schema_exact": correction.get("schema_version")
        == "apps_rg.authorization_correction.v1",
        "correction_digest_valid": _semantic_digest_valid(correction),
        "correction_source_bound": correction.get("source_run_id") == source.name,
        "correction_pass": correction.get("status") == "PASS",
        "correction_supersedes_invalid_authority": correction.get(
            "correction_disposition"
        )
        == "SUPERSEDED_INVALID_AUTHORITY"
        and correction.get("corrected_product_authorized") is False
        and correction.get("corrected_publish_allowed") is False,
        "correction_preserves_source": correction.get("source_artifacts_mutated")
        is False
        and correction.get("candidate_artifacts_preserved") is True,
        "correction_no_eval_l6_or_uwg": correction.get("apps_eval_executed")
        is False
        and correction.get("l6_executed") is False
        and correction.get("new_uwg_operation_attempted") is False,
        "correction_reconciliation_bound": correction.get(
            "reconciliation_semantic_digest"
        )
        == reconciliation.get("semantic_digest"),
        "correction_original_authorization_bound": _source_binding_valid(
            source,
            correction.get("original_authorization"),
        ),
        "completion_schema_exact": completion.get("schema_version")
        == "apps_rg.authority_reconciliation_completion.v1",
        "completion_digest_valid": _semantic_digest_valid(completion),
        "completion_source_bound": completion.get("source_run_id") == source.name,
        "completion_authorizes_w2": completion.get("status") == "PASS"
        and completion.get("scope_complete") is True
        and completion.get("w2_authorized") is True,
        "completion_product_denied": completion.get("product_authorized") is False
        and completion.get("pipeline_complete") is False,
        "completion_refs_exact": completion.get("reconciliation_ref")
        == W1_RECONCILIATION_FILENAME
        and completion.get("correction_ref") == W1_CORRECTION_FILENAME,
        "guard_schema_exact": guard.get("schema_version")
        == "apps_rg.post_runtime_zero_provider_replay.v1",
        "guard_digest_valid": _semantic_digest_valid(guard),
        "guard_source_bound": guard.get("source_run_id") == source.name,
        "guard_pass": guard.get("status") == "PASS"
        and guard.get("source_unchanged") is True,
        "guard_binds_completion": guard.get(
            "operation_completion_semantic_digest"
        )
        == completion.get("semantic_digest"),
        "guard_zero_attempts": bool(guard_counters)
        and all(int(value or 0) == 0 for value in guard_counters.values()),
        "guard_no_eval_l6_or_uwg": guard.get("apps_eval_executed") is False
        and guard.get("l6_executed") is False
        and guard.get("uwg_operation_attempted") is False,
    }
    failures = _failed_checks(checks)
    if failures:
        raise AppsEvalReplayError("w1_authority_invalid:" + ",".join(failures))
    return {
        "checks": checks,
        "paths": paths,
        "reconciliation": reconciliation,
        "correction": correction,
        "completion": completion,
        "guard": guard,
    }


def _historical_result_summary(source: Path) -> dict[str, Any]:
    path = source / MANDATORY_RUN_OUTPUT
    if not path.is_file():
        return {}
    payload = _read_json(path, label="mandatory_run_output")
    result = payload.get("result_summary")
    return dict(result) if isinstance(result, Mapping) else {}


def _atomic_write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex[:12]}.tmp")
    temporary.write_text(
        json.dumps(dict(payload), ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def emit_w2_apps_eval_replay(
    *,
    source_run: Path | str,
    output_dir: Path | str,
) -> dict[str, Any]:
    """Emit one complete deterministic Apps Eval verdict without L6 execution."""

    source = Path(source_run).resolve(strict=True)
    output = Path(output_dir).resolve()
    try:
        output.relative_to(source)
    except ValueError:
        pass
    else:
        raise AppsEvalReplayError("W2 output cannot be inside source run")

    w1 = _validate_w1_authority(source=source, output_dir=output)

    # Imports occur only after the caller has installed ZeroProviderReplayGuard.
    from apps_eval.adapters.apps_rg import (  # noqa: PLC0415
        normalize_existing_apps_rg_run_snapshot,
    )
    from apps_eval.runner.core import (  # noqa: PLC0415
        run_current_snapshot_eval,
        verify_apps_rg_eval_package_seal,
    )

    snapshot = normalize_existing_apps_rg_run_snapshot(
        scenario_id=f"post-runtime-{source.name}",
        result=_historical_result_summary(source),
        artifact_dir=source,
    )
    correction = w1["correction"]
    reconciliation = w1["reconciliation"]
    provenance = dict(snapshot.provenance)
    provenance.update(
        {
            "source_seal_verified": False,
            "source_seal_verification_errors": sorted(
                {
                    *list(
                        provenance.get("source_seal_verification_errors") or []
                    ),
                    "w1_authorization_superseded_invalid_authority",
                    *[
                        "w1:" + str(reason)
                        for reason in reconciliation.get("failure_reasons", [])
                    ],
                }
            ),
            "product_authorized": False,
            "product_authorization_correction_ref": w1["paths"][
                "correction"
            ].as_posix(),
            "product_authorization_correction_digest": correction[
                "semantic_digest"
            ],
            "product_authorization_correction_disposition": correction[
                "correction_disposition"
            ],
            "w1_reconciliation_ref": w1["paths"][
                "reconciliation"
            ].as_posix(),
            "w1_reconciliation_digest": reconciliation["semantic_digest"],
        }
    )
    snapshot = replace(snapshot, provenance=provenance)

    def _evaluate() -> Any:
        return run_current_snapshot_eval(
            snapshot,
            out_dir=str(output / "apps_eval"),
            deterministic_only=True,
            emit_l6_handoff=True,
            emit_l6_shadow_bridge=False,
            git_commit_override="",
            platform_override="post-runtime-zero-provider",
        )

    first_record = _evaluate()
    first_eval_record_path = Path(first_record.artifact_paths["eval_record"])
    first_eval_record_sha256 = _sha256_file(first_eval_record_path)
    first_seal_valid, first_seal_errors = verify_apps_rg_eval_package_seal(
        first_eval_record_path.parent
    )
    record = _evaluate()
    eval_record_path = Path(record.artifact_paths["eval_record"])
    eval_run_dir = eval_record_path.parent
    seal_valid, seal_errors = verify_apps_rg_eval_package_seal(eval_run_dir)
    persisted_record = _read_json(eval_record_path, label="eval_record")
    scorecard_rows_path = Path(record.artifact_paths["scorecard_rows"])
    try:
        scorecard_rows = [
            json.loads(line)
            for line in scorecard_rows_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise AppsEvalReplayError("scorecard_rows_unreadable") from exc
    admission_rows = [
        row
        for row in scorecard_rows
        if isinstance(row, Mapping)
        and row.get("component_id") == "apps_rg.eval_admission"
    ]
    admission_failure_modes = sorted(
        str(row.get("failure_mode") or "")
        for row in admission_rows
        if row.get("verdict") == "FAIL"
    )
    saved_judge_rows = [
        row
        for row in scorecard_rows
        if isinstance(row, Mapping)
        and row.get("artifact_role") == "lane_x1d_llm_judge_outputs"
        and str(row.get("artifact_ref") or "").strip()
    ]
    l6_handoff_path = Path(record.artifact_paths["l6_handoff"])
    eval_seal_path = Path(record.artifact_paths["eval_package_seal"])
    coverage_path = Path(record.artifact_paths["coverage_matrix"])
    component_path = Path(record.artifact_paths["apps_rg_component_scorecard"])

    checks = {
        "w1_authority_validated": all(w1["checks"].values()),
        "eval_execution_complete": record.eval_execution_complete is True
        and persisted_record.get("eval_execution_complete") is True,
        "eval_verdict_fail": record.eval_verdict == "fail"
        and record.scorecard.verdict == "fail"
        and persisted_record.get("eval_verdict") == "fail",
        "release_blocked": record.release_blocked is True
        and record.scorecard.coverage_summary.get("release_blocked") is True
        and persisted_record.get("release_blocked") is True,
        "admission_failed_without_abort": record.admission_status == "FAIL"
        and persisted_record.get("admission_status") == "FAIL",
        "preflight_unverifiable_key_material_recorded": record.preflight_verification_status
        == "UNVERIFIABLE_KEY_MATERIAL"
        and "admission.preflight_unverifiable_key_material"
        in admission_failure_modes,
        "invalid_product_authority_recorded": "admission.product_authority_invalid"
        in admission_failure_modes,
        "complete_identity_row_emitted": any(
            row.get("microstep_id") == "admission.source_identity"
            for row in admission_rows
        ),
        "deterministic_only": record.deterministic_only is True
        and record.record_seed.get("with_judge") is False,
        "repeated_replay_record_id_stable": first_record.record_id
        == record.record_id,
        "repeated_replay_record_bytes_stable": first_eval_record_sha256
        == _sha256_file(eval_record_path),
        "first_replay_package_sealed": first_seal_valid
        and not first_seal_errors,
        "saved_judge_artifacts_inspected": bool(saved_judge_rows),
        "scorecard_rows_sealed": scorecard_rows_path.is_file()
        and scorecard_rows_path.stat().st_size > 0,
        "component_scorecard_sealed": component_path.is_file()
        and component_path.stat().st_size > 0,
        "coverage_matrix_sealed": coverage_path.is_file()
        and coverage_path.stat().st_size > 0,
        "eval_record_sealed": eval_seal_path.is_file()
        and seal_valid
        and not seal_errors,
        "l6_handoff_emitted": l6_handoff_path.is_file(),
        "l6_shadow_bridge_not_executed": "l6_shadow_bridge"
        not in record.artifact_paths
        and not (eval_run_dir / "l6_shadow_bridge.json").exists(),
    }
    failures = _failed_checks(checks)
    completion: dict[str, Any] = {
        "schema_version": W2_COMPLETION_SCHEMA,
        "wave": "W2",
        "status": "PASS" if not failures else "BLOCKED",
        "scope_complete": not failures,
        "w3_authorized": not failures,
        "source_run_id": source.name,
        "eval_execution_complete": record.eval_execution_complete,
        "eval_verdict": record.eval_verdict,
        "release_blocked": record.release_blocked,
        "product_authorized": False,
        "pipeline_complete": False,
        "deterministic_only": record.deterministic_only,
        "with_judge": False,
        "preflight_verification_status": record.preflight_verification_status,
        "admission_status": record.admission_status,
        "admission_failures": list(record.admission_failures),
        "admission_failure_modes": admission_failure_modes,
        "record_id": record.record_id,
        "record_seed_digest": record.run_metadata.record_seed_digest,
        "determinism_replay": {
            "execution_count": 2,
            "first_record_id": first_record.record_id,
            "second_record_id": record.record_id,
            "record_id_stable": first_record.record_id == record.record_id,
            "first_eval_record_sha256": first_eval_record_sha256,
            "second_eval_record_sha256": _sha256_file(eval_record_path),
            "eval_record_bytes_stable": first_eval_record_sha256
            == _sha256_file(eval_record_path),
            "first_package_seal_valid": first_seal_valid
            and not first_seal_errors,
            "second_package_seal_valid": seal_valid and not seal_errors,
        },
        "saved_judge_artifact_row_count": len(saved_judge_rows),
        "saved_judge_artifact_refs": sorted(
            {str(row.get("artifact_ref") or "") for row in saved_judge_rows}
        ),
        "l6_handoff_emitted": l6_handoff_path.is_file(),
        "l6_shadow_bridge_executed": False,
        "eval_record": _file_binding(eval_record_path, relative_to=output),
        "eval_package_seal": _file_binding(eval_seal_path, relative_to=output),
        "scorecard_rows": _file_binding(scorecard_rows_path, relative_to=output),
        "component_scorecard": _file_binding(component_path, relative_to=output),
        "coverage_matrix": _file_binding(coverage_path, relative_to=output),
        "l6_handoff": _file_binding(l6_handoff_path, relative_to=output),
        "w1_completion_ref": w1["paths"]["completion"].as_posix(),
        "w1_completion_semantic_digest": w1["completion"]["semantic_digest"],
        "w1_correction_ref": w1["paths"]["correction"].as_posix(),
        "w1_correction_semantic_digest": correction["semantic_digest"],
        "checks": checks,
        "failed_checks": failures,
    }
    completion["semantic_digest"] = _canonical_digest(completion)
    _atomic_write_json(output / W2_COMPLETION_FILENAME, completion)
    return {
        "completion": completion,
        "activity": {
            "apps_eval_executed": True,
            "l6_executed": False,
            "uwg_operation_attempted": False,
        },
        "record_id": record.record_id,
        "eval_record_path": eval_record_path.as_posix(),
        "eval_package_seal_path": eval_seal_path.as_posix(),
    }


__all__ = [
    "AppsEvalReplayError",
    "W2_COMPLETION_FILENAME",
    "W2_COMPLETION_SCHEMA",
    "emit_w2_apps_eval_replay",
]
