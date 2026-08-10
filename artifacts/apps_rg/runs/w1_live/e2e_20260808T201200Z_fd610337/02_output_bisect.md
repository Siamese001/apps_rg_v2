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
| 1 | `PREFLIGHT` | `BASELINE_UNAVAILABLE` | `PINNED_BASELINE_PREFLIGH` | `False` | `CAUSAL` | The first divergence is the process-ingestion boundary: the passing run could sign route evidence, while the current process lacked required signing configuration. | `PINNED_BASELINE_DIGEST_MISMATCH:expected=3270158fd4c3bf52d8c97b24254d2c3d0365956ef416b50d6936090f5e6cd128:observed=91d3227e01b8fa39e9b7e31f8369a50d43f0ce5c353702794150cfcb9e5dd29d` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 2 | `RESEARCH` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | RESEARCH could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 3 | `U0` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | U0 could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 4 | `L1` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L1 could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 5 | `L0` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L0 could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 6 | `L2` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L2 could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 7 | `X1-X3` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | X1-X3 could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 8 | `APPS_EVAL` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | APPS_EVAL could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 9 | `L6_SHADOW` | `BASELINE_UNAVAILABLE` | `NOT_REACHED` | `False` | `DOWNSTREAM_EFFECT` | L6_SHADOW could not run after the causal preflight block. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |

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
| 1 | `preflight` | `1` | `-` | PINNED_BASELINE_PREFLIGHT_FAILED | stop without retry because configuration is non-retriable | `PREFLIGHT` | `FAIL` | `JUDGES_NOT_REACHED` | `BLOCKED_BEFORE_RESEARCH` | `RUN_CONTROL` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |
| 2 | `retry_decision` | `0` | `-` | The missing process configuration would be identical on every in-process retry. | require external configuration injection before a new run | `RETRY_DECISION` | `NOT_RUN` | `JUDGES_NOT_REACHED` | `NO_RETRY_SCHEDULED` | `RUN_CONTROL` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201200Z_fd610337\e2e_preflight_receipt.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `APPS_RG_ROUTE_SIGNING_PREFLIGHT` | `BASELINE_UNAVAILABLE` | `FAIL` | `True` | PINNED_BASELINE_PREFLIGHT_FAILED |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `BASELINE_UNAVAILABLE` | `JUDGES_NOT_REACHED` | Preflight blocked judge dispatch. |
