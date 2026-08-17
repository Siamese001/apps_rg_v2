# Section Failure Forensics - executive_summary

- failure_type: `independent_failure`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_exec_summary_allowed_fact_utilization`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bd7b4d8fe14b\apps_research\runs\bridge_rg_research_bridge_e0ccb045_34acaf68-3298-4718-8667-3294862b72a2\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 3 pre-judge repair attempt(s), but repeated formulaic transition phrases; and combined too many source facts in one sentence; and resume_graph_claim_binding:claim_6:causal_claim_merges_unrelated_graph_roots; and resume_graph_claim_binding:orphan_allocation_claim_units:executive_summary:claim:01; and DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis'; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_allowed_fact_utilization), so JUDGES_NOT_REACHED and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `retry_loop` - The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_exec_summary_allowed_fact_utilization.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `NOT_OBSERVED` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `cdf59adecf73b019ba0304707601053cff360b835ea75c98ec2a80b7e0e02451` / `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bd7b4d8fe14b\lanes\executive_summary\resume_display_text.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Make `executive_summary` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_exec_summary_allowed_fact_utilization`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
