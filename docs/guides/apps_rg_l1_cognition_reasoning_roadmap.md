# L1 Cognitive Planner Roadmap

Status: replacement plan, derived from the goal of improving L1 cognition and
reasoning. The existing W0-W6 contracts are reusable support code; they are not
this roadmap and do not prove that L1 became more capable.

Scope: `apps_rg_v2` only. Do not add or modify `agentic_core`.

## Goal

Make L1 a materially better planner. Given a U0-validated request, it must:

1. understand the actual goal and constraints;
2. decompose it into atomic, related requirements;
3. deliberate over feasible ways to serve those requirements;
4. challenge its own assumptions before handing work downstream; and
5. revise the affected plan when observed outcomes disprove an assumption.

The success condition is a safer, more compliant downstream artifact—not a
larger L1 schema. L1 remains advisory: it may recommend a plan, uncertainty,
and verification work, but it does not take L0 route authority, C0 evidence
authority, PA prompt authority, or L2/L3 execution authority.

```
U0 request
   |
   v
L1: understand -> decompose -> deliberate -> critique -> revise
   |                  |              |             |          |
   |                  |              |             |          +-- bounded update
   |                  |              |             +-- assumptions and failures
   |                  |              +-- alternative advisory plans
   |                  +-- atomic goal and constraint graph
   +-- source-bound goal frame
```

## Current cognitive gaps

The present v2 capsule improves bookkeeping, but it does not yet supply the
full cognitive loop above.

| Gap | Current behavior | Needed reasoning capability |
| --- | --- | --- |
| Understanding | A bullet or explicit-requirement line is usually one requirement. | Recover atomic requirements, their logical relations, and qualifier scope. |
| Semantics | Type and target choices are mainly keyword/taxonomy matches. | Distinguish actual meaning, unknown concepts, hard constraints, and preferences. |
| Deliberation | The DAG orders work but does not compare ways to satisfy the goal. | Build feasible options, their dependencies, risks, and justification. |
| Critique | Open decisions exist, but L1 does not systematically challenge its plan. | Detect uncovered goals, conflicts, invalid assumptions, and broad targeting before execution. |
| Revision | Failure receipts are available after execution. | Update only the affected belief/plan after an observed contradiction, or escalate. |

## Target cognitive plan

L1 v3 is an immutable, source-bound cognitive plan with five linked ledgers.
Stable IDs and source/receipt references make its reasoning inspectable; raw JD
text remains targeting input and is never candidate evidence.

| Ledger | Cognitive function | Required content |
| --- | --- | --- |
| Goal and constraint frame | Understand success. | Requested artifact, audience, role, hard constraints, preferences, conflicts, input authority, and definition of done. |
| Atomic requirement graph | Decompose meaning. | Atomic requirements, parent/child links, `AND`/`OR`/`NOT`/exception relations, source spans, type, modality, qualifier scope, and unknown semantics. |
| Feasibility graph | Deliberate over options. | Candidate work-unit options, dependencies, needed source/evidence shape, counterevidence risk, and target/escalation rationale. |
| Alternative-plan and critique ledger | Compare and challenge plans. | Primary/alternative plan when there is a real trade-off, coverage/risk rationale, uncovered goals, conflicts, assumptions, counterexamples, and designated resolver. |
| Revision ledger | Learn from observed outcomes. | Parent plan, disproved assumption, observed failure, affected requirement, bounded revision, predicted correction, and escalation when revision is unjustified. |

`MAPPED`, `ESCALATED`, and `UNMAPPED` are separate decisions. Escalation is a
safe result when appropriate; it is not successful targeting, evidence, or
completion.

## Evidence standard

Each wave has one direct capability claim and one acceptance gate. The gate is
not the work; it prevents a plausible implementation from being called an L1
improvement when it did not improve reasoning.

Before the first behavior change, lock a small source-bound development set and
a sealed holdout. Include ordinary, compound, cross-cutting, unknown,
conflicting, stale, and missing-evidence requests. Human review supplies only
semantic labels and final outcome judgments; fixtures and validators never
invent human grades.

Track these outcome measures:

1. **Understanding fidelity**: atomic requirement, relation, type, and
   qualifier accuracy against adjudicated source spans.
