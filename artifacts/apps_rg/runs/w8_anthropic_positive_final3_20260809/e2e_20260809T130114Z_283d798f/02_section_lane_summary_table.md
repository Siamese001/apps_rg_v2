# apps_rg Mandatory Run Output

Generated: `2026-08-09T13:03:17Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final3_20260809\e2e_20260809T130114Z_283d798f`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3A_DENY_REROUTE; unify_bullets:PHASE1_NO_RUN_DIR; ibm_bullets:PHASE1_NO_RUN_DIR; insurtech_bullets:PHASE1_NO_RUN_DIR; ey_bullets:PHASE1_NO_RUN_DIR; unify_narrative:PHASE1_NO_RUN_DIR; ibm_narrative:PHASE1_NO_RUN_DIR; insurtech_narrative:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 2059, 'sha256': 'c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=competencies,unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 7031, 'sha256': 'b185dbdac3baad8f1c9aafb193b1ad8147ae35d84142be63c2ef567d7bf9315c'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=competencies,unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 2948, 'sha256': '95bd28ece12bc20c396bade79ba52621dd124f7de40f1d02b9596f7a613832ea'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=competencies,unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0', 'P1'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 656, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=final_resume_aggregation', 'pre_run_blocked=competencies,unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 12, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics', 'missing_or_incomplete': []}` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 0 | 0 | 0 | 11 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=741931df97fef3133f9a6b7596afb5915cc47641ea400b37081bb0a49c73946b;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final3_20260809\e2e_20260809T130114Z_283d798f\apps_research\runs\r-a567938cd6c8d11f09a0f25b\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7687</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final3_20260809\e2e_20260809T130114Z_283d798f\apps_research\runs\r-a567938cd6c8d11f09a0f25b\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:EXECUTED_X3A_DENY_REROUTE</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:OSError:[Errno 22] Invalid argument</code></span> | `MISSING` | `not_observed` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED</code></span> | `MISSING` | `not_observed` |
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
| `competencies` | `pre_run_blocked` | `PRE_RUN:EXECUTED_X3A_DENY_REROUTE` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `unify_bullets` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ibm_bullets` | `pre_run_blocked` | `PRE_RUN:PHASE1_NO_RUN_DIR` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
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
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 7031 | `b185dbdac3baad8f1c9aafb193b1ad8147ae35d84142be63c2ef567d7bf9315c` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 2059 | `c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 2948 | `95bd28ece12bc20c396bade79ba52621dd124f7de40f1d02b9596f7a613832ea` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 2059, 'sha256': 'c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 2948, 'sha256': '95bd28ece12bc20c396bade79ba52621dd124f7de40f1d02b9596f7a613832ea'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 182, 'ENGINEERING & PLATFORM COMPETENCIES': 273, 'PROFESSIONAL EXPERIENCE': 392, 'EDUCATION': 1524, 'CERTIFICATIONS': 1688}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 180, 'ENGINEERING & PLATFORM COMPETENCIES': 270, 'PROFESSIONAL EXPERIENCE': 388, 'EDUCATION': 1514, 'CERTIFICATIONS': 1677}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [417, 474], 'ibm': [604, 618], 'insurtech': [742, 795], 'ey': [922, 948], 'early_career': [1068, 1133]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [412, 469], 'ibm': [598, 612], 'insurtech': [735, 788], 'ey': [914, 940], 'early_career': [1059, 1124]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 1534, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 1619}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 1524, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 1609}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 1717, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 1776, 'Certified Solutions Architect – Professional, AWS, 2023': 1830, 'Fellow of the Society of Actuaries, 2010': 1886}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 1706, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 1765, 'Certified Solutions Architect – Professional, AWS, 2023': 1819, 'Fellow of the Society of Actuaries, 2010': 1875}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': True, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `unify_bullets` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ibm_bullets` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
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

1. `competencies` - Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:OSError:[Errno 22] Invalid argument
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:EXECUTED_X3A_DENY_REROUTE`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:OSError:[Errno 22] Invalid argument Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
2. `unify_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
3. `ibm_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
4. `insurtech_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
5. `ey_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
6. `unify_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
7. `ibm_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
8. `insurtech_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
9. `ey_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
10. `executive_summary` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
11. `headline` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
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
- Failed section count: `12`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `competencies` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/competencies.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/competencies.md` |
| `unify_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/unify_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/unify_bullets.md` |
| `ibm_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ibm_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ibm_bullets.md` |
| `insurtech_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/insurtech_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/insurtech_bullets.md` |
| `ey_bullets` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ey_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ey_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/unify_narrative.md` |
| `ibm_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ibm_narrative.md` |
| `insurtech_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/insurtech_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/insurtech_narrative.md` |
| `ey_narrative` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ey_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/ey_narrative.md` |
| `executive_summary` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/executive_summary.md` |
| `headline` | `upstream_cascade` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_final3_20260809/e2e_20260809T130114Z_283d798f/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 0 | `not_observed` |
| `unify_bullets` | 0 | `not_observed` |
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
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final3_20260809\e2e_20260809T130114Z_283d798f
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=final_resume_aggregation; pre_run_blocked=competencies,unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
