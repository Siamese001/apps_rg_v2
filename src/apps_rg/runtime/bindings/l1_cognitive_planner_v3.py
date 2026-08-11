"""Source-bound, advisory cognitive planning for the Apps RG L1 boundary.

V3 is deliberately separate from the compatibility v1/v2 capsules.  It
improves the planner's representation and self-checking without taking route,
evidence, prompt, execution, model, tool, state-write, or release authority.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping, Sequence
from typing import Any, Final

from apps_rg.runtime.bindings.l1_planning_capsule import FrozenDict, _freeze
from apps_rg.runtime.bindings.l1_planning_capsule_v2 import (
    L1PlanningV2IntegrityError,
    _classify_requirement,
    _declared_jd_hash,
    _inline_jd_text,
    _load_taxonomy,
    _modality,
    _qualifiers,
    build_apps_rg_l1_planning_capsule_v2,
    verify_apps_rg_l1_planning_capsule_v2,
)


L1_COGNITIVE_V3_SCHEMA_VERSION: Final[str] = "apps_rg.l1_cognitive_plan.v3"
L1_COGNITIVE_V3_REVISION_SCHEMA_VERSION: Final[str] = (
    "apps_rg.l1_cognitive_revision.v1"
)
_AUTHORITY_CLASS: Final[str] = "PLANNING_ADVISORY_ONLY"
_APP_SCOPE: Final[str] = "APPS_RG_V2_ONLY"
_FORBIDDEN_AUTHORITY_KEYS: Final[frozenset[str]] = frozenset(
    {
        "route_id",
        "route_family",
        "selected_route",
        "evidence_items",
        "evidence_refs",
        "provider",
        "model",
        "tool_call",
        "write_path",
        "release_approval",
    }
)
_VALID_COVERAGE: Final[frozenset[str]] = frozenset(
    {"MAPPED", "ESCALATED", "UNMAPPED"}
)
_VALID_OBSERVED_OUTCOMES: Final[frozenset[str]] = frozenset(
    {
        "C0_CONTRADICTED",
        "C0_INSUFFICIENT",
        "CRITIQUE_VALIDATED",
        "DOWNSTREAM_OMISSION",
        "EXECUTION_PRECONDITION_FAILED",
    }
)
_SPLIT_RELATION_RE: Final[re.Pattern[str]] = re.compile(
    r"\s+(?P<relation>and|or)\s+(?=(?:must|should|need\s+to|have|lead|own|"
    r"manage|build|deliver|drive|demonstrate|ensure|create|develop|maintain)\b)",
    re.IGNORECASE,
)
_BULLET_PREFIX_RE: Final[re.Pattern[str]] = re.compile(r"^(?:[-*\u2022]+|\d+[.)])\s*")


class L1CognitivePlanError(ValueError):
    """Raised when an L1 v3 cognitive plan or bounded revision is invalid."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256(value: Any) -> str:
    return "sha256:" + hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _digest_without(value: Mapping[str, Any], field: str) -> str:
    body = dict(value)
    body.pop(field, None)
    return _sha256(body)


def cognitive_plan_digest(plan: Mapping[str, Any]) -> str:
    """Return the canonical digest of a cognitive plan excluding itself."""

    return _digest_without(plan, "plan_digest")


def cognitive_revision_digest(revision: Mapping[str, Any]) -> str:
    """Return the canonical digest of a revision excluding itself."""

    return _digest_without(revision, "revision_digest")


def _required_string(value: Any, *, field: str) -> str:
    normalized = str(value or "").strip()
    if not normalized:
        raise L1CognitivePlanError(f"{field} is required")
    return normalized


def _mapping(value: Any) -> dict[str, Any]:
    return dict(value) if isinstance(value, Mapping) else {}


