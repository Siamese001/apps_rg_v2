# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T07:22:01Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `insurtech_bullets, ey_bullets, executive_summary, headline` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=b622dabd89ba343732c8c77407c80b6b56bb1cd25fd658c014a766ad200413c3; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7041` |
| Did resume generation run? | `5 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: insurtech_bullets, ey_bullets, executive_summary, headline` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `insurtech_bullets`: Output contract failure: parsed content or claim ledger did not satisfy section schema.
  - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
  - Evidence: `x2_insurtech_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_display_text_proof_authorized, x2_insurtech_bullets_runtime_real_llm, x2_insurtech_bullets_bullet_count_3, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
    - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
    - `Parser / normalization contract` / `PRIMARY` / `40%`: x2_insurtech_bullets_bullet_count_3: expected exactly 3 bullets observed=0 Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_claim_ledger_claim_text_non_empty: claim_ledger missing or empty claim_text observed=0 Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
    - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_insurtech_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_display_text_proof_authorized, x2_insurtech_bullets_runtime_real_llm, x2_insurtech_bullets_bullet_count_3, x2_resume_graph_claim_binding`. Required work: Attach parser input/output references and failed field names to the gate evidence.
    - `Retry / repair policy` / `LOW_RECOVERY` / `15%`: Retries target the model, while the observed failure is an empty parsed artifact after generation. Evidence: `self_consistency_paths.json, parsed_output.json`. Required work: Allow retry only after parser and claim-ledger contracts prove they can preserve a valid generated payload.
  - Required implementation plan:
    - Trace the lane's canonical output schema from provider prompt to parser to X2 gate input and remove alternate empty or partial shapes.
    - Move required-field and bullet-count validation ahead of X2 so malformed provider responses fail before claim evaluation.
    - Emit claim-ledger rows with source_fact_id and claim_text at generation/parsing time instead of attempting post-hoc repair.
    - Add a fixture that proves malformed provider output is rejected and a compliant provider payload produces the expected ledger rows.
    - Add a CI assertion that the lane cannot emit display content unless the schema and claim-ledger contract is satisfied.
- `ey_bullets`: Output contract failure: parsed content or claim ledger did not satisfy section schema.
  - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
  - Evidence: `x2_ey_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_ey_bullets_display_text_proof_authorized, x2_ey_bullets_runtime_real_llm, x2_ey_bullets_bullet_count_3, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
    - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
    - `Parser / normalization contract` / `PRIMARY` / `40%`: x2_ey_bullets_bullet_count_3: expected exactly 3 bullets observed=0 Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_claim_ledger_claim_text_non_empty: claim_ledger missing or empty claim_text observed=0 Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
    - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_ey_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_ey_bullets_display_text_proof_authorized, x2_ey_bullets_runtime_real_llm, x2_ey_bullets_bullet_count_3, x2_resume_graph_claim_binding`. Required work: Attach parser input/output references and failed field names to the gate evidence.
    - `Retry / repair policy` / `LOW_RECOVERY` / `15%`: Retries target the model, while the observed failure is an empty parsed artifact after generation. Evidence: `self_consistency_paths.json, parsed_output.json`. Required work: Allow retry only after parser and claim-ledger contracts prove they can preserve a valid generated payload.
  - Required implementation plan:
    - Trace the lane's canonical output schema from provider prompt to parser to X2 gate input and remove alternate empty or partial shapes.
    - Move required-field and bullet-count validation ahead of X2 so malformed provider responses fail before claim evaluation.
    - Emit claim-ledger rows with source_fact_id and claim_text at generation/parsing time instead of attempting post-hoc repair.
    - Add a fixture that proves malformed provider output is rejected and a compliant provider payload produces the expected ledger rows.
    - Add a CI assertion that the lane cannot emit display content unless the schema and claim-ledger contract is satisfied.
