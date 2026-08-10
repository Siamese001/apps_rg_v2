# L1 Cognition and Reasoning Roadmap

Status: Waves 0-5 implemented and verified; Wave 6 remains proposed.

Branch baseline: local `main` at `8d7432fdb6c485f48a520cb4bc813cd8683d7e68`

## Decision

Improve L1 by making its deterministic plan a useful, source-bound decision
model that downstream owners must explicitly reconcile, rather than simply
increasing declared model-reasoning knobs. Preserve the spine and its authority
boundaries:

```
U0 -> L1 -> L0 -> C0 -> PA -> L2 -> Exit
     plan   route  evidence prompt execution
```

L1 remains `PLANNING_ADVISORY_ONLY`: it must not choose a route, retrieve or
rank evidence, assemble prompts, call a model or tool, write state, retry work,
or authorize Exit. L0 remains the route authority; C0 remains the evidence
authority; PA owns prompt assembly; L2/L3 own execution and must prove what was
actually applied.

## Evidence and diagnosis

| Finding | Evidence | Why it limits reasoning |
| --- | --- | --- |
| The capsule is trustworthy but planning-only. | `l1_planning_capsule.py` makes an immutable, digest-bound capsule and asserts no route, retrieval, prompt, model, tool, or L4 authority. | This is the correct boundary, but L1 needs a richer decision object for later owners to act on. |
| Requirement extraction is intentionally narrow. | `_extract_jd_obligation_texts()` uses line/bullet and explicit-requirement regexes; `_jd_obligation_unit_ids()` maps keyword matches to broad resume sections. | Compound requirements, conditions, scope qualifiers, and cross-cutting requirements can be flattened, broadly mapped, or only escalated. |
| The dependency graph is generic. | `_dependency_sketch()` emits only `role_analysis -> unit` and `source_resume_facts -> unit` edges. | It cannot express evidence-before-generation, validation-before-merge, optional work, or precise reasons to wait. |
| C0 records L1 lineage but does not prove semantic plan consumption. | `c0_planned_binding.py` requires a capsule digest in the FEC; `c0_binding.py` derives `retrieval_plan_ref` by hashing the `evidence_plan`. | A run can be lineage-correct while no receipt says whether every planned requirement was supported, contradicted, or unresolved. |
| PA preserves L1 hashes. | `pa_planned_binding.py` verifies hashes for the capsule, prompt plan, completion criteria, and requested cognition plan. | Hash preservation is necessary, but it does not show that a prompt or generation used the intended evidence/control semantics. |
| Cognition controls are requests, not execution proof. | Each `cognition_plan` row sets `controls_applied=False` and `ADVISORY_ONLY_UNTIL_L2_RECEIPT`; singleton provider transports can ignore ToT/reflection knobs. | Raising self-consistency, ToT, or reflection values now would make the plan look stronger without demonstrating stronger execution. |
| Replanning classifies failures without a structured cause ledger. | W1 produces per-unit observations and W2 maps frozen failure codes to the next owner. | The next plan cannot distinguish an input defect, missing source, failed retrieval, unmet requirement, unsupported control, or generation defect precisely enough to learn safely. |

Current focused regression baseline: `68 passed, 1 skipped` across the L1
capsule, JD obligation, reconciliation, and failure-aware replan suites. A real
non-product L1 invocation produced `READY`, seven work units, fourteen generic
dependency edges, three obligations (two critical mapped and one critical
escalated), generic `collect_support_for_<unit>` C0 intents, and no applied
cognition controls.

## Priorities

| Priority | Recommendation | Wave | Defense |
| --- | --- | --- | --- |
| P0 | Freeze an apps_rg_v2-only behavioral baseline before changing the plan contract. | 0 | A v2 plan must be compared to the present L1, C0, PA, L2, W1, and W2 behavior in this repository. This prevents an architecture improvement from becoming an unmeasured change in output, latency, or claim safety. |
| P1 | Make the L1 plan a structured requirement, uncertainty, evidence-obligation, and work-dependency model. | 1 | Better reasoning begins with a better representation of the problem. This replaces broad keyword-to-section intent with source-span-bound deterministic planning while making no candidate-evidence claim. |
| P1 | Make C0 and L2/L3 reconcile, not merely hash, the plan. | 2-3 | A cognition plan is useful only if later stages report the requested versus observed result. This closes the gap between a digest-bound intention and actual evidence/control execution. |
| P2 | Use a typed, acyclic work graph and explicit readiness conditions. | 4 | It makes multi-unit work explainable and safely schedulable without letting L1 select the route or launch work. |
| P2 | Turn W1/W2 into evidence-backed failure diagnosis and bounded plan revision. | 5 | Feedback becomes informative only when a replan can name the missing or failed requirement, cite its receipt, and prevent unbounded retry loops. |
| P3 | Promote only after comparative evaluation and human review of ambiguous cases. | 6 | A richer plan can increase coverage while also increasing false targeting. Measured comparison and named authority are required before a production posture changes. |

