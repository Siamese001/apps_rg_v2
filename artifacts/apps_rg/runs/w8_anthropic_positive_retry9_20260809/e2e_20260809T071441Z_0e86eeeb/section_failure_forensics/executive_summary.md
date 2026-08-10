# Section Failure Forensics - executive_summary

- failure_type: `upstream_cascade`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

This section did not independently certify because an upstream dependency or pre-run blocker prevented normal section authorization: Executive summary synthesis contract failure: deterministic producer repair did not satisfy brushstroke coverage, attribution density, and transition-quality gates..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `cba1303f044f24af364b888122971cab7a972457` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `7675ffe4d3782bdcee097b962c47ffae0d797b152a29af067f12b31c42a1cfb6` / `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\command_output.txt` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `FAIL` / `X3_BLOCK` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Resolve the upstream blocker before dispatching `executive_summary`.
- Write the upstream dependency status into the section pre-run receipt.
- Keep the section blocked until its own X1-X3 inputs are present.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
