"""Lane hooks: RuntimeExhaustBundle after Exit, before L6 shadow (Wave 7)."""
from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path
from typing import Any, Iterator

from apps_rg.runtime.failure_evidence import atomic_write_json

from apps_rg.runtime.section_runtime_exhaust_spine_receipt import (
    assert_section_l6_may_consume_exhaust,
    emit_section_runtime_exhaust_spine_artifacts,
)

_CORE_RUNTIME_CALLBACK_ACTIVE: ContextVar[bool] = ContextVar(
    "apps_rg_core_runtime_callback_active",
    default=False,
)


@contextmanager
def core_runtime_callback_scope() -> Iterator[None]:
    """Mark only the dynamic extent in which core may still rewrite receipts."""

    token = _CORE_RUNTIME_CALLBACK_ACTIVE.set(True)
    try:
        yield
    finally:
        _CORE_RUNTIME_CALLBACK_ACTIVE.reset(token)


def core_runtime_callback_active() -> bool:
    return _CORE_RUNTIME_CALLBACK_ACTIVE.get()


def finalize_section_runtime_exhaust_before_l6(
    artifact_dir: Path,
    section_id: str,
    runtime_payload: dict[str, Any],
    *,
    repo_root: Path,
) -> dict[str, Path]:
    """After ExitDispositionReceipt — emit exhaust bundle + handoff receipt; gate L6."""
    paths = emit_section_runtime_exhaust_spine_artifacts(
        artifact_dir,
        section_id=section_id,
        runtime_payload=runtime_payload,
        repo_root=repo_root,
    )
    # A section lane runs inside the pinned core L2 callback.  Core L5 is only
    # sealed after that callback returns, so running L6 here would permanently
    # record a false L5-missing failure.  Defer exactly this nested-core case;
    # the app-owned spine seam resumes it immediately after core closeout.
    core_in_progress = core_runtime_callback_active()
    if core_in_progress:
        deferred = artifact_dir / "l6_deferred_until_core_certification.json"
        atomic_write_json(
            deferred,
            {
                "schema_version": "apps_rg.l6_deferred_until_core_certification.v1",
                "status": "DEFERRED",
                "section_id": section_id,
                "run_id": str(runtime_payload.get("run_id") or ""),
                "reason": "PINNED_CORE_L5_NOT_YET_SEALED",
                "resume_boundary": "post_core_runtime_authority",
                "current_run_mutated": False,
            },
        )
        paths["l6_deferred_until_core_certification"] = deferred
        return paths

    from apps_rg.runtime.spine.l6_shadow_eval_runner import (
        maybe_run_l6_v40_shadow_eval_for_section,
    )

    l6_paths = maybe_run_l6_v40_shadow_eval_for_section(
        artifact_dir,
        section_id=section_id,
        repo_root=repo_root,
        session_id=str(runtime_payload.get("session_id") or ""),
        tenant_id=str(runtime_payload.get("tenant_id") or ""),
        l5_certification_ref=str(runtime_payload.get("l5_certification_ref") or ""),
    )
    product_visible = bool(runtime_payload.get("product_visible", True))
    if product_visible and not l6_paths:
        raise RuntimeError(
            "product-visible apps_rg section runtime requires L6 v40 shadow eval output; "
            "set APPS_RG_L6_V40_SHADOW_EVAL_SKIP only for explicit local-dev waivers"
        )
    paths.update(l6_paths)
    return paths


def finalize_deferred_section_l6_after_core(
    artifact_dir: Path,
    *,
    repo_root: Path,
) -> dict[str, Path]:
    """Resume a nested section's L6 only after core L5 is byte-sealed."""

    artifact_dir = Path(artifact_dir).resolve()
    deferred = artifact_dir / "l6_deferred_until_core_certification.json"
    if not deferred.is_file():
        return {}
    import json

    runtime_payload = json.loads((artifact_dir / "runtime_payload.json").read_text(encoding="utf-8"))
    if not isinstance(runtime_payload, dict):
        raise RuntimeError("deferred L6 runtime payload is not an object")
    section_id = str(runtime_payload.get("section_id") or artifact_dir.name).strip()
    from apps_rg.runtime.spine.l6_shadow_eval_runner import (
        emit_l5_certification_receipt_from_core,
        maybe_run_l6_v40_shadow_eval_for_section,
    )

    l5_path = emit_l5_certification_receipt_from_core(
        artifact_dir=artifact_dir,
        repo_root=repo_root,
    )
    paths = maybe_run_l6_v40_shadow_eval_for_section(
        artifact_dir,
        section_id=section_id,
        repo_root=repo_root,
        l5_certification_ref=l5_path.name,
    )
    if not paths:
        raise RuntimeError("deferred product-visible section L6 did not execute")
    atomic_write_json(
        deferred,
        {
            "schema_version": "apps_rg.l6_deferred_until_core_certification.v1",
            "status": "RESUMED",
            "section_id": section_id,
            "run_id": str(runtime_payload.get("run_id") or ""),
            "reason": "PINNED_CORE_L5_SEALED",
            "resume_boundary": "post_core_runtime_authority",
            "l5_certification_ref": l5_path.name,
            "current_run_mutated": False,
        },
    )
    return {"l5_certification_receipt": l5_path, **paths}


def gate_section_l6_shadow_after_exhaust(
    artifact_dir: Path,
    runtime_payload: dict[str, Any],
) -> None:
    """Call immediately before build_l6_shadow_package."""
    assert_section_l6_may_consume_exhaust(runtime_payload, artifact_dir)


__all__ = [
    "finalize_section_runtime_exhaust_before_l6",
    "finalize_deferred_section_l6_after_core",
    "core_runtime_callback_active",
    "core_runtime_callback_scope",
    "gate_section_l6_shadow_after_exhaust",
]
