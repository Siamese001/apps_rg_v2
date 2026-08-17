# apps_rg Mandatory Run Output

Generated: `2026-08-17T02:57:34Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3_REVIEW_JUDGE_SOFT_FAIL` |
| Fault | `RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:unify_bullets:PHASE1_NO_RUN_DIR; unify_narrative:PHASE1_NO_RUN_DIR; executive_summary:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7206, 'sha256': '150fa147aea79d195d797284cceb931189f04eba79474931a3780ba7b92f3211'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 21745861, 'sha256': '906b9c9d66199d7efc30179aa80f4f9e2073a1fb94281b4f5102b20887bb1880'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4997, 'sha256': '388741b4ce4ab25118673d50161e79a23db722de82b534f3a6dea8fc93b008e2'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 471, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=unify_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 4, 'artifact_dir': 'artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics', 'missing_or_incomplete': []}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `PASS` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 10 | 8 | 2 | 1 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=4d45accc9442371277e957bd80d88e334a7517eca6add0f8f4d853fcb8d218d9;<br>ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7999</code></span> | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.8 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `lanes/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.74 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 3 vs 4 FAIL` | `decisive_judge_failures=gemini_pro` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Deterministic gate failure.</code></span> | `lanes/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.77 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.8 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.83 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ibm_narrative/ibm_narrative_output.txt` | `future_run_advisory_only` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.</code></span> | `lanes/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.8 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `lanes/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_bullet_seniority_floor` | `lanes/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ibm_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ibm_narrative/ibm_narrative_output.txt` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/ey_narrative/ey_narrative_output.txt` |
| `executive_summary` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory` | `lanes/executive_summary/resume_display_text.txt` |
| `headline` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `lanes/headline/headline_output.txt` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 21745861 | `906b9c9d66199d7efc30179aa80f4f9e2073a1fb94281b4f5102b20887bb1880` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 7206 | `150fa147aea79d195d797284cceb931189f04eba79474931a3780ba7b92f3211` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 4997 | `388741b4ce4ab25118673d50161e79a23db722de82b534f3a6dea8fc93b008e2` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7206, 'sha256': '150fa147aea79d195d797284cceb931189f04eba79474931a3780ba7b92f3211'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4997, 'sha256': '388741b4ce4ab25118673d50161e79a23db722de82b534f3a6dea8fc93b008e2'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 233, 'ENGINEERING & PLATFORM COMPETENCIES': 1370, 'PROFESSIONAL EXPERIENCE': 2947, 'EDUCATION': 6634, 'CERTIFICATIONS': 6798}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 231, 'ENGINEERING & PLATFORM COMPETENCIES': 1367, 'PROFESSIONAL EXPERIENCE': 2943, 'EDUCATION': 6624, 'CERTIFICATIONS': 6787}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2972, 3029], 'ibm': [4126, 4140], 'insurtech': [5166, 5219], 'ey': [5549, 5575], 'early_career': [6178, 6243]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2967, 3024], 'ibm': [4120, 4134], 'insurtech': [5159, 5212], 'ey': [5541, 5567], 'early_career': [6169, 6234]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6644, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6729}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6634, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6719}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6827, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6886, 'Certified Solutions Architect – Professional, AWS, 2023': 6940, 'Fellow of the Society of Actuaries, 2010': 6996}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6816, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6875, 'Certified Solutions Architect – Professional, AWS, 2023': 6929, 'Fellow of the Society of Actuaries, 2010': 6985}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': False, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `decisive_judge_failures=gemini_pro, model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `unify_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `decisive_judge_failures=gemini_pro, model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_FAIL` | 3 | 4 | `FAIL` | `decisive_judge_failures=gemini_pro, model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.77 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.8 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.83 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `unify_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ibm_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `unify_bullets` - Deterministic gate failure.
   - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
   - Evidence: `x2_bullet_seniority_floor`
   - Causal allocation:
     - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
     - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
     - Allocation rows:
       - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x2_bullet_seniority_floor`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
   - Required implementation plan:
     - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
     - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
     - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
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
3. `executive_summary` - Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.
   - Root cause: The executive-summary final producer path accepted repaired prose before revalidating required brushstroke coverage, row-level attribution density, and non-robotic transition shape.
   - Evidence: `x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory`
   - Causal allocation:
     - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
     - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
     - Allocation rows:
       - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: The final producer accepted text that still carried robotic S2-S5 transition openers. Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
       - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: x2_exec_summary_allowed_fact_utilization: uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] observed=uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
       - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
       - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
   - Required implementation plan:
     - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
     - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
     - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
     - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `PASS`
- Required: `True`
- Failed section count: `4`
- Artifact directory: `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `unify_bullets` | `independent_failure` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.json` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.md` |
| `executive_summary` | `independent_failure` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `True` | `False` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/final_resume_aggregation.md` |

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
run_root=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=unify_bullets,executive_summary,final_resume_aggregation; pre_run_blocked=unify_narrative
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
