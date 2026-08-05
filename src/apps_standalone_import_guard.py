"""Protect standalone Apps packages from an incomplete local core namespace.

The standalone checkout intentionally does not vendor ``agentic_core``.  A
directory left at the checkout root for templates can nevertheless be treated
by Python as a namespace package and shadow the editable core dependency.  The
guard imports the real dependency while the checkout root is temporarily
hidden, then restores the original import path unchanged.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path
from types import ModuleType


def _resolves_to(path_entry: str, target: Path) -> bool:
    try:
        return Path(path_entry or ".").resolve() == target.resolve()
    except OSError:
        return False


def _is_local_namespace(module: ModuleType, local_core: Path) -> bool:
    if getattr(module, "__file__", None):
        return False
    module_paths = getattr(module, "__path__", ())
    return any(_resolves_to(str(entry), local_core) for entry in module_paths)


def ensure_external_agentic_core(*, repository_root: Path | None = None) -> bool:
    """Load the editable core before a root-level namespace can shadow it.

    Returns ``True`` only when this guard had to resolve an incomplete local
    namespace and successfully loaded a regular external ``agentic_core``
    package.  It intentionally leaves a valid preloaded core untouched.
    """

    repo = (repository_root or Path(__file__).resolve().parent.parent).resolve()
    local_core = repo / "agentic_core"
    if not local_core.is_dir() or (local_core / "__init__.py").is_file():
        return False

    existing = sys.modules.get("agentic_core")
    if isinstance(existing, ModuleType) and getattr(existing, "__file__", None):
        return False

    original_path = list(sys.path)
    original_modules: dict[str, ModuleType] = {}
    for name, module in tuple(sys.modules.items()):
        if not name.startswith("agentic_core") or not isinstance(module, ModuleType):
            continue
        if _is_local_namespace(module, local_core):
            original_modules[name] = module
    # Do not delete while iterating: a nested namespace's lazy ``__path__``
    # resolves through its parent package and raises KeyError if that parent
    # has already been removed from sys.modules.
    for name in original_modules:
        sys.modules.pop(name, None)

    sys.path[:] = [
        entry for entry in original_path if not _resolves_to(str(entry), repo)
    ]
    importlib.invalidate_caches()
    try:
        resolved = importlib.import_module("agentic_core")
    except ImportError:
        for name in tuple(sys.modules):
            if name.startswith("agentic_core") and name not in original_modules:
                del sys.modules[name]
        sys.modules.update(original_modules)
        return False
    finally:
        sys.path[:] = original_path

    if getattr(resolved, "__file__", None):
        return True

    # Do not leave a different incomplete namespace cached if no regular core
    # dependency was available.
    for name in tuple(sys.modules):
        if name.startswith("agentic_core") and name not in original_modules:
            del sys.modules[name]
    sys.modules.update(original_modules)
    return False


__all__ = ["ensure_external_agentic_core"]
