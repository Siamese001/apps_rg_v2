from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from apps_rg.runtime.c0.graph_skill_embedding_allocation import (
    GraphSkillEmbeddingAllocationError,
)
from tools.apps_rg_standalone import c03_embeddings

ROOT = Path(__file__).resolve().parents[4]
ACTIVE = ROOT / "artifacts/apps_rg/c03/graph_skill_embeddings"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _historical_generation_payload(candidate: Path) -> dict[str, object]:
    """Bypass only the intentionally stale graph binding for qualification tests."""
    generation = json.loads(
        (candidate / c03_embeddings.GENERATION_MANIFEST_NAME).read_bytes()
    )
    corpus_path = candidate / generation["assertion_corpus"]["path"]
    model_path = candidate / generation["model"]["path"]
    projection_path = candidate / generation["projection"]["path"]
    return {
        "generation": generation,
        "generation_digest": generation["manifest_sha256"],
        "corpus": json.loads(corpus_path.read_bytes()),
        "referenced_paths": [corpus_path, model_path, projection_path],
        "runtime_contract": c03_embeddings.verify_embedding_runtime_contract(ROOT),
    }


def test_script_bootstraps_src_without_preconfigured_pythonpath() -> None:
    environment = dict(os.environ)
    environment.pop("PYTHONPATH", None)

    completed = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/apps_rg_standalone/c03_embeddings.py"),
            "--help",
        ],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert "preflight" in completed.stdout
    assert "rebuild" in completed.stdout


def test_standalone_source_paths_use_src_owned_inputs() -> None:
    paths = c03_embeddings.standalone_source_paths(ROOT)

    assert paths == {
        "graph": ROOT / "src/apps_rg/fact_inventory/master_skills_arsenal_ledger.json",
        "candidate_facts": ROOT
        / (
            "artifacts/apps_rg/fact_inventory/"
            "master_candidate_skills_fact_ledger_20260518T1100Z.json"
        ),
        "base_resume": ROOT / "src/apps_rg/resume/base/amit_ayer_base_resume_v1.json",
    }
    assert all(path.is_file() for path in paths.values())


@pytest.mark.parametrize("output", [ACTIVE, ACTIVE / "candidate"])
def test_build_rejects_active_artifact_directory_before_model_load(
    output: Path,
) -> None:
    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="must not be the active artifact directory",
    ):
        c03_embeddings.build_candidate(
            repository_root=ROOT,
            output_dir=output,
            model_path=None,
            device=None,
        )


def test_build_passes_repository_root_and_src_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    model = tmp_path / "model"
    model.mkdir()
    observed: dict[str, object] = {}

    def fake_build(**kwargs: object) -> dict[str, object]:
        observed.update(kwargs)
        return {
            "manifest_sha256": "a" * 64,
            "model": {},
            "runtime_proof": {},
        }

    monkeypatch.setattr(
        c03_embeddings,
        "build_assertion_embedding_generation",
        fake_build,
    )
    monkeypatch.setattr(
        c03_embeddings,
        "verify_embedding_runtime_contract",
        lambda _root: {},
    )
    monkeypatch.setattr(
        c03_embeddings,
        "_validate_model_runtime_contract",
        lambda *_args: None,
    )
    monkeypatch.setattr(
        c03_embeddings,
        "_validate_runtime_proof",
        lambda *_args: None,
    )

    result = c03_embeddings.build_candidate(
        repository_root=ROOT,
        output_dir=tmp_path / "candidate",
        model_path=model,
        device="cpu",
    )

    assert result["manifest_sha256"] == "a" * 64
    assert observed["repository_root"] == ROOT
    assert observed["graph_path"] == (
        ROOT / "src/apps_rg/fact_inventory/master_skills_arsenal_ledger.json"
    )
    assert observed["base_resume_path"] == (
        ROOT / "src/apps_rg/resume/base/amit_ayer_base_resume_v1.json"
    )
    assert observed["output_dir"] == (tmp_path / "candidate").resolve()


def test_active_bundle_is_standalone_bound_and_regression_only() -> None:
    generation = json.loads(
        (ACTIVE / "graph_skill_embedding_manifest.json").read_bytes()
    )
    qualification = json.loads(
        (ACTIVE / "graph_embedding_qualification_manifest.json").read_bytes()
    )

    assert generation["graph"]["path"].startswith("src/apps_rg/")
    assert generation["base_resume"]["path"].startswith("src/apps_rg/")
    assert qualification["qualification_scope"] == "REGRESSION_ONLY"
    assert qualification["release_authorizing"] is False
    assert (
        qualification["embedding_generation_manifest_sha256"]
        == generation["manifest_sha256"]
    )
    assert generation["runtime_proof"]["sentence_transformers_version"] == "5.2.3"
    assert generation["runtime_proof"]["python_major_minor"] == "3.12"
    report = json.loads((ACTIVE / qualification["qualification"]["path"]).read_bytes())
    assert report["runtime_contract"]["contract_sha256"] == (
        "ab2cacbff73801b52ab31a8f9016f3cec11e3e60551a16d4a2411cd6e2bb5c79"
    )


