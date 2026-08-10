# apps_rg Output Bisect

## Section: competencies

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_visible_terms_svp_agentic_richness, x2_no_bullet_outcome_restatement, x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `fda43858cf4cbb4a40ba2c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `3d3fe96ebc5e2d6a38e17027` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `b8898b40bde73bc7d289e4bf` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `8ffa825cc5ce5c5c8512d7e7` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `9f5383ac09c295f4262866e4` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `d08293b7c281c35707d20941` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `8ffa825cc5ce5c5c` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | sync_and_coerce | competencies_pre_x2_deterministic_pipeline | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_repair_ledger.json` |
| 3 | `deterministic_repair` | `2` | `-` | capability_projection | finalize_competencies_v3_output | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\section_repair_ledger.json` |
| 4 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x2_gate_outputs.json` |
| 5 | `judge_panel` | `gemini_pro` | `490e522b9af6d800` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x1d_gemini_provider_response_raw_20260808_214456_011.json` |
| 6 | `judge_panel` | `openai_chatgpt` | `490e522b9af6d800` | S2 repeats control-plane architecture and title-stuffs SVP Engineering. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.6/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x1d_openai_provider_response_raw_20260808_214529_394.json` |
| 7 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\judge_remediation_cycles.json` |
| 8 | `x3_disposition` | `-` | `7491cb18c04e2e72` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\competencies\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '9c7aa097ad244e9fae1bb240b0fbae449be0481d897007a3bffebb5be9d848c6', 'fec_allowed_fact_ids_digest': '9c7aa097ad244e9fae1bb240b0fbae449be0481d897007a3bffebb5be9d848c6', 'fec_narrowed_from_pool': True} |
| `x2_all_terms_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_base_archive_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 10, 'violations': []} |
| `x2_competencies_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'competencies', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '6bf8d0cd2493aaad998995a9ec71fb69e9fd4b5533ed61aeed472bcfa23dd7ed', 'canonical_evidence_set_digest': '6bf8d0cd2493aaad998995a9ec71fb69e9fd4b5533ed61aeed472bcfa23dd7ed', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 40, 'source_fact_ids_checked': ['reb_unify_partner_channel_cosell', 'fact_revenue_ops_002', 'fact_partnerships_gtm_002', 'exp_unify_001', 'fact_engineering_platform_001', 'fact_engineering_platform_002', 'reb_unify_agentic_platform_architecture', 'fact_revenue_ops_001', 'reb_ibm_presales_solution_engineering', 'fact_revenue_ops_004', 'reb_ibm_aws_alliance_partner_cosell_gtm'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 40, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'competencies'} |
| `x2_competencies_approved_category_labels` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_competencies_capability_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | 9 |
| `x2_competencies_capability_family_coverage` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_platform', 'runtime_governance', 'retrieval_context', 'llmops', 'distributed_infra', 'productization', 'partner_architecture', 'engineering_leadership'] |
| `x2_competencies_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_competencies_generic_category_blocked_without_graph` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_competencies_graph_granularity_gates` | `NOT_OBSERVED` | `PASS` | `True` | {'category_count': 8, 'min_unique_leaf_skills_per_category': 1, 'categories_missing_leaf_skills': [], 'min_unique_source_facts_per_category': 1, 'categories_missing_source_facts': [], 'dominant_source_fact_id': 'reb_unify_partner_channel_cosell', 'dominant_source_fact_category_share': 0.25, 'source_fact_concentration_threshold': 0.75, 'target_role_profile': 'ai_partnerships_gtm', 'required_role_axes': ['co_sell', 'gtm_enablement', 'hyperscaler_alliance', 'joint_solution', 'partner_architecture', 'partner_motions'], 'missing_role_axes': []} |
| `x2_competencies_graph_traversal_sufficiency` | `NOT_OBSERVED` | `PASS` | `True` | {'target_role_profile': 'ai_partnerships_gtm', 'candidate_nodes_visited_count': 85, 'selected_unique_leaf_skill_count': 30, 'selected_unique_metric_count': 16, 'selected_source_fact_count': 8, 'rejected_sibling_skill_count': 19, 'candidate_conservation': {'candidate_count': 337, 'terminal_decision_count': 337, 'unexplained_candidate_count': 0, 'duplicate_candidate_path_ids': [], 'count_by_candidate_type': {'leaf_skill': 165, 'metric_outcome': 100, 'role_episode_root': 35, 'source_fact': 37}, 'selected_by_candidate_type': {'leaf_skill': 30, 'metric_outcome': 16, 'role_episode_root': 8, 'source_fact': 8}, 'rejected_by_candidate_type': {'leaf_skill': 135, 'metric_outcome': 84, 'role_episode_root': 27, 'source_fact': 29}, 'role_episode_roots_total': 35, 'role_episode_roots_selected': 8, 'role_episode_roots_rejected': 27, 'role_episode_roots_unexplained': 0, 'pass': True}, 'rejected_eligible_root_count': 27, 'frontier_size_by_hop_depth': {'0_role_episode_roots': 35, '1_leaf_skill_candidates': 165, '2_metric_outcome_candidates': 100, '1_source_fact_candidates': 37}, 'graph_evidence_depth_status': 'judge_grade', 'missing_role_axes': []} |
| `x2_competencies_keyword_repetition_limit` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_min_category_count` | `NOT_OBSERVED` | `PASS` | `True` | 8 |
| `x2_competencies_min_items_per_category` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_all_generic_skill_phrase` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_credential_relisting` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_default_fid_proof` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_competencies_no_fragment_or_one_word_terms` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_low_rigor_two_word_items` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_metric_ids_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_metrics_as_skills_without_capability_context` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_no_reserved_certification_category` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_per_category_confidence_nonconstant` | `NOT_OBSERVED` | `PASS` | `True` | {'missing_confidence_category_labels': [], 'unique_selector_confidence_values': [0.813, 0.821, 0.829, 0.841, 0.847, 0.853, 0.901], 'unique_confidence_values': [0.5626, 0.6091, 0.6532, 0.6556, 0.6685, 0.7768, 0.7785, 0.7944], 'category_count': 8} |
| `x2_competencies_rejected_neighbor_audit_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_ok': True, 'audit_status': 'thin_candidate_pool', 'candidate_label_count': 0, 'candidate_variant_count': 0, 'selected_count': 0, 'rejected_neighbor_count': 0, 'graph_candidate_receipt_schema_ok': True, 'graph_candidate_conservation_pass': True, 'graph_rejected_candidate_count': 275} |
| `x2_competencies_role_alignment_terms` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_selected_graph_evidence_depth_sufficient` | `NOT_OBSERVED` | `PASS` | `True` | {'status': 'judge_grade', 'summary': 'competencies: 8/8 rich items, 30 unique skills, 16 unique metrics, 100% semantic coverage, 100% axis coverage', 'thin_item_ids': []} |
| `x2_competencies_source_fact_concentration_limit` | `NOT_OBSERVED` | `PASS` | `True` | {'dominant_source_fact_id': 'reb_unify_partner_channel_cosell', 'dominant_source_fact_category_share': 0.25, 'dominant_source_fact_category_count': 2, 'category_count': 8} |
| `x2_competencies_term_support_ids_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_visible_terms_svp_agentic_richness` | `NOT_OBSERVED` | `FAIL` | `True` | visible_competency_missing_agentic_mechanism label='Partner Applied AI Architecture' phrase='partner cloud vendor joint gtm' |
| `x2_competency_bundle_id_required_per_category` | `NOT_OBSERVED` | `PASS` | `True` | all_bound |
| `x2_competency_companion_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_context_used_as_proof': False} |
| `x2_competency_duplicate_variant_absent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_format_category_colon_terms` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_jd_mirroring_within_limit` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_rigor_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | 30 |
| `x2_competency_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_compact_word_count` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_primary_fact_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_primary_fact_unique` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_supported` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_terms_canonical_structured` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_default_fid_only_support_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_duplicate_variants_collapsed` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 40, 'violations': []} |
| `x2_gate_rows_are_internally_consistent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_generic_taxonomy_only_category_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_graph_skill_node_ids_required_per_category` | `NOT_OBSERVED` | `PASS` | `True` | all_have_graph_nodes |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 30, 'claims_supported_by_selected_resume_facts': 30, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 30, 'claims_supported_by_selected_resume_facts': 30, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_only_skill_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_briefing_only_skills` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_bullet_format` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_bullet_outcome_restatement` | `NOT_OBSERVED` | `FAIL` | `True` | Term restates bullet text. |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_full_sentences` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_jd_only_skills` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_keyword_stuffing` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_no_mock_fixture_markers_in_real_llm_output` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | REAL_LLM |
| `x2_no_unsupported_tools_frameworks_models` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_partner_architecture_bundle_present` | `NOT_OBSERVED` | `PASS` | `True` | {'proof_pool_has_bundle': True, 'rendered_categories': ['cloud & partner ecosystems']} |
| `x2_partner_architecture_terms_require_partner_bundle` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_partner_terms_source_roots_forbid_insurtech_ey` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 40, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | external_claude->external_provider_http |
| `x2_required_capability_families_covered` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_platform', 'runtime_governance', 'retrieval_context', 'llmops', 'distributed_infra', 'productization', 'partner_architecture', 'engineering_leadership'] |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 30, 'claims_supported_by_selected_resume_facts': 30, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_source_fact_ids_or_graph_lineage_required_per_category` | `NOT_OBSERVED` | `PASS` | `True` | all_have_lineage |
| `x2_structured_term_primary_facts` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_technical_density_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | 0.8 |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | ['gemini_pro', 'openai_chatgpt'] |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `4.6/4.0 PASS` | - |

