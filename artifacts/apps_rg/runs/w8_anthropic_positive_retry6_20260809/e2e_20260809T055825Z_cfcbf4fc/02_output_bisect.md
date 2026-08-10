# apps_rg Output Bisect

## Section: ibm_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ibm_narrative_claim_theme_coverage), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `4741da18ffd0ebae8370afd8` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `657aac1fc7a3bc2107e98022` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `3fe5f7d6e1c422194eef8951` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `a560554c492e57bc73a0bd42` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `138837eddee39105e94c85fb` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `ec9ff1bcb8bb24cf0545a59f` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `45ad40457e16eea9091b4ba6` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `b148e36b011bdce0` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x1d_gemini_provider_response_raw_20260809_060641_564.json` |
| 4 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\judge_remediation_cycles.json` |
| 5 | `x3_disposition` | `-` | `0e91f48bacb7a551` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\ibm_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 5} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '30c7fa712daefec2cd34ba879c41ccf689b401e867275ee2a0196eedd15a3352', 'fec_allowed_fact_ids_digest': '30c7fa712daefec2cd34ba879c41ccf689b401e867275ee2a0196eedd15a3352', 'fec_narrowed_from_pool': True} |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | all_rows_non_empty |
| `x2_claim_ledger_source_fact_ids_allow_list` | `NOT_OBSERVED` | `PASS` | `True` | all_tokens_in_allowed_fact_ids |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 2, 'violations': []} |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 33, 'violations': []} |
| `x2_ibm_narrative_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'ibm_narrative', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'c6ad44a0060bc61518655076151efc6003af70bd661e5dfc3c594fbbdfd75282', 'canonical_evidence_set_digest': 'c6ad44a0060bc61518655076151efc6003af70bd661e5dfc3c594fbbdfd75282', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 36, 'source_fact_ids_checked': ['bul_ibm_001', 'bul_ibm_002'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 36, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'ibm_narrative'} |
| `x2_ibm_narrative_bullet_overlap_threshold` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_claim_ledger_clause_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | {'reason': 'ok', 'ledger_rows': 2} |
| `x2_ibm_narrative_claim_theme_coverage` | `NOT_OBSERVED` | `FAIL` | `True` | narrative_sentence material themes require matching bul_ibm_* in claim_ledger union; missing: ['unsupported_companion_theme:regulated_financial'] |
| `x2_ibm_narrative_exactly_one_sentence` | `NOT_OBSERVED` | `PASS` | `True` | Must be exactly one sentence. |
| `x2_ibm_narrative_exactly_one_sentence_mechanical` | `NOT_OBSERVED` | `PASS` | `True` | single sentence required |
| `x2_ibm_narrative_forbidden_opener` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_hold_metric_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_ibm_only_fact_scope` | `NOT_OBSERVED` | `PASS` | `True` | Non-IBM fact scope in payload. |
| `x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets` | `NOT_OBSERVED` | `PASS` | `True` | {'mechanisms': ['aws', 'bi'], 'cited_companion_ids': ['bul_ibm_001', 'bul_ibm_002'], 'unsupported_mechanisms': []} |
| `x2_ibm_narrative_metric_cap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ibm_narrative_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | Candidate name must not appear in the role narrative sentence. |
| `x2_ibm_narrative_no_meta_disclaimer_in_display` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_requires_finalized_bullets` | `NOT_OBSERVED` | `PASS` | `True` | IBM narrative must run after ACCEPTED_FINALIZED IBM bullets when companion-aware. |
| `x2_ibm_narrative_role_episode_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | {'change_log_bundle_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_presales_solution_engineering', 'reb_ibm_data_modeling_bi_decision_support'], 'pool_bundle_ids': ['reb_ibm_aws_modernization_architecture', 'reb_ibm_cognitive_business_decision_support', 'reb_ibm_presales_solution_engineering', 'reb_ibm_offering_accelerator_management', 'reb_ibm_revenue_sales_target_execution', 'reb_ibm_nlp_ml_decision_support']} |
| `x2_ibm_narrative_role_episode_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'flat_skill_only': False} |
| `x2_ibm_narrative_source_supported` | `NOT_OBSERVED` | `PASS` | `True` | claim_ledger must map to IBM bullet facts only. |
| `x2_ibm_narrative_weak_resume_jargon_phrases` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_ibm_narrative_word_budget` | `NOT_OBSERVED` | `PASS` | `True` | {'word_count': 33, 'char_len': 300} |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 2, 'claims_supported_by_selected_resume_facts': 2, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 2, 'claims_supported_by_selected_resume_facts': 2, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_base_prose_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_narrative_no_consulting_language` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_narrative_not_bullet_recap` | `NOT_OBSERVED` | `PASS` | `True` | {'max_5gram_overlap': 0.0, 'est_shared_ngrams': 0} |
| `x2_narrative_seniority_floor` | `NOT_OBSERVED` | `PASS` | `True` | {'strong_verbs': ['led', 'operationalized'], 'authority': ['regulated', 'enterprise', 'architecture'], 'issues': []} |
| `x2_narrative_technical_specificity_floor` | `NOT_OBSERVED` | `PASS` | `True` | ['aws', 'bi'] |
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
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '32866090ae2d4a79dc4b301f6fecf82b63049014baf9e9040b4fe02fcf7cbc79', 'claim_count': 2, 'bound_claim_count': 2, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 2 pre-judge repair attempt(s), but DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis'; it reverted to its first candidate, the final deterministic check still failed (x2_resume_graph_claim_binding), so 4.8/4.0 MODEL_BACKED_PASS and the resume remained blocked.

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `4741da18ffd0ebae8370afd8` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `657aac1fc7a3bc2107e98022` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `3fe5f7d6e1c422194eef8951` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `4466d513af4564d54f218bf6` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `3e1aac62173b2ebd9acee716` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `b1bca21db29cc99d95ceb2d0` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `8c2ce8925970bb9811ffc54e` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `b03b847f49adeb4f9dfb273b` | `False` | `CAUSAL` | The current repair loop exhausted its attempts with a failing defect still present and reverted to the first candidate. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `8d21d81991aaa3892f8039a5` | `False` | `CAUSAL` | Current deterministic finalization changed the published text before full X2 evaluation. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `ce0f5db3e3c78999b8fc39a9` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `5b9d5c658aa82b540af795cc` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK_FINAL_MATERIALI` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `8c2ce8925970bb98` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis' | dispatch provider generation | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `REPAIR_TRIGGERED` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 2 | `pre_judge_synthesis_retry` | `1` | `083be03e767e49bf` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis' | provider retry synthesis_regen-00-01-fb15ae5f | `PRE_X2_SYNTHESIS_SHAPE` | `FAIL` | `NOT_REACHED_PRE_X2` | `ADVANCED_AS_IMPROVEMENT` | `MONOTONIC_IMPROVEMENT_ONLY` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 3 | `pre_judge_synthesis_retry` | `2` | `8c2ce8925970bb98` | DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis' | provider retry synthesis_regen-00-02-29c9e087 | `PRE_X2_SYNTHESIS_SHAPE` | `PASS` | `NOT_REACHED_PRE_X2` | `ADVANCED_TO_X2` | `FULL_PRE_X2_SHAPE_PASS` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 4 | `deterministic_repair` | `1` | `-` | cross_fact_display_conflation:too_many_source_fact_ids_in_one_sentence; DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis' | synthesis_regen | `PRE_FINAL_X2` | `MUTATED` | `NOT_REACHED` | `REPLACED_L2` | `DETERMINISTIC_REWRITE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\section_repair_ledger.json` |
| 5 | `final_x2` | `2` | `8c2ce8925970bb98` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 6 | `judge_panel` | `gemini_pro` | `d7c12f0057aa4fcc` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.8/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x1d_gemini_provider_response_raw_20260809_060852_636.json` |
| 7 | `judge_panel` | `openai_chatgpt` | `d7c12f0057aa4fcc` | Strong governed-platform synthesis with a supported $22M commercialization outcome.; Judge packet omits the display override for fact_engineering_platform_002, preventing full parity verification. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.5/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x1d_openai_provider_response_raw_20260809_060910_658.json` |
| 8 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\judge_remediation_cycles.json` |
| 9 | `x3_disposition` | `-` | `8c2ce8925970bb98` | REAL_LLM output, X2 pass, all X1D judges model-backed pass, product quality PASS. | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\executive_summary\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_PROVIDER_MODEL_provider_stub_transport_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '0d7b9a2b79948e1403b13cef35fe79e1d133e726b432759faa4df84e4d41178b', 'fec_allowed_fact_ids_digest': '0d7b9a2b79948e1403b13cef35fe79e1d133e726b432759faa4df84e4d41178b', 'fec_narrowed_from_pool': True} |
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
| `x2_executive_summary_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'executive_summary', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '259c467c9f7cd61dc92a705aaae09795c5d32f5640bde072fe8a723311103a07', 'canonical_evidence_set_digest': '259c467c9f7cd61dc92a705aaae09795c5d32f5640bde072fe8a723311103a07', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 17, 'source_fact_ids_checked': ['reb_ibm_devsecops_release_resilience', 'reb_unify_agentic_platform_architecture', 'metric_unify_policy_gated_agent_execution_surface', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'fact_engineering_platform_002', 'reb_unify_platform_commercialization_leadership', 'skill_agentic_platform_productization', 'skill_unify_agentic_human_override_escalation_paths', 'skill_unify_agentic_runtime_proof_bundle_lineage', 'metric_unify_22m_ip_led_revenue', 'fact_engineering_platform_001', 'fact_engineering_platform_006'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 17, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'executive_summary'} |
| `x2_executive_summary_synthesis_quality` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 17, 'violations': []} |
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
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 17, 'violations': []} |
| `x2_prompt_hash_known` | `NOT_OBSERVED` | `PASS` | `True` | 61169a88a29c720a |
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
| `x2_x1d_judge_packet_hash_uniform` | `NOT_OBSERVED` | `PASS` | `True` | ['d7c12f0057aa4fcc'] |
| `x2_x1d_raw_responses_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | - |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `4.8/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `4.5/4.0 PASS` | - |

## Section: headline

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_executive_abstraction_floor, x2_headline_technical_specificity_floor_met), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `4741da18ffd0ebae8370afd8` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `657aac1fc7a3bc2107e98022` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `3fe5f7d6e1c422194eef8951` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `c66e948abafb68ccb7b7f46f` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `ea3343c6197a6b9fa744564d` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `82840892b07f88148a953193` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `21056cdb4b5eb282fa61bc16` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `fab853a9a4dec70c` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x1d_gemini_provider_response_raw_20260809_061013_326.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `fab853a9a4dec70c` | X and Z read as compressed keyword stacks rather than natural executive positioning.; The parallel three-word segments create conspicuously machine-generated cadence.; Runtime governance and context evaluation signals are insufficiently differentiated for a skeptical TA screen. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `3.4/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x1d_openai_provider_response_raw_20260809_061031_054.json` |
| 5 | `x3_disposition` | `-` | `c0fda75ac8bc4fec` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\sections\headline\x3_disposition.json` |

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
| `x2_headline_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'headline', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'c6456093488c29d016b6d160e7fb235e624a2aa084d1f88219115fd3317deffb', 'canonical_evidence_set_digest': 'c6456093488c29d016b6d160e7fb235e624a2aa084d1f88219115fd3317deffb', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 6, 'source_fact_ids_checked': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 6, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'headline'} |
| `x2_headline_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_base_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_briefing_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'runtime governance paired with enterprise pursuit ownership and evaluation-driven context engineering', 'anti_stuffing_check': 'no JD/briefing phrases lifted; segments built from cited claim_text nouns only'} |
| `x2_headline_claim_ledger_no_silent_row_drop` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_claim_ledger_rows_present` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_headline_claim_ledger_segment_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | {'matched_segments': ['client portfolio expansion', 'context engineering evaluation', 'runtime governance telemetry'], 'expected_segments': ['Runtime Governance Telemetry', 'Client Portfolio Expansion', 'Context Engineering Evaluation'], 'row_count': 3} |
| `x2_headline_companion_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'runtime governance paired with enterprise pursuit ownership and evaluation-driven context engineering', 'anti_stuffing_check': 'no JD/briefing phrases lifted; segments built from cited claim_text nouns only'} |
| `x2_headline_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_e0_ngram_overlap_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_exactly_one_line` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_executive_abstraction_floor` | `NOT_OBSERVED` | `FAIL` | `True` | Each headline segment must express executive scope such as platform, architecture, governance, ecosystem, commercialization, or regulated systems. |
| `x2_headline_executive_length` | `NOT_OBSERVED` | `PASS` | `True` | 108 |
| `x2_headline_generic_it_strategy_demote_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_governance_or_regulated_ai_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance'] |
| `x2_headline_graph_skill_node_ids_required` | `NOT_OBSERVED` | `PASS` | `True` | ['skill_context_engineering', 'skill_partner_pnl_oversight'] |
| `x2_headline_jd_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'runtime governance paired with enterprise pursuit ownership and evaluation-driven context engineering', 'anti_stuffing_check': 'no JD/briefing phrases lifted; segments built from cited claim_text nouns only'} |
| `x2_headline_jd_only_phrase_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_currency_percent_literals` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_digit_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_hype_markers` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_headline_no_keyword_stuffing_heuristic` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_metrics` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_narrowing_it_labels` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_standalone_vendor_architecture` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Runtime Governance Telemetry', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Client Portfolio Expansion', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Context Engineering Evaluation', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Client Portfolio Expansion', 'Context Engineering Evaluation'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_no_title_inflation` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_unsupported_employer_names` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_pipe_four_segments` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_platform_or_runtime_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance'] |
| `x2_headline_positioning_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'] |
| `x2_headline_positioning_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'mode': 'headline_positioning_bundle_required'} |
| `x2_headline_positioning_family_preserved` | `NOT_OBSERVED` | `PASS` | `True` | Only 1 positioning families detected (need 2): ['runtime_governance']. Headline must preserve SVP Engineering positioning families (Agentic AI Platforms, Distributed AI Infrastructure, Runtime Governance, etc.) |
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
| `x2_headline_technical_specificity_floor_met` | `NOT_OBSERVED` | `FAIL` | `True` | Only 1 positioning families detected (need 2): ['runtime_governance']. Headline must preserve SVP Engineering positioning families (Agentic AI Platforms, Distributed AI Infrastructure, Runtime Governance, etc.) |
| `x2_headline_text_claim_coverage_integrity` | `NOT_OBSERVED` | `PASS` | `True` | [{'segment_index': 2, 'segment_text': 'Runtime Governance Telemetry', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}, {'segment_index': 3, 'segment_text': 'Client Portfolio Expansion', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}, {'segment_index': 4, 'segment_text': 'Context Engineering Evaluation', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight']}] |
| `x2_headline_vendor_terms_proof_only` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Runtime Governance Telemetry', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Client Portfolio Expansion', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Context Engineering Evaluation', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Client Portfolio Expansion', 'Context Engineering Evaluation'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_word_count_10_to_13` | `NOT_OBSERVED` | `PASS` | `True` | 11 |
| `x2_headline_xyz_literal_grounding` | `NOT_OBSERVED` | `PASS` | `True` | {'segments': [{'segment': 'Runtime Governance Telemetry', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'evidence': [{'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': ['telemetry'], 'fact_text_known': True}, {'fact_id': 'skill_context_engineering', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'skill_partner_pnl_oversight', 'shared_tokens': [], 'fact_text_known': True}], 'ungrounded_tokens': [], 'grounded_tokens': ['telemetry'], 'majority_grounded': True}, {'segment': 'Client Portfolio Expansion', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'evidence': [{'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': ['client', 'expansion', 'portfolio'], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'skill_context_engineering', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'skill_partner_pnl_oversight', 'shared_tokens': [], 'fact_text_known': True}], 'ungrounded_tokens': [], 'grounded_tokens': ['client', 'expansion', 'portfolio'], 'majority_grounded': True}, {'segment': 'Context Engineering Evaluation', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance', 'skill_context_engineering', 'skill_partner_pnl_oversight'], 'evidence': [{'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': ['evaluation'], 'fact_text_known': True}, {'fact_id': 'skill_context_engineering', 'shared_tokens': ['context'], 'fact_text_known': True}, {'fact_id': 'skill_partner_pnl_oversight', 'shared_tokens': [], 'fact_text_known': True}], 'ungrounded_tokens': [], 'grounded_tokens': ['context', 'evaluation'], 'majority_grounded': True}], 'checked': 3} |
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
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '32866090ae2d4a79dc4b301f6fecf82b63049014baf9e9040b4fe02fcf7cbc79', 'claim_count': 3, 'bound_claim_count': 3, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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
| `openai_chatgpt` | `NOT_OBSERVED` | `3.4/4.0 FAIL` | - |

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `4741da18ffd0ebae8370afd8` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `657aac1fc7a3bc2107e98022` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x3_disposition.json` |

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
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\modular_r4\final_resume_assembly\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
