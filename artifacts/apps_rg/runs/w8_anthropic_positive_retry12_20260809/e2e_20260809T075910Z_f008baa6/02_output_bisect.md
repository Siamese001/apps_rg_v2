# apps_rg Output Bisect

## Section: unify_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `32ccc9d9d51aea8d167bfe15` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `2758f9645d7222ad9b8ff735` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `25719b1801b93eb601559c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `3feb2efc26779324a23818a2` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `4b45fe2cc82f4a93975dbee7` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `aa619e3f962e7ed65323ecc4` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `7e736bb6130198a1716794b0` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK_FINAL_MATERIALI` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `bcfb430189cc535b` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x1d_gemini_provider_response_raw_20260809_080237_994.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `e87010e60300fb5e` | Employment pool selector: 6 slots, min_score=0.74, threshold=0.72, gate_ok=True | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `0.74/0.72 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x1d_openai_provider_response_raw_20260809_080224_786.json` |
| 5 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\judge_remediation_cycles.json` |
| 6 | `x3_disposition` | `-` | `0cc3f4363788741a` | REAL_LLM output, X2 pass, all X1D judges model-backed pass, product quality PASS. | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 6} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '0010fe378c3c44178bee87bd7b04d0ee3125d5612ff9788e8607b75a3c43693c', 'fec_allowed_fact_ids_digest': '0010fe378c3c44178bee87bd7b04d0ee3125d5612ff9788e8607b75a3c43693c', 'fec_narrowed_from_pool': True} |
| `x2_base_resume_ngram_overlap_unify` | `NOT_OBSERVED` | `PASS` | `True` | all_below_threshold |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_bullet_seniority_floor` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_bullet_technical_specificity_floor` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | Every bul_unify_* bullet must appear in output and claim_ledger. |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 16, 'violations': []} |
| `x2_e0_example_ngram_overlap_unify` | `NOT_OBSERVED` | `PASS` | `True` | all_below_threshold |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 61, 'violations': []} |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_metric_fact_id_granularity` | `NOT_OBSERVED` | `PASS` | `True` | Metric claims lack granular source_fact_ids. |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | Em dash found. |
| `x2_no_ey_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | EY fact leakage detected. |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | First-person pronoun found. |
| `x2_no_generic_consulting_substitution` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_no_generic_filler` | `NOT_OBSERVED` | `PASS` | `True` | Generic filler phrase found. |
| `x2_no_ibm_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | IBM fact leakage detected. |
| `x2_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | Inline source tags found in bullet text. |
| `x2_no_insurtech_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | InsurTech fact leakage detected. |
| `x2_no_jd_only_claims` | `NOT_OBSERVED` | `PASS` | `True` | JD phrase copied into bullet proof. |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | Silent mock fallback detected. |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 61, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider requested does not match attempted. |
| `x2_required_top_level_json_keys` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_text_claim_coverage_integrity` | `NOT_OBSERVED` | `PASS` | `True` | structural_alignment_ok |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_unify_at_most_one_mechanism_dense_bullet` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_unify_augmented_skills_graph_proof_pool_only` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_unify_bullet_count_6` | `NOT_OBSERVED` | `PASS` | `True` | Must output exactly 6 bullets. |
| `x2_unify_bullet_graph_skill_node_ids_required` | `NOT_OBSERVED` | `PASS` | `True` | all_present |
| `x2_unify_bullet_no_embedded_newline` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_unify_bullet_no_paragraph_block` | `NOT_OBSERVED` | `PASS` | `True` | <=320 chars |
| `x2_unify_bullet_single_thought` | `NOT_OBSERVED` | `PASS` | `True` | 1 sentence each |
| `x2_unify_bullets_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'unify_bullets', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'f9e12caa4ea2cc88e445489e1894889f2419d03148d6960102ec5ac335606b11', 'canonical_evidence_set_digest': 'f9e12caa4ea2cc88e445489e1894889f2419d03148d6960102ec5ac335606b11', 'id_alias_map': {'bul_unify_001': 'fact_engineering_platform_001', 'bul_unify_002': 'exp_unify_001', 'bul_unify_003': 'fact_engineering_platform_003', 'bul_unify_004': 'fact_engineering_platform_004', 'bul_unify_005': 'fact_engineering_platform_002', 'bul_unify_006': 'fact_engineering_platform_006'}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 61, 'source_fact_ids_checked': ['bul_unify_001', 'fact_engineering_platform_001', 'bul_unify_001_metric_a50f35f7', 'bul_unify_002', 'exp_unify_001', 'bul_unify_003', 'fact_engineering_platform_003', 'bul_unify_003_metric_d667f2d7', 'bul_unify_004', 'fact_engineering_platform_004', 'bul_unify_004_metric_ca90d7a2', 'bul_unify_005', 'fact_engineering_platform_002', 'bul_unify_006', 'fact_engineering_platform_006', 'bul_unify_006_metric_943d2c1c'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 61, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'unify_bullets'} |
| `x2_unify_each_bullet_approved_metric_outcome_lineage` | `NOT_OBSERVED` | `PASS` | `True` | {'missing_metric_outcome_ids': [], 'unapproved_metric_outcome_ids': [], 'slot_metric_allowlist': {'bul_unify_001': ['metric_unify_agentic_graphrag_context_pack_grounding_surface', 'metric_unify_agentic_human_override_escalation_surface', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_multi_agent_orchestration_contract_surface', 'metric_unify_agentic_replay_key_audit_manifest_surface', 'metric_unify_agentic_runtime_gate_verdict_contract_surface', 'metric_unify_agentic_runtime_proof_bundle_lineage_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'metric_unify_replayable_runtime_traceability'], 'bul_unify_002': ['metric_unify_cfo_aligned_adoption_motion_count', 'metric_unify_consumption_renewal_signal_instrumentation'], 'bul_unify_003': ['metric_unify_audit_grade_runtime_observability_coverage', 'metric_unify_eval_telemetry_rollback_control_set'], 'bul_unify_004': ['metric_unify_cycle_six_months_to_three_weeks', 'metric_unify_production_readiness_gate_set'], 'bul_unify_005': ['metric_unify_cloud_data_runtime_integration_patterns', 'metric_unify_high_availability_distributed_service_patterns'], 'bul_unify_006': ['metric_unify_20pct_gross_margin_expansion', 'metric_unify_22m_ip_led_revenue', 'metric_unify_team_scaled_8_to_28']}} |
| `x2_unify_each_bullet_metric_outcome_surface_visible` | `NOT_OBSERVED` | `PASS` | `True` | {'visible_matches': {'bul_unify_001': [{'metric_outcome_id': 'metric_unify_policy_gated_agent_execution_surface', 'token': 'policy-gated agent execution surface for governed enterprise AI workflows'}], 'bul_unify_002': [{'metric_outcome_id': 'metric_unify_cfo_aligned_adoption_motion_count', 'token': 'CFO-aligned adoption motions'}], 'bul_unify_003': [{'metric_outcome_id': 'metric_unify_audit_grade_runtime_observability_coverage', 'token': 'audit-grade observability'}], 'bul_unify_004': [{'metric_outcome_id': 'metric_unify_production_readiness_gate_set', 'token': 'production-readiness gates'}], 'bul_unify_005': [{'metric_outcome_id': 'metric_unify_high_availability_distributed_service_patterns', 'token': 'high-availability distributed service patterns for enterprise AI platforms'}], 'bul_unify_006': [{'metric_outcome_id': 'metric_unify_team_scaled_8_to_28', 'token': 'engineering team from 8 to 28'}]}, 'missing_visible_metric_surface': []} |
| `x2_unify_graph_granularity_gates` | `NOT_OBSERVED` | `PASS` | `True` | {'role_specific_axis_coverage': {'required_axes': ['agentic_platform_architecture', 'enterprise_adoption_revenue', 'runtime_reliability_governance', 'production_adoption_lifecycle', 'distributed_ecosystem_engineering', 'platform_commercialization_leadership'], 'selected_axes': ['agentic_platform_architecture', 'enterprise_adoption_revenue', 'runtime_reliability_governance', 'production_adoption_lifecycle', 'distributed_ecosystem_engineering', 'platform_commercialization_leadership'], 'missing_axes': []}, 'frontier_size_by_hop_depth': {'hop_0_role_episode_roots': 6, 'hop_1_graph_skill_nodes': 31, 'hop_2_metric_outcome_nodes': 21, 'rejected_hop_0_sibling_roots': 2, 'rejected_hop_1_sibling_skill_nodes': 8, 'rejected_hop_2_sibling_metric_nodes': 4}} |
| `x2_unify_graph_only_no_base_resume_bullets` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_unify_graph_traversal_sufficiency` | `NOT_OBSERVED` | `PASS` | `True` | {'candidate_conservation': {'eligible_role_episode_root_count': 8, 'selected_role_episode_root_count': 6, 'rejected_role_episode_root_count': 2, 'unexplained_selected_role_episode_bundle_ids': [], 'pass': True}, 'selected_role_episode_root_count': 6, 'selected_unique_leaf_skill_count': 31, 'selected_unique_metric_count': 21, 'rejected_sibling_skill_count': 8, 'rejected_sibling_metric_count': 4} |
| `x2_unify_metric_anchor_bullet_ownership` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_metric_outcomes_distributed_by_slot` | `NOT_OBSERVED` | `PASS` | `True` | {'unique_visible_metric_outcome_ids': ['metric_unify_audit_grade_runtime_observability_coverage', 'metric_unify_cfo_aligned_adoption_motion_count', 'metric_unify_high_availability_distributed_service_patterns', 'metric_unify_policy_gated_agent_execution_surface', 'metric_unify_production_readiness_gate_set', 'metric_unify_team_scaled_8_to_28'], 'expected_metric_slots': 6} |
| `x2_unify_metric_source_required` | `NOT_OBSERVED` | `PASS` | `True` | all_traceable |
| `x2_unify_metrics_preserved` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_no_archive_claim_verbatim` | `NOT_OBSERVED` | `PASS` | `True` | Bullet copies archive claim_text run:  |
| `x2_unify_no_rewrite_intensity_model` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_unify_not_legacy_six_pack_allocation` | `NOT_OBSERVED` | `PASS` | `True` | Proof pool reverted to legacy sorted six-pack ledger order. |
| `x2_unify_only_fact_scope` | `NOT_OBSERVED` | `PASS` | `True` | ['bul_unify_001', 'bul_unify_001_metric_a50f35f7', 'bul_unify_002', 'bul_unify_003', 'bul_unify_003_metric_d667f2d7', 'bul_unify_004', 'bul_unify_004_metric_ca90d7a2', 'bul_unify_005', 'bul_unify_006', 'bul_unify_006_metric_943d2c1c', 'exp_unify_001', 'fact_engineering_platform_001', 'fact_engineering_platform_002', 'fact_engineering_platform_003', 'fact_engineering_platform_004', 'fact_engineering_platform_006'] |
| `x2_unify_protected_bullet_metrics_preserved` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_track_ranked_selection_method` | `NOT_OBSERVED` | `PASS` | `True` | selected_fact_plan must use graph track-ranked allocation (not company_hint / hydrate). |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges with invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `0.74/0.72 PASS` | - |

