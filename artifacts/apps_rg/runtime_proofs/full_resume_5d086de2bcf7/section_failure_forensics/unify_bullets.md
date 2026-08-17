# Section Failure Forensics - unify_bullets

- failure_type: `upstream_cascade`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5d086de2bcf7\apps_research\runs\bridge_rg_research_bridge_b1940741_74ec0a11-f6cd-4ba5-a694-e8714aba0323\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

This section did not independently certify because an upstream dependency or pre-run blocker prevented normal section authorization: No section-level failure recorded..

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `NOT_OBSERVED` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `NOT_OBSERVED` / `NOT_OBSERVED` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `—` / `NOT_RUN` |
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
