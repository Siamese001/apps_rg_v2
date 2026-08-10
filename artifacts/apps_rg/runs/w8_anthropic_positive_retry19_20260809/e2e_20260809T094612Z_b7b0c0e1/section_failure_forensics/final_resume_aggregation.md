# Section Failure Forensics - final_resume_aggregation

- failure_type: `aggregation_downstream`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `x2_full_resume_llm_coherence_aggregation`

## Layperson Explanation

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.
The aggregate panel ran and recorded gemini_pro 4.8/4.0 MODEL_BACKED_PASS; openai_chatgpt 3.6/4.0 MODEL_BACKED_FAIL; the required two-of-two model-backed quorum was not met.
The controlling product defect is aggregate coherence, not upstream section eligibility: S1 uses present-tense IBM-AWS leadership although the IBM role ended in 2022.; S2 redundantly repeats S1's alliance-modernization point.; S5 is vague and repeats “through,” weakening executive polish.; S6 is prospective and generic rather than evidence-led.; Competencies are clustered but over-dense and repeat co-sell, GraphRAG, telemetry, quota, and discovery content.; FSA appears in Early Career and Certifications, violating strict section ownership.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `aggregate_coherence_quorum` - Final assembly completed, but the whole-resume model-backed judge quorum failed: S1 uses present-tense IBM-AWS leadership although the IBM role ended in 2022.; S2 redundantly repeats S1's alliance-modernization point.; S5 is vague and repeats “through,” weakening executive polish.; S6 is prospective and generic rather than evidence-led.; Competencies are clustered but over-dense and repeat co-sell, GraphRAG, telemetry, quota, and discovery content.; FSA appears in Early Career and Certifications, violating strict section ownership.
- Code cause status: `AGGREGATE_GATE_ISOLATED`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

Final aggregation was downstream of section certification and product-output gates; it failed on x2_full_resume_llm_coherence_aggregation.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `ad4ee9d1efba5292db3f568339bf525a18e7622c4557651c8973c3f7adcf4b5a` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry19_20260809\e2e_20260809T094612Z_b7b0c0e1\modular_r4\final_resume_assembly\final_resume.json` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_REVIEW_AGGREGATION` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 4.8/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 3.6/5 vs 4 FAIL` |

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
