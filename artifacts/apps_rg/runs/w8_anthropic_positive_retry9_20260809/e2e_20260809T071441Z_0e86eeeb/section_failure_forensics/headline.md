# Section Failure Forensics - headline

- failure_type: `upstream_cascade`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding), so 0.0/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

This section did not independently certify because an upstream dependency or pre-run blocker prevented normal section authorization: Output contract failure: parsed content or claim ledger did not satisfy section schema..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `e89a0b0ab6b509f3507358984fbe09277c7e7c1f012a90bc34895c85abca4da6` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\command_output.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `Google Gemini 3.6 Flash `gemini-3.6-flash`: 0/5 vs 4 FAIL; OpenAI ChatGPT `gpt-5.6-sol`: 0/5 vs 4 FAIL` |

## Required Fix

- Resolve the upstream blocker before dispatching `headline`.
- Write the upstream dependency status into the section pre-run receipt.
- Keep the section blocked until its own X1-X3 inputs are present.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
