# apps_rg Mandatory Run Output

Generated: `2026-08-09T08:09:30Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:unify_bullets:EXECUTED_X3_ALLOW; unify_narrative:upstream_not_finalized; ibm_narrative:EXECUTED_X3_BLOCK; executive_summary:EXECUTED_X3_BLOCK' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7274, 'sha256': '72775b19a9e2fc35248ee7e19b71294953a455085b51315ba67c7c58e8806431'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,ibm_narrative,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 21784869, 'sha256': '122461e957b901e3730fdc2a2c87634c2eae542b32a876199a9f2c021a2ea578'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,ibm_narrative,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4982, 'sha256': 'cca43dc081b6dc6f8775d0f6ca0573fd52dde379550fd33f5ea77d32b4161950'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,ibm_narrative,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `FAIL` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': ['bcg.forensics.incomplete_artifact:executive_summary', 'bcg.forensics.incomplete_artifact:final_resume_aggregation', 'bcg.forensics.incomplete_artifact:ibm_narrative', 'bcg.forensics.incomplete_artifact:unify_bullets', 'bcg.forensics.incomplete_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:unify_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_narrative']}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 561, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,ibm_narrative,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `FAIL` | `{'required': True, 'failed_section_count': 5, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics', 'missing_or_incomplete': [{'section_id': 'unify_bullets', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_bullets.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'unify_narrative', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ibm_narrative', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/ibm_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/ibm_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'executive_summary', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/executive_summary.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/executive_summary.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'final_resume_aggregation', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/final_resume_aggregation.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/final_resume_aggregation.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'aggregation_downstream', 'baseline_confidence': 'pinned_baseline_unavailable'}]}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `FAIL` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 10 | 7 | 3 | 1 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=25719b1801b93eb601559c9c1c6df97d569336e1887de4f37498453f5c6a417e;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7942</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.2 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.77 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.78 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Output contract failure: parsed content or claim ledger did not satisfy section schema.</code></span> | `modular_r4/sections/ibm_narrative/ibm_narrative_output.txt` | `future_run_advisory_only` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.2 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.6 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.2 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` | `FAIL` | `PASS` | `REAL_LLM` | `x2_resume_graph_claim_binding` | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ibm_narrative` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets` | `modular_r4/sections/ibm_narrative/ibm_narrative_output.txt` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` |
| `executive_summary` | `ran_real_llm` | `X3_BLOCK` | `PASS` | `FAIL` | `REAL_LLM` | `-` | `modular_r4/sections/executive_summary/resume_display_text.txt` |
| `headline` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/headline/headline_output.txt` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 21784869 | `122461e957b901e3730fdc2a2c87634c2eae542b32a876199a9f2c021a2ea578` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 7274 | `72775b19a9e2fc35248ee7e19b71294953a455085b51315ba67c7c58e8806431` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 4982 | `cca43dc081b6dc6f8775d0f6ca0573fd52dde379550fd33f5ea77d32b4161950` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7274, 'sha256': '72775b19a9e2fc35248ee7e19b71294953a455085b51315ba67c7c58e8806431'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4982, 'sha256': 'cca43dc081b6dc6f8775d0f6ca0573fd52dde379550fd33f5ea77d32b4161950'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 240, 'ENGINEERING & PLATFORM COMPETENCIES': 1285, 'PROFESSIONAL EXPERIENCE': 3004, 'EDUCATION': 6702, 'CERTIFICATIONS': 6866}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 238, 'ENGINEERING & PLATFORM COMPETENCIES': 1282, 'PROFESSIONAL EXPERIENCE': 3000, 'EDUCATION': 6692, 'CERTIFICATIONS': 6855}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [3029, 3086], 'ibm': [4194, 4208], 'insurtech': [5178, 5231], 'ey': [5566, 5592], 'early_career': [6195, 6260]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [3024, 3081], 'ibm': [4188, 4202], 'insurtech': [5171, 5224], 'ey': [5558, 5584], 'early_career': [6186, 6251]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6712, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6797}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6702, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6787}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6895, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6954, 'Certified Solutions Architect – Professional, AWS, 2023': 7008, 'Fellow of the Society of Actuaries, 2010': 7064}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6884, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6943, 'Certified Solutions Architect – Professional, AWS, 2023': 6997, 'Fellow of the Society of Actuaries, 2010': 7053}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': False, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.2 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.77 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.78 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ibm_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.2 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `executive_summary` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.6 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.2 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `unify_bullets` - Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
   - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
   - Evidence: `x2_resume_graph_claim_binding`
   - Causal allocation:
     - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
     - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
     - Allocation rows:
       - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
       - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
       - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_resume_graph_claim_binding`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
       - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
   - Required implementation plan:
     - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
     - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
     - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
     - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
