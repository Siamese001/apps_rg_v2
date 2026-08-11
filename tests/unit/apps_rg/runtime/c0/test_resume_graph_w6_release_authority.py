from __future__ import annotations

import json
from pathlib import Path

import pytest

from apps_rg.runtime.c0 import resume_graph_w6_release_authority as subject


def test_missing_w6_authority_blocks_before_dispatch_and_emits_receipt(
    tmp_path: Path,
) -> None:
    artifact_dir = tmp_path / "run"

    with pytest.raises(subject.ResumeGraphW6ReleaseAuthorityError, match="artifact_missing"):
        subject.require_w6_release_authority(
            repo_root=tmp_path,
            artifact_dir=artifact_dir,
            environ={},
        )

    receipt = json.loads(
        (artifact_dir / subject.W6_PREFLIGHT_RECEIPT).read_text(encoding="utf-8")
    )
    assert receipt["status"] == "BLOCKED"
    assert receipt["provider_dispatch_allowed"] is False
    assert receipt["human_authority_inferred"] is False
    assert "official_w6_artifact_missing" in receipt["failure_reasons"]


def test_validated_w6_authority_is_bound_without_creating_human_authority(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    receipt_path = tmp_path / "artifacts" / "official_w6.json"
    receipt_path.parent.mkdir(parents=True)
    receipt_path.write_text('{"status":"PASS"}\n', encoding="utf-8")
    monkeypatch.setattr(subject, "validate_artifact", lambda *args, **kwargs: [])

    evidence = subject.require_w6_release_authority(
        repo_root=tmp_path,
        artifact_dir=tmp_path / "run",
        environ={
            subject.W6_ARTIFACT_ENV: "artifacts/official_w6.json",
            subject.TRUSTED_REPORT_SHA256_ENV: "sha256:" + "a" * 64,
            subject.TRUSTED_FULL_REPORT_SHA256_ENV: "sha256:" + "b" * 64,
        },
    )

    assert evidence["receipt_ref"] == "artifacts/official_w6.json"
    assert evidence["receipt_sha256"].startswith("sha256:")
    persisted = json.loads(
        (tmp_path / "run" / subject.W6_PREFLIGHT_RECEIPT).read_text(encoding="utf-8")
    )
    assert persisted["status"] == "PASS"
    assert persisted["human_authority_created"] is False
