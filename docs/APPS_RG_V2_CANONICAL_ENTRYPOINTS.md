# Apps RG v2 Canonical Resume Entrypoint

## Scope

This document governs the **end-to-end resume pipeline** only. It does not
turn every maintenance, graph, calibration, or evaluation utility in the
repository into a resume-pipeline command.

## The one public command

```text
python -m apps_rg run [--mode live|deterministic] [optional JD/resume overrides]
```

The zero-input form uses the canonical Anthropic partnership JD and canonical
Amit Ayer base resume. It is the only supported user-facing command that can
produce a résumé, outreach email, research brief, evaluation, and delivery
artifacts.

The same top-level command owns inspection actions:

```text
python -m apps_rg eval --run-dir <completed-run>
python -m apps_rg show --run-dir <completed-run> --artifact resume|email|research|summary|evaluation
```

`eval` only reads existing output and makes no provider call. `show` prints
the exact stored artifact; use it to display the full résumé without copying a
different version.

## Explicit modes

| Mode | Purpose | Providers | Result label |
| --- | --- | --- | --- |
| `live` | Product end-to-end proof. | Real SearXNG, OpenAI, and Gemini only. | `LIVE_PROVIDER_PASS` when all stages/evaluation pass. |
| `deterministic` | Offline repeatability proof. | None. No credential is read. | `DETERMINISTIC_OFFLINE_PASS` when the local contract/evaluator pass. |

Neither mode substitutes for the other. A deterministic result is not a
live-provider result; a live LLM result is not byte-deterministic proof.

## Explicitly not resume-pipeline entrypoints

The following may remain as internal libraries, maintenance tools, or
separate-app utilities. They are not allowed to be represented as alternate
end-to-end Apps RG resume runners:

- `python -m apps_research` — separate research-app surface.
- `python -m apps_eval` — generic grader harness.
- `python -m apps_rg.evals.*` — evaluation, calibration, and qualification
  utilities.
- `tools/apps_rg_standalone/*` — historical/maintenance tools.
- `apps_rg.runtime.*`, `apps_rg.fact_inventory.*`, and section-lane modules —
  implementation or maintenance surfaces, not operator resume pipelines.

The historical `python -m apps_rg --section ...`, `doctor`, bootstrap,
manual-brief, cache, W6, and legacy-spine command shapes are not part of this
public resume command. They must not be added back to its parser.

## Enforcement

The public parser exposes only `run`, `eval`, and `show`. Focused tests verify
that deterministic mode cannot call the live credentials, retrieval, OpenAI,
or Gemini hooks; that the complete stage contract is present; and that `eval`
and `show` operate only on completed artifacts.
