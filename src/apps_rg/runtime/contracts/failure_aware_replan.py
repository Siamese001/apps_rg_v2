"""W2 failure-aware, non-executing replans over W1 observations.

The replan decision is an immutable advisory revision.  It links a verified
parent L1 capsule to the exact W1 receipt that triggered it, and it proposes
only the next governed owner.  It never retries work, changes a route,
retrieves evidence, calls a model, or authorizes an exit.
"""

from __future__ import annotations

import copy
import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Final

from apps_rg.runtime.bindings.l1_planning_capsule import (
    PlanningCapsuleIntegrityError,
    verify_apps_rg_l1_planning_capsule,
)
from apps_rg.runtime.contracts.plan_execution_reconciliation import (
    PlanExecutionReconciliationError,
    validate_plan_execution_reconciliation,
)
from apps_rg.runtime.dispatch import spine_stage_receipts as sr


FAILURE_AWARE_REPLAN_SCHEMA_VERSION: Final[str] = "apps_rg.failure_aware_replan.v1"
L1_REPLAN_REVISION_SCHEMA_VERSION: Final[str] = "apps_rg.l1_replan_revision.v1"
FAILURE_AWARE_REPLAN_CONTRACT_TYPE: Final[str] = "FailureAwareReplanDecision"
_EMITTER: Final[str] = "apps_rg.runtime.contracts.failure_aware_replan"

_ACTIONABLE_HINTS: Final[dict[str, tuple[str, str]]] = {
    "CLARIFY_OR_REPAIR_INPUT": ("CLARIFY_OR_REPAIR_INPUT", "U0"),
    "REPLAN_EVIDENCE": ("REPLAN_EVIDENCE", "C0"),
    "REPLAN_RETRIEVAL": ("REPLAN_RETRIEVAL", "C0"),
    "REPAIR_OR_RETRY_GENERATION": ("REPAIR_OR_RETRY_GENERATION", "L2"),
}
_TERMINAL_HINT: Final[str] = "TERMINAL_BLOCK"


