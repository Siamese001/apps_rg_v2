# Section Failure Forensics - whole_run

- failure_type: `mandatory_output_authorization_block`
- baseline_confidence: `pinned_contract_invalid`
- failed_gate_ids: `-`

## Layperson Explanation

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.
The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ce77c5d3b476\apps_research\runs\bridge_rg_research_bridge_cb645228_326c1dba-c962-4eed-a818-7b89cf877f6a\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.
The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

## First Divergence And Underlying Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

## Why It Passed Before

The pinned prior-pass baseline was unavailable, so this RCA cannot claim a clean passing comparison.

## Why It Failed Now

Mandatory output authorization failed before the run could be treated as explainable.

## Prior Working Revision Comparison

| Signal | Prior passing revision | Current failure |
|---|---|---|
| Revision | `PR #None` / `NOT_OBSERVED` | `NOT_OBSERVED` |
| Materialized output | `NOT_OBSERVED` / `NOT_OBSERVED` | `NOT_OBSERVED` / `NOT_OBSERVED` |
| X2 / X3 | `NOT_OBSERVED` / `NOT_OBSERVED` | `NOT_OBSERVED` / `X3D_ALLOW_FINISH` |
| Judges | `NOT_OBSERVED` | `NOT_OBSERVED` |

## Required Fix

- Generate missing mandatory BCG, run-ledger, and forensic RCA artifacts before exit.
- Validate every required forensic RCA field before declaring the E2E failure explainable.
- Fail with E2E_FAIL_WITHOUT_SECTION_FORENSICS when any required RCA artifact is missing or incomplete.

## Artifact Hash Comparisons

- input_hash_comparison: `False`
- selected_fact_plan_comparison: `False`
- provider_request_hash_comparison: `False`
- materialized_output_hash_comparison: `False`
- comparison_complete: `False`
