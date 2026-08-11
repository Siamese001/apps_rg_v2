# L1 Cognition and Reasoning: Outcome-First Roadmap

Status: replacement plan. The earlier W0-W6 contracts are supporting
infrastructure, not evidence that L1 cognition improved. No wave in this plan
is complete merely because code, receipts, or unit tests exist.

Scope: `apps_rg_v2` only. This plan does not add or modify `agentic_core`.

## Objective

Improve L1's ability to turn a U0-validated job description into a faithful,
atomic, appropriately typed and qualified requirement model; make correct
targeting and escalation decisions; and measurably improve downstream
requirement compliance without increasing unsupported candidate claims.

L1 remains `PLANNING_ADVISORY_ONLY`. It does not select routes, retrieve or
rank evidence, assemble prompts, invoke a model or tool, generate output, write
state, retry work, or authorize Exit. L0, C0, PA, L2/L3, and human reviewers
retain their existing authority. The goal is better planning cognition, not an
authority transfer.

```
U0 -> L1 requirement model -> L0 -> C0 -> PA -> L2/L3 -> Exit
                 |             |      |      |
          measured fidelity     |      |      +-- output compliance evidence
                                |      +-- evidence reconciliation
                                +-- route authority remains outside L1
```

## What counts as improvement

An L1 change is successful only when it beats the frozen v1 baseline on a
protected, source-bound holdout and satisfies every safety guardrail below.
The development set may guide iteration but cannot establish success.

| Outcome | Definition | Authority | Initial promotion threshold |
| --- | --- | --- | --- |
| Atomic segmentation | Exact-match F1 for independently meaningful JD requirements, including conjunctions, disjunctions, and nested qualifications. | Two blinded human adjudicators; an adjudicator resolves disagreement. | At least +0.12 absolute F1 over v1; paired 95% CI lower bound above 0. |
| Requirement typing | Macro-F1 across responsibility, hard requirement, preferred qualification, outcome, scope/scale, leadership, domain, credential, and unknown. | Same adjudicated labels. | At least +0.10 absolute macro-F1; no type loses more than 0.03 F1. |
| Qualifier fidelity | Exact-match F1 for modality, years, location, seniority, scope, recency, and logical relation. | Same adjudicated labels. | At least +0.10 absolute F1; critical-modality false negatives do not increase. |
| Targeting precision | Fraction of mapped requirement-to-work-unit links a reviewer judges appropriate. | Blinded human review. | At least +0.10 absolute precision; broad or unrelated mappings do not increase. |
| Escalation judgment | Precision and recall for cases that should be escalated rather than silently targeted. | Blinded human review. | Precision >= 0.85 and recall >= 0.90, with no critical unknown silently mapped. |
| Evidence and claim safety | For mapped requirements, C0 disposition coverage; unsupported candidate-claim incidence in downstream output. | C0 receipt plus independent output review. | 100% mapped-obligation reconciliation; no increase in unsupported-claim rate. |
| Downstream usefulness | Requirement-compliance rate in the produced section/resume artifact, measured against the same held-out requirement ledger. | Blinded output review. | At least +0.08 absolute compliance; no material degradation in factuality or style controls. |
| Operating cost | End-to-end completion, latency, and cost for the same held-out inputs. | Runtime telemetry. | No more than 10% p95 latency or cost increase unless separately approved. |

These thresholds are hypotheses, not retrospective score targets. The exact
scoring guide, holdout identities, and analysis script must be locked before a
candidate implementation is evaluated. If corpus size makes a confidence
interval unstable, increase the holdout before changing a threshold.

### Non-negotiable metric rules

- `MAPPED`, `ESCALATED`, and `UNMAPPED` are separate states. Escalation is a
  safe outcome, never evidence of successful targeting or coverage.
- `critical_targeted_rate` counts only correct `MAPPED` links.
- `critical_c0_reconciled_rate` counts only mapped critical requirements with
  exactly one C0 disposition. It cannot include escalated requirements.
