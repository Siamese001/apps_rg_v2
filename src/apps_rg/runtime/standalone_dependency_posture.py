"""Fail-closed evidence for the standalone checkout's external core runtime.

``apps_rg_v2`` intentionally does not vendor ``agentic_core``.  A regular
external package is therefore a runtime prerequisite, not an implementation
detail.  This module records the resolved source package and a small set of
spine-contract import sentinels before product work begins.  It proves only
that boundary; it does not claim a distributable standalone install or runtime
behavior parity.
"""

from __future__ import annotations

import hashlib
import importlib
import json
from collections.abc import Mapping, Sequence
from datetime import datetime, timezone
from importlib import metadata as importlib_metadata
from pathlib import Path
from types import ModuleType
from typing import Any, Final

from apps_rg.repository_layout import repository_root


STANDALONE_RUNTIME_DEPENDENCY_SCHEMA_VERSION: Final[str] = (
    "apps_rg.standalone_runtime_dependency_receipt.v1"
)
STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_SCHEMA_VERSION: Final[str] = (
    "apps_rg.standalone_runtime_dependency_contract.v1"
)
STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_RELPATH: Final[Path] = Path(
    "config/contracts/apps_rg_standalone_runtime_dependency.v1.json"
)
STANDALONE_RUNTIME_DEPENDENCY_RECEIPT_FILENAME: Final[str] = (
    "standalone_runtime_dependency_receipt.json"
)
EXTERNAL_RUNTIME_BOUND: Final[str] = "EXTERNAL_RUNTIME_BOUND"


class StandaloneRuntimeDependencyError(RuntimeError):
    """Raised when a caller requires an unavailable external core runtime."""


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _sha256_bytes(value: bytes) -> str:
    return "sha256:" + hashlib.sha256(value).hexdigest()


def _path_is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def standalone_runtime_dependency_contract_path(repo_root: Path | None = None) -> Path:
    """Return the app-owned declaration for the external runtime boundary."""

    root = Path(repo_root).resolve() if repo_root is not None else repository_root(Path(__file__))
    return root / STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_RELPATH


def _read_contract(path: Path) -> tuple[dict[str, Any], str]:
    try:
        raw = path.read_bytes()
        value = json.loads(raw)
    except (OSError, json.JSONDecodeError) as exc:
        raise StandaloneRuntimeDependencyError(
            f"standalone runtime dependency contract is unreadable: {type(exc).__name__}"
        ) from exc
    if not isinstance(value, dict):
        raise StandaloneRuntimeDependencyError(
            "standalone runtime dependency contract must be an object"
        )
    return value, _sha256_bytes(raw)


