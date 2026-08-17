"""The sole public, governed Apps RG product command.

``python -m apps_rg run`` always enters the full product flow: signed
preflight, Apps Research, the governed whole-resume runtime, Exit/UWG, Apps
Eval, L6 shadow evidence, and terminal stage-ledger sealing. It intentionally
does not expose the compact ``bare_pipeline`` as a public product route.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence


DEFAULT_TARGET_COMPANY = "Anthropic"
DEFAULT_TARGET_ROLE = "Manager of Applied AI Architecture, Partnerships"

__all__ = ["_build_parser", "evaluate_full_run", "main"]


def _add_run_arguments(parser: argparse.ArgumentParser) -> None:
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
        help=(
            "Optional fresh run directory beneath artifacts/apps_rg/runtime_proofs. "
            "Product artifacts cannot be redirected outside that governed root."
        ),
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m apps_rg",
        description=(
            "The single full Apps RG product pipeline. A successful run includes "
            "Apps Eval, L6 shadow evidence, and terminal E2E sealing."
        ),
    )
    subparsers = parser.add_subparsers(dest="action", metavar="ACTION")

    run = subparsers.add_parser("run", help="run the full governed Apps RG pipeline")
    _add_run_arguments(run)

    evaluate = subparsers.add_parser(
        "eval",
        help="verify an existing full-run Apps Eval package and E2E closure without a provider call",
    )
    evaluate.add_argument("--run-dir", required=True, help="Full governed run directory.")

    show = subparsers.add_parser("show", help="print an exact artifact from a full governed run")
    show.add_argument("--run-dir", required=True, help="Full governed run directory.")
    show.add_argument(
        "--artifact",
        required=True,
        choices=("resume", "research", "summary", "evaluation"),
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


def _run_root(value: str | Path) -> Path:
    root = Path(value).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"full Apps RG run directory is unavailable: {root}")
    return root


def _read_json_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, TypeError) as exc:
        raise ValueError(f"unreadable JSON artifact: {path}: {type(exc).__name__}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"JSON artifact is not an object: {path}")
    return dict(payload)


def _within_run_root(root: Path, reference: str | Path) -> Path | None:
    raw = Path(reference)
    candidate = raw.resolve() if raw.is_absolute() else (root / raw).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate


def _summary_from_mandatory_output(root: Path) -> tuple[Path, dict[str, Any]]:
    from apps_rg.runtime.run_output_contract import APPS_RG_MANDATORY_RUN_OUTPUT_JSON

    path = root / APPS_RG_MANDATORY_RUN_OUTPUT_JSON
    payload = _read_json_object(path)
    summary = payload.get("result_summary")
    if not isinstance(summary, Mapping):
        raise ValueError(f"mandatory run output has no result_summary: {path}")
    return path, dict(summary)


def _referenced_eval_record_path(root: Path, summary: Mapping[str, Any]) -> Path | None:
    """Resolve the sealed Apps Eval record named by the run's result summary.

    Apps Eval owns a suite/run subdirectory beneath ``apps_eval``.  The
    summary is the run-specific, contained reference; treating the parent
    directory as the package root loses that binding and can accidentally
    inspect an unrelated evaluation package.
    """

    reference = str(summary.get("apps_eval_record_ref") or "").strip()
    path = _within_run_root(root, reference) if reference else None
    if path is not None and path.name == "eval_record.json" and path.is_file():
        return path
    legacy_path = root / "apps_eval" / "eval_record.json"
    return legacy_path if legacy_path.is_file() else None


def _ledger_terminal_state(root: Path) -> dict[str, Any]:
    """Read the immutable product completion state from the sealed ledger."""

    payload = _read_json_object(root / "e2e_stage_ledger.json")
    terminal_state = payload.get("terminal_state")
    return dict(terminal_state) if isinstance(terminal_state, Mapping) else {}


def _post_x3_completion(root: Path) -> dict[str, Any]:
    """Read the persisted post-X3 decision that the terminal ledger seals."""

    return _read_json_object(root / "apps_rg_post_x3_completion_receipt.json")


def _evaluation_exit_code(checks: Mapping[str, Mapping[str, Any]]) -> int:
    """Return stable public exit classes without concealing why eval failed."""

    if all(row.get("status") == "PASS" for row in checks.values()):
        return 0
    decision = checks.get("evaluation_decision") or {}
    if decision.get("status") == "FAIL":
        if decision.get("evaluation_validity") != "PASS" or decision.get(
            "l6_integrity_status"
        ) != "PASS":
            return 3  # evaluation invalid or independent assurance failed
        if decision.get("deterministic_product_status") != "PASS":
            return 2  # product / review-required outcome
    if (checks.get("apps_eval") or {}).get("status") == "FAIL" or (
        checks.get("l6_assurance") or {}
    ).get("status") == "FAIL":
        return 3
    return 4  # execution/terminal-artifact failure


def evaluate_full_run(run_dir: str | Path) -> dict[str, Any]:
    """Verify a closed product run's E2E ledger and Apps Eval package.

    This is deliberately read-only: a missing or invalid Apps Eval package is
    a failed full run, not a reason for the CLI to run evaluation late.
    """

    root = _run_root(run_dir)
    checks: dict[str, dict[str, Any]] = {}
    try:
        mandatory_path, summary = _summary_from_mandatory_output(root)
    except ValueError as exc:
        return {
            "status": "FAIL",
            "run_dir": str(root),
            "checks": {"mandatory_output": {"status": "FAIL", "error": str(exc)}},
            "exit_code": 4,
        }

    checks["mandatory_output"] = {"status": "PASS", "path": str(mandatory_path)}

    from apps_rg.runtime.e2e_stage_ledger import verify_e2e_stage_ledger

    ledger_path = root / "e2e_stage_ledger.json"
    ledger = verify_e2e_stage_ledger(ledger_path)
    checks["e2e_stage_ledger"] = {
        "status": "PASS" if ledger.valid and ledger.complete else "FAIL",
        "valid": ledger.valid,
        "complete": ledger.complete,
        "errors": list(ledger.errors),
    }
    try:
        terminal_state = _ledger_terminal_state(root)
    except ValueError as exc:
        terminal_state = {}
        terminal_state_error = str(exc)
    else:
        terminal_state_error = ""
    checks["product_authorization"] = {
        "status": "PASS"
        if ledger.valid and terminal_state.get("product_authorized") is True
        else "FAIL",
        "product_authorized": terminal_state.get("product_authorized"),
        "source": "e2e_stage_ledger.terminal_state",
        "error": terminal_state_error,
    }
    checks["pipeline_completion"] = {
        "status": "PASS"
        if ledger.valid
        and ledger.complete
        and terminal_state.get("pipeline_complete") is True
        else "FAIL",
        "pipeline_complete": terminal_state.get("pipeline_complete"),
        "source": "e2e_stage_ledger.terminal_state",
        "error": terminal_state_error,
    }

    from apps_eval.runner.core import verify_apps_rg_eval_package_seal

    eval_record_path = _referenced_eval_record_path(root, summary)
    eval_root = eval_record_path.parent if eval_record_path is not None else root / "apps_eval"
    eval_valid, eval_errors = verify_apps_rg_eval_package_seal(eval_root)
    checks["apps_eval"] = {
        "status": "PASS" if eval_valid else "FAIL",
        "package_root": str(eval_root),
        "errors": list(eval_errors),
    }

    try:
        post_x3 = _post_x3_completion(root)
    except ValueError as exc:
        post_x3 = {}
        post_x3_error = str(exc)
    else:
        post_x3_error = ""
    post_eval = post_x3.get("apps_eval")
    post_eval = dict(post_eval) if isinstance(post_eval, Mapping) else {}
    post_l6 = post_x3.get("l6_shadow")
    post_l6 = dict(post_l6) if isinstance(post_l6, Mapping) else {}
    candidate_ref = str(post_eval.get("candidate_evaluation_manifest_ref") or "")
    candidate_path = _within_run_root(root, candidate_ref) if candidate_ref else None
    candidate_errors: list[str]
    if candidate_path is None or not candidate_path.is_file():
        candidate_errors = ["candidate_evaluation_manifest_missing"]
    else:
        from apps_rg.runtime.evaluation_manifest import (
            validate_candidate_evaluation_manifest,
        )

        _candidate_manifest, candidate_errors = validate_candidate_evaluation_manifest(root)

    l6_reference = str(post_l6.get("l6_evaluation_audit_ref") or "")
    l6_path = _within_run_root(root, l6_reference) if l6_reference else None
    l6_audit: dict[str, Any] = {}
    l6_error = ""
    if l6_path is not None and l6_path.is_file():
        try:
            l6_audit = _read_json_object(l6_path)
        except ValueError as exc:
            l6_error = str(exc)
    checks["evaluation_decision"] = {
        "status": "PASS"
        if post_x3_error == ""
        and post_eval.get("execution_status") == "PASS"
        and post_eval.get("evaluation_validity") == "PASS"
        and post_eval.get("deterministic_product_status") == "PASS"
        and post_l6.get("l6_integrity_status") == "PASS"
        and not candidate_errors
        else "FAIL",
        "execution_status": post_eval.get("execution_status"),
        "evaluation_validity": post_eval.get("evaluation_validity"),
        "deterministic_product_status": post_eval.get(
            "deterministic_product_status"
        ),
        "l6_integrity_status": post_l6.get("l6_integrity_status"),
        "candidate_manifest_ref": candidate_ref,
        "candidate_manifest_errors": list(candidate_errors),
        "error": post_x3_error,
    }
    checks["l6_assurance"] = {
        "status": "PASS"
        if l6_path is not None
        and l6_path.is_file()
        and not l6_error
        and l6_audit.get("schema_version") == "apps_rg.l6_evaluation_audit.v2"
        and l6_audit.get("l6_integrity_status") == "PASS"
        and l6_audit.get("grain_parity_status") == "PASS"
        and l6_audit.get("apps_eval_rows_bound") is True
        and l6_audit.get("independent_observations") is True
        else "FAIL",
        "reference": l6_reference,
        "l6_integrity_status": l6_audit.get("l6_integrity_status"),
        "row_binding": l6_audit.get("apps_eval_rows_bound"),
        "error": l6_error,
    }

    from apps_rg.runtime.run_output_contract import FINAL_RESUME_OUTPUT_TXT

    final_resume = root / FINAL_RESUME_OUTPUT_TXT
    checks["final_resume"] = {
        "status": "PASS" if final_resume.is_file() and final_resume.stat().st_size > 0 else "FAIL",
        "path": str(final_resume),
    }
    status = "PASS" if all(row["status"] == "PASS" for row in checks.values()) else "FAIL"
    return {
        "status": status,
        "run_dir": str(root),
        "checks": checks,
        "exit_code": _evaluation_exit_code(checks),
    }


def _result_run_dir(result: Mapping[str, Any]) -> Path | None:
    raw = str(result.get("artifact_dir") or "").strip()
    if not raw:
        return None
    candidate = Path(raw).expanduser()
    return candidate if candidate.is_dir() else None


def _evaluation_for_result(result: Mapping[str, Any]) -> dict[str, Any]:
    root = _result_run_dir(result)
    if root is None:
        return {
            "status": "FAIL",
            "exit_code": 4,
            "checks": {
                "run_artifact_directory": {
                    "status": "FAIL",
                    "error": "full run artifact directory is unavailable",
                }
            },
        }
    return evaluate_full_run(root)


def _read_full_artifact(run_dir: str | Path, artifact: str) -> str:
    root = _run_root(run_dir)
    from apps_rg.runtime.dispatch import spine_stage_receipts as stage_receipts
    from apps_rg.runtime.run_output_contract import (
        APPS_RG_MANDATORY_RUN_OUTPUT_JSON,
        FINAL_RESUME_OUTPUT_TXT,
    )

    filenames = {
        "resume": FINAL_RESUME_OUTPUT_TXT,
        "research": stage_receipts.FILENAME_DELEGATED_BRIEFING,
        "summary": APPS_RG_MANDATORY_RUN_OUTPUT_JSON,
    }
    requested = str(artifact).strip().casefold()
    if requested == "evaluation":
        _, summary = _summary_from_mandatory_output(root)
        path = _referenced_eval_record_path(root, summary)
        if path is None:
            raise ValueError("run summary does not reference a readable Apps Eval record")
    else:
        path = root / filenames[requested]
    if not path.is_file():
        raise ValueError(f"run artifact does not exist: {path}")
    return path.read_text(encoding="utf-8")


def _print_run_result(result: Mapping[str, Any], evaluation: Mapping[str, Any]) -> None:
    succeeded = evaluation.get("status") == "PASS"
    print(
        "APPS_RG "
        f"status={'SUCCESS' if succeeded else 'FAIL'} "
        f"product_authorized={result.get('product_authorized', False)} "
        f"pipeline_complete={result.get('pipeline_complete', False)} "
        f"run_dir={result.get('artifact_dir', '')}",
        flush=True,
    )

    root = _result_run_dir(result)
    from apps_rg.runtime.run_output_contract import FINAL_RESUME_OUTPUT_TXT

    resume_path = root / FINAL_RESUME_OUTPUT_TXT if root is not None else None
    resume_text = "UNAVAILABLE: final resume artifact was not emitted"
    if resume_path is not None and resume_path.is_file():
        try:
            resume_text = resume_path.read_text(encoding="utf-8").rstrip()
        except OSError as exc:
            resume_text = f"UNAVAILABLE: cannot read final resume artifact ({type(exc).__name__})"
    print("FULL_RESUME", flush=True)
    print(resume_text, flush=True)

    print("EVALS", flush=True)
    print(json.dumps(evaluation, ensure_ascii=False, indent=2, sort_keys=True), flush=True)

    detail_keys = (
        "exit_status",
        "execution_status",
        "completion_status",
        "fault",
        "run_id",
        "request_id",
        "artifact_dir",
        "product_authorized",
        "pipeline_complete",
        "e2e_stage_ledger",
        "e2e_stage_ledger_valid",
        "e2e_stage_ledger_complete",
        "apps_eval_record_ref",
        "l6_shadow_bridge_ref",
        "mandatory_run_output_json",
    )
    print("RUNTIME_DETAILS", flush=True)
    print(json.dumps({key: result[key] for key in detail_keys if key in result}, indent=2, sort_keys=True), flush=True)
    if not succeeded:
        print(
            "APPS_RG_ERROR " + str(result.get("fault") or "FULL_E2E_OR_APPS_EVAL_INCOMPLETE"),
            file=sys.stderr,
            flush=True,
        )


def _print_evaluation(report: Mapping[str, Any]) -> None:
    print(f"APPS_RG_EVAL status={report.get('status', 'FAIL')} run_dir={report.get('run_dir', '')}")
    for name, check in (report.get("checks") or {}).items():
        if isinstance(check, Mapping):
            print(f"{name} {check.get('status', 'FAIL')}")
    print(json.dumps(dict(report), ensure_ascii=False, indent=2, sort_keys=True))


def main(argv: list[str] | None = None) -> int:
    """Run or inspect the one full Apps RG product workflow."""

    parser = _build_parser()
    args = parser.parse_args(_normalize_argv(argv))
    action = args.action or "run"
    try:
        if action == "run":
            from apps_rg.runtime.orchestration.canonical_dispatch import (
                run_canonical_apps_rg_from_cli_primitives,
            )

            result = run_canonical_apps_rg_from_cli_primitives(
                target_company=args.target_company,
                target_role=args.target_role,
                jd=args.jd,
                resume_path=args.resume,
                artifact_dir=args.artifact_dir,
            )
            evaluation = _evaluation_for_result(result)
            _print_run_result(result, evaluation)
            return int(evaluation.get("exit_code", 0 if evaluation.get("status") == "PASS" else 1))
        if action == "eval":
            report = evaluate_full_run(args.run_dir)
            _print_evaluation(report)
            return int(report.get("exit_code", 0 if report.get("status") == "PASS" else 1))
        if action == "show":
            sys.stdout.write(_read_full_artifact(args.run_dir, args.artifact))
            return 0
    except Exception as exc:  # noqa: BLE001 - public CLI must return a useful nonzero result.
        print(f"APPS_RG_ERROR {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        return 1
    parser.error(f"unsupported action: {action!r}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
