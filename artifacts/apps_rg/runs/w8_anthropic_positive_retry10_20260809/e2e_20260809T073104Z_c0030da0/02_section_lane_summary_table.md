# apps_rg Mandatory Run Output

Generated: `2026-08-09T07:37:20Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry10_20260809\e2e_20260809T073104Z_c0030da0`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3_ALLOW; unify_bullets:EXECUTED_X3_BLOCK; ibm_bullets:EXECUTED_X3_BLOCK; unify_narrative:upstream_not_finalized; ibm_narrative:upstream_not_finalized; executive_summary:EXECUTED_X3_BLOCK; headline:EXECUTED_X3A_DENY_REROUTE' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 6793, 'sha256': '45478f0888912030678f6cb419e1fdea774b93e0c0305398638ac2b29a5b8b18'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,unify_bullets,ibm_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative,ibm_narrative,headline']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 19170606, 'sha256': 'b604b6e0088ff4d8cfd8cc8531bb9ba9fe5ddd2027b7a6cf4ab742f96ddd77c9'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,unify_bullets,ibm_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative,ibm_narrative,headline']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4885, 'sha256': '0b7c0df44660da727a44b49d443e8bc436f831a45e9715f9eb9007f833415498'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,unify_bullets,ibm_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative,ibm_narrative,headline']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `FAIL` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': ['bcg.forensics.incomplete_artifact:competencies', 'bcg.forensics.incomplete_artifact:executive_summary', 'bcg.forensics.incomplete_artifact:final_resume_aggregation', 'bcg.forensics.incomplete_artifact:headline', 'bcg.forensics.incomplete_artifact:ibm_bullets', 'bcg.forensics.incomplete_artifact:ibm_narrative', 'bcg.forensics.incomplete_artifact:unify_bullets', 'bcg.forensics.incomplete_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:competencies', 'bcg.issue_tree.incomplete_forensic_artifact:unify_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:executive_summary', 'bcg.issue_tree.incomplete_forensic_artifact:headline']}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 595, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,unify_bullets,ibm_bullets,executive_summary,final_resume_aggregation', 'pre_run_blocked=unify_narrative,ibm_narrative,headline']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `FAIL` | `{'required': True, 'failed_section_count': 8, 'artifact_dir': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics', 'missing_or_incomplete': [{'section_id': 'competencies', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/competencies.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/competencies.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'unify_bullets', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_bullets.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ibm_bullets', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_bullets.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'unify_narrative', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ibm_narrative', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'executive_summary', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/executive_summary.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/executive_summary.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'headline', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/headline.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/headline.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'final_resume_aggregation', 'json_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/final_resume_aggregation.json', 'md_path': 'artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/final_resume_aggregation.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'aggregation_downstream', 'baseline_confidence': 'pinned_baseline_unavailable'}]}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `FAIL` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 8 | 4 | 4 | 3 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=1f6a61b95747c1b0b513e7014441a777fb26f117f8e105ace7aa48b9c339303b;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry10_20260809\e2e_20260809T073104Z_c0030da0\apps_research\runs\r-a2c5cbf2348185f5b43843f6\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7809</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry10_20260809\e2e_20260809T073104Z_c0030da0\apps_research\runs\r-a2c5cbf2348185f5b43843f6\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.4 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.76 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Deterministic gate failure.</code></span> | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.74 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Deterministic specificity failure: generated text missed required mechanism/technology signal.</code></span> | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.76 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 0.76 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` | `future_run_advisory_only` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.</code></span> | `modular_r4/sections/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:EXECUTED_X3A_DENY_REROUTE</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:TypeError:normalize_parsed_output() got an unexpected keyword argument 'artifact_dir'</code></span> | `MISSING` | `not_observed` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` | `FAIL` | `PASS` | `REAL_LLM` | `x2_resume_graph_claim_binding` | `modular_r4/sections/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_unify_only_fact_scope` | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_bullet_technical_specificity_floor` | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `ibm_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_narrative/ey_narrative_output.txt` |
| `executive_summary` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_exec_summary_display_override_compliance, x2_resume_graph_claim_binding` | `modular_r4/sections/executive_summary/resume_display_text.txt` |
| `headline` | `pre_run_blocked` | `PRE_RUN:EXECUTED_X3A_DENY_REROUTE` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 19170606 | `b604b6e0088ff4d8cfd8cc8531bb9ba9fe5ddd2027b7a6cf4ab742f96ddd77c9` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 6793 | `45478f0888912030678f6cb419e1fdea774b93e0c0305398638ac2b29a5b8b18` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 4885 | `0b7c0df44660da727a44b49d443e8bc436f831a45e9715f9eb9007f833415498` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 6793, 'sha256': '45478f0888912030678f6cb419e1fdea774b93e0c0305398638ac2b29a5b8b18'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 4885, 'sha256': '0b7c0df44660da727a44b49d443e8bc436f831a45e9715f9eb9007f833415498'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 182, 'ENGINEERING & PLATFORM COMPETENCIES': 1071, 'PROFESSIONAL EXPERIENCE': 2805, 'EDUCATION': 6220, 'CERTIFICATIONS': 6384}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 180, 'ENGINEERING & PLATFORM COMPETENCIES': 1068, 'PROFESSIONAL EXPERIENCE': 2801, 'EDUCATION': 6210, 'CERTIFICATIONS': 6373}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2830, 2887], 'ibm': [4046, 4060], 'insurtech': [4696, 4749], 'ey': [5084, 5110], 'early_career': [5713, 5778]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [2825, 2882], 'ibm': [4040, 4054], 'insurtech': [4689, 4742], 'ey': [5076, 5102], 'early_career': [5704, 5769]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6230, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6315}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6220, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 6305}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6413, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6472, 'Certified Solutions Architect – Professional, AWS, 2023': 6526, 'Fellow of the Society of Actuaries, 2010': 6582}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 6402, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 6461, 'Certified Solutions Architect – Professional, AWS, 2023': 6515, 'Fellow of the Society of Actuaries, 2010': 6571}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': True, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.4 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.76 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ibm_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.74 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `insurtech_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.76 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `ey_bullets` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 0.76 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `ibm_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `executive_summary` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |
| `headline` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `competencies` - Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
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
2. `unify_bullets` - Deterministic gate failure.
   - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
   - Evidence: `x2_unify_only_fact_scope`
   - Causal allocation:
     - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
     - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
     - Allocation rows:
       - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x2_unify_only_fact_scope`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
   - Required implementation plan:
     - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
     - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
     - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
3. `ibm_bullets` - Deterministic specificity failure: generated text missed required mechanism/technology signal.
   - Root cause: The lane does not bind narrative text to evidence-backed mechanism or technology requirements before deterministic specificity validation.
   - Evidence: `x2_bullet_technical_specificity_floor`
   - Causal allocation:
     - Dominant cause: The generated narrative was not constrained to include an evidence-backed mechanism token before deterministic specificity validation.
     - Retry recoverability: `HIGH` - A targeted repair can add a source-backed mechanism or technology token without changing the underlying evidence set.
     - Allocation rows:
       - `Generation instruction / output control` / `PRIMARY` / `45%`: x2_bullet_technical_specificity_floor: bul_ibm_002: no named mechanism/technology in bullet text observed=['bul_ibm_002: no named mechanism/technology in bullet text'] Evidence: `x2_narrative_technical_specificity_floor`. Required work: Bind the narrative prompt and repair step to accepted source-backed mechanism vocabulary.
       - `Claim ledger / provenance contract` / `CONTRIBUTING` / `20%`: The accepted mechanism must be present in both display text and the claim ledger, not only in hidden evidence. Evidence: `claim_ledger.json, text_claim_coverage.json`. Required work: Expose the mechanism token in claim text and source_fact_ids before the specificity gate runs.
       - `Retry / repair policy` / `HIGH_RECOVERY` / `25%`: The lane had supported content but missed a deterministic token, so gate-aware text repair is the correct retry shape. Evidence: `x2_narrative_technical_specificity_floor, section_repair_ledger.json`. Required work: Trigger a targeted rewrite that only inserts an evidence-backed mechanism token.
       - `Validation / gate precision` / `DETECTION` / `10%`: The gate names the missing token class but should also emit the accepted vocabulary and evidence source used for repair. Evidence: `x2_gate_outputs.json`. Required work: Include accepted mechanism vocabulary and source-fact anchors in the gate receipt.
   - Required implementation plan:
     - Define the accepted mechanism and technology vocabulary for the lane from source evidence, not from generic resume keywords.
     - Require each narrative sentence that makes a capability claim to bind to at least one evidence-backed mechanism fact.
     - Update the deterministic specificity gate to check evidence-bound mechanisms in the claim ledger before accepting display text.
     - Add a regression fixture with one generic narrative rejection and one mechanism-bound narrative acceptance.
4. `unify_narrative` - Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
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
5. `ibm_narrative` - Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
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
6. `executive_summary` - Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.
   - Root cause: The executive-summary final producer path accepted repaired prose before revalidating required brushstroke coverage, row-level attribution density, and non-robotic transition shape.
   - Evidence: `x2_exec_summary_display_override_compliance, x2_resume_graph_claim_binding`
   - Causal allocation:
     - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
     - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
     - Allocation rows:
       - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: The final producer accepted text that still carried robotic S2-S5 transition openers. Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
       - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: The claim ledger dropped the B4 commercialization-leadership fact required by the composition plan. Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
       - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
       - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_exec_summary_display_override_compliance, x2_resume_graph_claim_binding`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
   - Required implementation plan:
     - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
     - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
     - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
     - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.
