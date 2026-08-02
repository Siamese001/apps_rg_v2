from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

from apps_rg.runtime.c0.graph_evidence_cluster_embedding_activation import (
    ACTIVE_CLUSTER_MANIFEST,
    GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV,
    GraphEvidenceClusterEmbeddingActivationError,
    graph_evidence_cluster_embeddings_required,
    require_graph_evidence_cluster_embedding_activation,
    validate_graph_evidence_cluster_activation_manifest,
)


def _canonical_sha256(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _valid_manifest(*, projection_sha256: str = "a" * 64) -> dict[str, object]:
    manifest: dict[str, object] = {
        "schema_version": (
            "apps_rg.graph_evidence_cluster_embedding_activation_manifest.v1"
        ),
        "status": "PASS",
        "completion_marker": "GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_QUALIFIED",
        "release_authorizing": True,
        "logical_retrieval_unit": "graph_evidence_cluster",
        "legacy_skill_vector_generation_active": False,
        "projection": {
            "path": (
                "artifacts/apps_rg/c03/graph_evidence_cluster_embeddings/"
                "projection.sqlite"
            ),
            "file_sha256": projection_sha256,
            "corpus_sha256": "b" * 64,
            "model_artifact_sha256": "c" * 64,
            "graph_sha256": "d" * 64,
            "cluster_count": 35,
            "top_k": 5,
            "dimension": 1024,
            "normalization": "l2",
            "exact_rehydration_required": True,
        },
    }
    manifest["manifest_sha256"] = _canonical_sha256(manifest)
    return manifest


def test_cluster_activation_is_disabled_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV, raising=False)
    assert graph_evidence_cluster_embeddings_required() is False


def test_cluster_activation_rejects_malformed_boolean(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV, "maybe")
    with pytest.raises(GraphEvidenceClusterEmbeddingActivationError, match="boolean"):
        graph_evidence_cluster_embeddings_required()


def test_cluster_activation_fails_closed_without_opt_in(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV, raising=False)
    with pytest.raises(
        GraphEvidenceClusterEmbeddingActivationError,
        match="not explicitly required",
    ):
        require_graph_evidence_cluster_embedding_activation(tmp_path)


def test_cluster_activation_fails_closed_when_manifest_is_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV, "1")
    with pytest.raises(
        GraphEvidenceClusterEmbeddingActivationError,
        match="missing or malformed",
    ):
        require_graph_evidence_cluster_embedding_activation(tmp_path)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("release_authorizing", False, "not release authorizing"),
        (
            "logical_retrieval_unit",
            "skill",
            "logical retrieval unit is invalid",
        ),
        (
            "legacy_skill_vector_generation_active",
            True,
            "legacy skill-vector generation must be retired",
        ),
    ],
)
def test_cluster_activation_rejects_non_promotable_manifests(
    field: str,
    value: object,
    message: str,
) -> None:
    manifest = _valid_manifest()
    manifest[field] = value
    manifest["manifest_sha256"] = _canonical_sha256(
        {key: item for key, item in manifest.items() if key != "manifest_sha256"}
    )
    with pytest.raises(GraphEvidenceClusterEmbeddingActivationError, match=message):
        validate_graph_evidence_cluster_activation_manifest(manifest)


def test_cluster_activation_accepts_exact_release_authority(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    projection_path = tmp_path / (
        "artifacts/apps_rg/c03/graph_evidence_cluster_embeddings/projection.sqlite"
    )
    projection_path.parent.mkdir(parents=True)
    projection_path.write_bytes(b"cluster projection")
    projection_sha256 = hashlib.sha256(projection_path.read_bytes()).hexdigest()
    manifest = _valid_manifest(projection_sha256=projection_sha256)
    path = tmp_path / ACTIVE_CLUSTER_MANIFEST
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest), encoding="utf-8")
    monkeypatch.setenv(GRAPH_EVIDENCE_CLUSTER_EMBEDDINGS_REQUIRED_ENV, "true")

    authority = require_graph_evidence_cluster_embedding_activation(tmp_path)

    assert authority["logical_retrieval_unit"] == "graph_evidence_cluster"
    assert authority["manifest_sha256"] == manifest["manifest_sha256"]
    assert authority["projection"] == manifest["projection"]
