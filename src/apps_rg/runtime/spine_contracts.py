"""Verified spine contract facade for apps_rg.

apps_rg code should import spine contract types through this module during the
lean-core migration. This facade re-exports only symbols verified in
docs/reports/apps_rg/apps_rg_contract_symbol_inventory.md.

Do not add aliases for missing contracts. Missing contracts require an explicit
spine owner decision or a clearly non-canonical app-local migration protocol.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any, Final


_CONTRACTS = "agentic_core.runtime.contracts"
_SYMBOL_BINDINGS: Final[dict[str, tuple[str, str | None]]] = {
    "ALLOWED_PROMPT_SLOT_C0_EVIDENCE_DATA_ONLY": (
        f"{_CONTRACTS}.final_evidence_contract",
        "ALLOWED_PROMPT_SLOT_C0_EVIDENCE_DATA_ONLY",
    ),
    "AppsRgIngressPayload": (f"{_CONTRACTS}.apps_rg_ingress_payload", "AppsRgIngressPayload"),
    "CompiledPromptArtifact": (
        f"{_CONTRACTS}.compiled_prompt_artifact",
        "CompiledPromptArtifact",
    ),
    "EvidenceItem": (f"{_CONTRACTS}.final_evidence_contract", "EvidenceItem"),
    "FinalEvidenceContract": (
        f"{_CONTRACTS}.final_evidence_contract",
        "FinalEvidenceContract",
    ),
    "GraphTraversePolicy": (f"{_CONTRACTS}.route_contract", "GraphTraversePolicy"),
    "L1PlanContract": (f"{_CONTRACTS}.l1_plan_contract", "L1PlanContract"),
    "L3_RUNTIME_RECEIPT_SCHEMA_VERSION": (
        f"{_CONTRACTS}.l3_runtime_orchestration_receipt",
        "L3_RUNTIME_RECEIPT_SCHEMA_VERSION",
    ),
    "L3RuntimeOrchestrationReceipt": (
        f"{_CONTRACTS}.l3_runtime_orchestration_receipt",
        "L3RuntimeOrchestrationReceipt",
    ),
    "L3StepContractRef": (
        f"{_CONTRACTS}.l3_runtime_orchestration_receipt",
        "L3StepContractRef",
    ),
    "L3ToL2StepContract": (f"{_CONTRACTS}.l3_to_l2_step_contract", "L3ToL2StepContract"),
    "Origin": (f"{_CONTRACTS}.origin", "Origin"),
    "PackageValidationReceipt": (
        f"{_CONTRACTS}.runtime_customization_package",
        "PackageValidationReceipt",
    ),
    "PromptBlock": (f"{_CONTRACTS}.compiled_prompt_artifact", "PromptBlock"),
    "RequestEnvelope": (f"{_CONTRACTS}.apps_rg_ingress_payload", "RequestEnvelope"),
    "RouteContract": (f"{_CONTRACTS}.route_contract", "RouteContract"),
    "RouteGateReceipt": (f"{_CONTRACTS}.route_gate_receipt", "RouteGateReceipt"),
    "RuntimeCustomizationPackage": (
        f"{_CONTRACTS}.runtime_customization_package",
        "RuntimeCustomizationPackage",
    ),
    "RuntimePosture": (f"{_CONTRACTS}.posture", "RuntimePosture"),
    "SealedL2Artifact": (f"{_CONTRACTS}.sealed_l2_artifact", "SealedL2Artifact"),
    "ValidatedRequest": (f"{_CONTRACTS}.apps_rg_ingress_payload", "ValidatedRequest"),
    "X3Disposition": (f"{_CONTRACTS}.x3_disposition", "X3Disposition"),
    "compute_l3_runtime_digest": (
        f"{_CONTRACTS}.l3_runtime_orchestration_receipt",
        "compute_l3_runtime_digest",
    ),
    "lifecycle_trace_contract": (f"{_CONTRACTS}.lifecycle_trace_contract", None),
}
for _status_name in (
    "STATUS_NOT_APPLICABLE",
    "STATUS_UNKNOWN",
    "SUPPORT_STATUS_BLOCKED",
    "SUPPORT_STATUS_CONFLICTED",
    "SUPPORT_STATUS_EMPTY",
    "SUPPORT_STATUS_PARTIAL",
    "SUPPORT_STATUS_PASS",
    "SUPPORT_STATUS_PASSING_VALUES",
    "SUPPORT_STATUS_WEAK",
    "SUPPORT_STATUS_WEAK_WITH_CAVEATS",
):
    _SYMBOL_BINDINGS[_status_name] = (f"{_CONTRACTS}.final_evidence_contract", _status_name)


def __getattr__(name: str) -> Any:
    """Resolve one canonical contract at a time to avoid core/app import cycles."""

    try:
        module_name, attribute = _SYMBOL_BINDINGS[name]
    except KeyError as exc:
        raise AttributeError(name) from exc
    module = import_module(module_name)
    value = module if attribute is None else getattr(module, attribute)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))

__all__ = sorted(_SYMBOL_BINDINGS)
