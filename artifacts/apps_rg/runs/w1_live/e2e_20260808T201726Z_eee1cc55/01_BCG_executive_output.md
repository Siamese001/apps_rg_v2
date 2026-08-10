# BCG Executive Output - apps_rg Run

Generated: `2026-08-08T20:26:37Z`
Run root: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55`

## Executive Answer

The run is blocked and must not authorize a final resume. Required generation and/or final product gates did not clear. The source X3 decision was X3A_DENY_REROUTE, but completion ended BLOCKED because APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE. Use the P0/P1/PX recommendations below as the repair order.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `P0` | Fix competencies first-lane execution failure before scheduling downstream lanes. | `PRE_RUN:EXECUTED_X3A_DENY_REROUTE` | No downstream lane without upstream authorization. |
| `P0` | Fix final_resume_aggregation before authorizing the final resume. | `final_resume_aggregation: x2=UNKNOWN; product=UNKNOWN; x3=X3_REVIEW_AGGREGATION` | Outcome remains blocked until full-resume aggregation clears X2/product gates. |
| `P0` | Keep final resume product gate failed while generated-section gap markers exist. | `final_resume_no_gap_markers` | Final resume unauthorized. |
| `P1` | Add dependency-token reporting for every PHASE1_NO_RUN_DIR lane. | `PHASE1_NO_RUN_DIR lanes: unify_bullets, ibm_bullets, insurtech_bullets, ey_bullets, unify_narrative, ibm_narrative, insurtech_narrative, ey_narrative, executive_summary, headline` | Show exact upstream repair order. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=6e9880dff8d87bad07fd94ace0a7b620af726e0c65bb90e1b9e000eb7e71b722; ref=C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7895` |
| Did resume generation run? | `0 REAL_LLM section(s)` |
| Source X3 decision | `X3A_DENY_REROUTE` |
| Completion status | `BLOCKED` |
| Completion fault | `APPS_RG_MANDATORY_OUTPUTS_INCOMPLETE` |
| Final product authorized? | `False` |
| Primary blocker | `Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: PRE_RUN:EXECUTED_X3A_DENY_REROUTE` |
| Decision | `Do not authorize; fix P0 gates first.` |

## Issue Tree

- `competencies`: Pre-run dependency blocked execution: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:PoolSelectorUnavailableError:competencies selector unavailable: no parsed candidate paths; first failure: External provider call failed: TimeoutError: External provider wall-clock timeout after 240s [last_progress_after_s=229.828, chars_received=0, chunk_count=2]
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:EXECUTED_X3A_DENY_REROUTE`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/competencies.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/competencies.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: EXECUTED_X3A_DENY_REROUTE; dispatch_error:L2_EXECUTION_ERROR:PoolSelectorUnavailableError:competencies selector unavailable: no parsed candidate paths; first failure: External provider call failed: TimeoutError: External provider wall-clock timeout after 240s [last_progress_after_s=229.828, chars_received=0, chunk_count=2] Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `unify_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ibm_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `insurtech_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ey_bullets`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_bullets.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_bullets.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `unify_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ibm_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `insurtech_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `ey_narrative`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_narrative.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_narrative.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `executive_summary`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/executive_summary.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/executive_summary.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
    - `Aggregation / product authorization` / `CONTRIBUTING` / `25%`: The dependent narrative must not schedule until its upstream bullets lane is certified. Evidence: `APPS_RG_MANDATORY_RUN_OUTPUT.json`. Required work: Consume the upstream token before dependent-lane scheduling.
    - `Retry / repair policy` / `NO_RECOVERY` / `10%`: No model retry can create the missing upstream authorization token. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Route retries to the upstream blocked lane, not the dependent lane.
    - `Observability / RCA reporting` / `REPORTING_GAP` / `10%`: The operator output must name the upstream blocker, artifact, and lane token that is missing. Evidence: `integrated_lane_pre_run_failure.json`. Required work: Surface upstream lane, missing token, and repair order in the RCA.
  - Required implementation plan:
    - Represent the upstream lane's product authorization as an explicit dependency token consumed by the downstream lane.
    - Write the upstream blocker lane, gate, and artifact path into the pre-run failure receipt when dependency authorization is absent.
    - Update rerun orchestration so upstream repair lanes execute and certify before dependent lanes are scheduled.
    - Add an integration fixture proving the dependent lane remains blocked until the upstream authorization token is present.
