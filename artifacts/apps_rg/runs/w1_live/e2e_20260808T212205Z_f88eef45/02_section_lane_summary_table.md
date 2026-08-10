# apps_rg Mandatory Run Output

Generated: `2026-08-08T21:34:33Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T212205Z_f88eef45`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A_DENY_REROUTE` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3_BLOCK; ibm_bullets:EXECUTED_X3_BLOCK; ey_bullets:EXECUTED_X3_BLOCK; ibm_narrative:upstream_not_finalized; ey_narrative:upstream_not_finalized; executive_summary:EXECUTED_X3_BLOCK; headline:EXECUTED_X3A_DENY_REROUTE' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7515, 'sha256': '89ddef79a126c25cfc24ba7776746968deb0d21966468880d9b5dee2027c5dfe'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,ibm_bullets,ey_bullets,executive_summary,headline,final_resume_aggregation', 'pre_run_blocked=ibm_narrative,ey_narrative']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 16511998, 'sha256': '7d36694af6f9e01a803f8add3f01eefa53f893f62b74f1769f2a551962e407ab'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,ibm_bullets,ey_bullets,executive_summary,headline,final_resume_aggregation', 'pre_run_blocked=ibm_narrative,ey_narrative']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5133, 'sha256': '646fc9e16a4e7275e43dee84701856ad522218502590d6f7439e7a949b3bf4c9'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,ibm_bullets,ey_bullets,executive_summary,headline,final_resume_aggregation', 'pre_run_blocked=ibm_narrative,ey_narrative']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `FAIL` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0'], 'truth_errors': ['bcg.forensics.incomplete_artifact:competencies', 'bcg.forensics.incomplete_artifact:executive_summary', 'bcg.forensics.incomplete_artifact:ey_bullets', 'bcg.forensics.incomplete_artifact:ey_narrative', 'bcg.forensics.incomplete_artifact:final_resume_aggregation', 'bcg.forensics.incomplete_artifact:headline', 'bcg.forensics.incomplete_artifact:ibm_bullets', 'bcg.forensics.incomplete_artifact:ibm_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:competencies', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:ey_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:ey_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:executive_summary', 'bcg.issue_tree.incomplete_forensic_artifact:headline']}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS; judge=gemini-3.6-flash', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 558, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,ibm_bullets,ey_bullets,executive_summary,headline,final_resume_aggregation', 'pre_run_blocked=ibm_narrative,ey_narrative']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `FAIL` | `{'required': True, 'failed_section_count': 8, 'artifact_dir': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics', 'missing_or_incomplete': [{'section_id': 'competencies', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/competencies.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/competencies.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'ibm_bullets', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_bullets.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'ey_bullets', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_bullets.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'ibm_narrative', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'ey_narrative', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_narrative.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'executive_summary', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/executive_summary.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/executive_summary.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'headline', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/headline.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/headline.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_contract_invalid'}, {'section_id': 'final_resume_aggregation', 'json_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/final_resume_aggregation.json', 'md_path': 'artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/final_resume_aggregation.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'aggregation_downstream', 'baseline_confidence': 'pinned_contract_invalid'}]}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `FAIL` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 9 | 4 | 5 | 2 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-terra` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS; judge=gemini-3.6-flash</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=f2e3b3d9bf6a76ef4ee3815148d4390670a95a726bce503ec7f88d99f7dd9a92;<br>ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T212205Z_f88eef45\apps_research\runs\bridge_rg_research_bridge_6b416da9_eab3922a-184c-4d98-84c8-b387835b24cc\briefing.md;<br>target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=6991</code></span> | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T212205Z_f88eef45\apps_research\runs\bridge_rg_research_bridge_6b416da9_eab3922a-184c-4d98-84c8-b387835b24cc\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.8 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.4 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `modular_r4/sections/competencies/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 4.8 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.78 vs 0.72 PASS; Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` | `future_run_advisory_only` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.82 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Deterministic specificity failure: generated text missed required mechanism/technology signal.</code></span> | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` | `future_run_advisory_only` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.82 vs 0.72 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` | `future_run_advisory_only` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; Anthropic Claude / claude-sonnet-5: 0.77 vs 0.72 FAIL` | `decisive_judge_failures=anthropic_claude` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>X1D decisive judge failure: model-backed judge rejected section product quality.</code></span> | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` | `future_run_advisory_only` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/unify_narrative/unify_narrative_output.txt` | `future_run_advisory_only` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.6-luna` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_ALLOW</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>No section-level failure recorded.</code></span> | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` | `future_run_advisory_only` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:upstream_not_finalized</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED</code></span> | `MISSING` | `not_observed` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.</code></span> | `modular_r4/sections/executive_summary/resume_display_text.txt` | `future_run_advisory_only` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.6 Flash / gemini-3.6-flash: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.6-sol: 4.1 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Headline executive positioning contract failure: vendor/tool proof terms reached display without an executive abstraction segment.</code></span> | `modular_r4/sections/headline/headline_output.txt` | `future_run_advisory_only` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding` | `modular_r4/sections/competencies/competencies_display.txt` |
| `unify_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/unify_bullets/unify_bullets_output.txt` |
| `ibm_bullets` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_bullet_technical_specificity_floor` | `modular_r4/sections/ibm_bullets/ibm_bullets_output.txt` |
| `insurtech_bullets` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_bullets/insurtech_bullets_output.txt` |
| `ey_bullets` | `ran_real_llm` | `X3_BLOCK` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/ey_bullets/ey_bullets_output.txt` |
| `unify_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/unify_narrative/unify_narrative_output.txt` |
| `ibm_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `insurtech_narrative` | `ran_real_llm` | `X3_ALLOW` | `PASS` | `PASS` | `REAL_LLM` | `-` | `modular_r4/sections/insurtech_narrative/insurtech_narrative_output.txt` |
| `ey_narrative` | `pre_run_blocked` | `PRE_RUN:upstream_not_finalized` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
| `executive_summary` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids, x2_exec_summary_no_mechanism_inventory, x2_resume_graph_claim_binding` | `modular_r4/sections/executive_summary/resume_display_text.txt` |
| `headline` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_headline_executive_abstraction_floor` | `modular_r4/sections/headline/headline_output.txt` |
| `final_resume_aggregation` | `assembled` | `X3_REVIEW_AGGREGATION` | `UNKNOWN` | `UNKNOWN` | `ASSEMBLED` | `-` | `modular_r4/final_resume_assembly/final_resume.json` |

## Final Resume Product Outputs

| Artifact | Path | Status | Bytes | SHA256 |
|---|---|---|---:|---|
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 16511998 | `7d36694af6f9e01a803f8add3f01eefa53f893f62b74f1769f2a551962e407ab` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 7515 | `89ddef79a126c25cfc24ba7776746968deb0d21966468880d9b5dee2027c5dfe` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 5133 | `646fc9e16a4e7275e43dee84701856ad522218502590d6f7439e7a949b3bf4c9` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 7515, 'sha256': '89ddef79a126c25cfc24ba7776746968deb0d21966468880d9b5dee2027c5dfe'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 5133, 'sha256': '646fc9e16a4e7275e43dee84701856ad522218502590d6f7439e7a949b3bf4c9'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 182, 'ENGINEERING & PLATFORM COMPETENCIES': 1278, 'PROFESSIONAL EXPERIENCE': 3049, 'EDUCATION': 6934, 'CERTIFICATIONS': 7098}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 180, 'ENGINEERING & PLATFORM COMPETENCIES': 1275, 'PROFESSIONAL EXPERIENCE': 3045, 'EDUCATION': 6924, 'CERTIFICATIONS': 7087}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [3074, 3131], 'ibm': [4674, 4688], 'insurtech': [5308, 5361], 'ey': [5796, 5822], 'early_career': [6427, 6492]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [3069, 3126], 'ibm': [4668, 4682], 'insurtech': [5301, 5354], 'ey': [5788, 5814], 'early_career': [6418, 6483]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6944, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 7029}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 6934, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 7019}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 7127, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 7186, 'Certified Solutions Architect – Professional, AWS, 2023': 7240, 'Fellow of the Society of Actuaries, 2010': 7296}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 7116, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 7175, 'Certified Solutions Architect – Professional, AWS, 2023': 7229, 'Fellow of the Society of Actuaries, 2010': 7285}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': True, 'not_generated_by_run': True}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.4 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 4.8 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.78 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `unify_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude,gemini_pro` |
| `ibm_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ibm_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.82 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `insurtech_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_PASS` | 0.82 | 0.72 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,anthropic_claude` |
| `ey_bullets` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `decisive_judge_failures=anthropic_claude, model_backed_pass_provider_keys=gemini_pro` |
| `ey_bullets` | `Anthropic Claude` | `claude-sonnet-5` | `MODEL_BACKED_FAIL` | 0.77 | 0.72 | `FAIL` | `decisive_judge_failures=anthropic_claude, model_backed_pass_provider_keys=gemini_pro` |
| `unify_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ibm_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `insurtech_narrative` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro` |
| `ey_narrative` | `-` | `-` | `section_not_run` |  |  | `UNKNOWN` | `-` |
| `executive_summary` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |
| `headline` | `Google Gemini 3.6 Flash` | `gemini-3.6-flash` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `headline` | `OpenAI ChatGPT` | `gpt-5.6-sol` | `MODEL_BACKED_PASS` | 4.1 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `final_resume_aggregation` | `-` | `-` | `no_judge_rows_observed` |  |  | `UNKNOWN` | `-` |