Do not start by raising the numeric ToT, self-consistency, or reflexion values.
They are presently copied into L1's requested-control rows, and some provider
lanes document those orchestration knobs as ignored. First prove execution and
measure quality; only then tune controls whose execution receipt says they were
applied.

## Target L1 plan contract

Introduce `apps_rg_l1_planning_capsule.v2` alongside the immutable v1 capsule.
V1 remains readable until all canonical consumers accept v2. The v2 capsule
must have a canonical JSON digest, immutable representation, exact planning
profile digest, and the existing non-authority assertions.

### 1. Source-bound requirement ledger

Replace free-form/broad JD targeting with a deterministic ledger produced only
from U0-validated inputs:

- Stable requirement ID, exact JD source span/digest, section, and ordinal.
- Type: responsibility, hard requirement, preferred qualification, outcome,
  scope/scale, leadership, domain, credential, or unknown.
- Modality and qualifier: must/preferred, years, location, seniority, domain,
  scope, recency, and conjunction/disjunction when explicitly present.
- Criticality and extraction confidence for parsing quality, never candidate
  qualification.
- Explicit target work-unit candidates and `MAPPED`, `UNMAPPED`, or
  `ESCALATED` status. An ambiguous critical requirement escalates; it is never
  silently spread across unrelated sections.

Use a versioned app-owned taxonomy/profile and keep the extraction deterministic.
It need not call a model. Keep raw JD as targeting input only; neither L1 nor
the ledger may assert that the candidate satisfies a requirement.

### 2. Decision and uncertainty ledger

Extend the current missing-field ambiguity register with typed, source-bound
planning conditions:

- Missing or inconsistent identity, role, level, JD, resume, output format,
  and authoritative briefing status.
- Requirement parsing ambiguity, unknown taxonomy, compound requirement,
  unsupported source class, and conflicting user constraint.
- A unique decision ID, severity, blocking policy, affected requirement/unit,
  permitted resolver (`U0`, `C0`, `L2`, or human), and resolution-evidence
  shape.

The register changes L1 readiness only where the profile says it should. It must
not inspect retrieved evidence, invent a conflict, or authorize a resolution. A
valid U0 briefing remains an upstream prerequisite for product-visible
generation; L1 only carries its already-validated provenance and status.

### 3. Evidence-obligation ledger

Replace each generic `collect_support_for_<unit>` row with per-requirement
advisory retrieval intent:

- Required versus optional source classes and source role:
  `candidate_support`, `candidate_counterevidence`, `JD_targeting`, or
  `company_context`.
- Minimum evidence shape and allowed absence disposition, not an evidence item
  or relevance judgment.
- Required contradiction/absence check, affected work units, and the C0
  receipt fields that must be returned.

This gives C0 an auditable question to answer without making L1 a retriever or
ranker. C0 can return `SUPPORTED`, `CONTRADICTED`, `INSUFFICIENT`, or
`NOT_APPLICABLE` with its own evidence references. Only C0's final evidence
contract remains authoritative for claims.

### 4. Work graph and control intent

Replace the generic dependency sketch with a validated DAG of advisory work
nodes. Each node names input artifacts, evidence-obligation IDs, readiness
conditions, expected output contract, validation dependency, and only the
permitted downstream owner. Edge kinds are limited to `REQUIRES_EVIDENCE`,
`REQUIRES_VALIDATION`, `ENABLES`, and `MERGE_AFTER`.

Keep requested model controls in `cognition_plan`, but add explicit control
semantics: `requested`, `required_for_certification`, `transport_supported`,
and `receipt_required`. L1 may never set `applied`; L2/L3 must produce that
fact.

## Wave plan

### Wave 0 — Freeze an apps_rg_v2-only proof baseline

Owner: apps_rg_v2 maintainer.

