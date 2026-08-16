"""Focused tests for the sole Apps RG run/eval/show surface."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

import apps_rg.bare_pipeline as bare_pipeline
from apps_rg.__main__ import main


def _run_deterministic(tmp_path: Path, name: str) -> dict[str, object]:
    result = bare_pipeline.run_bare_e2e(
        mode="deterministic",
        artifact_root=str(tmp_path / name),
    )
    assert result["status"] == "SUCCESS"
    return result


def _prepare_live_x3_failure(monkeypatch, tmp_path: Path) -> tuple[dict[str, object], dict[str, int]]:
    """Produce a sealed X3-only failure without issuing a real provider call."""

    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("GOOGLE_API_KEY", "test-google-key")
    monkeypatch.setattr(
        bare_pipeline,
        "_retrieve_sources",
        lambda _company, _role: (
            [
                {
                    "family": "company",
                    "query": "test query",
                    "title": "Test source",
                    "url": "https://example.test/source",
                    "snippet": "Test source material.",
                    "engines": [],
                }
            ],
            [],
        ),
    )
    resolved_resume = bare_pipeline.resolve_resume_for_lanes(
        repo_root=bare_pipeline._repo_root(),
        require_json_document=False,
    )
    tailored_resume = bare_pipeline._render_deterministic_resume(
        resume_source=resolved_resume.raw_utf8,
        company=bare_pipeline.DEFAULT_TARGET_COMPANY,
        role=bare_pipeline.DEFAULT_TARGET_ROLE,
    )
    outreach_email = bare_pipeline._render_deterministic_email(
        resume_source=resolved_resume.raw_utf8,
        company=bare_pipeline.DEFAULT_TARGET_COMPANY,
        role=bare_pipeline.DEFAULT_TARGET_ROLE,
    )
    calls = {"openai": 0}

    def raw_openai_receipt() -> dict[str, object]:
        return {
            "provider": "external_openai",
            "requested_model": "test-openai",
            "observed_model": "test-openai",
            "provider_response_id": "openai-response",
            "terminal_status": "SUCCESS",
            "usage": {},
        }

    def fake_openai(*, max_completion_tokens: int, **_kwargs):
        calls["openai"] += 1
        if max_completion_tokens == 2400:
            return "Grounded research brief. " * 20, raw_openai_receipt()
        return (
            "<tailored_resume>\n"
            + tailored_resume
            + "\n</tailored_resume>\n<outreach_email>\n"
            + outreach_email
            + "\n</outreach_email>",
            raw_openai_receipt(),
        )

    def failing_gemini(**_kwargs):
        raise bare_pipeline.BarePipelineError("injected X3 transport failure")

    monkeypatch.setattr(bare_pipeline, "_call_openai", fake_openai)
    monkeypatch.setattr(bare_pipeline, "_run_gemini_evaluation", failing_gemini)
    result = bare_pipeline.run_bare_live_e2e(artifact_root=str(tmp_path / "live-x3-failure"))
    assert result["status"] == "FAIL"
    assert result["failure_stage"] == "X3"
    return result, calls


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
    resume_check = result["section_checks"]["resume"]
    assert resume_check["shape"]["core_competency_category_count"] == {
        "actual": 8,
        "minimum": 6,
        "maximum": 8,
    }
    assert resume_check["shape"]["employment_bullet_counts"] == {
        "unify_bullet_count": {"actual": 6, "required": 6},
        "ibm_bullet_count": {"actual": 5, "required": 5},
    }
    assert "## TECHNICAL EXPERTISE" not in (run_dir / "resume.md").read_text(encoding="utf-8")
    assert "Subject:" not in (run_dir / "resume.md").read_text(encoding="utf-8")
    assert (run_dir / "outreach_email.md").read_text(encoding="utf-8").startswith("Subject:")
    delivery = next(stage for stage in result["stages"] if stage["stage"] == "DELIVERY")
    assert delivery["details"]["docx_check"]["forbidden_headings"] == {
        "TECHNICAL EXPERTISE": True
    }


def test_public_cli_deterministic_run_enforces_the_same_resume_shape(capsys, tmp_path: Path) -> None:
    assert main(["run", "--mode", "deterministic", "--artifact-dir", str(tmp_path)]) == 0
    output = capsys.readouterr().out
    assert "APPS_RG status=SUCCESS mode=deterministic" in output
    assert "FULL_RESUME\n```markdown\n# Amit Ayer" in output
    assert "EVALS\n```json" in output
    assert '"run_evaluation"' in output
    assert "RUNTIME_DETAILS\n```json" in output
    assert '"stages"' in output

    run_dirs = [path for path in tmp_path.iterdir() if path.is_dir()]
    assert len(run_dirs) == 1
    summary = json.loads((run_dirs[0] / "run_summary.json").read_text(encoding="utf-8"))
    resume_check = summary["section_checks"]["resume"]
    assert resume_check["checks"]["core_competency_category_count"] is True
    assert resume_check["checks"]["unify_bullet_count"] is True
    assert resume_check["checks"]["ibm_bullet_count"] is True
    assert resume_check["checks"]["technical_expertise_not_separate_section"] is True
    assert resume_check["checks"]["outreach_email_not_embedded_in_resume"] is True


def test_run_inline_outputs_are_mandatory_when_a_run_fails_before_artifacts(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "apps_rg.__main__.run_bare_e2e",
        lambda **_kwargs: {
            "status": "FAIL",
            "mode": "live",
            "outcome_label": "LIVE_PROVIDER_FAIL",
            "artifact_dir": "C:/not-a-real-run",
            "stages": [],
            "error": "injected failure",
        },
    )

    assert main(["run"]) == 1
    captured = capsys.readouterr()
    assert "FULL_RESUME\n```markdown\nUNAVAILABLE: run artifact directory is unavailable" in captured.out
    assert "EVALS\n```json" in captured.out
    assert '"status": "UNAVAILABLE"' in captured.out
    assert "RUNTIME_DETAILS\n```json" in captured.out
    assert "APPS_RG_ERROR injected failure" in captured.err


def test_live_provider_timeout_is_recorded_as_a_failed_attempt(monkeypatch, tmp_path: Path) -> None:
    """A dispatched provider call must remain observable when it raises."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("GOOGLE_API_KEY", "test-google-key")
    monkeypatch.setattr(
        bare_pipeline,
        "_retrieve_sources",
        lambda _company, _role: (
            [
                {
                    "family": "company",
                    "query": "test query",
                    "title": "Test source",
                    "url": "https://example.test/source",
                    "snippet": "Test source material.",
                    "engines": [],
                }
            ],
            [],
        ),
    )

    def timed_out_openai(**_kwargs):
        raise TimeoutError("injected transport timeout")

    monkeypatch.setattr(bare_pipeline, "_call_openai", timed_out_openai)

    result = bare_pipeline.run_bare_live_e2e(artifact_root=str(tmp_path / "timeout"))

    assert result["status"] == "FAIL"
    assert result["failure_stage"] == "APPS_RESEARCH"
    assert result["provider_call_count"] == 1
    provider = result["providers"]["apps_research_openai"]
    assert provider["provider_call_attempted"] is True
    assert provider["status"] == "FAIL"
    assert provider["failure_code"] == "TRANSPORT_TIMEOUT"
    assert "TimeoutError: injected transport timeout" in provider["error"]
    report = json.loads(
        (Path(str(result["artifact_dir"])) / "provider_calls.json").read_text(encoding="utf-8")
    )
    assert report["provider_call_count"] == 1
    assert report["providers"]["apps_research_openai"]["failure_code"] == "TRANSPORT_TIMEOUT"
    assert result["outputs"]["provider_calls"] == "provider_calls.json"