## RCA Findings

1. `competencies` - Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
   - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
   - Evidence: `x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding`
   - Causal allocation:
     - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
     - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
     - Allocation rows:
       - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
       - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
       - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
       - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
   - Required implementation plan:
     - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
     - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
     - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
     - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
2. `ibm_bullets` - Deterministic specificity failure: generated text missed required mechanism/technology signal.
   - Root cause: The lane does not bind narrative text to evidence-backed mechanism or technology requirements before deterministic specificity validation.
   - Evidence: `x2_bullet_technical_specificity_floor`
   - Causal allocation:
     - Dominant cause: The generated narrative was not constrained to include an evidence-backed mechanism token before deterministic specificity validation.
     - Retry recoverability: `HIGH` - A targeted repair can add a source-backed mechanism or technology token without changing the underlying evidence set.
     - Allocation rows:
       - `Generation instruction / output control` / `PRIMARY` / `45%`: x2_bullet_technical_specificity_floor: bul_ibm_003: no named mechanism/technology in bullet text; bul_ibm_004: no named mechanism/technology in bullet text observed=['bul_ibm_003: no named mechanism/technology in bullet text', 'bul_ibm_004: no named mechanism/technology in bullet text'] Evidence: `x2_narrative_technical_specificity_floor`. Required work: Bind the narrative prompt and repair step to accepted source-backed mechanism vocabulary.
       - `Claim ledger / provenance contract` / `CONTRIBUTING` / `20%`: The accepted mechanism must be present in both display text and the claim ledger, not only in hidden evidence. Evidence: `claim_ledger.json, text_claim_coverage.json`. Required work: Expose the mechanism token in claim text and source_fact_ids before the specificity gate runs.
       - `Retry / repair policy` / `HIGH_RECOVERY` / `25%`: The lane had supported content but missed a deterministic token, so gate-aware text repair is the correct retry shape. Evidence: `x2_narrative_technical_specificity_floor, section_repair_ledger.json`. Required work: Trigger a targeted rewrite that only inserts an evidence-backed mechanism token.
       - `Validation / gate precision` / `DETECTION` / `10%`: The gate names the missing token class but should also emit the accepted vocabulary and evidence source used for repair. Evidence: `x2_gate_outputs.json`. Required work: Include accepted mechanism vocabulary and source-fact anchors in the gate receipt.
   - Required implementation plan:
     - Define the accepted mechanism and technology vocabulary for the lane from source evidence, not from generic resume keywords.
     - Require each narrative sentence that makes a capability claim to bind to at least one evidence-backed mechanism fact.
     - Update the deterministic specificity gate to check evidence-bound mechanisms in the claim ledger before accepting display text.
     - Add a regression fixture with one generic narrative rejection and one mechanism-bound narrative acceptance.