def _source_text_for_requirement(
    jd_text: str, requirement: Mapping[str, Any]
) -> tuple[str, int]:
    span = _mapping(requirement.get("source_span"))
    start = span.get("start_offset")
    end = span.get("end_offset")
    if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end < start:
        raise L1CognitivePlanError("v2 requirement source span is invalid")
    source = jd_text[start:end]
    if not source.strip():
        raise L1CognitivePlanError("v2 requirement source span has no text")
    leading = len(source) - len(source.lstrip())
    trimmed = source.strip()
    match = _BULLET_PREFIX_RE.match(trimmed)
    prefix_size = match.end() if match else 0
    text = trimmed[prefix_size:].strip()
    if not text:
        raise L1CognitivePlanError("v2 requirement source span has no requirement text")
    content_start = start + leading + prefix_size
    while content_start < end and jd_text[content_start].isspace():
        content_start += 1
    return text, content_start


def _atomic_clause_rows(text: str, *, absolute_start: int) -> list[dict[str, Any]]:
    """Split only explicit predicate-to-predicate joins; preserve other scope."""

    rows: list[dict[str, Any]] = []
    cursor = 0
    relation = "ROOT"
    for match in _SPLIT_RELATION_RE.finditer(text):
        clause = text[cursor:match.start()].strip()
        if clause:
            relative = text.find(clause, cursor, match.start())
            rows.append(
                {
                    "text": clause,
                    "start_offset": absolute_start + relative,
                    "end_offset": absolute_start + relative + len(clause),
                    "relation_to_previous": relation,
                }
            )
        relation = str(match.group("relation")).upper()
        cursor = match.end()
    clause = text[cursor:].strip()
    if clause:
        relative = text.find(clause, cursor)
        rows.append(
            {
                "text": clause,
                "start_offset": absolute_start + relative,
                "end_offset": absolute_start + relative + len(clause),
                "relation_to_previous": relation,
            }
        )
    if not rows:
        raise L1CognitivePlanError("atomic clause extraction produced no clause")
    return rows


def _goal_constraint_frame(app_payload: Mapping[str, Any]) -> dict[str, Any]:
    task = _mapping(app_payload.get("task_spec"))
    user_constraints = _mapping(app_payload.get("user_constraints"))
    hard_keys = sorted(
        str(key)
        for key, value in user_constraints.items()
        if value not in (None, "", [], {}, False)
    )
    conflict_keys = sorted(
        str(key)
        for key in user_constraints
        if "conflict" in str(key).lower()
    )
    body = {
        "requested_artifact": str(
            task.get("task_class") or app_payload.get("task_class") or "resume_generation"
        ),
        "generation_mode": str(
            task.get("generation_mode") or app_payload.get("generation_mode") or ""
        ),
        "target_role_digest": _sha256(
            {"target_role": str(app_payload.get("target_role") or "")}
        ),
        "target_level": str(app_payload.get("target_level") or ""),
        "hard_constraint_keys": hard_keys,
        "conflict_constraint_keys": conflict_keys,
        "definition_of_done": {
            "all_critical_requirements_targeted_or_escalated": True,
            "candidate_evidence_claims_forbidden": True,
            "downstream_authority_required": True,
        },
        "authority_class": _AUTHORITY_CLASS,
    }
    body["goal_frame_id"] = "l1goal-" + _sha256(body).removeprefix("sha256:")[:16]
    return body