Implementation: `l1_reasoning_baseline.py` now emits a privacy-safe,
digest-bound `l1_reasoning_baseline.json` from a verified v1 capsule and any
already-produced L0/C0/PA/L2/W1/W2 artifacts. The capture is observation-only;
it does not invoke those stages or authorize an outcome.

1. Capture current v1 capsules for representative full-resume and section-regen
   fixtures, including the ambiguity register, requirement plan, evidence plan,
   cognition plan, and route-hint digest.
2. Capture the existing apps_rg_v2 C0 FEC, PA artifact, per-section L2/control
   receipts, W1 reconciliation, and W2 replan decision for the same fixture
   inputs where those stages are exercised.
3. Freeze the focused test suite and comparison inputs used in Waves 1-6. Keep
   the fixtures source-bound and separate development cases from holdout cases.

Exit criteria: the before-state is reproducible from apps_rg_v2 inputs, every
artifact is tied to one run/request/trace identity, and the baseline makes no
production-authorization claim.

### Wave 1 — Build L1 v2 as a better deterministic decision model

Owner: apps_rg.

Implementation: `l1_planning_capsule_v2.py` now emits a separate immutable
`apps_rg_l1_planning_capsule.v2`, bound to the exact v1 planning profile bytes
and the app-owned `rg_l1_requirement_taxonomy.v1.json`. It contains source-span
and digest-bound U0-JD requirements, an open typed decision ledger, advisory C0
evidence obligations, and an acyclic work DAG. `l1_binding.py` carries it beside
the unchanged v1 projection; L0 signs its identifiers as advisory lineage only,
without treating v2 status as route authority or a new gate.

Primary files:

- `src/apps_rg/runtime/bindings/l1_planning_capsule.py`
- `src/apps_rg/runtime/bindings/l1_planning_capsule_v2.py`
- `src/apps_rg/runtime/bindings/l1_binding.py`
- `src/apps_rg/profiles/rg_planning_profile.yaml`
- `src/apps_rg/profiles/rg_l1_requirement_taxonomy.v1.json`
- New app-owned requirement/uncertainty taxonomy profile under
  `src/apps_rg/profiles/`.
- `tests/unit/apps_rg/runtime/bindings/test_l1_jd_obligation_plan.py` and new
  v2 capsule/fixture tests.

1. Define v2 schemas, canonical ordering, digest rules, v1/v2 compatibility,
   and fail-closed validation. Do not mutate a v1 capsule in place.
2. Implement the source-span-bound requirement parser and typed decision ledger
   from U0 payloads only.
3. Emit the evidence-obligation ledger and validated work DAG. Detect duplicate
   requirements, orphaned nodes, cyclic edges, and critical unknowns.
4. Thread only advisory v2 identifiers through `L1PlanContract` projections and
   L0's signed binding. L0 still owns the selected route.

Exit criteria:

- Same U0 payload and profile bytes yield byte-stable v2 capsules.
- A critical compound/unknown requirement is targeted precisely or escalated.
- V2 contains no route authority keys, evidence items, provider calls, or
  mutable state.
- Existing v1 integration continues to pass until Wave 2 enables v2 consumption.

### Wave 2 — Make C0 prove evidence-plan consumption

Owner: apps_rg C0 owner.

Implementation: `l1_evidence_obligation_receipt.py` now builds a C0-owned,
digest-bound sidecar from the verified v2 ledger. Every L1 obligation receives
exactly one C0 disposition. C0 considers only requirement-bound, C0 candidate
evidence; generic retrieved material remains `INSUFFICIENT`, while inline JD
targeting is always excluded. `c0_binding.py` attaches the ledger and receipt
digests (and, when an artifact directory is supplied, the canonical relative
receipt reference) to compatible FEC audit references. The planned C0 boundary
independently rebuilds the sidecar and rejects a hash-only v2 lineage claim.
This remains comparison/shadow evidence: it neither changes C0 support gating
nor grants L1 evidence authority.

Primary files:

- `src/apps_rg/runtime/bindings/c0_planned_binding.py`
- `src/apps_rg/runtime/bindings/c0_binding.py`
- `src/apps_rg/runtime/spine/section_c0_retrieve.py`
- `src/apps_rg/runtime/contracts/l1_evidence_obligation_receipt.py` and tests.

1. Have the planned C0 boundary read and validate the v2 evidence-obligation
   ledger rather than only include its digest in `retrieval_plan_ref`.