2. `unify_narrative` - Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:upstream_not_finalized`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
3. `ibm_narrative` - Output contract failure: parsed content or claim ledger did not satisfy section schema.
   - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
   - Evidence: `x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets`
   - Causal allocation:
     - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
     - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
     - Allocation rows:
       - `Parser / normalization contract` / `PRIMARY` / `40%`: The bullet-count gate observed an empty parsed bullet artifact. Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
       - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_ibm_narrative_claim_theme_coverage: narrative_sentence material themes require matching bul_ibm_* in claim_ledger union; missing: ['unsupported_companion_theme:ecosystem', 'unsupported_companion_theme:ecosystems', 'unsupported_companion_theme:regulated_financial'] observed={'themes_detected': ['bul_ibm_001', 'unsupported_companion_theme:ecosystem', 'unsupported_companion_theme:ecosystems', 'unsupported_companion_theme:regulated_financial'], 'missing_in_ledger_union': ['unsupported_companion_theme:ecosystem', 'unsupported_companion_theme:ecosystems', 'unsupported_companion_theme:regulated_financial']} Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
       - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets`. Required work: Attach parser input/output references and failed field names to the gate evidence.
       - `Retry / repair policy` / `LOW_RECOVERY` / `15%`: Retries target the model, while the observed failure is an empty parsed artifact after generation. Evidence: `self_consistency_paths.json, parsed_output.json`. Required work: Allow retry only after parser and claim-ledger contracts prove they can preserve a valid generated payload.
   - Required implementation plan:
     - Trace the lane's canonical output schema from provider prompt to parser to X2 gate input and remove alternate empty or partial shapes.
     - Move required-field and bullet-count validation ahead of X2 so malformed provider responses fail before claim evaluation.
     - Emit claim-ledger rows with source_fact_id and claim_text at generation/parsing time instead of attempting post-hoc repair.
     - Add a fixture that proves malformed provider output is rejected and a compliant provider payload produces the expected ledger rows.
     - Add a CI assertion that the lane cannot emit display content unless the schema and claim-ledger contract is satisfied.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `FAIL`
- Required: `True`
- Failed section count: `5`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics`
- Baseline confidence: `pinned_baseline_unavailable`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `unify_bullets` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/unify_narrative.md` |
| `ibm_narrative` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/ibm_narrative.md` |
| `executive_summary` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/executive_summary.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry12_20260809/e2e_20260809T075910Z_f008baa6/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 17 | `future_run_advisory_only` |
| `unify_bullets` | 15 | `future_run_advisory_only` |
| `ibm_bullets` | 15 | `future_run_advisory_only` |
| `insurtech_bullets` | 1 | `future_run_advisory_only` |
| `ey_bullets` | 1 | `future_run_advisory_only` |
| `unify_narrative` | 0 | `not_observed` |
| `ibm_narrative` | 15 | `future_run_advisory_only` |
| `insurtech_narrative` | 1 | `future_run_advisory_only` |
| `ey_narrative` | 1 | `future_run_advisory_only` |
| `executive_summary` | 18 | `future_run_advisory_only` |
| `headline` | 15 | `future_run_advisory_only` |
| `final_resume_aggregation` | 0 | `not_observed` |

## Resume DOCX Full Version Inline

Source: `No authorized resume text emitted; this block is derived only from the current E2E run ledger and final-resume output contract.`

```text
NO_AUTHORIZED_RESUME_OUTPUT
source_of_truth=current_e2e_run_artifacts_only
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=unify_bullets,ibm_narrative,executive_summary,final_resume_aggregation; pre_run_blocked=unify_narrative
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
