# apps_rg Mandatory Run Output

Generated: `2026-08-09T08:33:38Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:headline:EXECUTED_X3_BLOCK' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7274, 'sha256': '632560a24ec32698893d5e7a914e99f886fb98734e50c2b3d78236eb4f3fd505'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=headline,final_resume_aggregation']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 21791383, 'sha256': '048d307ed5512288fa6a59ec664a8fb1daac702717c89f5e2f994642aa3b483f'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=headline,final_resume_aggregation']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5007, 'sha256': '7dc6258122e91ca92332d8a555ce3f0bea876176a2aa4070223c947003b6a3f2'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=headline,final_resume_aggregation']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `FAIL` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': ['bcg.forensics.incomplete_artifact:final_resume_aggregation', 'bcg.forensics.incomplete_artifact:headline', 'bcg.issue_tree.incomplete_forensic_artifact:headline']}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 491, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=headline,final_resume_aggregation']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `FAIL` | `{'required': True, 'failed_section_count': 2, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics', 'missing_or_incomplete': [{'section_id': 'headline', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'final_resume_aggregation', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'aggregation_downstream', 'baseline_confidence': 'pinned_baseline_unavailable'}]}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `FAIL` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 11 | 10 | 1 | 0 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=6a36e10597884f17e66a1f83476a92224656f158f32fbc6e7e1507b2a1c5d32c;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\apps_research\runs\r-41c059ab17564d1cc7ddb527\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7506</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\apps_research\runs\r-41c059ab17564d1cc7ddb527\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.3 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.78 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 4.5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.73 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/unify_narrative/unify_narrative_output.txt` | `future_run_advisory_only` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ibm_narrative/ibm_narrative_output.txt` | `future_run_advisory_only` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.2 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 2.5 vs 4 FAIL; OpenAI ChatGPT / gpt-5.6-sol: 3 vs 4 FAIL` | `decisive_judge_failures=gemini_pro,openai_chatgpt` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>X1D decisive judge failure: model-backed judge rejected section product quality.</code></span> | `modular_r4/sections/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/unify_narrative/unify_narrative_output.txt` |
| `ibm_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ibm_narrative/ibm_narrative_output.txt` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` |
| `executive_summary` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/executive_summary/resume_display_text.txt` |
| `headline` | `ran_real_llm` | `X3_BLOCK` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/headline/headline_output.txt` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 21791383 | `048d307ed5512288fa6a59ec664a8fb1daac702717c89f5e2f994642aa3b483f` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 7274 | `632560a24ec32698893d5e7a914e99f886fb98734e50c2b3d78236eb4f3fd505` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 5007 | `7dc6258122e91ca92332d8a555ce3f0bea876176a2aa4070223c947003b6a3f2` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7274, 'sha256': '632560a24ec32698893d5e7a914e99f886fb98734e50c2b3d78236eb4f3fd505'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5007, 'sha256': '7dc6258122e91ca92332d8a555ce3f0bea876176a2aa4070223c947003b6a3f2'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 234, 'ENGINEERING & PLATFORM COMPETENCIES': 1146, 'PROFESSIONAL EXPERIENCE': 2757, 'EDUCATION': 6701, 'CERTIFICATIONS': 6865}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 232, 'ENGINEERING & PLATFORM COMPETENCIES': 1143, 'PROFESSIONAL EXPERIENCE': 2753, 'EDUCATION': 6691, 'CERTIFICATIONS': 6854}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2782, 2839], 'ibm': [4242, 4256], 'insurtech': [5177, 5230], 'ey': [5565, 5591], 'early_career': [6194, 6259]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2777, 2834], 'ibm': [4236, 4250], 'insurtech': [5170, 5223], 'ey': [5557, 5583], 'early_career': [6185, 6250]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6711, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6796}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6701, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6786}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6894, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6953, 'Certified Solutions Architect – Professional, AWS, 2023': 7007, 'Fellow of the Society of Actuaries, 2010': 7063}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6883, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6942, 'Certified Solutions Architect – Professional, AWS, 2023': 6996, 'Fellow of the Society of Actuaries, 2010': 7052}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': False, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.3 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.78 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=openai_chatgpt,gemini_pro` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.5 | 4 | `PASS` | `model_backed_pass_provider_keys=openai_chatgpt,gemini_pro` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.73 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ibm_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `executive_summary` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.2 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_FAIL` | 2.5 | 4 | `FAIL` | `decisive_judge_failures=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_FAIL` | 3 | 4 | `FAIL` | `decisive_judge_failures=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `headline` - X1D decisive judge failure: model-backed judge rejected section product quality.
   - Root cause: The lane published judge-visible narrative text after normalizing the provider payload through a lossy claim-ledger path that dropped source_fact_ids needed to support material claims.
   - Evidence: `Google Gemini 3.6 Flash \| gemini-3.6-flash \| MODEL_BACKED_FAIL \| score=2.5/4 \|\| OpenAI ChatGPT \| gpt-5.6-sol \| MODEL_BACKED_FAIL \| score=3/4`
   - Causal allocation:
     - Dominant cause: The section was generated, parsed, and X2-clean, but the published claim ledger lost source-fact bindings that X1D required for judge-visible material claims.
     - Retry recoverability: `LOW_UNTIL_LEDGER_FIX` - Blind regeneration can return a valid parsed claim ledger again, but the same lossy normalization path will keep dropping support before X1D.
     - Allocation rows:
       - `Claim ledger normalization` / `PRIMARY` / `45%`: Google Gemini 3.6 Flash | gemini-3.6-flash | MODEL_BACKED_FAIL | score=2.5/4 || OpenAI ChatGPT | gpt-5.6-sol | MODEL_BACKED_FAIL | score=3/4 Evidence: `parsed_output.json, claim_ledger.json, x1d_llm_judge_outputs.json`. Required work: Preserve valid source_fact_ids from parsed narrative claim_ledger rows when publishing the single-sentence role-episode ledger.
       - `Narrative source binding` / `CONTRIBUTING` / `25%`: Narrative material phrases such as insurance operations, model risk, and traceable controls must bind to selected role-episode facts before judge review. Evidence: `selected_fact_plan.json, role_episode_lane.py`. Required work: Add deterministic phrase-to-fact reconciliation for EY narrative material claims within the allowed graph packet.
       - `X1D authorization policy` / `DETECTION` / `20%`: X2 PASS and product PASS were not enough because the model-backed judge rejected factual support. Evidence: `x3_disposition.json, x1d_llm_judge_outputs.json`. Required work: Keep X3 blocked on decisive factual-support judge failures and surface the judge finding as the primary RCA.
       - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: The fix belongs at the parser/ledger boundary, not in downstream rerun scheduling or final assembly. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Rerun only after the narrative ledger preservation fixture and mandatory-RCA fixture pass.
   - Required implementation plan:
     - Preserve valid source_fact_ids from parsed narrative claim_ledger rows when normalizing role-episode narrative output.
     - Add source-binding patterns for material EY insurance, ERM, CCAR, regulatory analytics, and capital/solvency claims.
     - Keep X2 PASS insufficient for authorization when X1D factual-support judges reject the published claim ledger.
     - Add a regression fixture using the live EY narrative where insurance operations must cite reb_ey_insurance_core_modernization.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `FAIL`
- Required: `True`
- Failed section count: `2`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics`
- Baseline confidence: `pinned_baseline_unavailable`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `headline` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 17 | `future_run_advisory_only` |
| `unify_bullets` | 15 | `future_run_advisory_only` |
| `ibm_bullets` | 15 | `future_run_advisory_only` |
| `insurtech_bullets` | 1 | `future_run_advisory_only` |
| `ey_bullets` | 1 | `future_run_advisory_only` |
| `unify_narrative` | 16 | `future_run_advisory_only` |
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
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=headline,final_resume_aggregation
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