2. Emit a digest-bound C0 sidecar receipt per requirement: source role, evidence
   references, C0 support disposition, contradiction-scan status, and reason
   for unresolved/not-applicable results. Keep the FEC shape compatible by
   linking the sidecar through FEC audit references.
3. Require exact coverage: every L1 evidence obligation has one C0 disposition;
   a C0 receipt cannot add an L1 obligation or convert JD targeting into
   candidate evidence.
4. Start in comparison/shadow mode against v1; then turn on a narrow
   fail-closed gate for critical unsupported requirements after Wave 6 approval.

Exit criteria:

- No canonical C0 run can claim v2 plan consumption from a hash alone.
- Every critical requirement is `SUPPORTED`, `CONTRADICTED`, `INSUFFICIENT`, or
  `NOT_APPLICABLE` with source-bound reason/evidence references.
- C0 remains the only evidence authority.

### Wave 3 — Prove applied cognition controls and generation constraints

Owner: apps_rg execution and lane owners. Keep the new receipt app-local to
apps_rg_v2.

Implementation: `reasoning_control_execution_receipt.py` now emits a
digest-bound, per-unit L2/L3 execution sidecar from a verified L1 capsule.
It records the L1 request separately from L2/L3 transport observation,
provider/model configuration, candidate count, selection method, C0 obligation
receipt references, and an explicit quality-certification result. W1 stores
each sidecar under `reasoning_control_execution/<unit>.json` and reconciles
its digest, applied-control summary, quality result, and C0 references with the
unit outcome. Existing phase-1 lane records can substantiate temperature and
self-consistency observations only; absent ToT/reflection transport evidence
is recorded as `IGNORED`, never inferred from L1's requested values.

Primary files:

- `src/apps_rg/runtime/contracts/reasoning_control_execution_receipt.py`
- `src/apps_rg/runtime/contracts/plan_execution_reconciliation.py`
- `src/apps_rg/runtime/reasoning/section_reasoning_intensity.py`
- `src/apps_rg/runtime/bindings/l1_planning_capsule.py`
- `tests/unit/apps_rg/runtime/contracts/test_reasoning_control_execution_receipt.py`
- `tests/unit/apps_rg/runtime/contracts/test_plan_execution_reconciliation.py`

1. The fixed app-local policy derives certification requirements from the
   requested values. A capsule cannot lower that policy by declaring a required
   control optional.
2. A required control that is `UNSUPPORTED`, `IGNORED`, or `BLOCKED` denies
   quality certification. Non-required controls remain visible diagnostics.
3. W1 marks an otherwise-complete unit `BLOCKED` with
   `REQUIRED_CONTROL_EXECUTION_ABSENT` until every certification-required
   control is observed as `APPLIED` or `ADAPTED`.
4. Controlled ablations may now be considered, but only for controls whose
   L2/L3 receipt proves transport support and recorded execution. This receipt
   remains execution observability; it neither promotes evidence nor authorizes
   routing, Exit, release, or human qualification.

Exit criteria:

- `controls_applied` is only emitted by L2/L3 and is never copied from L1.
- A singleton transport that ignores a requested knob cannot be certified as
  having applied it.
- A completed W1 unit cannot be quality-certified from an output file alone
  when a certification-required control lacks execution proof.

### Wave 4 — Use the plan graph for governed scheduling and merge checks

Owner: apps_rg orchestration owner.

Implementation: the v2 DAG now adds `merge:final_resume` and one
`MERGE_AFTER` edge from every unit validation node for multi-unit work. The
app-local `governed_l3_schedule.py` validates the v2 graph, the C0
evidence-obligation sidecar, and (when present) the W1 reconciliation with its
W3 control receipts. `l3_schedule_apps_rg()` exposes that L3-owned scheduling
seam without modifying the generic runtime contract.

Primary files:

- `src/apps_rg/runtime/bindings/l1_planning_capsule_v2.py`
- `src/apps_rg/runtime/bindings/l3_binding.py`
- `src/apps_rg/runtime/contracts/governed_l3_schedule.py`
- `tests/unit/apps_rg/runtime/contracts/test_governed_l3_schedule.py`

1. L3 uses its fixed `TOPOLOGICAL_LEXICAL_SERIAL` policy and records every
   selected node in its own one-item parallel batch. L1 contributes the DAG and
   no order, parallelism setting, retry, route, or execution decision.
