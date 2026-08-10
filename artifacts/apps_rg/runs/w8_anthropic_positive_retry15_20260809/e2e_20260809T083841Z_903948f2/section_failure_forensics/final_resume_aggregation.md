# Section Failure Forensics - final_resume_aggregation

- failure_type: `aggregation_downstream`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `x2_full_resume_llm_coherence_aggregation`

## Layperson Explanation

The prior passing revision authorized final assembly because every required section, including the executive summary, had already cleared its product checks.
The current final assembly did not fail as an independent writing attempt; it was blocked downstream because the executive summary never became eligible for assembly.
No aggregation retry or aggregation judge could repair that upstream section failure, so the underlying executive-summary retry and X2 evidence remains the controlling root cause.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `upstream_section_authorization` - Final assembly was blocked because the executive summary never reached product authorization.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

Final aggregation was downstream of section certification and product-output gates; it failed on x2_full_resume_llm_coherence_aggregation.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `1a4c19585c8f1f66bb0deaa40cde884e58d4a9b38cb6e6e23e0584af6845e364` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry15_20260809\e2e_20260809T083841Z_903948f2\modular_r4\final_resume_assembly\final_resume.json` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_REVIEW_AGGREGATION` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 4.5/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 3.8/5 vs 4 FAIL` |

## Required Fix

- Require final aggregation to consume only sections with accepted X3 evidence.
- Record the exact upstream section or product-output gate that blocked assembly.
- Rerun aggregation only after the failed section RCA artifacts are complete.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