- `appropriate_escalation_rate` is reported separately from targeting.
- Requirement counts, schema validity, digests, and contract tests are harness
  health metrics; they are not cognition metrics.
- A synthetic fixture can test deterministic behavior but cannot substitute for
  semantic ground truth, human judgment, or protected-holdout evidence.

## Current-state diagnosis

The existing v2 capsule is a useful candidate, not a proven improvement. It
already supplies source spans, a taxonomy, decision ledger, evidence-obligation
ledger, and work DAG. The current comparison harness is insufficient as an
outcome benchmark because it uses four synthetic single-statement development
fixtures, has no holdout results or human grades, records runtime metrics as
unmeasured, and treats escalation as critical coverage.

Existing supporting code remains valuable only when it enables a listed
experiment:

| Existing capability | Keep for | Do not claim |
| --- | --- | --- |
| v2 capsule, taxonomy, and source spans | Candidate representation and baseline comparator. | Semantic parsing accuracy. |
| C0 obligation receipt | Measuring reconciliation and unsupported-claim safety. | Evidence quality or candidate qualification. |
| L2/L3 control receipt | Verifying a requested control was actually executed. | Better L1 reasoning. |
| Governed L3 schedule | Measuring whether a valid plan can be consumed safely. | Better targeting or output quality. |
| W5 diagnostic/replan receipt | Failure analysis after an observed outcome. | Learning or correction effectiveness without a measured rerun. |
| Existing W6 comparator | Determinism/tamper regression. | Protected-holdout improvement or promotion readiness. |

## Required experimental assets

Before changing L1 behavior, create and lock the following app-owned assets.
They are work products, not optional documentation.

1. A source-bound corpus with at least 150 JD examples, stratified across
   straightforward, multi-requirement, compound, cross-cutting, unknown type,
   stale brief, conflicting constraint, absent candidate evidence, preferred
   qualification, scope/scale, credential, and multi-section cases.
2. A development/protected split by job description, not by individual line,
   so near-duplicates cannot leak across splits. The protected input set stays
   outside developer access after sealing.
3. A versioned annotation guide that defines atomic segmentation, type,
   qualifiers, target units, escalation, and permitted `UNKNOWN` use; it must
   include positive and counterexamples.
4. Two independent blinded annotations per holdout example plus an adjudication
   record. The corpus must preserve source spans and annotation provenance.
5. A deterministic scoring program that compares v1 and v2 from their emitted
   planning artifacts and emits per-example errors, aggregate metrics,
   confidence intervals, and slice metrics.
6. A shadow-run harness that binds the selected L1 plan to C0/PA/L2 receipts and
   presents final artifacts to blinded reviewers without revealing v1/v2.

No implementation wave may begin until its evaluation inputs and success rule
are frozen. No production or product-visible gate changes may occur before the
protected-holdout and human-review gates pass.

## Prioritized roadmap

### Wave A — Establish semantic ground truth and the v1 baseline

Priority: P0. This is measurement work, not a cognition improvement claim.

Deliverables:

- Lock the annotation guide, source-bound corpus manifest, development split,
  and externally sealed protected holdout.
- Collect blinded human annotations and adjudication for atomic requirements,
  type, qualifiers, targeting, and escalation.
- Run the current v1 planner and score every metric in the objective table.
- Publish an error taxonomy with counts and concrete source spans: missed
  atomic requirement, merged conjunction, wrong type, dropped qualifier, broad
  mapping, wrongful escalation, missed escalation, and downstream omission.

Exit gate:

- Corpus provenance, split isolation, agreement, adjudication, and v1 score
  report are independently reproducible.
- The baseline includes per-slice results and an error set large enough to
  select the next intervention. A test-only fixture corpus is not sufficient.

Stop rule: if annotator agreement is inadequate, revise the guide and reannotate
before looking at candidate v2 results. Do not tune the planner against an
ambiguous label set.

Defense: without a semantic baseline, every later wave can prove only that L1
emits a well-formed artifact. This wave makes the requested improvement
falsifiable.

