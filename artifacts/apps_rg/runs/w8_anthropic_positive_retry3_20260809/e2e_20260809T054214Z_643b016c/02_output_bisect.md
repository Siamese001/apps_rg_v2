# apps_rg Output Bisect

## Section: whole_run

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry3_20260809\e2e_20260809T054214Z_643b016c\apps_research\runs\r-429475ee040dbed06bf1054a\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `d5b2f154e10bee97ae8013d5` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry3_20260809\e2e_20260809T054214Z_643b016c\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `9fce7d2de92f7e8596d16236` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry3_20260809\e2e_20260809T054214Z_643b016c\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `-` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `-` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| revision comparison | `-` | `-` | `False` | `PREEXISTED_BASELINE` | `NOT_APPLICABLE_NO_PRIOR_BASELINE` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | lane artifact directory not found | none | `NONE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `-` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
