# Apps RG V2

Local `main` integration target for the simplified `apps_rg` extraction.

This initial commit is a provenance-preserving source transplant from the
Agentic Workflow source-refreeze and standalone worktrees. It is intentionally
not yet an independently installable package: packaging, import reconciliation,
and behavior-parity certification are later refactoring waves.

The complete six-wave offline evaluation surface is now implemented under
`src/apps_rg/evals`. It provides the G1-G6 measurement contract, modular
resume-graph metrics, section and whole-resume quality evaluation, stored-run
repeatability, critical-grader mutation testing, and seven-receipt CI
ratcheting. Run its owned suite with:

`PYTHONPATH=C:\Git\apps_rg_v2\src python -m pytest -q src/apps_rg/evals`

This evaluation implementation does not make the repository independently
installable, invoke the Apps RG runtime, create human labels, qualify real-run
repeatability, or authorize release.

See `MIGRATION_PROVENANCE.md` for the exact imported source state and explicit
exclusions. `SOURCE_SYNC_RECEIPT.json` binds this local main to the complete
chat-owned source history inside the original v2 import surface.
`src/apps_rg/evals/EVALUATION_SYNC_RECEIPT.json` records the later evaluator
convergence sync and its single lint-only source difference.
