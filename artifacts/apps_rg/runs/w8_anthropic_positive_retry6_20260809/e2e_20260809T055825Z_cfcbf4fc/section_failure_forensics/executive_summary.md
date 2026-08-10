# Section Failure Forensics - executive_summary

- failure_type: `independent_failure`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 2 pre-judge repair attempt(s), but DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis'; it reverted to its first candidate, the final deterministic check still failed (x2_resume_graph_claim_binding), so 4.8/4.0 MODEL_BACKED_PASS and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `retry_loop` - The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_resume_graph_claim_binding.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `8c2ce8925970bb9811ffc54e81560bf324e5f6a048d191d46e63480a7f72ec11` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\resume_display_text.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 4.8/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 4.5/5 vs 4 PASS` |

## Required Fix

- Make `executive_summary` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_resume_graph_claim_binding`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
