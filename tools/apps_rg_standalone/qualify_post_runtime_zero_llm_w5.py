"""Qualify two sealed post-runtime replay chains without any provider calls."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
REPLAY_MODULE_PATH = REPO_ROOT / "src/apps_rg/runtime/post_runtime_replay.py"
QUALIFICATION_MODULE_PATH = (
    REPO_ROOT / "src/apps_rg/runtime/zero_llm_qualification.py"
)


def _load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-run",
        action="append",
        type=Path,
        required=True,
        help="Preserved source run; provide exactly twice.",
    )
    parser.add_argument(
        "--replay-root",
        action="append",
        type=Path,
        required=True,
        help="Matching W0-W4 replay root; provide exactly twice.",
    )
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args(argv)
    if len(args.source_run) != 2 or len(args.replay_root) != 2:
        parser.error("W5 requires exactly two --source-run and --replay-root values")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    replay = _load_module("_apps_rg_post_runtime_replay_w5", REPLAY_MODULE_PATH)
    qualification = _load_module(
        "_apps_rg_zero_llm_qualification_w5", QUALIFICATION_MODULE_PATH
    )
    run_inputs = [
        {"source_run": source, "replay_root": replay_root}
        for source, replay_root in zip(
            args.source_run, args.replay_root, strict=True
        )
    ]

    def _provider_tripwire_probe() -> dict[str, Any]:
        controlled_guard = replay.ZeroProviderReplayGuard()
        exception_type = ""
        blocked = False
        try:
            controlled_guard.block_attempt(
                "provider", "w5.controlled_provider_tripwire"
            )
        except replay.ProviderExecutionBlocked as exc:
            exception_type = type(exc).__name__
            blocked = True
        return {
            "status": "PASS" if blocked else "FAIL",
            "provider_attempt_blocked": blocked,
            "exception_type": exception_type,
            "controlled_attempt_counters": controlled_guard.counters.to_dict(),
        }

    def _operation(_source: Path, output_dir: Path) -> dict[str, Any]:
        return qualification.emit_w5_zero_llm_qualification(
            run_inputs=run_inputs,
            output_dir=output_dir,
            source_manifest_builder=replay.build_source_manifest,
            provider_tripwire_probe=_provider_tripwire_probe,
        )

    try:
        receipt = replay.run_guarded_artifact_replay(
            source_run=args.source_run[0],
            output_root=args.output_root,
            wave="W5",
            operation=_operation,
            receipt_filename="w5_zero_provider_guard_receipt.json",
            require_clean_import_state=True,
            expected_activity={
                "apps_eval_executed": False,
                "l6_executed": False,
                "uwg_operation_attempted": False,
            },
        )
    except (OSError, RuntimeError, ValueError) as exc:
        print(
            json.dumps(
                {
                    "status": "FAIL",
                    "wave": "W5",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                },
                sort_keys=True,
            )
        )
        return 1

    operation = receipt["operation_result"]
    completion = operation["completion"]
    summary = {
        "status": receipt["status"],
        "wave": receipt["wave"],
        "qualification_status": completion["status"],
        "scope_complete": completion["scope_complete"],
        "w6_authorized": completion["w6_authorized"],
        "positive_control_fixture_status": completion[
            "positive_control_fixture"
        ]["status"],
        "real_run_ids": completion["real_run_ids"],
        "record_ids": completion["record_ids"],
        "provider_calls": receipt["provider_calls"],
        "judge_calls": receipt["judge_calls"],
        "embedding_calls": receipt["embedding_calls"],
        "model_calls": receipt["model_calls"],
        "network_attempts": receipt["network_attempts"],
        "subprocess_attempts": receipt["subprocess_attempts"],
        "model_span_delta": receipt["model_span_delta"],
        "source_files_changed": completion["source_files_changed"],
        "apps_eval_records": completion["apps_eval_records"],
        "l6_terminal_closures": completion["l6_terminal_closures"],
        "non_product_terminal_manifests": completion[
            "non_product_terminal_manifests"
        ],
        "new_uwg_operations": completion["new_uwg_operations"],
        "eval_error_receipt_durable": completion[
            "injected_eval_exception"
        ]["durable_error_receipt"],
        "l6_resumed_from_l6_only": completion["injected_l6_exception"][
            "resumed_from_l6_only"
        ],
        "deterministic_replay_count": completion["determinism_replay"][
            "execution_count"
        ],
        "deterministic_artifact_bytes_stable": completion[
            "determinism_replay"
        ]["artifact_bytes_stable"],
        "qualification_dir": operation["qualification_dir"],
        "receipt_path": receipt["receipt_path"],
        "semantic_digest": receipt["semantic_digest"],
    }
    print(json.dumps(summary, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
