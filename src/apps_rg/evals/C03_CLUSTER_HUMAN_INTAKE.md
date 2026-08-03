# C0.3 cluster human intake (W9)

W9 validates human-owned review evidence for the cluster-level embedding
projection created in W6 and packetized in W8. It does not create grades,
reviewer authority, adjudications, semantic-qualification results, an activation
manifest, or production approval.

Official finalization must run on controlled POSIX storage where Python can
verify owner-only files and directories. Native Windows may run readiness and
contract tests, but it fails closed for `--finalize`.

## Controlled input layout

Keep all inputs under ignored `.runtime/c03-cluster-w9/` or an equivalent
controller-owned POSIX location:

```text
authority/
  human_review_authority.v1.json
returns/
  reviewer_a/
    reviewer_return_manifest.v1.json
    reviews.jsonl
  reviewer_b/
    reviewer_return_manifest.v1.json
    reviews.jsonl
  adjudication/
    adjudication_manifest.v1.json
    adjudications.jsonl
```

The evaluation owner creates and externally pins the authority file. It must
bind the exact W8 receipt, packet manifest, packet-manifest file, and both cohort
manifests. Its roster contains exactly three distinct `human-reviewer://`
identities: one primary assigned to each reviewer distribution and one separate
adjudicator. Each participant needs a `cluster-relevance://` qualification.
Automation must never author this receipt.

Each primary return contains all 48 `item_ref` records and all 456
`candidate_ref` grades from its own W8 distribution. Every candidate has a
final integer `relevance_grade` from 0 through 3 and a nonempty human rationale.
The return manifest binds the reviewer identity, qualification, W8 packet,
source review-item file, completed return file, timestamp, and exact counts.

Adjudication uses the opaque references from `reviewer_a`, covers all 48 items
and 456 candidates, binds both primary-return manifests, and records the two
primary grades, one final grade from 0 through 3, and a nonempty rationale. The
adjudicator identity must be the separately rostered human.

## Commands

Verify the non-authorizing readiness receipt and W8 packet:

```powershell
python tools/apps_rg_standalone/c03_graph_evidence_cluster_human_intake_wave9.py --check
```

After controlled human work is complete, transfer the owner-pinned authority
file SHA-256 through a separate trusted channel and finalize on the supported
POSIX authority host:

```bash
python tools/apps_rg_standalone/c03_graph_evidence_cluster_human_intake_wave9.py \
  --finalize \
  --expected-human-authority-file-sha256 "$TRUSTED_AUTHORITY_FILE_SHA256"
```

Successful finalization creates controlled W7-compatible QRELs and a W9
finalization receipt. It still does not qualify or activate embeddings; W7 must
be rerun against those QRELs and any later activation remains a separate,
explicitly authorized wave.
