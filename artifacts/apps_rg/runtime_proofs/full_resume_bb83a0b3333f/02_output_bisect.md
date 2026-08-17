# apps_rg Output Bisect

## Section: unify_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_bullet_seniority_floor), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `6356b6c3ace7ebaf4fb0b950` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `fd02a3bfa4c7030366915940` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `4d45accc9442371277e957bd` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `fb6535f316fd5084bda14ae3` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `7aa18bc9047543fa7047aa02` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `d0ea77f96a4800775643ea2f` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `c4da1a503434ccaefa6e4e4b` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `3c830301563c4eb3a198addb` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `038fef72954454cd` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x1d_gemini_provider_response_raw_20260817_025239_088.json` |
| 4 | `judge_panel` | `anthropic_claude` | `1ca467ab6714874a` | Employment pool selector: 6 slots, min_score=0.74, threshold=0.72, gate_ok=True | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `0.74/0.72 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x1d_anthropic_claude_provider_response_raw_20260817_025230_155.json` |
| 5 | `judge_panel` | `gemini_pro` | `038fef72954454cd` | bul_unify_006 omits protected commercial metrics ($22M ARR / margin). | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `3.0/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x1d_gemini_provider_response_raw_20260817_025251_243.json` |
| 6 | `x3_disposition` | `-` | `666309aa5b080559` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 6} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '3768363a68da448460d49269cb4eee326b2213813a79c75749acb4a20f7206e8', 'fec_allowed_fact_ids_digest': '3768363a68da448460d49269cb4eee326b2213813a79c75749acb4a20f7206e8', 'fec_narrowed_from_pool': True} |
| `x2_base_resume_ngram_overlap_unify` | `NOT_OBSERVED` | `PASS` | `True` | bul_unify_004: 52.63% 4-gram overlap with base resume (threshold 25%) |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_bullet_seniority_floor` | `NOT_OBSERVED` | `FAIL` | `True` | bul_unify_006: seniority score 0 < floor 1 (signals=[]) |
| `x2_bullet_technical_specificity_floor` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | Every bul_unify_* bullet must appear in output and claim_ledger. |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 12, 'violations': []} |
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
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '86b518ae7a25da010c2bb8999c5fd5936c1090c9f703aa825124188c8937dfda', 'claim_count': 6, 'bound_claim_count': 6, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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
| `x2_unify_bullets_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'unify_bullets', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'c54c8001cea3864e28107344b16b58bb6f6dd3230c3b9128f7e4916c20300645', 'canonical_evidence_set_digest': 'c54c8001cea3864e28107344b16b58bb6f6dd3230c3b9128f7e4916c20300645', 'id_alias_map': {'bul_unify_001': 'fact_engineering_platform_001', 'bul_unify_002': 'exp_unify_001', 'bul_unify_003': 'fact_engineering_platform_003', 'bul_unify_004': 'fact_engineering_platform_004', 'bul_unify_005': 'fact_engineering_platform_002', 'bul_unify_006': 'fact_engineering_platform_006'}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 61, 'source_fact_ids_checked': ['fact_engineering_platform_001', 'bul_unify_001', 'exp_unify_001', 'bul_unify_002', 'fact_engineering_platform_003', 'bul_unify_003', 'fact_engineering_platform_004', 'bul_unify_004', 'fact_engineering_platform_002', 'bul_unify_005', 'fact_engineering_platform_006', 'bul_unify_006'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 61, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'unify_bullets'} |
| `x2_unify_each_bullet_approved_metric_outcome_lineage` | `NOT_OBSERVED` | `PASS` | `True` | {'missing_metric_outcome_ids': [], 'unapproved_metric_outcome_ids': [], 'slot_metric_allowlist': {'bul_unify_001': ['metric_unify_agentic_graphrag_context_pack_grounding_surface', 'metric_unify_agentic_human_override_escalation_surface', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_multi_agent_orchestration_contract_surface', 'metric_unify_agentic_replay_key_audit_manifest_surface', 'metric_unify_agentic_runtime_gate_verdict_contract_surface', 'metric_unify_agentic_runtime_proof_bundle_lineage_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'metric_unify_replayable_runtime_traceability'], 'bul_unify_002': ['metric_unify_cfo_aligned_adoption_motion_count', 'metric_unify_consumption_renewal_signal_instrumentation'], 'bul_unify_003': ['metric_unify_audit_grade_runtime_observability_coverage', 'metric_unify_eval_telemetry_rollback_control_set'], 'bul_unify_004': ['metric_unify_cycle_six_months_to_three_weeks', 'metric_unify_production_readiness_gate_set'], 'bul_unify_005': ['metric_unify_cloud_data_runtime_integration_patterns', 'metric_unify_high_availability_distributed_service_patterns'], 'bul_unify_006': ['metric_unify_20pct_gross_margin_expansion', 'metric_unify_22m_ip_led_revenue', 'metric_unify_team_scaled_8_to_28']}} |
| `x2_unify_each_bullet_metric_outcome_surface_visible` | `NOT_OBSERVED` | `PASS` | `True` | {'visible_matches': {'bul_unify_001': [{'metric_outcome_id': 'metric_unify_policy_gated_agent_execution_surface', 'token': 'agent execution surface'}], 'bul_unify_002': [{'metric_outcome_id': 'metric_unify_cfo_aligned_adoption_motion_count', 'token': 'CFO-aligned enterprise adoption motions tied to reusable AI platform commercialization'}], 'bul_unify_003': [{'metric_outcome_id': 'metric_unify_audit_grade_runtime_observability_coverage', 'token': 'audit-grade runtime observability coverage for regulated AI workflows'}], 'bul_unify_004': [{'metric_outcome_id': 'metric_unify_cycle_six_months_to_three_weeks', 'token': 'six months to three weeks'}], 'bul_unify_005': [{'metric_outcome_id': 'metric_unify_cloud_data_runtime_integration_patterns', 'token': 'vector services'}], 'bul_unify_006': [{'metric_outcome_id': 'metric_unify_team_scaled_8_to_28', 'token': 'engineering team from 8 to 28'}]}, 'missing_visible_metric_surface': []} |
| `x2_unify_graph_granularity_gates` | `NOT_OBSERVED` | `PASS` | `True` | {'role_specific_axis_coverage': {'required_axes': ['agentic_platform_architecture', 'enterprise_adoption_revenue', 'runtime_reliability_governance', 'production_adoption_lifecycle', 'distributed_ecosystem_engineering', 'platform_commercialization_leadership'], 'selected_axes': ['agentic_platform_architecture', 'enterprise_adoption_revenue', 'runtime_reliability_governance', 'production_adoption_lifecycle', 'distributed_ecosystem_engineering', 'platform_commercialization_leadership'], 'missing_axes': []}, 'frontier_size_by_hop_depth': {'hop_0_role_episode_roots': 6, 'hop_1_graph_skill_nodes': 31, 'hop_2_metric_outcome_nodes': 21, 'rejected_hop_0_sibling_roots': 2, 'rejected_hop_1_sibling_skill_nodes': 8, 'rejected_hop_2_sibling_metric_nodes': 4}} |
| `x2_unify_graph_only_no_base_resume_bullets` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_unify_graph_traversal_sufficiency` | `NOT_OBSERVED` | `PASS` | `True` | {'candidate_conservation': {'eligible_role_episode_root_count': 8, 'selected_role_episode_root_count': 6, 'rejected_role_episode_root_count': 2, 'unexplained_selected_role_episode_bundle_ids': [], 'pass': True}, 'selected_role_episode_root_count': 6, 'selected_unique_leaf_skill_count': 31, 'selected_unique_metric_count': 21, 'rejected_sibling_skill_count': 8, 'rejected_sibling_metric_count': 4} |
| `x2_unify_metric_anchor_bullet_ownership` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_metric_outcomes_distributed_by_slot` | `NOT_OBSERVED` | `PASS` | `True` | {'unique_visible_metric_outcome_ids': ['metric_unify_audit_grade_runtime_observability_coverage', 'metric_unify_cfo_aligned_adoption_motion_count', 'metric_unify_cloud_data_runtime_integration_patterns', 'metric_unify_cycle_six_months_to_three_weeks', 'metric_unify_policy_gated_agent_execution_surface', 'metric_unify_team_scaled_8_to_28'], 'expected_metric_slots': 6} |
| `x2_unify_metric_source_required` | `NOT_OBSERVED` | `PASS` | `True` | all_traceable |
| `x2_unify_metrics_preserved` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_no_archive_claim_verbatim` | `NOT_OBSERVED` | `PASS` | `True` | Bullet copies archive claim_text run:  |
| `x2_unify_no_rewrite_intensity_model` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_unify_not_legacy_six_pack_allocation` | `NOT_OBSERVED` | `PASS` | `True` | Proof pool reverted to legacy sorted six-pack ledger order. |
| `x2_unify_only_fact_scope` | `NOT_OBSERVED` | `PASS` | `True` | ['bul_unify_001', 'bul_unify_002', 'bul_unify_003', 'bul_unify_004', 'bul_unify_005', 'bul_unify_006', 'exp_unify_001', 'fact_engineering_platform_001', 'fact_engineering_platform_002', 'fact_engineering_platform_003', 'fact_engineering_platform_004', 'fact_engineering_platform_006'] |
| `x2_unify_protected_bullet_metrics_preserved` | `NOT_OBSERVED` | `PASS` | `True` | delegated_to_role_episode_metric_outcome_contract |
| `x2_unify_track_ranked_selection_method` | `NOT_OBSERVED` | `PASS` | `True` | selected_fact_plan must use graph track-ranked allocation (not company_hint / hydrate). |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges with invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `anthropic_claude` | `NOT_OBSERVED` | `0.74/0.72 PASS` | - |
| `gemini_pro` | `NOT_OBSERVED` | `3.0/4.0 FAIL` | - |