2. **Plan coherence**: each critical requirement has a defensible option or an
   explicit escalation; no conflict is silently ignored.
3. **Critique quality**: precision and recall for missing preconditions,
   contradictions, broad mappings, and unsupported assumptions.
4. **Revision quality**: resolvable L1 failures corrected by one bounded
   revision without widening unrelated scope.
5. **Downstream usefulness**: blinded requirement compliance, unsupported claim
   rate, latency, and cost for paired v1/v3 shadow artifacts.

Digests, schema validity, receipt presence, and unit-test counts are regression
checks. They are not cognition measures.

## Priority roadmap

### Wave 0 — Lock the behavioral target

Priority: P0. Small enabling checkpoint; not an L1 cognition claim.

Create the source-bound development/holdout split and a concise scoring guide.
For each request, annotate goal, atomic requirements, constraint relations,
appropriate escalation, and expected completion criteria. Run v1 and current
v2 once to identify the dominant error slice.

Exit:

- The split and guide are locked before candidate tuning.
- The baseline includes source-span examples of decomposition, semantic,
  targeting, critique, and revision failures.
- One priority failure slice is named for Wave 1.

Defense: this is only enough measurement to ensure that the first direct
intervention attacks the real cognitive bottleneck rather than a convenient
infrastructure task.

### Wave 1 — Understand and decompose the request

Priority: P0. First direct cognition intervention.

Capability: L1 produces a goal/constraint frame and atomic requirement graph,
not a list of bullet-sized keyword matches.

Build:

- A deterministic clause and relation parser for bullets and prose. It splits
  conjunctions/disjunctions only when scope is unambiguous; otherwise it keeps a
  source-bound parent and records why review is needed.
- Parent/child requirement identities and `AND`, `OR`, `NOT`, exception, and
  shared-qualifier relationships.
- A constraint frame that separates non-negotiable requirements, preferences,
  output constraints, and conflicting instructions.
- Explicit `UNKNOWN` semantics: a generic `must`/`required` pattern cannot
  disguise an unknown concept as a safe generic type.

Acceptance gate:

- Understanding fidelity improves over v1, especially on compound,
  cross-cutting, and unknown slices.
- Critical qualifier/relation errors do not increase.
- Every split, merge, and unknown result is source-span and rule explainable;
  ambiguity is escalated rather than invented.

Stop: if this capability fails, refine decomposition from observed errors or
reject it. Do not start targeting, scheduling, or replan work.

Defense: this improves the object L1 reasons over. Later stages cannot repair a
plan whose requirements were merged, mis-scoped, or misread.

### Wave 2 — Deliberate over feasible plans

Priority: P0. Second direct cognition intervention.

Capability: for each atomic requirement, L1 reasons about feasible ways to
serve it, what could disprove an option, and whether to target, defer, or
escalate.

Build:

- A feasibility graph linking a requirement to candidate work units, needed
  input/evidence shape, dependencies, and counterevidence risk.
- A primary advisory plan plus an alternative only when there is a real
  trade-off, such as split versus merge work or direct support versus escalation.
- A choice rationale comparing coverage, constraint satisfaction,
  preconditions, and risk. L1 recommends; L0 still selects routes and C0 still
  decides evidence.
- A precise target rule: map only when a work-unit option satisfies the type and
  qualifiers. Otherwise ask the smallest resolver question.

Acceptance gate:

- Plan coherence and targeting precision improve on the holdout.
- Broad mappings decrease or remain zero; appropriate escalation stays high.
- Every critical requirement has a defensible option or a named unresolved
  decision. Escalation never counts as target success.

Stop: reject a decorative alternative-plan ledger, unjustified choices, or any
reversion to one-keyword-to-one-section mapping.

Defense: a DAG only orders work. Deliberation determines whether the work is
actually the right response to the user's goal.

### Wave 3 — Critique the plan before execution

Priority: P1. Third direct cognition intervention.

Capability: L1 performs a bounded adversarial review of its own plan and emits
an actionable critique instead of silently forwarding assumptions downstream.

For every critical requirement, the critique asks:

- Is source and qualifier scope preserved?
- Does the selected plan serve the requirement, or only a related keyword?
- Does another requirement or user constraint conflict with the plan?
- Is a briefing, candidate-evidence, output-format, or downstream-capability
  assumption unsupported?