### Wave B — Atomic requirement segmentation and qualifier parsing

Priority: P0. This is the first direct L1 cognition intervention.

Hypothesis: a source-span-preserving deterministic parser that splits explicit
conjunctions/disjunctions into linked atomic requirements, while retaining a
parent relation and qualifier scope, will improve segmentation and qualifier
fidelity over v1 without raising false positives.

Implementation scope:

- Replace line-as-requirement behavior with a deterministic clause parser for
  bullets and prose. It must identify conjunction, disjunction, exception, and
  shared-qualifier scopes; ambiguous cases remain one source-bound parent and
  become `ESCALATED`.
- Add stable parent/child requirement IDs and source spans for each child.
- Extend the taxonomy only where the Wave A error taxonomy demonstrates a
  recurring gap. A generic keyword rule is not a substitute for a semantics
  rule.
- Preserve raw JD as targeting input only; no candidate-evidence assertion is
  permitted.

Evaluation gate:

- Development tuning may continue only while protected input remains sealed.
- On the holdout, atomic segmentation and qualifier fidelity must meet their
  objective thresholds, and critical-modality false negatives must not rise.
- Report every split/merge error by source span and slice.

Stop rule: if segmentation does not meet threshold, do not proceed to targeting,
  scheduling, control, or replan work. Improve parsing based on adjudicated
  errors or reject the candidate.

Defense: this directly corrects the current failure mode in which compound and
cross-cutting statements remain a single escalated requirement. It improves the
object L1 reasons over rather than merely recording that it failed to reason.

### Wave C — Requirement typing, targeting, and calibrated escalation

Priority: P0. This is the second direct L1 cognition intervention.

Hypothesis: type classification that considers atomic clause structure and
qualifier scope, plus a conservative target policy, improves precise mapping
while routing genuine ambiguity to review instead of broadly mapping it.

Implementation scope:

- Classify each atomic requirement using the locked taxonomy and deterministic
  rules that expose their rule/source evidence.
- Produce target candidates only when the type, qualifier, and available
  work-unit semantics support a single defensible target. Otherwise record an
  explicit reasoned escalation.
- Add an explicit `UNKNOWN` branch that is exercised by the benchmark; do not
  let a generic `must` rule disguise an unknown concept as a hard requirement.
- Record targeted, escalated, and unmapped states independently. Only mapped
  requirements create a C0 evidence obligation; escalations create a human or
  upstream decision item, not a fake evidence request.

Evaluation gate:

- Type macro-F1, targeting precision, escalation precision/recall, and broad
  mapping all meet the objective thresholds on the protected holdout.
- Every critical unknown is escalated; every target error is inspectable from
  rule ID and source span.

Stop rule: if targeting precision improves by sacrificing escalation recall, or
vice versa, keep the candidate in development. The acceptance decision requires
both measures and the false-target guardrail.

Defense: L1 reasoning is useful only when it makes the correct distinction
between a request that can be targeted and one whose meaning remains unresolved.

### Wave D — Prove downstream plan consumption and output usefulness in shadow

Priority: P1. This verifies that a better plan changes useful work without
changing L1's authority.

Hypothesis: when C0, PA, and L2/L3 consume the richer plan as bounded advisory
input, output requirement compliance improves without increasing unsupported
claims, latency, or cost.

Implementation scope:

- Run paired v1/v2 shadows against identical source-bound requests.
- For each mapped requirement, record C0 disposition, PA inclusion/exclusion
  decision, and L2/L3 output compliance evidence. For each escalation, record
  that it was not silently converted into a candidate claim.
- Keep route selection, evidence authority, prompt authority, and execution
  authority where they are. This wave may add observations and bounded consumer
  behavior, but must not give L1 a route, retrieval, model, or write capability.

Evaluation gate:

- Blinded output review meets downstream-compliance and unsupported-claim
  thresholds on the protected holdout.
