"""The sole public Apps RG resume command.

Use one command surface only:

``python -m apps_rg run``
``python -m apps_rg eval``
``python -m apps_rg show``
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Sequence

from apps_rg.bare_pipeline import (
    DEFAULT_TARGET_COMPANY,
    DEFAULT_TARGET_ROLE,
    BarePipelineError,
    evaluate_bare_run,
    read_bare_artifact,
    run_bare_e2e,
)

__all__ = ["_build_parser", "main"]


def _add_run_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--mode",
        choices=("live", "deterministic"),
        default="live",
        help="live uses actual providers; deterministic uses the fixed local source pack and no provider.",
    )
    parser.add_argument("--target-company", default=DEFAULT_TARGET_COMPANY)
    parser.add_argument("--target-role", default=DEFAULT_TARGET_ROLE)
    parser.add_argument(
        "--jd",
        default="",
        help="Optional JD file path or inline text. Defaults to the canonical Anthropic JD.",
    )
    parser.add_argument(
        "--resume",
        default="",
        help="Optional base-resume JSON, Markdown, or text path. Defaults to the canonical base resume.",
    )
    parser.add_argument(
        "--artifact-dir",
        default="",
        help="Optional parent directory for this run's output directory.",
    )
    parser.add_argument(
        "--fresh-e2e",
        action="store_true",
        help=argparse.SUPPRESS,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m apps_rg",
        description=(
            "The single Apps RG resume pipeline. Run a live provider proof, a no-provider deterministic "
            "proof, inspect a completed run, or print an exact output artifact."
        ),
    )
    subparsers = parser.add_subparsers(dest="action", metavar="ACTION")

    run = subparsers.add_parser("run", help="run the canonical resume pipeline")
    _add_run_arguments(run)

    evaluate = subparsers.add_parser("eval", help="re-evaluate an existing run without a provider call")
    evaluate.add_argument("--run-dir", required=True, help="Completed run directory.")
    evaluate.add_argument(
        "--compare-run-dir",
        default="",
        help="Second deterministic run directory for a normalized repeatability comparison.",
    )

    show = subparsers.add_parser("show", help="print an exact output artifact from a completed run")
    show.add_argument("--run-dir", required=True, help="Completed run directory.")
    show.add_argument(
        "--artifact",
        required=True,
        choices=("resume", "email", "research", "summary", "evaluation"),
        help="Artifact to print exactly.",
    )
    return parser


def _normalize_argv(argv: Sequence[str] | None) -> list[str]:
    values = list(sys.argv[1:] if argv is None else argv)
    if not values:
        return ["run"]
    if values[0] in {"-h", "--help"}:
        return values
    actions = {"run", "eval", "show"}
    if values[0] not in actions and values[0].startswith("-"):
        return ["run", *values]
    return values


def _print_result(result: dict[str, Any]) -> None:
    print(
        "APPS_RG "
        f"status={result.get('status', 'FAIL')} "
        f"mode={result.get('mode', '')} "
        f"outcome={result.get('outcome_label', '')} "
        f"run_dir={result.get('artifact_dir', '')}",
        flush=True,
    )
    repository = result.get("repository")
    if isinstance(repository, dict):
        print(
            "CODE "
            f"root={repository.get('repository_root', '')} "
            f"branch={repository.get('branch', '')} "
            f"commit={repository.get('commit_sha', '')} "
            f"on_local_main={repository.get('head_is_ancestor_of_local_main', False)} "
            f"dirty={repository.get('worktree_dirty', False)}",
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
    evaluation = result.get("evaluation")
    if isinstance(evaluation, dict):
        print(
            f"EVALUATION {evaluation.get('verdict', '')} score={evaluation.get('score', '')}",
            flush=True,
        )
    if result.get("error"):
        print(f"APPS_RG_ERROR {result['error']}", file=sys.stderr, flush=True)


def _print_evaluation(report: dict[str, Any]) -> None:
    print(f"APPS_RG_EVAL status={report.get('status', 'FAIL')} run_dir={report.get('run_dir', '')}")
    for name, check in (report.get("checks") or {}).items():
        if isinstance(check, dict):
            print(f"{name} {check.get('status', 'FAIL')}")
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    """Run the sole supported Apps RG resume workflow or its inspection actions."""
    parser = _build_parser()
    args = parser.parse_args(_normalize_argv(argv))
    action = args.action or "run"
    try:
        if action == "run":
            result = run_bare_e2e(
                mode=args.mode,
                target_company=args.target_company,
                target_role=args.target_role,
                jd=args.jd,
                resume_path=args.resume,
                artifact_root=args.artifact_dir,
            )
            _print_result(result)
            return 0 if result.get("status") == "SUCCESS" else 1
        if action == "eval":
            report = evaluate_bare_run(
                args.run_dir,
                compare_run_dir=args.compare_run_dir or None,
            )
            _print_evaluation(report)
            return 0 if report.get("status") == "PASS" else 1
        if action == "show":
            sys.stdout.write(read_bare_artifact(args.run_dir, args.artifact))
            return 0
    except BarePipelineError as exc:
        print(f"APPS_RG_ERROR {exc}", file=sys.stderr, flush=True)
        return 1
    parser.error(f"unsupported action: {action!r}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
