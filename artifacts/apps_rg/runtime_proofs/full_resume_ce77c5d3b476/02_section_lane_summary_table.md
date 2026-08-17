# apps_rg Mandatory Run Output

Generated: `2026-08-17T03:13:31Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ce77c5d3b476`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `True` |
| X3 disposition | `X3D_ALLOW_FINISH` |
| Fault | `PRODUCT_E2E_RECEIPT_AUTHORITY_FAILED` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `PASS` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `PASS` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7363, 'sha256': '35616dea5214dd7e7baf74e024e0b3796048c0bf556c5d95953f656ba6e2de6f'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_final_resume_json_present` | `PASS` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 943938, 'sha256': '6d7221ced92849cf53329289b10a92315377b15746e04d1ebd5929c2a2883962'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_resume_docx_present` | `PASS` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5081, 'sha256': '9eeba22e317584b52e5d152bf97104fa8b896c9150506f896768a7890949cb55'}, 'current_run_authorized': True, 'blockers': []}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['PX'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `PASS` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 7239, 'current_run_authorized': True, 'blockers': []}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 1, 'artifact_dir': 'artifacts/apps_rg/runtime_proofs/full_resume_ce77c5d3b476/section_failure_forensics', 'missing_or_incomplete': []}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `PASS` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 11 | 12 | 0 | 0 | 0 | 0 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=e2ce8cc450b0aa968c55ce73c2f826804f2ac76b2b370fbed056f200a4fd6592;<br>ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ce77c5d3b476\apps_research\runs\bridge_rg_research_bridge_cb645228_326c1dba-c962-4eed-a818-7b89cf877f6a\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7917</code></span> | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ce77c5d3b476\apps_research\runs\bridge_rg_research_bridge_cb645228_326c1dba-c962-4eed-a818-7b89cf877f6a\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.6 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `lanes/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.75 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 4.8 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Anthropic Claude / claude-sonnet-5: 0.79 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.8 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.83 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/unify_narrative/unify_narrative_output.txt` | `future_run_advisory_only` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_narrative/ibm_narrative_output.txt` | `future_run_advisory_only` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.2 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.9 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.1 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

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
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `PASS` | 943938 | `6d7221ced92849cf53329289b10a92315377b15746e04d1ebd5929c2a2883962` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `PASS` | 7363 | `35616dea5214dd7e7baf74e024e0b3796048c0bf556c5d95953f656ba6e2de6f` |
| Final resume DOCX | `outputs/resume.docx` | `PASS` | 5081 | `9eeba22e317584b52e5d152bf97104fa8b896c9150506f896768a7890949cb55` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runtime_proofs/full_resume_ce77c5d3b476/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7363, 'sha256': '35616dea5214dd7e7baf74e024e0b3796048c0bf556c5d95953f656ba6e2de6f'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5081, 'sha256': '9eeba22e317584b52e5d152bf97104fa8b896c9150506f896768a7890949cb55'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 239, 'ENGINEERING & PLATFORM COMPETENCIES': 1225, 'PROFESSIONAL EXPERIENCE': 2802, 'EDUCATION': 6837, 'CERTIFICATIONS': 7001}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 237, 'ENGINEERING & PLATFORM COMPETENCIES': 1222, 'PROFESSIONAL EXPERIENCE': 2798, 'EDUCATION': 6827, 'CERTIFICATIONS': 6990}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2827, 2884], 'ibm': [4365, 4379], 'insurtech': [5369, 5422], 'ey': [5752, 5778], 'early_career': [6381, 6446]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2822, 2879], 'ibm': [4359, 4373], 'insurtech': [5362, 5415], 'ey': [5744, 5770], 'early_career': [6372, 6437]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6847, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6932}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6837, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6922}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 7030, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 7089, 'Certified Solutions Architect – Professional, AWS, 2023': 7143, 'Fellow of the Society of Actuaries, 2010': 7199}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 7019, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 7078, 'Certified Solutions Architect – Professional, AWS, 2023': 7132, 'Fellow of the Society of Actuaries, 2010': 7188}}` |
| `final_resume_no_gap_markers` | `PASS` | `{'not_completed': False, 'not_generated_by_run': False}` |

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.6 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.75 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.79 | 0.72 | `PASS` | `model_backed_pass_provider_keys=anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=anthropic_claude,gemini_pro` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.8 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.83 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `unify_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ibm_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `executive_summary` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.2 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.9 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `-` |
| `final_resume_aggregation` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.1 | 4 | `PASS` | `-` |

## RCA Findings

- No blocking RCA findings recorded.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `PASS`
- Required: `True`
- Failed section count: `1`
- Artifact directory: `artifacts/apps_rg/runtime_proofs/full_resume_ce77c5d3b476/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `whole_run` | `mandatory_output_authorization_block` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_ce77c5d3b476/section_failure_forensics/whole_run.json` | `artifacts/apps_rg/runtime_proofs/full_resume_ce77c5d3b476/section_failure_forensics/whole_run.md` |

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
SVP Engineering | Hyperscaler Alliance Co-Sell | Runtime Telemetry Governance | Enterprise Portfolio Expansion

EXECUTIVE SUMMARY
Engineering executive leading regulated modernization delivery through release automation and security scanning embedded in resilient release pipelines. Designs the control-plane architecture for a governed agentic AI platform that coordinates policy-gated routing across the runtime. Software dependency graph intelligence enables accelerated legacy-system analysis, exposes architecture dependency chains, and improves transformation visibility across enterprise complexity. From that commercial base, proof bundle lineage gives operators traceable, auditable visibility into every agent decision. In parallel, that platform's productization work generated $22M in IP-led revenue while scaling the supporting engineering team from eight to twenty-eight specialists. That combined foundation of governed architecture, release resilience, and commercialization leadership positions this leader to scale partner-facing AI architecture with the same disciplined rigor.

ENGINEERING & PLATFORM COMPETENCIES
Cloud & Partner Ecosystems: partner-ready applied AI reference architectures, Buyer-specific solution mapping for enterprise pursuits, Partner AI solution architecture and co-sell execution
AI Platform Leadership: governed multi-agent orchestration control planes, agentic workflow routing across enterprise systems, Agentic platform route-policy dispatch architecture
Governance, Risk & Compliance: fail-closed runtime control gate design, policy enforcement across agent execution paths, Regulated DevSecOps release governance pipelines
Technology Strategy & Innovation: relationship-grounded context retrieval for enterprise workflows, dense-sparse retrieval with relationship-aware ranking, authority-ordered prompt context assembly pipelines
Commercial & Operating Impact: Enterprise pursuit execution across portfolio expansion motions, Partner value-realization operating cadence and deal support, AI co-sell bundling with strategic partners
LLMOps & Reliability: audit-ready agent reliability evidence for governed systems, evaluation gauntlets for behavior assurance, production reliability lifecycle for agentic workflows
Data & Analytics Modernization: cloud-native AI data reference architectures, microservices integration for regulated ecosystems, lakehouse modernization for decision intelligence
Engineering & Delivery Leadership: executive-aligned technical discovery operating cadences, cross-functional enterprise solution architecture delivery governance, Presales-to-delivery customer success operating handoff cadence

PROFESSIONAL EXPERIENCE

Unify Consulting — SVP Engineering, Agentic AI Platforms
Boca Raton, FL | Feb 2023 – Present
Owned Unify Consulting's mandate to industrialize governed agentic AI, linking control-plane architecture, consistent operating discipline, and alliance distribution so regulated enterprise clients could adopt durable platform services rather than isolated consulting engagements at scale across complex workflows.
• Architected the control-plane for Unify's agentic AI platform, establishing a policy-gated agent execution surface for governed enterprise AI workflows spanning routing, orchestration, and audit-grade trace lineage.
• Drove CFO-aligned enterprise adoption motions tied to reusable AI platform commercialization, aligning generative-AI workflows to finance priorities and expanding consumption-based revenue.
• Established audit-grade runtime observability coverage for regulated AI workflows through evaluation gates, telemetry instrumentation, and rollback controls governing production agentic execution.
• Standardized the AI systems lifecycle from intake through production monitoring, compressing lab-to-production cycle time from six months to three weeks with deterministic auditability.
• Engineered distributed cloud data runtime integration patterns across Databricks, vector services, and API gateways to support high-availability agentic workloads.
• Converted bespoke delivery into reusable platform IP while scaling the engineering team from 8 to 28 to support enterprise-wide agentic platform commercialization.

IBM — Partner
Edgewater, NJ | Apr 2017 – Oct 2022
Championed partner-led solution architecture for complex enterprise client pursuits at IBM, establishing repeatable AWS and BI mechanisms that connected technical validation to executive operating decisions and made regulated modernization more consistent across client engagements.
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
