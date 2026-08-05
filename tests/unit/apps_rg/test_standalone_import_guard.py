from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType

from apps_standalone_import_guard import ensure_external_agentic_core


def _clear_agentic_core_modules() -> dict[str, ModuleType]:
    saved: dict[str, ModuleType] = {}
    for name, module in tuple(sys.modules.items()):
        if name == "agentic_core" or name.startswith("agentic_core."):
            if isinstance(module, ModuleType):
                saved[name] = module
            del sys.modules[name]
    return saved


def test_incomplete_checkout_namespace_does_not_shadow_external_core(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo = tmp_path / "standalone"
    (repo / "agentic_core" / "prompt_governance" / "templates").mkdir(
        parents=True
    )
    external = tmp_path / "external"
    core = external / "agentic_core"
    core.mkdir(parents=True)
    (core / "__init__.py").write_text("SOURCE = 'external'\n", encoding="utf-8")

    saved_modules = _clear_agentic_core_modules()
    monkeypatch.setattr(sys, "path", [str(repo), str(external)])
    try:
        assert ensure_external_agentic_core(repository_root=repo) is True
        import agentic_core

        assert agentic_core.SOURCE == "external"
        assert Path(agentic_core.__file__).resolve() == (core / "__init__.py").resolve()
    finally:
        _clear_agentic_core_modules()
        sys.modules.update(saved_modules)


def test_guard_replaces_nested_incomplete_namespace_without_parent_key_error(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo = tmp_path / "standalone"
    (repo / "agentic_core" / "runtime").mkdir(parents=True)
    external = tmp_path / "external"
    core = external / "agentic_core"
    core.mkdir(parents=True)
    (core / "__init__.py").write_text("SOURCE = 'external'\n", encoding="utf-8")

    saved_modules = _clear_agentic_core_modules()
    monkeypatch.setattr(sys, "path", [str(repo)])
    try:
        import agentic_core.runtime  # noqa: F401

        sys.path.append(str(external))
        assert ensure_external_agentic_core(repository_root=repo) is True
        import agentic_core

        assert agentic_core.SOURCE == "external"
        assert Path(agentic_core.__file__).resolve() == (core / "__init__.py").resolve()
    finally:
        _clear_agentic_core_modules()
        sys.modules.update(saved_modules)


def test_guard_leaves_checkout_without_namespace_shadow_unchanged(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "standalone"
    repo.mkdir()

    assert ensure_external_agentic_core(repository_root=repo) is False
