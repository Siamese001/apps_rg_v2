# Section Failure Forensics - executive_summary

- failure_type: `independent_failure`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T210449Z_62899bbe\apps_research\runs\bridge_rg_research_bridge_53bbccf2_ca44835d-1ed2-42e5-acfb-34681c4163a1\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 1 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids), so JUDGES_NOT_REACHED and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `retry_loop` - The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `ee2c59c1df416a741b07bf4875958f226b72f52d2c86051aed19209f8618a08c` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T210449Z_62899bbe\modular_r4\sections\executive_summary\resume_display_text.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Make `executive_summary` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
