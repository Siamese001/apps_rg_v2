from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
from types import ModuleType

import pytest


_REQUIRED_MODULES = (
    "agentic_core.runtime.contracts.apps_rg_ingress_payload",
    "agentic_core.runtime.contracts.l1_plan_contract",
    "agentic_core.runtime.contracts.route_contract",
    "agentic_core.runtime.contracts.final_evidence_contract",
    "agentic_core.runtime.contracts.compiled_prompt_artifact",
    "agentic_core.runtime.contracts.sealed_l2_artifact",
    "agentic_core.runtime.exit.exit_disposition",
)


def _module(name: str, path: Path) -> ModuleType:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {name}\n", encoding="utf-8")
    value = ModuleType(name)
    value.__file__ = str(path)
    return value


def _external_modules(root: Path) -> dict[str, ModuleType]:
    package = root / "agentic_core"
    modules = {"agentic_core": _module("agentic_core", package / "__init__.py")}
    for name in _REQUIRED_MODULES:
        parts = name.split(".")[1:]
        modules[name] = _module(name, package.joinpath(*parts).with_suffix(".py"))
    return modules


def _patch_imports(
    monkeypatch: pytest.MonkeyPatch,
    modules: dict[str, ModuleType],
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    def _import(name: str) -> ModuleType:
        if name in modules:
            return modules[name]
        raise ModuleNotFoundError(name)

    monkeypatch.setattr(posture.importlib, "import_module", _import)
    monkeypatch.setattr(
        posture.importlib_metadata,
        "distribution",
        lambda _name: (_ for _ in ()).throw(posture.importlib_metadata.PackageNotFoundError),
    )


def _trusted_contract(tmp_path: Path, package_root: Path) -> Path:
    """Pin the synthetic external package exactly as production requires."""

    subprocess.run(["git", "init", str(package_root)], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(package_root), "config", "user.email", "tests@example.invalid"],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "-C", str(package_root), "config", "user.name", "Apps RG tests"],
        check=True,
        capture_output=True,
    )
    subprocess.run(["git", "-C", str(package_root), "add", "agentic_core"], check=True, capture_output=True)
    subprocess.run(
        ["git", "-C", str(package_root), "commit", "-m", "synthetic core"],
        check=True,
        capture_output=True,
    )
    head = subprocess.check_output(
        ["git", "-C", str(package_root), "rev-parse", "HEAD"], text=True
    ).strip()
    tree = subprocess.check_output(
        ["git", "-C", str(package_root), "rev-parse", "HEAD:agentic_core"], text=True
    ).strip()
    contract = json.loads(
        (Path(__file__).resolve().parents[4] / "config/contracts/apps_rg_standalone_runtime_dependency.v1.json").read_text(
            encoding="utf-8"
        )
    )
    contract["runtime_trust"] = {
        "mode": "GIT_COMMIT_AND_PACKAGE_TREE_PIN",
        "approved_repository_commit": head,
        "approved_package_tree": tree,
        "package_relative_path": "agentic_core",
        "require_clean_tracked_worktree": True,
    }
    path = tmp_path / "runtime-contract.json"
    path.write_text(json.dumps(contract), encoding="utf-8")
    return path


def test_external_source_runtime_receipt_proves_spine_sentinels(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    external = tmp_path / "external"
    modules = _external_modules(external)
    _patch_imports(monkeypatch, modules)

    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=_trusted_contract(tmp_path, external),
        generated_at_utc=datetime(2026, 8, 6, tzinfo=timezone.utc),
    )

    assert receipt["status"] == posture.EXTERNAL_RUNTIME_BOUND
    assert receipt["standalone_installability"] == "NOT_CLAIMED_EXTERNAL_RUNTIME_REQUIRED"
    assert receipt["runtime_behavior_parity"] == "NOT_CLAIMED"
    assert receipt["distribution_metadata"]["status"] == "NOT_INSTALLED_METADATA"
    assert [row["spine_stage"] for row in receipt["required_module_results"]] == [
        "U0",
        "L1",
        "L0",
        "C0",
        "PA",
        "L2",
        "Exit",
    ]
    assert {row["status"] for row in receipt["required_module_results"]} == {"RESOLVED"}
    posture.validate_standalone_runtime_dependency_receipt(receipt)

    artifact_dir = tmp_path / "run"
    artifact_dir.mkdir()
    receipt_path = posture.write_standalone_runtime_dependency_receipt(
        artifact_dir=artifact_dir,
        receipt=receipt,
    )
    assert receipt_path.name == posture.STANDALONE_RUNTIME_DEPENDENCY_RECEIPT_FILENAME
    assert receipt_path.is_file()


