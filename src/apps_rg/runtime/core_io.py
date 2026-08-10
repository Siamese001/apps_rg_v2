"""Approved apps_rg boundary for the shared-core durable write gateway.

The shared core imports selected app modules while its package is initializing.
Resolving ``write_gateway`` eagerly here therefore creates a cycle whenever one
of those app modules imports this boundary.  Keep the public module-like object
stable, but resolve the external dependency only on its first operation.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any


class _LazyWriteGateway:
    """Proxy the core gateway without importing the core during app bootstrap."""

    def __init__(self) -> None:
        self._target: Any | None = None

    def _resolve(self) -> Any:
        target = self._target
        if target is None:
            target = import_module("agentic_core.L2_execution.utils.write_gateway")
            self._target = target
        return target

    def __getattr__(self, name: str) -> Any:
        return getattr(self._resolve(), name)


write_gateway = _LazyWriteGateway()

__all__ = ["write_gateway"]
