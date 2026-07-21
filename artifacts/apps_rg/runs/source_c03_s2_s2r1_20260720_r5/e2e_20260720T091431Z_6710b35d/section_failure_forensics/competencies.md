# Section Failure Forensics - competencies

- failure_type: `independent_failure`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `x2_competencies_required_proof_present, x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_required_proof_present, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_competencies_required_proof_present, x2_resume_graph_claim_binding.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `1375bf16a4d7774481aceb5594b7b7b924362e01` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `63ac49efa30b2f895a2b5acec0a72ff04f8237fd61ed7fd855e01a8ad67fe1d9` / `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runtime_proofs\full_resume_81ee1b5017db\command_output.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Make `competencies` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_competencies_required_proof_present, x2_resume_graph_claim_binding`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