3. `ey_bullets` - X1D decisive judge failure: model-backed judge rejected section product quality.
   - Root cause: The lane published judge-visible narrative text after normalizing the provider payload through a lossy claim-ledger path that dropped source_fact_ids needed to support material claims.
   - Evidence: `Anthropic Claude \| claude-sonnet-5 \| MODEL_BACKED_FAIL \| score=0.77/0.72`
   - Causal allocation:
     - Dominant cause: The section was generated, parsed, and X2-clean, but the published claim ledger lost source-fact bindings that X1D required for judge-visible material claims.
     - Retry recoverability: `LOW_UNTIL_LEDGER_FIX` - Blind regeneration can return a valid parsed claim ledger again, but the same lossy normalization path will keep dropping support before X1D.
     - Allocation rows:
       - `Claim ledger normalization` / `PRIMARY` / `45%`: Anthropic Claude | claude-sonnet-5 | MODEL_BACKED_FAIL | score=0.77/0.72 Evidence: `parsed_output.json, claim_ledger.json, x1d_llm_judge_outputs.json`. Required work: Preserve valid source_fact_ids from parsed narrative claim_ledger rows when publishing the single-sentence role-episode ledger.
       - `Narrative source binding` / `CONTRIBUTING` / `25%`: Narrative material phrases such as insurance operations, model risk, and traceable controls must bind to selected role-episode facts before judge review. Evidence: `selected_fact_plan.json, role_episode_lane.py`. Required work: Add deterministic phrase-to-fact reconciliation for EY narrative material claims within the allowed graph packet.
       - `X1D authorization policy` / `DETECTION` / `20%`: X2 PASS and product PASS were not enough because the model-backed judge rejected factual support. Evidence: `x3_disposition.json, x1d_llm_judge_outputs.json`. Required work: Keep X3 blocked on decisive factual-support judge failures and surface the judge finding as the primary RCA.
       - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: The fix belongs at the parser/ledger boundary, not in downstream rerun scheduling or final assembly. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Rerun only after the narrative ledger preservation fixture and mandatory-RCA fixture pass.
   - Required implementation plan:
     - Preserve valid source_fact_ids from parsed narrative claim_ledger rows when normalizing role-episode narrative output.
     - Add source-binding patterns for material EY insurance, ERM, CCAR, regulatory analytics, and capital/solvency claims.
     - Keep X2 PASS insufficient for authorization when X1D factual-support judges reject the published claim ledger.
     - Add a regression fixture using the live EY narrative where insurance operations must cite reb_ey_insurance_core_modernization.
