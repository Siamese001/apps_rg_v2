"""Resolve app-owned files in monorepo and standalone source layouts."""

from __future__ import annotations

from pathlib import Path


def apps_rg_package_root(repo_root: Path | None = None) -> Path:
    """Return the filesystem root of the ``apps_rg`` package.

    The production monorepo stores the package at ``apps_rg`` while the
    standalone repository uses the conventional ``src/apps_rg`` layout.  A
    caller may also pass the standalone ``src`` directory directly.
    """

    if repo_root is None:
        return Path(__file__).resolve().parent

    root = Path(repo_root)
    if root.name == "apps_rg" and (root / "__init__.py").is_file():
        return root

    for candidate in (root / "apps_rg", root / "src" / "apps_rg"):
        if candidate.is_dir():
            return candidate

    # Preserve the historical monorepo-shaped error path when the repository
    # itself is missing or malformed; callers will then fail closed on access.
    return root / "apps_rg"


def resolve_apps_rg_path(repo_root: Path | None, *parts: str) -> Path:
    """Resolve ``parts`` beneath the package root for the active layout."""

    return apps_rg_package_root(repo_root).joinpath(*parts)
