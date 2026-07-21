# Section Failure Forensics - competencies

- failure_type: `independent_failure`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\apps_research\runs\r-80e758cb11db9efc0bed092e\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `bb7a8e4620eacfa4d64ad44f71b46dcbbdf99b53` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `aa9814b73e4c902419af3154bc9dca47bb2935b26a9f5f25d6deb9ffcf2bbba2` / `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runtime_proofs\full_resume_c005cc5512d7\competencies_display.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.1 Pro Preview `gemini-3.1-pro-preview`: 5/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.5`: 4.35/5 vs 4 PASS` |

## Required Fix

- Make `competencies` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
