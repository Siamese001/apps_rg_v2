# BCG Executive Output - apps_rg Run

Generated: `2026-08-09T06:10:35Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `ibm_narrative, executive_summary, headline` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=3fe5f7d6e1c422194eef89518e32f4914472b289e6861113f41cba6701a25ff8; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7670` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ibm_narrative, executive_summary, headline` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `ibm_narrative`: Output contract failure: parsed content or claim ledger did not satisfy section schema.
  - Root cause: The lane's provider output, parser, and claim-ledger contract are not a single enforced schema from generation through X2 validation.
  - Evidence: `x2_ibm_narrative_claim_theme_coverage`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The runtime accepted provider output but the parser/schema/ledger contract emitted an empty product artifact.
    - Retry recoverability: `LOW` - Additional model attempts cannot repair a parser and claim-ledger path that converts generated bullets into zero product bullets and zero claims.
    - `Parser / normalization contract` / `PRIMARY` / `40%`: The bullet-count gate observed an empty parsed bullet artifact. Evidence: `x2_insurtech_bullets_bullet_count_3`. Required work: Normalize provider JSON into the canonical bullet schema before X2 and fail closed before display when parsing yields zero bullets.
    - `Claim ledger / provenance contract` / `CONTRIBUTING` / `30%`: x2_ibm_narrative_claim_theme_coverage: narrative_sentence material themes require matching bul_ibm_* in claim_ledger union; missing: ['unsupported_companion_theme:regulated_financial'] observed={'themes_detected': ['bul_ibm_001', 'bul_ibm_002', 'unsupported_companion_theme:regulated_financial'], 'missing_in_ledger_union': ['unsupported_companion_theme:regulated_financial']} Evidence: `x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_source_fact_ids_supported`. Required work: Emit claim_text and source_fact_ids during parsing so every bullet is provenance-bound before judge or gate review.
    - `Validation / gate precision` / `DETECTION` / `15%`: X2 detected empty bullets and ledger rows, but the RCA must preserve which parser/schema contract produced the empty artifact. Evidence: `x2_ibm_narrative_claim_theme_coverage`. Required work: Attach parser input/output references and failed field names to the gate evidence.
    - `Retry / repair policy` / `LOW_RECOVERY` / `15%`: Retries target the model, while the observed failure is an empty parsed artifact after generation. Evidence: `self_consistency_paths.json, parsed_output.json`. Required work: Allow retry only after parser and claim-ledger contracts prove they can preserve a valid generated payload.
  - Required implementation plan:
    - Trace the lane's canonical output schema from provider prompt to parser to X2 gate input and remove alternate empty or partial shapes.
    - Move required-field and bullet-count validation ahead of X2 so malformed provider responses fail before claim evaluation.
    - Emit claim-ledger rows with source_fact_id and claim_text at generation/parsing time instead of attempting post-hoc repair.
    - Add a fixture that proves malformed provider output is rejected and a compliant provider payload produces the expected ledger rows.
    - Add a CI assertion that the lane cannot emit display content unless the schema and claim-ledger contract is satisfied.
- `executive_summary`: Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
  - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
  - Evidence: `x2_resume_graph_claim_binding`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The executive summary can over-compress platform, modernization, governance, and alliance facts into dense sentences before X2 attribution gates run.
    - Retry recoverability: `MEDIUM` - Blind retries can repeat the density pattern, but gate-aware synthesis repair plus deterministic density trimming can recover without changing the research substrate.
    - `Synthesis density / prose shaping` / `PRIMARY` / `40%`: Failed gates show over-budget prose or mechanism-inventory wording in the executive summary. Evidence: `x2_exec_summary_paragraph_max_words, x2_exec_summary_no_mechanism_inventory`. Required work: Constrain the repair prompt and deterministic polish chain to produce six sentences under the word ceiling without mechanism inventories.
    - `Claim attribution density` / `CONTRIBUTING` / `30%`: A claim-ledger row carried too many distinct source_fact_ids for a single displayed sentence. Evidence: `x2_exec_summary_cross_fact_conflation_zero`. Required work: Keep each claim-ledger row bound to the directly supporting facts for that sentence and split or compact overloaded proof themes.
    - `Validation / gate precision` / `DETECTION` / `20%`: X2 identified the exact failed executive-summary gates, but the run RCA must preserve sentence-level failure details. Evidence: `x2_resume_graph_claim_binding`. Required work: Emit sentence index, word count, mechanism hits, and source_fact_id counts in executive-summary gate evidence.
    - `Retry / repair policy` / `RECOVERY` / `10%`: Repair must be allowed to reduce source-fact density when the failing gate is over-compression, not treat fact-count reduction as a substance regression. Evidence: `synthesis_regen_receipt.json, exec_summary_word_budget_repair_receipt.json`. Required work: Let density-specific repairs reduce over-packed source_fact_ids while preserving six claim rows and required brushstroke coverage.
  - Required implementation plan:
    - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
    - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
    - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
    - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
- `headline`: Headline executive positioning contract failure: vendor/tool proof terms reached display without an executive abstraction segment.
  - Root cause: The headline normalization path did not rewrite a vendor-specific migration phrase into the executive positioning vocabulary required for X/Y/Z display segments.
  - Evidence: `x2_headline_executive_abstraction_floor, x2_headline_technical_specificity_floor_met`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: The headline producer let a vendor-specific migration phrase remain in display position instead of projecting it to a proof-backed executive operating abstraction.
    - Retry recoverability: `HIGH_AFTER_NORMALIZATION_FIX` - The selected proof was valid and judges passed; deterministic normalization can recover by rewriting the display segment and ledger before X2.
    - `Headline normalization / display policy` / `PRIMARY` / `45%`: x2_headline_executive_abstraction_floor: Each headline segment must express executive scope such as platform, architecture, governance, ecosystem, commercialization, or regulated systems. observed={'display_tier': 'executive_positioning', 'raw_vendor_architecture_as_segment': 'forbid_by_default', 'preferred_abstractions': ['Enterprise AI Platforms', 'Cloud Data Platforms', 'Runtime Governance Architecture', 'Partner AI Ecosystems', 'Platform Commercialization', 'Regulated AI Systems'], 'segments': [{'segment_index': 2, 'segment': 'Runtime Governance Telemetry', 'vendor_or_product_terms': [], 'has_executive_abstraction': True, 'standalone_vendor_architecture': False}, {'segment_index': 3, 'segment': 'Client Portfolio Expansion', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}, {'segment_index': 4, 'segment': 'Context Engineering Evaluation', 'vendor_or_product_terms': [], 'has_executive_abstraction': False, 'standalone_vendor_architecture': False}], 'standalone_vendor_architecture_segments': [], 'segments_missing_executive_abstraction': ['Client Portfolio Expansion', 'Context Engineering Evaluation'], 'vendor_terms_without_executive_abstraction': []} Evidence: `x2_headline_executive_abstraction_floor, x2_headline_vendor_terms_proof_only`. Required work: Rewrite vendor-specific migration phrases to allowed executive headline abstractions before display validation.
    - `Claim ledger segment rebinding` / `CONTRIBUTING` / `25%`: Headline segment rewrites must also update claim_text rows so visible X/Y/Z phrases remain the ledger authority. Evidence: `claim_ledger.json, parsed_output.json`. Required work: Rebuild the three segment claim-ledger rows after deterministic headline phrase repair.
    - `Validation / gate precision` / `DETECTION` / `20%`: The deterministic headline gates correctly blocked a proof-only vendor term in display despite model-backed judge passes. Evidence: `x2_gate_outputs.json`. Required work: Keep display-policy X2 gates authoritative over X1D judge approval for headline formatting and abstraction constraints.
    - `Retry / repair policy` / `HIGH_RECOVERY` / `10%`: The failure is a deterministic phrase-normalization gap, so a targeted repair fixture should recover without changing research or section evidence. Evidence: `headline_output.txt`. Required work: Rerun after the live failed headline fixture proves X2 clears with the repaired segment.
  - Required implementation plan:
    - Map vendor-specific migration fragments to proof-backed executive headline abstractions before X2 runs.
    - Rebuild the segment claim ledger after headline rewrites so the displayed X/Y/Z phrases remain source-bound.
    - Keep vendor names and product terms in proof evidence, not standalone display segments, unless the segment also carries an executive abstraction.
    - Add a regression fixture using the live failed headline with AWS Migration Modernization Execution.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK_FINAL_MATERIALIZED_ACCEPTANCE` | `False` |
| `headline` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ibm_narrative_claim_theme_coverage), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 2 pre-judge repair attempt(s), but DISPLAY_OVERRIDE compliance failed: fact_engineering_platform_002 missing anchor 'dependency graph intelligence enables accelerated legacy-system analysis'; it reverted to its first candidate, the final deterministic check still failed (x2_resume_graph_claim_binding), so 4.8/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `retry_loop`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\apps_research\runs\r-73ff483d7ddda9402be67a57\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_executive_abstraction_floor, x2_headline_technical_specificity_floor_met), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

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

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: ibm_narrative, executive_summary, headline.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry6_20260809\e2e_20260809T055825Z_cfcbf4fc\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/index.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/executive_summary.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/headline.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w8_anthropic_positive_retry6_20260809/e2e_20260809T055825Z_cfcbf4fc/section_failure_forensics/final_resume_aggregation.md`