def test_live_x3_provider_receipt_preserves_terminal_identity(monkeypatch, tmp_path: Path) -> None:
    """X3 must store the raw gateway receipt exactly once before summarizing it."""
    monkeypatch.setenv("OPENAI_API_KEY", "test-openai-key")
    monkeypatch.setenv("GOOGLE_API_KEY", "test-google-key")
    monkeypatch.setattr(
        bare_pipeline,
        "_retrieve_sources",
        lambda _company, _role: (
            [
                {
                    "family": "company",
                    "query": "test query",
                    "title": "Test source",
                    "url": "https://example.test/source",
                    "snippet": "Test source material.",
                    "engines": [],
                }
            ],
            [],
        ),
    )
    resolved_resume = bare_pipeline.resolve_resume_for_lanes(
        repo_root=bare_pipeline._repo_root(),
        require_json_document=False,
    )
    tailored_resume = bare_pipeline._render_deterministic_resume(
        resume_source=resolved_resume.raw_utf8,
        company=bare_pipeline.DEFAULT_TARGET_COMPANY,
        role=bare_pipeline.DEFAULT_TARGET_ROLE,
    )
    outreach_email = bare_pipeline._render_deterministic_email(
        resume_source=resolved_resume.raw_utf8,
        company=bare_pipeline.DEFAULT_TARGET_COMPANY,
        role=bare_pipeline.DEFAULT_TARGET_ROLE,
    )

    def raw_openai_receipt() -> dict[str, object]:
        return {
            "provider": "external_openai",
            "requested_model": "test-openai",
            "observed_model": "test-openai",
            "provider_response_id": "openai-response",
            "terminal_status": "SUCCESS",
            "usage": {},
        }

    def fake_openai(*, max_completion_tokens: int, **_kwargs):
        if max_completion_tokens == 2400:
            return "Grounded research brief. " * 20, raw_openai_receipt()
        return (
            "<tailored_resume>\n"
            + tailored_resume
            + "\n</tailored_resume>\n<outreach_email>\n"
            + outreach_email
            + "\n</outreach_email>",
            raw_openai_receipt(),
        )

    monkeypatch.setattr(bare_pipeline, "_call_openai", fake_openai)

    def fake_gemini(*, run_dir: Path, **_kwargs):
        bare_pipeline._write_text(
            run_dir / "x3_raw.txt",
            '{"verdict":"PASS","score":1.0,"reasoning":"grounded"}',
        )
        return (
            {"verdict": "PASS", "score": 1.0, "reasoning": "grounded"},
            {
                "provider": "google_gemini",
                "requested_model": "test-gemini",
                "observed_model": "test-gemini",
                "provider_response_id": "gemini-response",
                "terminal_status": "SUCCESS",
                "usage": {},
            },
        )

    monkeypatch.setattr(bare_pipeline, "_run_gemini_evaluation", fake_gemini)

    result = bare_pipeline.run_bare_live_e2e(artifact_root=str(tmp_path / "live"))

    assert result["status"] == "SUCCESS"
    x3_provider = result["providers"]["x3_gemini"]
    assert x3_provider["status"] == "SUCCESS"
    assert x3_provider["response_id"] == "gemini-response"


