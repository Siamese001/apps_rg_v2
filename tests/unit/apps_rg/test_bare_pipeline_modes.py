"""Focused tests for the sole Apps RG run/eval/show surface."""

from __future__ import annotations

import json
from pathlib import Path

import apps_rg.bare_pipeline as bare_pipeline
from apps_rg.__main__ import main


def _run_deterministic(tmp_path: Path, name: str) -> dict[str, object]:
    result = bare_pipeline.run_bare_e2e(
        mode="deterministic",
        artifact_root=str(tmp_path / name),
    )
    assert result["status"] == "SUCCESS"
    return result


def test_deterministic_mode_runs_full_contract_without_live_hooks(monkeypatch, tmp_path: Path) -> None:
    def forbidden(*_args, **_kwargs):
        raise AssertionError("a deterministic run must not use a live-provider hook")

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("GOOGLE_API_KEY", raising=False)
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    monkeypatch.setattr(bare_pipeline, "_require_live_provider_credentials", forbidden)
    monkeypatch.setattr(bare_pipeline, "_retrieve_sources", forbidden)
    monkeypatch.setattr(bare_pipeline, "_call_openai", forbidden)
    monkeypatch.setattr(bare_pipeline, "_run_gemini_evaluation", forbidden)

    result = _run_deterministic(tmp_path, "first")

    assert result["mode"] == "deterministic"
    assert result["outcome_label"] == "DETERMINISTIC_OFFLINE_PASS"
    assert result["provider_call_count"] == 0
    assert result["providers"] == {}
    assert [stage["stage"] for stage in result["stages"]] == list(bare_pipeline.CANONICAL_STAGE_ORDER)
    assert all(stage["status"] == "PASS" for stage in result["stages"])
    run_dir = Path(str(result["artifact_dir"]))
    assert not (run_dir / "external_model_usage_ledger.jsonl").exists()
    assert json.loads((run_dir / "provider_calls.json").read_text(encoding="utf-8")) == {
        "mode": "deterministic",
        "provider_call_count": 0,
        "providers": {},
        "schema_version": "apps_rg.provider_calls.v1",
    }


def test_deterministic_runs_compare_equal_after_documented_normalization(tmp_path: Path) -> None:
    first = _run_deterministic(tmp_path, "first")
    second = _run_deterministic(tmp_path, "second")

    report = bare_pipeline.evaluate_bare_run(
        str(first["artifact_dir"]),
        compare_run_dir=str(second["artifact_dir"]),
    )

    assert report["status"] == "PASS"
    assert report["checks"]["deterministic_comparison"]["status"] == "PASS"


def test_eval_and_show_actions_use_completed_artifacts_without_provider_calls(capsys, tmp_path: Path) -> None:
    result = _run_deterministic(tmp_path, "run")
    run_dir = str(result["artifact_dir"])
    expected_resume = (Path(run_dir) / "resume.md").read_text(encoding="utf-8")

    assert main(["eval", "--run-dir", run_dir]) == 0
    evaluation_output = capsys.readouterr().out
    assert "APPS_RG_EVAL status=PASS" in evaluation_output

    assert main(["show", "--run-dir", run_dir, "--artifact", "resume"]) == 0
    assert capsys.readouterr().out == expected_resume


def test_legacy_fresh_e2e_flag_remains_one_live_run_alias(monkeypatch) -> None:
    captured: dict[str, object] = {}

    def fake_run(**kwargs):
        captured.update(kwargs)
        return {"status": "SUCCESS", "mode": "live", "artifact_dir": "C:/Temp/run", "stages": []}

    monkeypatch.setattr("apps_rg.__main__.run_bare_e2e", fake_run)

    assert main(["--fresh-e2e"]) == 0
    assert captured["mode"] == "live"


def test_zero_argument_cli_routes_to_the_canonical_live_run(monkeypatch) -> None:
    captured: dict[str, object] = {}

    def fake_run(**kwargs):
        captured.update(kwargs)
        return {"status": "SUCCESS", "mode": "live", "artifact_dir": "C:/Temp/run", "stages": []}

    monkeypatch.setattr("apps_rg.__main__.run_bare_e2e", fake_run)

    assert main([]) == 0
    assert captured["mode"] == "live"
    assert captured["target_company"] == bare_pipeline.DEFAULT_TARGET_COMPANY
    assert captured["target_role"] == bare_pipeline.DEFAULT_TARGET_ROLE


def test_replay_detects_tampered_resume_artifact(tmp_path: Path) -> None:
    result = _run_deterministic(tmp_path, "run")
    run_dir = Path(str(result["artifact_dir"]))
    resume = run_dir / "resume.md"
    resume.write_text("# Incomplete\n", encoding="utf-8")

    report = bare_pipeline.evaluate_bare_run(run_dir)

    assert report["status"] == "FAIL"
    assert report["checks"]["resume_markdown"]["status"] == "FAIL"
