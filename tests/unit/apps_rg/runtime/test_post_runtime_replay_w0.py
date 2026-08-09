"""W0 acceptance for immutable, zero-provider post-runtime replay."""

from __future__ import annotations

import importlib
import json
import os
import socket
import subprocess
import sys
from pathlib import Path

import pytest

from apps_rg.runtime.post_runtime_replay import (
    NetworkExecutionBlocked,
    PostRuntimeReplaySafetyError,
    ProviderExecutionBlocked,
    SubprocessExecutionBlocked,
    ZeroProviderReplayGuard,
    build_source_manifest,
    compare_source_manifests,
    run_w0_zero_provider_preflight,
)

REPO_ROOT = Path(__file__).resolve().parents[4]
REPLAY_TOOL = REPO_ROOT / "tools/apps_rg_standalone/reconcile_existing_run_post_runtime.py"


def _source_run(root: Path) -> Path:
    source = root / "source_run"
    (source / "modular_r4" / "sections" / "headline").mkdir(parents=True)
    (source / "route_contract.json").write_text(
        '{"schema_version":"route.v1"}\n',
        encoding="utf-8",
    )
    (source / "modular_r4" / "sections" / "headline" / "l2_output.json").write_text(
        '{"status":"REAL_LLM"}\n',
        encoding="utf-8",
    )
    return source


def test_w0_preflight_is_deterministic_and_source_immutable(tmp_path: Path) -> None:
    source = _source_run(tmp_path)
    output = tmp_path / "derived_replay"
    before = build_source_manifest(source)

    first = run_w0_zero_provider_preflight(source_run=source, output_root=output)
    second = run_w0_zero_provider_preflight(source_run=source, output_root=output)
    after = build_source_manifest(source)

    assert first["status"] == "PASS"
    assert first["semantic_digest"] == second["semantic_digest"]
    assert first["source_manifest_sha256"] == second["source_manifest_sha256"]
    assert first["receipt_path"] == second["receipt_path"]
    assert compare_source_manifests(before, after)["unchanged"] is True
    assert first["source_unchanged"] is True
    assert first["next_wave_authorized"] is True
    assert first["apps_eval_executed"] is False
    assert first["l6_executed"] is False
    assert all(value == 0 for value in first["attempt_counters"].values())

    persisted = json.loads(Path(first["receipt_path"]).read_text(encoding="utf-8"))
    assert persisted["semantic_digest"] == first["semantic_digest"]


def test_w0_rejects_output_inside_or_above_source(tmp_path: Path) -> None:
    source = _source_run(tmp_path)

    with pytest.raises(PostRuntimeReplaySafetyError, match="inside"):
        run_w0_zero_provider_preflight(
            source_run=source,
            output_root=source / "derived",
        )
    with pytest.raises(PostRuntimeReplaySafetyError, match="contain"):
        run_w0_zero_provider_preflight(
            source_run=source,
            output_root=tmp_path,
        )


def test_guard_scrubs_credentials_and_blocks_every_escape_path(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "must-not-be-observable")
    monkeypatch.delenv("APPS_RG_POST_RUNTIME_NO_PROVIDER", raising=False)
    guard = ZeroProviderReplayGuard()

    with guard:
        assert "OPENAI_API_KEY" not in os.environ
        assert os.environ["APPS_RG_POST_RUNTIME_NO_PROVIDER"] == "1"
        assert os.environ["APPS_EVAL_WITH_JUDGE"] == "0"

        with pytest.raises(NetworkExecutionBlocked):
            socket.create_connection(("example.invalid", 443))
        with pytest.raises(NetworkExecutionBlocked):
            socket.getaddrinfo("example.invalid", 443)
        with pytest.raises(SubprocessExecutionBlocked):
            subprocess.run([sys.executable, "-c", "print('blocked')"], check=False)
        with pytest.raises(ProviderExecutionBlocked):
            guard.block_attempt("provider", "unit.provider")
        with pytest.raises(ProviderExecutionBlocked):
            guard.block_attempt("model", "unit.model")
        with pytest.raises(ProviderExecutionBlocked):
            guard.block_attempt("judge", "unit.judge")
        with pytest.raises(ProviderExecutionBlocked):
            guard.block_attempt("embedding", "unit.embedding")

    assert os.environ["OPENAI_API_KEY"] == "must-not-be-observable"
    assert "APPS_RG_POST_RUNTIME_NO_PROVIDER" not in os.environ
    assert "OPENAI_API_KEY" in guard.credentials_scrubbed
    assert guard.counters.network_attempts == 2
    assert guard.counters.subprocess_attempts == 1
    assert guard.counters.provider_calls == 1
    assert guard.counters.model_calls == 1
    assert guard.counters.judge_calls == 1
    assert guard.counters.embedding_calls == 1


def test_guard_blocks_provider_import_before_module_resolution() -> None:
    module_name = "w0_fake_provider_sdk"
    sys.modules.pop(module_name, None)
    guard = ZeroProviderReplayGuard(forbidden_import_prefixes=(module_name,))

    with guard:
        with pytest.raises(ProviderExecutionBlocked, match=module_name):
            importlib.import_module(module_name)

    assert guard.counters.blocked_import_attempts == 1
    assert guard.counters.provider_calls == 1


def test_source_manifest_reports_exact_mutation(tmp_path: Path) -> None:
    source = _source_run(tmp_path)
    before = build_source_manifest(source)
    changed = source / "route_contract.json"
    changed.write_text('{"schema_version":"route.v2"}\n', encoding="utf-8")
    (source / "added.json").write_text("{}\n", encoding="utf-8")
    after = build_source_manifest(source)

    delta = compare_source_manifests(before, after)

    assert delta["unchanged"] is False
    assert delta["changed_files"] == ["route_contract.json"]
    assert delta["added_files"] == ["added.json"]


def test_cli_enters_clean_guard_before_apps_rg_package_import(tmp_path: Path) -> None:
    source = _source_run(tmp_path)
    output = tmp_path / "cli_replay"

    completed = subprocess.run(
        [
            sys.executable,
            str(REPLAY_TOOL),
            "--source-run",
            str(source),
            "--output-root",
            str(output),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    summary = json.loads(completed.stdout)
    receipt = json.loads(Path(summary["receipt_path"]).read_text(encoding="utf-8"))
    assert receipt["clean_import_state_required"] is True
    assert receipt["clean_import_state"] is True
    assert receipt["preloaded_forbidden_modules"] == []
    assert all(value == 0 for value in receipt["attempt_counters"].values())
