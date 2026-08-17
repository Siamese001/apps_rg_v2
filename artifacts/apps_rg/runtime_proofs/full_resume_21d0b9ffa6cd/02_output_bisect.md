# apps_rg Output Bisect

## Section: headline

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\apps_research\runs\bridge_rg_research_bridge_7cee9beb_067b1ade-e50d-4580-8886-bf966939d703\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_executive_abstraction_floor), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9acead875de19b1259d7f453` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `87f153289cd56b3ed4678020` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `7007d1c94751961bbca210c2` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `9edf5e9a2029f45c4453c1df` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `fb6535f316fd5084bda14ae3` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `f21fb06a5c9b7854d8aa26b4` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `a01ea986a13de8ab70ea9de2` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `fa574a2f48d669b71b52fd54` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `855b899b0872b433898fca20` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `fa5cd6806bd89409` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `5.0/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x1d_gemini_provider_response_raw_20260817_020124_507.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `fa5cd6806bd89409` | Formatting, prefix, and 12-word length comply.; All three positioning claims have allowed factual support.; The segments provide distinct alliance, runtime-governance, and commercial signals.; Noun-stack phrasing slightly reduces natural executive cadence. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.2/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x1d_openai_provider_response_raw_20260817_020145_925.json` |
| 5 | `judge_retry_status` | `-` | `-` | all configured judges passed | no judge retry required | `JUDGE_REMEDIATION` | `NOT_NEEDED` | `NOT_NEEDED_ALL_JUDGES_PASSED` | `NO_RETRY` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\judge_remediation_cycles.json` |
| 6 | `x3_disposition` | `-` | `21137856f804225e` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\lanes\headline\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': 'b09f7cf3d2038c63bdd870fdfb0b96970b9d7ebe2810c902f03df2052d6c4c4d', 'fec_allowed_fact_ids_digest': 'b09f7cf3d2038c63bdd870fdfb0b96970b9d7ebe2810c902f03df2052d6c4c4d', 'fec_narrowed_from_pool': True} |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 3, 'violations': []} |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 14, 'violations': []} |
| `x2_headline_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'headline', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': 'ad5d71e715ba4f751a1cbd982f63e376c0b895578bfb8af9a36063d12aaf9f31', 'canonical_evidence_set_digest': 'ad5d71e715ba4f751a1cbd982f63e376c0b895578bfb8af9a36063d12aaf9f31', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 14, 'source_fact_ids_checked': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': None, 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 14, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'headline'} |
| `x2_headline_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_base_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_briefing_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'Partner alliance co-sell execution paired with governed runtime discipline and quota-driven solution leadership, ranked for relevance to a partner-facing applied AI architecture role.', 'anti_stuffing_check': "No JD phrases (e.g. 'Applied AI Architecture', 'Partnerships') copied verbatim; segments built from literal candidate fact text only."} |
| `x2_headline_claim_ledger_no_silent_row_drop` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_claim_ledger_rows_present` | `NOT_OBSERVED` | `PASS` | `True` | 3 |
| `x2_headline_claim_ledger_segment_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | {'matched_segments': ['alliance co-sell motions', 'quota aligned solution pursuits', 'runtime governance telemetry'], 'expected_segments': ['Alliance Co-Sell Motions', 'Runtime Governance Telemetry', 'Quota Aligned Solution Pursuits'], 'row_count': 3} |
| `x2_headline_companion_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'Partner alliance co-sell execution paired with governed runtime discipline and quota-driven solution leadership, ranked for relevance to a partner-facing applied AI architecture role.', 'anti_stuffing_check': "No JD phrases (e.g. 'Applied AI Architecture', 'Partnerships') copied verbatim; segments built from literal candidate fact text only."} |
| `x2_headline_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_e0_ngram_overlap_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_exactly_one_line` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_executive_abstraction_floor` | `NOT_OBSERVED` | `FAIL` | `True` | Each headline segment must express executive scope such as platform, architecture, governance, ecosystem, commercialization, or regulated systems. |
| `x2_headline_executive_length` | `NOT_OBSERVED` | `PASS` | `True` | 107 |
| `x2_headline_generic_it_strategy_demote_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_governance_or_regulated_ai_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance'] |
| `x2_headline_graph_skill_node_ids_required` | `NOT_OBSERVED` | `PASS` | `True` | ['skill_context_engineering', 'skill_partner_pnl_oversight', 'skill_sr_w12_hyperscaler_alliance_co_sell'] |
| `x2_headline_jd_context_not_proof` | `NOT_OBSERVED` | `PASS` | `True` | {'targeting_only': True, 'jd_used_as_proof': False, 'briefing_used_as_proof': False, 'companion_used_as_proof': False, 'selected_theme': 'Partner alliance co-sell execution paired with governed runtime discipline and quota-driven solution leadership, ranked for relevance to a partner-facing applied AI architecture role.', 'anti_stuffing_check': "No JD phrases (e.g. 'Applied AI Architecture', 'Partnerships') copied verbatim; segments built from literal candidate fact text only."} |
| `x2_headline_jd_only_phrase_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_currency_percent_literals` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_digit_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_hype_markers` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_headline_no_keyword_stuffing_heuristic` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_metrics` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_narrowing_it_labels` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_standalone_vendor_architecture` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Alliance Co-Sell Motions', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Runtime Governance Telemetry', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Quota Aligned Solution Pursuits', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Quota Aligned Solution Pursuits'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_no_title_inflation` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_unsupported_employer_names` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_pipe_four_segments` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_platform_or_runtime_signal_required` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance'] |
| `x2_headline_positioning_bundle_id_required` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'] |
| `x2_headline_positioning_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'mode': 'headline_positioning_bundle_required'} |
| `x2_headline_positioning_family_preserved` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance', 'partner_applied_ai_architecture'] |
| `x2_headline_prompt_reasoning_receipt_clean` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_raw_model_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_segments_quality` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_selected_fact_plan_matches_ledger` | `NOT_OBSERVED` | `PASS` | `True` | {'required_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'ledger_union': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'cited_but_not_selected': []} |
| `x2_headline_self_check_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'runtime': {'word_count': 12, 'segment_count': 4, 'separator_count': 3, 'word_count_in_range': True, 'fixed_prefix': True, 'no_metrics': True, 'no_employer_names': True, 'no_company_names': True}, 'model': {'fixed_prefix': True, 'segment_count': 4, 'separator_count': 3, 'word_count': 12, 'word_count_in_range': True, 'no_metrics': True, 'no_employer_names': True, 'no_company_names': True}} |
| `x2_headline_seniority_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | SVP Engineering |
| `x2_headline_source_fact_or_graph_lineage_required` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'] |
| `x2_headline_source_supported` | `NOT_OBSERVED` | `PASS` | `True` | ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'] |
| `x2_headline_svp_engineering_seniority_required` | `NOT_OBSERVED` | `PASS` | `True` | SVP Engineering |
| `x2_headline_technical_specificity_floor_met` | `NOT_OBSERVED` | `PASS` | `True` | ['runtime_governance', 'partner_applied_ai_architecture'] |
| `x2_headline_text_claim_coverage_integrity` | `NOT_OBSERVED` | `PASS` | `True` | [{'segment_index': 2, 'segment_text': 'Alliance Co-Sell Motions', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance']}, {'segment_index': 3, 'segment_text': 'Runtime Governance Telemetry', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance']}, {'segment_index': 4, 'segment_text': 'Quota Aligned Solution Pursuits', 'pass': True, 'matching_claim_count': 1, 'source_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance']}] |
| `x2_headline_vendor_terms_proof_only` | `NOT_OBSERVED` | `PASS` | `True` | {'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Alliance Co-Sell Motions', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Runtime Governance Telemetry', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Quota Aligned Solution Pursuits', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Quota Aligned Solution Pursuits'], 'vendor_terms_without_executive_abstraction': []} |
| `x2_headline_word_count_10_to_13` | `NOT_OBSERVED` | `PASS` | `True` | 12 |
| `x2_headline_xyz_literal_grounding` | `NOT_OBSERVED` | `PASS` | `True` | {'segments': [{'segment': 'Alliance Co-Sell Motions', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'evidence': [{'fact_id': 'reb_ibm_aws_alliance_partner_cosell_gtm', 'shared_tokens': ['alliance', 'co-sell', 'motion', 'motions'], 'fact_text_known': True}, {'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': ['motion', 'motions'], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': [], 'fact_text_known': True}], 'ungrounded_tokens': [], 'grounded_tokens': ['alliance', 'co-sell', 'motion', 'motions'], 'majority_grounded': True}, {'segment': 'Runtime Governance Telemetry', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'evidence': [{'fact_id': 'reb_ibm_aws_alliance_partner_cosell_gtm', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': ['telemetry'], 'fact_text_known': True}], 'ungrounded_tokens': [], 'grounded_tokens': ['telemetry'], 'majority_grounded': True}, {'segment': 'Quota Aligned Solution Pursuits', 'ground_pass': True, 'cited_fact_ids': ['reb_ibm_aws_alliance_partner_cosell_gtm', 'reb_ibm_revenue_sales_target_execution', 'reb_unify_runtime_reliability_governance'], 'evidence': [{'fact_id': 'reb_ibm_aws_alliance_partner_cosell_gtm', 'shared_tokens': [], 'fact_text_known': True}, {'fact_id': 'reb_ibm_revenue_sales_target_execution', 'shared_tokens': ['pursuit', 'pursuits', 'solution'], 'fact_text_known': True}, {'fact_id': 'reb_unify_runtime_reliability_governance', 'shared_tokens': [], 'fact_text_known': True}], 'ungrounded_tokens': ['aligned', 'quota'], 'grounded_tokens': ['pursuit', 'pursuits', 'solution'], 'majority_grounded': True}], 'checked': 3} |
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
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 14, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider mismatch. |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `PASS` | `True` | {'allocation_plan_digest': '86b518ae7a25da010c2bb8999c5fd5936c1090c9f703aa825124188c8937dfda', 'claim_count': 3, 'bound_claim_count': 3, 'binding_coverage': 1.0, 'metric_exactness_pass': True, 'orphan_allocation_claim_unit_ids': [], 'failure_reasons': []} |
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
| `openai_chatgpt` | `NOT_OBSERVED` | `4.2/4.0 PASS` | - |

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
| 1 | `u0_ingress` | `NOT_OBSERVED` | `9acead875de19b1259d7f453` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `87f153289cd56b3ed4678020` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\x3_disposition.json` |

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
| 1 | `assembly_input` | `0` | `e5c92626a571babf` | accepted section snapshots | assemble accepted X3 section outputs | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `ASSEMBLED_RESUME_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\final_resume.json` |
| 2 | `final_x2` | `1` | `e5c92626a571babf` | structural and aggregate coherence gates | evaluate final resume release gates | `FINAL_RESUME_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\final_resume_x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\x1d_full_resume_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_21d0b9ffa6cd\modular_r4\final_resume_assembly\full_resume_llm_coherence_review.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