def _atomic_requirement_graph(
    *,
    v2_capsule: Mapping[str, Any],
    jd_text: str,
    taxonomy: Mapping[str, Any],
) -> dict[str, Any]:
    parent_rows = v2_capsule.get("requirements")
    if not isinstance(parent_rows, Sequence) or isinstance(parent_rows, (str, bytes)):
        raise L1CognitivePlanError("v2 requirements are invalid")
    requirements: list[dict[str, Any]] = []
    relations: list[dict[str, Any]] = []
    jd_hash = _declared_jd_hash({}, jd_text)
    for parent in parent_rows:
        if not isinstance(parent, Mapping):
            raise L1CognitivePlanError("v2 requirement is invalid")
        parent_id = _required_string(parent.get("requirement_id"), field="parent requirement_id")
        text, content_start = _source_text_for_requirement(jd_text, parent)
        clauses = _atomic_clause_rows(text, absolute_start=content_start)
        source_kind = str(parent.get("source_kind") or "JD_STATEMENT")
        for ordinal, clause in enumerate(clauses, start=1):
            clause_text = str(clause["text"])
            requirement_type, target_unit_id, confidence, rule_id = _classify_requirement(
                text=clause_text,
                source_kind=source_kind,
                taxonomy=taxonomy,
            )
            if rule_id == "hard_requirement_unspecified" and not target_unit_id:
                requirement_type = "UNKNOWN"
                confidence = "LOW"
                rule_id = "generic_hard_requirement_requires_semantic_review"
            parent_critical = parent.get("criticality") == "CRITICAL"
            criticality = "CRITICAL" if parent_critical else str(parent.get("criticality") or "STANDARD")
            relation_to_previous = str(clause["relation_to_previous"])
            relation_ambiguous = relation_to_previous == "OR"
            if requirement_type == "UNKNOWN" or relation_ambiguous or not target_unit_id:
                coverage_status = "ESCALATED" if criticality == "CRITICAL" else "UNMAPPED"
                target_unit_ids: list[str] = []
                escalation_reason = (
                    "UNKNOWN_SEMANTICS_REVIEW_REQUIRED"
                    if requirement_type == "UNKNOWN"
                    else "ALTERNATIVE_OR_UNMAPPED_TARGET_REVIEW_REQUIRED"
                )
            else:
                coverage_status = "MAPPED"
                target_unit_ids = [target_unit_id]
                escalation_reason = ""
            span = {
                "source_field": str(_mapping(parent.get("source_span")).get("source_field") or "job_description_text"),
                "start_offset": int(clause["start_offset"]),
                "end_offset": int(clause["end_offset"]),
                "text_digest": _sha256({"text": " ".join(clause_text.lower().split())}),
            }
            span["span_digest"] = _sha256({"jd_hash": jd_hash, **span})
            seed = {
                "parent_requirement_id": parent_id,
                "ordinal": ordinal,
                "span_digest": span["span_digest"],
            }
            requirement_id = "l1cogreq-" + _sha256(seed).removeprefix("sha256:")[:16]
            requirements.append(
                {
                    "requirement_id": requirement_id,
                    "parent_requirement_id": parent_id,
                    "ordinal": ordinal,
                    "source_span": span,
                    "requirement_type": requirement_type,
                    "classification_rule_id": rule_id,
                    "extraction_confidence": confidence,
                    "criticality": criticality,
                    "modality": _modality(clause_text, source_kind),
                    "qualifiers": _qualifiers(clause_text),
                    "target_unit_ids": target_unit_ids,
                    "coverage_status": coverage_status,
                    "escalation_reason": escalation_reason,
                }
            )
            if ordinal > 1:
                relations.append(
                    {
                        "from_requirement_id": requirements[-2]["requirement_id"],
                        "to_requirement_id": requirement_id,
                        "relation": relation_to_previous,
                    }
                )
    requirements.sort(key=lambda row: str(row["requirement_id"]))
    relations.sort(
        key=lambda row: (str(row["from_requirement_id"]), str(row["to_requirement_id"]))
    )
    body = {
        "schema_version": "apps_rg.l1_atomic_requirement_graph.v1",
        "authority_class": _AUTHORITY_CLASS,
        "requirements": requirements,
        "relations": relations,
    }
    body["graph_digest"] = _sha256(body)
    return body


def _empty_atomic_requirement_graph() -> dict[str, Any]:
    body = {
        "schema_version": "apps_rg.l1_atomic_requirement_graph.v1",
        "authority_class": _AUTHORITY_CLASS,
        "requirements": [],
        "relations": [],
    }
    body["graph_digest"] = _sha256(body)
    return body