def test_runtime_contract_pins_promoted_cuda_dependencies() -> None:
    contract = c03_embeddings.verify_embedding_runtime_contract(ROOT)

    assert contract["python_major_minor"] == "3.12"
    assert contract["packages"] == {
        "torch": "2.12.0.dev20260228+cu128",
        "sentence-transformers": "5.2.3",
    }
    assert contract["promoted_device"] == "cuda:0"


def test_runtime_contract_rejects_cpu_proof() -> None:
    contract = c03_embeddings.verify_embedding_runtime_contract(ROOT)

    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError, match="device mismatch"
    ):
        c03_embeddings._validate_runtime_proof(
            contract,
            {
                "python_major_minor": "3.12",
                "torch_version": "2.12.0.dev20260228+cu128",
                "sentence_transformers_version": "5.2.3",
                "device": "cpu",
                "cuda_available": True,
                "fallback_used": False,
            },
        )


def test_active_activation_receipt_binds_current_manifests() -> None:
    activation = json.loads(
        (ACTIVE / c03_embeddings.ACTIVATION_MANIFEST_NAME).read_bytes()
    )
    activation_digest = activation.pop("manifest_sha256")
    assert activation_digest == c03_embeddings.canonical_sha256(activation)
    receipt_ref = activation["activation_receipt"]
    receipt_path = ACTIVE / receipt_ref["path"]
    assert _sha256(receipt_path) == receipt_ref["file_sha256"]
    receipt = json.loads(receipt_path.read_bytes())
    receipt_digest = receipt.pop("activation_receipt_sha256")
    assert receipt_digest == receipt_ref["sha256"]
    assert receipt_digest == c03_embeddings.canonical_sha256(receipt)
    assert (
        receipt["active_generation_manifest_sha256"]
        == activation["active_generation_manifest_sha256"]
    )
    assert (
        receipt["active_qualification_sha256"]
        == activation["active_qualification_sha256"]
    )
    for key in ("generation_manifest", "qualification_manifest"):
        assert receipt[key] == activation[key]
        immutable_path = ACTIVE / receipt[key]["path"]
        assert _sha256(immutable_path) == receipt[key]["file_sha256"]
    assert receipt["qualification_scope"] == "REGRESSION_ONLY"
    assert receipt["release_authorizing"] is False
    assert receipt["graph_mutated"] is False


def test_preflight_is_read_only_and_rejects_stale_legacy_bundle() -> None:
    watched = [
        ACTIVE / "graph_skill_embedding_manifest.json",
        ACTIVE / "graph_embedding_qualification_manifest.json",
        ROOT / "src/apps_rg/fact_inventory/master_skills_arsenal_ledger.json",
    ]
    before = {path: _sha256(path) for path in watched}

    with pytest.raises(
        GraphSkillEmbeddingAllocationError,
        match="graph file digest mismatch",
    ):
        c03_embeddings.preflight(repository_root=ROOT)

    after = {path: _sha256(path) for path in watched}
    assert before == after


def test_candidate_validator_rejects_stale_active_bytes_and_active_dir() -> None:
    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="graph digest mismatch",
    ):
        c03_embeddings.validate_candidate_bundle(
            repository_root=ROOT,
            candidate_dir=ACTIVE,
        )
    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="must differ from active directory",
    ):
        c03_embeddings.activate_candidate(
            repository_root=ROOT,
            candidate_dir=ACTIVE,
        )


