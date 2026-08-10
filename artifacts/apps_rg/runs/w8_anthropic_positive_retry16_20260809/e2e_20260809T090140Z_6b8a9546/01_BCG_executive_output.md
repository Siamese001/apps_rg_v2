# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T09:11:23Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3_BLOCK; ibm_bullets:EXECUTED_X3_BLOCK; ey_bullets:EXECUTED_X3_BLOCK; ibm_narrative:upstream_not_finalized; ey_narrative:upstream_not_finalized' schema_ok=False lane_ok=False. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix competencies first-lane execution failure before scheduling downstream lanes. | `x2_required_capability_families_covered, x2_resume_graph_claim_binding` | No downstream lane without upstream authorization. |
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `competencies, ibm_bullets, ey_bullets` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=b81b6e2838e4252ffc39bf45e513fccfcc84a15b4b782746527c176dba187ffb; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7246` |
| Did resume generation run? | `9 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_required_capability_families_covered, x2_resume_graph_claim_binding` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `competencies`: Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
  - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
  - Evidence: `x2_required_capability_families_covered, x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/competencies.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/competencies.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
    - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
    - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
    - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
    - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_required_capability_families_covered, x2_resume_graph_claim_binding`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
  - Required implementation plan:
    - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
    - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
    - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
    - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
- `ibm_bullets`: Deterministic specificity failure: generated text missed required mechanism/technology signal.
  - Root cause: The lane does not bind narrative text to evidence-backed mechanism or technology requirements before deterministic specificity validation.
  - Evidence: `x2_bullet_technical_specificity_floor`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The generated narrative was not constrained to include an evidence-backed mechanism token before deterministic specificity validation.
    - Retry recoverability: `HIGH` - A targeted repair can add a source-backed mechanism or technology token without changing the underlying evidence set.
    - `Generation instruction / output control` / `PRIMARY` / `45%`: x2_bullet_technical_specificity_floor: bul_ibm_004: no named mechanism/technology in bullet text observed=['bul_ibm_004: no named mechanism/technology in bullet text'] Evidence: `x2_narrative_technical_specificity_floor`. Required work: Bind the narrative prompt and repair step to accepted source-backed mechanism vocabulary.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `20%`: The accepted mechanism must be present in both display text and the claim ledger, not only in hidden evidence. Evidence: `claim_ledger.json, text_claim_coverage.json`. Required work: Expose the mechanism token in claim text and source_fact_ids before the specificity gate runs.
    - `Retry / repair policy` / `HIGH_RECOVERY` / `25%`: The lane had supported content but missed a deterministic token, so gate-aware text repair is the correct retry shape. Evidence: `x2_narrative_technical_specificity_floor, section_repair_ledger.json`. Required work: Trigger a targeted rewrite that only inserts an evidence-backed mechanism token.
    - `Validation / gate precision` / `DETECTION` / `10%`: The gate names the missing token class but should also emit the accepted vocabulary and evidence source used for repair. Evidence: `x2_gate_outputs.json`. Required work: Include accepted mechanism vocabulary and source-fact anchors in the gate receipt.
  - Required implementation plan:
    - Define the accepted mechanism and technology vocabulary for the lane from source evidence, not from generic resume keywords.
    - Require each narrative sentence that makes a capability claim to bind to at least one evidence-backed mechanism fact.
    - Update the deterministic specificity gate to check evidence-bound mechanisms in the claim ledger before accepting display text.
    - Add a regression fixture with one generic narrative rejection and one mechanism-bound narrative acceptance.
- `ey_bullets`: X1D decisive judge failure: model-backed judge rejected section product quality.
  - Root cause: The lane published judge-visible narrative text after normalizing the provider payload through a lossy claim-ledger path that dropped source_fact_ids needed to support material claims.
  - Evidence: `OpenAI ChatGPT \| gpt-5.6-sol \| MODEL_BACKED_FAIL \| score=0.72/0.72`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The section was generated, parsed, and X2-clean, but the published claim ledger lost source-fact bindings that X1D required for judge-visible material claims.
    - Retry recoverability: `LOW_UNTIL_LEDGER_FIX` - Blind regeneration can return a valid parsed claim ledger again, but the same lossy normalization path will keep dropping support before X1D.
    - `Claim ledger normalization` / `PRIMARY` / `45%`: OpenAI ChatGPT | gpt-5.6-sol | MODEL_BACKED_FAIL | score=0.72/0.72 Evidence: `parsed_output.json, claim_ledger.json, x1d_llm_judge_outputs.json`. Required work: Preserve valid source_fact_ids from parsed narrative claim_ledger rows when publishing the single-sentence role-episode ledger.
    - `Narrative source binding` / `CONTRIBUTING` / `25%`: Narrative material phrases such as insurance operations, model risk, and traceable controls must bind to selected role-episode facts before judge review. Evidence: `selected_fact_plan.json, role_episode_lane.py`. Required work: Add deterministic phrase-to-fact reconciliation for EY narrative material claims within the allowed graph packet.
    - `X1D authorization policy` / `DETECTION` / `20%`: X2 PASS and product PASS were not enough because the model-backed judge rejected factual support. Evidence: `x3_disposition.json, x1d_llm_judge_outputs.json`. Required work: Keep X3 blocked on decisive factual-support judge failures and surface the judge finding as the primary RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: The fix belongs at the parser/ledger boundary, not in downstream rerun scheduling or final assembly. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Rerun only after the narrative ledger preservation fixture and mandatory-RCA fixture pass.
  - Required implementation plan:
    - Preserve valid source_fact_ids from parsed narrative claim_ledger rows when normalizing role-episode narrative output.
    - Add source-binding patterns for material EY insurance, ERM, CCAR, regulatory analytics, and capital/solvency claims.
    - Keep X2 PASS insufficient for authorization when X1D factual-support judges reject the published claim ledger.
    - Add a regression fixture using the live EY narrative where insurance operations must cite reb_ey_insurance_core_modernization.
- `ibm_narrative`: Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:upstream_not_finalized`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=True`
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
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_narrative.md`
  - Evidence: `forensics_complete=True`
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

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `competencies` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `ibm_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> PASS/X3_BLOCK` | `False` |
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_required_capability_families_covered, x2_resume_graph_claim_binding), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_bullet_technical_specificity_floor), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\apps_research\runs\r-0bfffce086e7b821a6da65eb\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### final_resume_aggregation

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.

The aggregate panel ran and recorded - EVIDENCE_NOT_RECORDED; the required two-of-two model-backed quorum was not met.

The controlling product defect is aggregate coherence, not upstream section eligibility: the failed aggregate gate is recorded in the final-resume review artifact.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `aggregate_coherence_quorum`
- Code cause status: `AGGREGATE_GATE_ISOLATED`


## Recommended Next Move

1. Resolve P0: Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_required_capability_families_covered, x2_resume_graph_claim_binding.
2. Resolve the remaining 3 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry16_20260809\e2e_20260809T090140Z_6b8a9546\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/competencies.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/competencies.md`
- Section forensic RCA: ibm_bullets: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_bullets.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_bullets.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry16_20260809/e2e_20260809T090140Z_6b8a9546/section_failure_forensics/final_resume_aggregation.md`