def test_x3_uses_the_bounded_transport_retry_policy(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("GOOGLE_API_KEY", "test-google-key")
    captured: dict[str, object] = {}

    def fake_gateway(**kwargs):
        captured.update(kwargs)
        return type(
            "Result",
            (),
            {
                "output": '{"verdict":"PASS","score":1.0,"reasoning":"grounded"}',
                "receipt": {
                    "provider": "google_gemini",
                    "requested_model": "gemini-3.6-flash",
                    "observed_model": "gemini-3.6-flash",
                    "provider_response_id": "gemini-policy",
                    "terminal_status": "SUCCESS",
                    "usage": {},
                    "transport_attempt_count": 2,
                    "retry_count": 1,
                },
            },
        )()

    monkeypatch.setattr(bare_pipeline, "invoke_gemini_handoff_judge", fake_gateway)
    decision, receipt = bare_pipeline._run_gemini_evaluation(
        run_dir=tmp_path,
        jd_text="JD",
        resume_source="Base resume",
        research_brief="Research",
        tailored_resume="Tailored resume",
        outreach_email="Subject: Anthropic\nbody",
        sources=[
            {
                "title": "Source",
                "url": "https://example.test/source",
                "snippet": "Evidence",
            }
        ],
    )

    assert decision["verdict"] == "PASS"
    assert captured["timeout"] == bare_pipeline.X3_GEMINI_TIMEOUT_SECONDS == 90.0
    assert captured["max_transport_attempts"] == bare_pipeline.X3_GEMINI_MAX_TRANSPORT_ATTEMPTS == 2
    assert captured["retry_backoff_base_seconds"] == 1.0
    assert captured["retry_backoff_max_seconds"] == 3.0
    assert receipt["transport_attempt_count"] == 2
    assert receipt["retry_count"] == 1
    assert receipt["input_characters"] > 0


def test_resume_x3_reuses_sealed_artifacts_without_replaying_openai(monkeypatch, tmp_path: Path) -> None:
    failed, calls = _prepare_live_x3_failure(monkeypatch, tmp_path)
    run_dir = Path(str(failed["artifact_dir"]))
    assert (run_dir / bare_pipeline.X3_RESUME_MANIFEST_FILENAME).is_file()
    assert (run_dir / bare_pipeline.X3_RESUME_JD_FILENAME).is_file()
    assert (run_dir / bare_pipeline.X3_RESUME_BASE_RESUME_FILENAME).is_file()

    def successful_gemini(*, run_dir: Path, **_kwargs):
        bare_pipeline._write_text(
            run_dir / "x3_raw.txt",
            '{"verdict":"PASS","score":1.0,"reasoning":"grounded"}',
        )
        return (
            {"verdict": "PASS", "score": 1.0, "reasoning": "grounded"},
            {
                "provider": "google_gemini",
                "requested_model": "gemini-3.6-flash",
                "observed_model": "gemini-3.6-flash",
                "provider_response_id": "gemini-resume",
                "terminal_status": "SUCCESS",
                "usage": {},
                "transport_attempt_count": 2,
                "retry_count": 1,
            },
        )

    monkeypatch.setattr(bare_pipeline, "_run_gemini_evaluation", successful_gemini)
    resumed = bare_pipeline.run_bare_e2e(resume_run_dir=str(run_dir))

    assert resumed["status"] == "SUCCESS"
    assert resumed["outcome_label"] == "LIVE_PROVIDER_PASS_AFTER_X3_RESUME"
    assert "failure_stage" not in resumed
    assert "error" not in resumed
    assert calls == {"openai": 2}
    assert [stage["stage"] for stage in resumed["stages"]] == list(bare_pipeline.CANONICAL_STAGE_ORDER)
    assert all(stage["status"] == "PASS" for stage in resumed["stages"])
    assert resumed["providers"]["x3_gemini"]["transport_attempt_count"] == 2
    assert resumed["providers"]["x3_gemini"]["retry_count"] == 1
    assert resumed["resume_history"][-1]["prior_x3_stage"]["status"] == "FAIL"
    assert (run_dir / "evaluation.json").is_file()
    assert (run_dir / "resume.docx").is_file()


def test_resume_x3_rejects_tampered_artifacts_without_provider_dispatch(monkeypatch, tmp_path: Path) -> None:
    failed, _calls = _prepare_live_x3_failure(monkeypatch, tmp_path)
    run_dir = Path(str(failed["artifact_dir"]))
    (run_dir / "resume.md").write_text("tampered", encoding="utf-8")
    dispatched = {"value": False}

    def forbidden_gemini(**_kwargs):
        dispatched["value"] = True
        raise AssertionError("tampered X3 inputs must fail before provider dispatch")

    monkeypatch.setattr(bare_pipeline, "_run_gemini_evaluation", forbidden_gemini)
    with pytest.raises(bare_pipeline.BarePipelineError, match="digests do not match"):
        bare_pipeline.run_bare_e2e(resume_run_dir=str(run_dir))
    assert dispatched["value"] is False


def test_terminal_x3_failure_never_emits_delivery_artifacts(monkeypatch, tmp_path: Path) -> None:
    failed, _calls = _prepare_live_x3_failure(monkeypatch, tmp_path)
    run_dir = Path(str(failed["artifact_dir"]))

    assert failed["failure_stage"] == "X3"
    assert [stage["stage"] for stage in failed["stages"]] == list(bare_pipeline.CANONICAL_STAGE_ORDER[:10])
    assert not (run_dir / "x3_raw.txt").exists()
    assert not (run_dir / "evaluation.json").exists()
    assert not (run_dir / "resume.docx").exists()


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
