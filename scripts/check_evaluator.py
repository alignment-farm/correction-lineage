"""Non-model checks for evaluator false positives and fixture integrity."""
from study import fixture,score,valid_state,graph_score,KEYS
for seed in [101,211,307,419]:
 f=fixture(seed)
 for truth in f['truth']:
  assert valid_state(truth) and all(score(truth,truth).values())
  assert not all(score({},truth).values())
  for key in KEYS:
   damaged=dict(truth);damaged.pop(key)
   assert not valid_state(damaged) and not all(score(damaged,truth).values())
  damaged=dict(truth);damaged['cold']=int(damaged['cold'])
  assert not valid_state(damaged) and not score(damaged,truth)['cold']
 assert f['truth'][1]['escort'] is True
 assert f['truth'][2]['escort'] is False
 assert not all(score(f['truth'][0],f['truth'][1]).values())
 assert not all(score(f['truth'][1],f['truth'][2]).values())
 g=graph_score(f['gold_support_candidates'],f['gold_support_candidates'])
 assert g['precision']==g['recall']==1
 g=graph_score({k:[] for k in KEYS},f['gold_support_candidates'])
 assert g['recall']==0
print('PASS: erasure, omission, stale state, bool/int confusion, independent support, link scoring')