4. `ibm_narrative` - Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
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
5. `ey_narrative` - Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
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
   - Evidence: `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids, x2_exec_summary_no_mechanism_inventory, x2_resume_graph_claim_binding`
   - Causal allocation:
     - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
     - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
     - Allocation rows:
       - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: The final producer accepted text that still carried robotic S2-S5 transition openers. Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
       - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: The claim ledger dropped the B4 commercialization-leadership fact required by the composition plan. Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
       - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
       - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids, x2_exec_summary_no_mechanism_inventory, x2_resume_graph_claim_binding`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
   - Required implementation plan:
     - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
     - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
     - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
     - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.
7. `headline` - Headline executive positioning contract failure: vendor/tool proof terms reached display without an executive abstraction segment.
   - Root cause: The headline normalization path did not rewrite a vendor-specific migration phrase into the executive positioning vocabulary required for X/Y/Z display segments.
   - Evidence: `x2_headline_executive_abstraction_floor`
   - Causal allocation:
     - Dominant cause: The headline producer let a vendor-specific migration phrase remain in display position instead of projecting it to a proof-backed executive operating abstraction.
     - Retry recoverability: `HIGH_AFTER_NORMALIZATION_FIX` - The selected proof was valid and judges passed; deterministic normalization can recover by rewriting the display segment and ledger before X2.
     - Allocation rows:
       - `Headline normalization / display policy` / `PRIMARY` / `45%`: x2_headline_executive_abstraction_floor: Each headline segment must express executive scope such as platform, architecture, governance, ecosystem, commercialization, or regulated systems. observed={'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Enterprise Portfolio Leadership', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Runtime Governance Controls', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Context Engineering Evaluation', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Context Engineering Evaluation'], 'vendor_terms_without_executive_abstraction': []} Evidence: `x2_headline_executive_abstraction_floor, x2_headline_vendor_terms_proof_only`. Required work: Rewrite vendor-specific migration phrases to allowed executive headline abstractions before display validation.
       - `Claim ledger segment rebinding` / `CONTRIBUTING` / `25%`: Headline segment rewrites must also update claim_text rows so visible X/Y/Z phrases remain the ledger authority. Evidence: `claim_ledger.json, parsed_output.json`. Required work: Rebuild the three segment claim-ledger rows after deterministic headline phrase repair.
       - `Validation / gate precision` / `DETECTION` / `20%`: The deterministic headline gates correctly blocked a proof-only vendor term in display despite model-backed judge passes. Evidence: `x2_gate_outputs.json`. Required work: Keep display-policy X2 gates authoritative over X1D judge approval for headline formatting and abstraction constraints.
       - `Retry / repair policy` / `HIGH_RECOVERY` / `10%`: The failure is a deterministic phrase-normalization gap, so a targeted repair fixture should recover without changing research or section evidence. Evidence: `headline_output.txt`. Required work: Rerun after the live failed headline fixture proves X2 clears with the repaired segment.
   - Required implementation plan:
     - Map vendor-specific migration fragments to proof-backed executive headline abstractions before X2 runs.
     - Rebuild the segment claim ledger after headline rewrites so the displayed X/Y/Z phrases remain source-bound.
     - Keep vendor names and product terms in proof evidence, not standalone display segments, unless the segment also carries an executive abstraction.
     - Add a regression fixture using the live failed headline with AWS Migration Modernization Execution.

## Section Failure Forensics

Gate `E2E_FAIL_WITHOUT_SECTION_FORENSICS`: `FAIL`
- Required: `True`
- Failed section count: `8`
- Artifact directory: `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics`
- Baseline confidence: `pinned_contract_invalid`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `competencies` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/competencies.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/competencies.md` |
| `ibm_bullets` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_bullets.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_bullets.md` |
| `ey_bullets` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_bullets.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_bullets.md` |
| `ibm_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ibm_narrative.md` |
| `ey_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_narrative.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/ey_narrative.md` |
| `executive_summary` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/executive_summary.md` |
| `headline` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `False` | `False` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/w1_live/e2e_20260808T212205Z_f88eef45/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 18 | `future_run_advisory_only` |
| `unify_bullets` | 15 | `future_run_advisory_only` |
| `ibm_bullets` | 15 | `future_run_advisory_only` |
| `insurtech_bullets` | 1 | `future_run_advisory_only` |
| `ey_bullets` | 1 | `future_run_advisory_only` |
| `unify_narrative` | 16 | `future_run_advisory_only` |
| `ibm_narrative` | 0 | `not_observed` |
| `insurtech_narrative` | 1 | `future_run_advisory_only` |
| `ey_narrative` | 0 | `not_observed` |
| `executive_summary` | 18 | `future_run_advisory_only` |
| `headline` | 14 | `future_run_advisory_only` |
| `final_resume_aggregation` | 0 | `not_observed` |

## Resume DOCX Full Version Inline

Source: `No authorized resume text emitted; this block is derived only from the current E2E run ledger and final-resume output contract.`

```text
NO_AUTHORIZED_RESUME_OUTPUT
source_of_truth=current_e2e_run_artifacts_only
run_root=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T212205Z_f88eef45
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=competencies,ibm_bullets,ey_bullets,executive_summary,headline,final_resume_aggregation; pre_run_blocked=ibm_narrative,ey_narrative
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
