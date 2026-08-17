# BCG Executive Output - apps_rg Run

Generated: `2026-08-17T02:57:34Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3_REVIEW_JUDGE_SOFT_FAIL, but completion ended BLOCKED because RuntimeError:FAILED_MODULAR_R4: decisive='FAIL' failure='fatal_lane_recipe_policy:unify_bullets:PHASE1_NO_RUN_DIR; unify_narrative:PHASE1_NO_RUN_DIR; executive_summary:PHASE1_NO_RUN_DIR' schema_ok=False lane_ok=False. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix X3-blocked generated lanes before authorizing the final resume. | `unify_bullets, executive_summary` | Outcome remains blocked until every required generated lane clears X3. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=4d45accc9442371277e957bd80d88e334a7517eca6add0f8f4d853fcb8d218d9; ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7999` |
| Did resume generation run? | `10 REAL_LLM section(s)` |
| Source X3 decision | `X3_REVIEW_JUDGE_SOFT_FAIL` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix X3-blocked generated lanes before authorizing the final resume. Evidence: unify_bullets, executive_summary` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `unify_bullets`: Deterministic gate failure.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `x2_bullet_seniority_floor`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x2_bullet_seniority_floor`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `unify_narrative`: Pre-run dependency blocked execution: upstream_not_finalized; pre_run_blocked:UPSTREAM_BULLETS_NOT_FINALIZED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:upstream_not_finalized`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.md`
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
- `executive_summary`: Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates.
  - Root cause: The executive-summary final producer path accepted repaired prose before revalidating required brushstroke coverage, row-level attribution density, and non-robotic transition shape.
  - Evidence: `x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The executive-summary repair path let a word-budget candidate become final without re-closing brushstroke utilization and transition-shape gates.
    - Retry recoverability: `MEDIUM` - Blind retry can recreate the same bridge stack, but producer-side rebinding and transition repair can recover without changing the evidence substrate.
    - `Producer finalization / repair ordering` / `PRIMARY` / `35%`: The final producer accepted text that still carried robotic S2-S5 transition openers. Evidence: `x2_executive_summary_synthesis_quality, x2_exec_summary_robotic_transition_stack_zero`. Required work: Apply bridge-density repair after all final polish and word-budget rewrites, then re-run the same synthesis-shape predicate X2 uses.
    - `Composition-plan brushstroke coverage` / `CONTRIBUTING` / `30%`: x2_exec_summary_allowed_fact_utilization: uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] observed=uncovered_required_brushstrokes=['reb_ibm_devsecops_release_resilience'] Evidence: `x2_exec_summary_allowed_fact_utilization`. Required work: Preserve at least one cited source fact for every required B1-B4 brushstroke group after display-ledger reconciliation.
    - `Claim attribution density` / `CONTRIBUTING` / `20%`: Density repair must choose direct supporting facts instead of carrying every adjacent source_fact_id. Evidence: `x2_exec_summary_cross_fact_conflation_zero, claim_ledger.json`. Required work: Cap each sentence row to the direct proof facts while preferring composition-required facts when multiple facts compete.
    - `Validation / RCA reporting` / `DETECTION` / `15%`: The mandatory output must allocate deterministic executive-summary gate failures to the producer contract instead of generic validation precision. Evidence: `x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory`. Required work: Classify executive-summary deterministic gate families with sentence-shape, brushstroke, and attribution-density RCA rows.
  - Required implementation plan:
    - Rebind the final executive-summary display text to the required composition-plan brushstroke facts after every deterministic and LLM repair.
    - Run transition-shape repair after word-budget and judge-polish rewrites so stock bridge openers cannot re-enter X2.
    - Keep each claim-ledger row capped to directly supporting source facts while preserving one cited fact per required B1-B4 brushstroke group.
    - Add regression fixtures using the live failed Anthropic paragraph for allowed-fact utilization and robotic-transition stack gates.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `unify_bullets` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `unify_narrative` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:upstream_not_finalized` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> FAIL/X3_BLOCK` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### unify_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_bullet_seniority_floor), so 5.0/4.0 MODEL_BACKED_PASS and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\apps_research\runs\bridge_rg_research_bridge_43cfbc63_0dfcac04-9185-4835-bfd1-81a9f6028664\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 3 pre-judge repair attempt(s), but combined too many source facts in one sentence; and sentence 1: mechanism_inventory:5_terms; and dominant_source_fact=unknown; and claim_support_graph_refs=[]; and suppressed_skills=[]; and sentence 1: mechanism_inventory:3_terms; it reverted to its first candidate, the final deterministic check still failed (x2_exec_summary_allowed_fact_utilization, x2_exec_summary_no_mechanism_inventory), so JUDGES_NOT_REACHED and the resume remained blocked.

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

1. Resolve P0: Fix X3-blocked generated lanes before authorizing the final resume. Evidence: unify_bullets, executive_summary.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_bb83a0b3333f\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/index.json; @artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/index.md`
- Section forensic RCA: unify_bullets: `@artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.json; @artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_bullets.md`
- Section forensic RCA: unify_narrative: `@artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.json; @artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/unify_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/executive_summary.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runtime_proofs/full_resume_bb83a0b3333f/section_failure_forensics/final_resume_aggregation.md`
