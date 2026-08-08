from __future__ import annotations


def test_whole_resume_cli_refuses_to_bypass_fresh_e2e(
    capsys,
) -> None:
    from apps_rg.__main__ import main

    assert main([]) == 2
    assert "whole-resume product runs require --fresh-e2e" in capsys.readouterr().err
