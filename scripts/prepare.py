import hashlib,json,pathlib,urllib.request,subprocess,datetime
p=pathlib.Path('sources'); manifest=[]
for ident in ['2605.07242v1','2608.10502v1','2608.19652v1','2608.01619v1']:
 url=f'https://arxiv.org/html/{ident}'
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'CorrectionLineageStudy/0.1 (local research methods archival)'}),timeout=40).read()
  (p/f'{ident}.html').write_bytes(data)
  manifest.append({'url':url,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
 except Exception as e: manifest.append({'url':url,'error':str(e)})
for name in ['README.md','retrieval.json','selected-metadata.xml','followup-metadata.xml']:
 manifest.append({'file':name,'copied_from':'../../construct-2/sources/2026-09-17-independent-study-selection/'+name,'sha256':hashlib.sha256((p/name).read_bytes()).hexdigest()})
(p/'manifest.json').write_text(json.dumps({'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root_revision':subprocess.check_output(['git','-C','../../construct-2','rev-parse','HEAD'],text=True).strip(),'artifacts':manifest},indent=2))
