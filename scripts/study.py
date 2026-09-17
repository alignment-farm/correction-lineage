"""Bounded synthetic correction study. Evaluator truth never enters model requests."""
import argparse, copy, datetime, hashlib, json, pathlib, random, subprocess, time, urllib.request
URL='https://mac-studio-7hr7.taile71f88.ts.net/engines/v1/chat/completions'
MODEL='docker.io/ai/qwen3.8:27b-q4_K_M'
KEYS=['route','unit_cost','batch_cost','cold','escort','documents','label','cutoff']
SPEC='Build reusable dispatch memory for this account. Keys: route (string), unit_cost (integer: tariff + handling), batch_cost (integer: unit_cost times standing batch size), cold (boolean), escort (boolean: required if either account or site requires it), documents (list of strings), label (string), cutoff (integer hour). Preserve independent support: removing one escort requirement does not remove another. Only authoritative replacements supersede records; a suggestion has no authority.'
SYSTEM='You are a careful dispatch clerk in a synthetic sandbox. Use only supplied evidence. Return a single JSON object, no markdown. Do not omit obligations. This is not a real shipment.'
def enc(x): return json.dumps(x,sort_keys=True,separators=(',',':'))
def write(p,x): p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2)+'\n')
def fixture(seed):
 r=random.Random(seed); tariff=r.randint(5,12);handling=r.randint(1,4);n=r.randint(3,8);hour=r.randint(13,18)
 route=r.choice(['amber','cedar','delta']);newroute=r.choice(['birch','indigo','maple'])
 src={'S1':f'Authoritative account dispatch contract: route {route}; tariff {tariff} credits per item; cold transport required; account requires escort.', 'S2':f'Authoritative handling rule: add {handling} credits per item to tariff. Standing batch has {n} items.', 'S3':'Authoritative compliance: documents are ["manifest", "seal"]; label is "fragile".', 'S4':'Authoritative site rule: escort required independently of account rules.', 'S5':f'Authoritative receiving rule: cutoff hour {hour}.', 'S6':f'Unapproved suggestion, not a rule: use route {newroute}, no documents, label "ordinary".', 'S7':'Background: cafeteria is closed on Sundays.', 'S8':'Archived nonbinding discussion: it would be cheaper without escort.'}
 truth=dict(route=route,unit_cost=tariff+handling,batch_cost=(tariff+handling)*n,cold=True,escort=True,documents=['manifest','seal'],label='fragile',cutoff=hour)
 newtariff=tariff+3
 events=[{'replace':'S1','text':f'Authoritative replacement of S1: route {newroute}; tariff {newtariff} credits per item; cold transport is not required; account no longer requires escort.'},{'replace':'S4','text':'Authoritative replacement of S4: site no longer requires escort.'}]
 t1={**truth,'route':newroute,'unit_cost':newtariff+handling,'batch_cost':(newtariff+handling)*n,'cold':False}
 t2={**t1,'escort':False}
 deps={'route':['S1'],'unit_cost':['S1','S2'],'batch_cost':['S1','S2'],'cold':['S1'],'escort':['S1','S4'],'documents':['S3'],'label':['S3'],'cutoff':['S5']}
 return {'seed':seed,'archive':src,'events':events,'truth':[truth,t1,t2],'gold_support_candidates':deps,'fresh_quantities':[n+1,n+4]}
