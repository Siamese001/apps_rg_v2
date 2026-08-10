# apps_rg Mandatory Run Output

Generated: `2026-08-09T10:24:34Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry22_20260809\e2e_20260809T102053Z_3266f3a1`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:ibm_bullets:EXECUTED_X3A_DENY_REROUTE; insurtech_bullets:PHASE1_NO_RUN_DIR; ey_bullets:PHASE1_NO_RUN_DIR; unify_narrative:PHASE1_NO_RUN_DIR; ibm_narrative:PHASE1_NO_RUN_DIR; insurtech_narrative:PHASE1_NO_RUN_DIR; ey_narrative:PHASE1_NO_RUN_DIR; executive_summary:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 4503, 'sha256': '8989ad527227c4636e772c46a2ddd62a74a3115b78870af798cd03d9eef1778b'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 5634794, 'sha256': '2325eb692850da2f56263775b91906968af5f2802ff8e3e532d94e1b76874f8f'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4033, 'sha256': 'a38ae2ab6f552fb9925181ac723786c035522be79f2c41478537a53f2e90205d'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0', 'P1'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 618, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 9, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics', 'missing_or_incomplete': []}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `PASS` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 3 | 3 | 0 | 8 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=224cf9baeb7969c8cb503ce2ff8f2d1531399bdc197dd0bed39c6d395b9d0d3c;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry22_20260809\e2e_20260809T102053Z_3266f3a1\apps_research\runs\r-f4e7da93ac2ddf09a574981a\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7798</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry22_20260809\e2e_20260809T102053Z_3266f3a1\apps_research\runs\r-f4e7da93ac2ddf09a574981a\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.6 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.77 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:WriteAmplificationError:WRITE_AMPLIFICATION_DETECTED: path=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry22_20260809\e2e_20260809T102053Z_3266f3a1\modular_r4\sections\ibm_bullets\l2_output.json original=8914 proposed=22439 growth_ratio=2.52x max=2.0x</code></span> | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` | `not_observed` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ey_bullets` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `unify_narrative` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ibm_narrative` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `insurtech_narrative` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ey_narrative` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `executive_summary` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `headline` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 5634794 | `2325eb692850da2f56263775b91906968af5f2802ff8e3e532d94e1b76874f8f` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 4503 | `8989ad527227c4636e772c46a2ddd62a74a3115b78870af798cd03d9eef1778b` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 4033 | `a38ae2ab6f552fb9925181ac723786c035522be79f2c41478537a53f2e90205d` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 4503, 'sha256': '8989ad527227c4636e772c46a2ddd62a74a3115b78870af798cd03d9eef1778b'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4033, 'sha256': 'a38ae2ab6f552fb9925181ac723786c035522be79f2c41478537a53f2e90205d'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 182, 'ENGINEERING & PLATFORM COMPETENCIES': 273, 'PROFESSIONAL EXPERIENCE': 1796, 'EDUCATION': 3948, 'CERTIFICATIONS': 4112}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 180, 'ENGINEERING & PLATFORM COMPETENCIES': 270, 'PROFESSIONAL EXPERIENCE': 1792, 'EDUCATION': 3938, 'CERTIFICATIONS': 4101}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [1821, 1878], 'ibm': [3028, 3042], 'insurtech': [3166, 3219], 'ey': [3346, 3372], 'early_career': [3492, 3557]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [1816, 1873], 'ibm': [3022, 3036], 'insurtech': [3159, 3212], 'ey': [3338, 3364], 'early_career': [3483, 3548]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 3958, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 4043}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 3948, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 4033}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 4141, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 4200, 'Certified Solutions Architect – Professional, AWS, 2023': 4254, 'Fellow of the Society of Actuaries, 2010': 4310}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 4130, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 4189, 'Certified Solutions Architect – Professional, AWS, 2023': 4243, 'Fellow of the Society of Actuaries, 2010': 4299}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': True, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.6 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.77 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ey_bullets` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `unify_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ibm_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `insurtech_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ey_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `executive_summary` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `headline` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `insurtech_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
2. `ey_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
3. `unify_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
4. `ibm_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
5. `insurtech_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
6. `ey_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
7. `executive_summary` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
8. `headline` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `PASS`
- Required: `True`
- Failed section count: `9`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `insurtech_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/insurtech_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/insurtech_bullets.md` |
| `ey_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ey_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ey_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/unify_narrative.md` |
| `ibm_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ibm_narrative.md` |
| `insurtech_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/insurtech_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/insurtech_narrative.md` |
| `ey_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ey_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/ey_narrative.md` |
| `executive_summary` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/executive_summary.md` |
| `headline` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry22_20260809/e2e_20260809T102053Z_3266f3a1/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 17 | `future_run_advisory_only` |
| `unify_bullets` | 15 | `future_run_advisory_only` |
| `ibm_bullets` | 0 | `not_observed` |
| `insurtech_bullets` | 0 | `not_observed` |
| `ey_bullets` | 0 | `not_observed` |
| `unify_narrative` | 0 | `not_observed` |
| `ibm_narrative` | 0 | `not_observed` |
| `insurtech_narrative` | 0 | `not_observed` |
| `ey_narrative` | 0 | `not_observed` |
| `executive_summary` | 0 | `not_observed` |
| `headline` | 0 | `not_observed` |
| `final_resume_aggregation` | 0 | `not_observed` |

## Resume DOCX Full Version Inline

Source: `No authorized resume text emitted; this block is derived only from the current E2E run ledger and final-resume output contract.`

```text
NO_AUTHORIZED_RESUME_OUTPUT
source_of_truth=current_e2e_run_artifacts_only
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry22_20260809\e2e_20260809T102053Z_3266f3a1
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=final_resume_aggregation; pre_run_blocked=insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