## Section: ibm_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_bullet_technical_specificity_floor), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `fda43858cf4cbb4a40ba2c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `f8cad925bdfa9b5c5fd64ce8` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `bb07ba6e59f30dee9774b604` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `68db11a2fdcb513d53995e82` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `728f5a0367d08bffd567b223` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | graph_plan_fact_id_alignment | align_ibm_claim_ledger_from_canonical_facts | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_repair_ledger.json` |
| 3 | `deterministic_repair` | `2` | `-` | surface_fact_backed_metric_tokens_model_dropped | inject_ibm_plan_fact_metric_anchors | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\section_repair_ledger.json` |
| 4 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x2_gate_outputs.json` |
| 5 | `judge_panel` | `gemini_pro` | `0a4ff20778c90715` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x1d_gemini_provider_response_raw_20260808_214711_590.json` |
| 6 | `judge_panel` | `anthropic_claude` | `4b0b49d0dc3efd18` | Employment pool selector: 5 slots, min_score=0.78, threshold=0.72, gate_ok=True | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `0.78/0.72 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x1d_anthropic_claude_provider_response_raw_20260808_214702_830.json` |
| 7 | `judge_panel` | `gemini_pro` | `0a4ff20778c90715` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x1d_gemini_provider_response_raw_20260808_214722_215.json` |
| 8 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\judge_remediation_cycles.json` |
| 9 | `x3_disposition` | `-` | `f7c1beafa069986c` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 5} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'b3482f7f7eca9fc5f3000f4cb395ab1cf62d14eda1d3c25faa63030241ff5b0b', 'fec_allowed_fact_ids_digest': 'b3482f7f7eca9fc5f3000f4cb395ab1cf62d14eda1d3c25faa63030241ff5b0b', 'fec_narrowed_from_pool': True} |
| `x2_base_resume_ngram_overlap_ibm` | `NOT_OBSERVED` | `PASS` | `True` | all_below_threshold |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_bullet_seniority_floor` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_bullet_technical_specificity_floor` | `NOT_OBSERVED` | `FAIL` | `True` | bul_ibm_003: no named mechanism/technology in bullet text; bul_ibm_004: no named mechanism/technology in bullet text |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | Every bul_ibm_* bullet must appear in output and claim_ledger. |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 5, 'violations': []} |
| `x2_e0_example_ngram_overlap_ibm` | `NOT_OBSERVED` | `PASS` | `True` | all_below_threshold |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 39, 'violations': []} |
| `x2_ibm_augmented_skills_graph_proof_pool_only` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_ibm_bullet_count_5` | `NOT_OBSERVED` | `PASS` | `True` | Must output exactly 5 IBM bullets. |
| `x2_ibm_bullet_graph_skill_node_ids_required` | `NOT_OBSERVED` | `PASS` | `True` | all_present |
| `x2_ibm_bullet_no_embedded_newline` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_bullet_no_paragraph_block` | `NOT_OBSERVED` | `PASS` | `True` | <=320 chars |
| `x2_ibm_bullet_role_episode_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | all_present |
| `x2_ibm_bullet_single_thought` | `NOT_OBSERVED` | `PASS` | `True` | 1 sentence each |
| `x2_ibm_bullets_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'ibm_bullets', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'b3482f7f7eca9fc5f3000f4cb395ab1cf62d14eda1d3c25faa63030241ff5b0b', 'canonical_evidence_set_digest': 'b3482f7f7eca9fc5f3000f4cb395ab1cf62d14eda1d3c25faa63030241ff5b0b', 'id_alias_map': {'bul_ibm_001': 'fact_partnerships_gtm_002', 'bul_ibm_002': 'fact_revenue_ops_005', 'bul_ibm_003': 'fact_revenue_ops_001', 'bul_ibm_004': 'fact_revenue_ops_003', 'bul_ibm_005': 'fact_revenue_ops_005'}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 39, 'source_fact_ids_checked': ['bul_ibm_001', 'bul_ibm_002', 'bul_ibm_003', 'bul_ibm_004', 'bul_ibm_005'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 39, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'ibm_bullets'} |
| `x2_ibm_graph_only_no_base_resume_bullets` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_ibm_hold_metric_forbidden_in_output` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_metric_anchor_bullet_ownership` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_ibm_metric_outcome_id_required_when_has_metric` | `NOT_OBSERVED` | `PASS` | `True` | all_traceable |
| `x2_ibm_metrics_preserved` | `NOT_OBSERVED` | `PASS` | `True` | {'forbidden_absent': True, 'promotable_ids': ['metric_ibm_onprem_to_aws_modernization_waves', 'metric_ibm_regulated_reference_architecture_reuse', 'metric_ibm_stress_test_cycle_weeks_to_hours', 'metric_ibm_decision_support_scenario_traceability', 'metric_ibm_presales_discovery_to_solution_handoff', 'metric_ibm_executive_buyer_architecture_alignment', 'metric_ibm_offering_accelerator_package_reuse', 'metric_ibm_client_facing_modernization_playbooks', 'metric_ibm_quota_aligned_solution_cadence', 'metric_ibm_revenue_target_solution_validation', 'metric_ibm_text_signal_to_review_queue', 'metric_ibm_ml_output_business_action_packaging', 'metric_ibm_budget_portfolio_bi_views', 'metric_ibm_modeling_delivery_cost_assumption_traceability', 'metric_ibm_value_realization_account_reviews', 'metric_ibm_adoption_risk_to_expansion_readiness', 'metric_ibm_20pct_joint_revenue_growth', 'metric_ibm_alliance_cosell_operating_cadence', 'metric_ibm_ai_driven_sales_frameworks', 'metric_ibm_release_gate_security_scanning_coverage', 'metric_ibm_deployment_blueprint_repeatability']} |
| `x2_ibm_narrative_slot_reservation` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_no_rewrite_intensity_model` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_ibm_only_fact_scope` | `NOT_OBSERVED` | `PASS` | `True` | ['bul_ibm_001', 'bul_ibm_002', 'bul_ibm_003', 'bul_ibm_004', 'bul_ibm_005'] |
| `x2_ibm_role_episode_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'flat_skill_only': False, 'consumption_mode': 'role_episode_bundle_required'} |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 5, 'claims_supported_by_selected_resume_facts': 5, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 5, 'claims_supported_by_selected_resume_facts': 5, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_metric_fact_id_granularity` | `NOT_OBSERVED` | `PASS` | `True` | Metric claims lack matching bul_ibm_* source_fact_ids in claim_ledger. |
| `x2_no_agentic_inflation` | `NOT_OBSERVED` | `PASS` | `True` | Agentic inflation language in IBM bullets. |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | Em dash found. |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | First-person pronoun found. |
| `x2_no_generic_consulting_substitution` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_no_generic_filler` | `NOT_OBSERVED` | `PASS` | `True` | Generic filler phrase found. |
| `x2_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | Inline source tags found in bullet text. |
| `x2_no_jd_only_claims` | `NOT_OBSERVED` | `PASS` | `True` | JD phrase copied into bullet proof. |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | Silent mock fallback detected. |
| `x2_no_taxonomy_label_prefix_in_display_text` | `NOT_OBSERVED` | `PASS` | `True` | bullet_text must not start with a category-style Title: prefix. |
| `x2_no_unify_fact_leakage` | `NOT_OBSERVED` | `PASS` | `True` | Unify bullet fact leakage detected. |
| `x2_no_unify_runtime_terms` | `NOT_OBSERVED` | `PASS` | `True` | Unify runtime vocabulary leaked into IBM bullets. |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 39, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider requested does not match attempted. |
| `x2_required_top_level_json_keys` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 5, 'claims_supported_by_selected_resume_facts': 5, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_text_claim_coverage_integrity` | `NOT_OBSERVED` | `PASS` | `True` | structural_alignment_ok |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges with invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `anthropic_claude` | `NOT_OBSERVED` | `0.78/0.72 PASS` | - |
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |

## Section: ey_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `fda43858cf4cbb4a40ba2c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `329c4399636ffc04e98f9752` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `229eaa5a0478f0f56324b7be` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `e1a9b05732afc23bec605a39` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `578f9c910ee63f8f676a373e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `7cdc5c68e2d62019` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x1d_gemini_provider_response_raw_20260808_214845_285.json` |
| 4 | `judge_panel` | `anthropic_claude` | `eb04954a889612f5` | Employment pool selector: 3 slots, min_score=0.82, threshold=0.72, gate_ok=False | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `0.82/0.72 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x1d_anthropic_claude_provider_response_raw_20260808_214837_397.json` |
| 5 | `x3_disposition` | `-` | `1631fc3126e3f25a` | X1D decisive judge failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_ey_bullets_allowed_fact_ids_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | 11 |
| `x2_ey_bullets_bullet_count_3` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_ey_bullets_bullet_no_embedded_newline` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ey_bullets_bullet_single_thought` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ey_bullets_display_text_proof_authorized` | `NOT_OBSERVED` | `PASS` | `True` | {'status': 'PASS', 'display_text_authority': 'selected_fact_plan_claim_text', 'rows': [{'row_id': 'bul_ey_001', 'source_fact_ids': ['bul_ey_001'], 'source_fact_ids_allowed': True, 'text_matches_selected_fact_claim_text': True}, {'row_id': 'bul_ey_002', 'source_fact_ids': ['bul_ey_002'], 'source_fact_ids_allowed': True, 'text_matches_selected_fact_claim_text': True}, {'row_id': 'bul_ey_003', 'source_fact_ids': ['bul_ey_003'], 'source_fact_ids_allowed': True, 'text_matches_selected_fact_claim_text': True}]} |
| `x2_ey_bullets_graph_role_episode_bundle_consumed` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_ey_bullets_runtime_real_llm` | `NOT_OBSERVED` | `PASS` | `True` | REAL_LLM |
| `x2_ey_bullets_source_fact_ids_supported` | `NOT_OBSERVED` | `PASS` | `True` | {'bad': [], 'cited_count': 3} |
| `x2_ey_bullets_targeting_only_not_experience_claim` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': 'e4e30b08c589f051b2eb20b73b06f56aec10ebff4b72eda748fdd77d09d66ff2', 'claim_count': 3, 'bound_claim_count': 3, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `anthropic_claude` | `NOT_OBSERVED` | `0.82/0.72 FAIL` | - |
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |

