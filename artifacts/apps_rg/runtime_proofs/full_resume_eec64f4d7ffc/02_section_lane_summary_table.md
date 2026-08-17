# apps_rg Mandatory Run Output

Generated: `2026-08-17T03:43:29Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_eec64f4d7ffc`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `True` |
| X3 disposition | `X3D_ALLOW_FINISH` |
| Fault | `-` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `PASS` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `PASS` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 6610, 'sha256': '3fcc7ec0bec082f0cb2b4818cbb0b2abc8522a7634c76e561cf5f6c98cad27f2'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_final_resume_json_present` | `PASS` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 944619, 'sha256': '0e56bec07958369b3368fdbe495cea639fbe112ae8d0bb40a264c4d57d0bbdb3'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_resume_docx_present` | `PASS` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4802, 'sha256': '13eb65a5bcf8d4e482b651fafb23ada84fa86866ab56a1e8f31819171e588dc4'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['PX'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `PASS` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 6489, 'current_run_authorized': True, 'blockers': []}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 1, 'artifact_dir': 'artifacts/apps_rg/runtime_proofs/full_resume_eec64f4d7ffc/section_failure_forensics', 'missing_or_incomplete': []}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `PASS` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 11 | 12 | 0 | 0 | 0 | 0 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=e4a57082576a784e018a603ff5afd4243956cfe4df7f4fe2dda1832afa080e5f;<br>ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_eec64f4d7ffc\apps_research\runs\bridge_rg_research_bridge_9118b393_3c65e8b9-6b7f-4940-862b-031d5e7fb9b3\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7889</code></span> | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_eec64f4d7ffc\apps_research\runs\bridge_rg_research_bridge_9118b393_3c65e8b9-6b7f-4940-862b-031d5e7fb9b3\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.8 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `lanes/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.8 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.75 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.8 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.78 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.77 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/unify_narrative/unify_narrative_output.txt` | `future_run_advisory_only` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_narrative/ibm_narrative_output.txt` | `future_run_advisory_only` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.6 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.4 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.4 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.8 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.1 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/unify_narrative/unify_narrative_output.txt` |
| `ibm_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ibm_narrative/ibm_narrative_output.txt` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ey_narrative/ey_narrative_output.txt` |
| `executive_summary` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/executive_summary/resume_display_text.txt` |
| `headline` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/headline/headline_output.txt` |
| `final_resume_aggregation` | `assembled` | `X3_ALLOW` | `PASS` | `PASS` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `PASS` | 944619 | `0e56bec07958369b3368fdbe495cea639fbe112ae8d0bb40a264c4d57d0bbdb3` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `PASS` | 6610 | `3fcc7ec0bec082f0cb2b4818cbb0b2abc8522a7634c76e561cf5f6c98cad27f2` |
| Final resume DOCX | `outputs/resume.docx` | `PASS` | 4802 | `13eb65a5bcf8d4e482b651fafb23ada84fa86866ab56a1e8f31819171e588dc4` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runtime_proofs/full_resume_eec64f4d7ffc/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 6610, 'sha256': '3fcc7ec0bec082f0cb2b4818cbb0b2abc8522a7634c76e561cf5f6c98cad27f2'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4802, 'sha256': '13eb65a5bcf8d4e482b651fafb23ada84fa86866ab56a1e8f31819171e588dc4'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 240, 'ENGINEERING & PLATFORM COMPETENCIES': 1235, 'PROFESSIONAL EXPERIENCE': 2013, 'EDUCATION': 6087, 'CERTIFICATIONS': 6251}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 238, 'ENGINEERING & PLATFORM COMPETENCIES': 1232, 'PROFESSIONAL EXPERIENCE': 2009, 'EDUCATION': 6077, 'CERTIFICATIONS': 6240}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2038, 2095], 'ibm': [3575, 3589], 'insurtech': [4619, 4672], 'ey': [5002, 5028], 'early_career': [5631, 5696]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2033, 2090], 'ibm': [3569, 3583], 'insurtech': [4612, 4665], 'ey': [4994, 5020], 'early_career': [5622, 5687]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6097, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6182}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6087, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6172}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6280, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6339, 'Certified Solutions Architect – Professional, AWS, 2023': 6393, 'Fellow of the Society of Actuaries, 2010': 6449}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6269, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6328, 'Certified Solutions Architect – Professional, AWS, 2023': 6382, 'Fellow of the Society of Actuaries, 2010': 6438}}` |
| `final_resume_no_gap_markers` | `PASS` | `{'not_completed': False, 'not_generated_by_run': False}` |

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.75 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ibm_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.8 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.78 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.77 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `unify_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ibm_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.6 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `executive_summary` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.4 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.4 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `-` |
| `final_resume_aggregation` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.1 | 4 | `PASS` | `-` |

## RCA Findings

- No blocking RCA findings recorded.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `PASS`
- Required: `True`
- Failed section count: `1`
- Artifact directory: `artifacts/apps_rg/runtime_proofs/full_resume_eec64f4d7ffc/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `whole_run` | `mandatory_output_authorization_block` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_eec64f4d7ffc/section_failure_forensics/whole_run.json` | `artifacts/apps_rg/runtime_proofs/full_resume_eec64f4d7ffc/section_failure_forensics/whole_run.md` |

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

Source: `FINAL_RESUME_OUTPUT.txt rendered from the current E2E run final-resume spine used for outputs/resume.docx.`

```text
Amit Ayer
+1-917-239-3830 | amitayer1@gmail.com | linkedin.com/in/amitayer1 | github.com/Siamese001/Agentic-Workflow