## Section: unify_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `32ccc9d9d51aea8d167bfe15` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `2758f9645d7222ad9b8ff735` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\unify_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: ibm_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `32ccc9d9d51aea8d167bfe15` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `2758f9645d7222ad9b8ff735` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `25719b1801b93eb601559c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `1a48b5c85feeee895f3149e4` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `6d2fd9f59853cf6a9588e0af` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `80322318fefcce4a7e085f49` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `45ad40457e16eea9091b4ba6` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `adfd306d67c6bf3d` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x1d_gemini_provider_response_raw_20260809_080525_623.json` |
| 4 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\judge_remediation_cycles.json` |
| 5 | `x3_disposition` | `-` | `0b37cb2461bd4eb9` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\ibm_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 5} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '3523ffe92353bae4fde5307d66db54ccd236efd7ec3835517500955e8766a719', 'fec_allowed_fact_ids_digest': '3523ffe92353bae4fde5307d66db54ccd236efd7ec3835517500955e8766a719', 'fec_narrowed_from_pool': True} |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | all_rows_non_empty |
| `x2_claim_ledger_source_fact_ids_allow_list` | `NOT_OBSERVED` | `PASS` | `True` | all_tokens_in_allowed_fact_ids |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 2, 'violations': []} |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 33, 'violations': []} |
| `x2_ibm_narrative_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'ibm_narrative', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '21d43a91181a06c45824b349e5adeccaf970c5011cd8877a1be6e194e55c3cd1', 'canonical_evidence_set_digest': '21d43a91181a06c45824b349e5adeccaf970c5011cd8877a1be6e194e55c3cd1', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 36, 'source_fact_ids_checked': ['bul_ibm_001', 'bul_ibm_002'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 36, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'ibm_narrative'} |
| `x2_ibm_narrative_bullet_overlap_threshold` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_claim_ledger_clause_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | {'reason': 'ok', 'ledger_rows': 2} |
| `x2_ibm_narrative_claim_theme_coverage` | `NOT_OBSERVED` | `FAIL` | `True` | narrative_sentence material themes require matching bul_ibm_* in claim_ledger union; missing: ['unsupported_companion_theme:ecosystem', 'unsupported_companion_theme:ecosystems', 'unsupported_companion_theme:regulated_financial'] |
| `x2_ibm_narrative_exactly_one_sentence` | `NOT_OBSERVED` | `PASS` | `True` | Must be exactly one sentence. |
| `x2_ibm_narrative_exactly_one_sentence_mechanical` | `NOT_OBSERVED` | `PASS` | `True` | single sentence required |
| `x2_ibm_narrative_forbidden_opener` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_hold_metric_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_ibm_only_fact_scope` | `NOT_OBSERVED` | `PASS` | `True` | Non-IBM fact scope in payload. |
| `x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets` | `NOT_OBSERVED` | `FAIL` | `True` | Narrative mechanism is absent from cited finalized IBM bullets: bi |
| `x2_ibm_narrative_metric_cap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ibm_narrative_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | Candidate name must not appear in the role narrative sentence. |
| `x2_ibm_narrative_no_meta_disclaimer_in_display` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_requires_finalized_bullets` | `NOT_OBSERVED` | `PASS` | `True` | IBM narrative must run after ACCEPTED_FINALIZED IBM bullets when companion-aware. |
| `x2_ibm_narrative_role_episode_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | {'change_log_bundle_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_presales_solution_engineering', 'reb_ibm_data_modeling_bi_decision_support', 'reb_ibm_revenue_sales_target_execution'], 'pool_bundle_ids': ['reb_ibm_aws_modernization_architecture', 'reb_ibm_cognitive_business_decision_support', 'reb_ibm_presales_solution_engineering', 'reb_ibm_offering_accelerator_management', 'reb_ibm_revenue_sales_target_execution', 'reb_ibm_nlp_ml_decision_support']} |
| `x2_ibm_narrative_role_episode_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'flat_skill_only': False} |
| `x2_ibm_narrative_source_supported` | `NOT_OBSERVED` | `PASS` | `True` | claim_ledger must map to IBM bullet facts only. |
| `x2_ibm_narrative_weak_resume_jargon_phrases` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_word_budget` | `NOT_OBSERVED` | `PASS` | `True` | {'word_count': 34, 'char_len': 304} |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 2, 'claims_supported_by_selected_resume_facts': 2, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 2, 'claims_supported_by_selected_resume_facts': 2, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_base_prose_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_no_consulting_language` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_narrative_not_bullet_recap` | `NOT_OBSERVED` | `PASS` | `True` | {'max_5gram_overlap': 0.0, 'est_shared_ngrams': 0} |
| `x2_narrative_seniority_floor` | `NOT_OBSERVED` | `PASS` | `True` | {'strong_verbs': ['championed'], 'authority': ['regulated', 'architecture', 'enterprise'], 'issues': []} |
| `x2_narrative_technical_specificity_floor` | `NOT_OBSERVED` | `PASS` | `True` | ['bi', 'pipeline', 'aws'] |
| `x2_narrative_upstream_graph_proof_required` | `NOT_OBSERVED` | `PASS` | `True` | Upstream gate 'x2_bullet_graph_skill_node_ids_required' did not pass. Narrative proof authority depends on bullet graph_skill_node_ids being validated. Resolve bullet X2 gates before promoting narrative to HARD FAIL. |
| `x2_no_bullet_sentence_structure_copy` | `NOT_OBSERVED` | `PASS` | `True` | Narrative copies a bullet-leading phrase. |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | Em dash found. |
| `x2_no_ey_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | EY leakage. |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | First person in narrative. |
| `x2_no_five_bullet_roll_up_tone` | `NOT_OBSERVED` | `PASS` | `True` | Reads like stacked bullet summary. |
| `x2_no_generic_filler` | `NOT_OBSERVED` | `PASS` | `True` | Generic filler. |
| `x2_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | Inline source tags in narrative. |
| `x2_no_insurtech_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | InsurTech leakage. |
| `x2_no_jd_only_claims` | `NOT_OBSERVED` | `PASS` | `True` | JD phrase copied as proof. |
| `x2_no_metric_repetition_unless_justified` | `NOT_OBSERVED` | `PASS` | `True` | no companion IBM bullets artifact |
| `x2_no_mock_or_plumbing_language_in_real_l2_output` | `NOT_OBSERVED` | `PASS` | `True` | no_stale_mock_terms_detected |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | Silent mock fallback detected. |
| `x2_no_unify_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | Unify bullet fact leakage detected. |
| `x2_no_unify_runtime_terms` | `NOT_OBSERVED` | `PASS` | `True` | Unify runtime vocabulary leaked into IBM narrative. |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 33, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider mismatch. |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '84524aee2b0cbd5d7fde829eabf7fce2e051089bb1526e99fecaf391eb1af3df', 'claim_count': 2, 'bound_claim_count': 2, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 2, 'claims_supported_by_selected_resume_facts': 2, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |

