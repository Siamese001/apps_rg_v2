"""Standalone-owned BGE-M3 vector materialization.

The Apps RG runtime must not depend on the monorepo-only
``tools.ingestion`` package merely to turn an already loaded local BGE-M3
model into a vector.  This module preserves that helper's contract while
making its model dimension and L2-normalization invariants explicit.
"""

from __future__ import annotations

import math
from typing import Any

from apps_rg.runtime.embedding_settings import BGE_M3_DIMENSION


class BgeEmbeddingContractError(RuntimeError):
    """A loaded embedding model did not return the pinned BGE-M3 vector shape."""


def embed_text(model: Any, text: str) -> list[float]:
    """Return one L2-normalized, 1024-dimensional BGE-M3 vector for ``text``.

    ``model`` is supplied by ``load_bge_sentence_transformer`` after that
    loader has already enforced the local pinned BGE-M3 model policy.  This
    helper deliberately does not load a model or contact a hub.
    """

    encoded = model.encode(str(text), normalize_embeddings=True)
    raw = encoded.tolist() if hasattr(encoded, "tolist") else list(encoded)
    vector = [float(value) for value in raw]
    if len(vector) != BGE_M3_DIMENSION:
        raise BgeEmbeddingContractError(
            f"BGE-M3 embedding dimension mismatch: expected {BGE_M3_DIMENSION}, got {len(vector)}"
        )
    norm = math.sqrt(sum(value * value for value in vector))
    if not math.isfinite(norm) or not math.isclose(norm, 1.0, rel_tol=1e-4, abs_tol=1e-4):
        raise BgeEmbeddingContractError(
            f"BGE-M3 embedding is not L2 normalized: observed norm={norm!r}"
        )
    return vector


__all__ = ["BgeEmbeddingContractError", "embed_text"]
