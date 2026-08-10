# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T05:54:41Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `ibm_narrative` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=9f32f449c4a23cfebd37db48968cccb9058108530ff1a7c7247bf320fb591502; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\apps_research\runs\r-9f15864f648c1cb985b96a05\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7204` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ibm_narrative` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `ibm_narrative`: Output contract failure: parsed content or claim ledger did not satisfy section schema.
  - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
  - Evidence: `x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
    - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
    - `Parser / normalization contract` / `PRIMARY` / `40%`: The bullet-count gate observed an empty parsed bullet artifact. Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_ibm_narrative_claim_theme_coverage: narrative_sentence material themes require matching bul_ibm_* in claim_ledger union; missing: ['unsupported_companion_theme:regulated_financial'] observed={'themes_detected': ['bul_ibm_001', 'bul_ibm_002', 'unsupported_companion_theme:regulated_financial'], 'missing_in_ledger_union': ['unsupported_companion_theme:regulated_financial']} Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
    - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets`. Required work: Attach parser input/output references and failed field names to the gate evidence.
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
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\apps_research\runs\r-9f15864f648c1cb985b96a05\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ibm_narrative_claim_theme_coverage, x2_ibm_narrative_mechanisms_supported_by_cited_companion_bullets), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

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

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ibm_narrative.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry4_20260809\e2e_20260809T054405Z_a3e2e6aa\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/index.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry4_20260809/e2e_20260809T054405Z_a3e2e6aa/section_failure_forensics/final_resume_aggregation.md`
