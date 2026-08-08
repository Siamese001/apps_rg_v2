"""Canonical Apps RG product entry with an unavoidable signed preflight."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from apps_rg.runtime.runtime_proof_layout import (
    allocate_product_full_resume_artifact_dir,
    find_repo_root,
)


def _baseline_ref(repo_root: Path) -> Path:
    raw = Path(
        str(
            os.environ.get("APPS_RG_E2E_BASELINE_REF")
            or "apps_rg/config/e2e_baselines/anthropic_partnership.v1.json"
        )
    )
    return raw.resolve() if raw.is_absolute() else (repo_root / raw).resolve()


def _non_fresh_artifact_dir_result(artifact_dir: Path) -> dict[str, Any]:
    return {
        "exit_status": "error",
        "execution_status": "failed",
        "outcome_authorized": False,
        "product_authorized": False,
        "pipeline_complete": False,
        "observability_repair_required": False,
        "completion_status": "BLOCKED",
        "fault": "PRODUCT_ARTIFACT_DIR_NOT_FRESH",
        "completion_fault": "PRODUCT_ARTIFACT_DIR_NOT_FRESH",
        "artifact_dir": str(artifact_dir),
        "authority_contract_id": "apps_research_rg_e2e_authority",
    }


def _unsafe_artifact_dir_result(*, detail: str) -> dict[str, Any]:
    return {
        "exit_status": "error",
        "execution_status": "failed",
        "outcome_authorized": False,
        "product_authorized": False,
        "pipeline_complete": False,
        "observability_repair_required": False,
        "completion_status": "BLOCKED",
        "fault": "PRODUCT_ARTIFACT_DIR_UNSAFE",
        "completion_fault": "PRODUCT_ARTIFACT_DIR_UNSAFE",
        "artifact_dir_detail": detail,
        "authority_contract_id": "apps_research_rg_e2e_authority",
    }


def _runtime_dependency_blocked_result(
    *, artifact_dir: Path, dependency_receipt_path: Path, dependency_receipt: dict[str, Any]
) -> dict[str, Any]:
    """Fail closed before preflight when the excluded core runtime is unavailable."""

    dependency_status = str(dependency_receipt.get("status") or "UNKNOWN")
    return {
        "exit_status": "error",
        "execution_status": "failed",
        "outcome_authorized": False,
        "product_authorized": False,
        "pipeline_complete": False,
        "observability_repair_required": False,
        "completion_status": "BLOCKED",
        "fault": "STANDALONE_RUNTIME_DEPENDENCY_UNAVAILABLE",
        "completion_fault": "STANDALONE_RUNTIME_DEPENDENCY_UNAVAILABLE",
        "artifact_dir": str(artifact_dir),
        "standalone_runtime_dependency_receipt": str(dependency_receipt_path),
        "standalone_runtime_dependency_status": dependency_status,
        "authority_contract_id": "apps_research_rg_e2e_authority",
    }


def _input_bundle_blocked_result(*, artifact_dir: Path, detail: str) -> dict[str, Any]:
    return {
        "exit_status": "error",
        "execution_status": "failed",
        "outcome_authorized": False,
        "product_authorized": False,
        "pipeline_complete": False,
        "observability_repair_required": False,
        "completion_status": "BLOCKED",
        "fault": "PRODUCT_INPUT_REFERENCE_REJECTED",
        "completion_fault": "PRODUCT_INPUT_REFERENCE_REJECTED",
        "input_validation_detail": detail,
        "artifact_dir": str(artifact_dir),
        "authority_contract_id": "apps_research_rg_e2e_authority",
    }


def run_product_whole_run_from_primitives(
    *,
    target_company: str,
    target_role: str,
    target_level: str = "",
    jd: str = "",
    job_description_ref: str = "",
    job_description_text: str = "",
    manual_brief: str = "",
    resume_path: str = "",
    source_resume_text: str = "",
    generation_mode: str = "strategic_tailor",
    artifact_dir: str = "",
) -> dict[str, Any]:
    """Run preflight and the only product-authorizing whole-run orchestrator."""

    repo = find_repo_root()
    try:
        art = allocate_product_full_resume_artifact_dir(repo, artifact_dir)
    except ValueError as exc:
        return _unsafe_artifact_dir_result(detail=str(exc))
    if art.exists() and any(art.iterdir()):
        return _non_fresh_artifact_dir_result(art)
    art.mkdir(parents=True, exist_ok=True)

    from apps_rg.runtime.immutable_input_bundle import (
        ProductInputBundleError,
        freeze_product_inputs,
    )

    try:
        inputs = freeze_product_inputs(
            artifact_dir=art,
            source_resume_text=source_resume_text,
            source_resume_ref=resume_path,
            jd=jd,
            job_description_text=job_description_text,
            job_description_ref=job_description_ref,
            manual_brief=manual_brief,
        )
    except ProductInputBundleError as exc:
        return _input_bundle_blocked_result(artifact_dir=art, detail=str(exc))

    from apps_rg.runtime.standalone_dependency_posture import (
        EXTERNAL_RUNTIME_BOUND,
        verify_external_agentic_core_runtime,
        write_standalone_runtime_dependency_receipt,
    )

    dependency_receipt = verify_external_agentic_core_runtime(repo_root=repo)
    dependency_receipt_path = write_standalone_runtime_dependency_receipt(
        artifact_dir=art,
        receipt=dependency_receipt,
    )
    if dependency_receipt.get("status") != EXTERNAL_RUNTIME_BOUND:
        result = _runtime_dependency_blocked_result(
            artifact_dir=art,
            dependency_receipt_path=dependency_receipt_path,
            dependency_receipt=dependency_receipt,
        )
        result["validated_input_bundle_ref"] = str(inputs.manifest_path)
        result["validated_input_bundle_digest"] = inputs.digest
        return result

    from apps_rg.runtime.e2e_preflight import (
        E2E_PREFLIGHT_CONTINUATION_RECEIPT_FILENAME,
        run_fresh_e2e_preflight,
    )
    from apps_rg.runtime.live_judge_only_guard import assert_production_runtime

    preflight = run_fresh_e2e_preflight(
        artifact_dir=art,
        e2e_run_id=art.name,
        repo_root=repo,
        baseline_ref=_baseline_ref(repo),
        runtime_check=lambda: assert_production_runtime(
            context="apps_rg product dispatch"
        ),
    )
    if not preflight.passed:
        result = dict(preflight.result)
        result.setdefault("product_authorized", False)
        result.setdefault("pipeline_complete", False)
        result.setdefault("observability_repair_required", False)
        result["authority_contract_id"] = "apps_research_rg_e2e_authority"
        result["validated_input_bundle_ref"] = str(inputs.manifest_path)
        result["validated_input_bundle_digest"] = inputs.digest
        return result

    from apps_rg.runtime.orchestration.r3r4_whole_run_orchestration import (
        run_whole_run_with_route_governance,
    )

    envelope_env = "APPS_RG_WHOLE_RUN_ENVELOPE"
    prior_envelope = os.environ.get(envelope_env)
    os.environ[envelope_env] = "1"
    try:
        result = run_whole_run_with_route_governance(
            target_company=target_company,
            target_role=target_role,
            target_level=target_level,
            jd=inputs.job_description_text,
            job_description_ref="",
            job_description_text=inputs.job_description_text,
            manual_brief=inputs.manual_brief_ref,
            resume_path="",
            source_resume_text=inputs.source_resume_text,
            generation_mode=generation_mode,
            artifact_dir=str(art),
            validated_input_bundle_ref=str(inputs.manifest_path),
            validated_input_bundle_digest=inputs.digest,
            preflight_continuation_ref=str(
                art / E2E_PREFLIGHT_CONTINUATION_RECEIPT_FILENAME
            ),
            require_fresh_preflight=True,
        )
    finally:
        if prior_envelope is None:
            os.environ.pop(envelope_env, None)
        else:
            os.environ[envelope_env] = prior_envelope
    result["authority_contract_id"] = "apps_research_rg_e2e_authority"
    result["validated_input_bundle_ref"] = str(inputs.manifest_path)
    result["validated_input_bundle_digest"] = inputs.digest
    return result


__all__ = ["run_product_whole_run_from_primitives"]
