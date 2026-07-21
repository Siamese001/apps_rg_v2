# Section Failure Forensics - final_resume_aggregation

- failure_type: `aggregation_downstream`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `-`

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

Final aggregation was downstream of section certification and product-output gates; it failed on Final resume aggregation failure: full-resume coherence or product release gate did not pass..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `bb7a8e4620eacfa4d64ad44f71b46dcbbdf99b53` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `591fc80d6f8f71db3104b4ae6923d892a2334e148205fefec0d12a069f7caca2` / `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2r3_r3\e2e_20260720T221146Z_7d629b48\modular_r4\final_resume_assembly\final_resume.json` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `UNKNOWN` / `X3_REVIEW_AGGREGATION` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

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
