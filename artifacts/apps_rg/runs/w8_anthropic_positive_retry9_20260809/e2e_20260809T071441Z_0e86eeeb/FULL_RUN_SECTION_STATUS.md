# Full resume — per-section status

Run folder: `e2e_20260809T071441Z_0e86eeeb`

| Section | X3 | X2 | Product quality | Runtime | Judges / score | Display text |
|---|---|---|---|---|---|---|
| competencies | X3_ALLOW | PASS | PASS | REAL_LLM | Google Gemini 3.6 Flash `gemini-3.6-flash`: 4.8/5 vs 4 PASS; OpenAI ChatGPT `gpt-5.6-sol`: 4.2/5 vs 4 PASS | [modular_r4/sections/competencies/competencies_display.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/competencies/competencies_display.txt) |
| unify_bullets | X3_ALLOW | PASS | PASS | REAL_LLM | Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS; Anthropic Claude `claude-sonnet-5`: 0.77/5 vs 0.72 PASS; Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS | [modular_r4/sections/unify_bullets/unify_bullets_output.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/unify_bullets/unify_bullets_output.txt) |
| ibm_bullets | X3_ALLOW | PASS | PASS | REAL_LLM | Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS; Anthropic Claude `claude-sonnet-5`: 0.78/5 vs 0.72 PASS; Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS | [modular_r4/sections/ibm_bullets/ibm_bullets_output.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/ibm_bullets/ibm_bullets_output.txt) |
| insurtech_bullets | X3_BLOCK | FAIL | FAIL | BLOCKED | gemini_pro: —/5 vs — FAIL | — (missing) |
| ↳ failed gates | | | | | | `x2_insurtech_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_display_text_proof_authorized, x2_insurtech_bullets_runtime_real_llm, x2_insurtech_bullets_bullet_count_3, x2_resume_graph_claim_binding` |
| ey_bullets | X3_BLOCK | FAIL | FAIL | BLOCKED | gemini_pro: —/5 vs — FAIL | — (missing) |
| ↳ failed gates | | | | | | `x2_ey_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_ey_bullets_display_text_proof_authorized, x2_ey_bullets_runtime_real_llm, x2_ey_bullets_bullet_count_3, x2_resume_graph_claim_binding` |
| unify_narrative | X3_ALLOW | PASS | PASS | REAL_LLM | Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS | [modular_r4/sections/unify_narrative/unify_narrative_output.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/unify_narrative/unify_narrative_output.txt) |
| ibm_narrative | X3_ALLOW | PASS | PASS | REAL_LLM | Google Gemini 3.6 Flash `gemini-3.6-flash`: 5/5 vs 4 PASS | [modular_r4/sections/ibm_narrative/ibm_narrative_output.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/ibm_narrative/ibm_narrative_output.txt) |
| insurtech_narrative | PRE_RUN:upstream_not_finalized | UNKNOWN | UNKNOWN | UNKNOWN | — | — (missing) |
| ↳ pre-run | | | | | | `PRE_RUN:upstream_not_finalized` |
| ey_narrative | PRE_RUN:upstream_not_finalized | UNKNOWN | UNKNOWN | UNKNOWN | — | — (missing) |
| ↳ pre-run | | | | | | `PRE_RUN:upstream_not_finalized` |
| executive_summary | X3_BLOCK | FAIL | FAIL | BLOCKED | — | [modular_r4/sections/executive_summary/resume_display_text.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/executive_summary/resume_display_text.txt) |
| ↳ failed gates | | | | | | `x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality` |
| headline | X3_BLOCK | FAIL | FAIL | BLOCKED | Google Gemini 3.6 Flash `gemini-3.6-flash`: 0/5 vs 4 FAIL; OpenAI ChatGPT `gpt-5.6-sol`: 0/5 vs 4 FAIL | [modular_r4/sections/headline/headline_output.txt](artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/modular_r4/sections/headline/headline_output.txt) |
| ↳ failed gates | | | | | | `x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger` |
| final_resume_aggregation | NOT_RUN | — | — | — | — | — (missing) |
