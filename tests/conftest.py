"""Repository-wide pytest isolation for generated runtime caches."""

from __future__ import annotations

import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def _isolate_runtime_cache_root(
    tmp_path_factory: pytest.TempPathFactory,
) -> None:
    """Never let a test create the default repository-owned R1B cache."""
    env_name = "APPS_RG_R1B_CACHE_ROOT"
    previous = os.environ.get(env_name)
    os.environ[env_name] = str(tmp_path_factory.mktemp("apps_rg_runtime_cache"))
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop(env_name, None)
        else:
            os.environ[env_name] = previous
