# Acquired correction lineage: bounded dispatch study

## Abstract

We tested model-acquired source support against conservative exposure repair, correction-time reconstruction, and whole-state rebuilding using a fixed Qwen3.8 27B model. One pilot and three prospectively specified fresh parameter instances each contain two cumulative authoritative corrections, eight persistent obligations, and two later dispatch tasks per event. Initial acquired links covered all 33 evaluator candidate-support edges on the fresh instances, with 0 spurious links and 0 omissions. All four methods repaired persistent state in 6/6 fresh episodes but achieved complete state-plus-task success in 4/6. Selective recomputed fewer fields yet used 39.1% more total tokens than rebuilding. Correct acquisition therefore did not repay its cost against the simplest competent alternative in this workload. This is a synthetic feasibility result, not a public-method reproduction or a general comparison of memory systems.

## Fresh results

Complete success requires the entire persistent memory and both later orders to be correct. Every arm received the original archive, current evidence, authoritative corrections and source-checking instructions. Later tasks used unseen quantities but the same task template.

| Method | Complete | Persistent state | Unaffected obligations | Later tasks | Recomputed fields | Calls | Input tokens | Output tokens |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| selective | 4/6 | 6/6 | 6/6 | 4/6 | 18 | 24 | 12,119 | 1,494 |
| exposure | 4/6 | 6/6 | 6/6 | 4/6 | 48 | 15 | 8,553 | 1,464 |
| reconstruct | 4/6 | 6/6 | 6/6 | 4/6 | 48 | 21 | 12,435 | 1,602 |
| rebuild | 4/6 | 6/6 | 6/6 | 4/6 | 48 | 15 | 8,285 | 1,504 |

## Failures and read-time checks

All failures remain in the primary denominator.

| Seed | Event | Method | Persistent state correct | Later tasks correct |
|---:|---:|---|---|---|
| 211 | 1 | exposure | True | False |
| 211 | 1 | selective | True | False |
| 211 | 1 | rebuild | True | False |
| 211 | 1 | reconstruct | True | False |
| 307 | 1 | selective | True | False |
| 307 | 1 | exposure | True | False |
| 307 | 1 | rebuild | True | False |
| 307 | 1 | reconstruct | True | False |

There were 6 groups of byte-identical later-task request bodies across arms; 0 groups differed in pass/fail outcome. When repaired states and later-task requests are identical, a later-task error does not identify a lineage-specific mechanism. Inspect raw requests and outputs before attributing differences to repair.


Each arm is charged one initial write per instance. Selective also pays acquisition and link maintenance; reconstruction pays its selection calls. All arms pay repair and audited use. Shared initial writes count once per hypothetical deployment, although experimentally executed once for the matched fork.

## Observed lifetime costs

| Method | Write only (0 corrections) | After 1 correction + use | After 2 corrections + uses |
|---|---:|---:|---:|
| selective | 2,566 | 8,276 | 13,613 |
| exposure | 1,181 | 5,735 | 10,017 |
| reconstruct | 1,181 | 7,736 | 14,037 |
| rebuild | 1,181 | 5,603 | 9,789 |

These are token totals over three instances, not dollar or energy costs. Selective used 1.391 times the rebuild token total over the observed two-event lifetimes. Fewer recomputed fields are not by themselves a saving: every repair still reads a small common archive, and separate link acquisition/maintenance adds work. Selective crosses below reconstruction between the observed one- and two-correction horizons (8,276 versus 7,736 tokens after one; 13,613 versus 14,037 after two), but exposure and rebuilding remain cheaper. These observed totals do not establish a crossover beyond the measured horizons.

## Acquisition and maintenance diagnosis

Fresh initial writes were complete in 3/3 instances. Initial acquisition precision and recall were both 1.0 on the predefined candidate-support labels. Labels score all plausible authoritative functional inputs, including both independent escort inputs, rather than asserting a unique minimal causal proof. Gold labels were never supplied as model lineage.