## Section: executive_summary

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\apps_research\runs\r-d0838e0df8682e94b58fb932\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 4.2/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `deterministic_finalization` - Current deterministic finalization changed the published text before full X2 evaluation.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `first_observed_divergence_root_cause` / `NOT_CAUSALLY_ISOLATED`: U0 ingested a different briefing source and the downstream targeting, proof-selection, provider-request, and initial-candidate evidence changed. Without a controlled replay, those upstream changes explain where divergence began but do not prove one sole cause.
- `recovery_failure_root_cause` / `ISOLATED`: Both pre-judge retries were only monotonic improvements: each retained the fact-conflation defect, the retry budget ended, and retry_provider_for_synthesis reverted to the first candidate.
  - Code surface: `apps_rg/runtime/sections/executive_summary_lane.py::retry_provider_for_synthesis`
- `final_gate_root_cause` / `ISOLATED`: Deterministic required-fact finalization changed the published text before X2; the final fragment and fact-conflation checks then blocked judge dispatch.
  - Code surface: `apps_rg/runtime/sections/executive_summary_voice_repair.py::ensure_required_allowed_fact_utilization`

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `32ccc9d9d51aea8d167bfe15` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `2758f9645d7222ad9b8ff735` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `25719b1801b93eb601559c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `79ea2cdeae815e7d6417ebae` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `534e5a12e3731ef8735283f0` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `49afbb96749d86638c5fcba0` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `5348f5797931318505ea44f0` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `998970c7c25d7c1c91f05132` | `False` | `CAUSAL` | Current deterministic finalization changed the published text before full X2 evaluation. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `09833e282e3f42fa1f6f1ebd` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `c69a9c559e1a3f894ce6a432` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `initial_generation` | `0` | `5348f57979313185` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | sentence_5_source_fact_ids_compacted_to_3 | repair_exec_summary_cross_fact_conflation_row | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_repair_ledger.json` |
| 3 | `deterministic_repair` | `2` | `-` | claim_5_metric_20_PERCENT_not_reserved_by:executive_summary:claim:03 | repair_exec_summary_unallocated_metric_row | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_repair_ledger.json` |
| 4 | `deterministic_repair` | `3` | `-` | judge_remediation | judge_remediation_regen | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\section_repair_ledger.json` |
| 5 | `final_x2` | `2` | `f1021808cab1e57f` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 6 | `judge_panel` | `gemini_pro` | `47ab219b37236068` | Sentence 5 repeats the IBM-AWS alliance co-sell claim already established in sentence 2.; Deterministic gate x2_exec_summary_judge_packet_display_override_parity indicated a display override parity gap for fact_engineering_platform_002. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.2/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x1d_gemini_provider_response_raw_20260809_080802_841.json` |
| 7 | `judge_panel` | `openai_chatgpt` | `47ab219b37236068` | Judge packet omits the display override for fact_engineering_platform_002, preventing independent parity review of S3. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.6/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x1d_openai_provider_response_raw_20260809_080820_829.json` |
| 8 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\judge_remediation_cycles.json` |
| 9 | `x3_disposition` | `-` | `f1021808cab1e57f` | Product quality is FAIL. | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\sections\executive_summary\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_PROVIDER_MODEL_provider_stub_transport_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'fc8c8bdeba5b601d02182ad66fa01ee10ac09c2575f6df482181b9b1868366ae', 'fec_allowed_fact_ids_digest': 'fc8c8bdeba5b601d02182ad66fa01ee10ac09c2575f6df482181b9b1868366ae', 'fec_narrowed_from_pool': True} |
| `x2_briefing_as_proof_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': [], 'material_delivered_to_l2': True, 'parity_match_generation_judge': True} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_coverage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_claim_field_maps_to_display_sentence` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | all_rows_non_empty |
| `x2_claim_ledger_materialized_or_gap_excused` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_orphan_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | 6 |
| `x2_claim_ledger_row_count_matches_sentence_count` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 9, 'violations': []} |
| `x2_em_dash_count_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_exec_summary_allowed_fact_utilization` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_colon_stitch_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_cross_fact_conflation_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_cross_sentence_metric_dedup` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_display_override_compliance` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_display_roundtrip_integrity` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_evidence_utilization` | `NOT_OBSERVED` | `PASS` | `True` | ok_pool_below_utilization_threshold |
| `x2_exec_summary_jd_alignment_proof_flags` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_context_used_as_proof': False, 'companion_used_as_proof': False, 'graph_targeting': {'role_family_key': 'PARTNER_APPLIED_AI_ARCHITECTURE', 'projection_source': 'sqlite_role_family_projection', 'sqlite_projection_row_found': True, 'fallback_pillar_bridge_used': False, 'release_eligible_targeting_proof': True, 'targeting_degraded_explicit': False, 'pillar_hint_ids': ['pillar_applied_ai_partner_architecture', 'pillar_partner_gtm_alliances', 'pillar_presales_solutioning', 'pillar_technical_presales_accelerators'], 'briefing_targeting_supplement': []}} |
| `x2_exec_summary_mechanical_opener_stack_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_meta_filler_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_bloated_sentence` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_certifications_section_duplication` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_competencies_duplication` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_credential_dump` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_mechanism_inventory` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_sentence_fragment` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_paragraph_max_words` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_prompt_template_authority` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_robotic_transition_stack_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_sentence_count_6` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_strategy_no_commercialization_thread` | `NOT_OBSERVED` | `PASS` | `True` | skipped_not_strategy_lane |
| `x2_executive_summary_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'executive_summary', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'f08809fc8a28b4644155a3c9e22d80bdcb9f5f76d3f9725fae1e92a8dd77f369', 'canonical_evidence_set_digest': 'f08809fc8a28b4644155a3c9e22d80bdcb9f5f76d3f9725fae1e92a8dd77f369', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 18, 'source_fact_ids_checked': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_unify_platform_commercialization_leadership', 'skill_partner_alliance_gtm_execution', 'skill_partner_hyperscaler_cosell', 'fact_engineering_platform_002', 'reb_ibm_devsecops_release_resilience', 'skill_ibm_devsecops_pipeline_security', 'fact_partnerships_gtm_002', 'skill_agentic_platform_productization'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 18, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'executive_summary'} |
| `x2_executive_summary_synthesis_quality` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 18, 'violations': []} |
| `x2_first_person_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_generic_filler_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_inline_source_tags_absent` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_input_output_hashes_present` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_as_proof_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_jd_phrase_copy_violation_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_material_clause_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_metric_fact_id_granularity` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_mixed_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_model_name_allowed` | `NOT_OBSERVED` | `PASS` | `True` | skipped_provider_not_external_claude |
| `x2_no_extra_unrecognized_fields` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_inferred_bridge_claims` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_monolithic_prompt` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_selected_fact_plan_model_echo` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | provider=external_openai, status=REAL_LLM |
| `x2_north_star_style_echo_unsupported_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_overbroad_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 18, 'violations': []} |
| `x2_prompt_hash_known` | `NOT_OBSERVED` | `PASS` | `True` | 6be369a83ed59479 |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | requested=external_openai, attempted=external_openai |
| `x2_required_artifacts_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_required_fields_complete` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '84524aee2b0cbd5d7fde829eabf7fce2e051089bb1526e99fecaf391eb1af3df', 'claim_count': 6, 'bound_claim_count': 6, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
| `x2_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 6, 'claims_supported_by_selected_resume_facts': 6, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_self_check_claim_ledger_consistent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_sentence_coverage_pass` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_sentence_coverage_present` | `NOT_OBSERVED` | `PASS` | `True` | 6 |
| `x2_sentence_stacking_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_source_fact_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | 100% |
| `x2_source_sensitive_phrases_supported` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_target_company_as_experience_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_target_title_inflation_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_temperature_in_profile` | `NOT_OBSERVED` | `PASS` | `True` | 0.45 |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_unsupported_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_unsupported_industry_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_judge_packet_hash_uniform` | `NOT_OBSERVED` | `PASS` | `True` | ['47ab219b37236068'] |
| `x2_x1d_raw_responses_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `4.2/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `4.6/4.0 PASS` | - |

## Section: final_resume_aggregation

### Layperson RCA

The prior passing revision authorized final assembly because every required section, including the executive summary, had already cleared its product checks.

The current final assembly did not fail as an independent writing attempt; it was blocked downstream because the executive summary never became eligible for assembly.

No aggregation retry or aggregation judge could repair that upstream section failure, so the underlying executive-summary retry and X2 evidence remains the controlling root cause.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `upstream_section_authorization` - Final assembly was blocked because the executive summary never reached product authorization.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `32ccc9d9d51aea8d167bfe15` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `2758f9645d7222ad9b8ff735` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry12_20260809\e2e_20260809T075910Z_f008baa6\modular_r4\final_resume_assembly\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
