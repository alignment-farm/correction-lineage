"""Regenerate local results, integrity checks and full cost ledger without model calls."""
import collections,datetime,hashlib,json,pathlib
from study import enc,fixture,score,valid_state
root=pathlib.Path('evidence'); ledger={};identities=set(); checks=0
for phase in ['pilot-v1','fresh-v1']:
 p=root/phase
 if not (p/'summary.json').exists():continue
 rows=json.loads((p/'results.json').read_text());calls={x.stem:json.loads(x.read_text()) for x in (p/'calls').glob('*.json')}
 for tag,c in calls.items():
  assert hashlib.sha256(enc(c['request']).encode()).hexdigest()==c['request_sha256']
  text=enc(c['request']);assert 'gold_support_candidates' not in text and '"truth"' not in text
  response=c['response'];identities.add((response['model'],response.get('system_fingerprint')))
  assert response['choices'][0]['finish_reason']=='stop',tag
  checks+=1
 stages=collections.defaultdict(lambda:{'calls':0,'prompt_tokens':0,'completion_tokens':0,'seconds':0.0})
 for tag,c in calls.items():
  v=stages[tag.split('-')[-1]];u=c['response']['usage'];v['calls']+=1;v['prompt_tokens']+=u['prompt_tokens'];v['completion_tokens']+=u['completion_tokens'];v['seconds']+=c['elapsed_seconds']
 for row in rows:
  f=fixture(row['seed']);assert row['fieldscore']==score(row['state'],f['truth'][row['event']])
  assert row['state_complete']==(all(row['fieldscore'].values()) and valid_state(row['state']))
 # Lifetime budgets count initial costs once, plus cumulative observed events.
 horizons={}
 for arm in ['selective','exposure','reconstruct','rebuild']:
  horizons[arm]={}
  for horizon in [0,1,2]:
   chosen=[r for r in rows if r['arm']==arm and r['event']<=max(horizon,1)]
   tags=set(t for r in chosen for t in r['initial_tags']+(r['event_tags'] if horizon else []))
   horizons[arm][str(horizon)]={'calls':len(tags),'tokens':sum(calls[t]['response']['usage']['total_tokens'] for t in tags)}
 maintenance=[]
 for tag,c in calls.items():
  if not tag.endswith('-maintain'):continue
  content=c['response']['choices'][0]['message']['content']
  graph=json.loads(content)
  maintenance.append({'tag':tag,'route_links':graph.get('route'),'nonauthoritative_route_link':'S6' in graph.get('route',[])})
 acquisitions=[json.loads(a.read_text()) for a in p.glob('acquisition-*.json')]
 starts=[datetime.datetime.fromisoformat(c['utc']).timestamp() for c in calls.values()]
 finishes=[datetime.datetime.fromisoformat(c['utc']).timestamp()+c['elapsed_seconds'] for c in calls.values()]
 ledger[phase]={'summary':json.loads((p/'summary.json').read_text()),'research_unique_calls':len(calls),'research_tokens':sum(c['response']['usage']['total_tokens'] for c in calls.values()),'stages':dict(stages),'maintenance_diagnostic':maintenance,'lifetime_horizons':horizons,'acquisition':{'instances':len(acquisitions),'tp':sum(a['graph_score']['tp'] for a in acquisitions),'fp':sum(a['graph_score']['fp'] for a in acquisitions),'fn':sum(a['graph_score']['fn'] for a in acquisitions),'initial_complete':sum(all(a['initial_score'].values()) and a['schema_valid'] for a in acquisitions)},'observed_run_span_seconds':max(finishes)-min(starts),'failures':[r for r in rows if not r['complete']]}
assert len(identities)==1,identities
ledger['integrity']={'verified_requests':checks,'resolved_model_identities':sorted(identities),'checks':['request hashes','no gold fixture keys in requests','no truncated completions','offline rescore','single resolved model and server fingerprint']}
(root/'analysis.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(ledger,indent=2))
