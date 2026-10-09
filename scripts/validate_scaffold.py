"""Check project/library consistency. This is not a regulatory compliance audit."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote,urlsplit
import yaml
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=['README.md','README.es.md','LICENSE','CONTRIBUTING.md','CHANGELOG.md','THIRD_PARTY_NOTICES.md','.gitignore','.github/workflows/validate-scaffold.yml','framework/metadata.json','framework/README.md','framework/releases/README.md','framework/drafts/README.md','framework/drafts/REQUIREMENT_TEMPLATE.md','mappings/README.md','mappings/MAPPING_TEMPLATE.md','docs/IMPORT.md','docs/LICENSING.md','docs/PROJECT_STATUS.md','docs/SOURCES.md','docs/UPLOAD.es.md','docs/VALIDATION.md','docs/TRACEABILITY.json','docs/VALIDATION_RESULTS.json','docs/SOURCE_CONTROL_HASHES.json','scripts/requirements-validation.txt','scripts/validate_scaffold.py']
def record_hash(n):
 fields={'ref_id':n['ref_id'],'name':n['name'],'description':n['description'].split('\n\n',1)[1],'name_en':n['translations']['en']['name'],'description_en':n['translations']['en']['description'].split('\n\n',1)[1]}
 return hashlib.sha256(json.dumps(fields,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def validate():
 errors=[]
 for name in REQUIRED:
  if not (ROOT/name).is_file() or (ROOT/name).stat().st_size==0:errors.append('Missing or empty: '+name)
 try:
  meta=json.loads((ROOT/'framework/metadata.json').read_text());relative=Path(meta['artifact']);assert not relative.is_absolute() and '..' not in relative.parts
  lib=yaml.safe_load((ROOT/relative).read_text());fw=lib['objects']['framework'];nodes=fw['requirement_nodes'];trace=json.loads((ROOT/'docs/TRACEABILITY.json').read_text());baselines=json.loads((ROOT/'docs/SOURCE_CONTROL_HASHES.json').read_text())
  assert lib['urn']==meta['library_urn'] and lib['version']==meta['library_version']
  assert lib['locale']=='es' and lib['translations']['en']['name']
  urns={n['urn'] for n in nodes};assert len(urns)==len(nodes)==144
  byurn={n['urn']:n for n in nodes};byref={n['ref_id']:n for n in nodes if n.get('ref_id')};assert len(byref)==138
  groups={g['ref_id'] for g in fw['implementation_groups_definition']};assert len(groups)==6
  for n in nodes:
   assert re.fullmatch(r'urn:[a-z0-9_-]+:risk:req_node:[a-z0-9_.:-]+',n['urn'])
   assert len(n['name'])<=200 and n['translations']['en']['name']
   assert set(n.get('implementation_groups',[]))<=groups
   if n.get('parent_urn'):assert n['parent_urn'] in urns and n['depth']==byurn[n['parent_urn']]['depth']+1
   else:assert n['depth']==1
  assert len(baselines)==47 and meta['official_technical_control_count']==47
  for ref,baseline in baselines.items():
   n=byref[ref];assert record_hash(n)==baseline['hash'] and n['assessable'] is True
   assert n['implementation_groups']==['cat'+str(i) for i in (1,2) if baseline['category_'+str(i)]!='not_applicable']
   labels={'mandatory':'Obligatorio','optional':'Opcional','not_applicable':'No aplicable'}
   expected='Clasificación BCCR — Categoría 1: '+labels[baseline['category_1']]+'; Categoría 2: '+labels[baseline['category_2']]+'.'
   assert n['description'].startswith(expected+'\n\n')
  assert len(trace)==75 and len({r['id'] for r in trace})==75
  covered={ref for r in trace for ref in r['legacy_ids']};assert covered=={f'NT-RCS-P-{i:03}' for i in range(1,43)}
  checks=[r for r in trace if r['kind']=='checklist'];contexts=[r for r in trace if r['kind']=='context'];assert len(checks)==66==meta['procedural_checklist_count'] and len(contexts)==9==meta['non_assessable_context_count']
  for r in trace:
   n=byref[r['id']];assert r['id'].startswith(r['section']+'.') and n['description'].startswith(r['text_es']) and n['translations']['en']['description'].startswith(r['text_en'])
   assert r['source_refs'] and r['pdf_pages']
   assert n['assessable']==(r['kind']=='checklist')
   if r['kind']=='context':assert not n.get('questions');continue
   assert n['implementation_groups']==['checklist-'+r['stage']]
   assert len(n['questions'])==1
   qurn,q=next(iter(n['questions'].items()));assert qurn.startswith(n['urn']+':question:') and q['type']=='unique_choice'
   assert q['translations']['en']['text'] and q['required'] is True
   expected={'compliant','non_compliant'}|({'not_applicable'} if r['condition_es'] else set())
   assert {c['compute_result'] for c in q['choices']}==expected and len(q['choices'])==len(expected)
   for c in q['choices']:assert c.get('add_score') is None and c['translations']['en']['value'] and c['urn'].startswith(qurn+':choice:')
  for field in ['score','documentation_score']:assert fw['field_visibility'][field]=={'auditor':'hidden','respondent':'hidden'}
  for stage,total in [('preparation',17),('report',36),('followup',6),('incidents',7)]:assert sum(r['stage']==stage for r in checks)==total
  counts={g:sum(g in byref[ref]['implementation_groups'] for ref in baselines) for g in ['cat1','cat2']};assert list(counts.values())==[47,39]
  assert byref['6.3.3']['implementation_groups']==['cat1','cat2'] and byref['6.3.3']['description'].startswith('Clasificación BCCR — Categoría 1: Opcional; Categoría 2: Opcional.')
 except (OSError,ValueError,KeyError,TypeError,AssertionError,yaml.YAMLError) as exc:errors.append('Library/metadata consistency: '+(str(exc) or 'assertion failed'))
 for path in ROOT.rglob('*.md'):
  if '.git' in path.parts:continue
  for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',path.read_text()):
   u=urlsplit(target)
   if u.scheme or u.netloc or not u.path:continue
   local=(path.parent/unquote(u.path)).resolve()
   if (ROOT.resolve() not in local.parents and local!=ROOT.resolve()) or not local.exists():errors.append(str(path.relative_to(ROOT))+': invalid local link '+target)
 if errors:
  for error in errors:print('ERROR:',error,file=sys.stderr)
  return 1
 print('PASS: repository structure, bilingual YAML, source control hashes, hierarchy, 47 controls, 66 checklist items, 9 context notes and applicability.')
 print('Scope: no regulatory certification, no live database import, no automatic BCCR verdict.')
 return 0
if __name__=='__main__':sys.exit(validate())