The pilot introduced a spurious S6 route link during maintenance: an unapproved suggestion happened to match the corrected route. This diagnostic was recorded before fresh runs. On fresh material it recurred in 1/3 route-maintenance calls. The scheduled corrections target S1 and S4, so this extra S6 edge cannot demonstrate an observed repair failure here. It does show why successful initial acquisition and maintained semantic support must be evaluated separately. No causal explanation is established without a controlled authority/content ablation.

The first correction removes the account escort requirement while the site still requires it; the second removes the site requirement. Inspect episode states for preservation and subsequent removal. The baseline is permitted to reconstruct conservatively and select more than the truly changing fields.

## Original expectations

- **CL1:** Initial usable acquisition is demonstrated in this narrow workload. Maintenance can add unsupported links. No missed-link correction failure or reliability threshold was observed, so the broader expectation is unresolved.
- **CL2:** Small archives make reconstruction/rebuilding viable. Explicit lifetime accounting tests the implemented acquisition scheme; it does not establish whether fused acquisition, expensive repair or long correction histories would repay lineage.
- **CL3:** Independent support and unaffected obligations are explicit complete-success requirements. Successful preservation does not establish an advantage over other methods when those methods also succeed.

## Evidence, costs and limits

The primary pilot and fresh experiment made 88 workload calls using 58,327 tokens, plus the capability probe (27 tokens). This is separate from per-arm deployment accounting. All 96 recorded model requests passed hash, normal-completion, no-gold-key and model-identity checks; persistent state was rescored offline. No transport or truncation failures were observed. Raw timing and server token/cache details are retained, but shared-server timing is not a controlled performance comparison. Energy and hardware utilization, as well as research preparation labor, are unmeasured. Python bookkeeping is visible in the observed run span but is not separately attributed to arms.

There are three fresh parameter instances of one authored template, one fixed model, flat source-to-field links and two corrections per instance. State fields include indirect arithmetic but not a multi-stage generated memory graph. All sources fit easily in context; all arms use a common source audit at read time. Initial acquisition is a separate call, so the result cannot rank an optimized joint-write/link extractor. No gradient access, learned adapter or KV reuse was required or tested. Six episodes per arm are correlated within three instances; no significance or domain-generalization claim is made.

Protocol and runner were frozen at `2cfa10f`; pilot evidence and prospective maintenance diagnosis were committed at `71c653f` before fresh execution. Run manifests pin code hashes and resolved responses pin the GGUF bundle and server fingerprint. The experiment closes this bounded feasibility phase on an explanatory cost comparison; broader workload selection and publication acceptance remain open.

- [Protocol](methods/protocol-v1.md) and [public-method inspection](methods/public-methods.md).
- [Prospective pilot diagnosis](methods/pilot-diagnosis.md).
- [Fresh summary](evidence/fresh-v1/summary.json), [all fresh episodes](evidence/fresh-v1/results.json), and [pilot summary](evidence/pilot-v1/summary.json).
- [Full analysis and research cost ledger](evidence/analysis.json).
- [Reproduction](REPRODUCE.md) and [source hashes/provenance](sources/manifest.json).

## Separate fresh-material read diagnostic

After the first two fresh instances showed correct state but excessive order totals, a separate protocol was committed at `151df75` (schema-only code cleanup at `dac6c08`). New seeds 523 and 631 compare original read wording with an explicit quantity-times-unit-cost formula. Both conditions receive the same model-produced repaired state and archives; call order is counterbalanced. This does not revise or replace any primary outcome.

| Read wording | Complete later tasks |
|---|---:|
| Original | 1/2 |
| Explicit formula | 2/2 |

This diagnostic used 8 additional research calls and 5,221 tokens, including initial writing and rebuilding. The total local research execution, including the 27-token capability probe, is 97 calls and 63,575 tokens. The contrast on seed 631 supports wording sensitivity on new material: both variants received correct persistent state, but only the explicit formula produced correct totals. Seed 523 passed both variants. This does not prove double-counting as the internal cause or establish a general remedy from two instances.

[Diagnostic protocol](methods/read-diagnostic-v1.md), [outputs](evidence/read-diagnostic-v1/results.json), and [costs](evidence/read-diagnostic-v1/summary.json).
