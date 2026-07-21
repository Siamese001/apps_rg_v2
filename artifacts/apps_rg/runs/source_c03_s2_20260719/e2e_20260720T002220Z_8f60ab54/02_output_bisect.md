# apps_rg Output Bisect

## Section: run_preflight

### Layperson RCA

The earlier passing run had the private signing configuration needed to prove where work was routed, and its first section attempts cleared their gates and judges without a retry.

This run stopped at its first recorded check because that configuration was missing when the process started; research, resume generation, and judges never ran.

Retries did not fail one after another: zero retries were scheduled because repeating the same process with the same missing configuration could not change the result.

### Divergence And Root Cause

- First observed divergence: `PREFLIGHT` - The first divergence is the process-ingestion boundary: the passing run could sign route evidence, while the current process lacked required signing configuration.
- First causally relevant divergence: `PREFLIGHT` - The first divergence is the process-ingestion boundary: the passing run could sign route evidence, while the current process lacked required signing configuration.
- Code cause status: `EXTERNAL_CONFIGURATION_CAUSE_ISOLATED`

### Underlying Root Cause

- `environment_ingestion_root_cause` / `ISOLATED`: Required route-signing configuration was absent at process ingestion, so the run could not create signed L0 route evidence.
  - Code surface: `apps_rg/runtime/e2e_preflight.py::run_fresh_e2e_preflight`

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `PREFLIGHT` | `BASELINE_UNAVAILABLE` | `APPS_RG_ROUTE_SIGNING_CO` | `False` | `CAUSAL` | The first divergence is the process-ingestion boundary: the passing run could sign route evidence, while the current process lacked required signing configuration. | `PINNED_BASELINE_ARTIFACT_MISSING:C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\anthropic_partnership_fresh_s2e_20260630_094000\APPS_RG_MANDATORY_RUN_OUTPUT.json` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 2 | `RESEARCH` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | RESEARCH could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 3 | `U0` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | U0 could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 4 | `L1` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L1 could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 5 | `L0` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L0 could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 6 | `L2` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L2 could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 7 | `X1-X3` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | X1-X3 could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 8 | `APPS_EVAL` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | APPS_EVAL could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 9 | `L6_SHADOW` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L6_SHADOW could not run after the causal preflight block. | `-` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| configuration ingestion and fail-fast evidence | `apps_rg/runtime/e2e_preflight.py` | `run_fresh_e2e_preflight` | `True` | `PREEXISTED_BASELINE` | `RUNTIME_GATE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `preflight` | `1` | `-` | APPS_RG_ROUTE_SIGNING_CONFIGURATION_REQUIRED | stop without retry because configuration is non-retriable | `PREFLIGHT` | `FAIL` | `JUDGES_NOT_REACHED` | `BLOCKED_BEFORE_RESEARCH` | `RUN_CONTROL` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |
| 2 | `retry_decision` | `0` | `-` | The missing process configuration would be identical on every in-process retry. | require external configuration injection before a new run | `RETRY_DECISION` | `NOT_RUN` | `JUDGES_NOT_REACHED` | `NO_RETRY_SCHEDULED` | `RUN_CONTROL` | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_20260719\e2e_20260720T002220Z_8f60ab54\e2e_preflight_receipt.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `APPS_RG_ROUTE_SIGNING_PREFLIGHT` | `BASELINE_UNAVAILABLE` | `FAIL` | `True` | APPS_RG_ROUTE_SIGNING_CONFIGURATION_REQUIRED |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `BASELINE_UNAVAILABLE` | `JUDGES_NOT_REACHED` | Preflight blocked judge dispatch. |
