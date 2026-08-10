# apps_rg Output Bisect

## Section: insurtech_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_insurtech_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_insurtech_bullets_display_text_proof_authorized, x2_insurtech_bullets_runtime_real_llm, x2_insurtech_bullets_bullet_count_3, x2_resume_graph_claim_binding), so None/None BLOCKED_PROVIDER_UNAVAILABLE and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b622dabd89ba343732c8c774` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `1cc1c55ffbc6785bc5d924f4` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `730c8658291c679f92e55f3b` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `519c69afe79226aa7223c301` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `d8d49ac70f8927fdd10de4a5` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `-` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `None/None BLOCKED_PROVIDER_UNAVAILABLE` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `e3b0c44298fc1c14` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `BLOCKED_PROVIDER_UNAVAILABLE` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger missing or empty claim_text |
| `x2_insurtech_bullets_allowed_fact_ids_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | 16 |
| `x2_insurtech_bullets_bullet_count_3` | `NOT_OBSERVED` | `FAIL` | `True` | expected exactly 3 bullets |
| `x2_insurtech_bullets_bullet_no_embedded_newline` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_insurtech_bullets_bullet_single_thought` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_insurtech_bullets_display_text_proof_authorized` | `NOT_OBSERVED` | `FAIL` | `True` | display text must be rendered from selected proof fact claim_text |
| `x2_insurtech_bullets_graph_role_episode_bundle_consumed` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_insurtech_bullets_runtime_real_llm` | `NOT_OBSERVED` | `FAIL` | `True` | runtime_generation_status=BLOCKED |
| `x2_insurtech_bullets_source_fact_ids_supported` | `NOT_OBSERVED` | `FAIL` | `True` | claim source_fact_ids missing or outside allowed pool |
| `x2_insurtech_bullets_targeting_only_not_experience_claim` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `None/None FAIL` | - |

