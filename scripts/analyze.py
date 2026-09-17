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
 access={}
 for tag,c in calls.items():
  if not (tag.endswith('-use') or tag.endswith('-repair')):continue
  body=json.loads(c['request']['messages'][1]['content'])
  key=tuple(tag.split('-')[:2])
  evidence=enc({k:body[k] for k in ['original_archive','current_archive','corrections']})
  if key in access:assert access[key]==evidence,tag
  else:access[key]=evidence
 use_groups=collections.defaultdict(list)
 for row in rows:
  tag=next(t for t in row['event_tags'] if t.endswith('-use'))
  use_groups[calls[tag]['request_sha256']].append({'tag':tag,'fresh_complete':row['fresh_complete'],'output':row['fresh_output']})
 repeated=[{'request_sha256':h,'calls':v,'outcome_disagreement':len({r['fresh_complete'] for r in v})>1,'output_disagreement':len({enc(r['output']) for r in v})>1} for h,v in use_groups.items() if len(v)>1]
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
 for arm,v in json.loads((p/'summary.json').read_text()).items():
  budget=v['deployment_cost'];assert horizons[arm]['2']['tokens']==budget['prompt_tokens']+budget['completion_tokens']
  assert horizons[arm]['2']['calls']==budget['calls']
 maintenance=[]
 for tag,c in calls.items():
  if not tag.endswith('-maintain'):continue
  content=c['response']['choices'][0]['message']['content']
  graph=json.loads(content)
  maintenance.append({'tag':tag,'route_links':graph.get('route'),'nonauthoritative_route_link':'S6' in graph.get('route',[])})
 acquisitions=[json.loads(a.read_text()) for a in p.glob('acquisition-*.json')]
 starts=[datetime.datetime.fromisoformat(c['utc']).timestamp() for c in calls.values()]
 finishes=[datetime.datetime.fromisoformat(c['utc']).timestamp()+c['elapsed_seconds'] for c in calls.values()]
 ledger[phase]={'summary':json.loads((p/'summary.json').read_text()),'identical_use_requests':repeated,'research_unique_calls':len(calls),'research_tokens':sum(c['response']['usage']['total_tokens'] for c in calls.values()),'stages':dict(stages),'maintenance_diagnostic':maintenance,'lifetime_horizons':horizons,'acquisition':{'instances':len(acquisitions),'tp':sum(a['graph_score']['tp'] for a in acquisitions),'fp':sum(a['graph_score']['fp'] for a in acquisitions),'fn':sum(a['graph_score']['fn'] for a in acquisitions),'initial_complete':sum(all(a['initial_score'].values()) and a['schema_valid'] for a in acquisitions)},'observed_run_span_seconds':max(finishes)-min(starts),'failures':[r for r in rows if not r['complete']]}
diagnostic=root/'read-diagnostic-v1'
if (diagnostic/'summary.json').exists():
 dcalls=[json.loads(p.read_text()) for p in (diagnostic/'calls').glob('*.json')]
 for c in dcalls:
  assert hashlib.sha256(enc(c['request']).encode()).hexdigest()==c['request_sha256']
  body=enc(c['request']);assert 'gold_support_candidates' not in body and '\"truth\"' not in body
  response=c['response'];assert response['choices'][0]['finish_reason']=='stop'
  identities.add((response['model'],response.get('system_fingerprint')));checks+=1
 drows=json.loads((diagnostic/'results.json').read_text())
 for row in drows:
  f=fixture(row['seed']);truth=f['truth'][1]
  assert row['state_complete']==(valid_state(row['state']) and all(score(row['state'],truth).values()))
  expected=[{'quantity':q,'total_cost':q*truth['unit_cost'],**{k:truth[k] for k in ['route','cold','escort','documents','label','cutoff']}} for q in f['fresh_quantities']]
  assert row['expected']==expected
  got=row['output'].get('orders',[])
  assert row['fresh_complete']==(len(got)==len(expected) and all(isinstance(g,dict) and all(score(g,e).values()) for g,e in zip(got,expected)))
 for seed in [523,631]:
  pair=[c for c in dcalls if c['tag'] in [f's{seed}-original',f's{seed}-explicit']]
  bodies=[json.loads(c['request']['messages'][1]['content']) for c in pair]
  assert len(bodies)==2
  for b in bodies:b.pop('task')
  assert bodies[0]==bodies[1]
 ledger['read_diagnostic']={'summary':json.loads((diagnostic/'summary.json').read_text()),'results':json.loads((diagnostic/'results.json').read_text()),'research_unique_calls':len(dcalls),'research_tokens':sum(c['response']['usage']['total_tokens'] for c in dcalls)}
assert len(identities)==1,identities
ledger['integrity']={'verified_requests':checks,'resolved_model_identities':sorted(identities),'checks':['request hashes','no gold fixture keys in requests','no truncated completions','offline rescore','single resolved model and server fingerprint','equal archives and corrections across repair/use arms']}
(root/'analysis.json').write_text(json.dumps(ledger,indent=2)+'\n')
print(json.dumps(ledger,indent=2))