- `insurtech_narrative`: Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:upstream_not_finalized`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ey_narrative`: Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:upstream_not_finalized`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `executive_summary`: Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.
  - Root cause: The executive-summary final producer path accepted repaired prose before revalidating required brushstroke coverage, row-level attribution density, and non-robotic transition shape.
  - Evidence: `x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
    - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
    - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: x2_executive_summary_synthesis_quality: Output has 0 sentences; executive synthesis requires exactly 6 sentences observed=Output has 0 sentences; executive synthesis requires exactly 6 sentences Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
    - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: x2_exec_summary_allowed_fact_utilization: unused_required_allowed_facts=['fact_engineering_platform_001', 'fact_engineering_platform_002', 'fact_engineering_platform_006', 'metric_unify_22m_ip_led_revenue', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'reb_ibm_devsecops_release_resilience', 'reb_unify_agentic_platform_architecture', 'reb_unify_platform_commercialization_leadership', 'skill_agentic_platform_productization', 'skill_governed_agentic_systems_architecture', 'skill_ibm_devsecops_pipeline_security', 'skill_unify_agentic_human_override_escalation_paths', 'skill_unify_agentic_l0_route_policy_dispatch', 'skill_unify_agentic_replay_key_audit_manifest_design', 'skill_unify_agentic_runtime_proof_bundle_lineage'] observed=unused_required_allowed_facts=['fact_engineering_platform_001', 'fact_engineering_platform_002', 'fact_engineering_platform_006', 'metric_unify_22m_ip_led_revenue', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'reb_ibm_devsecops_release_resilience', 'reb_unify_agentic_platform_architecture', 'reb_unify_platform_commercialization_leadership', 'skill_agentic_platform_productization', 'skill_governed_agentic_systems_architecture', 'skill_ibm_devsecops_pipeline_security', 'skill_unify_agentic_human_override_escalation_paths', 'skill_unify_agentic_l0_route_policy_dispatch', 'skill_unify_agentic_replay_key_audit_manifest_design', 'skill_unify_agentic_runtime_proof_bundle_lineage'] Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
    - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
    - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
  - Required implementation plan:
    - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
    - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
    - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
    - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.
- `headline`: Output contract failure: parsed content or claim ledger did not satisfy section schema.
  - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
  - Evidence: `x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
    - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
    - `Parser / normalization contract` / `PRIMARY` / `40%`: The bullet-count gate observed an empty parsed bullet artifact. Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_headline_claim_ledger_rows_present: claim_ledger must contain dict rows with non-empty source_fact_ids (no fabrication). observed=0 Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
    - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding`. Required work: Attach parser input/output references and failed field names to the gate evidence.
    - `Retry / repair policy` / `LOW_RECOVERY` / `15%`: Retries target the model, while the observed failure is an empty parsed artifact after generation. Evidence: `self_consistency_paths.json, parsed_output.json`. Required work: Allow retry only after parser and claim-ledger contracts prove they can preserve a valid generated payload.
  - Required implementation plan:
    - Trace the lane's canonical output schema from provider prompt to parser to X2 gate input and remove alternate empty or partial shapes.
    - Move required-field and bullet-count validation ahead of X2 so malformed provider responses fail before claim evaluation.
    - Emit claim-ledger rows with source_fact_id and claim_text at generation/parsing time instead of attempting post-hoc repair.
    - Add a fixture that proves malformed provider output is rejected and a compliant provider payload produces the expected ledger rows.
    - Add a CI assertion that the lane cannot emit display content unless the schema and claim-ledger contract is satisfied.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `insurtech_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `insurtech_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `headline` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### insurtech_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_insurtech_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_display_text_proof_authorized, x2_insurtech_bullets_runtime_real_llm, x2_insurtech_bullets_bullet_count_3, x2_resume_graph_claim_binding), so None/None BLOCKED_PROVIDER_UNAVAILABLE and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ey_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_ey_bullets_display_text_proof_authorized, x2_ey_bullets_runtime_real_llm, x2_ey_bullets_bullet_count_3, x2_resume_graph_claim_binding), so None/None BLOCKED_PROVIDER_UNAVAILABLE and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding), so 0.0/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### final_resume_aggregation

The prior passing revision authorized final assembly because every required section, including the executive summary, had already cleared its product checks.

The current final assembly did not fail as an independent writing attempt; it was blocked downstream because the executive summary never became eligible for assembly.

No aggregation retry or aggregation judge could repair that upstream section failure, so the underlying executive-summary retry and X2 evidence remains the controlling root cause.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `upstream_section_authorization`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`


## Recommended Next Move

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: insurtech_bullets, ey_bullets, executive_summary, headline.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/index.md`
- Section forensic RCA: insurtech_bullets: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_bullets.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_bullets.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: insurtech_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/insurtech_narrative.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/executive_summary.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/headline.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry9_20260809/e2e_20260809T071441Z_0e86eeeb/section_failure_forensics/final_resume_aggregation.md`