def test_local_agentic_core_shadow_is_blocked_before_sentinel_imports(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    modules = _external_modules(repo)
    _patch_imports(monkeypatch, modules)

    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=posture.standalone_runtime_dependency_contract_path(),
    )

    assert receipt["status"] == "BLOCKED_AGENTIC_CORE_LOCAL_TO_STANDALONE"
    assert receipt["required_module_results"] == []
    posture.validate_standalone_runtime_dependency_receipt(receipt)
    with pytest.raises(posture.StandaloneRuntimeDependencyError, match="unavailable"):
        posture.require_external_agentic_core_runtime(
            repo_root=repo,
            contract_path=posture.standalone_runtime_dependency_contract_path(),
        )


def test_missing_required_core_module_is_a_fail_closed_runtime_boundary(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    external = tmp_path / "external"
    modules = _external_modules(external)
    missing = _REQUIRED_MODULES[-1]
    del modules[missing]
    _patch_imports(monkeypatch, modules)

    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=_trusted_contract(tmp_path, external),
    )

    assert receipt["status"] == "BLOCKED_REQUIRED_AGENTIC_CORE_MODULES_UNAVAILABLE"
    result_by_module = {row["module"]: row for row in receipt["required_module_results"]}
    assert result_by_module[missing] == {
        "module": missing,
        "spine_stage": "Exit",
        "status": "UNAVAILABLE",
        "error_class": "ModuleNotFoundError",
    }
    posture.validate_standalone_runtime_dependency_receipt(receipt)


def test_external_runtime_commit_or_tree_drift_is_fail_closed(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    external = tmp_path / "external"
    modules = _external_modules(external)
    contract_path = _trusted_contract(tmp_path, external)
    (external / "agentic_core" / "__init__.py").write_text("# drift\n", encoding="utf-8")
    _patch_imports(monkeypatch, modules)

    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=contract_path,
    )

    assert receipt["status"] == "BLOCKED_AGENTIC_CORE_TRUST_PIN_MISMATCH"
    assert receipt["failure_code"] == "AGENTIC_CORE_RUNTIME_TRUST_PIN_MISMATCH"


def test_invalid_dependency_contract_is_a_fail_closed_runtime_boundary(
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    malformed_contract = tmp_path / "malformed_dependency_contract.json"
    malformed_contract.write_text("{}\n", encoding="utf-8")

    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=malformed_contract,
    )

    assert receipt["status"] == "BLOCKED_DEPENDENCY_CONTRACT_INVALID"
    assert receipt["failure_code"] == "STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_INVALID"
    posture.validate_standalone_runtime_dependency_receipt(receipt)


def test_dependency_receipt_digest_rejects_a_promotion_like_claim(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from apps_rg.runtime import standalone_dependency_posture as posture

    repo = tmp_path / "standalone"
    repo.mkdir()
    external = tmp_path / "external"
    modules = _external_modules(external)
    _patch_imports(monkeypatch, modules)
    receipt = posture.verify_external_agentic_core_runtime(
        repo_root=repo,
        contract_path=_trusted_contract(tmp_path, external),
    )
    receipt["standalone_installability"] = "INDEPENDENTLY_INSTALLABLE"

    with pytest.raises(posture.StandaloneRuntimeDependencyError, match="installability claim"):
        posture.validate_standalone_runtime_dependency_receipt(receipt)