HEADLINE
SVP Engineering | Hyperscaler Alliance Co-Sell | Runtime Governance Telemetry | Enterprise Portfolio Governance

EXECUTIVE SUMMARY
Engineering executive builds governed agentic AI platform systems for regulated enterprise delivery. The platform's control plane keeps autonomous execution bounded through policy-gated dispatch through operating discipline. Software dependency graph intelligence enables accelerated legacy-system analysis, exposes architecture dependency chains, and improves transformation visibility across enterprise complexity. In parallel, embedded release automation and security scanning across regulated modernization delivery paths raised deployment repeatability and scanning coverage without slowing throughput. That operating foundation also underpins platform commercialization leadership, converting governed capability into $22M in IP-led revenue while expanding margins and scaling the platform team. The same platform discipline positions the leader to extend governed architecture and productized platform economics into repeatable, revenue-generating enterprise outcomes.

ENGINEERING & PLATFORM COMPETENCIES
Partner AI Architecture & Commercialization: Buyer-specific solution mapping for enterprise pursuits, Partner AI solution architecture and co-sell execution, Enterprise pursuit execution across portfolio expansion motions, Partner value-realization operating cadence and deal support, AI co-sell bundling with strategic partners
Governed AI Platforms & Reliability: Agentic platform route-policy dispatch architecture, Regulated DevSecOps release governance pipelines, governed multi-agent orchestration control planes
Enterprise Architecture & Delivery: Presales-to-delivery customer success operating handoff cadence, relationship-grounded context retrieval for enterprise workflows, dense-sparse retrieval with relationship-aware ranking

PROFESSIONAL EXPERIENCE

Unify Consulting — SVP Engineering, Agentic AI Platforms
Boca Raton, FL | Feb 2023 – Present
Owned Unify Consulting’s transformation of agentic AI from bespoke enterprise engagements into an industrialized, governed commercial capability, aligning platform architecture, reusable IP, operating discipline and alliance distribution to make regulated-enterprise deployment repeatable and valuable.
• Architected a policy-gated agent execution surface for governed enterprise AI workflows, establishing L0 route-policy dispatch, runtime gate verdict contracts, and proof-bundle lineage across production agentic deployments.
• Drove CFO-aligned enterprise adoption motions tied to reusable AI platform commercialization, pairing usage-based forecasting with partner-led deal support to expand recurring revenue.
• Delivered audit-grade runtime observability coverage for regulated AI workflows by instituting evaluation gates, telemetry, and rollback controls across the production agentic runtime.
• Standardized the AI systems lifecycle from intake through production monitoring, compressing deployment cycle time from six months to three weeks through replayable runtime design.
• Architected distributed cloud data runtime integration patterns across Databricks, vector services, and API gateways to support high-availability agentic workloads.
• Converted bespoke delivery into reusable platform IP through agentic platform productization, scaling the engineering team from 8 to 28 while advancing the operating model for agentic AI.

IBM — Partner
Edgewater, NJ | Apr 2017 – Oct 2022
Operationalized alliance-led AWS solution architecture at IBM, establishing BI-informed executive decision support and repeatable enterprise pursuit discipline across complex financial-services modernization portfolios, from initial qualification through executive stakeholder alignment and delivery readiness for clients.
• Led IBM-AWS alliance co-sell motions for financial-services modernization opportunities, delivering 20% joint revenue growth.
• Built decision-support data models and BI views that connected modernization programs to executive operating decisions.
• Led technical discovery and solution architecture mapping for enterprise financial-services pursuits.
• Prioritized enterprise pursuits using solution-architecture feasibility reviews, account context, and buyer readiness, connecting technical validation to executive deal support.
• Architected industry-specific AI, analytics, and cloud modernization reference architectures for financial-services decision support.

InsurTech Cloud Solutions — Chief Technology Officer
New York, NY | Apr 2014 – Mar 2017
Led AWS modernization execution for monolithic policy administration and insurance platform workloads.
• Implemented SOC 2-aligned AWS controls for regulated insurers adopting analytics and ML.
• Built safety operating-model framing around AWS shared responsibility and insurer-owned controls.

Ernst & Young — Principal
New York, NY | Oct 2009 – Mar 2014
Led quantitative derivatives, variable-annuity hedging, and insurance-capital work using exotic pricing, liability Greeks, higher-order stress testing, and hedge design.
• Led CCAR-era capital, liquidity, stress testing, and model-validation work by structuring traceable scenarios, challenger variants, model-risk remediation, and governance evidence for regulated financial institutions.
• Architected ERM operating models and BCBS 239-aligned risk-data aggregation by defining three-lines-of-defense accountability, metadata standards, and auditable risk metrics.

Early Career Roles — Actuarial Consultant and Quantitative Roles
Philadelphia, PA | Oct 2002 – Sep 2009
• Actuarial & Quantitative Foundation: Priced exotic derivatives and structured multi-Greek hedging strategies, built stochastic capital models, and supported HPC-based valuation frameworks for scenario testing and capital adequacy — quantitative rigor and risk discipline that now underpin my work in AI platform architecture and runtime governance.

EDUCATION
Master of Science in Biostatistics, Columbia University (Graduated with Distinction)
Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)

CERTIFICATIONS & CREDENTIALS
Certified Machine Learning Engineer – Associate, AWS, 2025
Databricks Lakehouse Fundamentals Accreditation, 2023
Certified Solutions Architect – Professional, AWS, 2023
Fellow of the Society of Actuaries, 2010
```