7. `headline` - Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:TypeError:normalize_parsed_output() got an unexpected keyword argument 'artifact_dir'
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:EXECUTED_X3A_DENY_REROUTE`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:TypeError:normalize_parsed_output() got an unexpected keyword argument 'artifact_dir' Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `FAIL`
- Required: `True`
- Failed section count: `8`
- Artifact directory: `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics`
- Baseline confidence: `pinned_baseline_unavailable`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `competencies` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/competencies.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/competencies.md` |
| `unify_bullets` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_bullets.md` |
| `ibm_bullets` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_bullets.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/unify_narrative.md` |
| `ibm_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/ibm_narrative.md` |
| `executive_summary` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/executive_summary.md` |
| `headline` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `False` | `False` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w8_anthropic_positive_retry10_20260809/e2e_20260809T073104Z_c0030da0/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 18 | `future_run_advisory_only` |
| `unify_bullets` | 15 | `future_run_advisory_only` |
| `ibm_bullets` | 15 | `future_run_advisory_only` |
| `insurtech_bullets` | 1 | `future_run_advisory_only` |
| `ey_bullets` | 1 | `future_run_advisory_only` |
| `unify_narrative` | 0 | `not_observed` |
| `ibm_narrative` | 0 | `not_observed` |
| `insurtech_narrative` | 1 | `future_run_advisory_only` |
| `ey_narrative` | 1 | `future_run_advisory_only` |
| `executive_summary` | 18 | `future_run_advisory_only` |
| `headline` | 0 | `not_observed` |
| `final_resume_aggregation` | 0 | `not_observed` |

## Resume DOCX Full Version Inline

Source: `No authorized resume text emitted; this block is derived only from the current E2E run ledger and final-resume output contract.`

```text
NO_AUTHORIZED_RESUME_OUTPUT
source_of_truth=current_e2e_run_artifacts_only
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry10_20260809\e2e_20260809T073104Z_c0030da0
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=competencies,unify_bullets,ibm_bullets,executive_summary,final_resume_aggregation; pre_run_blocked=unify_narrative,ibm_narrative,headline
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
