# apps_rg Output Bisect

## Section: final_resume_aggregation

### Layperson RCA

Every required section reached X3_ALLOW, so the current run assembled a complete resume candidate and advanced it to the whole-resume coherence panel.

The aggregate panel ran and recorded gemini_pro 4.9/4.0 MODEL_BACKED_PASS; openai_chatgpt 3.8/4.0 MODEL_BACKED_FAIL; the required two-of-two model-backed quorum was not met.

The controlling product defect is aggregate coherence, not upstream section eligibility: Competencies are over-dense and repeat route-policy, governance, co-sell, and solution-mapping themes.; Several competency items are near-synonyms rather than distinct executive capabilities.; Summary S2-S4 is jargon-heavy and delays commercial and organizational impact until S5.; Partnership leadership is fragmented across the headline, competencies, IBM history, and current-role narrative.

### Divergence And Root Cause

- First observed divergence: `u0_ingress` - The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape.
- First causally relevant divergence: `aggregate_coherence_quorum` - Final assembly completed, but the whole-resume model-backed judge quorum failed: Competencies are over-dense and repeat route-policy, governance, co-sell, and solution-mapping themes.; Several competency items are near-synonyms rather than distinct executive capabilities.; Summary S2-S4 is jargon-heavy and delays commercial and organizational impact until S5.; Partnership leadership is fragmented across the headline, competencies, IBM history, and current-role narrative.
- Code cause status: `AGGREGATE_GATE_ISOLATED`

### Underlying Root Cause

- `aggregate_coherence_root_cause` / `ISOLATED_TO_AGGREGATE_JUDGE`: All required section outputs were assembled; final authorization failed because the model-backed whole-resume panel did not reach its required quorum.

### Ingestion-To-Outcome Lineage

| Order | Stage | Prior | Current | Match | Classification | Why | Prior evidence | Current evidence |
|---:|---|---|---|---|---|---|---|---|
| 1 | `u0_ingress` | `NOT_OBSERVED` | `3930f92610071af150a0ed44` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\ingress_raw.json` |
| 2 | `u0_payload` | `NOT_OBSERVED` | `5186c08205c86c20812b6716` | `False` | `CORRELATED_ONLY` | The runs differ here, but the available artifacts do not prove this targeting change caused the failed sentence shape. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\u0_receipt.json` |
| 3 | `jd_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 4 | `briefing_material` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 5 | `targeting_bundle` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 6 | `proof_pool` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 7 | `selected_fact_plan` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\section_input_usage_ledger.json` |
| 8 | `provider_request` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\provider_request.json` |
| 9 | `initial_candidate` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `-` |
| 10 | `retry_loop` | `2304adee64d3547ac7581f6a` | `2304adee64d3547ac7581f6a` | `True` | `RULED_OUT` | The evidence is identical at this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\synthesis_regen_receipt.json` |
| 11 | `deterministic_finalization` | `NOT_OBSERVED` | `NOT_OBSERVED` | `False` | `EVIDENCE_GAP` | Neither run recorded evidence for this stage. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\executive_summary_finalize_coherence.json` |
| 12 | `final_x2` | `NOT_OBSERVED` | `02e78f6172e78860bf9588c7` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\x2_gate_outputs.json` |
| 13 | `judges` | `NO_JUDGE_ROWS` | `6ba078ecdacbaff507cee246` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\x1d_llm_judge_outputs.json` |
| 14 | `x3` | `NOT_OBSERVED` | `X3_REVIEW_AGGREGATION` | `False` | `DOWNSTREAM_EFFECT` | This is an observed consequence of the earlier candidate and recovery differences. | `-` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\x3_disposition.json` |

### Code Bindings

| Role | File | Symbol | Changed in comparison | First change commit / PR | Status |
|---|---|---|---|---|---|
| final resume aggregation and judge quorum | `apps_rg/runtime/assembly/full_resume_llm_coherence.py` | `emit_full_resume_llm_coherence_review` | `False` | `PREEXISTED_BASELINE` | `CURRENT_RUN_EVIDENCE_ISOLATED` |
| final resume release gate | `apps_rg/runtime/assembly/final_resume_x2.py` | `gate_x2_full_resume_llm_coherence_aggregation` | `False` | `PREEXISTED_BASELINE` | `CURRENT_RUN_EVIDENCE_ISOLATED` |

### Prior Passing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `lane_resolution` | `-` | `-` | no prior passing lane was found | none | `NONE` | `NOT_APPLICABLE` | `NO_PRIOR_PASSING_RUN` | `NO_BASELINE` | `NOT_APPLICABLE` | `-` |

### Current Failing Run

