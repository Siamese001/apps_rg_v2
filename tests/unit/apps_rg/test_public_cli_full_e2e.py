"""Public CLI coverage for the governed full Apps RG path."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from apps_rg import __main__ as cli
from apps_rg.runtime.bindings.l0_binding import (
    l0_route_apps_rg,
    reset_route_profiles_cache,
)
from apps_rg.runtime.orchestration.r3r4_whole_run_orchestration import (
    ROUTE_FAMILY_R3R4,
)
from apps_rg.runtime.spine_contracts import L1PlanContract


def test_zero_argument_cli_dispatches_the_governed_product_entry(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    captured: dict[str, object] = {}
    run_dir = tmp_path / "full-run"
    run_dir.mkdir()

    def fake_dispatch(**kwargs: object) -> dict[str, object]:
        captured.update(kwargs)
        return {
            "artifact_dir": str(run_dir),
            "product_authorized": True,
            "pipeline_complete": True,
        }

    monkeypatch.setattr(
        "apps_rg.runtime.orchestration.canonical_dispatch."
        "run_canonical_apps_rg_from_cli_primitives",
        fake_dispatch,
    )
    monkeypatch.setattr(
        cli,
        "_evaluation_for_result",
        lambda _result: {"status": "PASS", "checks": {}},
    )

    assert cli.main([]) == 0
    assert captured == {
        "target_company": cli.DEFAULT_TARGET_COMPANY,
        "target_role": cli.DEFAULT_TARGET_ROLE,
        "jd": "",
        "resume_path": "",
        "artifact_dir": "",
    }


def test_public_full_resume_route_is_active_outside_test_posture(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A production CLI full resume must not fall through to the simple route."""
    monkeypatch.delenv("PYTEST_CURRENT_TEST", raising=False)
    monkeypatch.delenv("APPS_RG_L0_TEST_POSTURE", raising=False)
    monkeypatch.delenv("APPS_RG_ENABLE_MANAGED_WORKFLOW_L0", raising=False)
    monkeypatch.setenv("APPS_RG_ROUTE_HMAC_SECRET", "test-route-signing-secret")
    reset_route_profiles_cache()

    route = l0_route_apps_rg(
        L1PlanContract(
            request_id="request-full-resume",
            run_id="run-full-resume",
            app_id="apps_rg",
            trace_id="trace-full-resume",
            grounding_required=True,
            apps_research_call_required=True,
            model_generation_required=True,
            task_spec={"generation_mode": "strategic_tailor"},
            query_spec={"jd_hash": "jd", "resume_hash": "resume"},
            support_expectation={"targeting": "required"},
            merge_required_hint=True,
        )
    )

    assert route.route_family == ROUTE_FAMILY_R3R4
    assert route.route_profile_ref.endswith("full_resume_managed::v1")
    assert route.allowed_next_stage == frozenset({"L3"})


