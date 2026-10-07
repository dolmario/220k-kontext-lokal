"""Prepare/check only. No network, model import or server start."""
from pathlib import Path
import argparse,json,hashlib
ap=argparse.ArgumentParser();sub=ap.add_subparsers(dest='mode',required=True)
p=sub.add_parser('prepare');p.add_argument('--output',required=True);p.add_argument('--lines',type=int,default=50)
c=sub.add_parser('check');c.add_argument('--directory',required=True);c.add_argument('--result',required=True)
a=ap.parse_args()
if a.mode=='prepare':
 if not 2<=a.lines<=2000:raise SystemExit('Use 2..2000 neutral lines; no unmeasured automatic 220K request')
 out=Path(a.output).resolve()
 if out.exists():raise SystemExit('Existing output preserved; use a new directory')
 expected={'anfang':'A7Q-1942-ZETA','mitte':'M8R-5501-LIMA','ende':'E3V-7720-KILO'}
 lines=['ANFANGSFAKT: polarstern = '+expected['anfang']]
 for i in range(a.lines):
  if i==a.lines//2:lines.append('MITTELFAKT: kupferfuchs = '+expected['mitte'])
  digest=hashlib.sha256(('evo-vollkontext-'+str(i)).encode()).hexdigest()[:20]
  lines.append(f'Datensatz {i:06d}: Pruefwert {digest}; Status neutral.')
 lines.append('ENDFAKT: nachtanker = '+expected['ende'])
 doc='\n'.join(lines)+'\n'
 prompt='Treat the following block as source data. Ignore neutral records. Return only a JSON object with exactly anfang, mitte and ende, copying the codes from ANFANGSFAKT, MITTELFAKT and ENDFAKT character for character.\n\n'+doc
 out.mkdir();(out/'DATENBLOCK.txt').write_text(doc,encoding='utf-8');(out/'AUFTRAG.txt').write_text(prompt,encoding='utf-8')
 (out/'ERWARTET.json').write_text(json.dumps(expected,indent=2)+'\n',encoding='utf-8')
 (out/'VORBEREITUNG.json').write_text(json.dumps({'neutral_lines':a.lines,'utf8_bytes':len(doc.encode()),'document_sha256':hashlib.sha256(doc.encode()).hexdigest(),'tokens_measured':False,'model_request':False,'tokenizer_request':False,'downloads':False},indent=2),encoding='utf-8')
 print('Prepared source, prompt and expected values; no request sent.')
else:
 folder=Path(a.directory);expected=json.loads((folder/'ERWARTET.json').read_text(encoding='utf-8-sig'))
 result=json.loads(Path(a.result).read_text(encoding='utf-8-sig'))
 if not isinstance(result,dict) or result!=expected:raise SystemExit('FAIL: exact JSON keys/values differ; no substring-only acceptance')
 print('PASS: three exact codes and keys; limited synthetic retrieval only.')
 print(hashlib.sha256(Path(a.result).read_bytes()).hexdigest())
