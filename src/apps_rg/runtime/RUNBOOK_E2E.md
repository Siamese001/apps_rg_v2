# Apps RG resume workflow

The sole public, end-to-end resume command is:

```bash
python -m apps_rg run [--mode live|deterministic] [--target-company <company>] [--target-role <role>] [--jd <path-or-text>] [--resume <path>]
```

With no arguments, `python -m apps_rg` runs the same canonical workflow. It
uses the canonical Anthropic partnership JD and base resume unless an override
is supplied.

## Supported actions

| Goal | Command |
| --- | --- |
| Run the complete product workflow | `python -m apps_rg run` |
| Run a no-provider repeatability proof | `python -m apps_rg run --mode deterministic` |
| Re-evaluate a completed run | `python -m apps_rg eval --run-dir <run-dir>` |
| Print a stored artifact | `python -m apps_rg show --run-dir <run-dir> --artifact resume\|email\|research\|summary\|evaluation` |

`eval` and `show` are actions of the same command surface; neither produces a
new resume or makes a provider call.

## Retired command shapes

There is no section, manual-brief, bootstrap, cache, W6, patch-run, or runtime
module command for the public resume workflow. Those historical paths must not
be used to claim an end-to-end Apps RG run. Runtime modules, evaluators,
validators, fact-inventory tools, and graph maintenance utilities may have
their own maintainer interfaces, but none generates the complete resume
product.

Every `run` prints the full resume, evaluation results, and runtime details in
fenced blocks. See
[`docs/APPS_RG_V2_CANONICAL_ENTRYPOINTS.md`](../../../docs/APPS_RG_V2_CANONICAL_ENTRYPOINTS.md)
for the authoritative public-command contract.