- `headline`: Pre-run dependency blocked execution: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED
  - Root cause: The lane dependency graph allows a downstream lane to be scheduled without an explicit upstream product-authorization token.
  - Evidence: `PRE_RUN:PHASE1_NO_RUN_DIR`
  - Evidence: `forensics_json=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/headline.json`
  - Evidence: `forensics_md=artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/headline.md`
  - Evidence: `forensics_complete=False`
  - Causal allocation:
    - Dominant cause: A downstream lane was evaluated without an upstream product-authorization token.
    - Retry recoverability: `NONE` - The dependent lane cannot recover through generation retries until the upstream lane is product-authorized.
    - `Orchestration / dependency control` / `PRIMARY` / `55%`: PHASE1_NO_RUN_DIR; pre_run_blocked:PHASE1_PRIOR_LANE_FAILED Evidence: `integrated_lane_pre_run_failure.json`. Required work: Represent upstream lane product authorization as an explicit dependency token.
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
| `competencies` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:EXECUTED_X3A_DENY_REROUTE` | `False` |
| `unify_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ibm_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `insurtech_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ey_bullets` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `unify_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ibm_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `insurtech_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `ey_narrative` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `executive_summary` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `headline` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/PRE_RUN:PHASE1_NO_RUN_DIR` | `False` |
| `final_resume_aggregation` | `NO_PRIOR_PASSING_RUN` | `cba1303f044f24af364b888122971cab7a972457` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> UNKNOWN/X3_REVIEW_AGGREGATION` | `False` |

## Layperson Retry And Root-Cause Explanation

### competencies

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_bullets

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### unify_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ibm_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### insurtech_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### ey_narrative

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### executive_summary

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### headline

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\apps_research\runs\bridge_rg_research_bridge_1d54138c_21bc6b90-f700-4d1a-af3c-db7021d79619\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

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

1. Resolve P0: Fix competencies first-lane execution failure before scheduling downstream lanes. Evidence: PRE_RUN:EXECUTED_X3A_DENY_REROUTE.
2. Resolve the remaining 2 P0 row(s) before rerun.
3. Rerun the integrated apps_rg path only after the listed P0 evidence clears.
4. Treat final assembly as valid only when every required section and product output is product-authorized.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w1_live\e2e_20260808T201726Z_eee1cc55\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/index.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/index.md`
- Section forensic RCA: competencies: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/competencies.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/competencies.md`
- Section forensic RCA: unify_bullets: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_bullets.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_bullets.md`
- Section forensic RCA: ibm_bullets: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_bullets.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_bullets.md`
- Section forensic RCA: insurtech_bullets: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_bullets.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_bullets.md`
- Section forensic RCA: ey_bullets: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_bullets.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_bullets.md`
- Section forensic RCA: unify_narrative: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_narrative.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/unify_narrative.md`
- Section forensic RCA: ibm_narrative: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_narrative.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ibm_narrative.md`
- Section forensic RCA: insurtech_narrative: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_narrative.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/insurtech_narrative.md`
- Section forensic RCA: ey_narrative: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_narrative.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/ey_narrative.md`
- Section forensic RCA: executive_summary: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/executive_summary.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/executive_summary.md`
- Section forensic RCA: headline: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/headline.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/headline.md`
- Section forensic RCA: final_resume_aggregation: `@artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/final_resume_aggregation.json; @artifacts/apps_rg/runs/w1_live/e2e_20260808T201726Z_eee1cc55/section_failure_forensics/final_resume_aggregation.md`