def test_full_eval_requires_the_apps_eval_package_l6_and_e2e_ledger(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    (tmp_path / "APPS_RG_MANDATORY_RUN_OUTPUT.json").write_text(
        json.dumps(
            {
                "result_summary": {
                    "product_authorized": True,
                    "pipeline_complete": True,
                    "apps_eval_record_ref": "apps_eval/eval_record.json",
                    "l6_shadow_bridge_ref": "l6_shadow_bridge.json",
                }
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "FINAL_RESUME_OUTPUT.txt").write_text("# Resume\n", encoding="utf-8")
    (tmp_path / "l6_shadow_bridge.json").write_text("{}\n", encoding="utf-8")
    (tmp_path / "candidate_evaluation_manifest.v2.json").write_text("{}\n", encoding="utf-8")
    (tmp_path / "l6_evaluation_audit.v2.json").write_text(
        json.dumps(
            {
                "schema_version": "apps_rg.l6_evaluation_audit.v2",
                "l6_integrity_status": "PASS",
                "grain_parity_status": "PASS",
                "apps_eval_rows_bound": True,
                "independent_observations": True,
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "apps_rg_post_x3_completion_receipt.json").write_text(
        json.dumps(
            {
                "apps_eval": {
                    "execution_status": "PASS",
                    "evaluation_validity": "PASS",
                    "deterministic_product_status": "PASS",
                    "candidate_evaluation_manifest_ref": "candidate_evaluation_manifest.v2.json",
                },
                "l6_shadow": {
                    "l6_evaluation_audit_ref": "l6_evaluation_audit.v2.json",
                    "l6_integrity_status": "PASS",
                },
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "apps_eval").mkdir()
    (tmp_path / "apps_eval" / "eval_record.json").write_text("{}\n", encoding="utf-8")
    (tmp_path / "e2e_stage_ledger.json").write_text(
        json.dumps(
            {
                "terminal_state": {
                    "product_authorized": True,
                    "pipeline_complete": True,
                }
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "apps_rg.runtime.e2e_stage_ledger.verify_e2e_stage_ledger",
        lambda _path: SimpleNamespace(valid=True, complete=True, errors=()),
    )
    monkeypatch.setattr(
        "apps_eval.runner.core.verify_apps_rg_eval_package_seal",
        lambda _path: (True, []),
    )
    monkeypatch.setattr(
        "apps_rg.runtime.evaluation_manifest.validate_candidate_evaluation_manifest",
        lambda _path: ({}, []),
    )

    report = cli.evaluate_full_run(tmp_path)

    assert report["status"] == "PASS"
    assert {name for name, row in report["checks"].items() if row["status"] == "PASS"} == {
        "mandatory_output",
        "product_authorization",
        "pipeline_completion",
        "e2e_stage_ledger",
        "apps_eval",
        "evaluation_decision",
        "l6_assurance",
        "final_resume",
    }


def test_full_eval_uses_sealed_ledger_state_and_the_referenced_eval_package(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """The mandatory report is pre-terminal; the sealed ledger is authoritative."""
    eval_record = (
        tmp_path
        / "apps_eval"
        / "apps_rg_current_resume_generation"
        / "record-123"
        / "eval_record.json"
    )
    eval_record.parent.mkdir(parents=True)
    eval_record.write_text("{}\n", encoding="utf-8")
    l6_path = eval_record.parent / "l6_shadow_bridge.json"
    l6_path.write_text("{}\n", encoding="utf-8")
    (tmp_path / "candidate_evaluation_manifest.v2.json").write_text("{}\n", encoding="utf-8")
    audit = tmp_path / "l6_evaluation_audit.v2.json"
    audit.write_text(
        json.dumps(
            {
                "schema_version": "apps_rg.l6_evaluation_audit.v2",
                "l6_integrity_status": "PASS",
                "grain_parity_status": "PASS",
                "apps_eval_rows_bound": True,
                "independent_observations": True,
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "apps_rg_post_x3_completion_receipt.json").write_text(
        json.dumps(
            {
                "apps_eval": {
                    "execution_status": "PASS",
                    "evaluation_validity": "PASS",
                    "deterministic_product_status": "PASS",
                    "candidate_evaluation_manifest_ref": "candidate_evaluation_manifest.v2.json",
                },
                "l6_shadow": {
                    "l6_evaluation_audit_ref": audit.name,
                    "l6_integrity_status": "PASS",
                },
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "FINAL_RESUME_OUTPUT.txt").write_text("# Resume\n", encoding="utf-8")
    (tmp_path / "APPS_RG_MANDATORY_RUN_OUTPUT.json").write_text(
        json.dumps(
            {
                "result_summary": {
                    "product_authorized": True,
                    "pipeline_complete": False,
                    "apps_eval_record_ref": eval_record.relative_to(tmp_path).as_posix(),
                    "l6_shadow_bridge_ref": l6_path.relative_to(tmp_path).as_posix(),
                }
            }
        ),
        encoding="utf-8",
    )
    (tmp_path / "e2e_stage_ledger.json").write_text(
        json.dumps(
            {
                "terminal_state": {
                    "product_authorized": True,
                    "pipeline_complete": True,
                }
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        "apps_rg.runtime.e2e_stage_ledger.verify_e2e_stage_ledger",
        lambda _path: SimpleNamespace(valid=True, complete=True, errors=()),
    )
    verified_roots: list[Path] = []

    def verify_eval(path: Path) -> tuple[bool, list[str]]:
        verified_roots.append(path)
        return path == eval_record.parent, []

    monkeypatch.setattr(
        "apps_eval.runner.core.verify_apps_rg_eval_package_seal",
        verify_eval,
    )
    monkeypatch.setattr(
        "apps_rg.runtime.evaluation_manifest.validate_candidate_evaluation_manifest",
        lambda _path: ({}, []),
    )

    report = cli.evaluate_full_run(tmp_path)

    assert report["status"] == "PASS"
    assert verified_roots == [eval_record.parent]
    assert report["checks"]["pipeline_completion"]["pipeline_complete"] is True


def test_cli_returns_nonzero_when_full_e2e_evaluation_is_incomplete(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    run_dir = tmp_path / "incomplete"
    run_dir.mkdir()
    monkeypatch.setattr(
        "apps_rg.runtime.orchestration.canonical_dispatch."
        "run_canonical_apps_rg_from_cli_primitives",
        lambda **_kwargs: {
            "artifact_dir": str(run_dir),
            "product_authorized": True,
            "pipeline_complete": True,
        },
    )
    monkeypatch.setattr(
        cli,
        "_evaluation_for_result",
        lambda _result: {"status": "FAIL", "checks": {"apps_eval": {"status": "FAIL"}}},
    )

    assert cli.main(["run"]) == 1
    captured = capsys.readouterr()
    assert captured.out.index("FULL_RESUME") < captured.out.index("EVALS")
    assert captured.out.index("EVALS") < captured.out.index("RUNTIME_DETAILS")
    assert "UNAVAILABLE: final resume artifact was not emitted" in captured.out
    assert "```" not in captured.out


def test_public_cli_uses_distinct_product_and_evaluation_exit_classes() -> None:
    invalid_eval = {
        "evaluation_decision": {
            "status": "FAIL",
            "evaluation_validity": "INVALID",
            "l6_integrity_status": "PASS",
            "deterministic_product_status": "PASS",
        }
    }
    product_failure = {
        "evaluation_decision": {
            "status": "FAIL",
            "evaluation_validity": "PASS",
            "l6_integrity_status": "PASS",
            "deterministic_product_status": "FAIL",
        }
    }

    assert cli._evaluation_exit_code(invalid_eval) == 3
    assert cli._evaluation_exit_code(product_failure) == 2


def test_zero_provider_eval_returns_execution_class_for_a_partial_run(
    tmp_path: Path,
) -> None:
    report = cli.evaluate_full_run(tmp_path)

    assert report["status"] == "FAIL"
    assert report["exit_code"] == 4
