import copy,hashlib,json,pathlib,subprocess
from study import Runner,fixture,SPEC,score,valid_state,write
out=pathlib.Path('evidence/read-diagnostic-v1');r=Runner(out)
write(out/'manifest.json',{'revision':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'seeds':[523,631],'phase':'exploratory fresh read-wording diagnostic'})
results=[]
for seed in [523,631]:
 f=fixture(seed);write(out/f'fixture-{seed}.json',f);prefix=f's{seed}';event=f['events'][0];archive=copy.deepcopy(f['archive']);archive[event['replace']]=event['text']
 initial=r.call(prefix+'-write',{'task':SPEC,'archive':f['archive']})
 state=r.call(prefix+'-rebuild',{'task':SPEC+' Recompute exactly the requested keys from current authoritative evidence. Return only those key/value pairs. Check arithmetic and retain independently supported requirements.','requested_keys':list(f['truth'][0]),'original_archive':f['archive'],'current_archive':archive,'corrections':[event]})
 old='total_cost is quantity times current per-item tariff plus handling (both per item).'
 new='total_cost = quantity * (current tariff + per-item handling) = quantity * memory.unit_cost when memory.unit_cost is correct. Do not add handling again to unit_cost.'
 task='Audit memory against the authoritative archive, then produce dispatch orders for each new quantity. Each order must have quantity,total_cost,route,cold,escort,documents,label,cutoff. '+old+' Return {"orders":[...]}. Preserve every obligation.'
 for arm in (['original','explicit'] if seed==523 else ['explicit','original']):
  output=r.call(prefix+'-'+arm,{'task':task if arm=='original' else task.replace(old,new),'memory_schema':SPEC,'memory':state,'original_archive':f['archive'],'current_archive':archive,'corrections':[event],'quantities':f['fresh_quantities']})
  truth=f['truth'][1];expected=[{'quantity':q,'total_cost':q*truth['unit_cost'],**{k:truth[k] for k in ['route','cold','escort','documents','label','cutoff']}} for q in f['fresh_quantities']]
  got=output.get('orders',[]);ok=len(got)==len(expected) and all(isinstance(g,dict) and all(score(g,e).values()) for g,e in zip(got,expected))
  results.append({'seed':seed,'arm':arm,'initial':initial,'initial_complete':valid_state(initial) and all(score(initial,f['truth'][0]).values()),'state':state,'state_complete':valid_state(state) and all(score(state,truth).values()),'output':output,'expected':expected,'fresh_complete':ok})
  write(out/'results.json',results)
write(out/'summary.json',{'arms':{a:{'instances':2,'fresh_complete':sum(x['fresh_complete'] for x in results if x['arm']==a)} for a in ['original','explicit']},'research_cost':r.cost([x['tag'] for x in r.calls])})
