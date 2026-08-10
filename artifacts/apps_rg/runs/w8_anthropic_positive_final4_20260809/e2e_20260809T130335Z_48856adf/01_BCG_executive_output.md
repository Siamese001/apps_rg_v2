# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T13:14:40Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because L2_EXECUTION_ERROR:RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:ey_bullets:EXECUTED_X3_BLOCK; ey_narrative:upstream_not_finalized' schema_ok=False lane_ok=False. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `ey_bullets` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=fd88226ad5dc9ed655ee95f19162fc9b22f342e3828790f252cf9076dc280c38; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\apps_research\runs\r-4d3972bfe361debc6a211041\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7828` |
| Did resume generation run? | `10 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ey_bullets` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `ey_bullets`: X1D decisive judge failure: model-backed judge rejected section product quality.
  - Root cause: The lane published judge-visible narrative text after normalizing the provider payload through a lossy claim-ledger path that dropped source_fact_ids needed to support material claims.
  - Evidence: `OpenAI ChatGPT \| gpt-5.6-sol \| MODEL_BACKED_FAIL \| score=0/0.72`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The section was generated, parsed, and X2-clean, but the published claim ledger lost source-fact bindings that X1D required for judge-visible material claims.
    - Retry recoverability: `LOW_UNTIL_LEDGER_FIX` - Blind regeneration can return a valid parsed claim ledger again, but the same lossy normalization path will keep dropping support before X1D.
    - `Claim ledger normalization` / `PRIMARY` / `45%`: OpenAI ChatGPT | gpt-5.6-sol | MODEL_BACKED_FAIL | score=0/0.72 Evidence: `parsed_output.json, claim_ledger.json, x1d_llm_judge_outputs.json`. Required work: Preserve valid source_fact_ids from parsed narrative claim_ledger rows when publishing the single-sentence role-episode ledger.
    - `Narrative source binding` / `CONTRIBUTING` / `25%`: Narrative material phrases such as insurance operations, model risk, and traceable controls must bind to selected role-episode facts before judge review. Evidence: `selected_fact_plan.json, role_episode_lane.py`. Required work: Add deterministic phrase-to-fact reconciliation for EY narrative material claims within the allowed graph packet.
    - `X1D authorization policy` / `DETECTION` / `20%`: X2 PASS and product PASS were not enough because the model-backed judge rejected factual support. Evidence: `x3_disposition.json, x1d_llm_judge_outputs.json`. Required work: Keep X3 blocked on decisive factual-support judge failures and surface the judge finding as the primary RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: The fix belongs at the parser/ledger boundary, not in downstream rerun scheduling or final assembly. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Rerun only after the narrative ledger preservation fixture and mandatory-RCA fixture pass.
  - Required implementation plan:
    - Preserve valid source_fact_ids from parsed narrative claim_ledger rows when normalizing role-episode narrative output.
    - Add source-binding patterns for material EY insurance, ERM, CCAR, regulatory analytics, and capital/solvency claims.
    - Keep X2 PASS insufficient for authorization when X1D factual-support judges reject the published claim ledger.
    - Add a regression fixture using the live EY narrative where insurance operations must cite reb_ey_insurance_core_modernization.
- `ey_narrative`: Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:upstream_not_finalized`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_narrative.md`
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
| `competencies` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> PASS/X3_REVIEW_JUDGE_PROVIDER_BLOCKED` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> PASS/X3_BLOCK` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\apps_research\runs\r-4d3972bfe361debc6a211041\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so None/0.8 BLOCKED_PROVIDER_UNAVAILABLE and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\apps_research\runs\r-4d3972bfe361debc6a211041\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\apps_research\runs\r-4d3972bfe361debc6a211041\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ey_bullets.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_final4_20260809\e2e_20260809T130335Z_48856adf\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/competencies.json; @artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/competencies.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_final4_20260809/e2e_20260809T130335Z_48856adf/section_failure_forensics/final_resume_aggregation.md`
