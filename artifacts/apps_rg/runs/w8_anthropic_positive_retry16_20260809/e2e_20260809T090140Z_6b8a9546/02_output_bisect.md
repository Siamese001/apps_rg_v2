# apps_rg Output Bisect

## Section: competencies

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_required_capability_families_covered, x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b81b6e2838e4252ffc39bf45` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `5d4d78528017ec83c470242e` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `592e39cd4b666f3b295b1479` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `0615ec962dde643ac19f4a7e` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `2d041442332f43315bd30279` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `855b899b0872b433898fca20` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `0615ec962dde643a` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | sync_and_coerce | competencies_pre_x2_deterministic_pipeline | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_repair_ledger.json` |
| 3 | `deterministic_repair` | `2` | `-` | capability_projection | finalize_competencies_v3_output | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\section_repair_ledger.json` |
| 4 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x2_gate_outputs.json` |
| 5 | `judge_panel` | `gemini_pro` | `969351582d0e0bf6` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x1d_gemini_provider_response_raw_20260809_090356_662.json` |
| 6 | `judge_panel` | `openai_chatgpt` | `969351582d0e0bf6` | Four technical categories lean heavily on one platform fact surface.; Alliance GTM mixes customer success cadence with partner execution.; Engineering Leadership is supported mainly by presales and pursuit terms.; Enterprise technical pre-sales solution engineering is comparatively generic.; Runtime governance and LLMOps show minor assurance-concept overlap. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.2/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x1d_openai_provider_response_raw_20260809_090427_551.json` |
| 7 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\judge_remediation_cycles.json` |
| 8 | `x3_disposition` | `-` | `fd4dc2006ed98c17` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\competencies\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'e00e0b1bc231e9375a7b2b1a32ac1f420ffc8b0106f38b987ad4992435768e7a', 'fec_allowed_fact_ids_digest': 'e00e0b1bc231e9375a7b2b1a32ac1f420ffc8b0106f38b987ad4992435768e7a', 'fec_narrowed_from_pool': True} |
| `x2_all_terms_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_base_archive_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 8, 'violations': []} |
| `x2_competencies_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'competencies', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '81c06162fb03cea929e91f0c3f69861e96d0047130751379fc22da4e5b1a6269', 'canonical_evidence_set_digest': '81c06162fb03cea929e91f0c3f69861e96d0047130751379fc22da4e5b1a6269', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 37, 'source_fact_ids_checked': ['reb_unify_partner_channel_cosell', 'fact_engineering_platform_001', 'fact_engineering_platform_002', 'reb_unify_agentic_platform_architecture', 'fact_revenue_ops_001', 'fact_revenue_ops_004', 'exp_unify_001', 'reb_ibm_presales_solution_engineering', 'reb_ibm_aws_alliance_partner_cosell_gtm'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 37, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'competencies'} |
| `x2_competencies_approved_category_labels` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_competencies_capability_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | 9 |
| `x2_competencies_capability_family_coverage` | `NOT_OBSERVED` | `PASS` | `True` | ['agentic_platform', 'runtime_governance', 'retrieval_context', 'llmops', 'distributed_infra', 'partner_architecture', 'engineering_leadership'] |
| `x2_competencies_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_competencies_generic_category_blocked_without_graph` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_competencies_graph_granularity_gates` | `NOT_OBSERVED` | `PASS` | `True` | {'category_count': 8, 'min_unique_leaf_skills_per_category': 1, 'categories_missing_leaf_skills': [], 'min_unique_source_facts_per_category': 1, 'categories_missing_source_facts': [], 'dominant_source_fact_id': 'fact_engineering_platform_001', 'dominant_source_fact_category_share': 0.5, 'source_fact_concentration_threshold': 0.75, 'target_role_profile': 'ai_partnerships_gtm', 'required_role_axes': ['co_sell', 'gtm_enablement', 'hyperscaler_alliance', 'joint_solution', 'partner_architecture', 'partner_motions'], 'missing_role_axes': []} |
| `x2_competencies_graph_traversal_sufficiency` | `NOT_OBSERVED` | `PASS` | `True` | {'target_role_profile': 'ai_partnerships_gtm', 'candidate_nodes_visited_count': 65, 'selected_unique_leaf_skill_count': 27, 'selected_unique_metric_count': 16, 'selected_source_fact_count': 8, 'rejected_sibling_skill_count': 10, 'candidate_conservation': {'candidate_count': 337, 'terminal_decision_count': 337, 'unexplained_candidate_count': 0, 'duplicate_candidate_path_ids': [], 'count_by_candidate_type': {'leaf_skill': 165, 'metric_outcome': 100, 'role_episode_root': 35, 'source_fact': 37}, 'selected_by_candidate_type': {'leaf_skill': 27, 'metric_outcome': 16, 'role_episode_root': 8, 'source_fact': 8}, 'rejected_by_candidate_type': {'leaf_skill': 138, 'metric_outcome': 84, 'role_episode_root': 27, 'source_fact': 29}, 'role_episode_roots_total': 35, 'role_episode_roots_selected': 8, 'role_episode_roots_rejected': 27, 'role_episode_roots_unexplained': 0, 'pass': True}, 'rejected_eligible_root_count': 27, 'frontier_size_by_hop_depth': {'0_role_episode_roots': 35, '1_leaf_skill_candidates': 165, '2_metric_outcome_candidates': 100, '1_source_fact_candidates': 37}, 'graph_evidence_depth_status': 'judge_grade', 'missing_role_axes': []} |
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
| `x2_competencies_per_category_confidence_nonconstant` | `NOT_OBSERVED` | `PASS` | `True` | {'missing_confidence_category_labels': [], 'unique_selector_confidence_values': [0.813, 0.821, 0.837, 0.841, 0.847, 0.889], 'unique_confidence_values': [0.6091, 0.6532, 0.6756, 0.7185, 0.7768, 0.7785, 0.7909], 'category_count': 8} |
| `x2_competencies_rejected_neighbor_audit_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_ok': True, 'audit_status': 'present', 'candidate_label_count': 35, 'candidate_variant_count': 36, 'selected_count': 8, 'rejected_neighbor_count': 28, 'graph_candidate_receipt_schema_ok': True, 'graph_candidate_conservation_pass': True, 'graph_rejected_candidate_count': 278} |
| `x2_competencies_role_alignment_terms` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_selected_graph_evidence_depth_sufficient` | `NOT_OBSERVED` | `PASS` | `True` | {'status': 'judge_grade', 'summary': 'competencies: 8/8 rich items, 27 unique skills, 16 unique metrics, 100% semantic coverage, 100% axis coverage', 'thin_item_ids': []} |
| `x2_competencies_source_fact_concentration_limit` | `NOT_OBSERVED` | `PASS` | `True` | {'dominant_source_fact_id': 'fact_engineering_platform_001', 'dominant_source_fact_category_share': 0.5, 'dominant_source_fact_category_count': 4, 'category_count': 8} |
| `x2_competencies_term_support_ids_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competencies_visible_terms_svp_agentic_richness` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_bundle_id_required_per_category` | `NOT_OBSERVED` | `PASS` | `True` | all_bound |
| `x2_competency_companion_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_context_used_as_proof': False} |
| `x2_competency_duplicate_variant_absent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_format_category_colon_terms` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_jd_mirroring_within_limit` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_rigor_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | 25 |
| `x2_competency_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_compact_word_count` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_primary_fact_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_primary_fact_unique` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_term_supported` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_competency_terms_canonical_structured` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_default_fid_only_support_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_duplicate_variants_collapsed` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 37, 'violations': []} |
| `x2_gate_rows_are_internally_consistent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_generic_taxonomy_only_category_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_graph_skill_node_ids_required_per_category` | `NOT_OBSERVED` | `PASS` | `True` | all_have_graph_nodes |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 25, 'claims_supported_by_selected_resume_facts': 25, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 25, 'claims_supported_by_selected_resume_facts': 25, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_only_skill_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_briefing_only_skills` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_bullet_format` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_bullet_outcome_restatement` | `NOT_OBSERVED` | `PASS` | `True` | ok |
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
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 37, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | external_openai->real_llm |
| `x2_required_capability_families_covered` | `NOT_OBSERVED` | `FAIL` | `True` | Only 7/8 capability families detected (need 8): ['agentic_platform', 'runtime_governance', 'retrieval_context', 'llmops', 'distributed_infra', 'partner_architecture', 'engineering_leadership']. SVP Engineering competencies must cover Agentic Platform, Runtime Governance, Retrieval Context, LLMOps, Distributed Infra, Productization, Partner Architecture, and Engineering Leadership. |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 25, 'claims_supported_by_selected_resume_facts': 25, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
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
| `openai_chatgpt` | `NOT_OBSERVED` | `4.2/4.0 PASS` | - |

