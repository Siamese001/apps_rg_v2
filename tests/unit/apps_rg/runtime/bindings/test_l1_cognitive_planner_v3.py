"""Regression and QA tests for the capability-first L1 cognitive planner."""

from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any

import pytest

from apps_rg.runtime.bindings.l1_binding import l1_plan_apps_rg
from apps_rg.runtime.bindings.l1_cognitive_planner_v3 import (
    L1CognitivePlanError,
    build_l1_cognitive_plan_v3,
    build_l1_cognitive_revision_v3,
    cognitive_plan_digest,
    cognitive_revision_digest,
    validate_l1_cognitive_plan_v3,
    validate_l1_cognitive_revision_v3,
)
from apps_rg.runtime.bindings.u0_profile_manifest import (
    l1_planning_profile_digest,
    l1_planning_profile_ref,
)
from apps_rg.runtime.spine_contracts import ValidatedRequest


def _profile_manifest() -> dict[str, str]:
    return {
        "l1_planning_profile_ref": l1_planning_profile_ref(),
        "l1_planning_profile_digest": l1_planning_profile_digest(allow_missing=False),
        "manifest_digest": "f" * 64,
    }


def _payload(jd_text: str, *, conflicts: bool = False) -> dict[str, Any]:
    constraints: dict[str, Any] = {"output_format": "executive_resume"}
    if conflicts:
        constraints["conflicting_scope"] = "product and engineering ownership conflict"
    return {
        "non_product_certified": True,
        "target_company": "Acme Corp",
        "target_role": "VP Engineering",
        "target_level": "EXECUTIVE",
        "job_description_text": jd_text,
        "source_resume_text": "Built governed AI infrastructure.",
        "generation_mode": "strategic_tailor",
        "task_spec": {
            "generation_mode": "strategic_tailor",
            "task_class": "resume_generation",
        },
        "query_spec": {"jd_hash": "a" * 64, "resume_hash": "b" * 64},
        "support_expectation": {},
        "output_expectation": {},
        "profile_manifest": _profile_manifest(),
        "user_constraints": constraints,
    }


def _plan(jd_text: str, *, conflicts: bool = False) -> dict[str, Any]:
    return dict(
        build_l1_cognitive_plan_v3(
            app_payload=_payload(jd_text, conflicts=conflicts),
            request_id="req-l1-cognitive-v3",
            run_id="run-l1-cognitive-v3",
            trace_id="trace-l1-cognitive-v3",
            replay_key="replay-l1-cognitive-v3",
            planning_profile_ref=l1_planning_profile_ref(),
            planning_profile_digest=l1_planning_profile_digest(allow_missing=False),
        )
    )


def _refresh_plan(plan: dict[str, Any]) -> None:
    plan["plan_digest"] = cognitive_plan_digest(plan)


def _mutable(value: Any) -> dict[str, Any]:
    return json.loads(json.dumps(value))


def test_qa_atomic_decomposition_creates_related_requirements_without_raw_jd() -> None:
    jd_text = "Requirements\n- Must lead AI strategy and own platform governance."
    first = _plan(jd_text)
    second = _plan(jd_text)

    assert first == second
    requirements = first["atomic_requirement_graph"]["requirements"]
    assert len(requirements) == 2
    assert {row["coverage_status"] for row in requirements} == {"MAPPED"}
    assert first["atomic_requirement_graph"]["relations"]
    assert first["atomic_requirement_graph"]["relations"][0]["relation"] == "AND"
    rendered = json.dumps(first, sort_keys=True)
    assert "Must lead AI strategy" not in rendered
    assert "platform governance" not in rendered
    validate_l1_cognitive_plan_v3(first)


def test_qa_generic_hard_requirement_is_unknown_and_escalated() -> None:
    plan = _plan("Requirements\n- Must demonstrate quantum-superiority governance.")
    requirement = plan["atomic_requirement_graph"]["requirements"][0]

    assert requirement["requirement_type"] == "UNKNOWN"
    assert requirement["coverage_status"] == "ESCALATED"
    assert plan["planning_status"] == "BLOCKED"
    assert plan["critique_ledger"]["findings"]