## Section: unify_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `6356b6c3ace7ebaf4fb0b950` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `fd02a3bfa4c7030366915940` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\unify_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: executive_summary

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 3 pre-judge repair attempt(s), but combined too many source facts in one sentence; and sentence 1: mechanism_inventory:5_terms; and dominant_source_fact=unknown; and claim_support_graph_refs=[]; and suppressed_skills=[]; and sentence 1: mechanism_inventory:3_terms; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory), so JUDGES_NOT_REACHED and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `retry_loop` - The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate.
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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `6356b6c3ace7ebaf4fb0b950` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `fd02a3bfa4c7030366915940` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `4d45accc9442371277e957bd` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `219dbf42ecf83af204d604c4` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `fb6535f316fd5084bda14ae3` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `8551253f97cbc7b9b28710ff` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `3f86b9c47d8c34cf77185563` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `8d04c2c533c12bfa414c7809` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `f1bbfae93eeee55f258d54f7` | `False` | `CAUSAL` | The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `3ebeb84ddedcf79982553eae` | `False` | `CAUSAL` | Current deterministic finalization changed the published text before full X2 evaluation. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `80a595eb83ceea56c30d1c9f` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `8d04c2c533c12bfa` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; sentence 1: mechanism_inventory:5_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | dispatch provider generation | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `REPAIR_TRIGGERED` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\raw_model_output.txt` |
| 2 | `pre_judge_synthesis_retry` | `1` | `993a94bd5f4262f4` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; sentence 1: mechanism_inventory:5_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | provider retry synthesis_regen-00-01-9cd08b3f | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `monotonicity_rejected` | `REJECTED` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\synthesis_regen_receipt.json` |
| 3 | `pre_judge_synthesis_retry` | `2` | `b72e6ac1990e9a06` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; sentence 1: mechanism_inventory:5_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | provider retry synthesis_regen-00-02-0a1187e2 | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `ADVANCED_AS_IMPROVEMENT` | `MONOTONIC_IMPROVEMENT_ONLY` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\synthesis_regen_receipt.json` |
| 4 | `pre_judge_synthesis_retry` | `3` | `3c070a06b9c1196d` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; sentence 1: mechanism_inventory:3_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | provider retry synthesis_regen-00-03-0884548c | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `ADVANCED_AS_IMPROVEMENT` | `MONOTONIC_IMPROVEMENT_ONLY` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\synthesis_regen_receipt.json` |
| 5 | `deterministic_repair` | `1` | `-` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; sentence 1: mechanism_inventory:5_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | synthesis_regen | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_repair_ledger.json` |
| 6 | `deterministic_repair` | `2` | `-` | sentence_4_mechanism_inventory_compacted | repair_exec_summary_mechanism_inventory_sentence | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_repair_ledger.json` |
| 7 | `deterministic_repair` | `3` | `-` | sentence_2_source_fact_ids_compacted_to_3 | repair_exec_summary_cross_fact_conflation_row | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_repair_ledger.json` |
| 8 | `deterministic_repair` | `4` | `-` | sentence 1: mechanism_inventory:5_terms; dominant_source_fact=unknown; claim_support_graph_refs=[]; suppressed_skills=[] | graph_only_display_authority_fallback | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\section_repair_ledger.json` |
| 9 | `final_x2` | `1` | `58a7ca1606d95866` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x2_gate_outputs.json` |
| 10 | `judge_panel` | `-` | `-` | X2 failed before judge dispatch | none | `X1D_MODEL_BACKED_JUDGE` | `NOT_RUN` | `JUDGES_NOT_REACHED` | `PRE_JUDGE_BLOCK` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x1d_llm_judge_outputs.json` |
| 11 | `x3_disposition` | `-` | `58a7ca1606d95866` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `NO_JUDGE_ROWS_EMITTED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\lanes\executive_summary\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_PROVIDER_MODEL_provider_stub_transport_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'a52a8659fe2514c6957a3892569574cc031a83007731546c8aab5b4b22309059', 'fec_allowed_fact_ids_digest': 'a52a8659fe2514c6957a3892569574cc031a83007731546c8aab5b4b22309059', 'fec_narrowed_from_pool': True} |
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
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 13, 'violations': []} |
| `x2_em_dash_count_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_exec_summary_allowed_fact_utilization` | `NOT_OBSERVED` | `FAIL` | `True` | uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] |
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
| `x2_exec_summary_no_mechanism_inventory` | `NOT_OBSERVED` | `FAIL` | `True` | sentence 1: mechanism_inventory:5_terms; dominant_source_fact=reb_ibm_devsecops_release_resilience; claim_support_graph_refs=[skill_ibm_devsecops_pipeline_security]; suppressed_skills=[] |
| `x2_exec_summary_no_sentence_fragment` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_paragraph_max_words` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_partner_narrative_continuity` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_prompt_template_authority` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_robotic_transition_stack_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_sentence_count_6` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_speculative_capstone_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_strategy_no_commercialization_thread` | `NOT_OBSERVED` | `PASS` | `True` | skipped_not_strategy_lane |
| `x2_executive_summary_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'executive_summary', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '27a42627edf3088e9ae02d8faaf61c557fe6d004065b9079cf49fcfbd7bb63f0', 'canonical_evidence_set_digest': '27a42627edf3088e9ae02d8faaf61c557fe6d004065b9079cf49fcfbd7bb63f0', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 21, 'source_fact_ids_checked': ['reb_unify_agentic_platform_architecture', 'skill_unify_agentic_multi_agent_orchestration_contracts', 'skill_unify_agentic_human_override_escalation_paths', 'skill_unify_agentic_replay_key_audit_manifest_design', 'fact_engineering_platform_002', 'skill_unify_agentic_runtime_proof_bundle_lineage', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'reb_unify_platform_commercialization_leadership', 'metric_unify_22m_ip_led_revenue', 'skill_agentic_platform_productization', 'fact_engineering_platform_001', 'fact_engineering_platform_006'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 21, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'executive_summary'} |
| `x2_executive_summary_synthesis_quality` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 21, 'violations': []} |
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
| `x2_model_name_allowed` | `NOT_OBSERVED` | `PASS` | `True` | claude-sonnet-5 |
| `x2_no_extra_unrecognized_fields` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_inferred_bridge_claims` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_monolithic_prompt` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_selected_fact_plan_model_echo` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | provider=external_claude, status=REAL_LLM |
| `x2_north_star_style_echo_unsupported_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_overbroad_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 21, 'violations': []} |
| `x2_prompt_hash_known` | `NOT_OBSERVED` | `PASS` | `True` | c64cb64e21f9fc98 |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | requested=external_claude, attempted=external_claude |
| `x2_required_artifacts_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_required_fields_complete` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '86b518ae7a25da010c2bb8999c5fd5936c1090c9f703aa825124188c8937dfda', 'claim_count': 6, 'bound_claim_count': 6, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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
| `x2_x1d_judge_packet_hash_uniform` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_raw_responses_written` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: final_resume_aggregation