## Section: ey_bullets

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_ey_bullets_source_fact_ids_supported, x2_claim_ledger_claim_text_non_empty, x2_ey_bullets_display_text_proof_authorized, x2_ey_bullets_runtime_real_llm, x2_ey_bullets_bullet_count_3, x2_resume_graph_claim_binding), so None/None BLOCKED_PROVIDER_UNAVAILABLE and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b622dabd89ba343732c8c774` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `ef6408a5137fd37174162259` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `debe72070fb8174fa6032e06` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `af3c064de1d39bdb73330503` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `d8d49ac70f8927fdd10de4a5` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `-` | - | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `None/None BLOCKED_PROVIDER_UNAVAILABLE` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `e3b0c44298fc1c14` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `BLOCKED_PROVIDER_UNAVAILABLE` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_bullets\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger missing or empty claim_text |
| `x2_ey_bullets_allowed_fact_ids_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | 11 |
| `x2_ey_bullets_bullet_count_3` | `NOT_OBSERVED` | `FAIL` | `True` | expected exactly 3 bullets |
| `x2_ey_bullets_bullet_no_embedded_newline` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ey_bullets_bullet_single_thought` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_ey_bullets_display_text_proof_authorized` | `NOT_OBSERVED` | `FAIL` | `True` | display text must be rendered from selected proof fact claim_text |
| `x2_ey_bullets_graph_role_episode_bundle_consumed` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_ey_bullets_runtime_real_llm` | `NOT_OBSERVED` | `FAIL` | `True` | runtime_generation_status=BLOCKED |
| `x2_ey_bullets_source_fact_ids_supported` | `NOT_OBSERVED` | `FAIL` | `True` | claim source_fact_ids missing or outside allowed pool |
| `x2_ey_bullets_targeting_only_not_experience_claim` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `None/None FAIL` | - |

## Section: insurtech_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\insurtech_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: ey_narrative

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so EVIDENCE_NOT_RECORDED and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\ey_narrative\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: executive_summary

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_schema_valid, x2_claim_ledger_present, x2_sentence_coverage_present, x2_source_fact_coverage_100, x2_exec_summary_jd_alignment_proof_flags, x2_exec_summary_sentence_count_6, x2_exec_summary_allowed_fact_utilization, x2_executive_summary_synthesis_quality, x2_required_fields_complete, x2_json_parse_valid, x2_no_extra_unrecognized_fields, x2_model_name_allowed, x2_input_output_hashes_present, x2_resume_graph_claim_binding), so JUDGES_NOT_REACHED and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `first_observed_divergence_root_cause` / `NOT_CAUSALLY_ISOLATED`: U0 ingested a different briefing source and the downstream targeting, proof-selection, provider-request, and initial-candidate evidence changed. Without a controlled replay, those upstream changes explain where divergence began but do not prove one sole cause.
- `recovery_failure_root_cause` / `ISOLATED`: Both pre-judge retries were only monotonic improvements: each retained the fact-conflation defect, the retry budget ended, and retry_provider_for_synthesis reverted to the first candidate.
  - Code surface: `apps_rg/runtime/sections/executive_summary_lane.py::retry_provider_for_synthesis`
- `final_gate_root_cause` / `ISOLATED`: Deterministic required-fact finalization changed the published text before X2; the final fragment and fact-conflation checks then blocked judge dispatch.
  - Code surface: `apps_rg/runtime/sections/executive_summary_voice_repair.py::ensure_required_allowed_fact_utilization`

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b622dabd89ba343732c8c774` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `89ac77aba4374e55b71a13bc` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `6273fe0cf27a5c65e6120d3f` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `ee29203fba323d6c5191c8f6` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `2e2ac7608afba98bf659896f` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | X2 failed before judge dispatch | none | `X1D_MODEL_BACKED_JUDGE` | `NOT_RUN` | `JUDGES_NOT_REACHED` | `PRE_JUDGE_BLOCK` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `e3b0c44298fc1c14` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `NO_JUDGE_ROWS_EMITTED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\executive_summary\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_PROVIDER_MODEL_provider_stub_transport_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '81d715adce62625a2391dbea65d4b9c4dafe2fede3cc06cca94b21fcc87f1aa0', 'fec_allowed_fact_ids_digest': '81d715adce62625a2391dbea65d4b9c4dafe2fede3cc06cca94b21fcc87f1aa0', 'fec_narrowed_from_pool': True} |
| `x2_briefing_as_proof_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': [], 'material_delivered_to_l2': True, 'parity_match_generation_judge': True} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_coverage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_claim_field_maps_to_display_sentence` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_claim_text_non_empty` | `NOT_OBSERVED` | `PASS` | `True` | all_rows_non_empty |
| `x2_claim_ledger_materialized_or_gap_excused` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_orphan_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_present` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger is empty or missing. |
| `x2_claim_ledger_row_count_matches_sentence_count` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 0, 'violations': []} |
| `x2_em_dash_count_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_exec_summary_allowed_fact_utilization` | `NOT_OBSERVED` | `FAIL` | `True` | unused_required_allowed_facts=['fact_engineering_platform_001', 'fact_engineering_platform_002', 'fact_engineering_platform_006', 'metric_unify_22m_ip_led_revenue', 'metric_unify_agentic_l0_route_policy_dispatch_surface', 'metric_unify_agentic_tool_sandbox_egress_policy_surface', 'metric_unify_policy_gated_agent_execution_surface', 'reb_ibm_devsecops_release_resilience', 'reb_unify_agentic_platform_architecture', 'reb_unify_platform_commercialization_leadership', 'skill_agentic_platform_productization', 'skill_governed_agentic_systems_architecture', 'skill_ibm_devsecops_pipeline_security', 'skill_unify_agentic_human_override_escalation_paths', 'skill_unify_agentic_l0_route_policy_dispatch', 'skill_unify_agentic_replay_key_audit_manifest_design', 'skill_unify_agentic_runtime_proof_bundle_lineage'] |
| `x2_exec_summary_c03_selected_fact_ids_claimable_subset_allowed_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_colon_stitch_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_cross_fact_conflation_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_cross_sentence_metric_dedup` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_display_override_compliance` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_display_roundtrip_integrity` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_evidence_utilization` | `NOT_OBSERVED` | `PASS` | `True` | ok_pool_below_utilization_threshold |
| `x2_exec_summary_jd_alignment_proof_flags` | `NOT_OBSERVED` | `FAIL` | `True` | missing parsed output |
| `x2_exec_summary_mechanical_opener_stack_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_meta_filler_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_bloated_sentence` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_certifications_section_duplication` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_competencies_duplication` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_credential_dump` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_mechanism_inventory` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_no_sentence_fragment` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_paragraph_max_words` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_prompt_template_authority` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_robotic_transition_stack_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_exec_summary_sentence_count_6` | `NOT_OBSERVED` | `FAIL` | `True` | resume_display_text must have exactly 6 sentences; found 0 (legacy 4–5 and 5–6 bands retired) |
| `x2_exec_summary_strategy_no_commercialization_thread` | `NOT_OBSERVED` | `PASS` | `True` | skipped_not_strategy_lane |
| `x2_executive_summary_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'section': 'executive_summary', 'proof_source': 'augmented_skills_graph', 'proof_pool_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'proof_pool_digest': '9d4800c6d613c08e8047aa315fda8fd8b903764389cfab0390507df1f8c4e92b', 'canonical_evidence_set_digest': '9d4800c6d613c08e8047aa315fda8fd8b903764389cfab0390507df1f8c4e92b', 'id_alias_map': {}, 'claim_evidence_source_type': 'augmented_skills_graph', 'claim_evidence_source_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'skills_authority_source_type': 'augmented_skills_graph', 'skills_authority_status': 'PASS', 'skills_authority_graph_ref': 'apps_rg/fact_inventory/master_skills_arsenal_ledger.json', 'legacy_broad_skills_ledger_skills_authority': False, 'broad_skills_ledger_claim_evidence_only': None, 'allowed_source_fact_ids_count': 17, 'source_fact_ids_checked': [], 'unsupported_source_fact_ids': [], 'rejected_non_proof_source_ids': [], 'jd_or_briefing_ids_rejected': [], 'x2_source_fact_pool_status': 'PASS', 'decisive_reason': 'no_source_fact_ids_collected', 'validator_name': 'evaluate_proof_pool_source_fact_gate', 'skills_authority_x2_boundary': 'PASS', 'x2_srfs_gate_status': 'NOT_APPLICABLE', 'out_of_slice_fact_ids': [], 'srfs_allowed_fact_ids_count': 17, 'selected_role_fact_set_used': False, 'broad_skills_ledger_used': False, 'broad_skills_ledger_used_as_authority': False, 'base_resume_fallback_used': False, 'srfs_section_id': 'executive_summary'} |
| `x2_executive_summary_synthesis_quality` | `NOT_OBSERVED` | `FAIL` | `True` | Output has 0 sentences; executive synthesis requires exactly 6 sentences |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 17, 'violations': []} |
| `x2_first_person_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_generic_filler_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_inline_source_tags_absent` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_input_output_hashes_present` | `NOT_OBSERVED` | `FAIL` | `True` | Missing input/output hashes. |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_summary': {'displayed_claim_count': 0, 'claims_supported_by_selected_resume_facts': 0, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'runtime_summary': {'displayed_claim_count': 0, 'claims_supported_by_selected_resume_facts': 0, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0}, 'coverage_overall_pass': True} |
| `x2_jd_as_proof_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_jd_phrase_copy_violation_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `FAIL` | `True` | parsed_output is None - parsing failed |
| `x2_material_clause_coverage_100` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_metric_fact_id_granularity` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_mixed_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_model_name_allowed` | `NOT_OBSERVED` | `FAIL` | `True` | Model name must match executive_summary primary/backup allowlist when external_claude asserts REAL_LLM provider proof. |
| `x2_no_extra_unrecognized_fields` | `NOT_OBSERVED` | `FAIL` | `True` | parsed_output is None |
| `x2_no_inferred_bridge_claims` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_monolithic_prompt` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_selected_fact_plan_model_echo` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | provider=external_claude, status=BLOCKED |
| `x2_north_star_style_echo_unsupported_zero` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_overbroad_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 17, 'violations': []} |
| `x2_prompt_hash_known` | `NOT_OBSERVED` | `PASS` | `True` | 123f56db5ea54c42 |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | requested=external_claude, attempted=external_claude |
| `x2_required_artifacts_written` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_required_fields_complete` | `NOT_OBSERVED` | `FAIL` | `True` | parsed_output is None |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
| `x2_schema_valid` | `NOT_OBSERVED` | `FAIL` | `True` | Model output did not parse to expected JSON object. |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 0, 'claims_supported_by_selected_resume_facts': 0, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_self_check_claim_ledger_consistent` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_sentence_coverage_pass` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_sentence_coverage_present` | `NOT_OBSERVED` | `FAIL` | `True` | text_claim_coverage missing. |
| `x2_sentence_stacking_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_source_fact_coverage_100` | `NOT_OBSERVED` | `FAIL` | `True` | One or more claims lack allowed source_fact_ids. |
| `x2_source_sensitive_phrases_supported` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_target_company_as_experience_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_target_title_inflation_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_temperature_in_profile` | `NOT_OBSERVED` | `PASS` | `True` | 0.45 |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_unsupported_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_unsupported_industry_claim_zero` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_judge_packet_hash_uniform` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_raw_responses_written` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | deferred_until_post_x2_judge_phase |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |

## Section: headline

### Layperson RCA

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\apps_research\runs\r-a1c74aeba61837293a70a277\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (x2_headline_exactly_one_line, x2_headline_pipe_four_segments, x2_headline_word_count_10_to_13, x2_headline_claim_ledger_rows_present, x2_headline_text_claim_coverage_integrity, x2_headline_source_supported, x2_headline_xyz_literal_grounding, x2_headline_selected_fact_plan_matches_ledger, x2_json_parse_valid, x2_headline_schema_valid, x2_headline_executive_length, x2_headline_jd_context_not_proof, x2_headline_briefing_context_not_proof, x2_headline_companion_context_not_proof, x2_input_usage_accounting_consistent, x2_headline_positioning_bundle_id_required, x2_headline_graph_skill_node_ids_required, x2_headline_source_fact_or_graph_lineage_required, x2_headline_svp_engineering_seniority_required, x2_headline_seniority_floor_met, x2_headline_platform_or_runtime_signal_required, x2_headline_governance_or_regulated_ai_signal_required, x2_headline_technical_specificity_floor_met, x2_resume_graph_claim_binding), so 0.0/4.0 MODEL_BACKED_FAIL and the resume remained blocked.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `NOT_ISOLATED` - -
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `d75ff7ec9aced5b64507928e` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `b622dabd89ba343732c8c774` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `47d41419a4235c588d622375` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `0ffb1ea82c1072aa85466b39` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `edb5a91902ed22e095df462f` | `False` | `CONTRIBUTING` | This changed the material presented to generation or the generated candidate, but no counterfactual replay isolates it as the sole cause. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\raw_model_output.txt` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `c717532a0c40d2ac06800235` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `f7284209739f02fe79d07912` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_BLOCK` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\raw_model_output.txt` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `FAIL` | `NOT_REACHED_X2_FAILED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `9549f916ea880c9e` | Headline line is empty, failing prefix, word count, and structure requirements. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `0.0/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x1d_gemini_provider_response_raw_20260809_072141_638.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `9549f916ea880c9e` | Headline is empty.; Required fixed prefix and four-segment structure are absent.; Word count is 0, outside the required 10–13 range.; No supported executive positioning signals are presented. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `0.0/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x1d_openai_provider_response_raw_20260809_072157_191.json` |
| 5 | `x3_disposition` | `-` | `e3b0c44298fc1c14` | X2 deterministic gate failure | authorize or block product output | `X3` | `FAIL` | `MODEL_BACKED` | `X3_BLOCK` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\sections\headline\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `X2_BLOCK_ID_NAMESPACE_SPLIT` | `NOT_OBSERVED` | `PASS` | `True` | {'disjoint_without_alias': [], 'alias_map_size': 0} |
| `x2_active_pool_digest_matches_fec_digest` | `NOT_OBSERVED` | `PASS` | `True` | {'canonical_evidence_set_digest': '9de857fbb1d8ecbff9db9398bf9df2ff0bad4daf112ba1ca1336b125e9227b1e', 'fec_allowed_fact_ids_digest': '9de857fbb1d8ecbff9db9398bf9df2ff0bad4daf112ba1ca1336b125e9227b1e', 'fec_narrowed_from_pool': True} |
| `x2_briefing_used_as_required_context_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'CONTEXT_INPUT', 'used_for': []} |
| `x2_c0_metrics_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'schema_version': 'c0_metrics.v1', 'required_keys_present': ['blocked_source_refs', 'briefing_source_type', 'citation_map', 'company_brief_provenance', 'evidence_counts', 'excluded_evidence_refs', 'final_evidence_digest', 'freshness_receipts', 'retrieval_mode', 'retrieval_sources', 'route_id', 'run_id', 'schema_version', 'source_class_coverage', 'support_score_profile', 'support_status', 'support_target_met']} |
| `x2_c0_support_status_gate` | `NOT_OBSERVED` | `PASS` | `True` | {'support_status': 'PASS', 'support_target_met': True, 'c0_minimum_safe': True, 'canonical_enum': True} |
| `x2_claim_ledger_source_fact_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'ledger_id_count': 0, 'violations': []} |
| `x2_fec_subset_of_canonical_evidence_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'fec_count': 6, 'violations': []} |
| `x2_headline_active_proof_pool_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | no_source_fact_ids_collected |
| `x2_headline_base_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_base_ngram_overlap_forbidden_or_warn` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_briefing_context_not_proof` | `NOT_OBSERVED` | `FAIL` | `True` | briefing_used_as_proof must be present and exactly false |
| `x2_headline_claim_ledger_no_silent_row_drop` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_claim_ledger_rows_present` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger must contain dict rows with non-empty source_fact_ids (no fabrication). |
| `x2_headline_claim_ledger_segment_decomposition` | `NOT_OBSERVED` | `PASS` | `True` | n/a |
| `x2_headline_companion_context_not_proof` | `NOT_OBSERVED` | `FAIL` | `True` | companion_used_as_proof must be present and exactly false when companion exists |
| `x2_headline_e0_ngram_overlap` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_e0_ngram_overlap_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_headline_exactly_one_line` | `NOT_OBSERVED` | `FAIL` | `True` | Headline must be a single line. |
| `x2_headline_executive_abstraction_floor` | `NOT_OBSERVED` | `PASS` | `True` | {'skipped': True, 'reason': 'skipped_not_four_segments', 'display_tier': 'executive_positioning'} |
| `x2_headline_executive_length` | `NOT_OBSERVED` | `FAIL` | `True` | Headline too long for ATS headline slot. |
| `x2_headline_generic_it_strategy_demote_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_governance_or_regulated_ai_signal_required` | `NOT_OBSERVED` | `FAIL` | `True` | Headline missing governance/regulated-AI positioning signal. |
| `x2_headline_graph_skill_node_ids_required` | `NOT_OBSERVED` | `FAIL` | `True` | No graph_skill_node_ids bound in output/change_log. |
| `x2_headline_jd_context_not_proof` | `NOT_OBSERVED` | `FAIL` | `True` | jd_used_as_proof must be present and exactly false |
| `x2_headline_jd_only_phrase_forbidden` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_candidate_name_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_currency_percent_literals` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_digit_tokens` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_hype_markers` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_inline_source_tags` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_headline_no_keyword_stuffing_heuristic` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_metrics` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_narrowing_it_labels` | `NOT_OBSERVED` | `PASS` | `True` | none |
| `x2_headline_no_standalone_vendor_architecture` | `NOT_OBSERVED` | `PASS` | `True` | {'skipped': True, 'reason': 'skipped_not_four_segments', 'display_tier': 'executive_positioning'} |
| `x2_headline_no_title_inflation` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_no_unsupported_employer_names` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_pipe_four_segments` | `NOT_OBSERVED` | `FAIL` | `True` | must have exactly three ' \| ' separators (four segments) |
| `x2_headline_platform_or_runtime_signal_required` | `NOT_OBSERVED` | `FAIL` | `True` | Headline missing platform/runtime positioning signal. |
| `x2_headline_positioning_bundle_id_required` | `NOT_OBSERVED` | `FAIL` | `True` | No headline_positioning_bundle_id in output/change_log. |
| `x2_headline_positioning_bundles_in_proof_pool` | `NOT_OBSERVED` | `PASS` | `True` | {'bundles_present': True, 'mode': 'headline_positioning_bundle_required'} |
| `x2_headline_positioning_family_preserved` | `NOT_OBSERVED` | `PASS` | `True` | Only 0 positioning families detected (need 2): []. Headline must preserve SVP Engineering positioning families (Agentic AI Platforms, Distributed AI Infrastructure, Runtime Governance, etc.) |
| `x2_headline_prompt_reasoning_receipt_clean` | `NOT_OBSERVED` | `PASS` | `True` | n/a_not_real_llm |
| `x2_headline_raw_model_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | n/a_not_real_llm |
| `x2_headline_schema_valid` | `NOT_OBSERVED` | `FAIL` | `True` | Missing headline schema keys: ['change_log', 'claim_ledger', 'gap_notes', 'headline_line', 'jd_alignment', 'selected_fact_plan', 'self_check'] |
| `x2_headline_segments_quality` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_headline_selected_fact_plan_matches_ledger` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger union empty or selected_fact_plan.required_fact_ids empty. |
| `x2_headline_self_check_consistent` | `NOT_OBSERVED` | `PASS` | `True` | n/a_not_real_llm |
| `x2_headline_seniority_floor_met` | `NOT_OBSERVED` | `FAIL` | `True` | First segment '' is not 'SVP Engineering'. Headline must open with the senior engineering title to preserve seniority posture. |
| `x2_headline_source_fact_or_graph_lineage_required` | `NOT_OBSERVED` | `FAIL` | `True` | No source_fact_ids or graph_lineage_refs bound in output. |
| `x2_headline_source_supported` | `NOT_OBSERVED` | `FAIL` | `True` | claim_ledger must cite active allowed_fact_ids only. |
| `x2_headline_svp_engineering_seniority_required` | `NOT_OBSERVED` | `FAIL` | `True` | First segment '' is not 'SVP Engineering'. Headline must open with the senior engineering title to preserve seniority posture. |
| `x2_headline_technical_specificity_floor_met` | `NOT_OBSERVED` | `FAIL` | `True` | Only 0 positioning families detected (need 2): []. Headline must preserve SVP Engineering positioning families (Agentic AI Platforms, Distributed AI Infrastructure, Runtime Governance, etc.) |
| `x2_headline_text_claim_coverage_integrity` | `NOT_OBSERVED` | `FAIL` | `True` | Segment-level text_claim_coverage failed. |
| `x2_headline_vendor_terms_proof_only` | `NOT_OBSERVED` | `PASS` | `True` | {'skipped': True, 'reason': 'skipped_not_four_segments', 'display_tier': 'executive_positioning'} |
| `x2_headline_word_count_10_to_13` | `NOT_OBSERVED` | `FAIL` | `True` | Word count out of range (count words with pipes as spaces). |
| `x2_headline_xyz_literal_grounding` | `NOT_OBSERVED` | `FAIL` | `True` | headline_line empty; cannot check grounding. |
| `x2_input_usage_accounting_consistent` | `NOT_OBSERVED` | `FAIL` | `True` | section_input_usage_ledger counts mismatch or text_claim_coverage failed |
| `x2_jd_used_as_required_targeting_input` | `NOT_OBSERVED` | `PASS` | `True` | {'required': True, 'used': True, 'authority': 'TARGETING_INPUT', 'used_for': []} |
| `x2_json_parse_valid` | `NOT_OBSERVED` | `FAIL` | `True` | raw_output is missing |
| `x2_no_em_dash` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_no_first_person` | `NOT_OBSERVED` | `PASS` | `True` | absent |
| `x2_no_jd_only_claims` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_non_evidence_inputs_as_claim_evidence` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_non_evidence_inputs_in_source_fact_ids` | `NOT_OBSERVED` | `PASS` | `True` | {'row_scan_found_reserved_non_resume_ids': False, 'ledger_non_evidence_inputs_in_source_fact_ids': False} |
| `x2_no_silent_mock_fallback` | `NOT_OBSERVED` | `PASS` | `True` | Silent mock fallback detected. |
| `x2_no_target_company_as_experience` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_prompt_c0_ids_subset_of_fec` | `NOT_OBSERVED` | `PASS` | `True` | {'prompt_c0_count': 6, 'violations': []} |
| `x2_provider_requested_attempted` | `NOT_OBSERVED` | `PASS` | `True` | Provider mismatch. |
| `x2_resume_graph_claim_binding` | `NOT_OBSERVED` | `FAIL` | `True` | resume_graph_claim_binding_failed |
| `x2_section_claims_supported_by_base_resume` | `NOT_OBSERVED` | `PASS` | `True` | {'displayed_claim_count': 0, 'claims_supported_by_selected_resume_facts': 0, 'claims_with_targeting_input_in_source_fact_ids': 0, 'claims_with_context_input_in_source_fact_ids': 0, 'unsupported_claim_count': 0, 'orphan_source_fact_id_count': 0} |
| `x2_section_input_usage_ledger_present` | `NOT_OBSERVED` | `PASS` | `True` | section_input_usage_ledger_v1 |
| `x2_selected_fact_ids_only` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_title_company_used_as_required_positioning_input` | `NOT_OBSERVED` | `PASS` | `True` | {'target_title': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}, 'target_company': {'required': True, 'used': True, 'authority': 'POSITIONING_INPUT', 'used_for': []}} |
| `x2_x1d_required_judges_present` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_x1d_schema_valid` | `NOT_OBSERVED` | `PASS` | `True` | Blocked judges invalid schema: [] |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `0.0/4.0 FAIL` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `0.0/4.0 FAIL` | - |

## Section: final_resume_aggregation

### Layperson RCA

The prior passing revision authorized final assembly because every required section, including the executive summary, had already cleared its product checks.

The current final assembly did not fail as an independent writing attempt; it was blocked downstream because the executive summary never became eligible for assembly.

No aggregation retry or aggregation judge could repair that upstream section failure, so the underlying executive-summary retry and X2 evidence remains the controlling root cause.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `upstream_section_authorization` - Final assembly was blocked because the executive summary never reached product authorization.
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`

