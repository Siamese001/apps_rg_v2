"""W5 qualification acceptance without provider or model execution."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Mapping

from apps_rg.runtime import post_runtime_replay
from apps_rg.runtime import terminal_closeout_replay
from apps_rg.runtime import zero_llm_qualification as subject


REPO_ROOT = Path(__file__).resolve().parents[4]


def _canonical(value: Any) -> str:
    raw = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sha(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(path: Path, payload: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return path


def _write_semantic(path: Path, payload: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(payload)
    result["semantic_digest"] = _canonical(result)
    _write_json(path, result)
    return result


def _file_binding(path: Path, *, root: Path) -> dict[str, Any]:
    return {
        "artifact_ref": path.relative_to(root).as_posix(),
        "byte_length": path.stat().st_size,
        "sha256": _sha(path),
    }


def _seal(
    path: Path,
    *,
    schema: str,
    root: Path,
    artifacts: Mapping[str, Path],
) -> Path:
    rows = [
        {"artifact_role": role, **_file_binding(artifact, root=root)}
        for role, artifact in sorted(artifacts.items())
    ]
    body = {
        "schema_version": schema,
        "status": "PASS",
        "artifact_count": len(rows),
        "artifacts": rows,
    }
    return _write_json(path, {**body, "manifest_sha256": _canonical(body)})


def _counters() -> dict[str, int]:
    return {
        "blocked_import_attempts": 0,
        "embedding_calls": 0,
        "judge_calls": 0,
        "model_calls": 0,
        "network_attempts": 0,
        "provider_calls": 0,
        "subprocess_attempts": 0,
    }


def _guard(
    path: Path,
    *,
    wave: str,
    source_run_id: str,
    completion: Mapping[str, Any],
    apps_eval: bool,
    l6: bool,
    source_manifest_sha256: str,
) -> dict[str, Any]:
    return _write_semantic(
        path,
        {
            "schema_version": "apps_rg.post_runtime_zero_provider_replay.v1",
            "wave": wave,
            "status": "PASS",
            "scope_complete": True,
            "source_run_id": source_run_id,
            "source_manifest_sha256": source_manifest_sha256,
            "source_unchanged": True,
            "attempt_counters": _counters(),
            "clean_import_state": True,
            "apps_eval_executed": apps_eval,
            "l6_executed": l6,
            "uwg_operation_attempted": False,
            "operation_completion_status": "PASS",
            "operation_completion_semantic_digest": completion[
                "semantic_digest"
            ],
        },
    )


def _build_sealed_chain(
    root: Path, *, run_id: str, record_id: str
) -> tuple[Path, Path]:
    source = root / run_id
    replay = root / f"{run_id}-replay"
    source.mkdir(parents=True)
    replay.mkdir(parents=True)

    source_entries = []
    for sequence, stage_id in enumerate(
        terminal_closeout_replay.EXPECTED_SOURCE_STAGE_IDS
    ):
        receipt = _write_json(
            source
            / "e2e_ledger_receipts"
            / f"{sequence:04d}_{stage_id.lower()}.json",
            {
                "schema_version": f"test.{stage_id.lower()}.v1",
                "status": "PASS",
                "stage_id": stage_id,
            },
        )
        source_entries.append(
            {
                "sequence": sequence,
                "stage_id": stage_id,
                "status": "PASS",
                "authoritative_receipt_ref": receipt.relative_to(
                    source
                ).as_posix(),
                "authoritative_receipt_sha256": _sha(receipt),
            }
        )
    _write_json(
        source / "e2e_stage_ledger.json",
        {
            "schema_version": "apps_rg.e2e_stage_ledger.v2",
            "entries": source_entries,
        },
    )
    _write_json(
        source / "uwg_commit_receipt.json",
        {"schema_version": "L4-UWG-1.0.0", "commit_status": "COMMITTED"},
    )
    _write_json(
        source / "apps_rg_product_authorization_receipt.json",
        {
            "schema_version": "apps_rg.product_authorization_receipt.v1",
            "authorized": True,
        },
    )
    source_digest = post_runtime_replay.build_source_manifest(source)[
        "content_sha256"
    ]

    _write_semantic(
        replay / "w0_zero_provider_preflight_receipt.json",
        {
            "schema_version": "apps_rg.post_runtime_zero_provider_preflight.v1",
            "wave": "W0",
            "status": "PASS",
            "w0_scope_complete": True,
            "source_run_id": run_id,
            "source_unchanged": True,
            "source_manifest_sha256": source_digest,
            "attempt_counters": _counters(),
            "clean_import_state": True,
        },
    )

    w1_dir = replay / "w1"
    _write_semantic(
        w1_dir / "w1_authoritative_reconciliation.json",
        {
            "schema_version": "apps_rg.authority_reconciliation.v1",
            "status": "BLOCKED",
            "source_run_id": run_id,
            "product_authorized": False,
            "publish_allowed": False,
            "authorized_lane_count": 0,
            "blocked_lane_count": len(subject.EXPECTED_LANES),
            "authoritative_x3_codes": {
                lane: "X3A_DENY_REROUTE" for lane in subject.EXPECTED_LANES
            },
        },
    )
    _write_semantic(
        w1_dir / "w1_authorization_correction_receipt.json",
        {
            "schema_version": "apps_rg.authorization_correction.v1",
            "status": "PASS",
            "source_run_id": run_id,
            "corrected_product_authorized": False,
            "corrected_pipeline_complete": False,
            "correction_disposition": "SUPERSEDED_INVALID_AUTHORITY",
            "original_authorized_claim": True,
        },
    )
    _write_semantic(
        w1_dir / "w1_l0_parallel_replay_proof.json",
        {
            "schema_version": "apps_rg.l0_parallel_artifact_replay.v1",
            "status": "PASS",
            "parallel_overlap_proven": True,
            "provider_or_model_execution": False,
        },
    )
    w1_completion = _write_semantic(
        w1_dir / "w1_completion_receipt.json",
        {
            "schema_version": "apps_rg.authority_reconciliation_completion.v1",
            "wave": "W1",
            "status": "PASS",
            "scope_complete": True,
            "source_run_id": run_id,
            "product_authorized": False,
            "pipeline_complete": False,
        },
    )
    _guard(
        w1_dir / "w1_zero_provider_guard_receipt.json",
        wave="W1",
        source_run_id=run_id,
        completion=w1_completion,
        apps_eval=False,
        l6=False,
        source_manifest_sha256=source_digest,
    )

    w2_dir = replay / "w2"
    eval_dir = w2_dir / "apps_eval" / "record"
    eval_record = _write_json(
        eval_dir / "eval_record.json",
        {
            "schema_version": "apps_eval.completed_eval_record.v1",
            "record_id": record_id,
            "created_at": "1970-01-01T00:00:00Z",
            "eval_execution_complete": True,
            "eval_verdict": "fail",
            "release_blocked": True,
        },
    )
    eval_artifacts = {
        "eval_record": eval_record,
        "scorecard_rows": _write_json(
            eval_dir / "scorecard_rows.json", {"rows": []}
        ),
        "component_scorecards": _write_json(
            eval_dir / "component_scorecards.json", {"components": []}
        ),
        "coverage_matrix": _write_json(
            eval_dir / "coverage_matrix.json", {"coverage": []}
        ),
        "regression_summary": _write_json(
            eval_dir / "regression_summary.json", {"regressions": []}
        ),
    }
    eval_seal = _seal(
        eval_dir / "apps_rg_eval_package_seal.json",
        schema="apps_eval.apps_rg_eval_package_seal.v1",
        root=eval_dir,
        artifacts=eval_artifacts,
    )
    w2_completion = _write_semantic(
        w2_dir / "w2_completion_receipt.json",
        {
            "schema_version": "apps_rg.apps_eval_replay_completion.v1",
            "wave": "W2",
            "status": "PASS",
            "scope_complete": True,
            "source_run_id": run_id,
            "record_id": record_id,
            "product_authorized": False,
            "pipeline_complete": False,
            "eval_execution_complete": True,
            "eval_verdict": "fail",
            "release_blocked": True,
            "w3_authorized": True,
            "admission_status": "FAIL",
            "admission_failure_modes": [
                "admission.product_authority_invalid"
            ],
            "eval_record": _file_binding(eval_record, root=w2_dir),
            "eval_package_seal": _file_binding(eval_seal, root=w2_dir),
        },
    )
    _guard(
        w2_dir / "w2_zero_provider_guard_receipt.json",
        wave="W2",
        source_run_id=run_id,
        completion=w2_completion,
        apps_eval=True,
        l6=False,
        source_manifest_sha256=source_digest,
    )

    w3_dir = replay / "w3"
    bindings = []
    for lane in subject.EXPECTED_LANES:
        row = {
            "section_id": lane,
            "binding_status": "LEGACY_PACKAGE_ADVISORY",
            "evidence_class": "CONTRACT_ONLY_ADVISORY",
            "apps_eval_row_count": 10,
            "l6_observation_row_count": 0,
            "proof_gaps": [
                "governed_v40_package_required_for_independent_binding"
            ],
        }
        bindings.append(row)
        _write_json(
            w3_dir / "independent_bindings" / f"{lane}.binding.json",
            row,
        )
    bindings_path = w3_dir / "l6_section_apps_eval_bindings.json"
    _write_semantic(
        bindings_path,
        {
            "schema_version": "apps_rg.l6_section_apps_eval_bindings.v3",
            "eval_record_id": record_id,
            "bindings": bindings,
        },
    )
    closure_path = w3_dir / "l6_apps_eval_binding_closure_receipt.json"
    _write_semantic(
        closure_path,
        {
            "schema_version": (
                "apps_rg.l6_apps_eval_binding_closure_receipt.v2"
            ),
            "binding_closure_status": "FAIL",
            "apps_eval_rows_bound": False,
        },
    )
    w3_seal = _seal(
        w3_dir / "w3_l6_shadow_package_seal.json",
        schema="apps_rg.l6_shadow_replay_package_seal.v1",
        root=w3_dir,
        artifacts={
            "l6_apps_eval_binding_closure": closure_path,
            "l6_section_apps_eval_bindings": bindings_path,
        },
    )
    w3_seal_payload = json.loads(w3_seal.read_text(encoding="utf-8"))
    w3_seal_payload["record_id"] = record_id
    body = {
        key: value
        for key, value in w3_seal_payload.items()
        if key != "manifest_sha256"
    }
    w3_seal_payload["manifest_sha256"] = _canonical(body)
    _write_json(w3_seal, w3_seal_payload)
    w3_completion = _write_semantic(
        w3_dir / "w3_completion_receipt.json",
        {
            "schema_version": "apps_rg.l6_shadow_replay_completion.v1",
            "wave": "W3",
            "status": "PASS",
            "scope_complete": True,
            "source_run_id": run_id,
            "record_id": record_id,
            "product_authorized": False,
            "pipeline_complete": False,
            "l6_execution_complete": True,
            "l6_shadow_observability_verdict": "fail",
            "binding_closure_status": "FAIL",
            "release_blocked": True,
            "apps_eval_rows_bound": False,
            "w4_authorized": True,
            "section_summary": {
                "sections_total": len(subject.EXPECTED_LANES),
                "sections_bound": 0,
                "observed_lane_ids": list(subject.EXPECTED_LANES),
            },
            "w3_package_seal": _file_binding(w3_seal, root=w3_dir),
            "l6_section_apps_eval_bindings": _file_binding(
                bindings_path, root=w3_dir
            ),
            "l6_apps_eval_binding_closure": _file_binding(
                closure_path, root=w3_dir
            ),
        },
    )
    _guard(
        w3_dir / "w3_zero_provider_guard_receipt.json",
        wave="W3",
        source_run_id=run_id,
        completion=w3_completion,
        apps_eval=False,
        l6=True,
        source_manifest_sha256=source_digest,
    )

    w4_result = terminal_closeout_replay.emit_w4_terminal_closeout_replay(
        source_run=source,
        output_dir=replay / "w4",
    )
    _guard(
        replay / "w4" / "w4_zero_provider_guard_receipt.json",
        wave="W4",
        source_run_id=run_id,
        completion=w4_result["completion"],
        apps_eval=False,
        l6=False,
        source_manifest_sha256=source_digest,
    )
    return source, replay


def _tripwire_probe() -> dict[str, Any]:
    guard = post_runtime_replay.ZeroProviderReplayGuard()
    try:
        guard.block_attempt("provider", "w5.test.tripwire")
    except post_runtime_replay.ProviderExecutionBlocked as exc:
        return {
            "status": "PASS",
            "provider_attempt_blocked": True,
            "exception_type": type(exc).__name__,
            "controlled_attempt_counters": guard.counters.to_dict(),
        }
    raise AssertionError("provider tripwire did not block")


def _build_two_inputs(tmp_path: Path) -> list[dict[str, Path]]:
    cases = tmp_path / "cases"
    first = _build_sealed_chain(
        cases, run_id="e2e_fixture_a", record_id="record-a"
    )
    second = _build_sealed_chain(
        cases, run_id="e2e_fixture_b", record_id="record-b"
    )
    return [
        {"source_run": source, "replay_root": replay}
        for source, replay in (first, second)
    ]


def _emit(tmp_path: Path) -> tuple[list[dict[str, Path]], Path, dict[str, Any]]:
    run_inputs = _build_two_inputs(tmp_path)
    qualification = tmp_path / "qualification"
    result = subject.emit_w5_zero_llm_qualification(
        run_inputs=run_inputs,
        output_dir=qualification,
        source_manifest_builder=post_runtime_replay.build_source_manifest,
        provider_tripwire_probe=_tripwire_probe,
    )
    return run_inputs, qualification, result


def test_w5_qualifies_complete_matrix_with_zero_execution(tmp_path: Path) -> None:
    run_inputs, qualification, result = _emit(tmp_path)
    completion = result["completion"]

    assert completion["status"] == "PASS"
    assert completion["scope_complete"] is True
    assert completion["w6_authorized"] is True
    assert completion["provider_calls"] == 0
    assert completion["judge_calls"] == 0
    assert completion["embedding_calls"] == 0
    assert completion["network_attempts"] == 0
    assert completion["model_span_delta"] == 0
    assert completion["source_files_changed"] == 0
    assert completion["apps_eval_records"] == 2
    assert completion["l6_terminal_closures"] == 2
    assert completion["non_product_terminal_manifests"] == 2
    assert completion["new_uwg_operations"] == 0
    assert completion["determinism_replay"]["execution_count"] == 2
    assert completion["determinism_replay"]["artifact_bytes_stable"] is True
    assert completion["positive_control_fixture"] == {
        "status": "PASS",
        "fixture_class": "SYNTHETIC_SAVED_OUTPUT",
        "production_authority_granted": False,
        "publication_allowed": False,
    }

    eval_error = json.loads(
        (qualification / "fault_injection/apps_eval_error_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    l6_resume = json.loads(
        (qualification / "fault_injection/l6_resume_receipt.json").read_text(
            encoding="utf-8"
        )
    )
    assert eval_error["generation_retry_attempted"] is False
    assert eval_error["status"] == "CAPTURED"
    assert l6_resume["resume_from_stage"] == "L6_OBSERVABILITY"
    assert l6_resume["apps_eval_replayed"] is False
    assert l6_resume["generation_replayed"] is False
    assert l6_resume["uwg_operation_attempted"] is False

    valid, errors = subject.verify_w5_qualification(
        qualification_dir=qualification,
        run_inputs=run_inputs,
        source_manifest_builder=post_runtime_replay.build_source_manifest,
    )
    assert valid is True
    assert errors == []


def test_w5_verifier_reopens_nested_w4_package(tmp_path: Path) -> None:
    run_inputs, qualification, _ = _emit(tmp_path)
    ledger = run_inputs[0]["replay_root"] / "w4/terminal_stage_ledger.json"
    ledger.write_bytes(ledger.read_bytes() + b" ")

    valid, errors = subject.verify_w5_qualification(
        qualification_dir=qualification,
        run_inputs=run_inputs,
        source_manifest_builder=post_runtime_replay.build_source_manifest,
    )

    assert valid is False
    assert any(
        "w5_terminal_manifest_invalid" in error and "package_seal" in error
        for error in errors
    )
    assert "nested_chains_revalidated" in errors


def test_w5_verifier_rejects_resigned_fault_receipt(tmp_path: Path) -> None:
    run_inputs, qualification, _ = _emit(tmp_path)
    receipt_path = qualification / "fault_injection/apps_eval_error_receipt.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    receipt.pop("semantic_digest")
    receipt["generation_retry_attempted"] = True
    _write_semantic(receipt_path, receipt)

    seal_path = qualification / subject.W5_PACKAGE_SEAL_FILENAME
    seal = json.loads(seal_path.read_text(encoding="utf-8"))
    for row in seal["artifacts"]:
        if row["artifact_role"] == "eval_error_receipt":
            row["byte_length"] = receipt_path.stat().st_size
            row["sha256"] = _sha(receipt_path)
    seal_body = {
        key: value for key, value in seal.items() if key != "manifest_sha256"
    }
    seal["manifest_sha256"] = _canonical(seal_body)
    _write_json(seal_path, seal)

    completion_path = qualification / subject.W5_COMPLETION_FILENAME
    completion = json.loads(completion_path.read_text(encoding="utf-8"))
    completion.pop("semantic_digest")
    completion["w5_package_seal"]["byte_length"] = seal_path.stat().st_size
    completion["w5_package_seal"]["sha256"] = _sha(seal_path)
    _write_semantic(completion_path, completion)

    valid, errors = subject.verify_w5_qualification(
        qualification_dir=qualification,
        run_inputs=run_inputs,
        source_manifest_builder=post_runtime_replay.build_source_manifest,
    )

    assert valid is False
    assert "eval_error_durable" in errors
    assert "fault_matrix" in errors


def test_w5_module_load_is_stdlib_only() -> None:
    code = r'''
import importlib.util
import json
import sys

name = "_apps_rg_zero_llm_qualification_import_test"
spec = importlib.util.spec_from_file_location(name, sys.argv[1])
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[name] = module
spec.loader.exec_module(module)
blocked = [
    item for item in sys.modules
    if item == "openai"
    or item.startswith("openai.")
    or item == "anthropic"
    or item.startswith("anthropic.")
    or item.startswith("agentic_core")
]
assert blocked == []
print(json.dumps({"stdlib_only": True}))
'''
    environment = dict(os.environ)
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, (str(REPO_ROOT / "src"), environment.get("PYTHONPATH", "")))
    )
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
            str(REPO_ROOT / "src/apps_rg/runtime/zero_llm_qualification.py"),
        ],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout) == {"stdlib_only": True}