- Would a counterexample create an unsupported candidate claim or invalid
  completion claim?

The critique ledger contains severity, failed invariant, affected requirement,
counterexample/missing precondition, and permitted resolver. It may block its
own advisory plan or request clarification; it cannot create evidence, choose a
route, or fabricate a resolution.

Acceptance gate:

- Critique quality improves on seeded and natural conflict, missing-
  precondition, and broad-target cases.
- It suppresses no valid critical requirement and creates no candidate-evidence
  claim.

Defense: decomposition and deliberation still fail if their assumptions are not
challenged. This is an inspectable self-correction loop, not hidden
chain-of-thought or an unused model knob.

### Wave 4 — Revise from observed outcomes

Priority: P1. Fourth direct cognition intervention.

Capability: when C0, PA, or L2/L3 reports an observed contradiction of a named
plan assumption, L1 produces one smaller, justified revised plan or escalates.

Build:

- Triggers limited to source-bound failures: unsatisfied requirement coverage,
  C0 contradiction/absence, critique violation, downstream omission, or verified
  execution-precondition failure.
- Assumption-to-outcome links so L1 states what it learned rather than merely
  which receipt failed.
- One revision limited to affected requirements, option, and dependencies.
  Repeated/unchanged diagnostics escalate; they never automatic-retry or change
  routes.
- A parent-versus-revised comparison stating predicted correction and new risk.

Acceptance gate:

- One revision corrects more resolvable L1 planning errors than a no-revision
  control without increasing false targets, unsupported claims, or unrelated
  changes.
- Failures outside L1's causal responsibility are recorded as downstream defects
  and do not trigger arbitrary plan changes.

Defense: a planner reasons over time only if it changes the relevant belief or
plan after a prediction fails. Generic failure records and retry loops are not
learning.

### Wave 5 — Prove the better plan improves the pipeline

Priority: P0 gate for any product-visible use. It adds no new L1 capability; it
proves that Waves 1-4 are useful.

Run paired v1/v3 shadows on the sealed holdout. Bind each requirement and
critique decision to C0, PA, and L2/L3 receipts, then blind-review the final
artifacts. Report understanding fidelity, plan coherence, critique/revision
quality, output requirement compliance, unsupported-claim rate, completion,
latency, and cost.

Promotion requires:

- Meaningful protected-holdout improvement in Wave 1 and Wave 2 measures and
  downstream requirement compliance.
- No safety regression; escalation stays separate from successful targeting and
  C0 remains the evidence authority.
- Human adjudication for ambiguous semantics and named release approval for a
  limited, observable, reversible rollout.
- Requirement-level observation and rollback.

Defense: the goal is a better cognitive plan that causes a safer, more compliant
pipeline result—not a smarter-looking planning artifact.

## Existing code: disposition

Reuse existing v2 capsules, C0 reconciliation, execution receipts, scheduling,
diagnostics, and comparison tooling only where they serve a named capability.

- Keep source spans, taxonomy versioning, immutable capsules, and C0 claim
  boundaries as safety constraints.
- Replace line-level parsing and keyword-only targeting in Waves 1 and 2.
- Reuse the DAG only after Wave 2 gives its nodes and edges feasibility
  rationale.
- Reuse failure diagnostics only after Wave 4 binds them to a disproved L1
  assumption and scored revision result.
- Keep the current W6 comparator as a tamper/determinism regression tool. It
  cannot claim semantic improvement because its fixtures are synthetic and its
  human/runtime outcomes are absent.

No supporting artifact is a roadmap exit condition by itself.

## Pull-request rule

Every L1 change must name:

1. the cognitive capability it changes: understand, decompose, deliberate,
   critique, or revise;
2. the failure slice and source-bound examples it addresses;
3. the expected behavior change from the parent planner;
4. the direct acceptance measure and safety guardrail; and
5. the reject/stop condition that prevents the next wave.

Reject a pull request that adds receipts, schemas, scheduler behavior, model
knobs, or tests without a causal connection to one of the five capabilities.

## Completion definition

This roadmap is complete only when the accepted L1 planner demonstrably
understands, decomposes, deliberates, critiques, and revises better than the
baseline on protected source-bound inputs, and that improvement yields safer,
more compliant downstream artifacts under bounded human-approved rollout.
