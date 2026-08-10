# Section Failure Forensics - competencies

- failure_type: `independent_failure`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T210449Z_62899bbe\apps_research\runs\bridge_rg_research_bridge_53bbccf2_ca44835d-1ed2-42e5-acfb-34681c4163a1\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

The section's final materialized artifact did not pass x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `7491cb18c04e2e722171bf5b946af03cc7e505a2a4d3af835a3c3bf4982f4ebc` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T210449Z_62899bbe\modular_r4\sections\competencies\competencies_display.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 4.3/5 vs 4 PASS` |

## Required Fix

- Make `competencies` gate final displayed output, not intermediate provider output.
- Bind the failed gate evidence (`x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding`) to the producer/parser contract that emitted the artifact.
- Record retry and repair outputs in the lane ledger so repeated LLM variance is explainable.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