- Runtime telemetry meets the operating-cost threshold.
- Every claimed downstream benefit is traceable to a requirement-level plan
  decision; a digest-only lineage is insufficient.

Stop rule: if a richer plan does not improve downstream compliance, do not
continue with scheduling or replanning changes. Diagnose whether the problem is
the L1 representation, a consumer that ignored it, or the evaluation itself.

Defense: a planning improvement matters only if downstream owners can consume
it into safer, more compliant artifacts. This establishes that causal link while
preserving the spine's authority boundaries.

### Wave E — Error-directed replanning experiment

Priority: P2. This is a direct reasoning-feedback experiment, not a generic
replan implementation task.

Hypothesis: a bounded revision that receives an observed, requirement-level
failure can correct a new, resolvable planning error more often than v1 without
looping or widening scope.

Implementation scope:

- Use only failures observed in Wave D: segmentation error, target error,
  unresolved mapped evidence, downstream omission, or explicitly supported
  transport failure.
- Generate a revised advisory plan limited to the affected requirement and
  cited evidence. Unchanged, unresolvable, or repeated diagnostics escalate to
  the designated resolver; they never cause automatic retry or route changes.
- Compare one bounded revision with a no-revision control on a distinct,
  predeclared protected slice.

Evaluation gate:

- The revision improves the resolvable-error correction rate by at least 0.10
  absolute, does not increase false targeting or unsupported claims, and never
  exceeds one candidate revision in the experiment.

Stop rule: if the failure source is not attributable to L1 planning, record it
as a downstream defect and do not use it to tune L1.

Defense: feedback improves reasoning only when it corrects a demonstrated
planning mistake. Bounded scope prevents receipt-driven retry loops from being
mistaken for learning.

### Wave F — Independent decision and limited promotion

Priority: P1 after Waves B-D pass; P2 after Wave E.

Deliverables:

- Independent review packet containing protected-holdout metrics, confidence
  intervals, error slices, blinded human adjudication, downstream artifact
  review, safety results, runtime telemetry, and rollback plan.
- A signed decision that states whether the candidate is rejected, remains in
  shadow, or is approved for a narrow product-visible consumer change.

Promotion gate:

- Every objective threshold passes on the protected holdout.
- No safety guardrail regresses.
- Named human/release authority signs the decision.
- The first release is limited, observable, reversible, and evaluated against
  the same metrics. Passing unit tests, technical receipts, or a development
  corpus cannot authorize it.

Defense: the plan's objective is an outcome claim. Promotion must therefore be
based on outcome evidence rather than on implementation completeness.

## Work explicitly removed from the critical path

The following may be maintained when needed, but cannot be scheduled as an L1
cognition wave or cited as success by themselves:

- new digest fields, receipt formats, artifact filenames, or serializers;
- generic DAG scheduling policies and orchestration plumbing;
- control-execution telemetry without a demonstrated L1-quality effect;
- failure taxonomy expansion without a scored correction experiment;
- synthetic fixture count growth without adjudicated semantic labels;
- prompt knob changes such as ToT, self-consistency, or reflection unless the
  execution lane proves they were applied and a controlled experiment shows a
  protected-holdout benefit.

## Decision protocol for every proposed change

Every pull request affecting L1 must state, before implementation:

1. The one L1 failure mode it addresses, linked to Wave A adjudicated errors.
2. The causal hypothesis and the exact metric expected to improve.
3. The fixed safety and cost guardrails.
4. The development-only tests and the protected-holdout analysis that will
   decide acceptance.
5. The stop/reject condition and rollback behavior.

Reviewers reject a change if it substitutes a receipt, schema, test count, or
runtime trace for the declared outcome evidence.

## Completion definition

This roadmap is complete only when an independently reproducible protected
holdout demonstrates that the accepted L1 candidate meets every objective and
safety threshold, downstream output usefulness improves, and named authority
approves the bounded promotion. Until then, work may be described only as
baseline creation, candidate implementation, shadow evidence, or rejected
experiment—not as an L1 cognition improvement.
