# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T09:42:51Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:competencies:EXECUTED_X3_BLOCK' schema_ok=False lane_ok=False. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix competencies first-lane execution failure before scheduling downstream lanes. | `x2_competencies_visible_terms_svp_agentic_richness` | No downstream lane without upstream authorization. |
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `competencies` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=366f8981ed5b3e141f77f80c4478c10f4cfa1a73a9776ec942b6a0d767bd5f06; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\apps_research\runs\r-42979485e99f33e36aab853a\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7961` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_competencies_visible_terms_svp_agentic_richness` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `competencies`: Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
  - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
  - Evidence: `x2_competencies_visible_terms_svp_agentic_richness`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/competencies.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/competencies.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
    - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
    - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
    - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
    - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: `x2_competencies_visible_terms_svp_agentic_richness`. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
  - Required implementation plan:
    - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
    - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
    - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
    - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `competencies` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\apps_research\runs\r-42979485e99f33e36aab853a\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_competencies_visible_terms_svp_agentic_richness), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

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

1. Resolve P0: Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: x2_competencies_visible_terms_svp_agentic_richness.
2. Resolve the remaining 3 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry18_20260809\e2e_20260809T093313Z_b9e01dd6\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/competencies.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/competencies.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry18_20260809/e2e_20260809T093313Z_b9e01dd6/section_failure_forensics/final_resume_aggregation.md`