## Section: ibm_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b81b6e2838e4252ffc39bf45` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `cba4bddcdfc1dad0d3997cec` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `d6f7914fcab0c09ca4ad6203` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `021d99b511491e17280b6486` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `ddd0a16078ea6164b9cc1b69` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\raw_model_output.txt` |
| 2 | `deterministic_repair` | `1` | `-` | graph_plan_fact_id_alignment | align_ibm_claim_ledger_from_canonical_facts | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_repair_ledger.json` |
| 3 | `deterministic_repair` | `2` | `-` | surface_fact_backed_metric_tokens_model_dropped | inject_ibm_plan_fact_metric_anchors | `PRE_FINAL_X2` | `NO_CHANGE` | `NOT_REACHED` | `BLOCKED_OR_LEDGER_ONLY` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\section_repair_ledger.json` |
| 4 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x2_gate_outputs.json` |
| 5 | `judge_panel` | `gemini_pro` | `702db4f9e1408635` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x1d_gemini_provider_response_raw_20260809_090547_046.json` |
| 6 | `judge_panel` | `openai_chatgpt` | `b59b078aedad8102` | Employment pool selector: 5 slots, min_score=0.76, threshold=0.72, gate_ok=True | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `0.76/0.72 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x1d_openai_provider_response_raw_20260809_090537_904.json` |
| 7 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\judge_remediation_cycles.json` |
| 8 | `x3_disposition` | `-` | `5a99d9c6983a06b1` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 5} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'afe43974c923915a1a5ef47460f8ae497e23fc9b98779a38e7108cca9f7251b8', 'fec_allowed_fact_ids_digest': 'afe43974c923915a1a5ef47460f8ae497e23fc9b98779a38e7108cca9f7251b8', 'fec_narrowed_from_pool': True} |
| `x2_base_resume_ngram_overlap_ibm` | `NOT_OBSERVED` | `PASS` | `True` | all_below_threshold |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_bullet_seniority_floor` | `NOT_OBSERVED` | `PASS` | `True` | all_pass |
| `x2_bullet_technical_specificity_floor` | `NOT_OBSERVED` | `FAIL` | `True` | bul_ibm_004: no named mechanism/technology in bullet text |
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
| `x2_ibm_bullets_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'ibm_bullets', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'afe43974c923915a1a5ef47460f8ae497e23fc9b98779a38e7108cca9f7251b8', 'canonical_evidence_set_digest': 'afe43974c923915a1a5ef47460f8ae497e23fc9b98779a38e7108cca9f7251b8', 'id_alias_map': {'bul_ibm_001': 'fact_partnerships_gtm_002', 'bul_ibm_002': 'fact_revenue_ops_002', 'bul_ibm_003': 'fact_revenue_ops_005', 'bul_ibm_004': 'fact_revenue_ops_003', 'bul_ibm_005': 'fact_revenue_ops_001'}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 39, 'source_fact_ids_checked': ['bul_ibm_001', 'bul_ibm_002', 'bul_ibm_003', 'bul_ibm_004', 'bul_ibm_005'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 39, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'ibm_bullets'} |
| `x2_ibm_cross_bullet_semantic_overlap_zero` | `NOT_OBSERVED` | `PASS` | `True` | none |
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
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '1ee7cfd54c0485256c918010a03a534239f577adc3f483406349144a76b89015', 'claim_count': 5, 'bound_claim_count': 5, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `0.76/0.72 PASS` | - |

## Section: ey_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `8538b12272eb74d73be0dd36` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b81b6e2838e4252ffc39bf45` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `fd785de756e4475d46254c05` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `a3e5cda09eac678b273f8962` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `e1a9b05732afc23bec605a39` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `8b4298af52120bc560f31693` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `b01c18d35ed4eea1` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x1d_gemini_provider_response_raw_20260809_090706_162.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `11626f3e50b6af19` | Employment pool selector: 3 slots, min_score=0.72, threshold=0.72, gate_ok=False | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `0.72/0.72 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x1d_openai_provider_response_raw_20260809_090656_808.json` |
| 5 | `x3_disposition` | `-` | `1631fc3126e3f25a` | X1D decisive judge failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_bullets\x3_disposition.json` |

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
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '1ee7cfd54c0485256c918010a03a534239f577adc3f483406349144a76b89015', 'claim_count': 3, 'bound_claim_count': 3, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `5.0/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `0.72/0.72 FAIL` | - |

## Section: ibm_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ibm_narrative\x3_disposition.json` |

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

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\sections\ey_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `052754796e5cc5fef255cd82` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9ce19bb2c5709b8b7dda872d` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\x3_disposition.json` |

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
| 1 | `assembly_input` | `0` | `4443d7b2673d59f5` | accepted section snapshots | assemble accepted X3 section outputs | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `ASSEMBLED_RESUME_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\final_resume.json` |
| 2 | `final_x2` | `1` | `4443d7b2673d59f5` | structural and aggregate coherence gates | evaluate final resume release gates | `FINAL_RESUME_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\final_resume_x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\x1d_full_resume_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\modular_r4\final_resume_assembly\full_resume_llm_coherence_review.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
