# apps_eval report: apps_rg.current.resume_generation

## Run Context

Schema version: `apps_eval.completed_eval.v3`
Record ID: `c5473d430578a7dc`
Created at: `1970-01-01T00:00:00Z`
Project: `agentic-workflow 1.0.0`
Git commit: `6aabf74d9774609570d9f72b63649e3b285530e3`
Python: `3.12.10`
Platform: `Windows-11-10.0.26200-SP0`
Mode: `current_snapshot`
Deterministic only: `True`
Compare baseline: `False`
Record seed digest: `c5473d430578a7dc6bb8113ce97c3f6dc7d3b76721b413c8172d94cf1b5ac9b7`
Scorer version: `apps_eval.graders.deterministic.v2`

## Scorecard

App: `apps_rg`
Score: `0.209459`
Verdict: `fail`
Scenarios: `1`
Findings: `7` passed / `117` failed
Block failures: `103`

## apps_rg Microstep Coverage

Coverage verdict: `fail`
Coverage complete: `True`
Release blocked: `True`
Required microsteps: `137`
Emitted rows: `137`
Missing required artifacts: `0`
Unknown required: `0`
Not run required: `0`

| Component | Subcomponent | Stage | Lane | Score | Verdict | Blocks |
|---|---|---|---|---:|---|---:|
| apps_rg.cross_section | cross_section_graph_coherence | X2 |  | 1.000000 | pass | 0 |
| apps_rg.cross_section | cross_section_overlap | X2 |  | 1.000000 | pass | 0 |
| apps_rg.eval_package | component_scorecards | PACKAGE |  | 1.000000 | pass | 0 |
| apps_rg.eval_package | coverage_matrix | PACKAGE |  | 1.000000 | pass | 0 |
| apps_rg.eval_package | regression_outputs | REGRESSION |  | 1.000000 | pass | 0 |
| apps_rg.eval_package | scorecard_rows | PACKAGE |  | 1.000000 | pass | 0 |
| apps_rg.final_assembly | final_resume_structure | X2 |  | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | competencies | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | executive_summary | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ey_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ey_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | headline | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ibm_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ibm_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | insurtech_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | insurtech_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | unify_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l2_generation | L2 | unify_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | competencies | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | executive_summary | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ey_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ey_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | headline | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ibm_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ibm_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | insurtech_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | insurtech_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | unify_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | unify_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | competencies | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | executive_summary | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ey_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ey_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | headline | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ibm_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ibm_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | insurtech_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | insurtech_narrative | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | unify_bullets | 0.000000 | fail | 2 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | unify_narrative | 0.000000 | fail | 2 |
| _truncated_ | | | | | | 33 more |

## Failure Modes

Dominant family: `contract`
Dominant mode: `contract.artifact.required_artifacts_missing`

| Failure Family | Count |
|---|---:|
| evidence | 110 |
| microstep | 3 |
| contract | 1 |
| determinism | 1 |
| grounding | 1 |
| policy | 1 |

| Failure Mode | Count |
|---|---:|
| evidence.source_identity_missing | 110 |
| contract.artifact.required_artifacts_missing | 1 |
| determinism.snapshot_drift | 1 |
| grounding.claims_unsupported | 1 |
| microstep.c0_evidence_materiality_present | 1 |
| microstep.l1_static_plan_profile_schema_bound | 1 |
| microstep.pa_prompt_boundary_evidence_as_data | 1 |
| policy.x3_disposition_mismatch | 1 |

## Fixture Provenance

| Scenario | Fixture Path | Definition Digest | Input Digest | Expected Digest | Snapshot Digest |
|---|---|---|---|---|---|
| apps_rg_current_run_post_x3 | C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4 | 1c726b6581da1cd6d3ecb320b1979dcadd61f4e73a1d6be7470a8e544a5244cd | 44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a | 94c66666161ed3a7481822e7f207684d258ca753539f49606b8f05e93d6f558c | b4ede11fe3ca274fe560aa363e1aa39e8d41d608cbf9377d9884b83538cd1c97 |

## Scenario Results

| Scenario | Passed | Failed Findings | Primary Failure Mode | Snapshot Digest | Snapshot Ref |
|---|---:|---:|---|---|---|
| apps_rg_current_run_post_x3 | False | 4 | contract.artifact.required_artifacts_missing | b4ede11fe3ca274fe560aa363e1aa39e8d41d608cbf9377d9884b83538cd1c97 | C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4 |

## Dimension Scores

| Dimension | Score |
|---|---:|
| artifact_presence | 0.000000 |
| determinism | 0.000000 |
| escalation | 1.000000 |
| forbidden_content | 1.000000 |
| grounded_claim | 0.000000 |
| length_bounds | 1.000000 |
| provenance | 1.000000 |
| schema | 1.000000 |
| section_structure | 1.000000 |
| side_effect | 1.000000 |
| x3_disposition | 0.000000 |

## Regression

Compared: `False`
Verdict: `not_compared`
Delta: `0.000000`
Baseline path: `n/a`
Baseline digest: `n/a`