def _feasibility_graph(graph: Mapping[str, Any]) -> dict[str, Any]:
    options: list[dict[str, Any]] = []
    for requirement in graph["requirements"]:
        requirement_id = str(requirement["requirement_id"])
        targets = list(requirement["target_unit_ids"])
        if targets:
            option = {
                "requirement_id": requirement_id,
                "option_kind": "TARGET_WORK_UNIT",
                "work_unit_id": targets[0],
                "required_source_shape": ["candidate_support", "candidate_counterevidence"],
                "counterevidence_check_required": True,
                "coverage_status": "MAPPED",
                "rationale": "TYPE_AND_QUALIFIER_COMPATIBLE_TARGET",
            }
            option["option_id"] = "l1opt-" + _sha256(option).removeprefix("sha256:")[:16]
            options.append(option)
        escalation = {
            "requirement_id": requirement_id,
            "option_kind": "ESCALATE",
            "work_unit_id": "",
            "required_source_shape": [],
            "counterevidence_check_required": False,
            "coverage_status": "ESCALATED",
            "rationale": str(requirement.get("escalation_reason") or "ALTERNATIVE_SAFE_PATH"),
        }
        escalation["option_id"] = "l1opt-" + _sha256(escalation).removeprefix("sha256:")[:16]
        options.append(escalation)
    options.sort(key=lambda row: str(row["option_id"]))
    body = {
        "schema_version": "apps_rg.l1_feasibility_graph.v1",
        "authority_class": _AUTHORITY_CLASS,
        "options": options,
    }
    body["graph_digest"] = _sha256(body)
    return body


def _alternative_plan_ledger(
    graph: Mapping[str, Any], feasibility: Mapping[str, Any]
) -> dict[str, Any]:
    options_by_requirement: dict[str, list[Mapping[str, Any]]] = {}
    for option in feasibility["options"]:
        options_by_requirement.setdefault(str(option["requirement_id"]), []).append(option)
    decisions: list[dict[str, Any]] = []
    for requirement in graph["requirements"]:
        requirement_id = str(requirement["requirement_id"])
        options = sorted(
            options_by_requirement[requirement_id],
            key=lambda row: (row["option_kind"] != "TARGET_WORK_UNIT", str(row["option_id"])),
        )
        primary = options[0]
        alternative = options[1] if len(options) > 1 else None
        body = {
            "requirement_id": requirement_id,
            "primary_option_id": str(primary["option_id"]),
            "alternative_option_id": str(alternative["option_id"]) if alternative else "",
            "decision": str(primary["coverage_status"]),
            "rationale": str(primary["rationale"]),
            "risk": "COUNTEREVIDENCE_REQUIRED" if primary["option_kind"] == "TARGET_WORK_UNIT" else "SEMANTIC_REVIEW_REQUIRED",
        }
        body["decision_id"] = "l1decide-" + _sha256(body).removeprefix("sha256:")[:16]
        decisions.append(body)
    decisions.sort(key=lambda row: str(row["decision_id"]))
    body = {
        "schema_version": "apps_rg.l1_alternative_plan_ledger.v1",
        "authority_class": _AUTHORITY_CLASS,
        "decisions": decisions,
    }
    body["ledger_digest"] = _sha256(body)
    return body


def _critique_ledger(
    *,
    goal_frame: Mapping[str, Any],
    graph: Mapping[str, Any],
    alternatives: Mapping[str, Any],
) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    for requirement in graph["requirements"]:
        if requirement.get("criticality") != "CRITICAL":
            continue
        status = str(requirement["coverage_status"])
        if status != "MAPPED":
            finding = {
                "requirement_id": str(requirement["requirement_id"]),
                "severity": "HIGH",
                "code": "CRITICAL_REQUIREMENT_NOT_PRECISELY_TARGETED",
                "failed_invariant": "CRITICAL_REQUIREMENT_HAS_DEFENSIBLE_OPTION",
                "resolver": "HUMAN",
            }
            finding["finding_id"] = "l1crit-" + _sha256(finding).removeprefix("sha256:")[:16]
            findings.append(finding)
    for key in goal_frame["conflict_constraint_keys"]:
        finding = {
            "requirement_id": "",
            "severity": "HIGH",
            "code": "DECLARED_CONSTRAINT_CONFLICT",
            "failed_invariant": "CONFLICTING_CONSTRAINTS_REQUIRE_RESOLUTION",
            "resolver": "U0",
            "constraint_key": key,
        }
        finding["finding_id"] = "l1crit-" + _sha256(finding).removeprefix("sha256:")[:16]
        findings.append(finding)
    findings.sort(key=lambda row: str(row["finding_id"]))
    body = {
        "schema_version": "apps_rg.l1_critique_ledger.v1",
        "authority_class": _AUTHORITY_CLASS,
        "finding_count": len(findings),
        "findings": findings,
        "assertions": {
            "does_not_create_candidate_evidence": True,
            "does_not_resolve_conflicts": True,
            "does_not_select_route": True,
            "alternative_ledger_digest": str(alternatives["ledger_digest"]),
        },
    }
    body["ledger_digest"] = _sha256(body)
    return body


