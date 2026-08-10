# Section Failure Forensics - final_resume_aggregation

- failure_type: `aggregation_downstream`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `-`

## Layperson Explanation

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.
The aggregate panel ran and recorded - EVIDENCE_NOT_RECORDED; the required two-of-two model-backed quorum was not met.
The controlling product defect is aggregate coherence, not upstream section eligibility: the failed aggregate gate is recorded in the final-resume review artifact.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `aggregate_coherence_quorum` - Final assembly completed, but the whole-resume model-backed judge quorum failed.
- Code cause status: `AGGREGATE_GATE_ISOLATED`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

Final aggregation was downstream of section certification and product-output gates; it failed on Final resume aggregation failure: full-resume coherence or product release gate did not pass..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `7312be75955b21db7574d3d4574c30e0dda6e3e5616b49f53731ac632af017e0` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\final_resume.json` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `UNKNOWN` / `X3_REVIEW_AGGREGATION` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Preserve the accepted X3 section snapshots and repair the content findings named by the failed aggregate judge.
- Record every whole-resume judge score, finding, raw-response reference, and quorum calculation in the aggregation RCA.
- Keep product authorization blocked until the required model-backed whole-resume quorum passes.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