| Seq | Phase | Attempt | Candidate | Trigger / defect | Action | Gate scope | Gate result | Judge | Disposition | Acceptance meaning | Evidence |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `assembly_input` | `0` | `91cfc0f3bea82854` | accepted section snapshots | assemble accepted X3 section outputs | `FULL_X2` | `PASS_OR_NOT_TRIGGERED` | `PENDING` | `ADVANCED_TO_X2` | `ASSEMBLED_RESUME_CANDIDATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\final_resume.json` |
| 2 | `final_x2` | `1` | `91cfc0f3bea82854` | structural and aggregate coherence gates | evaluate final resume release gates | `FINAL_RESUME_X2` | `FAIL` | `JUDGES_EVALUATED` | `BLOCKED` | `PRODUCT_GATE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\final_resume_x2_gate_outputs.json` |
| 3 | `judge_panel` | `gemini_pro` | `ee02ffbba85bd266` | Strong narrative alignment from headline through executive summary and professional experience.; Competencies are structured into clean executive capability clusters without credential repetition.; All claims and metrics are grounded in the candidate evidence packet with clear binding. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `PASS` | `4.9/4.0 MODEL_BACKED_PASS` | `JUDGE_PASS` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\coherence_judge_providers\x1d_gemini_provider_response_raw_20260817_032634_766.json` |
| 4 | `judge_panel` | `openai_chatgpt` | `ee02ffbba85bd266` | Competencies are over-dense and repeat route-policy, governance, co-sell, and solution-mapping themes.; Several competency items are near-synonyms rather than distinct executive capabilities.; Summary S2-S4 is jargon-heavy and delays commercial and organizational impact until S5.; Partnership leadership is fragmented across the headline, competencies, IBM history, and current-role narrative. | grade candidate | `X1D_MODEL_BACKED_JUDGE` | `FAIL` | `3.8/4.0 MODEL_BACKED_FAIL` | `JUDGE_FAIL` | `MODEL_BACKED_GRADE` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\coherence_judge_providers\x1d_openai_provider_response_raw_20260817_032710_617.json` |
| 5 | `x3_disposition` | `-` | `dc1fe5b7474364b6` | quorum_not_met | authorize or block product output | `X3` | `FAIL` | `quorum_majority_model_backed` | `X3_REVIEW_AGGREGATION` | `PRODUCT_AUTHORIZATION` | `C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_5862e3a2adf8\modular_r4\final_resume_assembly\full_resume_llm_coherence_review.json` |

### Full X2 Gate Matrix

| Gate | Prior | Current | Changed | Current reason |
|---|---|---|---|---|
| `x2_all_required_sections_present` | `NOT_OBSERVED` | `PASS` | `True` | ['headline', 'executive_summary', 'competencies', 'unify_narrative', 'unify_bullets', 'ibm_narrative', 'ibm_bullets', 'insurtech_narrative', 'insurtech_bullets', 'ey_narrative', 'ey_bullets', 'early_career', 'education', 'certifications'] |
| `x2_artifact_refs_present` | `NOT_OBSERVED` | `PASS` | `True` | {'artifact_refs_ok': True, 'invariant_refs_ok': True, 'section_disposition_refs_ok': True, 'invariant_disposition_refs_ok': True} |
| `x2_certifications_preserved` | `NOT_OBSERVED` | `PASS` | `True` | certifications |
| `x2_company_names_preserved` | `NOT_OBSERVED` | `PASS` | `True` | company_names |
| `x2_dates_preserved` | `NOT_OBSERVED` | `PASS` | `True` | dates |
| `x2_education_preserved` | `NOT_OBSERVED` | `PASS` | `True` | education |
| `x2_final_resume_aggregate_judge_artifact_present` | `NOT_OBSERVED` | `PASS` | `True` | {'full_resume_llm_coherence_review.json': True, 'x1d_full_resume_judge_outputs.json': True} |
| `x2_final_resume_aggregate_judge_executed` | `NOT_OBSERVED` | `PASS` | `True` | True |
| `x2_final_resume_hash_present` | `NOT_OBSERVED` | `PASS` | `True` | dc1fe5b7474364b68aaf9649e7f6f4024c7867e6936f24eec88a306aecf703aa |
| `x2_full_resume_llm_coherence_aggregation` | `NOT_OBSERVED` | `FAIL` | `True` | quorum_not_met |
| `x2_generated_sections_final_materialized_contracts_pass` | `NOT_OBSERVED` | `PASS` | `True` | ['headline:ok', 'executive_summary:ok', 'unify_narrative:ok', 'unify_bullets:ok', 'ibm_narrative:ok', 'ibm_bullets:ok', 'insurtech_narrative:ok', 'insurtech_bullets:ok', 'ey_narrative:ok', 'ey_bullets:ok', 'competencies:ok'] |
| `x2_generated_sections_from_latest_successful_real` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_locations_preserved` | `NOT_OBSERVED` | `PASS` | `True` | locations |
| `x2_locked_sections_from_locked_copy_manifest` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_docx_render` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_generated_section_rewritten` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_l2_generation_calls` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_no_locked_copy_rewritten` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_no_provider_calls` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_section_digest_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_section_hashes_present` | `NOT_OBSERVED` | `PASS` | `True` | ok |
| `x2_section_order_valid` | `NOT_OBSERVED` | `PASS` | `True` | ['headline', 'executive_summary', 'competencies', 'unify_narrative', 'unify_bullets', 'ibm_narrative', 'ibm_bullets', 'insurtech_narrative', 'insurtech_bullets', 'ey_narrative', 'ey_bullets', 'early_career', 'education', 'certifications'] |
| `x2_structural_assembly_no_inline_lane_judges` | `NOT_OBSERVED` | `PASS` | `True` | - |
| `x2_titles_preserved` | `NOT_OBSERVED` | `PASS` | `True` | titles |

### Judge Matrix

| Judge | Prior | Current | Reason |
|---|---|---|---|
| `gemini_pro` | `NOT_OBSERVED` | `4.9/4.0 PASS` | - |
| `openai_chatgpt` | `NOT_OBSERVED` | `3.8/4.0 FAIL` | - |
