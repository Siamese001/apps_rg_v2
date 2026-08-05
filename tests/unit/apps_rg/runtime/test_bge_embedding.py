from __future__ import annotations

import math

import pytest

from apps_rg.runtime.bge_embedding import BgeEmbeddingContractError, embed_text
from apps_rg.runtime.embedding_settings import BGE_M3_DIMENSION


class _ArrayLike:
    def __init__(self, values: list[float]) -> None:
        self._values = values

    def tolist(self) -> list[float]:
        return list(self._values)


class _Model:
    def __init__(self, values: list[float]) -> None:
        self.values = values
        self.calls: list[tuple[str, bool]] = []

    def encode(self, text: str, *, normalize_embeddings: bool) -> _ArrayLike:
        self.calls.append((text, normalize_embeddings))
        return _ArrayLike(self.values)


def test_embed_text_preserves_bge_m3_l2_normalization_contract() -> None:
    value = 1.0 / math.sqrt(BGE_M3_DIMENSION)
    model = _Model([value] * BGE_M3_DIMENSION)

    vector = embed_text(model, "partner-led AI deployment")

    assert len(vector) == BGE_M3_DIMENSION
    assert model.calls == [("partner-led AI deployment", True)]
    assert math.isclose(math.sqrt(sum(item * item for item in vector)), 1.0)


def test_embed_text_rejects_wrong_dimension() -> None:
    with pytest.raises(BgeEmbeddingContractError, match="dimension mismatch"):
        embed_text(_Model([1.0]), "text")


def test_embed_text_rejects_non_normalized_vector() -> None:
    with pytest.raises(BgeEmbeddingContractError, match="not L2 normalized"):
        embed_text(_Model([1.0] * BGE_M3_DIMENSION), "text")