### Underlying Root Cause

- `downstream_root_cause` / `ISOLATED_TO_UPSTREAM_SECTION`: This section was blocked downstream of the executive-summary product-authorization failure.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `90559beb2706e95632500b4b` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `0a0093ffc31878b2d826c48c` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `NO_JUDGE_ROWS` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x3_disposition.json` |

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
| 1 | `initial_generation` | `0` | `-` | initial candidate | dispatch provider generation | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `INITIAL_CANDIDATE` | `-` |
| 2 | `final_x2` | `1` | `-` | all deterministic product gates | evaluate full X2 gate set | `FULL_X2` | `PASS` | `ADVANCED_TO_JUDGES` | `ADVANCED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 3 | `judge_panel` | `-` | `-` | judge evidence absent | none | `X1D_MODEL_BACKED_JUDGE` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_NOT_RECORDED` | `EVIDENCE_GAP` | `NOT_APPLICABLE` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 4 | `x3_disposition` | `-` | `-` | - | authorize or block product output | `X3` | `FAIL` | `-` | `NOT_OBSERVED` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2-worktrees\codex-e2e-defect-remediation-w0\artifacts\apps_rg\runs\w8_anthropic_positive_retry9_20260809\e2e_20260809T071441Z_0e86eeeb\modular_r4\final_resume_assembly\x3_disposition.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `configured_panel` | `NOT_OBSERVED` | `JUDGES_NOT_REACHED` | No current judge rows were emitted because X2 failed first. |
