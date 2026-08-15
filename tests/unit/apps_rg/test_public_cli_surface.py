"""Guard the one supported Apps RG end-to-end command surface."""

from __future__ import annotations

from pathlib import Path

import pytest

from apps_rg.__main__ import _build_parser


REPO_ROOT = Path(__file__).resolve().parents[3]
PUBLIC_CLI_MODULE = REPO_ROOT / "src" / "apps_rg" / "__main__.py"
PUBLIC_DOCUMENTS = (
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "APPS_RG_V2_CANONICAL_ENTRYPOINTS.md",
    REPO_ROOT / "src" / "apps_rg" / "runtime" / "RUNBOOK_E2E.md",
    REPO_ROOT / "src" / "apps_rg" / "config" / "targeting" / "README.md",
)


def test_public_cli_exposes_only_run_eval_and_show_actions() -> None:
    parser = _build_parser()
    subparsers = next(action for action in parser._actions if action.dest == "action")

    assert set(subparsers.choices) == {"run", "eval", "show"}
    assert parser.parse_args(["run", "--mode", "deterministic"]).action == "run"
    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(["run", "--section", "executive_summary"])
    assert excinfo.value.code == 2


def test_only_public_module_cli_invokes_the_whole_resume_runner() -> None:
    executable_whole_resume_modules: list[Path] = []
    for path in (REPO_ROOT / "src" / "apps_rg").rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        if 'if __name__ == "__main__"' in text and "run_bare_e2e(" in text:
            executable_whole_resume_modules.append(path)

    assert executable_whole_resume_modules == [PUBLIC_CLI_MODULE]


def test_retired_pre_run_cli_is_physically_absent() -> None:
    assert not (REPO_ROOT / "src" / "apps_rg" / "runtime" / "prepare_orchestrator_inputs.py").exists()


def test_public_documentation_contains_no_retired_top_level_command_shape() -> None:
    for path in PUBLIC_DOCUMENTS:
        text = path.read_text(encoding="utf-8")
        assert "python -m apps_rg --" not in text, path.as_posix()
        assert "python -m apps_rg.runtime.prepare_orchestrator_inputs" not in text, path.as_posix()