class FailureAwareReplanError(ValueError):
    """Raised when a W2 decision lacks a trustworthy parent or trigger."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _digest(value: Mapping[str, Any], *, field: str) -> str:
    body = dict(value)
    body.pop(field, None)
    return "sha256:" + hashlib.sha256(_canonical_json(body).encode("utf-8")).hexdigest()


def _mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _normalised_ref(value: Any, *, field_name: str) -> str:
    ref = str(value or "").strip().replace("\\", "/")
    if not ref:
        raise FailureAwareReplanError(f"{field_name} is required")
    if Path(ref).is_absolute() or ".." in Path(ref).parts:
        raise FailureAwareReplanError(f"{field_name} must be a relative artifact reference")
    return ref


def _verified_parent_binding(
    plan_capsule: Mapping[str, Any], *, parent_plan_ref: str
) -> dict[str, str]:
    try:
        verified = verify_apps_rg_l1_planning_capsule(plan_capsule)
    except PlanningCapsuleIntegrityError as exc:
        raise FailureAwareReplanError(f"invalid parent L1 capsule: {exc}") from exc
    prior = (plan_capsule.get("planning_prior_refs") or [None])[0]
    if not isinstance(prior, Mapping):
        raise FailureAwareReplanError("parent L1 capsule has no planning-prior binding")
    return {
        "capsule_ref": _normalised_ref(parent_plan_ref, field_name="parent_plan_ref"),
        "capsule_digest": str(verified["capsule_digest"]),
        "planning_status": str(verified["planning_status"]),
        "planning_profile_ref": str(prior.get("ref") or ""),
        "planning_profile_digest": str(prior.get("digest") or ""),
    }


def _validate_trigger_receipt(receipt: Mapping[str, Any]) -> None:
    try:
        validate_plan_execution_reconciliation(receipt)
    except (PlanExecutionReconciliationError, ValueError) as exc:
        raise FailureAwareReplanError(f"invalid W1 trigger receipt: {exc}") from exc


def _outcomes_by_unit(receipt: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    rows = receipt.get("unit_outcomes")
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        raise FailureAwareReplanError("W1 trigger receipt has no unit outcomes")
    out: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise FailureAwareReplanError("W1 trigger outcome must be a mapping")
        unit_id = str(row.get("unit_id") or "").strip()
        if not unit_id or unit_id in out:
            raise FailureAwareReplanError("W1 trigger outcome coverage is invalid")
        out[unit_id] = row
    return out


def _observations_by_unit(receipt: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    rows = receipt.get("unit_observations")
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        raise FailureAwareReplanError("W1 trigger receipt has no unit observations")
    out: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise FailureAwareReplanError("W1 trigger observation must be a mapping")
        unit_id = str(row.get("unit_id") or "").strip()
        if not unit_id or unit_id in out:
            raise FailureAwareReplanError("W1 trigger observation coverage is invalid")
        out[unit_id] = row
    return out


def _classification_rows(receipt: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for unit_id, outcome in _outcomes_by_unit(receipt).items():
        disposition = str(outcome.get("disposition") or "").upper()
        hint = str(outcome.get("w2_replan_hint") or "")
        failure_code = str(outcome.get("failure_code") or "")
        if disposition == "COMPLETED":
            status = "NO_REPLAN_REQUIRED"
        elif hint in _ACTIONABLE_HINTS:
            status = "REPLAN_PROPOSED"
        elif hint == _TERMINAL_HINT:
            status = "TERMINAL_BLOCKED"
        else:
            raise FailureAwareReplanError(
                f"W1 outcome {unit_id!r} has unsupported W2 replan hint {hint!r}"
            )
        rows.append(
            {
                "unit_id": unit_id,
                "source_disposition": disposition,
                "failure_code": failure_code,
                "failure_class": str(outcome.get("failure_class") or ""),
                "replan_hint": hint,
                "classification": status,
            }
        )
    return sorted(rows, key=lambda row: row["unit_id"])


def _action_rows(
    classifications: Sequence[Mapping[str, Any]],
    observations: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    actions: list[dict[str, Any]] = []
    for row in classifications:
        hint = str(row.get("replan_hint") or "")
        if hint not in _ACTIONABLE_HINTS:
            continue
        unit_id = str(row["unit_id"])
        observation = observations.get(unit_id)
        if observation is None:
            raise FailureAwareReplanError(
                f"W1 observation is missing for replan unit {unit_id!r}"
            )
        strategy, next_owner = _ACTIONABLE_HINTS[hint]
        evidence_only = strategy in {"REPLAN_EVIDENCE", "REPLAN_RETRIEVAL"}
        actions.append(
            {
                "unit_id": unit_id,
                "failure_code": str(row["failure_code"]),
                "failure_class": str(row["failure_class"]),
                "strategy": strategy,
                "next_governed_owner": next_owner,
                "parent_evidence_plan": copy.deepcopy(
                    _mapping(observation.get("evidence_plan"))
                ),
                "requested_controls": copy.deepcopy(
                    _mapping(observation.get("requested_controls"))
                ),
                "generation_retry_prohibited": evidence_only,
                "requires_new_governed_generation": (
                    strategy == "REPAIR_OR_RETRY_GENERATION"
                ),
                "automatic_execution": False,
                "automatic_retry": False,
                "automatic_route_change": False,
                "automatic_exit_authorization": False,
            }
        )
    return sorted(actions, key=lambda row: row["unit_id"])


def _revision(
    *,
    parent: Mapping[str, str],
    trigger: Mapping[str, str],
    actions: Sequence[Mapping[str, Any]],
) -> dict[str, Any] | None:
    if not actions:
        return None
    deltas = [
        {
            "unit_id": str(action["unit_id"]),
            "strategy": str(action["strategy"]),
            "next_governed_owner": str(action["next_governed_owner"]),
            "parent_evidence_plan": copy.deepcopy(action["parent_evidence_plan"]),
            "requested_controls": copy.deepcopy(action["requested_controls"]),
            "generation_retry_prohibited": bool(action["generation_retry_prohibited"]),
            "requires_new_governed_generation": bool(
                action["requires_new_governed_generation"]
            ),
        }
        for action in actions
    ]
    seed = {
        "schema_version": L1_REPLAN_REVISION_SCHEMA_VERSION,
        "parent_plan_capsule_digest": parent["capsule_digest"],
        "trigger_receipt_digest": trigger["receipt_digest"],
        "revision_number": 1,
        "plan_deltas": deltas,
    }
    revision_id = "l1r-" + hashlib.sha256(_canonical_json(seed).encode("utf-8")).hexdigest()[:16]
    revision: dict[str, Any] = {
        **seed,
        "revision_id": revision_id,
        "authority_class": "PLANNING_ADVISORY_ONLY",
        "execution_authority_assertions": {
            "does_not_execute_work_units": True,
            "does_not_select_retries": True,
            "does_not_change_route": True,
            "does_not_authorize_exit": True,
        },
    }
    revision["revision_digest"] = _digest(revision, field="revision_digest")
    return revision


def _decision_digest(decision: Mapping[str, Any]) -> str:
    return _digest(decision, field="decision_digest")


def build_failure_aware_replan(
    *,
    plan_capsule: Mapping[str, Any],
    parent_plan_ref: str,
    plan_execution_receipt: Mapping[str, Any],
    trigger_receipt_ref: str,
) -> dict[str, Any]:
    """Classify W1 outcomes and produce an optional digest-bound plan revision."""

    parent = _verified_parent_binding(plan_capsule, parent_plan_ref=parent_plan_ref)
    _validate_trigger_receipt(plan_execution_receipt)
    ref = _normalised_ref(trigger_receipt_ref, field_name="trigger_receipt_ref")
    if (
        str(plan_execution_receipt.get("request_id") or "")
        != str(plan_capsule.get("request_id") or "")
        or str(plan_execution_receipt.get("run_id") or "")
        != str(plan_capsule.get("run_id") or "")
    ):
        raise FailureAwareReplanError("W1 trigger receipt identity does not match parent L1 plan")
    trigger_plan = _mapping(plan_execution_receipt.get("plan"))
    if trigger_plan.get("capsule_digest") != parent["capsule_digest"]:
        raise FailureAwareReplanError("W1 trigger receipt is bound to a different L1 plan")

    classifications = _classification_rows(plan_execution_receipt)
    observations = _observations_by_unit(plan_execution_receipt)
    if set(observations) != {str(row["unit_id"]) for row in classifications}:
        raise FailureAwareReplanError("W1 trigger observations do not cover all classified units")
    actions = _action_rows(classifications, observations)
    trigger = {
        "receipt_ref": ref,
        "receipt_digest": str(plan_execution_receipt.get("receipt_digest") or ""),
        "schema_version": str(plan_execution_receipt.get("schema_version") or ""),
    }
    decision: dict[str, Any] = {
        "schema_version": FAILURE_AWARE_REPLAN_SCHEMA_VERSION,
        "contract_type": FAILURE_AWARE_REPLAN_CONTRACT_TYPE,
        "authority_class": "PLANNING_ADVISORY_ONLY",
        "request_id": str(plan_capsule.get("request_id") or ""),
        "run_id": str(plan_capsule.get("run_id") or ""),
        "parent_plan": parent,
        "trigger_receipt": trigger,
        "failure_classifications": classifications,
        "replan_actions": actions,
        "replan_status": "REPLAN_PROPOSED" if actions else "NO_ACTIONABLE_REPLAN",
        "replan_revision": _revision(parent=parent, trigger=trigger, actions=actions),
        "execution_authority_assertions": {
            "does_not_execute_work_units": True,
            "does_not_select_retries": True,
            "does_not_change_route": True,
            "does_not_authorize_exit": True,
        },
        "emitter": _EMITTER,
    }
    decision["decision_digest"] = _decision_digest(decision)
    validate_failure_aware_replan(
        decision,
        plan_capsule=plan_capsule,
        plan_execution_receipt=plan_execution_receipt,
    )
    return decision


def validate_failure_aware_replan(
    decision: Mapping[str, Any],
    *,
    plan_capsule: Mapping[str, Any],
    plan_execution_receipt: Mapping[str, Any],
) -> None:
    """Fail closed unless W2's revision exactly follows its parent and trigger."""

    if not isinstance(decision, Mapping):
        raise FailureAwareReplanError("W2 decision must be a mapping")
    if decision.get("schema_version") != FAILURE_AWARE_REPLAN_SCHEMA_VERSION:
        raise FailureAwareReplanError("unsupported W2 decision schema_version")
    if decision.get("contract_type") != FAILURE_AWARE_REPLAN_CONTRACT_TYPE:
        raise FailureAwareReplanError("invalid W2 decision contract_type")
    if decision.get("authority_class") != "PLANNING_ADVISORY_ONLY":
        raise FailureAwareReplanError("W2 decision authority_class is invalid")
    if decision.get("emitter") != _EMITTER:
        raise FailureAwareReplanError("W2 decision emitter is invalid")
    if decision.get("decision_digest") != _decision_digest(decision):
        raise FailureAwareReplanError("W2 decision digest mismatch")

    parent_ref = _mapping(decision.get("parent_plan")).get("capsule_ref")
    parent = _verified_parent_binding(plan_capsule, parent_plan_ref=str(parent_ref or ""))
    _validate_trigger_receipt(plan_execution_receipt)
    if decision.get("parent_plan") != parent:
        raise FailureAwareReplanError("W2 parent-plan binding is invalid")
    if (
        decision.get("request_id") != str(plan_capsule.get("request_id") or "")
        or decision.get("run_id") != str(plan_capsule.get("run_id") or "")
    ):
        raise FailureAwareReplanError("W2 decision identity is invalid")
    trigger = _mapping(decision.get("trigger_receipt"))
    expected_trigger = {
        "receipt_ref": _normalised_ref(
            trigger.get("receipt_ref"), field_name="trigger_receipt.receipt_ref"
        ),
        "receipt_digest": str(plan_execution_receipt.get("receipt_digest") or ""),
        "schema_version": str(plan_execution_receipt.get("schema_version") or ""),
    }
    if trigger != expected_trigger:
        raise FailureAwareReplanError("W2 trigger receipt binding is invalid")

    classifications = _classification_rows(plan_execution_receipt)
    if decision.get("failure_classifications") != classifications:
        raise FailureAwareReplanError("W2 failure classifications do not match W1 outcomes")
    observations = _observations_by_unit(plan_execution_receipt)
    actions = _action_rows(classifications, observations)
    if decision.get("replan_actions") != actions:
        raise FailureAwareReplanError("W2 replan actions do not match failure classifications")
    expected_status = "REPLAN_PROPOSED" if actions else "NO_ACTIONABLE_REPLAN"
    if decision.get("replan_status") != expected_status:
        raise FailureAwareReplanError("W2 replan status is invalid")
    expected_revision = _revision(parent=parent, trigger=expected_trigger, actions=actions)
    if decision.get("replan_revision") != expected_revision:
        raise FailureAwareReplanError("W2 replan revision does not match parent and trigger")
    assertions = _mapping(decision.get("execution_authority_assertions"))
    if any(
        assertions.get(key) is not True
        for key in (
            "does_not_execute_work_units",
            "does_not_select_retries",
            "does_not_change_route",
            "does_not_authorize_exit",
        )
    ):
        raise FailureAwareReplanError("W2 execution authority assertions are incomplete")


