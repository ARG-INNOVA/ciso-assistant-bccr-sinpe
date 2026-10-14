"""Check library contents, release metadata, traceability and local documentation links."""
from pathlib import Path
import json,re,sys,unittest
from urllib.parse import unquote,urlsplit
import yaml
from test_bccr_sinpe import TestBccrSinpe
ROOT=Path(__file__).resolve().parents[1]
def main():
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(TestBccrSinpe))
 if not result.wasSuccessful():return 1
 meta=json.loads((ROOT/'framework/metadata.json').read_text())
 assert meta['package_version']=='0.1.2' and len(meta['libraries'])==2
 for item in meta['libraries']:
  lib=yaml.safe_load((ROOT/item['artifact']).read_text())
  assert lib['version']==item['library_version']
  assert sum(n.get('assessable',False) for n in lib['objects']['framework']['requirement_nodes'])==item['assessable']
 trace=json.loads((ROOT/'docs/TRACEABILITY.json').read_text())
 assert len(trace)==75 and len({t['id'] for t in trace})==75
 assert {x for t in trace for x in t['legacy_ids']}=={f'NT-RCS-P-{i:03}' for i in range(1,43)}
 for item in meta['libraries']:
  nodes={n.get('ref_id'):n for n in yaml.safe_load((ROOT/item['artifact']).read_text())['objects']['framework']['requirement_nodes']}
  for t in trace:
   n=nodes[t['id']]
   assert n['description'].startswith(t['text_es']) and n['translations']['en']['description'].startswith(t['text_en'])
   assert n['assessable']==(t['kind']=='checklist')
 for file in ROOT.rglob('*.md'):
  if '.git' in file.parts:continue
  for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',file.read_text()):
   u=urlsplit(target)
   if u.scheme or u.netloc or not u.path:continue
   dest=(file.parent/unquote(u.path)).resolve()
   assert dest.is_relative_to(ROOT.resolve()) and dest.exists(),f'{file}: invalid link {target}'
 print('PASS: both category libraries, package metadata, 75 traceability entries and local documentation links.')
 return 0
if __name__=='__main__':sys.exit(main())
