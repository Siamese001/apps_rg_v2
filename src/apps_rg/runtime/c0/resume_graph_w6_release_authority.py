"""Fail-closed W6 release authority for whole-resume graph generation.

The whole-resume allocation is a product graph, so its official W6 release
receipt must be present *before* any paid lane or aggregate-judge work starts.
This module only hashes and validates a previously issued human/offline
authority artifact; it never creates, upgrades, or infers that authority.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Mapping

from apps_rg.evals.receipt_validation import (
    DEFAULT_ARTIFACT,
    TRUSTED_FULL_REPORT_SHA256_ENV,
    TRUSTED_REPORT_SHA256_ENV,
    validate_artifact,
)


W6_ARTIFACT_ENV = "APPS_RG_RESUME_GRAPH_W6_ARTIFACT"
W6_PREFLIGHT_RECEIPT = "resume_graph_w6_release_preflight_receipt.json"
W6_PREFLIGHT_SCHEMA = "apps_rg.resume_graph_w6_release_preflight.v1"


class ResumeGraphW6ReleaseAuthorityError(RuntimeError):
    """Raised before provider dispatch when W6 product authority is unavailable."""


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(value), ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _configured_artifact(repo_root: Path, environ: Mapping[str, str]) -> Path:
    configured = str(environ.get(W6_ARTIFACT_ENV) or "").strip()
    candidate = Path(configured) if configured else Path(DEFAULT_ARTIFACT)
    if not candidate.is_absolute():
        candidate = repo_root / candidate
    return candidate.resolve()


def _contained_ref(repo_root: Path, artifact: Path) -> str:
    try:
        return artifact.relative_to(repo_root.resolve()).as_posix()
    except ValueError as exc:
        raise ResumeGraphW6ReleaseAuthorityError(
            "official W6 artifact must be contained by the apps_rg repository"
        ) from exc


def resolve_w6_release_evidence(
    *,
    repo_root: Path | str,
    environ: Mapping[str, str] | None = None,
) -> tuple[dict[str, Any], list[str]]:
    """Return source-bound W6 evidence, or explicit non-authorizing reasons."""

    repo = Path(repo_root).resolve()
    env = os.environ if environ is None else environ
    artifact = _configured_artifact(repo, env)
    reasons: list[str] = []
    try:
        artifact_ref = _contained_ref(repo, artifact)
    except ResumeGraphW6ReleaseAuthorityError as exc:
        artifact_ref = ""
        reasons.append(str(exc))

    trusted_receipt = str(env.get(TRUSTED_REPORT_SHA256_ENV) or "").strip()
    trusted_full = str(env.get(TRUSTED_FULL_REPORT_SHA256_ENV) or "").strip()
    if not artifact.is_file():
        reasons.append("official_w6_artifact_missing")
    if not trusted_receipt:
        reasons.append("trusted_w6_receipt_sha256_missing")
    if not trusted_full:
        reasons.append("trusted_w6_full_report_sha256_missing")
    if not reasons:
        reasons.extend(
            str(value)
            for value in validate_artifact(
                artifact,
                trusted_report_sha256=trusted_receipt,
                trusted_full_report_sha256=trusted_full,
            )
        )

    evidence = {
        "receipt_ref": artifact_ref,
        "receipt_sha256": _sha256_file(artifact) if artifact.is_file() else "",
        "trusted_receipt_sha256": trusted_receipt,
        "trusted_full_report_sha256": trusted_full,
    }
    return evidence, list(dict.fromkeys(reasons))


def require_w6_release_authority(
    *,
    repo_root: Path | str,
    artifact_dir: Path | str,
    environ: Mapping[str, str] | None = None,
) -> dict[str, Any]:
    """Persist and return validated W6 evidence, otherwise block before a model call."""

    evidence, reasons = resolve_w6_release_evidence(
        repo_root=repo_root,
        environ=environ,
    )
    receipt = {
        "schema_version": W6_PREFLIGHT_SCHEMA,
        "status": "PASS" if not reasons else "BLOCKED",
        "provider_dispatch_allowed": not reasons,
        "resume_graph_w6_release_evidence": evidence,
        "failure_reasons": reasons,
        "human_authority_inferred": False,
        "human_authority_created": False,
    }
    _write_json(Path(artifact_dir) / W6_PREFLIGHT_RECEIPT, receipt)
    if reasons:
        raise ResumeGraphW6ReleaseAuthorityError(
            "whole-resume graph product release authority unavailable: "
            + "; ".join(reasons)
        )
    return evidence


__all__ = [
    "ResumeGraphW6ReleaseAuthorityError",
    "W6_ARTIFACT_ENV",
    "W6_PREFLIGHT_RECEIPT",
    "W6_PREFLIGHT_SCHEMA",
    "require_w6_release_authority",
    "resolve_w6_release_evidence",
]
