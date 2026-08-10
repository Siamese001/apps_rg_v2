"""apps_rg boundary for the integrated single-action spine runner."""

from __future__ import annotations

from dataclasses import is_dataclass, replace
from importlib import import_module
from pathlib import Path
from typing import Any

from apps_rg.repository_layout import resolve_apps_rg_path


def _load_apps_rg_route_id() -> str:
    """Resolve the app route without relying on monorepo-shaped cwd lookup."""

    import yaml

    path = resolve_apps_rg_path(None, "config", "route_registry.yaml")
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, TypeError, ValueError, yaml.YAMLError):
        return ""
    routes = payload.get("routes") if isinstance(payload, dict) else None
    if not isinstance(routes, list):
        return ""
    candidates = [row for row in routes if isinstance(row, dict)]
    if not candidates:
        return ""

    def priority(row: dict[str, Any]) -> int:
        try:
            return int(row.get("priority", 9999))
        except (TypeError, ValueError):
            return 9999

    return str(min(candidates, key=priority).get("route_id") or "").strip()


def run_integrated_single_action_spine(*args: Any, **kwargs: Any) -> Any:
    """Delegate to the current integrated spine runner behind an app-owned seam."""
    if (
        str(kwargs.get("app_name") or "") == "apps_rg"
        and not str(kwargs.get("route_id") or "").strip()
    ):
        route_id = _load_apps_rg_route_id()
        if route_id:
            kwargs["route_id"] = route_id
    mod = import_module(
        "agentic_core.runtime.entrypoints.integrated_single_action_spine_run"
    )
    runner = getattr(mod, "run_integrated_single_action_spine")
    from apps_rg.runtime.orchestration.core_runtime_producer_adapter import (
        adapt_pinned_core_w2_producer,
    )
    from apps_rg.runtime.section_runtime_exhaust_lane_integration import (
        core_runtime_callback_scope,
    )
    from apps_rg.runtime.orchestration.canonical_identity_context import (
        canonical_run_identity_scope,
        current_canonical_run_identity,
    )

    requested_runtime_mode = "fixture" if kwargs.get("_test_mode") else "production"
    raw_request = kwargs.get("raw_request")
    canonical_identity = (
        raw_request.get("canonical_run_identity")
        if isinstance(raw_request, dict)
        else None
    )
    if canonical_identity is None:
        canonical_identity = current_canonical_run_identity() or None
    with adapt_pinned_core_w2_producer(
        mod,
        requested_runtime_mode=requested_runtime_mode,
    ):
        with canonical_run_identity_scope(canonical_identity):
            with core_runtime_callback_scope():
                result = runner(*args, **kwargs)
    artifact_raw = kwargs.get("artifact_dir")
    if artifact_raw is None:
        return result
    artifact_dir = Path(artifact_raw).resolve()
    # Test doubles that do not emit the core bundle remain outside this
    # authority adapter. A real core run always emits the witness.
    if not (artifact_dir / "runtime_execution_witness.json").is_file():
        return result
    from apps_rg.runtime.orchestration.core_runtime_authority import (
        emit_core_runtime_authority,
    )

    authority = emit_core_runtime_authority(artifact_dir)
    from apps_rg.repository_layout import repository_root
    from apps_rg.runtime.section_runtime_exhaust_lane_integration import (
        finalize_deferred_section_l6_after_core,
    )

    finalize_deferred_section_l6_after_core(
        artifact_dir,
        repo_root=repository_root(Path(__file__)),
    )
    normalized = authority.get("normalized_contract") or {}
    x3 = normalized.get("x3") if isinstance(normalized, dict) else {}
    canonical_x3 = str(x3.get("x3_disposition") or "") if isinstance(x3, dict) else ""
    if is_dataclass(result) and canonical_x3:
        result = replace(result, x3_disposition=canonical_x3)
    return result


__all__ = ["run_integrated_single_action_spine"]
