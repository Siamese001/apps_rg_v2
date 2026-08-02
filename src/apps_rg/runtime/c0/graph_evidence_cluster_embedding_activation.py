"""Fail-closed activation boundary for future graph-evidence cluster embeddings."""

from __future__ import annotations

import hashlib
import json
import os
from collections.abc import Mapping
from pathlib import Path
from typing import Any

GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV = (
    "APPS_RG_GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED"
)
ACTIVE_CLUSTER_MANIFEST = Path(
    "artifacts/apps_rg/c03/graph_evidence_cluster_embeddings/"
    "graph_evidence_cluster_embedding_activation_manifest.json"
)
ACTIVATION_SCHEMA_VERSION = (
    "apps_rg.graph_evidence_cluster_embedding_activation_manifest.v1"
)
ACTIVATION_COMPLETION_MARKER = "GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_QUALIFIED"
_TRUE_VALUES = frozenset({"1", "true", "yes", "on"})
_FALSE_VALUES = frozenset({"0", "false", "no", "off", ""})
_ACTIVE_CLUSTER_ARTIFACT_DIR = ACTIVE_CLUSTER_MANIFEST.parent


class GraphEvidenceClusterEmbeddingActivationError(RuntimeError):
    """Raised when cluster embedding activation cannot prove its authority."""


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_sha256(value: object) -> bool:
    normalized = str(value or "")
    return len(normalized) == 64 and all(
        character in "0123456789abcdef" for character in normalized
    )


def graph_evidence_cluster_embeddings_required() -> bool:
    """Return the explicit opt-in state; reject malformed boolean values."""

    raw = (
        str(os.environ.get(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV) or "")
        .strip()
        .lower()
    )
    if raw in _TRUE_VALUES:
        return True
    if raw in _FALSE_VALUES:
        return False
    raise GraphEvidenceClusterEmbeddingActivationError(
        f"{GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV} must be a boolean value"
    )


def _load_manifest(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise GraphEvidenceClusterEmbeddingActivationError(
            f"cluster embedding activation manifest is missing or malformed: {path}"
        ) from exc
    if not isinstance(payload, dict):
        raise GraphEvidenceClusterEmbeddingActivationError(
            f"cluster embedding activation manifest must be an object: {path}"
        )
    return payload


def validate_graph_evidence_cluster_activation_manifest(
    manifest: Mapping[str, Any],
) -> str:
    """Validate release authority and return the manifest's self digest."""

    if manifest.get("schema_version") != ACTIVATION_SCHEMA_VERSION:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding activation schema is invalid"
        )
    if manifest.get("status") != "PASS":
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding activation status is not PASS"
        )
    if manifest.get("completion_marker") != ACTIVATION_COMPLETION_MARKER:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding qualification marker is invalid"
        )
    if manifest.get("release_authorizing") is not True:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding qualification is not release authorizing"
        )
    if manifest.get("logical_retrieval_unit") != "graph_evidence_cluster":
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding logical retrieval unit is invalid"
        )
    if manifest.get("legacy_skill_vector_generation_active") is not False:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "legacy skill-vector generation must be retired before cluster activation"
        )
    projection = manifest.get("projection")
    if not isinstance(projection, Mapping):
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection authority is missing"
        )
    for field in (
        "path",
        "file_sha256",
        "corpus_sha256",
        "model_artifact_sha256",
        "graph_sha256",
    ):
        if not str(projection.get(field) or "").strip():
            raise GraphEvidenceClusterEmbeddingActivationError(
                f"cluster embedding projection authority is missing {field}"
            )
    for field in (
        "file_sha256",
        "corpus_sha256",
        "model_artifact_sha256",
        "graph_sha256",
    ):
        if not _is_sha256(projection.get(field)):
            raise GraphEvidenceClusterEmbeddingActivationError(
                f"cluster embedding projection authority has invalid {field}"
            )
    cluster_count = projection.get("cluster_count")
    top_k = projection.get("top_k")
    if (
        not isinstance(cluster_count, int)
        or isinstance(cluster_count, bool)
        or cluster_count < 2
    ):
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection cluster_count must be at least two"
        )
    if (
        not isinstance(top_k, int)
        or isinstance(top_k, bool)
        or top_k < 1
        or top_k >= cluster_count
    ):
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection top_k must be bounded below cluster_count"
        )
    if projection.get("dimension") != 1024 or projection.get("normalization") != "l2":
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection shape is invalid"
        )
    if projection.get("exact_rehydration_required") is not True:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection must require exact graph rehydration"
        )
    unsigned = dict(manifest)
    recorded = str(unsigned.pop("manifest_sha256", "") or "")
    observed = _canonical_sha256(unsigned)
    if not recorded or recorded != observed:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding activation manifest digest is invalid"
        )
    return recorded


def require_graph_evidence_cluster_embedding_activation(
    repo_root: Path | str,
) -> dict[str, Any]:
    """Load and validate cluster authority when the future lane is required.

    The call fails closed if the opt-in is absent, or if any release-authority
    binding is missing.  Wave 0 intentionally ships no active manifest.
    """

    if not graph_evidence_cluster_embeddings_required():
        raise GraphEvidenceClusterEmbeddingActivationError(
            "graph-evidence cluster embeddings are not explicitly required"
        )
    root = Path(repo_root).resolve()
    manifest_path = (root / ACTIVE_CLUSTER_MANIFEST).resolve()
    try:
        manifest_path.relative_to(root)
    except ValueError as exc:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding activation path escapes the repository root"
        ) from exc
    manifest = _load_manifest(manifest_path)
    manifest_sha256 = validate_graph_evidence_cluster_activation_manifest(manifest)
    projection = manifest["projection"]
    projection_path = (root / str(projection["path"])).resolve()
    artifact_root = (root / _ACTIVE_CLUSTER_ARTIFACT_DIR).resolve()
    try:
        projection_path.relative_to(artifact_root)
    except ValueError as exc:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection path escapes the active artifact directory"
        ) from exc
    if not projection_path.is_file():
        raise GraphEvidenceClusterEmbeddingActivationError(
            f"cluster embedding projection is missing: {projection_path}"
        )
    observed_projection_sha256 = _file_sha256(projection_path)
    if observed_projection_sha256 != projection["file_sha256"]:
        raise GraphEvidenceClusterEmbeddingActivationError(
            "cluster embedding projection file digest is invalid"
        )
    return {
        "manifest_path": ACTIVE_CLUSTER_MANIFEST.as_posix(),
        "manifest_sha256": manifest_sha256,
        "logical_retrieval_unit": "graph_evidence_cluster",
        "projection": dict(projection),
    }


__all__ = [
    "ACTIVATION_COMPLETION_MARKER",
    "ACTIVATION_SCHEMA_VERSION",
    "ACTIVE_CLUSTER_MANIFEST",
    "GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV",
    "GraphEvidenceClusterEmbeddingActivationError",
    "graph_evidence_cluster_embeddings_required",
    "require_graph_evidence_cluster_embedding_activation",
    "validate_graph_evidence_cluster_activation_manifest",
]