def emit_failure_aware_replan(
    *,
    parent_plan_capsule_path: Path,
    plan_execution_receipt_path: Path,
    artifact_dir: Path,
) -> Path:
    """Load the canonical W1 receipt and write its W2 advisory decision."""

    artifact_dir = Path(artifact_dir)
    parent_source = Path(parent_plan_capsule_path)
    source = Path(plan_execution_receipt_path)
    try:
        plan_capsule = json.loads(parent_source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise FailureAwareReplanError(f"cannot read parent L1 capsule: {parent_source}") from exc
    if not isinstance(plan_capsule, Mapping):
        raise FailureAwareReplanError("parent L1 capsule must decode to a mapping")
    try:
        receipt = json.loads(source.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise FailureAwareReplanError(f"cannot read W1 trigger receipt: {source}") from exc
    if not isinstance(receipt, Mapping):
        raise FailureAwareReplanError("W1 trigger receipt must decode to a mapping")
    try:
        parent_ref = parent_source.resolve().relative_to(artifact_dir.resolve()).as_posix()
        trigger_ref = source.resolve().relative_to(artifact_dir.resolve()).as_posix()
    except ValueError as exc:
        raise FailureAwareReplanError("W1 trigger receipt must be inside the run artifact directory") from exc
    decision = build_failure_aware_replan(
        plan_capsule=plan_capsule,
        parent_plan_ref=parent_ref,
        plan_execution_receipt=receipt,
        trigger_receipt_ref=trigger_ref,
    )
    path = artifact_dir / sr.FILENAME_PLAN_REPLAN_DECISION
    sr.write_stage_receipt(path, decision)
    return path


__all__ = [
    "FAILURE_AWARE_REPLAN_SCHEMA_VERSION",
    "L1_REPLAN_REVISION_SCHEMA_VERSION",
    "FailureAwareReplanError",
    "build_failure_aware_replan",
    "emit_failure_aware_replan",
    "validate_failure_aware_replan",
]
