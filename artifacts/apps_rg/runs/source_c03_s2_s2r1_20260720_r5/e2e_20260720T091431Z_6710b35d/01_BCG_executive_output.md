# BCG Executive Output - apps_rg Run

Generated: `2026-07-20T09:15:47Z`
Run root: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix competencies first-lane execution failure before scheduling downstream lanes. | `x2_competencies_required_proof_present, x2_resume_graph_claim_binding` | No downstream lane without upstream authorization. |
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `competencies` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |
| `P1` | Add dependency-token reporting for every PHASE1_NO_RUN_DIR lane. | `PHASE1_NO_RUN_DIR lanes: ibm_bullets, insurtech_bullets, ey_bullets, unify_narrative, ibm_narrative, insurtech_narrative, ey_narrative, executive_summary, headline` | Show exact upstream repair order. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=29f2164b2f878eab64e5bbad28ca0e12c6617cd0cf494a4a6f906895a0ea8966; ref=C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; target=Unify Consulting / SVP Technical Pre-Sales, Enterprise Cloud & AI Solutions; briefing_text_chars=5982` |
| Did resume generation run? | `0 REAL_LLM section(s)` |
| Source X3 decision | `X3A` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_competencies_required_proof_present, x2_resume_graph_claim_binding` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `competencies`: Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
  - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
  - Evidence: `x2_competencies_required_proof_present, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/competencies.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/competencies.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
    - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
    - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
    - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
    - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_competencies_required_proof_present, x2_resume_graph_claim_binding`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
  - Required implementation plan:
    - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
    - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
    - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
    - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
- `unify_bullets`: Pre-run dependency blocked execution: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt|missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:EXECUTED_X3A`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt|missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ibm_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `insurtech_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ey_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `unify_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'unify_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'unify_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ibm_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ibm_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `insurtech_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'insurtech_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ey_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'ey_narrative' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `executive_summary`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'executive_summary' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'executive_summary' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `headline`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'headline' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED|missing_pointer:no resolvable run_dir pointer for lane 'headline' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\modular_r4\sections Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `competencies` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `unify_bullets` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:EXECUTED_X3A` | `False` |
| `ibm_bullets` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `insurtech_bullets` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `unify_narrative` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `insurtech_narrative` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `headline` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `1375bf16a4d7774481aceb5594b7b7b924362e01` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_required_proof_present, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\apps_research\runs\r-5682110b42f68916f5f2fa80\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

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

1. Resolve P0: Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_competencies_required_proof_present, x2_resume_graph_claim_binding.
2. Resolve the remaining 3 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\source_c03_s2_s2r1_20260720_r5\e2e_20260720T091431Z_6710b35d\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/index.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/competencies.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/competencies.md`
- Section forensic RCA: unify_bullets: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_bullets.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_bullets.md`
- Section forensic RCA: ibm_bullets: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_bullets.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_bullets.md`
- Section forensic RCA: insurtech_bullets: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_bullets.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_bullets.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: unify_narrative: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_narrative.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/unify_narrative.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: insurtech_narrative: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_narrative.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/insurtech_narrative.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/executive_summary.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/headline.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/source_c03_s2_s2r1_20260720_r5/e2e_20260720T091431Z_6710b35d/section_failure_forensics/final_resume_aggregation.md`