## Section: ibm_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ibm_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: ey_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\ey_narrative\x3_disposition.json` |

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

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `fda43858cf4cbb4a40ba2c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `53a7fe4a94ea54c42d1c89e9` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `dbe4e74905cf67d12ec72cb5` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `9f820f79db92a9e0504b0f27` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `81cc6ca5c0b23cc25f7a465b` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `ea274c3e9482fc759bb0966b` | `False` | `CAUSAL` | Current deterministic finalization changed the published text before full X2 evaluation. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `be0bcf73250f6e2766a99a42` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `81cc6ca5c0b23cc2` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `f76d7260eec843a1` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | X2 failed before judge dispatch | none | `X1D_MODEL_BACKED_JUDGE` | `NOT_RUN` | `JUDGES_NOT_REACHED` | `PRE_JUDGE_BLOCK` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `f76d7260eec843a1` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `NO_JUDGE_ROWS_EMITTED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\executive_summary\x3_disposition.json` |

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
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 11, 'violations': []} |
| `x2_em_dash_count_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_exec_summary_allowed_fact_utilization` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids` | `NOT_OBSERVED` | `FAIL` | `True` | filtered_out_mismatch:violations=['fact_engineering_platform_003', 'fact_partnerships_gtm_002', 'reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_unify_runtime_reliability_governance']:filtered=['fact_engineering_platform_003', 'fact_partnerships_gtm_002', 'reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_aws_modernization_architecture', 'reb_ibm_offering_accelerator_management', 'reb_insurtech_aws_guidewire_core_modernization', 'reb_insurtech_regulated_aws_control_implementation', 'reb_unify_distributed_ecosystem_engineering', 'reb_unify_partner_channel_cosell', 'reb_unify_runtime_reliability_governance'] |
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
| `x2_executive_summary_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'executive_summary', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'e5eda39114b37eaa32c3d7213346d85337a290a0b96447eec137b2cf99ab8e85', 'canonical_evidence_set_digest': 'e5eda39114b37eaa32c3d7213346d85337a290a0b96447eec137b2cf99ab8e85', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 21, 'source_fact_ids_checked': ['reb_ibm_devsecops_release_resilience', 'reb_unify_agentic_platform_architecture', 'skill_unify_agentic_multi_agent_orchestration_contracts', 'fact_engineering_platform_001', 'skill_agentic_platform_productization', 'skill_unify_agentic_runtime_proof_bundle_lineage', 'skill_unify_agentic_replay_key_audit_manifest_design', 'reb_unify_platform_commercialization_leadership', 'metric_unify_22m_ip_led_revenue', 'fact_engineering_platform_006', 'skill_ibm_devsecops_pipeline_security'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 21, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'executive_summary'} |
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
| `x2_prompt_hash_known` | `NOT_OBSERVED` | `PASS` | `True` | 0bfc7c629e69a7e0 |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | requested=external_claude, attempted=external_claude |
| `x2_required_artifacts_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_required_fields_complete` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
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

## Section: headline

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\apps_research\runs\bridge_rg_research_bridge_8f97ab9b_3da2370b-f1ae-4a16-955c-b48ffc256ab3\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_executive_abstraction_floor, x2_headline_xyz_literal_grounding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `fda43858cf4cbb4a40ba2c9c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `d64a923118dc7a837fc386e1` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `de5430052d58bfed7f648d8d` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `f5559f6674a69e921b313afe` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `72eaceb60d6036899c6fa41c` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | x2_headline_technical_specificity_floor_met:1_of_2 | headline_content_signal_repair | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\section_repair_ledger.json` |
| 3 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x2_gate_outputs.json` |
| 4 | `judge_panel` | `gemini_pro` | `3d8963514b6e0386` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x1d_gemini_provider_response_raw_20260808_215101_068.json` |
| 5 | `judge_panel` | `openai_chatgpt` | `3d8963514b6e0386` | X/Y/Z lack eligible active-pool proof bindings; the ledger cites only reb_* and skill_* IDs.; The noun-stack phrasing feels compressed and somewhat machine-generated. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `2.7/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x1d_openai_provider_response_raw_20260808_215125_540.json` |
| 6 | `x3_disposition` | `-` | `def4f76b9b86196b` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\sections\headline\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '9de857fbb1d8ecbff9db9398bf9df2ff0bad4daf112ba1ca1336b125e9227b1e', 'fec_allowed_fact_ids_digest': '9de857fbb1d8ecbff9db9398bf9df2ff0bad4daf112ba1ca1336b125e9227b1e', 'fec_narrowed_from_pool': True} |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 4, 'violations': []} |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 6, 'violations': []} |
| `x2_headline_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'headline', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '2790b56ef2e7f1a303daf9d644a3f28427238446d69b9e21d89adf0b5d51724a', 'canonical_evidence_set_digest': '2790b56ef2e7f1a303daf9d644a3f28427238446d69b9e21d89adf0b5d51724a', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 6, 'source_fact_ids_checked': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 6, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'headline'} |
| `x2_headline_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_base_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_briefing_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'anti_stuffing_check': 'No JD/briefing phrases lifted; segments built from cited fact claim_text nouns only', 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'jd_used_as_proof': False, 'selected_theme': 'Quota-aligned partner leadership combined with multi-agent runtime governance, foregrounded against Anthropic partnerships/architecture targeting context', 'targeting_only': True} |
| `x2_headline_claim_ledger_no_silent_row_drop` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_claim_ledger_rows_present` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_headline_claim_ledger_segment_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | {'matched_segments': ['multi-agent runtime governance', 'partner portfolio oversight', 'quota-aligned solution leadership'], 'expected_segments': ['Quota-Aligned Solution Leadership', 'Multi-Agent Runtime Governance', 'Partner Portfolio Oversight'], 'row_count': 3} |
| `x2_headline_companion_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'anti_stuffing_check': 'No JD/briefing phrases lifted; segments built from cited fact claim_text nouns only', 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'jd_used_as_proof': False, 'selected_theme': 'Quota-aligned partner leadership combined with multi-agent runtime governance, foregrounded against Anthropic partnerships/architecture targeting context', 'targeting_only': True} |
| `x2_headline_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_e0_ngram_overlap_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_exactly_one_line` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_executive_abstraction_floor` | `NOT_OBSERVED` | `FAIL` | `True` | Each headline segment must express executive scope such as platform, architecture, governance, ecosystem, commercialization, or regulated systems. |
| `x2_headline_executive_length` | `NOT_OBSERVED` | `PASS` | `True` | 114 |
| `x2_headline_generic_it_strategy_demote_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_governance_or_regulated_ai_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance'] |
| `x2_headline_graph_skill_node_ids_required` | `NOT_OBSERVED` | `PASS` | `True` | ['skill_context_engineering', 'skill_partner_pnl_oversight'] |
| `x2_headline_jd_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'anti_stuffing_check': 'No JD/briefing phrases lifted; segments built from cited fact claim_text nouns only', 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'jd_used_as_proof': False, 'selected_theme': 'Quota-aligned partner leadership combined with multi-agent runtime governance, foregrounded against Anthropic partnerships/architecture targeting context', 'targeting_only': True} |
| `x2_headline_jd_only_phrase_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_currency_percent_literals` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_digit_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_hype_markers` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_headline_no_keyword_stuffing_heuristic` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_metrics` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_narrowing_it_labels` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_standalone_vendor_architecture` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Quota-Aligned Solution Leadership', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Multi-Agent Runtime Governance', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Partner Portfolio Oversight', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Quota-Aligned Solution Leadership'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_no_title_inflation` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_unsupported_employer_names` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_pipe_four_segments` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_platform_or_runtime_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_ai_platforms', 'runtime_governance'] |
| `x2_headline_positioning_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'] |
| `x2_headline_positioning_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'mode': 'headline_positioning_bundle_required'} |
| `x2_headline_positioning_family_preserved` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_ai_platforms', 'runtime_governance'] |
| `x2_headline_prompt_reasoning_receipt_clean` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_raw_model_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_segments_quality` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_selected_fact_plan_matches_ledger` | `NOT_OBSERVED` | `PASS` | `True` | {'required_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'ledger_union': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'cited_but_not_selected': []} |
| `x2_headline_self_check_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'runtime': {'word_count': 11, 'segment_count': 4, 'separator_count': 3, 'word_count_in_range': True, 'fixed_prefix': True, 'no_metrics': True, 'no_employer_names': True, 'no_company_names': True}, 'model': {'fixed_prefix': True, 'segment_count': 4, 'separator_count': 3, 'word_count': 11, 'word_count_in_range': True, 'no_metrics': True, 'no_employer_names': True, 'no_company_names': True}} |
| `x2_headline_seniority_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | SVP Engineering |
| `x2_headline_source_fact_or_graph_lineage_required` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'] |
| `x2_headline_source_supported` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'] |
| `x2_headline_svp_engineering_seniority_required` | `NOT_OBSERVED` | `PASS` | `True` | SVP Engineering |
| `x2_headline_technical_specificity_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_ai_platforms', 'runtime_governance'] |
| `x2_headline_text_claim_coverage_integrity` | `NOT_OBSERVED` | `PASS` | `True` | [{'segment_index': 2, 'segment_text': 'Quota-Aligned Solution Leadership', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}, {'segment_index': 3, 'segment_text': 'Multi-Agent Runtime Governance', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}, {'segment_index': 4, 'segment_text': 'Partner Portfolio Oversight', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}] |
| `x2_headline_vendor_terms_proof_only` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Quota-Aligned Solution Leadership', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Multi-Agent Runtime Governance', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Partner Portfolio Oversight', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Quota-Aligned Solution Leadership'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_word_count_10_to_13` | `NOT_OBSERVED` | `PASS` | `True` | 11 |
| `x2_headline_xyz_literal_grounding` | `NOT_OBSERVED` | `FAIL` | `True` | 'Multi-Agent Runtime Governance' shares zero content nouns with cited fact(s) ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'] — phrase is not lexically grounded in fact claim_text |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 3, 'claims_supported_by_selected_resume_facts': 3, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 3, 'claims_supported_by_selected_resume_facts': 3, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_no_jd_only_claims` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | Silent mock fallback detected. |
| `x2_no_target_company_as_experience` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 6, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider mismatch. |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': 'e4e30b08c589f051b2eb20b73b06f56aec10ebff4b72eda748fdd77d09d66ff2', 'claim_count': 3, 'bound_claim_count': 3, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 3, 'claims_supported_by_selected_resume_facts': 3, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `2.7/4.0 FAIL` | - |

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9f8cb9c21ef8ef650953db56` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `11abfdc34199ecdf1e49b3ce` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T214028Z_8eadd696\modular_r4\final_resume_assembly\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
