# Migration Provenance

## Imported source

- Repository: `C:\Git\Agentic-Workflow-FRESH`
- Worktree: `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze`
- Branch: `codex-apps-rg-source-refreeze`
- Commit: `61addc9ec6322b75d692d14f3694552d04bd9b93`
- Relation to `origin/main`: 20 commits ahead, 0 behind at import time.

The import intentionally includes the source worktree's local, uncommitted
changes in these paths:

- `apps_research/engines/company_brief_engine.py`
- `apps_research/engines/query_decomposer.py`
- `apps_rg/runtime/sections/competencies_lane_runtime.py`
- `tests/unit/apps_research/engines/test_company_brief_engine.py`
- `tests/unit/apps_research/engines/test_query_decomposer_retrieval_contract.py`
- `tests/unit/apps_research/test_s2_grounded_retrieval_recovery.py`

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
- `.runtime/**`, Python bytecode, and test caches were not imported.
- The source-refreeze branch was not merged into Agentic Workflow `main`.
- This target does not yet contain standalone packaging or a parity claim.
