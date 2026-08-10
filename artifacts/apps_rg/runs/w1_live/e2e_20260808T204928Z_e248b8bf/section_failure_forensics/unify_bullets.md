# Section Failure Forensics - unify_bullets

- failure_type: `independent_failure`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T204928Z_e248b8bf\apps_research\runs\bridge_rg_research_bridge_d3f29352_8bc5b71d-03ec-4c41-a003-6f4aad5b5b5d\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 3.0/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass X1D decisive judge failure: model-backed judge rejected section product quality..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `183f4e91c963c5b88094380b5f9a6f97887e147617549032c39eee34049c1ad5` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T204928Z_e248b8bf\modular_r4\sections\unify_bullets\unify_bullets_output.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `PASS` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 3/5 vs 4 FAIL; Anthropic Claude `claude-sonnet-5`: 0.76/5 vs 0.72 PASS; Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS` |

## Required Fix

- Make `unify_bullets` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`X3_BLOCK`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