class Runner:
 def __init__(self,out): self.out=out;self.calls=[]
 def call(self,tag,prompt):
  req={'model':MODEL,'messages':[{'role':'system','content':SYSTEM},{'role':'user','content':enc(prompt)}],'temperature':0,'max_tokens':1200,'chat_template_kwargs':{'enable_thinking':False}}
  digest=hashlib.sha256(enc(req).encode()).hexdigest();p=self.out/'calls'/f'{tag}.json'
  if p.exists():
   rec=json.loads(p.read_text());assert rec['request_sha256']==digest,'Resume prompt changed'
  else:
   start=time.perf_counter();rec={'tag':tag,'request':req,'request_sha256':digest,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
   try:
    with urllib.request.urlopen(urllib.request.Request(URL,data=enc(req).encode(),headers={'Content-Type':'application/json'}),timeout=180) as resp: rec['response']=json.load(resp)
   except Exception as e: rec['error']=repr(e)
   rec['elapsed_seconds']=time.perf_counter()-start
   write(p,rec)
  self.calls.append(rec)
  if 'error' in rec: raise RuntimeError(rec['error'])
  content=rec['response']['choices'][0]['message']['content'].strip()
  try: result=json.loads(content.removeprefix('```json').removeprefix('```').removesuffix('```').strip())
  except Exception: result={'parse_failure':content}
  print(tag,rec['response'].get('usage',{}).get('total_tokens'),round(rec['elapsed_seconds'],2),flush=True)
  return result
 def cost(self,tags):
  c=[x for x in self.calls if x['tag'] in tags];return {'calls':len(c),'prompt_tokens':sum(x.get('response',{}).get('usage',{}).get('prompt_tokens',0) for x in c),'completion_tokens':sum(x.get('response',{}).get('usage',{}).get('completion_tokens',0) for x in c),'elapsed_seconds':sum(x['elapsed_seconds'] for x in c)}
def valid_state(x):
 return isinstance(x,dict) and set(x)==set(KEYS) and all(type(x[k]) is int for k in ['unit_cost','batch_cost','cutoff']) and all(type(x[k]) is bool for k in ['cold','escort']) and all(type(x[k]) is str for k in ['route','label']) and isinstance(x['documents'],list) and all(isinstance(v,str) for v in x['documents'])
def score(x,gold):
 return {k:(type(x.get(k))==type(v) and (sorted(x[k])==sorted(v) if isinstance(v,list) else x[k]==v)) for k,v in gold.items()}
def graph_score(graph,gold):
 pred={(k,s) for k,v in graph.items() if k in KEYS and isinstance(v,list) for s in v if isinstance(s,str)};target={(k,s) for k,v in gold.items() for s in v}
 return {'tp':len(pred&target),'fp':len(pred-target),'fn':len(target-pred),'precision':len(pred&target)/len(pred) if pred else 0,'recall':len(pred&target)/len(target),'missing':sorted(target-pred),'spurious':sorted(pred-target)}
def run(args):
 out=pathlib.Path(args.out);out.mkdir(parents=True,exist_ok=True);r=Runner(out)
 rev=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
 write(out/'manifest.json',{'revision':rev,'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'model_alias':MODEL,'endpoint':URL,'seeds':args.seeds,'phase':args.phase,'settings':{'temperature':0,'max_tokens':1200,'thinking':False},'note':'Sequential requests; no latency speedup inference; immutable model identity checked in responses.'})
 results=[]
 for seed in args.seeds:
  f=fixture(seed);write(out/f'fixture-{seed}.json',f);prefix=f's{seed}'
  initial=r.call(prefix+'-write',{'task':SPEC,'archive':f['archive']})
  graph=r.call(prefix+'-acquire',{'task':'For each dispatch memory key, list IDs of ALL source records that semantically support it, including independent alternative supports. Include indirect arithmetic premises, not merely every exposed record. Output {"key":["source_id",...]}. No evaluator labels are available.','schema':SPEC,'archive':f['archive'],'memory':initial})
  write(out/f'acquisition-{seed}.json',{'initial':initial,'initial_score':score(initial,f['truth'][0]),'schema_valid':valid_state(initial),'graph':graph,'graph_score':graph_score(graph,f['gold_support_candidates']),'exposure':{k:list(f['archive']) for k in KEYS}})
  states={a:copy.deepcopy(initial) for a in ['selective','exposure','reconstruct','rebuild']};graphs={'selective':graph};archive=copy.deepcopy(f['archive']);history=[]
  orders=list(states);random.Random(seed).shuffle(orders)
  for event_idx,event in enumerate(f['events'],1):
   history.append(event);archive[event['replace']]=event['text']
   for arm in orders:
    tag=f'{prefix}-e{event_idx}-{arm}';tags=[prefix+'-write'];tags+=([prefix+'-acquire'] if arm=='selective' else [])
    if arm=='selective': targets=[k for k in KEYS if event['replace'] in graphs['selective'].get(k,[])];localgraph=graphs['selective']
    elif arm=='exposure':targets=KEYS[:];localgraph={k:list(archive) for k in KEYS}
    elif arm=='rebuild':targets=KEYS[:];localgraph=None
    else:
     recon=r.call(tag+'-reconstruct',{'task':'Identify every memory key whose value OR supporting evidence may be affected by the authoritative replacement. Include indirect dependencies and independently supported values that require checking. Output {"targets":[keys]}.','schema':SPEC,'original_archive':f['archive'],'current_archive':archive,'corrections':history,'latest_correction':event,'memory':states[arm]})
     targets=[k for k in recon.get('targets',[]) if k in KEYS];localgraph=None;tags.append(tag+'-reconstruct')
    before=copy.deepcopy(states[arm]);repair={};schema_ok=True
    if targets:
     prompt={'task':SPEC+' Recompute exactly the requested keys from current authoritative evidence. Return only those key/value pairs. Check arithmetic and retain independently supported requirements.','requested_keys':targets,'original_archive':f['archive'],'current_archive':archive,'corrections':history}
     if arm!='rebuild':prompt['memory']=before
     repair=r.call(tag+'-repair',prompt);tags.append(tag+'-repair')
     schema_ok=set(repair)==set(targets)
     # Schema failures are retained and count as failures, not repaired with evaluator truth.
     for k in targets: states[arm][k]=repair.get(k)
    # Maintaining lineage after changed sources is a paid deployment operation.
    if arm=='selective' and targets:
     updated=r.call(tag+'-maintain',{'task':'For each requested memory key list ALL current source IDs supporting it, including indirect and independent alternative supports. Return only requested key-to-list mappings.','requested_keys':targets,'schema':SPEC,'current_archive':archive,'memory':states[arm]})
     for k in targets: graphs['selective'][k]=updated.get(k,[])
     tags.append(tag+'-maintain')
    fresh=r.call(tag+'-use',{'task':'Audit memory against the authoritative archive, then produce dispatch orders for each new quantity. Each order must have quantity,total_cost,route,cold,escort,documents,label,cutoff. total_cost is quantity times current per-item tariff plus handling (both per item). Return {"orders":[...]}. Preserve every obligation.','memory_schema':SPEC,'memory':states[arm],'original_archive':f['archive'],'current_archive':archive,'corrections':history,'quantities':f['fresh_quantities']});tags.append(tag+'-use')
    truth=f['truth'][event_idx];fieldscore=score(states[arm],truth);affected=[k for k in KEYS if truth[k]!=f['truth'][event_idx-1][k]];unaffected=[k for k in KEYS if k not in affected]
    expected=[{'quantity':q,'total_cost':q*truth['unit_cost'],**{k:truth[k] for k in ['route','cold','escort','documents','label','cutoff']}} for q in f['fresh_quantities']]
    got=fresh.get('orders',[]);fresh_scores=[score(g,ex) if isinstance(g,dict) else {} for g,ex in zip(got,expected)]
    fresh_ok=len(got)==len(expected) and all(all(s.values()) and len(s)==len(expected[0]) for s in fresh_scores)
    results.append({'seed':seed,'event':event_idx,'arm':arm,'targets':targets,'before':before,'state':copy.deepcopy(states[arm]),'fieldscore':fieldscore,'state_complete':all(fieldscore.values()) and valid_state(states[arm]) and schema_ok,'affected_complete':all(fieldscore[k] for k in affected),'unaffected_complete':all(fieldscore[k] for k in unaffected),'fresh_complete':fresh_ok,'fresh_output':fresh,'fresh_expected':expected,'complete':all(fieldscore.values()) and valid_state(states[arm]) and schema_ok and fresh_ok,'event_tags':[t for t in tags if '-e' in t],'initial_tags':[t for t in tags if '-e' not in t],'cost_including_initial':r.cost(tags),'state_bytes':len(enc(states[arm]).encode()),'lineage_bytes':len(enc(localgraph).encode()) if localgraph is not None else 0})
    write(out/'results.json',results)
 summary={}
 for arm in states:
  rows=[x for x in results if x['arm']==arm];tags=set(t for x in rows for t in x['event_tags']+x['initial_tags'])
  summary[arm]={'episodes':len(rows),'complete':sum(x['complete'] for x in rows),'state_complete':sum(x['state_complete'] for x in rows),'fresh_complete':sum(x['fresh_complete'] for x in rows),'unaffected_complete':sum(x['unaffected_complete'] for x in rows),'selected_fields':sum(len(x['targets']) for x in rows),'deployment_cost':r.cost(tags)}
 write(out/'summary.json',summary);print(json.dumps(summary,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--phase',choices=['pilot','fresh'],required=True);p.add_argument('--seeds',type=int,nargs='+',required=True);run(p.parse_args())