def test_candidate_validator_rejects_release_authorizing_manifest(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    candidate = tmp_path / "candidate"
    shutil.copytree(ACTIVE, candidate)
    monkeypatch.setattr(
        c03_embeddings,
        "_load_generation",
        lambda _root, generation_dir: _historical_generation_payload(generation_dir),
    )
    manifest_path = candidate / "graph_embedding_qualification_manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["release_authorizing"] = True
    manifest.pop("manifest_sha256")
    manifest["manifest_sha256"] = c03_embeddings.canonical_sha256(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="must be non-release-authorizing",
    ):
        c03_embeddings.validate_candidate_bundle(
            repository_root=ROOT,
            candidate_dir=candidate,
        )


def test_candidate_validator_cross_binds_report_to_query_qrels(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    candidate = tmp_path / "candidate"
    shutil.copytree(ACTIVE, candidate)
    monkeypatch.setattr(
        c03_embeddings,
        "_load_generation",
        lambda _root, generation_dir: _historical_generation_payload(generation_dir),
    )
    manifest_path = candidate / c03_embeddings.QUALIFICATION_MANIFEST_NAME
    manifest = json.loads(manifest_path.read_bytes())
    qrel_ref = manifest["query_qrels"]
    qrel_path = candidate / qrel_ref["path"]
    qrels = json.loads(qrel_path.read_bytes())
    qrels["tamper_probe"] = True
    qrels.pop("query_qrel_sha256")
    qrels["query_qrel_sha256"] = c03_embeddings.canonical_sha256(qrels)
    qrel_path.write_text(json.dumps(qrels, indent=2) + "\n", encoding="utf-8")
    qrel_ref["sha256"] = qrels["query_qrel_sha256"]
    qrel_ref["file_sha256"] = _sha256(qrel_path)
    manifest.pop("manifest_sha256")
    manifest["manifest_sha256"] = c03_embeddings.canonical_sha256(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="report/query QREL digest mismatch",
    ):
        c03_embeddings.validate_candidate_bundle(
            repository_root=ROOT,
            candidate_dir=candidate,
        )


def test_candidate_validator_requires_canonical_standalone_sources(
    tmp_path: Path,
) -> None:
    repository = tmp_path / "repo"
    repository.mkdir()
    candidate = repository / "candidate"
    shutil.copytree(ACTIVE, candidate)
    for label, source in c03_embeddings.standalone_source_paths(ROOT).items():
        destination = c03_embeddings.standalone_source_paths(repository)[label]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    alternate_graph = repository / "src/apps_rg/fact_inventory/alternate_graph.json"
    shutil.copyfile(
        c03_embeddings.standalone_source_paths(repository)["graph"],
        alternate_graph,
    )
    manifest_path = candidate / c03_embeddings.GENERATION_MANIFEST_NAME
    manifest = json.loads(manifest_path.read_bytes())
    manifest["graph"]["path"] = alternate_graph.relative_to(repository).as_posix()
    manifest.pop("manifest_sha256")
    manifest["manifest_sha256"] = c03_embeddings.canonical_sha256(manifest)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    with pytest.raises(
        c03_embeddings.StandaloneEmbeddingError,
        match="does not bind the canonical standalone source",
    ):
        c03_embeddings.validate_candidate_bundle(
            repository_root=repository,
            candidate_dir=candidate,
        )


def test_activation_rolls_back_manifests_and_receipt_when_pointer_write_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    candidate = tmp_path / "candidate"
    candidate.mkdir()
    active = tmp_path / c03_embeddings.ACTIVE_ARTIFACT_REL
    active.mkdir(parents=True)
    generation_path = active / c03_embeddings.GENERATION_MANIFEST_NAME
    qualification_path = active / c03_embeddings.QUALIFICATION_MANIFEST_NAME
    activation_path = active / c03_embeddings.ACTIVATION_MANIFEST_NAME
    old_generation = b'{"manifest_sha256":"old-generation"}\n'
    old_qualification = b'{"manifest_sha256":"old-qualification"}\n'
    old_activation = b'{"manifest_sha256":"old-activation"}\n'
    generation_path.write_bytes(old_generation)
    qualification_path.write_bytes(old_qualification)
    activation_path.write_bytes(old_activation)
    (candidate / c03_embeddings.GENERATION_MANIFEST_NAME).write_bytes(
        b'{"manifest_sha256":"new-generation"}\n'
    )
    (candidate / c03_embeddings.QUALIFICATION_MANIFEST_NAME).write_bytes(
        b'{"manifest_sha256":"new-qualification"}\n'
    )
    monkeypatch.setattr(
        c03_embeddings,
        "validate_candidate_bundle",
        lambda **_kwargs: {
            "generation_manifest_sha256": "new-generation",
            "qualification_manifest_sha256": "new-qualification-manifest",
            "qualification_sha256": "new-qualification-report",
            "qualification_scope": "REGRESSION_ONLY",
            "release_authorizing": False,
            "referenced_paths": [],
        },
    )
    monkeypatch.setattr(
        c03_embeddings,
        "load_graph_skill_embedding_authority",
        lambda _root: {
            "manifest_sha256": "new-generation",
            "qualification": {"qualification_sha256": "new-qualification-report"},
            "graph_sha256": "g" * 64,
            "corpus_sha256": "c" * 64,
            "embedding_generation_sha256": "e" * 64,
            "model_artifact_sha256": "m" * 64,
            "assertion_count": 198,
            "model_dimension": 1024,
        },
    )

    original_atomic_write = c03_embeddings._write_atomic_bytes
    injected = False

    def fail_activation_pointer(path: Path, data: bytes) -> None:
        nonlocal injected
        if path == activation_path and not injected:
            injected = True
            raise OSError("injected activation manifest failure")
        original_atomic_write(path, data)

    monkeypatch.setattr(c03_embeddings, "_write_atomic_bytes", fail_activation_pointer)

    with pytest.raises(OSError, match="injected activation manifest failure"):
        c03_embeddings.activate_candidate(
            repository_root=tmp_path,
            candidate_dir=candidate,
        )

    assert generation_path.read_bytes() == old_generation
    assert qualification_path.read_bytes() == old_qualification
    assert activation_path.read_bytes() == old_activation
    assert list(active.glob("graph_skill_embedding_activation.*.json")) == []
