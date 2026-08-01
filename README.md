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

The owned fixture suite does not create human labels, qualify a real corpus, or
authorize release. A source-bound control plane now exists under
`src/apps_rg/evals/authoritative`: it can invoke an explicit operator-supplied
Apps RG command, but reports real repeatability only when controller receipts,
human authority, truth, thresholds, and native evaluator receipts are
independently pinned.

See `MIGRATION_PROVENANCE.md` for the exact imported source state and explicit
exclusions. `SOURCE_SYNC_RECEIPT.json` binds this local main to the complete
chat-owned source history inside the original v2 import surface.
`src/apps_rg/evals/EVALUATION_SYNC_RECEIPT.json` records the later evaluator
convergence sync and its single lint-only source difference.
`src/apps_rg/evals/MEASUREMENT_VALIDITY_PLAN.md` records the subsequent
source-bound measurement remediation and remaining real-evidence gates;
`src/apps_rg/evals/MEASUREMENT_VALIDITY_IMPLEMENTATION_RECEIPT.json` seals its
code-only validation evidence.
