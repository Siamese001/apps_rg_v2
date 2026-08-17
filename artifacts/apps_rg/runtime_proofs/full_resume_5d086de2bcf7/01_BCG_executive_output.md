# BCG Executive Output - apps_rg Run

Generated: `2026-08-16T15:54:03Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because ValueError:canonical graph validation failed: GRAPH_AUTHORITY_RECONCILIATION_MARKER_MISMATCH: count=3 offenders=['current_graph_edges_sha256', 'current_graph_nodes_sha256', 'current_skill_rows_sha256']. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix competencies first-lane execution failure before scheduling downstream lanes. | `NOT_RUN` | No downstream lane without upstream authorization. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=NOT_OBSERVED; ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships` |
| Did resume generation run? | `0 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: NOT_RUN` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `competencies`: Evidence mapping failure: visible content was not fully backed by source facts or graph lineage.
  - Root cause: Visible content can be rendered before every term or claim has source-fact IDs, graph lineage, and claim-ledger coverage.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/competencies.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/competencies.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The visible competency surface can be assembled before category, term, confidence, and graph lineage proof is complete.
    - Retry recoverability: `LOW` - Blind retries regenerate text against the same incomplete proof contract; only gate-aware lineage repair can recover it.
    - `Evidence substrate / graph lineage` / `PRIMARY` / `45%`: Failed gates show missing category source facts or unsupported visible terms. Evidence: `x2_competencies_graph_granularity_gates, x2_competency_term_supported`. Required work: Add category-level source-fact coverage and remove or bind unsupported visible terms before display.
    - `Artifact transformation contract` / `CONTRIBUTING` / `25%`: Selected graph evidence was not preserved into per-term source_fact_ids and per-category confidence. Evidence: `x2_all_terms_source_fact_ids, x2_competencies_per_category_confidence_nonconstant`. Required work: Make graph selection, claim ledger, category confidence, and display a lossless transformation contract.
    - `Validation / gate precision` / `DETECTION` / `20%`: The gates detected missing lineage, but the RCA must preserve the exact category, term, source fact, and owning producer. Evidence: ``. Required work: Emit a category-by-category repair matrix in the gate receipt and RCA.
    - `Retry / repair policy` / `LOW_RECOVERY` / `10%`: More candidate generations cannot satisfy missing source_fact_ids or unsupported graph terms unless the repair step fills lineage first. Evidence: `self_consistency_paths.json, section_repair_ledger.json`. Required work: Replace blind retry with gate-aware lineage repair for missing facts, terms, and confidence.
  - Required implementation plan:
    - List every visible term or claim missing source_fact_id, graph path ID, or claim-ledger coverage from the failed gate evidence.
    - Change the section enrichment step so selected visible terms are emitted only with canonical source_fact_ids and graph lineage.
    - Add a pre-display validation guard that blocks rendering when any visible claim lacks lineage or per-term ledger coverage.
    - Add a regression fixture that rejects ungrounded terms and accepts the same terms only when backed by source facts and graph paths.
- `unify_bullets`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `ibm_bullets`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `insurtech_bullets`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `ey_bullets`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `unify_narrative`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_narrative.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `ibm_narrative`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `insurtech_narrative`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_narrative.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `ey_narrative`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_narrative.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `executive_summary`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.
- `headline`: No section-level failure recorded.
  - Root cause: The failed gate evidence has not been traced to a single owning runtime contract.
  - Evidence: `NOT_RUN`
  - Evidence: `forensics_json=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=True`
  - Causal allocation:
    - Dominant cause: The failed gate evidence has not been allocated to one owning runtime contract.
    - Retry recoverability: `UNKNOWN` - Recoverability cannot be assessed until the owning contract is identified.
    - `Validation / gate precision` / `PRIMARY` / `100%`: The available failed gates do not name a precise owning producer, parser, or validator contract. Evidence: `x3_disposition.json`. Required work: Trace the failed evidence to the runtime contract that first allowed invalid state.
  - Required implementation plan:
    - Assign the failed gate family to one owning runtime contract before changing prompts or thresholds.
    - Trace the artifact producer, parser, and validator for that contract and identify where invalid state first becomes representable.
    - Add a contract-level regression fixture at that boundary so symptom-only downstream repairs cannot pass.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `competencies` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `unify_bullets` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `ibm_bullets` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `insurtech_bullets` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `unify_narrative` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `insurtech_narrative` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `headline` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> —/NOT_RUN` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

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

1. Resolve P0: Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: NOT_RUN.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/index.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/competencies.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/competencies.md`
- Section forensic RCA: unify_bullets: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_bullets.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_bullets.md`
- Section forensic RCA: ibm_bullets: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_bullets.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_bullets.md`
- Section forensic RCA: insurtech_bullets: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_bullets.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_bullets.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: unify_narrative: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_narrative.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/unify_narrative.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: insurtech_narrative: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_narrative.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/insurtech_narrative.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/executive_summary.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/headline.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runtime_proofs/full_resume_5d086de2bcf7/section_failure_forensics/final_resume_aggregation.md`
