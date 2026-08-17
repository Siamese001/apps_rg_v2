# BCG Executive Output - apps_rg Run

Generated: `2026-08-17T02:15:08Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3_REVIEW_JUDGE_SOFT_FAIL, but completion ended BLOCKED because RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:executive_summary:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `executive_summary` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=c87cb39b9a630086e52dbe7e710139da17b5e9c8fd80e1668a450620d8b14263; ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\apps_research\runs\bridge_rg_research_bridge_4ffe731a_ff4e4cba-4197-4219-8c53-0a331384c729\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7988` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3_REVIEW_JUDGE_SOFT_FAIL` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: executive_summary` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `executive_summary`: Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.
  - Root cause: The executive-summary final producer path accepted repaired prose before revalidating required brushstroke coverage, row-level attribution density, and non-robotic transition shape.
  - Evidence: `x2_exec_summary_allowed_fact_utilization`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
    - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
    - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: The final producer accepted text that still carried robotic S2-S5 transition openers. Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
    - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: x2_exec_summary_allowed_fact_utilization: uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] observed=uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
    - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
    - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
  - Required implementation plan:
    - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
    - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
    - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
    - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\apps_research\runs\bridge_rg_research_bridge_4ffe731a_ff4e4cba-4197-4219-8c53-0a331384c729\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 1 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_allowed_fact_utilization), so JUDGES_NOT_REACHED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `retry_loop`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### final_resume_aggregation

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.

The aggregate panel ran and recorded - EVIDENCE_NOT_RECORDED; the required two-of-two model-backed quorum was not met.

The controlling product defect is aggregate coherence, not upstream section eligibility: the failed aggregate gate is recorded in the final-resume review artifact.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `aggregate_coherence_quorum`
- Code cause status: `AGGREGATE_GATE_ISOLATED`


## Recommended Next Move

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: executive_summary.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_f3e315ad1b38\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/index.json; @artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/index.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/executive_summary.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runtime_proofs/full_resume_f3e315ad1b38/section_failure_forensics/final_resume_aggregation.md`