def _contains_forbidden_authority(value: Any) -> bool:
    if isinstance(value, Mapping):
        return any(
            str(key) in _FORBIDDEN_AUTHORITY_KEYS or _contains_forbidden_authority(item)
            for key, item in value.items()
        )
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_forbidden_authority(item) for item in value)
    return False


def _plan_body(
    *,
    app_payload: Mapping[str, Any],
    request_id: str,
    run_id: str,
    trace_id: str,
    replay_key: str,
    planning_profile_ref: str,
    planning_profile_digest: str,
) -> dict[str, Any]:
    try:
        v2 = build_apps_rg_l1_planning_capsule_v2(
            app_payload=app_payload,
            request_id=request_id,
            run_id=run_id,
            trace_id=trace_id,
            replay_key=replay_key,
            planning_profile_ref=planning_profile_ref,
            planning_profile_digest=planning_profile_digest,
        )
        verification = verify_apps_rg_l1_planning_capsule_v2(v2)
    except L1PlanningV2IntegrityError as exc:
        raise L1CognitivePlanError("v2 planning baseline is invalid") from exc
    jd_text, _source_field = _inline_jd_text(app_payload)
    taxonomy, taxonomy_ref, taxonomy_digest = _load_taxonomy()
    goal_frame = _goal_constraint_frame(app_payload)
    graph = (
        _atomic_requirement_graph(v2_capsule=v2, jd_text=jd_text, taxonomy=taxonomy)
        if jd_text
        else _empty_atomic_requirement_graph()
    )
    feasibility = _feasibility_graph(graph)
    alternatives = _alternative_plan_ledger(graph, feasibility)
    critique = _critique_ledger(
        goal_frame=goal_frame, graph=graph, alternatives=alternatives
    )
    if not jd_text:
        finding = {
            "requirement_id": "",
            "severity": "HIGH",
            "code": "JD_TEXT_NOT_AVAILABLE_FOR_COGNITIVE_PLAN",
            "failed_invariant": "COGNITIVE_PLAN_REQUIRES_U0_JD_TEXT",
            "resolver": "U0",
        }
        finding["finding_id"] = "l1crit-" + _sha256(finding).removeprefix("sha256:")[:16]
        critique["findings"] = [finding]
        critique["finding_count"] = 1
        critique["ledger_digest"] = _sha256(
            {key: value for key, value in critique.items() if key != "ledger_digest"}
        )
    body = {
        "schema_version": L1_COGNITIVE_V3_SCHEMA_VERSION,
        "authority_class": _AUTHORITY_CLASS,
        "app_scope": _APP_SCOPE,
        "request_id": _required_string(request_id, field="request_id"),
        "run_id": _required_string(run_id, field="run_id"),
        "trace_id": _required_string(trace_id, field="trace_id"),
        "replay_key": _required_string(replay_key, field="replay_key"),
        "v2_parent": {
            "capsule_digest": str(verification["capsule_digest"]),
            "schema_version": str(v2["schema_version"]),
        },
        "planning_priors": [
            {"ref": taxonomy_ref, "digest": taxonomy_digest, "authority_class": "PLANNING_PRIOR_ONLY"},
            {
                "ref": planning_profile_ref,
                "digest": planning_profile_digest,
                "authority_class": "PLANNING_PRIOR_ONLY",
            },
        ],
        "goal_constraint_frame": goal_frame,
        "atomic_requirement_graph": graph,
        "feasibility_graph": feasibility,
        "alternative_plan_ledger": alternatives,
        "critique_ledger": critique,
        "planning_status": "BLOCKED" if critique["findings"] else "READY",
        "validation": {
            "u0_payload_only": True,
            "no_route_selection": True,
            "no_evidence_retrieval": True,
            "no_prompt_assembly": True,
            "no_model_call": True,
            "no_tool_call": True,
            "no_l4_write": True,
            "no_candidate_evidence_claim": True,
        },
    }
    return body