### Layperson RCA

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.

The aggregate panel ran and recorded - EVIDENCE_NOT_RECORDED; the required two-of-two model-backed quorum was not met.

The controlling product defect is aggregate coherence, not upstream section eligibility: the failed aggregate gate is recorded in the final-resume review artifact.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `aggregate_coherence_quorum` - Final assembly completed, but the whole-resume model-backed judge quorum failed.
- Code cause status: `AGGREGATE_GATE_ISOLATED`

### Underlying Root Cause

- `aggregate_coherence_root_cause` / `ISOLATED_TO_AGGREGATE_JUDGE`: All required section outputs were assembled; final authorization failed because the model-backed whole-resume panel did not reach its required quorum.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `6356b6c3ace7ebaf4fb0b950` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `fd02a3bfa4c7030366915940` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| final resume aggregation and judge quorum | `apps_rg/runtime/assembly/full_resume_llm_coherence.py` | `emit_full_resume_llm_coherence_review` | `False` | `PREEXISTED_BASELINE` | `CURRENT_RUN_EVIDENCE_ISOLATED` |
| final resume release gate | `apps_rg/runtime/assembly/final_resume_x2.py` | `gate_x2_full_resume_llm_coherence_aggregation` | `False` | `PREEXISTED_BASELINE` | `CURRENT_RUN_EVIDENCE_ISOLATED` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `assembly_input` | `0` | `58a7ca1606d95866` | accepted section snapshots | assemble accepted X3 section outputs | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `ASSEMBLED_RESUME_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\final_resume.json` |
| 2 | `final_x2` | `1` | `58a7ca1606d95866` | structural and aggregate coherence gates | evaluate final resume release gates | `FINAL_RESUME_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\final_resume_x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\x1d_full_resume_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\modular_r4\final_resume_assembly\full_resume_llm_coherence_review.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
