# Reproduction

The experiment is confined to this repository. No root or sibling files are
modified. Python 3.12 standard library is sufficient; use `uv`.

```sh
uv run --python 3.12 scripts/check_evaluator.py
uv run --python 3.12 scripts/analyze.py
```

Those commands do not call a model. Analysis verifies request hashes, absence of
gold fixture keys from requests, normal completion, independent state rescoring,
and a common resolved model path/server fingerprint. Inspect the exact request
bodies to audit the stronger semantic no-label-leakage claim.

The protocol and runner were frozen at `2cfa10f` before the pilot. Each run's
manifest records its starting revision and runner SHA-256. The checked-in calls
are resumable: the same request/tag reuses the saved response, and a changed
request with the same tag is rejected. To obtain independent model responses,
use a **new output directory**:

```sh
uv run --python 3.12 scripts/study.py --phase pilot --seeds 101 --out evidence/replication-pilot
uv run --python 3.12 scripts/study.py --phase fresh --seeds 211 307 419 --out evidence/replication-fresh
```

The endpoint is the dedicated Mac Studio Docker Model Runner address in
AGENTS.md, using `docker.io/ai/qwen3.8:27b-q4_K_M`, temperature 0, thinking off,
maximum 1200 output tokens. Serving is fixed-weight inference only. Resolved
model path, bundle digest and server fingerprint are retained in every response;
the tag alone is mutable, so check identity before claiming a replication.
No weights or credentials are in Git. Access requires the configured private
network. Calls are sequential; there is no timing/throughput experiment.

`fixture-*.json` contains evaluator truth and must not be handed wholesale to the
model. `calls/` records exactly what the model saw. `acquisition-*.json` separates
acquired links, exposure records and evaluator scores. `results.json` keeps every
arm/event and its persistent state, fresh outputs, targets and costs.
`summary.json` charges shared experimental writes once per hypothetical arm's
deployment. The research total in `analysis.json` counts actual unique calls;
these are different denominators. The capability probe is an additional call.
Costs include model self-check instructions and common source-audited use.
Energy, hardware utilization and literature-preparation labor are unmeasured.

Pinned primary HTML and copied metadata are in `sources/` with hashes and source
provenance. `scripts/prepare.py` downloads versioned HTML; it does not issue arXiv
metadata requests. Copied metadata originated in the root's cached, rate-limited
query API retrieval, recorded in `sources/retrieval.json`.
