"""Replay existing apps_rg post-runtime evidence without provider execution."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
REPLAY_MODULE_PATH = REPO_ROOT / "src/apps_rg/runtime/post_runtime_replay.py"


def _load_replay_module() -> object:
    """Load the stdlib-only guard without executing ``apps_rg.__init__``."""

    module_name = "_apps_rg_zero_provider_replay"
    spec = importlib.util.spec_from_file_location(module_name, REPLAY_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load replay guard: {REPLAY_MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--phase",
        choices=("w0-preflight",),
        default="w0-preflight",
        help="W0 only establishes the immutable zero-provider boundary.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        replay = _load_replay_module()
        receipt = replay.run_w0_zero_provider_preflight(
            source_run=args.source_run,
            output_root=args.output_root,
            require_clean_import_state=True,
        )
    except (OSError, RuntimeError, ValueError) as exc:
        print(
            json.dumps(
                {
                    "schema_version": "apps_rg.post_runtime_replay_cli_failure.v1",
                    "status": "FAIL",
                    "phase": args.phase,
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                },
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        return 2

    print(
        json.dumps(
            {
                "status": receipt["status"],
                "wave": receipt["wave"],
                "replay_id": receipt["replay_id"],
                "receipt_path": receipt["receipt_path"],
                "semantic_digest": receipt["semantic_digest"],
                "source_manifest_sha256": receipt["source_manifest_sha256"],
                "source_unchanged": receipt["source_unchanged"],
                "provider_calls": receipt["provider_calls"],
                "judge_calls": receipt["judge_calls"],
                "embedding_calls": receipt["embedding_calls"],
                "model_calls": receipt["model_calls"],
                "network_attempts": receipt["network_attempts"],
                "subprocess_attempts": receipt["subprocess_attempts"],
                "model_span_delta": receipt["model_span_delta"],
                "apps_eval_executed": receipt["apps_eval_executed"],
                "l6_executed": receipt["l6_executed"],
                "next_wave_authorized": receipt["next_wave_authorized"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