def _validated_contract(value: Mapping[str, Any]) -> tuple[dict[str, str], list[dict[str, str]], dict[str, Any]]:
    if value.get("schema_version") != STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_SCHEMA_VERSION:
        raise StandaloneRuntimeDependencyError("unsupported standalone runtime contract schema")
    if value.get("contract_type") != "StandaloneRuntimeDependencyContract":
        raise StandaloneRuntimeDependencyError("invalid standalone runtime contract type")
    dependency = value.get("dependency")
    if not isinstance(dependency, Mapping):
        raise StandaloneRuntimeDependencyError("standalone runtime contract dependency is required")
    normalized_dependency = {
        "import_name": str(dependency.get("import_name") or "").strip(),
        "distribution_name": str(dependency.get("distribution_name") or "").strip(),
        "resolution_mode": str(dependency.get("resolution_mode") or "").strip(),
    }
    if normalized_dependency != {
        "import_name": "agentic_core",
        "distribution_name": "agentic-core",
        "resolution_mode": "EXTERNAL_SOURCE_RUNTIME",
    }:
        raise StandaloneRuntimeDependencyError("standalone runtime dependency binding is invalid")

    raw_modules = value.get("required_runtime_modules")
    if not isinstance(raw_modules, Sequence) or isinstance(raw_modules, (str, bytes)):
        raise StandaloneRuntimeDependencyError("required_runtime_modules must be a sequence")
    modules: list[dict[str, str]] = []
    expected_stages = ("U0", "L1", "L0", "C0", "PA", "L2", "Exit")
    for raw in raw_modules:
        if not isinstance(raw, Mapping):
            raise StandaloneRuntimeDependencyError("required runtime module must be an object")
        module = str(raw.get("module") or "").strip()
        stage = str(raw.get("spine_stage") or "").strip()
        if not module.startswith("agentic_core.") or not stage:
            raise StandaloneRuntimeDependencyError("required runtime module binding is invalid")
        modules.append({"module": module, "spine_stage": stage})
    if tuple(row["spine_stage"] for row in modules) != expected_stages:
        raise StandaloneRuntimeDependencyError(
            "required runtime modules must cover the canonical U0-to-Exit spine once"
        )
    if len({row["module"] for row in modules}) != len(modules):
        raise StandaloneRuntimeDependencyError("required runtime modules must be unique")

    policy = value.get("resolution_policy")
    if not isinstance(policy, Mapping):
        raise StandaloneRuntimeDependencyError("standalone runtime resolution_policy is required")
    normalized_policy = {
        "package_must_resolve_outside_standalone_checkout": policy.get(
            "package_must_resolve_outside_standalone_checkout"
        ),
        "required_modules_must_resolve_within_resolved_package": policy.get(
            "required_modules_must_resolve_within_resolved_package"
        ),
        "installed_distribution_metadata": str(
            policy.get("installed_distribution_metadata") or ""
        ),
        "standalone_installability": str(policy.get("standalone_installability") or ""),
        "prohibited_claims": list(policy.get("prohibited_claims") or []),
    }
    if (
        normalized_policy["package_must_resolve_outside_standalone_checkout"] is not True
        or normalized_policy["required_modules_must_resolve_within_resolved_package"] is not True
        or normalized_policy["installed_distribution_metadata"] != "OPTIONAL"
        or normalized_policy["standalone_installability"]
        != "NOT_CLAIMED_EXTERNAL_RUNTIME_REQUIRED"
        or not all(isinstance(claim, str) and claim for claim in normalized_policy["prohibited_claims"])
    ):
        raise StandaloneRuntimeDependencyError("standalone runtime resolution_policy is invalid")
    return normalized_dependency, modules, normalized_policy


def _module_file(module: ModuleType) -> Path | None:
    raw = getattr(module, "__file__", None)
    if not raw:
        return None
    path = Path(str(raw)).resolve()
    return path if path.is_file() else None


def _distribution_metadata(distribution_name: str) -> dict[str, str]:
    try:
        distribution = importlib_metadata.distribution(distribution_name)
    except importlib_metadata.PackageNotFoundError:
        return {
            "distribution_name": distribution_name,
            "status": "NOT_INSTALLED_METADATA",
            "version": "",
        }
    except Exception as exc:  # metadata is observational-only; never an authorization input.
        return {
            "distribution_name": distribution_name,
            "status": "METADATA_UNAVAILABLE",
            "error_class": type(exc).__name__,
            "version": "",
        }
    return {
        "distribution_name": distribution_name,
        "status": "INSTALLED_METADATA_AVAILABLE",
        "version": str(distribution.version or ""),
    }


def _receipt_digest(receipt: Mapping[str, Any]) -> str:
    body = dict(receipt)
    body.pop("receipt_digest", None)
    return "sha256:" + hashlib.sha256(_canonical_json(body).encode("utf-8")).hexdigest()


def _base_receipt(
    *,
    repo: Path,
    contract_path: Path,
    contract_digest: str,
    generated_at_utc: datetime | None,
) -> dict[str, Any]:
    generated = generated_at_utc or datetime.now(timezone.utc)
    return {
        "schema_version": STANDALONE_RUNTIME_DEPENDENCY_SCHEMA_VERSION,
        "authority_class": "RUNTIME_DEPENDENCY_OBSERVABILITY_ONLY",
        "generated_at_utc": generated.astimezone(timezone.utc).isoformat(),
        "standalone_checkout_root": str(repo),
        "contract_ref": STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_RELPATH.as_posix(),
        "contract_path": str(contract_path),
        "contract_sha256": contract_digest,
        "standalone_installability": "NOT_CLAIMED_EXTERNAL_RUNTIME_REQUIRED",
        "runtime_behavior_parity": "NOT_CLAIMED",
    }


