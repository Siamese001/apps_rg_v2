# Apps RG V2

Local `main` integration target for the simplified `apps_rg` extraction.

This initial commit is a provenance-preserving source transplant from the
Agentic Workflow source-refreeze and standalone worktrees. It is intentionally
not yet an independently installable package: packaging, import reconciliation,
and behavior-parity certification are later refactoring waves.

The complete six-wave offline evaluation surface is now implemented under
`src/apps_rg/evals`. It provides the G1-G6 measurement contract, modular
resume-graph metrics, section and whole-resume quality evaluation, stored-run
repeatability, critical-grader mutation testing, and seven-receipt CI
ratcheting. Run its owned suite with:

`PYTHONPATH=C:\Git\apps_rg_v2\src python -m pytest -q src/apps_rg/evals`

The owned fixture suite does not create human labels, qualify a real corpus, or
authorize release. A source-bound control plane now exists under
`src/apps_rg/evals/authoritative`: it can invoke an explicit operator-supplied
Apps RG command, but reports real repeatability only when controller receipts,
human authority, truth, thresholds, and native evaluator receipts are
independently pinned.

See `MIGRATION_PROVENANCE.md` for the exact imported source state and explicit
exclusions. `SOURCE_SYNC_RECEIPT.json` binds this local main to the complete
chat-owned source history inside the original v2 import surface.
`src/apps_rg/evals/EVALUATION_SYNC_RECEIPT.json` records the later evaluator
convergence sync and its single lint-only source difference.
`src/apps_rg/evals/MEASUREMENT_VALIDITY_PLAN.md` records the subsequent
source-bound measurement remediation and remaining real-evidence gates;
`src/apps_rg/evals/MEASUREMENT_VALIDITY_IMPLEMENTATION_RECEIPT.json` seals its
code-only validation evidence.

## C0.3 graph embeddings

The canonical C0.3 ledger remains the only claim authority. Dense retrieval is
a derived, read-only ranking surface: it returns assertion IDs and similarity,
then rehydrates those IDs through the current graph, source facts, section
authority, and allowlists before they can affect allocation.

The standalone operator builds into an isolated candidate directory, performs
offline regression qualification, and only then replaces the active manifests:

```powershell
$env:APPS_RG_EMBEDDING_MODEL_PATH = 'C:\path\to\bge-m3\snapshots\5617a9f61b028005a4858fdac845db406aefb181'
$env:APPS_RG_GRAPH_SKILL_EMBEDDING_DEVICE = 'cuda:0'
$candidate = '.runtime\c03-embedding-candidate'
$qrels = 'artifacts\apps_rg\c03\graph_skill_embeddings\graph_embedding_query_qrels.08f8865fcf693606fb0ee1d1cfff9b7c63ffef2dc2e7eef4ec4e5ee96340ba85.json'

python tools\apps_rg_standalone\c03_embeddings.py rebuild `
  --candidate-dir $candidate `
  --query-qrels $qrels `
  --activate

python tools\apps_rg_standalone\c03_embeddings.py preflight
python tools\apps_rg_standalone\c03_embeddings.py smoke `
  --query 'regulated insurance AI transformation and cloud modernization' `
  --section competencies `
  --k 10
```

`tools/apps_rg_standalone/c03_embedding_runtime_contract.json` pins the
promoted Python 3.12, Torch `2.12.0.dev20260228+cu128`, Sentence Transformers
`5.2.3`, BGE-M3 revision, and offline/no-fallback rules. `preflight`, `build`,
`qualify`, and `smoke` fail closed when that runtime contract is not satisfied.

Set `APPS_RG_GRAPH_SKILL_EMBEDDINGS_REQUIRED=true` only for an explicit shadow
or governed runtime run. It remains false by default. The bundled seven-query
QREL artifact supports `REGRESSION_ONLY` qualification; it does not create
human labels or authorize release. Empirical promotion still requires the
externally pinned candidate universe, full ranking, two authorized reviewers,
and adjudication described by `src/apps_rg/evals/MEASUREMENT_VALIDITY_PLAN.md`.