## Regression Flywheel

Compared: `False`
Current score: `0.000000`
Baseline score: `0.000000`
Delta: `0.000000`
Verdict: `not_compared`
New failure modes: `contract.artifact.required_artifacts_missing, determinism.snapshot_drift, grounding.claims_unsupported, policy.x3_disposition_mismatch`
Recovered failure modes: `n/a`
Repeated failure modes: `n/a`

| Scenario | Failed Findings | Block Failures | Primary Failure Mode | Failure Modes |
|---|---:|---:|---|---|
| apps_rg_current_run_post_x3 | 4 | 4 | contract.artifact.required_artifacts_missing | contract.artifact.required_artifacts_missing, determinism.snapshot_drift, grounding.claims_unsupported, policy.x3_disposition_mismatch |

## Artifact Inventory

- `apps_rg_component_scorecard`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/apps_rg_component_scorecard.json`
- `apps_rg_l6_eval_handoff`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/apps_rg_l6_eval_handoff.json`
- `component_scorecards`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/component_scorecards.csv`
- `coverage_matrix`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/coverage_matrix.csv`
- `diagnostic_rows`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/diagnostic_rows.jsonl`
- `diagnostic_summary`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/diagnostic_summary.json`
- `eval_package_seal`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/apps_rg_eval_package_seal.json`
- `eval_record`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/eval_record.json`
- `evidence_index`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/evidence_index.csv`
- `grader_findings`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/grader_findings.jsonl`
- `l6_apps_eval_alignment`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_apps_eval_alignment.json`
- `l6_apps_eval_grain_parity`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_apps_eval_grain_parity.json`
- `l6_handoff`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_handoff.json`
- `l6_microstep_coverage`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_microstep_coverage.json`
- `l6_microstep_future_run_proposals`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_microstep_future_run_proposals.json`
- `l6_microstep_observations`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_microstep_observations.jsonl`
- `l6_microstep_patterns`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_microstep_patterns.json`
- `l6_microstep_rca`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_microstep_rca.json`
- `l6_shadow_bridge`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_shadow_bridge.json`
- `l6_shadow_bridge_spans`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_shadow_bridge_spans.json`
- `l6_shadow_bridge_spans_jsonl`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/l6_shadow_bridge_spans.jsonl`
- `manifest`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/manifest.json`
- `missing_required_components`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/missing_required_components.csv`
- `regression`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/regression.json`
- `regression_flywheel`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/regression_flywheel.json`
- `report`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/report.md`
- `scorecard`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/scorecard.csv`
- `scorecard_rows`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/apps_eval/apps_rg_current_resume_generation/c5473d430578a7dc/scorecard_rows.jsonl`

## Findings

| Scenario | Grader | Passed | Severity | Score | Message |
|---|---|---:|---|---:|---|
| apps_rg_current_run_post_x3 | schema | True | block | 1.000000 | schema keys present |
| apps_rg_current_run_post_x3 | artifact_presence | False | block | 0.000000 | missing artifacts: ['resume.md'] |
| apps_rg_current_run_post_x3 | x3_disposition | False | block | 0.000000 | expected X3D_ALLOW_FINISH, got UNKNOWN |
| apps_rg_current_run_post_x3 | forbidden_content | True | block | 1.000000 | no forbidden content |
| apps_rg_current_run_post_x3 | grounded_claim | False | block | 0.000000 | ungrounded claims: ['apps_rg_live_claim_1', 'apps_rg_live_claim_2', 'apps_rg_live_claim_3', 'apps_rg_live_claim_4', 'apps_rg_live_claim_5', 'apps_rg_live_claim_6', 'apps_rg_live_claim_7', 'apps_rg_live_claim_8', 'apps_rg_live_claim_9', 'apps_rg_live_claim_10', 'apps_rg_live_claim_11', 'apps_rg_live_claim_12', 'apps_rg_live_claim_13', 'apps_rg_live_claim_14', 'apps_rg_live_claim_15', 'apps_rg_live_claim_16', 'apps_rg_live_claim_17', 'apps_rg_live_claim_18'] |
| apps_rg_current_run_post_x3 | provenance | True | block | 1.000000 | provenance present |
| apps_rg_current_run_post_x3 | section_structure | True | block | 1.000000 | required sections present |
| apps_rg_current_run_post_x3 | length_bounds | True | warn | 1.000000 | length within bounds |
| apps_rg_current_run_post_x3 | side_effect | True | block | 1.000000 | no product state mutation |
| apps_rg_current_run_post_x3 | escalation | True | block | 1.000000 | escalation behavior matched |
| apps_rg_current_run_post_x3 | determinism | False | block | 0.000000 | snapshot hash mismatch |

## Review Guidance

- Treat any block failure as release-blocking until the fixture, snapshot, or product output is corrected.
- Treat warning failures as review items unless the suite threshold already fails.
- Promote a new baseline only from a passing record after reviewing changed fixtures and report artifacts.