def verify_external_agentic_core_runtime(
    *,
    repo_root: Path | None = None,
    contract_path: Path | None = None,
    generated_at_utc: datetime | None = None,
) -> dict[str, Any]:
    """Resolve and record the external core package required by this checkout.

    The result is a receipt for either a usable external runtime or a specific
    blocked state.  It intentionally does not make distribution metadata or
    runtime behavior parity a prerequisite/claim: this checkout currently uses
    a source-tree dependency and records that fact explicitly.
    """

    repo = Path(repo_root).resolve() if repo_root is not None else repository_root(Path(__file__))
    path = Path(contract_path).resolve() if contract_path is not None else standalone_runtime_dependency_contract_path(repo)
    contract_digest = ""
    try:
        contract, contract_digest = _read_contract(path)
        dependency, required_modules, policy = _validated_contract(contract)
    except StandaloneRuntimeDependencyError as exc:
        receipt = _base_receipt(
            repo=repo,
            contract_path=path,
            contract_digest=contract_digest,
            generated_at_utc=generated_at_utc,
        )
        receipt.update(
            {
                "status": "BLOCKED_DEPENDENCY_CONTRACT_INVALID",
                "failure_code": "STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_INVALID",
                "failure_class": type(exc).__name__,
                "dependency": {},
                "resolution_policy": {},
                "package": {},
                "required_module_results": [],
                "distribution_metadata": {},
            }
        )
        receipt["receipt_digest"] = _receipt_digest(receipt)
        return receipt

    receipt = _base_receipt(
        repo=repo,
        contract_path=path,
        contract_digest=contract_digest,
        generated_at_utc=generated_at_utc,
    )
    receipt.update(
        {
            "dependency": dependency,
            "resolution_policy": policy,
            "package": {},
            "required_module_results": [],
            "distribution_metadata": _distribution_metadata(dependency["distribution_name"]),
        }
    )
    try:
        package = importlib.import_module(dependency["import_name"])
    except Exception as exc:  # import may fail for a missing source-tree dependency.
        receipt.update(
            {
                "status": "BLOCKED_AGENTIC_CORE_UNAVAILABLE",
                "failure_code": "AGENTIC_CORE_EXTERNAL_RUNTIME_UNAVAILABLE",
                "failure_class": type(exc).__name__,
            }
        )
        receipt["receipt_digest"] = _receipt_digest(receipt)
        return receipt

    package_file = _module_file(package)
    if package_file is None:
        receipt.update(
            {
                "status": "BLOCKED_AGENTIC_CORE_NAMESPACE",
                "failure_code": "AGENTIC_CORE_NAMESPACE_PACKAGE_FORBIDDEN",
                "failure_class": "NamespacePackage",
            }
        )
        receipt["receipt_digest"] = _receipt_digest(receipt)
        return receipt
    package_root = package_file.parent
    receipt["package"] = {
        "import_name": dependency["import_name"],
        "source_file": str(package_file),
        "source_sha256": _sha256_bytes(package_file.read_bytes()),
        "package_root": str(package_root),
        "source_external_to_standalone_checkout": not _path_is_within(package_file, repo),
    }
    if _path_is_within(package_file, repo):
        receipt.update(
            {
                "status": "BLOCKED_AGENTIC_CORE_LOCAL_TO_STANDALONE",
                "failure_code": "AGENTIC_CORE_MUST_BE_EXTERNAL_TO_STANDALONE_CHECKOUT",
                "failure_class": "LocalShadow",
            }
        )
        receipt["receipt_digest"] = _receipt_digest(receipt)
        return receipt

    results: list[dict[str, Any]] = []
    for requirement in required_modules:
        module_name = requirement["module"]
        result: dict[str, Any] = dict(requirement)
        try:
            module = importlib.import_module(module_name)
        except Exception as exc:  # preserve only exception class in durable artifact.
            result.update({"status": "UNAVAILABLE", "error_class": type(exc).__name__})
            results.append(result)
            continue
        module_file = _module_file(module)
        if module_file is None:
            result.update({"status": "NAMESPACE_PACKAGE", "error_class": "NamespacePackage"})
        elif not _path_is_within(module_file, package_root):
            result.update(
                {
                    "status": "OUTSIDE_RESOLVED_AGENTIC_CORE_PACKAGE",
                    "source_file": str(module_file),
                    "source_sha256": _sha256_bytes(module_file.read_bytes()),
                }
            )
        else:
            result.update(
                {
                    "status": "RESOLVED",
                    "source_file": str(module_file),
                    "source_sha256": _sha256_bytes(module_file.read_bytes()),
                }
            )
        results.append(result)
    receipt["required_module_results"] = results
    if all(row.get("status") == "RESOLVED" for row in results):
        receipt.update(
            {
                "status": EXTERNAL_RUNTIME_BOUND,
                "failure_code": "",
                "failure_class": "",
            }
        )
    else:
        receipt.update(
            {
                "status": "BLOCKED_REQUIRED_AGENTIC_CORE_MODULES_UNAVAILABLE",
                "failure_code": "REQUIRED_AGENTIC_CORE_RUNTIME_MODULES_UNAVAILABLE",
                "failure_class": "RequiredModuleResolution",
            }
        )
    receipt["receipt_digest"] = _receipt_digest(receipt)
    return receipt


