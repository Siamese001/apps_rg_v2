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
from pathlib import Path
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


def _completed_run_path(result: dict[str, Any]) -> Path | None:
    raw = str(result.get("artifact_dir") or "").strip()
    if not raw:
        return None
    path = Path(raw).expanduser()
    return path if path.is_dir() else None


def _read_inline_artifact(result: dict[str, Any], filename: str) -> tuple[str | None, str | None]:
    run_dir = _completed_run_path(result)
    if run_dir is None:
        return None, "run artifact directory is unavailable"
    path = run_dir / filename
    if not path.is_file():
        return None, f"required artifact was not written: {filename}"
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, f"cannot read {filename}: {type(exc).__name__}: {exc}"


def _inline_evaluations(result: dict[str, Any]) -> dict[str, Any]:
    """Return every evaluation surface without issuing another provider call."""
    run_evaluation: dict[str, Any]
    run_dir = _completed_run_path(result)
    if run_dir is None:
        run_evaluation = {"status": "UNAVAILABLE", "reason": "run artifact directory is unavailable"}
    else:
        try:
            run_evaluation = evaluate_bare_run(run_dir)
        except BarePipelineError as exc:
            run_evaluation = {"status": "UNAVAILABLE", "reason": str(exc)}
    return {
        "x1_section_checks": result.get("section_checks") or {"status": "UNAVAILABLE"},
        "x3_evaluation": result.get("evaluation") or {"status": "UNAVAILABLE"},
        "run_evaluation": run_evaluation,
    }


def _runtime_details(result: dict[str, Any]) -> dict[str, Any]:
    """Render the operational receipt without duplicating the full resume."""
    keys = (
        "pipeline",
        "command",
        "run_id",
        "status",
        "mode",
        "outcome_label",
        "failure_stage",
        "error",
        "repository",
        "target_company",
        "target_role",
        "inputs",
        "outputs",
        "provider_call_count",
        "providers",
        "stages",
        "delivery",
        "finished_at_utc",
    )
    return {key: result[key] for key in keys if key in result}


def _print_inline_run_outputs(result: dict[str, Any]) -> None:
    """Always print the product, evaluations, and execution receipt after ``run``."""
    resume, resume_error = _read_inline_artifact(result, "resume.md")
    print("FULL_RESUME", flush=True)
    print("```markdown", flush=True)
    print(resume.rstrip() if resume is not None else f"UNAVAILABLE: {resume_error}", flush=True)
    print("```", flush=True)

    print("EVALS", flush=True)
    print("```json", flush=True)
    print(json.dumps(_inline_evaluations(result), ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    print("```", flush=True)

    print("RUNTIME_DETAILS", flush=True)
    print("```json", flush=True)
    print(json.dumps(_runtime_details(result), ensure_ascii=False, indent=2, sort_keys=True), flush=True)
    print("```", flush=True)


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
    _print_inline_run_outputs(result)


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
