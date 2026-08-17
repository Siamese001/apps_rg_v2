# Section Failure Forensics - final_resume_aggregation

- failure_type: `aggregation_downstream`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_full_resume_llm_coherence_aggregation`

## Layperson Explanation

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.
The aggregate panel ran and recorded gemini_pro 4.9/4.0 MODEL_BACKED_PASS; openai_chatgpt 3.8/4.0 MODEL_BACKED_FAIL; the required two-of-two model-backed quorum was not met.
The controlling product defect is aggregate coherence, not upstream section eligibility: Competencies are over-dense and repeat route-policy, governance, co-sell, and solution-mapping themes.; Several competency items are near-synonyms rather than distinct executive capabilities.; Summary S2-S4 is jargon-heavy and delays commercial and organizational impact until S5.; Partnership leadership is fragmented across the headline, competencies, IBM history, and current-role narrative.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `aggregate_coherence_quorum` - Final assembly completed, but the whole-resume model-backed judge quorum failed: Competencies are over-dense and repeat route-policy, governance, co-sell, and solution-mapping themes.; Several competency items are near-synonyms rather than distinct executive capabilities.; Summary S2-S4 is jargon-heavy and delays commercial and organizational impact until S5.; Partnership leadership is fragmented across the headline, competencies, IBM history, and current-role narrative.
- Code cause status: `AGGREGATE_GATE_ISOLATED`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

Final aggregation was downstream of section certification and product-output gates; it failed on x2_full_resume_llm_coherence_aggregation.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `NOT_OBSERVED` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `de1985f0ec50343cc42fc05baa6cf0c48c1c01ee20a0537f0598a40c438de803` / `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\final_resume.json` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_REVIEW_AGGREGATION` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 4.9/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 3.8/5 vs 4 FAIL` |

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
