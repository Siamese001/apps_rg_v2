"""AST ratchet for direct shared-core imports in standalone app source."""

from __future__ import annotations

import ast
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Final


CORE_IMPORT_BOUNDARY_SCHEMA_VERSION: Final[str] = "apps.core_import_boundary.v1"
CORE_IMPORT_BOUNDARY_CONTRACT_RELPATH: Final[Path] = Path(
    "config/contracts/apps_core_import_boundary.v1.json"
)


class CoreImportBoundaryError(RuntimeError):
    """Raised when source bypasses an approved shared-core boundary."""


@dataclass(frozen=True)
class CoreImportRecord:
    path: str
    module: str
    line: int

    @property
    def is_contract(self) -> bool:
        return self.module.startswith("agentic_core.runtime.contracts")


def _literal_import_module(node: ast.Call) -> str | None:
    if not node.args or not isinstance(node.args[0], ast.Constant):
        return None
    value = node.args[0].value
    if not isinstance(value, str) or not value.startswith("agentic_core"):
        return None
    function = node.func
    if isinstance(function, ast.Attribute) and function.attr == "import_module":
        return value
    if isinstance(function, ast.Name) and function.id == "import_module":
        return value
    return None


def scan_core_imports(source_root: Path) -> list[CoreImportRecord]:
    """Return direct imports, including literal dynamic imports, without importing source."""

    root = Path(source_root).resolve()
    repo = root.parent if root.name == "src" else root
    records: list[CoreImportRecord] = []
    for path in sorted(root.rglob("*.py")):
        relative = path.resolve().relative_to(repo).as_posix()
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if module == "agentic_core" or module.startswith("agentic_core."):
                    records.append(CoreImportRecord(relative, module, node.lineno))
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "agentic_core" or alias.name.startswith("agentic_core."):
                        records.append(CoreImportRecord(relative, alias.name, node.lineno))
            elif isinstance(node, ast.Call):
                module = _literal_import_module(node)
                if module is not None:
                    records.append(CoreImportRecord(relative, module, node.lineno))
    return sorted(records, key=lambda row: (row.path, row.line, row.module))


def _read_policy(contract_path: Path) -> dict[str, Any]:
    try:
        policy = json.loads(Path(contract_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CoreImportBoundaryError("core import boundary contract is unreadable") from exc
    approved = policy.get("approved_core_boundary_modules")
    if (
        policy.get("schema_version") != CORE_IMPORT_BOUNDARY_SCHEMA_VERSION
        or not isinstance(approved, Sequence)
        or isinstance(approved, (str, bytes))
        or any(not isinstance(path, str) or not path.startswith("src/") for path in approved)
        or len(set(approved)) != len(approved)
    ):
        raise CoreImportBoundaryError("core import boundary contract is invalid")
    return policy


def boundary_violations(
    records: Sequence[CoreImportRecord], policy: Mapping[str, Any]
) -> dict[str, list[str]]:
    """Compare an AST inventory with the exact approved boundary set."""

    approved = set(policy["approved_core_boundary_modules"])
    facade = str(policy["apps_rg_contract_facade"])
    concrete_paths = {record.path for record in records if not record.is_contract}
    contract_paths = {
        record.path
        for record in records
        if record.is_contract and record.path.startswith("src/apps_rg/")
    }
    return {
        "unauthorized_concrete_import_files": sorted(concrete_paths - approved),
        "stale_approved_boundary_files": sorted(approved - concrete_paths),
        "apps_rg_contract_facade_bypasses": sorted(contract_paths - {facade}),
    }


def validate_core_import_boundary(
    repo_root: Path, *, contract_path: Path | None = None
) -> dict[str, Any]:
    """Validate current source and return the complete W6 inventory evidence."""

    repo = Path(repo_root).resolve()
    path = contract_path or repo / CORE_IMPORT_BOUNDARY_CONTRACT_RELPATH
    policy = _read_policy(path)
    records = scan_core_imports(repo / "src")
    violations = boundary_violations(records, policy)
    if any(violations.values()):
        raise CoreImportBoundaryError(
            "core import boundary violation: " + json.dumps(violations, sort_keys=True)
        )
    concrete_files = sorted({record.path for record in records if not record.is_contract})
    return {
        "schema_version": CORE_IMPORT_BOUNDARY_SCHEMA_VERSION,
        "historical_static_direct_concrete_import_files": policy["historical_inventory"][
            "direct_concrete_import_files_before_w6"
        ],
        "additional_literal_dynamic_import_files": policy["historical_inventory"][
            "literal_dynamic_import_files_discovered_by_w6"
        ],
        "effective_historical_direct_concrete_import_files": policy["historical_inventory"][
            "effective_direct_concrete_import_files_before_w6"
        ],
        "current_approved_direct_concrete_import_files": len(concrete_files),
        "migrated_direct_concrete_import_files": (
            policy["historical_inventory"][
                "effective_direct_concrete_import_files_before_w6"
            ]
            - len(concrete_files)
        ),
        "approved_core_boundary_modules": concrete_files,
        "apps_rg_contract_facade": policy["apps_rg_contract_facade"],
    }


__all__ = [
    "CORE_IMPORT_BOUNDARY_CONTRACT_RELPATH",
    "CORE_IMPORT_BOUNDARY_SCHEMA_VERSION",
    "CoreImportBoundaryError",
    "CoreImportRecord",
    "boundary_violations",
    "scan_core_imports",
    "validate_core_import_boundary",
]