def build_l1_cognitive_plan_v3(
    *,
    app_payload: Mapping[str, Any],
    request_id: str,
    run_id: str,
    trace_id: str,
    replay_key: str,
    planning_profile_ref: str,
    planning_profile_digest: str,
) -> FrozenDict:
    """Build an immutable v3 cognitive plan beside the v1/v2 projections."""

    plan = _plan_body(
        app_payload=app_payload,
        request_id=request_id,
        run_id=run_id,
        trace_id=trace_id,
        replay_key=replay_key,
        planning_profile_ref=planning_profile_ref,
        planning_profile_digest=planning_profile_digest,
    )
    plan["plan_digest"] = cognitive_plan_digest(plan)
    validate_l1_cognitive_plan_v3(plan)
    return _freeze(plan)


def validate_l1_cognitive_plan_v3(plan: Mapping[str, Any]) -> None:
    """Fail closed unless a v3 plan is source-bound, coherent, and advisory."""

    if not isinstance(plan, Mapping):
        raise L1CognitivePlanError("cognitive plan must be a mapping")
    if plan.get("schema_version") != L1_COGNITIVE_V3_SCHEMA_VERSION:
        raise L1CognitivePlanError("cognitive plan schema_version is invalid")
    if plan.get("authority_class") != _AUTHORITY_CLASS or plan.get("app_scope") != _APP_SCOPE:
        raise L1CognitivePlanError("cognitive plan authority is invalid")
    if plan.get("plan_digest") != cognitive_plan_digest(plan):
        raise L1CognitivePlanError("cognitive plan digest mismatch")
    if _contains_forbidden_authority(plan):
        raise L1CognitivePlanError("cognitive plan contains forbidden authority")
    graph = _mapping(plan.get("atomic_requirement_graph"))
    requirements = graph.get("requirements")
    if not isinstance(requirements, Sequence) or isinstance(requirements, (str, bytes)):
        raise L1CognitivePlanError("atomic requirement graph is invalid")
    ids: set[str] = set()
    for requirement in requirements:
        if not isinstance(requirement, Mapping):
            raise L1CognitivePlanError("atomic requirement is invalid")
        requirement_id = _required_string(requirement.get("requirement_id"), field="requirement_id")
        if requirement_id in ids:
            raise L1CognitivePlanError("atomic requirement IDs must be unique")
        ids.add(requirement_id)
        status = str(requirement.get("coverage_status") or "")
        if status not in _VALID_COVERAGE:
            raise L1CognitivePlanError("atomic requirement coverage is invalid")
        span = _mapping(requirement.get("source_span"))
        if not str(span.get("span_digest") or "").startswith("sha256:"):
            raise L1CognitivePlanError("atomic requirement must have a source span")
        if requirement.get("requirement_type") == "UNKNOWN" and status == "MAPPED":
            raise L1CognitivePlanError("unknown requirement cannot be silently mapped")
    critique = _mapping(plan.get("critique_ledger"))
    findings = critique.get("findings")
    if not isinstance(findings, Sequence) or isinstance(findings, (str, bytes)):
        raise L1CognitivePlanError("critique ledger is invalid")
    if not requirements and not any(
        _mapping(finding).get("code") == "JD_TEXT_NOT_AVAILABLE_FOR_COGNITIVE_PLAN"
        for finding in findings
    ):
        raise L1CognitivePlanError("empty cognitive plan must record missing U0 JD text")
    expected_status = "BLOCKED" if findings else "READY"
    if plan.get("planning_status") != expected_status:
        raise L1CognitivePlanError("cognitive planning status is invalid")


