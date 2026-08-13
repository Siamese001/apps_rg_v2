"""The one public Apps RG command: a small live end-to-end resume pipeline."""

from __future__ import annotations

import argparse
import sys
from typing import Any

from apps_rg.bare_pipeline import (
    DEFAULT_TARGET_COMPANY,
    DEFAULT_TARGET_ROLE,
    run_bare_live_e2e,
)

__all__ = ["_build_parser", "main"]


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m apps_rg",
        description=(
            "Run Apps Research, live resume tailoring, outreach-email drafting, "
            "and Gemini evaluation. This is the only Apps RG CLI path."
        ),
    )
    parser.add_argument("--target-company", default=DEFAULT_TARGET_COMPANY)
    parser.add_argument("--target-role", default=DEFAULT_TARGET_ROLE)
    parser.add_argument(
        "--jd",
        default="",
        help="Job-description file path or inline job-description text. Defaults to Anthropic JD.",
    )
    parser.add_argument(
        "--resume",
        default="",
        help="Optional base-resume JSON, Markdown, or text file. Defaults to the canonical base resume.",
    )
    parser.add_argument(
        "--artifact-dir",
        default="",
        help="Optional parent directory for this run's outputs.",
    )
    parser.add_argument(
        "--fresh-e2e",
        action="store_true",
        help="Compatibility spelling for the same single fresh pipeline run.",
    )
    return parser


def _print_result(result: dict[str, Any]) -> None:
    print(
        "APPS_RG "
        f"status={result.get('status', 'FAIL')} "
        f"run_dir={result.get('artifact_dir', '')}",
        flush=True,
    )
    for stage in result.get("stages", []):
        if not isinstance(stage, dict):
            continue
        line = f"{stage.get('stage', '?')} {stage.get('status', '?')}"
        if stage.get("error"):
            line += f" {stage['error']}"
        print(line, flush=True)
    for name, provider in (result.get("providers") or {}).items():
        if not isinstance(provider, dict):
            continue
        print(
            f"PROVIDER {name} {provider.get('provider', '')} "
            f"{provider.get('observed_model', '')} {provider.get('status', '')}",
            flush=True,
        )
    if result.get("error"):
        print(f"APPS_RG_ERROR {result['error']}", file=sys.stderr, flush=True)


def main(argv: list[str] | None = None) -> int:
    """Run the sole supported Apps RG workflow."""
    args = _build_parser().parse_args(argv)
    result = run_bare_live_e2e(
        target_company=args.target_company,
        target_role=args.target_role,
        jd=args.jd,
        resume_path=args.resume,
        artifact_root=args.artifact_dir,
    )
    _print_result(result)
    return 0 if result.get("status") == "SUCCESS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
