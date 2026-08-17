# apps_eval report: apps_rg.current.resume_generation

## Run Context

Schema version: `apps_eval.completed_eval.v3`
Record ID: `01f499f691258985`
Created at: `1970-01-01T00:00:00Z`
Project: `agentic-workflow 1.0.0`
Git commit: `ad34314e854cb886270e2c81bfaf3f50a1a2c0e9`
Python: `3.12.10`
Platform: `Windows-11-10.0.26200-SP0`
Mode: `current_snapshot`
Deterministic only: `True`
Compare baseline: `False`
Record seed digest: `01f499f691258985a6ed7fb202deb16bc531a7afb98d36b671a50c7bd74ef35f`
Scorer version: `apps_eval.graders.deterministic.v2`

## Scorecard

App: `apps_rg`
Score: `1.000000`
Verdict: `pass`
Scenarios: `1`
Findings: `0` passed / `0` failed
Block failures: `0`

## apps_rg Microstep Coverage

Coverage verdict: `pass`
Coverage complete: `True`
Release blocked: `False`
Required microsteps: `131`
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
| apps_rg.generated_lane | lane_l2_generation | L2 | competencies | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | executive_summary | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ey_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ey_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | headline | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ibm_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | ibm_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | insurtech_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | insurtech_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | unify_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l2_generation | L2 | unify_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | competencies | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | executive_summary | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ey_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ey_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | headline | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ibm_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | ibm_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | insurtech_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | insurtech_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | unify_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_l6_shadow_package | L6 | unify_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | competencies | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | executive_summary | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ey_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ey_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | headline | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ibm_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | ibm_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | insurtech_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | insurtech_narrative | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | unify_bullets | 1.000000 | pass | 0 |
| apps_rg.generated_lane | lane_x1d_judge_panel | X1D | unify_narrative | 1.000000 | pass | 0 |
| _truncated_ | | | | | | 33 more |

## Failure Modes

Dominant family: `n/a`
Dominant mode: `n/a`

| Failure Family | Count |
|---|---:|
| _none_ | 0 |

| Failure Mode | Count |
|---|---:|
| _none_ | 0 |

## Fixture Provenance

| Scenario | Fixture Path | Definition Digest | Input Digest | Expected Digest | Snapshot Digest |
|---|---|---|---|---|---|
| apps_rg_current_run_post_x3 | C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_1bf5a3fd73c8 | 1c726b6581da1cd6d3ecb320b1979dcadd61f4e73a1d6be7470a8e544a5244cd | 44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a | 063334673a9a8f83b8fee3cfea0fcfc40521aea9945f927e9130c4daf8e1b0fc | 5f8f9987d8ad05c764206444f62500ef53b16fef066e1a006cc2bf882814198e |

## Scenario Results

| Scenario | Passed | Failed Findings | Primary Failure Mode | Snapshot Digest | Snapshot Ref |
|---|---:|---:|---|---|---|
| apps_rg_current_run_post_x3 | True | 0 |  | 5f8f9987d8ad05c764206444f62500ef53b16fef066e1a006cc2bf882814198e | C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_1bf5a3fd73c8 |

## Dimension Scores

| Dimension | Score |
|---|---:|

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
New failure modes: `n/a`
Recovered failure modes: `n/a`
Repeated failure modes: `n/a`

| Scenario | Failed Findings | Block Failures | Primary Failure Mode | Failure Modes |
|---|---:|---:|---|---|
| _none_ | 0 | 0 | _n/a_ | _n/a_ |

## Artifact Inventory

- `apps_rg_component_scorecard`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/apps_rg_component_scorecard.json`
- `apps_rg_l6_eval_handoff`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/apps_rg_l6_eval_handoff.json`
- `component_scorecards`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/component_scorecards.csv`
- `coverage_matrix`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/coverage_matrix.csv`
- `diagnostic_rows`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/diagnostic_rows.jsonl`
- `diagnostic_summary`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/diagnostic_summary.json`
- `eval_package_seal`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/apps_rg_eval_package_seal.json`
- `eval_record`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/eval_record.json`
- `evidence_index`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/evidence_index.csv`
- `grader_findings`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/grader_findings.jsonl`
- `l6_apps_eval_alignment`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_apps_eval_alignment.json`
- `l6_apps_eval_grain_parity`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_apps_eval_grain_parity.json`
- `l6_handoff`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_handoff.json`
- `l6_microstep_coverage`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_microstep_coverage.json`
- `l6_microstep_future_run_proposals`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_microstep_future_run_proposals.json`
- `l6_microstep_observations`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_microstep_observations.jsonl`
- `l6_microstep_patterns`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_microstep_patterns.json`
- `l6_microstep_rca`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_microstep_rca.json`
- `l6_shadow_bridge`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_shadow_bridge.json`
- `l6_shadow_bridge_spans`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_shadow_bridge_spans.json`
- `l6_shadow_bridge_spans_jsonl`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/l6_shadow_bridge_spans.jsonl`
- `manifest`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/manifest.json`
- `missing_required_components`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/missing_required_components.csv`
- `regression`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/regression.json`
- `regression_flywheel`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/regression_flywheel.json`
- `report`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/report.md`
- `scorecard`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/scorecard.csv`
- `scorecard_rows`: `C:/Git/apps_rg_v2/artifacts/apps_rg/runtime_proofs/full_resume_1bf5a3fd73c8/apps_eval/apps_rg_current_resume_generation/01f499f691258985/scorecard_rows.jsonl`

## Findings

| Scenario | Grader | Passed | Severity | Score | Message |
|---|---|---:|---|---:|---|

## Review Guidance

- Treat any block failure as release-blocking until the fixture, snapshot, or product output is corrected.
- Treat warning failures as review items unless the suite threshold already fails.
- Promote a new baseline only from a passing record after reviewing changed fixtures and report artifacts.
