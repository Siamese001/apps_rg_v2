# apps_rg Mandatory Run Output

Generated: `2026-07-21T01:04:30Z`
Run root: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8`

## Outcome

| Field | Value |
|---|---|
| Exit status | `error` |
| Execution status | `failed` |
| Outcome authorized | `False` |
| X3 disposition | `X3A` |
| Fault | `L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3_BLOCK; unify_bullets:EXECUTED_X3A; ibm_bullets:PHASE1_NO_RUN_DIR; insurtech_bullets:PHASE1_NO_RUN_DIR; ey_bullets:PHASE1_NO_RUN_DIR; unify_narrative:PHASE1_NO_RUN_DIR; ibm_narrative:PHASE1_NO_RUN_DIR; insurtech_narrative:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False` |
| Integrated proof gate | `-` `-` |
| Final resume output gate | `FAIL` |

## Mandatory Inline Output Gates

| Gate | Status | Observed |
|---|---|---|
| `mandatory_bcg_inline_output_present` | `PASS` | `01_BCG_executive_output.md` |
| `mandatory_section_lane_table_inline_present` | `PASS` | `13` |
| `mandatory_resume_text_inline_present` | `FAIL` | `{'artifact': {'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 3406, 'sha256': '9ee32564ce820352b2d84dc6141363716bef05af6b49c2bed707886c1077c2bb'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,final_resume_aggregation', 'pre_run_blocked=unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_final_resume_json_present` | `FAIL` | `{'artifact': {'relpath': 'modular_r4/final_resume_assembly/final_resume.json', 'exists': True, 'bytes': 1894241, 'sha256': '15fc8eeda81d9f6ff57fe842f1ac00f4001cd3b2adf63494a96feb70c63cbd81'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,final_resume_aggregation', 'pre_run_blocked=unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_resume_docx_present` | `FAIL` | `{'artifact': {'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 38500, 'sha256': '6bfc97346ab4293e4af1ebfe6f6efb92d9a45c3eae7614e138a470f7c33bb3e8'}, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,final_resume_aggregation', 'pre_run_blocked=unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `mandatory_inline_required_json_shape_locked` | `PASS` | `{'schema_version': 'apps_rg.inline_required_output.v1', 'immutable_section_order': ['bcg', 'section_lane_summary_table', 'resume_docx_full_version_inline'], 'shape_errors': []}` |
| `mandatory_bcg_p0_p1_px_recommendations_locked` | `FAIL` | `{'title': 'BCG Executive Output - apps_rg Run', 'section_order': ['executive_answer', 'p0_p1_px_recommendations', 'board_level_readout', 'issue_tree', 'recommended_next_move', 'evidence_map'], 'priorities': ['P0', 'P1'], 'truth_errors': ['bcg.forensics.incomplete_artifact:competencies', 'bcg.forensics.incomplete_artifact:executive_summary', 'bcg.forensics.incomplete_artifact:ey_bullets', 'bcg.forensics.incomplete_artifact:ey_narrative', 'bcg.forensics.incomplete_artifact:final_resume_aggregation', 'bcg.forensics.incomplete_artifact:headline', 'bcg.forensics.incomplete_artifact:ibm_bullets', 'bcg.forensics.incomplete_artifact:ibm_narrative', 'bcg.forensics.incomplete_artifact:insurtech_bullets', 'bcg.forensics.incomplete_artifact:insurtech_narrative', 'bcg.forensics.incomplete_artifact:unify_bullets', 'bcg.forensics.incomplete_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:competencies', 'bcg.issue_tree.incomplete_forensic_artifact:unify_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:insurtech_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:ey_bullets', 'bcg.issue_tree.incomplete_forensic_artifact:unify_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:ibm_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:insurtech_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:ey_narrative', 'bcg.issue_tree.incomplete_forensic_artifact:executive_summary', 'bcg.issue_tree.incomplete_forensic_artifact:headline']}` |
| `mandatory_research_briefing_input_row0_locked` | `PASS` | `{'order': 0, 'section': 'research_briefing_input', 'generation_status': 'BRIEFING_PRESENT:RUN_SPECIFIC'}` |
| `mandatory_apps_research_row0_x1_x2_x3_gates_locked` | `PASS` | `{'research_source_class': 'FRESH_APPS_RESEARCH', 'x2': 'PASS', 'x3': 'X3D_ALLOW_FINISH; X1=PASS'}` |
| `mandatory_resume_docx_inline_json_present` | `FAIL` | `{'title': 'Resume DOCX Full Version Inline', 'text_chars': 636, 'current_run_authorized': False, 'blockers': ['outcome_authorized_false', 'final_resume_output_status=FAIL', 'failed_final_resume_gates=final_resume_no_gap_markers', 'x3_blocked=competencies,final_resume_aggregation', 'pre_run_blocked=unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline']}` |
| `E2E_FAIL_WITHOUT_SECTION_FORENSICS` | `FAIL` | `{'required': True, 'failed_section_count': 12, 'artifact_dir': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics', 'missing_or_incomplete': [{'section_id': 'competencies', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/competencies.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/competencies.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'independent_failure', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'unify_bullets', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_bullets.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ibm_bullets', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_bullets.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'insurtech_bullets', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_bullets.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ey_bullets', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_bullets.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_bullets.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'unify_narrative', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_narrative.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ibm_narrative', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_narrative.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'insurtech_narrative', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_narrative.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'ey_narrative', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_narrative.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_narrative.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'executive_summary', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/executive_summary.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/executive_summary.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'headline', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/headline.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/headline.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'upstream_cascade', 'baseline_confidence': 'pinned_baseline_unavailable'}, {'section_id': 'final_resume_aggregation', 'json_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/final_resume_aggregation.json', 'md_path': 'artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/final_resume_aggregation.md', 'complete': False, 'errors': ['invalid:comparison_incomplete'], 'failure_type': 'aggregation_downstream', 'baseline_confidence': 'pinned_baseline_unavailable'}]}` |
| `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` | `FAIL` | `-` |

## Section Counts

| Total | Real LLM | X3 allow | X3 block | Pre-run blocked | Not run | Unknown/other |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 1 | 0 | 1 | 10 | 0 | 1 |

## Section Lane Summary Table

| # | Section | Research source class | R1A | R1B | Lane record | Provider call attempted | Primary provider | Primary model observed | Pooling selector LLM | Secondary provider | Secondary model observed | Generation status | Judges run | Judge models / scores | Judge retry / fallback | <span style="display:inline-block; min-width:32ch">X2</span> | <span style="display:inline-block; min-width:32ch">X3</span> | <span style="display:inline-block; min-width:44ch">Past fail / blocker</span> | Display output | L6 evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `research_briefing_input` | `FRESH_APPS_RESEARCH` | `miss` | `skipped` | `YES` | `True` | `external_openai` | `gpt-5.4-mini-2026-03-17` | `N/A` | `N/A` | `N/A` | `BRIEFING_PRESENT:RUN_SPECIFIC` | `N/A` | `N/A` | `N/A` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PASS</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3D_ALLOW_FINISH; X1=PASS</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=a66f65e058d33c661b82c4a32a82decc78e83c4882059854079ea2017bfa7351;<br>ref=C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\apps_research\runs\r-80e758cb11db9efc0bed092e\briefing.md;<br>target=Unify Consulting / SVP Technical Pre-Sales, Enterprise Cloud &amp; AI Solutions; briefing_text_chars=5554</code></span> | `C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\apps_research\runs\r-80e758cb11db9efc0bed092e\briefing.md` | `N/A` |
| 1 | `competencies` | `N/A` | `miss` | `skipped` | `YES` | `True` | `external_claude` | `claude-sonnet-5` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `REAL_LLM` | `YES` | `Google Gemini 3.1 Pro Preview / gemini-3.1-pro-preview: 5 vs 4 PASS; OpenAI ChatGPT / gpt-5.5: 4.35 vs 4 PASS` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>FAIL</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_BLOCK</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.</code></span> | `artifacts/apps_rg/runtime_proofs/full_resume_c005cc5512d7/competencies_display.txt` | `future_run_advisory_only` |
| 2 | `unify_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:EXECUTED_X3A</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt&#124;missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 3 | `ibm_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'ibm_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 4 | `insurtech_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'insurtech_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 5 | `ey_bullets` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'ey_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 6 | `unify_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'unify_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 7 | `ibm_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'ibm_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 8 | `insurtech_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'insurtech_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 9 | `ey_narrative` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_openai_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'ey_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 10 | `executive_summary` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'executive_summary' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 11 | `headline` | `N/A` | `miss` | `skipped` | `YES` | `False` | `external_claude_section_lane` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>PRE_RUN:PHASE1_NO_RUN_DIR</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED&#124;missing_pointer:no resolvable run_dir pointer for lane 'headline' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections</code></span> | `MISSING` | `not_observed` |
| 12 | `final_resume_aggregation` | `N/A` | `miss` | `skipped` | `YES` | `NOT_OBSERVED` | `NOT_OBSERVED` | `NOT_OBSERVED` | `N/A` | `NOT_OBSERVED` | `NOT_OBSERVED` | `ASSEMBLED` | `NO` | `NOT_OBSERVED` | `NOT_OBSERVED` | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>UNKNOWN</code></span> | <span style="display:inline-block; min-width:32ch; white-space:normal"><code>X3_REVIEW_AGGREGATION</code></span> | <span style="display:inline-block; min-width:44ch; white-space:normal"><code>Final resume aggregation failure: full-resume coherence or product release gate did not pass.</code></span> | `modular_r4/final_resume_assembly/final_resume.json` | `not_observed` |

## Section Execution Ledger

| Section | Ran status | X3 | X2 | Product | Runtime | Failed gates | Display |
|---|---|---|---|---|---|---|---|
| `competencies` | `ran_real_llm` | `X3_BLOCK` | `FAIL` | `FAIL` | `REAL_LLM` | `x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding` | `artifacts/apps_rg/runtime_proofs/full_resume_c005cc5512d7/competencies_display.txt` |
| `unify_bullets` | `pre_run_blocked` | `PRE_RUN:EXECUTED_X3A` | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `-` | `-` |
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
| Canonical final resume JSON | `modular_r4/final_resume_assembly/final_resume.json` | `EXISTS_UNAUTHORIZED` | 1894241 | `15fc8eeda81d9f6ff57fe842f1ac00f4001cd3b2adf63494a96feb70c63cbd81` |
| Rendered final resume text | `FINAL_RESUME_OUTPUT.txt` | `EXISTS_UNAUTHORIZED` | 3406 | `9ee32564ce820352b2d84dc6141363716bef05af6b49c2bed707886c1077c2bb` |
| Final resume DOCX | `outputs/resume.docx` | `EXISTS_UNAUTHORIZED` | 38500 | `6bfc97346ab4293e4af1ebfe6f6efb92d9a45c3eae7614e138a470f7c33bb3e8` |

| Gate | Status | Observed |
|---|---|---|
| `final_resume_json_spine_present` | `PASS` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/modular_r4/final_resume_assembly/final_resume.json` |
| `final_resume_rendered_text_present` | `PASS` | `{'relpath': 'FINAL_RESUME_OUTPUT.txt', 'exists': True, 'bytes': 3406, 'sha256': '9ee32564ce820352b2d84dc6141363716bef05af6b49c2bed707886c1077c2bb'}` |
| `final_resume_docx_present_nonempty` | `PASS` | `{'relpath': 'outputs/resume.docx', 'exists': True, 'bytes': 38500, 'sha256': '6bfc97346ab4293e4af1ebfe6f6efb92d9a45c3eae7614e138a470f7c33bb3e8'}` |
| `final_resume_rendered_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 182, 'ENGINEERING & PLATFORM COMPETENCIES': 273, 'PROFESSIONAL EXPERIENCE': 1730, 'EDUCATION': 2913, 'CERTIFICATIONS': 3077}` |
| `final_resume_docx_order_valid` | `PASS` | `{'EXECUTIVE SUMMARY': 187, 'ENGINEERING & PLATFORM COMPETENCIES': 284, 'PROFESSIONAL EXPERIENCE': 1748, 'EDUCATION': 2945, 'CERTIFICATIONS': 3108}` |
| `final_resume_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [1755, 1812], 'ibm': [1942, 1956], 'insurtech': [2080, 2133], 'ey': [2260, 2286], 'early_career': [2406, 2471]}}` |
| `final_resume_docx_base_role_headers_preserved` | `PASS` | `{'role_headers': {'unify': ['Unify Consulting — SVP Engineering, Agentic AI Platforms', 'Boca Raton, FL \| Feb 2023 – Present'], 'ibm': ['IBM — Partner', 'Edgewater, NJ \| Apr 2017 – Oct 2022'], 'insurtech': ['InsurTech Cloud Solutions — Chief Technology Officer', 'New York, NY \| Apr 2014 – Mar 2017'], 'ey': ['Ernst & Young — Principal', 'New York, NY \| Oct 2009 – Mar 2014'], 'early_career': ['Early Career Roles — Actuarial Consultant and Quantitative Roles', 'Philadelphia, PA \| Oct 2002 – Sep 2009']}, 'positions': {'unify': [1772, 1829], 'ibm': [1959, 1973], 'insurtech': [2101, 2154], 'ey': [2287, 2313], 'early_career': [2439, 2504]}}` |
| `final_resume_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 2923, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 3008}}` |
| `final_resume_docx_education_copied_from_base` | `PASS` | `{'section_id': 'education', 'expected_lines': ['Master of Science in Biostatistics, Columbia University (Graduated with Distinction)', 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)'], 'positions': {'Master of Science in Biostatistics, Columbia University (Graduated with Distinction)': 2955, 'Bachelor of Arts in Biology, Brown University (Graduated Cum Laude)': 3040}}` |
| `final_resume_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 3106, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 3165, 'Certified Solutions Architect – Professional, AWS, 2023': 3219, 'Fellow of the Society of Actuaries, 2010': 3275}}` |
| `final_resume_docx_certifications_copied_from_base` | `PASS` | `{'section_id': 'certifications', 'expected_lines': ['Certified Machine Learning Engineer – Associate, AWS, 2025', 'Databricks Lakehouse Fundamentals Accreditation, 2023', 'Certified Solutions Architect – Professional, AWS, 2023', 'Fellow of the Society of Actuaries, 2010'], 'positions': {'Certified Machine Learning Engineer – Associate, AWS, 2025': 3137, 'Databricks Lakehouse Fundamentals Accreditation, 2023': 3196, 'Certified Solutions Architect – Professional, AWS, 2023': 3250, 'Fellow of the Society of Actuaries, 2010': 3306}}` |
| `final_resume_no_gap_markers` | `FAIL` | `{'not_completed': True, 'not_generated_by_run': False}` |

Final resume output failed gates: `final_resume_no_gap_markers`

## Judge Execution Ledger

| Section | Judge | Model | Status | Score | Threshold | Pass | Issues |
|---|---|---|---|---:|---:|---|---|
| `competencies` | `Google Gemini 3.1 Pro Preview` | `gemini-3.1-pro-preview` | `MODEL_BACKED_PASS` | 5 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
| `competencies` | `OpenAI ChatGPT` | `gpt-5.5` | `MODEL_BACKED_PASS` | 4.35 | 4 | `PASS` | `model_backed_pass_provider_keys=gemini_pro,openai_chatgpt` |
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

1. `competencies` - Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
   - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
   - Evidence: `x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding`
   - Causal allocation:
     - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
     - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
     - Allocation rows:
       - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: x2_competencies_graph_granularity_gates: missing_role_axes:co_sell observed={'category_count': 8, 'min_unique_leaf_skills_per_category': 1, 'categories_missing_leaf_skills': [], 'min_unique_source_facts_per_category': 1, 'categories_missing_source_facts': [], 'dominant_source_fact_id': 'reb_unify_agentic_platform_architecture', 'dominant_source_fact_category_share': 0.25, 'source_fact_concentration_threshold': 0.75, 'target_role_profile': 'ai_partnerships_gtm', 'required_role_axes': ['co_sell', 'gtm_enablement', 'hyperscaler_alliance', 'joint_solution', 'partner_architecture', 'partner_motions'], 'missing_role_axes': ['co_sell']} Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
       - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
       - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_competencies_graph_traversal_sufficiency, x2_competencies_graph_granularity_gates, x2_resume_graph_claim_binding`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
       - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
   - Required implementation plan:
     - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
     - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
     - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
     - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
2. `unify_bullets` - Pre-run dependency blocked execution: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt|missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:EXECUTED_X3A`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt|missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
3. `ibm_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
4. `insurtech_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
5. `ey_bullets` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
6. `unify_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'unify_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'unify_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
7. `ibm_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
8. `insurtech_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
9. `ey_narrative` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
10. `executive_summary` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'executive_summary' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'executive_summary' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
       - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
       - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
       - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
   - Required implementation plan:
     - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
     - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
     - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
     - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
11. `headline` - Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'headline' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections
   - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
   - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
   - Causal allocation:
     - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
     - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
     - Allocation rows:
       - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'headline' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
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
- Failed section count: `12`
- Artifact directory: `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics`
- Baseline confidence: `pinned_baseline_unavailable`

| Section | Failure type | Complete | Comparison | JSON | MD |
|---|---|---:|---:|---|---|
| `competencies` | `independent_failure` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/competencies.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/competencies.md` |
| `unify_bullets` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_bullets.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_bullets.md` |
| `ibm_bullets` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_bullets.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_bullets.md` |
| `insurtech_bullets` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_bullets.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_bullets.md` |
| `ey_bullets` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_bullets.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_bullets.md` |
| `unify_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_narrative.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/unify_narrative.md` |
| `ibm_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_narrative.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ibm_narrative.md` |
| `insurtech_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_narrative.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/insurtech_narrative.md` |
| `ey_narrative` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_narrative.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/ey_narrative.md` |
| `executive_summary` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/executive_summary.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/executive_summary.md` |
| `headline` | `upstream_cascade` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/headline.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/headline.md` |
| `final_resume_aggregation` | `aggregation_downstream` | `False` | `False` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/final_resume_aggregation.json` | `artifacts/apps_rg/runs/s2u0_r1/e2e_20260721T010017Z_65f533a8/section_failure_forensics/final_resume_aggregation.md` |

## L6 Shadow Observability

| Section | L6 files | Authority |
|---|---:|---|
| `competencies` | 18 | `future_run_advisory_only` |
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
run_root=C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8
status=BLOCKED
reason=outcome_authorized_false; final_resume_output_status=FAIL; failed_final_resume_gates=final_resume_no_gap_markers; x3_blocked=competencies,final_resume_aggregation; pre_run_blocked=unify_bullets,ibm_bullets,insurtech_bullets,ey_bullets,unify_narrative,ibm_narrative,insurtech_narrative,ey_narrative,executive_summary,headline
policy=do_not_inline_FINAL_RESUME_OUTPUT_txt_unless_current_run_authorized
```