def test_qa_critique_blocks_declared_constraint_conflict() -> None:
    plan = _plan(
        "Requirements\n- Must lead platform engineering.", conflicts=True
    )

    codes = {row["code"] for row in plan["critique_ledger"]["findings"]}
    assert "DECLARED_CONSTRAINT_CONFLICT" in codes
    assert plan["planning_status"] == "BLOCKED"


def test_revision_is_bounded_to_an_observed_requirement_and_never_retries() -> None:
    plan = _plan("Requirements\n- Must lead platform engineering.")
    requirement_id = plan["atomic_requirement_graph"]["requirements"][0][
        "requirement_id"
    ]
    revision = dict(
        build_l1_cognitive_revision_v3(
            plan=plan,
            observed_outcomes=[
                {
                    "requirement_id": requirement_id,
                    "code": "C0_INSUFFICIENT",
                    "observation_ref": "receipts/c0_requirement.json",
                }
            ],
        )
    )

    assert revision["status"] == "PROPOSED"
    assert revision["revision_scope_requirement_ids"] == [requirement_id]
    assert revision["changes"][0]["automatic_retry"] is False
    assert revision["changes"][0]["route_change"] is False
    validate_l1_cognitive_revision_v3(revision, plan=plan)

    tampered = _mutable(revision)
    tampered["changes"][0]["route_change"] = True
    tampered["revision_digest"] = cognitive_revision_digest(tampered)
    with pytest.raises(L1CognitivePlanError, match="must remain advisory"):
        validate_l1_cognitive_revision_v3(tampered, plan=plan)


def test_regression_binding_threads_v3_without_granting_authority(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = _payload("Requirements\n- Must lead platform engineering.")
    validated = ValidatedRequest(
        request_id="req-l1-cognitive-binding",
        run_id="run-l1-cognitive-binding",
        app_id="apps_rg",
        task_class="resume_generation",
        payload_digest="e" * 64,
        authority_validation_receipt=SimpleNamespace(
            validation_timestamp="2026-08-10T00:00:00+00:00"
        ),
        trace_id="trace-l1-cognitive-binding",
        tenant_id="tenant-l1-cognitive",
        replay_key="replay-l1-cognitive-binding",
        l5_certification_ref="test:valid:cognitive-v3",
        app_payload=payload,
    )
    monkeypatch.setenv("APPS_RG_ROUTE_HMAC_SECRET", "l1-cognitive-v3-test-secret")

    plan = l1_plan_apps_rg(validated)
    cognitive = plan.task_spec["apps_rg_cognitive_v3_plan"]

    assert cognitive["schema_version"] == "apps_rg.l1_cognitive_plan.v3"
    assert plan.task_spec["apps_rg_cognitive_v3_plan_ref"] == cognitive["plan_digest"]
    assert (
        plan.output_expectation["apps_rg_cognitive_v3_critique_ref"]
        == cognitive["critique_ledger"]["ledger_digest"]
    )
    assert any(
        ref.startswith("l1_cognitive_v3_plan_digest:") for ref in plan.audit_refs
    )
    assert cognitive["validation"]["no_model_call"] is True
    assert cognitive["validation"]["no_candidate_evidence_claim"] is True


def test_validator_rejects_redigested_unknown_target_mapping() -> None:
    plan = _plan("Requirements\n- Must demonstrate quantum-superiority governance.")
    tampered = _mutable(plan)
    tampered["atomic_requirement_graph"]["requirements"][0]["coverage_status"] = "MAPPED"
    tampered["atomic_requirement_graph"]["requirements"][0]["target_unit_ids"] = [
        "experience_block"
    ]
    _refresh_plan(tampered)

    with pytest.raises(L1CognitivePlanError, match="unknown requirement"):
        validate_l1_cognitive_plan_v3(tampered)
