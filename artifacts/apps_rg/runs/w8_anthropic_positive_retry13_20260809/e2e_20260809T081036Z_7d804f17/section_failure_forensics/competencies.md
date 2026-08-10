# Section Failure Forensics - competencies

- failure_type: `independent_failure`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry13_20260809\e2e_20260809T081036Z_7d804f17\apps_research\runs\r-77043c7cf071fbc84d927acc\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass Pre-run dependency blocked execution: EXECUTED_X3_REVIEW_JUDGE_SOFT_FAIL; dispatch_error:lane_exit_error.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `82ec2939996d7afd4bb29e181fc122cd302c3508f84a4627a2ccea43d14d7c6f` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry13_20260809\e2e_20260809T081036Z_7d804f17\modular_r4\sections\competencies\competencies_display.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `PASS` / `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 3.8/5 vs 4 FAIL` |

## Required Fix

- Make `competencies` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
