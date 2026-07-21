# Section Failure Forensics - unify_bullets

- failure_type: `upstream_cascade`
- baseline_confidence: `pinned_baseline_unavailable`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\apps_research\runs\r-80e758cb11db9efc0bed092e\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

This section did not independently certify because an upstream dependency or pre-run blocker prevented normal section authorization: Pre-run dependency blocked execution: EXECUTED_X3A; dispatch_error:L2_EXECUTION_ERROR:ProductEvidenceAuthorityError:unify_bullets canonical C0.3 plan invalid: source_authority_contract, graph_candidate_decision_ledger, graph_traversal_receipt, graph_candidate_receipt|missing_pointer:no resolvable run_dir pointer for lane 'unify_bullets' under C:\Git\Agentic-Workflow-FRESH-worktrees\codex-apps-rg-source-refreeze\artifacts\apps_rg\runs\s2u0_r1\e2e_20260721T010017Z_65f533a8\modular_r4\sections.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `bb7a8e4620eacfa4d64ad44f71b46dcbbdf99b53` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `NOT_OBSERVED` / `NOT_OBSERVED` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `UNKNOWN` / `PRE_RUN:EXECUTED_X3A` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Resolve the upstream blocker before dispatching `unify_bullets`.
- Write the upstream dependency status into the section pre-run receipt.
- Keep the section blocked until its own X1-X3 inputs are present.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
