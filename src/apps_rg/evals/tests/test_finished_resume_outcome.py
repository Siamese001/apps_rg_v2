from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

from apps_rg.evals.finished_resume_outcome import (
    OUTCOME_VERSION,
    GUARDRAIL_DIMENSIONS,
    runtime_lanes,
    validate_finished_resume_outcome,
)


EVALS_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = EVALS_ROOT / "schemas" / "finished_resume_outcome.v1.schema.json"


def _outcome() -> dict[str, object]:
    return {
        "schema_version": OUTCOME_VERSION,
        "outcome_id": "P1",
        "required_lanes": list(runtime_lanes()),
        "review_protocol": {
            "blinded": True,
            "independent_primary_reviewers_per_pair": 2,
            "independent_adjudicators_per_pair": 1,
            "frozen_baseline_required": True,
            "candidate_preference_required": True,
            "utility_superiority_required": True,
        },
        "noninferiority_margins": {
            dimension: 0.1 for dimension in GUARDRAIL_DIMENSIONS
        },
        "p1_evidence": {
            "status": "COMPLETE",
            "pair_count": 12,
            "primary_review_count": 24,
            "adjudication_count": 12,
            "external_authority_receipt_sha256": "sha256:external-authority",
            "completed_review_receipt_digest": "sha256:completed-review",
            "utility_effect": 0.25,
            "utility_ci_lower": 0.03,
            "candidate_preference_count": 8,
            "baseline_preference_count": 3,
            "dimension_ci_lowers": {
                dimension: -0.05 for dimension in GUARDRAIL_DIMENSIONS
            },
            "synthetic_grades_created": False,
        },
        "owner_solo_status": "PRESENT_COMPLEMENTARY",
    }


def _write(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")


def test_schema_is_valid_and_tracked_p1_outcome_is_not_measured() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(_outcome())

    result = validate_finished_resume_outcome()

    assert result["status"] == "NOT_MEASURED"
    assert result["authority"]["human_qualified"] is False
    assert "P1_HUMAN_REVIEW_PENDING" in result["not_measured_reasons"]
    assert "P1_NONINFERIORITY_MARGINS_NOT_PREREGISTERED" in result[
        "not_measured_reasons"
    ]


def test_complete_summary_must_cover_all_lanes_and_strictly_pass_p1(tmp_path: Path) -> None:
    path = tmp_path / "p1.json"
    _write(path, _outcome())

    result = validate_finished_resume_outcome(path)

    assert result["status"] == "PASS"
    assert result["required_lanes"] == list(runtime_lanes())
    assert result["owner_solo_status"] == "PRESENT_COMPLEMENTARY"
    assert result["authority"]["release_authorizing"] is False


def test_tie_and_noninferiority_regression_fail_p1_without_becoming_authority(
    tmp_path: Path,
) -> None:
    tie = _outcome()
    evidence = tie["p1_evidence"]
    assert isinstance(evidence, dict)
    evidence["utility_effect"] = 0.0
    evidence["utility_ci_lower"] = 0.0
    evidence["candidate_preference_count"] = 4
    evidence["baseline_preference_count"] = 4
    path = tmp_path / "tie.json"
    _write(path, tie)

    tie_result = validate_finished_resume_outcome(path)
    assert tie_result["status"] == "FAIL"
    assert "P1_TIE_OR_BASELINE_PREFERENCE_CANNOT_ESTABLISH_SUPERIORITY" in tie_result[
        "failure_reasons"
    ]

    regression = _outcome()
    regression_evidence = regression["p1_evidence"]
    assert isinstance(regression_evidence, dict)
    dimensions = regression_evidence["dimension_ci_lowers"]
    assert isinstance(dimensions, dict)
    dimensions["grounding"] = -0.2
    regression_path = tmp_path / "regression.json"
    _write(regression_path, regression)
    regression_result = validate_finished_resume_outcome(regression_path)
    assert regression_result["status"] == "FAIL"
    assert "P1_NONINFERIORITY_GUARDRAIL_FAILED_grounding" in regression_result[
        "failure_reasons"
    ]


def test_synthetic_grades_or_wrong_lane_coverage_block_w4(tmp_path: Path) -> None:
    synthetic = _outcome()
    evidence = synthetic["p1_evidence"]
    assert isinstance(evidence, dict)
    evidence["synthetic_grades_created"] = True
    synthetic_path = tmp_path / "synthetic.json"
    _write(synthetic_path, synthetic)
    synthetic_result = validate_finished_resume_outcome(synthetic_path)
    assert synthetic_result["status"] == "BLOCKED"
    assert "P1_SYNTHETIC_GRADES_FORBIDDEN" in synthetic_result["blocking_reasons"]

    incomplete = _outcome()
    lanes = incomplete["required_lanes"]
    assert isinstance(lanes, list)
    lanes.pop()
    incomplete_path = tmp_path / "incomplete.json"
    _write(incomplete_path, incomplete)
    incomplete_result = validate_finished_resume_outcome(incomplete_path)
    assert incomplete_result["status"] == "BLOCKED"
    assert "P1_ALL_RUNTIME_LANES_REQUIRED" in incomplete_result["blocking_reasons"]
