# Section Failure Forensics - headline

- failure_type: `independent_failure`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\apps_research\runs\r-41c059ab17564d1cc7ddb527\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 2.5/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

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
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `a6cba3b23f662d9a7cc795b315396a6766556491c91f67cec0cd2a0a2799212e` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\modular_r4\sections\headline\headline_output.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `PASS` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 2.5/5 vs 4 FAIL; OpenAI ChatGPT `gpt-5.6-sol`: 3/5 vs 4 FAIL` |

## Required Fix

- Make `headline` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`X3_BLOCK`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