def validate_standalone_runtime_dependency_receipt(receipt: Mapping[str, Any]) -> None:
    """Check the immutable receipt shape and its self-digest without re-importing."""

    if not isinstance(receipt, Mapping):
        raise StandaloneRuntimeDependencyError("standalone runtime dependency receipt must be an object")
    if receipt.get("schema_version") != STANDALONE_RUNTIME_DEPENDENCY_SCHEMA_VERSION:
        raise StandaloneRuntimeDependencyError("unsupported standalone runtime dependency receipt")
    if receipt.get("authority_class") != "RUNTIME_DEPENDENCY_OBSERVABILITY_ONLY":
        raise StandaloneRuntimeDependencyError("invalid standalone runtime receipt authority")
    if receipt.get("standalone_installability") != "NOT_CLAIMED_EXTERNAL_RUNTIME_REQUIRED":
        raise StandaloneRuntimeDependencyError("standalone installability claim is invalid")
    if receipt.get("runtime_behavior_parity") != "NOT_CLAIMED":
        raise StandaloneRuntimeDependencyError("runtime behavior parity claim is invalid")
    if receipt.get("receipt_digest") != _receipt_digest(receipt):
        raise StandaloneRuntimeDependencyError("standalone runtime dependency receipt digest mismatch")
    status = str(receipt.get("status") or "")
    if status == EXTERNAL_RUNTIME_BOUND:
        package = receipt.get("package")
        if not isinstance(package, Mapping) or package.get("source_external_to_standalone_checkout") is not True:
            raise StandaloneRuntimeDependencyError("external runtime receipt package binding is invalid")
        modules = receipt.get("required_module_results")
        if not isinstance(modules, Sequence) or isinstance(modules, (str, bytes)) or not modules:
            raise StandaloneRuntimeDependencyError("external runtime receipt module results are missing")
        if any(not isinstance(row, Mapping) or row.get("status") != "RESOLVED" for row in modules):
            raise StandaloneRuntimeDependencyError("external runtime receipt has unresolved modules")


def require_external_agentic_core_runtime(**kwargs: Any) -> dict[str, Any]:
    """Return an externally-bound runtime receipt or raise a typed blocked error."""

    receipt = verify_external_agentic_core_runtime(**kwargs)
    validate_standalone_runtime_dependency_receipt(receipt)
    if receipt.get("status") != EXTERNAL_RUNTIME_BOUND:
        raise StandaloneRuntimeDependencyError(
            f"external agentic_core runtime is unavailable: {receipt.get('status')}"
        )
    return receipt


def write_standalone_runtime_dependency_receipt(
    *, artifact_dir: Path,
    receipt: Mapping[str, Any],
) -> Path:
    """Persist an already-validated boundary receipt beneath a fresh run artifact."""

    validate_standalone_runtime_dependency_receipt(receipt)
    target = Path(artifact_dir).resolve() / STANDALONE_RUNTIME_DEPENDENCY_RECEIPT_FILENAME
    target.write_text(
        json.dumps(dict(receipt), indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


__all__ = [
    "EXTERNAL_RUNTIME_BOUND",
    "STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_RELPATH",
    "STANDALONE_RUNTIME_DEPENDENCY_CONTRACT_SCHEMA_VERSION",
    "STANDALONE_RUNTIME_DEPENDENCY_RECEIPT_FILENAME",
    "STANDALONE_RUNTIME_DEPENDENCY_SCHEMA_VERSION",
    "StandaloneRuntimeDependencyError",
    "require_external_agentic_core_runtime",
    "standalone_runtime_dependency_contract_path",
    "validate_standalone_runtime_dependency_receipt",
    "verify_external_agentic_core_runtime",
    "write_standalone_runtime_dependency_receipt",
]
