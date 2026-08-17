# BCG Executive Output - apps_rg Run

Generated: `2026-08-17T02:43:36Z`
Run root: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4`

## Executive Answer

The run reached an authorized product outcome. Preserve the generated outputs and review the run ledger for section and judge proof.

## P0/P1/PX Recommendations

| Priority | Recommendation | Evidence | Gate / Outcome |
|---|---|---|---|
| `PX` | Review L6 shadow observations as future-run hardening inputs, not product blockers. | `competencies: future_run_advisory_only \| unify_bullets: future_run_advisory_only \| ibm_bullets: future_run_advisory_only \| insurtech_bullets: future_run_advisory_only \| ey_bullets: future_run_advisory_only \| unify_narrative: future_run_advisory_only` | Passing run stays authorized; L6 remains advisory unless promoted by policy. |

## Board-Level Readout

| Question | Answer |
|---|---|
| Did apps_research run? | `Yes` |
| Research source class | `FRESH_APPS_RESEARCH` |
| Research input used | `external_openai` |
| Briefing evidence | `auto_research_internal=True; research_delegation_executed=True; source=RUN_SPECIFIC; digest=085b422be4be1a1fd3ccf40e8879b84f1887101acb6c2bafa28834cbf9f322e2; ref=C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\apps_research\runs\bridge_rg_research_bridge_a7c4c601_12e3d55d-133a-43f4-952c-8e4a0acfc9e9\briefing.md; target=Anthropic / Manager of Applied AI Architecture, Partnerships; briefing_text_chars=7256` |
| Did resume generation run? | `11 REAL_LLM section(s)` |
| Source X3 decision | `X3D_ALLOW_FINISH` |
| Completion status | `BLOCKED` |
| Completion fault | `NONE` |
| Final product authorized? | `True` |
| Primary blocker | `BRIEFING_PRESENT:RUN_SPECIFIC` |
| Decision | `Authorized; preserve evidence.` |

## Issue Tree

- No blocking issue tree was generated from section evidence.

## Prior Working Revision Comparison

| Section | Prior PR / commit | Current commit | Inputs match | Provider request match | Output match | Gate delta | Complete |
|---|---|---|---|---|---|---|---|
| `whole_run` | `NO_PRIOR_PASSING_RUN` | `NOT_OBSERVED` | `False` | `False` | `False` | `NOT_OBSERVED/NOT_OBSERVED -> NOT_OBSERVED/X3D_ALLOW_FINISH` | `False` |

## Layperson Retry And Root-Cause Explanation

### whole_run

No prior passing same-scenario run was available, so this report does not claim a before-versus-after recovery result.

The runs first differ at ingestion: the prior run used NOT_OBSERVED, while the current run used C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\apps_research\runs\bridge_rg_research_bridge_a7c4c601_12e3d55d-133a-43f4-952c-8e4a0acfc9e9\briefing.md; later targeting, fact-selection, and provider-request evidence also changed, so the initial text difference cannot be attributed to the code revision alone.

The current run then made 0 pre-judge repair attempt(s), but the recorded defects were not cleared; it reverted to its first candidate, the final deterministic check still failed (failed gates not recorded), so the judges were not reached and the resume remained blocked.

- First observed divergence: `u0_ingress`
- First causally relevant divergence: `NOT_ISOLATED`
- Code cause status: `NOT_APPLICABLE_NO_PRIOR_BASELINE`


## Recommended Next Move

1. Preserve the generated output package and run evidence.
2. Review the mandatory ledger and section-status table for audit details.
3. Treat future edits as new changes requiring the same X2/X3 gates.

## Evidence Map

- Mandatory run ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\02_section_lane_summary_table.md`
- Machine-readable ledger: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\APPS_RG_MANDATORY_RUN_OUTPUT.json`
- Final resume text: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\FINAL_RESUME_OUTPUT.txt`
- Final resume output contract: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\FINAL_RESUME_OUTPUT.json`
- Resume DOCX: `@C:\Git\apps_rg_v2\artifacts\apps_rg\runtime_proofs\full_resume_ff337a0f42e4\outputs/resume.docx`
- Section failure forensics index: `@artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/section_failure_forensics/index.json; @artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/section_failure_forensics/index.md`
- Section forensic RCA: whole_run: `@artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/section_failure_forensics/whole_run.json; @artifacts/apps_rg/runtime_proofs/full_resume_ff337a0f42e4/section_failure_forensics/whole_run.md`
