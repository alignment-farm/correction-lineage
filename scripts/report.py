"""Render a compact report from completed offline analysis."""
import json,pathlib
x=json.loads(pathlib.Path('evidence/analysis.json').read_text());f=x['fresh-v1'];p=x['pilot-v1'];s=f['summary'];a=f['acquisition'];total=sum(x[k]['research_tokens'] for k in ['pilot-v1','fresh-v1']);n=sum(x[k]['research_unique_calls'] for k in ['pilot-v1','fresh-v1'])
lines=['# Acquired correction lineage: bounded dispatch study','',
'## Abstract','',
f'We tested model-acquired source support against conservative exposure repair, correction-time reconstruction, and whole-state rebuilding using a fixed Qwen3.8 27B model. One pilot and three prospectively specified fresh parameter instances each contain two cumulative authoritative corrections, eight persistent obligations, and two later dispatch tasks per event. Initial acquired links covered all {a["tp"]} evaluator candidate-support edges on the fresh instances, with {a["fp"]} spurious links and {a["fn"]} omissions. All four methods repaired persistent state in 6/6 fresh episodes but achieved complete state-plus-task success in 4/6. Selective recomputed fewer fields yet used 39.1% more total tokens than rebuilding. Correct acquisition therefore did not repay its cost against the simplest competent alternative in this workload. This is a synthetic feasibility result, not a public-method reproduction or a general comparison of memory systems.','',
'## Fresh results','',
'Complete success requires the entire persistent memory and both later orders to be correct. Every arm received the original archive, current evidence, authoritative corrections and source-checking instructions. Later tasks used unseen quantities but the same task template.','',
'| Method | Complete | Persistent state | Unaffected obligations | Later tasks | Recomputed fields | Calls | Input tokens | Output tokens |',
'|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for arm,v in s.items():
 c=v['deployment_cost'];den=v['episodes'];lines.append(f'| {arm} | {v["complete"]}/{den} | {v["state_complete"]}/{den} | {v["unaffected_complete"]}/{den} | {v["fresh_complete"]}/{den} | {v["selected_fields"]} | {c["calls"]} | {c["prompt_tokens"]:,} | {c["completion_tokens"]:,} |')
lines+=['','## Failures and read-time checks','']
failures=f['failures']
if failures:
 lines+=['All failures remain in the primary denominator.','', '| Seed | Event | Method | Persistent state correct | Later tasks correct |', '|---:|---:|---|---|---|']
 for row in failures:lines.append(f'| {row["seed"]} | {row["event"]} | {row["arm"]} | {row["state_complete"]} | {row["fresh_complete"]} |')
else:lines.append('No complete-success failures were observed on the fresh instances.')
groups=f['identical_use_requests'];disagreements=sum(g['outcome_disagreement'] for g in groups)
lines+=['',f'There were {len(groups)} groups of byte-identical later-task request bodies across arms; {disagreements} groups differed in pass/fail outcome. When repaired states and later-task requests are identical, a later-task error does not identify a lineage-specific mechanism. Inspect raw requests and outputs before attributing differences to repair.','']
lines+=['','Each arm is charged one initial write per instance. Selective also pays acquisition and link maintenance; reconstruction pays its selection calls. All arms pay repair and audited use. Shared initial writes count once per hypothetical deployment, although experimentally executed once for the matched fork.','',
'## Observed lifetime costs','',
'| Method | Write only (0 corrections) | After 1 correction + use | After 2 corrections + uses |','|---|---:|---:|---:|']
for arm,h in f['lifetime_horizons'].items():lines.append('| '+arm+' | '+' | '.join(f'{h[str(k)]["tokens"]:,}' for k in [0,1,2])+' |')
sel=s['selective']['deployment_cost'];base=s['rebuild']['deployment_cost'];ratio=(sel['prompt_tokens']+sel['completion_tokens'])/(base['prompt_tokens']+base['completion_tokens'])
lines+=['',f'These are token totals over three instances, not dollar or energy costs. Selective used {ratio:.3f} times the rebuild token total over the observed two-event lifetimes. Fewer recomputed fields are not by themselves a saving: every repair still reads a small common archive, and separate link acquisition/maintenance adds work. Selective crosses below reconstruction between the observed one- and two-correction horizons (8,276 versus 7,736 tokens after one; 13,613 versus 14,037 after two), but exposure and rebuilding remain cheaper. These observed totals do not establish a crossover beyond the measured horizons.','',
'## Acquisition and maintenance diagnosis','',
f'Fresh initial writes were complete in {a["initial_complete"]}/{a["instances"]} instances. Initial acquisition precision and recall were both 1.0 on the predefined candidate-support labels. Labels score all plausible authoritative functional inputs, including both independent escort inputs, rather than asserting a unique minimal causal proof. Gold labels were never supplied as model lineage.','']
route=[m for m in f['maintenance_diagnostic'] if m['route_links'] is not None];bad=sum(m['nonauthoritative_route_link'] for m in route)
lines += [f'The pilot introduced a spurious S6 route link during maintenance: an unapproved suggestion happened to match the corrected route. This diagnostic was recorded before fresh runs. On fresh material it recurred in {bad}/{len(route)} route-maintenance calls. The scheduled corrections target S1 and S4, so this extra S6 edge cannot demonstrate an observed repair failure here. It does show why successful initial acquisition and maintained semantic support must be evaluated separately. No causal explanation is established without a controlled authority/content ablation.','',
'The first correction removes the account escort requirement while the site still requires it; the second removes the site requirement. Inspect episode states for preservation and subsequent removal. The baseline is permitted to reconstruct conservatively and select more than the truly changing fields.','',
'## Original expectations','',
'- **CL1:** Initial usable acquisition is demonstrated in this narrow workload. Maintenance can add unsupported links. No missed-link correction failure or reliability threshold was observed, so the broader expectation is unresolved.',
'- **CL2:** Small archives make reconstruction/rebuilding viable. Explicit lifetime accounting tests the implemented acquisition scheme; it does not establish whether fused acquisition, expensive repair or long correction histories would repay lineage.',
'- **CL3:** Independent support and unaffected obligations are explicit complete-success requirements. Successful preservation does not establish an advantage over other methods when those methods also succeed.','',
'## Evidence, costs and limits','',
f'The primary pilot and fresh experiment made {n} workload calls using {total:,} tokens, plus the capability probe (27 tokens). This is separate from per-arm deployment accounting. All {x["integrity"]["verified_requests"]} recorded model requests passed hash, normal-completion, no-gold-key and model-identity checks; persistent state was rescored offline. No transport or truncation failures were observed. Raw timing and server token/cache details are retained, but shared-server timing is not a controlled performance comparison. Energy and hardware utilization, as well as research preparation labor, are unmeasured. Python bookkeeping is visible in the observed run span but is not separately attributed to arms.','',
'There are three fresh parameter instances of one authored template, one fixed model, flat source-to-field links and two corrections per instance. State fields include indirect arithmetic but not a multi-stage generated memory graph. All sources fit easily in context; all arms use a common source audit at read time. Initial acquisition is a separate call, so the result cannot rank an optimized joint-write/link extractor. No gradient access, learned adapter or KV reuse was required or tested. Six episodes per arm are correlated within three instances; no significance or domain-generalization claim is made.','',
'Protocol and runner were frozen at `2cfa10f`; pilot evidence and prospective maintenance diagnosis were committed at `71c653f` before fresh execution. Run manifests pin code hashes and resolved responses pin the GGUF bundle and server fingerprint. The experiment closes this bounded feasibility phase on an explanatory cost comparison; broader workload selection and publication acceptance remain open.','',
'- [Protocol](methods/protocol-v1.md) and [public-method inspection](methods/public-methods.md).',
'- [Prospective pilot diagnosis](methods/pilot-diagnosis.md).',
'- [Fresh summary](evidence/fresh-v1/summary.json), [all fresh episodes](evidence/fresh-v1/results.json), and [pilot summary](evidence/pilot-v1/summary.json).',
'- [Full analysis and research cost ledger](evidence/analysis.json).',
'- [Reproduction](REPRODUCE.md) and [source hashes/provenance](sources/manifest.json).','']
if 'read_diagnostic' in x:
 d=x['read_diagnostic'];dc=d['summary']['research_cost'];ds=d['summary']['arms']
 lines+=['## Separate fresh-material read diagnostic','',
 'After the first two fresh instances showed correct state but excessive order totals, a separate protocol was committed at `151df75` (schema-only code cleanup at `dac6c08`). New seeds 523 and 631 compare original read wording with an explicit quantity-times-unit-cost formula. Both conditions receive the same model-produced repaired state and archives; call order is counterbalanced. This does not revise or replace any primary outcome.','',
 '| Read wording | Complete later tasks |','|---|---:|',
 f'| Original | {ds["original"]["fresh_complete"]}/2 |',
 f'| Explicit formula | {ds["explicit"]["fresh_complete"]}/2 |','',
 f'This diagnostic used {dc["calls"]} additional research calls and {d["research_tokens"]:,} tokens, including initial writing and rebuilding. The total local research execution, including the 27-token capability probe, is {n+d["research_unique_calls"]+1} calls and {total+d["research_tokens"]+27:,} tokens. The contrast on seed 631 supports wording sensitivity on new material: both variants received correct persistent state, but only the explicit formula produced correct totals. Seed 523 passed both variants. This does not prove double-counting as the internal cause or establish a general remedy from two instances.','',
 '[Diagnostic protocol](methods/read-diagnostic-v1.md), [outputs](evidence/read-diagnostic-v1/results.json), and [costs](evidence/read-diagnostic-v1/summary.json).','']
pathlib.Path('RESULTS.md').write_text('\n'.join(lines))
