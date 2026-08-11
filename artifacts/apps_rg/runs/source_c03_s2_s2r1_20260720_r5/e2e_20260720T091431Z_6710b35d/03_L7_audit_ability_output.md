## 3. L7 Audit Ability Output

| Artifact | Path | Status |
|---|---|---|
| **HOW trace** | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_rg_how_trace.json` | `PRESENT` |
| **Route-family coverage** | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_rg_l7_route_family_coverage.json` | `PRESENT` |
| **Spine proof** | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_rg_spine_proof.json` | `PRESENT` |

| Signal | Value |
|---|---|
| Evidence plane | `L7_AUDITABILITY` |
| HOW trace class | `NOT_OBSERVED` |
| Spine proof class | `NOT_OBSERVED` |
| Certified route families | `1 / 9` |

Certified: **1 / 9** | fixture-only: 1 | not certified: 8

| Family | Status | Proof class | Exercised |
|---|---|---|---|
| `R1A_EXACT_CACHE` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `R1B_SEMANTIC_CACHE` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `R3_GROUNDED_READ` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `R4_SINGLE_ACTION` | ✅ CERTIFIED | `REAL_RUNTIME` | ✅ |
| `R5_FALLBACK` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `MANAGED_WORKFLOW_STRUCTURAL` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `MANAGED_WORKFLOW_REAL_EXECUTION` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `UWG_COMMIT_PATH` | ❌ NOT_CERTIFIED | `MISSING` | ❌ |
| `UWG_BLOCK_PATH` | ❌ NOT_CERTIFIED | `FIXTURE_ONLY` | ❌ |