2. A valid C0 obligation receipt is required before a work unit is selected.
   Before W1 exists, validation and merge nodes remain deferred. W1-completed
   units require a W3 quality-eligible control receipt before their validation
   predecessor is satisfied.
3. The merge node is selected only after every `MERGE_AFTER` validation node is
   satisfied. A skipped or blocked predecessor blocks the merge; no output file
   or L1 declaration can bypass the C0/W3 receipt checks.
4. The receipt is digest-bound, run/request/trace-bound, uses relative receipt
   references, and asserts that it neither dispatches work nor changes evidence,
   prompt, route, Exit, human-review, or release authority.

Exit criteria: the L3 receipt explains every selected, deferred, blocked, or
skipped node from the verified L1 graph and current C0/W1/W3 receipts; no
scheduling authority has moved into L1.

### Wave 5 — Make replan feedback diagnostic and bounded

Owner: apps_rg.

Implementation: W5 retains the legacy W2 decision for compatibility and adds
an app-local v2 diagnostic/replan pair. The diagnostic receipt validates the
same taxonomy as W1, then binds the verified L1 v2 capsule, C0 obligation
sidecar, W1/W3 reconciliation, and W4 L3 schedule. It records only observed
causes: an unbound C0 receipt, unresolved C0 obligation, missing required
control proof, provider/transport fault, unmet validation predecessor, or an
open U0 decision-ledger uncertainty. The v2 delta names only requirement IDs
affected by those diagnostics. Two advisory revisions are the maximum; an
unchanged diagnostic fingerprint or exhausted depth escalates to the named
resolver without automatic retry, reroute, generation, or Exit authorization.

Primary files:

- `src/apps_rg/runtime/contracts/plan_execution_failure_taxonomy.yaml`
- `src/apps_rg/runtime/contracts/plan_execution_reconciliation.py`
- `src/apps_rg/runtime/contracts/failure_aware_replan.py`
- New failure-diagnostic and replan-consumer tests.

1. Replace output-file-only failure classification with an observed diagnostic
   ledger that cites missing C0 obligation receipts, unsupported controls, unmet
   graph predecessors, provider faults, or U0 uncertainty IDs.
2. Generate a v2 advisory replan delta tied to the parent capsule, diagnostic
   receipt, and affected requirements only. It may propose the next owner but
   never execute, retry, reroute, or authorize Exit.
3. Limit revision depth, reject unchanged repeated diagnostics, and escalate to
   the designated resolver/human when no new evidence or input can change the
   outcome.

Exit criteria: every replan action names a verified cause and the smallest
affected scope; repeated failure cannot create an automatic retry loop.

### Wave 6 — Compare, calibrate, and promote deliberately

Owner: evaluation owner with named human reviewers for ambiguous cases.

1. Freeze a source-bound fixture corpus covering straightforward, compound,
   cross-cutting, unknown, stale-brief, conflicting-constraint, and absent
   candidate-evidence cases. Split development fixtures from a protected holdout.
2. Measure v1 versus v2 on deterministic requirement extraction/typing,
   critical-requirement coverage, false broad mapping, escalation precision, C0
   obligation reconciliation, unsupported-claim blocks, and completion
   rate/cost/latency.
3. Add adjudicated human review for semantic requirement segmentation and
   ambiguous escalation; no fixture or validator may prefill human grades.
4. Require a signed promotion decision before enabling critical-requirement
   fail-closed enforcement in product-visible runs. Passing technical tests and
   shadow metrics are not production authorization.

Exit criteria: protected-holdout gains meet predeclared thresholds without a
material false-targeting or latency regression, and named human/release
authority has approved promotion.

## Cross-wave safeguards and sequencing

- Taxonomy, profiles, bindings, contracts, and receipts remain within
  `apps_rg_v2`; this roadmap requires no work in another repository.
- Every new artifact is run/request/trace-bound, canonicalized, digest-bound,
  and uses relative receipt references.
- Canonical callers read v1 or v2 during rollout; a v2-only gate is enabled
  only after Wave 6 approval.
- No technical receipt, shadow evaluation, or fixture result is human
  qualification or production authorization.

The critical path is `0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6`. Waves 4 and 5 can
start design after Wave 1, but should not change canonical behavior until Waves
2 and 3 receipts exist. This order improves representation first, verifies
evidence and execution second, then adds scheduling, feedback, tuning, and
promotion controls.
