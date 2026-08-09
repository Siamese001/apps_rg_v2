"""Focused contracts for production-path W5 zero-provider qualification."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest


REPO_ROOT = Path(__file__).resolve().parents[4]
QUALIFICATION_PATH = (
    REPO_ROOT / "src/apps_rg/runtime/zero_llm_qualification.py"
)
PIPELINE_PATH = REPO_ROOT / "src/apps_rg/runtime/w5_end_to_end_pipeline.py"
REPLAY_PATH = REPO_ROOT / "src/apps_rg/runtime/post_runtime_replay.py"
WHOLE_RUN_EXIT_PATH = REPO_ROOT / "src/apps_rg/runtime/whole_run_exit.py"
CLI_PATH = (
    REPO_ROOT
    / "tools/apps_rg_standalone/qualify_post_runtime_zero_llm_w5.py"
)


def _load(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


subject = _load("_w5_qualification_unit", QUALIFICATION_PATH)


def _tripwire_probe() -> dict[str, Any]:
    return {
        "status": "PASS",
        "provider_attempt_blocked": True,
        "exception_type": "ProviderExecutionBlocked",
        "controlled_attempt_counters": {
            "blocked_import_attempts": 0,
            "provider_calls": 1,
            "judge_calls": 0,
            "embedding_calls": 0,
            "model_calls": 0,
            "network_attempts": 0,
            "subprocess_attempts": 0,
        },
    }


def test_w5_tripwire_is_controlled_and_excluded_from_execution_counts(
    tmp_path: Path,
) -> None:
    proof, path = subject._emit_tripwire_proof(
        output=tmp_path,
        probe=_tripwire_probe,
    )

    assert proof["status"] == "PASS"
    assert proof["controlled_attempt_counters"]["provider_calls"] == 1
    assert proof["qualification_attempt_counters_affected"] is False
    assert subject._verify_tripwire(path) == {
        "status": "PASS",
        "controlled_provider_attempts": 1,
        "actual_provider_calls": 0,
    }

    counts, _ = subject._emit_counts(
        output=tmp_path,
        integrated={
            "real_run_count": 2,
            "full_chain_execution_count": 4,
            "apps_eval_record_count": 2,
            "l6_closure_count": 2,
            "terminal_manifest_count": 2,
        },
        faults={
            "eval_failure_count": 1,
            "eval_recovery_count": 1,
            "l6_failure_count": 1,
            "l6_recovery_count": 1,
            "terminal_recovery_count": 1,
        },
        positive={"production_validator_count": 6},
    )
    subject._verify_counts(counts)
    assert counts["provider_calls"] == 0
    assert counts["controlled_tripwire_provider_attempts"] == 1
    assert counts[
        "controlled_tripwire_attempts_excluded_from_execution_counts"
    ] is True


def test_w5_binding_reopens_bytes_and_rejects_tampering(tmp_path: Path) -> None:
    artifact = tmp_path / "artifact.json"
    artifact.write_text('{"status":"PASS"}\n', encoding="utf-8")
    binding = subject._binding(
        artifact,
        root=tmp_path,
        role="artifact",
    )

    assert subject._resolve_binding(
        binding,
        root=tmp_path,
        label="artifact",
    ) == artifact.resolve()

    artifact.write_text('{"status":"FAIL"}\n', encoding="utf-8")
    with pytest.raises(
        subject.ZeroLlmQualificationError,
        match="artifact_digest_mismatch",
    ):
        subject._resolve_binding(
            binding,
            root=tmp_path,
            label="artifact",
        )


def test_w5_positive_control_runs_production_validators_under_guard(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    source.mkdir()
    (source / "saved.json").write_text("{}\n", encoding="utf-8")
    output = tmp_path / "out"
    code = r'''
import importlib.util
import json
import sys
from pathlib import Path

path = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("_w5_positive_subprocess", path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
result = module.execute_positive_control(
    source_run=Path(sys.argv[2]),
    output_dir=Path(sys.argv[3]),
)
valid, errors = module.verify_production_positive_control(
    result["manifest_path"]
)
manifest = json.loads(result["manifest_path"].read_text(encoding="utf-8"))
guard = json.loads(result["guard_path"].read_text(encoding="utf-8"))
print(json.dumps({
    "valid": valid,
    "errors": errors,
    "fixture_class": manifest["fixture_class"],
    "validator_count": len(manifest["production_validators"]),
    "fixture_product_authorized": manifest["fixture_product_authorized"],
    "fixture_pipeline_complete": manifest["fixture_pipeline_complete"],
    "production_authority_granted": manifest["production_authority_granted"],
    "publication_allowed": manifest["publication_allowed"],
    "guard_status": guard["status"],
    "attempt_counters": guard["attempt_counters"],
}, sort_keys=True))
'''
    environment = dict(os.environ)
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, (str(REPO_ROOT / "src"), environment.get("PYTHONPATH", "")))
    )
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
            str(PIPELINE_PATH),
            str(source),
            str(output),
        ],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    observed = json.loads(completed.stdout)
    assert observed == {
        "attempt_counters": {
            "blocked_import_attempts": 0,
            "embedding_calls": 0,
            "judge_calls": 0,
            "model_calls": 0,
            "network_attempts": 0,
            "provider_calls": 0,
            "subprocess_attempts": 0,
        },
        "errors": [],
        "fixture_class": "DETERMINISTIC_GOVERNED_SAVED_OUTPUT",
        "fixture_pipeline_complete": True,
        "fixture_product_authorized": True,
        "guard_status": "PASS",
        "production_authority_granted": False,
        "publication_allowed": False,
        "valid": True,
        "validator_count": 6,
    }


def test_whole_run_exit_import_boundary_remains_provider_free() -> None:
    code = r'''
import importlib.machinery
import importlib.util
import json
import sys
from pathlib import Path
from types import ModuleType

replay_path = Path(sys.argv[1]).resolve()
whole_run_exit_path = Path(sys.argv[2]).resolve()
apps_root = whole_run_exit_path.parents[1]
for name, path in {
    "apps_rg": apps_root,
    "apps_rg.runtime": apps_root / "runtime",
}.items():
    module = ModuleType(name)
    module.__package__ = name
    module.__path__ = [path.as_posix()]
    spec = importlib.machinery.ModuleSpec(name, loader=None, is_package=True)
    spec.submodule_search_locations = [path.as_posix()]
    module.__spec__ = spec
    sys.modules[name] = module

spec = importlib.util.spec_from_file_location("_w5_replay_guard", replay_path)
guard_module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = guard_module
spec.loader.exec_module(guard_module)
guard = guard_module.ZeroProviderReplayGuard()
with guard:
    __import__("apps_rg.runtime.whole_run_exit")
blocked = sorted(
    name for name in sys.modules
    if name == "openai"
    or name.startswith("openai.")
    or name == "anthropic"
    or name.startswith("anthropic.")
    or name.startswith("agentic_core")
)
print(json.dumps({
    "blocked_modules_loaded": blocked,
    "attempt_counters": guard.counters.to_dict(),
}, sort_keys=True))
'''
    environment = dict(os.environ)
    environment["PYTHONPATH"] = os.pathsep.join(
        filter(None, (str(REPO_ROOT / "src"), environment.get("PYTHONPATH", "")))
    )
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
            str(REPLAY_PATH),
            str(WHOLE_RUN_EXIT_PATH),
        ],
        cwd=REPO_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    observed = json.loads(completed.stdout)
    assert observed["blocked_modules_loaded"] == []
    assert all(value == 0 for value in observed["attempt_counters"].values())


def test_w5_modules_are_stdlib_only_and_synthetic_emitters_are_removed() -> None:
    code = r'''
import importlib.util
import json
import sys
from pathlib import Path

for index, raw in enumerate(sys.argv[1:]):
    path = Path(raw).resolve()
    spec = importlib.util.spec_from_file_location(f"_w5_import_{index}", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
blocked = sorted(
    name for name in sys.modules
    if name == "openai"
    or name.startswith("openai.")
    or name == "anthropic"
    or name.startswith("anthropic.")
    or name.startswith("agentic_core")
)
print(json.dumps({"blocked_modules_loaded": blocked}, sort_keys=True))
'''
    completed = subprocess.run(
        [
            sys.executable,
            "-c",
            code,
            str(QUALIFICATION_PATH),
            str(PIPELINE_PATH),
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout) == {"blocked_modules_loaded": []}

    qualification_source = QUALIFICATION_PATH.read_text(encoding="utf-8")
    assert "def _emit_positive_control(" not in qualification_source
    assert "def _emit_fault_matrix(" not in qualification_source
    assert "SYNTHETIC_SAVED_OUTPUT" not in qualification_source


def test_w5_cli_pins_this_checkout_ahead_of_ambient_pythonpath(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cli = _load("_w5_cli_path_unit", CLI_PATH)
    local_src = str(REPO_ROOT / "src")
    monkeypatch.setattr(sys, "path", list(sys.path))
    sys.path[:] = [item for item in sys.path if item != local_src]
    sys.path.insert(0, str(REPO_ROOT.parent / "foreign-checkout"))

    cli._pin_local_src()

    assert sys.path[0] == local_src
