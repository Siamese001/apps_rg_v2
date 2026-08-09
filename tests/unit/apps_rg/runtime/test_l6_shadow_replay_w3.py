"""W3 acceptance for deterministic, independent L6 shadow replay."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

from apps_rg.runtime import l6_shadow_replay as subject


REPO_ROOT = Path(__file__).resolve().parents[4]


def _scorecard_row(lane_id: str) -> dict[str, object]:
    digest = "sha256:" + "1" * 64
    return {
        "suite_id": "apps_rg.current.resume_generation",
        "scenario_id": "post-runtime-test",
        "app_id": "apps_rg",
        "row_id": f"row-{lane_id}",
        "microstep_id": f"{lane_id}.X1D.judge_result.pass",
        "stage_id": "X1D",
        "component_id": "apps_rg.generated_lane",
        "subcomponent_id": "lane_x1d_judge_panel",
        "verdict": "FAIL",
        "score": 0.0,
        "severity": "BLOCK",
        "required": True,
        "run_id": "eval-record",
        "lane_id": lane_id,
        "gate_id": "x1d",
        "artifact_role": "lane_x1d_llm_judge_outputs",
        "artifact_ref": f"modular_r4/sections/{lane_id}/x1d_llm_judge_outputs.json",
        "evidence_ref": f"modular_r4/sections/{lane_id}/x1d_llm_judge_outputs.json",
        "evidence_digest": digest,
        "failure_mode": "evidence.source_identity_missing",
        "failure_family": "evidence",
        "parent_run_id": "parent",
        "child_run_id": "child",
        "section_attempt_id": "",
        "eval_record_id": "eval-record",
        "runtime_exhaust_bundle_id": "",
        "microstep_contract_digest": digest,
        "registry_digest": digest,
        "snapshot_digest": digest,
    }


def test_legacy_l6_packages_remain_advisory_and_never_bind(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    output = tmp_path / "w3"
    rows = [_scorecard_row(lane) for lane in subject.EXPECTED_LANES]
    for lane in subject.EXPECTED_LANES:
        lane_dir = source / "modular_r4" / "sections" / lane
        lane_dir.mkdir(parents=True)
        (lane_dir / "l6_shadow_eval_package.json").write_text(
            json.dumps({"schema_version": "apps_rg.l6_shadow_eval_package.v1"}),
            encoding="utf-8",
        )
    record = SimpleNamespace(
        record_id="eval-record",
        snapshot_digest="sha256:" + "1" * 64,
        registry_digest="sha256:" + "1" * 64,
    )

    result = subject._write_independent_bindings(
        source=source,
        output_dir=output,
        record=record,
        scorecard_rows=rows,
        scorecard_ref="sealed-scorecard.jsonl",
    )

    assert result["summary"]["sections_total"] == 11
    assert result["summary"]["sections_legacy"] == 11
    assert result["summary"]["sections_bound"] == 0
    assert result["summary"]["apps_eval_rows_bound"] is False
    assert result["closure"]["binding_closure_status"] == "FAIL"
    assert result["closure"]["evidence_class"] == "CONTRACT_ONLY_ADVISORY"
    assert all(
        binding["binding_status"] == "LEGACY_PACKAGE_ADVISORY"
        and binding["evidence_class"] == "CONTRACT_ONLY_ADVISORY"
        for binding in result["payload"]["bindings"]
    )


def test_eval_package_seal_reopens_every_bound_artifact(tmp_path: Path) -> None:
    run_dir = tmp_path / "eval"
    run_dir.mkdir()
    roles = {
        "eval_record": "eval_record.json",
        "scorecard_rows": "scorecard_rows.jsonl",
        "component_scorecards": "component_scorecards.csv",
        "coverage_matrix": "coverage_matrix.csv",
        "regression_summary": "regression.json",
    }
    artifacts = []
    for role, name in roles.items():
        path = run_dir / name
        path.write_text(f"{role}\n", encoding="utf-8")
        artifacts.append(
            {
                "artifact_role": role,
                "artifact_ref": name,
                "byte_length": path.stat().st_size,
                "sha256": subject._sha256_file(path),
            }
        )
    body = {
        "schema_version": "apps_eval.apps_rg_eval_package_seal.v1",
        "status": "PASS",
        "record_id": "record",
        "artifacts": artifacts,
    }
    (run_dir / "apps_rg_eval_package_seal.json").write_text(
        json.dumps({**body, "manifest_sha256": subject._canonical_digest(body)}),
        encoding="utf-8",
    )

    valid, errors = subject._verify_eval_package_seal(run_dir)
    assert valid is True
    assert errors == []

    (run_dir / "scorecard_rows.jsonl").write_text("tampered\n", encoding="utf-8")
    valid, errors = subject._verify_eval_package_seal(run_dir)
    assert valid is False
    assert "eval_package_seal_artifact_digest_mismatch:scorecard_rows" in errors


def test_minimal_core_namespace_keeps_provider_and_uwg_modules_out(
    tmp_path: Path,
) -> None:
    code = r'''
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

module_name = "_apps_rg_l6_shadow_replay_test"
spec = importlib.util.spec_from_file_location(module_name, sys.argv[2])
assert spec is not None and spec.loader is not None
replay = importlib.util.module_from_spec(spec)
sys.modules[module_name] = replay
spec.loader.exec_module(replay)
replay._install_minimal_agentic_core_namespace()
from apps_eval.contracts.models import CompletedEvalRecord, RegressionSummary, Scorecard
from apps_eval.l6_shadow_bridge import emit_completed_eval_l6_shadow_bridge

digest = "sha256:" + "2" * 64
row = {
    "suite_id": "apps_rg.current.resume_generation",
    "scenario_id": "replay",
    "app_id": "apps_rg",
    "row_id": "row-headline",
    "microstep_id": "headline.X1D.judge_result.pass",
    "stage_id": "X1D",
    "component_id": "apps_rg.generated_lane",
    "subcomponent_id": "lane_x1d_judge_panel",
    "verdict": "FAIL",
    "score": 0.0,
    "severity": "BLOCK",
    "required": True,
    "run_id": "record",
    "lane_id": "headline",
    "gate_id": "x1d",
    "artifact_role": "lane_x1d_llm_judge_outputs",
    "artifact_ref": "source/x1d_llm_judge_outputs.json",
    "evidence_ref": "source/x1d_llm_judge_outputs.json",
    "evidence_digest": digest,
    "parent_run_id": "parent",
    "child_run_id": "child",
    "section_attempt_id": "attempt",
    "eval_record_id": "record",
    "runtime_exhaust_bundle_id": "source-rxb",
    "microstep_contract_digest": digest,
    "registry_digest": digest,
    "snapshot_digest": digest,
}
record = CompletedEvalRecord(
    record_id="record",
    created_at="1970-01-01T00:00:00Z",
    suite_id="apps_rg.current.resume_generation",
    app_id="apps_rg",
    mode="current_snapshot",
    deterministic_only=True,
    scenario_results=[],
    scorecard=Scorecard(
        suite_id="apps_rg.current.resume_generation",
        app_id="apps_rg",
        scenario_count=1,
        finding_count=1,
        passed_findings=0,
        failed_findings=1,
        block_failures=1,
        score=0.0,
        verdict="fail",
        scorecard_rows=[row],
        coverage_summary={"release_blocked": True},
    ),
    regression=RegressionSummary(compared=False),
    artifact_paths={"scorecard_rows": "scorecard_rows.jsonl"},
    rubric_ids=[],
    eval_execution_complete=True,
    eval_verdict="fail",
    release_blocked=True,
    parent_run_id="parent",
    child_run_id="child",
    section_attempt_id="attempt",
    eval_record_id="record",
    runtime_exhaust_bundle_id="source-rxb",
    microstep_contract_digest=digest,
    registry_digest=digest,
    snapshot_digest=digest,
)
root = Path(sys.argv[1])
paths = emit_completed_eval_l6_shadow_bridge(
    record,
    root,
    eval_record_path="eval_record.json",
    l6_handoff_path="l6_handoff.json",
    deterministic_replay=True,
)
first = {
    key: hashlib.sha256(Path(value).read_bytes()).hexdigest()
    for key, value in paths.items()
}
paths = emit_completed_eval_l6_shadow_bridge(
    record,
    root,
    eval_record_path="eval_record.json",
    l6_handoff_path="l6_handoff.json",
    deterministic_replay=True,
)
second = {
    key: hashlib.sha256(Path(value).read_bytes()).hexdigest()
    for key, value in paths.items()
}
assert first == second
assert "openai" not in sys.modules
assert "anthropic" not in sys.modules
assert "agentic_core.L2_execution.utils.write_gateway" not in sys.modules
bridge = json.loads(Path(paths["l6_shadow_bridge"]).read_text(encoding="utf-8"))
assert bridge["deterministic_replay"] is True
assert bridge["projection_consistency_only"] is True
assert bridge["evidence_class"] == "CONTRACT_ONLY_ADVISORY"
print(json.dumps({"stable": True, "artifact_count": len(paths)}))
'''
    environment = dict(os.environ)
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(
            None,
            (
                str(REPO_ROOT / "src"),
                environment.get("PYTHONPATH", ""),
            ),
        )
    )

    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
            str(tmp_path / "projection"),
            str(REPO_ROOT / "src/apps_rg/runtime/l6_shadow_replay.py"),
        ],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout) == {"artifact_count": 10, "stable": True}
