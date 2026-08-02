"""apps_rg boundary for the integrated single-action spine runner."""

from __future__ import annotations

from importlib import import_module
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
    if str(kwargs.get("app_name") or "") == "apps_rg" and not str(
        kwargs.get("route_id") or ""
    ).strip():
        route_id = _load_apps_rg_route_id()
        if route_id:
            kwargs["route_id"] = route_id
    mod = import_module(
        "agentic_core.runtime.entrypoints.integrated_single_action_spine_run"
    )
    runner = getattr(mod, "run_integrated_single_action_spine")
    return runner(*args, **kwargs)


__all__ = ["run_integrated_single_action_spine"]
