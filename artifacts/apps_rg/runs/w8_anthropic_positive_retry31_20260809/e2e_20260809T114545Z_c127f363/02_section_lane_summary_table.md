# apps_rg Mandatory Run Output

Generated: `2026-08-09T11:46:43Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry31_20260809\e2e_20260809T114545Z_c127f363`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3_BLOCK` |
| Fault | `APPS_RESEARCH_BLOCKED` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `1` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 2059, 'sha256': 'c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 7031, 'sha256': 'dffb6d397854cad43c2e8d9b238579cef8e0a0d8a35564e73ccceb8d92f7ef2a'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 2948, 'sha256': '985635530e95a14dde23415c355cf36fc8fde1cd66f25da332a86eba9e33cd02'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `PASS` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': []}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'MISSING_BRIEFING'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'NOT_OBSERVED; blocker=no_apps_research_handoff_present', 'x3': 'FAIL'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 445, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `PASS` | `{'required': True, 'failed_section_count': 1, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry31_20260809/e2e_20260809T114545Z_c127f363/section_failure_forensics', 'missing_or_incomplete': []}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `PASS` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NO` | `True` | `NOT_OBSERVED` | `MODEL_NOT_OBSERVED` | `N/A` | `N/A` | `N/A` | `MISSING_BRIEFING` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>NOT_OBSERVED;<br>blocker=no_apps_research_handoff_present</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=NOT_OBSERVED; briefing missing</code></span> | `MISSING` | `N/A` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 7031 | `dffb6d397854cad43c2e8d9b238579cef8e0a0d8a35564e73ccceb8d92f7ef2a` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 2059 | `c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 2948 | `985635530e95a14dde23415c355cf36fc8fde1cd66f25da332a86eba9e33cd02` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry31_20260809/e2e_20260809T114545Z_c127f363/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 2059, 'sha256': 'c421c11523a9a0230e0db27c5a167b3603cfff9b26d34372f175d7982e12fb60'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 2948, 'sha256': '985635530e95a14dde23415c355cf36fc8fde1cd66f25da332a86eba9e33cd02'}` |
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

## RCA Findings

- No blocking RCA findings recorded.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `PASS`
- Required: `True`
- Failed section count: `1`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_retry31_20260809/e2e_20260809T114545Z_c127f363/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `whole_run` | `mandatory_output_authorization_block` | `True` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry31_20260809/e2e_20260809T114545Z_c127f363/section_failure_forensics/whole_run.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry31_20260809/e2e_20260809T114545Z_c127f363/section_failure_forensics/whole_run.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|

## Resume DOCX Full Version Inline

Source: `No authorized resume text emitted; this block is derived only from the current E2E run ledger and final-resume output contract.`

```text
NO_AUTHORIZED_RESUME_OUTPUT
source_of_truth=current_e2e_run_artifacts_only
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry31_20260809\e2e_20260809T114545Z_c127f363
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