def build_l1_cognitive_revision_v3(
    *, plan: Mapping[str, Any], observed_outcomes: Sequence[Mapping[str, Any]]
) -> FrozenDict:
    """Produce one advisory delta from observed outcomes; never retry or execute."""

    validate_l1_cognitive_plan_v3(plan)
    requirement_ids = {
        str(row["requirement_id"])
        for row in plan["atomic_requirement_graph"]["requirements"]
    }
    changes: list[dict[str, Any]] = []
    for outcome in observed_outcomes:
        if not isinstance(outcome, Mapping):
            raise L1CognitivePlanError("observed outcome is invalid")
        requirement_id = _required_string(outcome.get("requirement_id"), field="outcome requirement_id")
        if requirement_id not in requirement_ids:
            raise L1CognitivePlanError("observed outcome is outside the cognitive plan")
        code = _required_string(outcome.get("code"), field="outcome code")
        if code not in _VALID_OBSERVED_OUTCOMES:
            raise L1CognitivePlanError("observed outcome code is invalid")
        observation_ref = _required_string(outcome.get("observation_ref"), field="observation_ref")
        change = {
            "requirement_id": requirement_id,
            "observed_outcome_code": code,
            "observation_ref": observation_ref,
            "action": "ESCALATE_AND_REPLAN_AFFECTED_REQUIREMENT",
            "automatic_retry": False,
            "route_change": False,
            "evidence_authority_change": False,
        }
        change["change_id"] = "l1rev-" + _sha256(change).removeprefix("sha256:")[:16]
        changes.append(change)
    changes.sort(key=lambda row: str(row["change_id"]))
    body = {
        "schema_version": L1_COGNITIVE_V3_REVISION_SCHEMA_VERSION,
        "authority_class": _AUTHORITY_CLASS,
        "app_scope": _APP_SCOPE,
        "parent_plan_digest": str(plan["plan_digest"]),
        "revision_scope_requirement_ids": sorted(
            {str(change["requirement_id"]) for change in changes}
        ),
        "changes": changes,
        "status": "PROPOSED" if changes else "NO_REVISION",
        "assertions": {
            "one_bounded_revision": True,
            "automatic_retry": False,
            "does_not_execute": True,
            "does_not_select_route": True,
            "does_not_create_evidence": True,
        },
    }
    body["revision_digest"] = cognitive_revision_digest(body)
    validate_l1_cognitive_revision_v3(body, plan=plan)
    return _freeze(body)


def validate_l1_cognitive_revision_v3(
    revision: Mapping[str, Any], *, plan: Mapping[str, Any]
) -> None:
    """Fail closed unless a revision is bounded to observed plan failures."""

    validate_l1_cognitive_plan_v3(plan)
    if not isinstance(revision, Mapping):
        raise L1CognitivePlanError("cognitive revision must be a mapping")
    if revision.get("schema_version") != L1_COGNITIVE_V3_REVISION_SCHEMA_VERSION:
        raise L1CognitivePlanError("cognitive revision schema_version is invalid")
    if revision.get("authority_class") != _AUTHORITY_CLASS or revision.get("app_scope") != _APP_SCOPE:
        raise L1CognitivePlanError("cognitive revision authority is invalid")
    if revision.get("revision_digest") != cognitive_revision_digest(revision):
        raise L1CognitivePlanError("cognitive revision digest mismatch")
    if revision.get("parent_plan_digest") != plan.get("plan_digest"):
        raise L1CognitivePlanError("cognitive revision parent plan is invalid")
    if _contains_forbidden_authority(revision):
        raise L1CognitivePlanError("cognitive revision contains forbidden authority")
    changes = revision.get("changes")
    if not isinstance(changes, Sequence) or isinstance(changes, (str, bytes)):
        raise L1CognitivePlanError("cognitive revision changes are invalid")
    scope = set(revision.get("revision_scope_requirement_ids") or ())
    if scope != {str(change.get("requirement_id") or "") for change in changes}:
        raise L1CognitivePlanError("cognitive revision scope is invalid")
    for change in changes:
        if not isinstance(change, Mapping):
            raise L1CognitivePlanError("cognitive revision change is invalid")
        if change.get("automatic_retry") is not False or change.get("route_change") is not False:
            raise L1CognitivePlanError("cognitive revision must remain advisory")


__all__ = [
    "L1CognitivePlanError",
    "L1_COGNITIVE_V3_REVISION_SCHEMA_VERSION",
    "L1_COGNITIVE_V3_SCHEMA_VERSION",
    "build_l1_cognitive_plan_v3",
    "build_l1_cognitive_revision_v3",
    "cognitive_plan_digest",
    "cognitive_revision_digest",
    "validate_l1_cognitive_plan_v3",
    "validate_l1_cognitive_revision_v3",
]
