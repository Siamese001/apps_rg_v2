# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T08:33:38Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `headline` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=6a36e10597884f17e66a1f83476a92224656f158f32fbc6e7e1507b2a1c5d32c; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\apps_research\runs\r-41c059ab17564d1cc7ddb527\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7506` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: headline` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `headline`: X1D decisive judge failure: model-backed judge rejected section product quality.
  - Root cause: The lane published judge-visible narrative text after normalizing the provider payload through a lossy claim-ledger path that dropped source_fact_ids needed to support material claims.
  - Evidence: `Google Gemini 3.6 Flash \| gemini-3.6-flash \| MODEL_BACKED_FAIL \| score=2.5/4 \|\| OpenAI ChatGPT \| gpt-5.6-sol \| MODEL_BACKED_FAIL \| score=3/4`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The section was generated, parsed, and X2-clean, but the published claim ledger lost source-fact bindings that X1D required for judge-visible material claims.
    - Retry recoverability: `LOW_UNTIL_LEDGER_FIX` - Blind regeneration can return a valid parsed claim ledger again, but the same lossy normalization path will keep dropping support before X1D.
    - `Claim ledger normalization` / `PRIMARY` / `45%`: Google Gemini 3.6 Flash | gemini-3.6-flash | MODEL_BACKED_FAIL | score=2.5/4 || OpenAI ChatGPT | gpt-5.6-sol | MODEL_BACKED_FAIL | score=3/4 Evidence: `parsed_output.json, claim_ledger.json, x1d_llm_judge_outputs.json`. Required work: Preserve valid source_fact_ids from parsed narrative claim_ledger rows when publishing the single-sentence role-episode ledger.
    - `Narrative source binding` / `CONTRIBUTING` / `25%`: Narrative material phrases such as insurance operations, model risk, and traceable controls must bind to selected role-episode facts before judge review. Evidence: `selected_fact_plan.json, role_episode_lane.py`. Required work: Add deterministic phrase-to-fact reconciliation for EY narrative material claims within the allowed graph packet.
    - `X1D authorization policy` / `DETECTION` / `20%`: X2 PASS and product PASS were not enough because the model-backed judge rejected factual support. Evidence: `x3_disposition.json, x1d_llm_judge_outputs.json`. Required work: Keep X3 blocked on decisive factual-support judge failures and surface the judge finding as the primary RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: The fix belongs at the parser/ledger boundary, not in downstream rerun scheduling or final assembly. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Rerun only after the narrative ledger preservation fixture and mandatory-RCA fixture pass.
  - Required implementation plan:
    - Preserve valid source_fact_ids from parsed narrative claim_ledger rows when normalizing role-episode narrative output.
    - Add source-binding patterns for material EY insurance, ERM, CCAR, regulatory analytics, and capital/solvency claims.
    - Keep X2 PASS insufficient for authorization when X1D factual-support judges reject the published claim ledger.
    - Add a regression fixture using the live EY narrative where insurance operations must cite reb_ey_insurance_core_modernization.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `headline` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> PASS/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\apps_research\runs\r-41c059ab17564d1cc7ddb527\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so 2.5/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

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

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: headline.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry14_20260809\e2e_20260809T082331Z_9f9147d4\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/index.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry14_20260809/e2e_20260809T082331Z_9f9147d4/section_failure_forensics/final_resume_aggregation.md`
