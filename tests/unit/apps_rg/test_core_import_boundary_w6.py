from __future__ import annotations

import ast
import json
from pathlib import Path

from apps_rg.runtime.core_import_boundary import (
    CORE_IMPORT_BOUNDARY_CONTRACT_RELPATH,
    CoreImportRecord,
    boundary_violations,
    scan_core_imports,
    validate_core_import_boundary,
)


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_repository_core_import_boundary_is_exact_and_reduced() -> None:
    evidence = validate_core_import_boundary(REPO_ROOT)

    assert evidence["historical_static_direct_concrete_import_files"] == 83
    assert evidence["additional_literal_dynamic_import_files"] == 1
    assert evidence["effective_historical_direct_concrete_import_files"] == 84
    assert evidence["current_approved_direct_concrete_import_files"] == 55
    assert evidence["migrated_direct_concrete_import_files"] == 29
    assert evidence["apps_rg_contract_facade"] == "src/apps_rg/runtime/spine_contracts.py"


def test_boundary_rejects_new_static_and_literal_dynamic_imports(tmp_path: Path) -> None:
    src = tmp_path / "src"
    module = src / "apps_rg" / "new_direct_import.py"
    module.parent.mkdir(parents=True)
    module.write_text(
        "import agentic_core.knowledge.retrieval\n"
        "import importlib\n"
        "importlib.import_module('agentic_core.runtime.providers.provider_gateway')\n",
        encoding="utf-8",
    )
    records = scan_core_imports(src)
    policy = {
        "apps_rg_contract_facade": "src/apps_rg/runtime/spine_contracts.py",
        "approved_core_boundary_modules": [],
    }

    violations = boundary_violations(records, policy)

    assert violations["unauthorized_concrete_import_files"] == [
        "src/apps_rg/new_direct_import.py"
    ]


def test_boundary_contract_has_no_duplicate_or_missing_approved_paths() -> None:
    policy = json.loads(
        (REPO_ROOT / CORE_IMPORT_BOUNDARY_CONTRACT_RELPATH).read_text(encoding="utf-8")
    )
    approved = policy["approved_core_boundary_modules"]

    assert len(approved) == len(set(approved)) == 55
    assert all((REPO_ROOT / path).is_file() for path in approved)


def test_apps_rg_contract_import_outside_facade_is_a_violation() -> None:
    records = [
        CoreImportRecord(
            "src/apps_rg/runtime/bypass.py",
            "agentic_core.runtime.contracts.route_contract",
            1,
        )
    ]
    policy = {
        "apps_rg_contract_facade": "src/apps_rg/runtime/spine_contracts.py",
        "approved_core_boundary_modules": [],
    }

    violations = boundary_violations(records, policy)

    assert violations["apps_rg_contract_facade_bypasses"] == [
        "src/apps_rg/runtime/bypass.py"
    ]


def test_canonical_fresh_cli_requires_the_pinned_external_runtime_preflight() -> None:
    tree = ast.parse((REPO_ROOT / "src/apps_rg/__main__.py").read_text(encoding="utf-8"))
    fresh_preflight_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "run_fresh_e2e_preflight"
    ]

    assert len(fresh_preflight_calls) == 1
    assert {
        keyword.arg for keyword in fresh_preflight_calls[0].keywords
    } >= {"dependency_check", "runtime_check", "bootstrap"}
