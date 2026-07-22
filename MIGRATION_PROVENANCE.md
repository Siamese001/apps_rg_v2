# Migration Provenance

## Imported source

- Repository: `C:\Git\Agentic-Workflow-FRESH`
- Worktree: `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze`
- Branch: `codex-apps-rg-source-refreeze`
- Commit: `f42e05c6f80f26b61505a42d193dae58215bd7cb`
- Relation to the frozen source main: 21 commits ahead, 0 behind.

The five role-context retrieval files that were uncommitted during the initial
transplant are now bound by source commit `f42e05c6f80f26b61505a42d193dae58215bd7cb`:

- `apps_research/engines/company_brief_engine.py`
- `apps_research/engines/query_decomposer.py`
- `tests/unit/apps_research/engines/test_company_brief_engine.py`
- `tests/unit/apps_research/engines/test_query_decomposer_retrieval_contract.py`
- `tests/unit/apps_research/test_s2_grounded_retrieval_recovery.py`

`apps_rg/runtime/sections/competencies_lane_runtime.py` had no content diff and
therefore required no source commit.

The standalone diagnostic tooling was imported from
`C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-standalone`, where it
was uncommitted at import time.

## Imported paths

- `src/apps_rg/`
- `src/apps_research/`
- `src/apps_eval/`
- `config/`
- `data/`
- `tests/apps_rg/`
- `tests/apps_research/`
- `tests/unit/apps_rg/`
- `tests/unit/apps_research/`
- `tools/apps_rg_standalone/`
- `tests/unit/tools/apps_rg_standalone/`
- `artifacts/apps_rg/`
- `artifacts/apps_rg_source_refreeze/`

## Explicit exclusions

- `agentic_core/**` remains in the Agentic Workflow source repository.
- Source-only ADRs, source plans, `ops_scripts/apps_rg/**`, and
  `tests/**/agentic_core/**` remain in the source repository under the approved
  Wave 1 import boundary.
- `.runtime/**`, Python bytecode, and test caches were not imported.
- The source-refreeze branch was not merged into Agentic Workflow `main`.
- This target does not yet contain standalone packaging or a parity claim.

## Local main authority

`C:\Git\apps_rg_v2` on branch `main` is the local integration authority for
the imported Apps RG v2 surface. Agentic Workflow remains the provenance
source; its local `main` is not the v2 delivery branch.

The synchronization receipt in `SOURCE_SYNC_RECEIPT.json` proves that all 85
chat-changed files inside the approved import surface match the source head by
exact SHA-256 file bytes. The 22 source-only paths outside that surface are
listed explicitly in the receipt. No source-only authority was silently copied
into this repository.
