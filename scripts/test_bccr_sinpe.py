"""Library regressions. Run: python -m unittest discover -s . -p test_bccr_sinpe.py"""
from pathlib import Path
import hashlib
import json
import unittest
import yaml

ROOT=Path(__file__).resolve().parents[1]/'framework/releases'


class TestBccrSinpe(unittest.TestCase):
    def test_category_libraries(self):
        baseline=json.loads((Path(__file__).resolve().parents[1]/'docs/SOURCE_CONTROL_HASHES.json').read_text())
        all_urns=set()
        for cat,expected in ((1,(47,43,4)),(2,(39,29,10))):
            with self.subTest(category=cat):
                path=ROOT/('bccr-sinpe-nt-rcs-ed7-evaluacion-integral'+('' if cat==1 else '-cat2')+'.yaml')
                lib=yaml.safe_load(path.read_text())
                fw=lib['objects']['framework']
                nodes=fw['requirement_nodes']
                by_urn={n['urn']:n for n in nodes}
                self.assertEqual(len(nodes),len(by_urn))
                self.assertFalse(fw.get('implementation_groups_definition'))
                technical=[n for n in nodes if n.get('ref_id') in baseline]
                self.assertEqual((len(technical),sum(n['importance']=='mandatory' for n in technical),sum(n['importance']=='recommended' for n in technical)),expected)
                self.assertEqual({n['ref_id'] for n in technical},{ref for ref,b in baseline.items() if b[f'category_{cat}']!='not_applicable'})
                self.assertEqual(next(n for n in technical if n['ref_id']=='6.3.3')['importance'],'recommended')
                for ref in ('6.5.5','6.7.1','6.7.2','6.7.3','6.7.4','6.12.2'):
                    self.assertEqual(next(n for n in technical if n['ref_id']==ref)['importance'],'mandatory' if cat==1 else 'recommended')
                for n in technical:
                    fields={'ref_id':n['ref_id'],'name':n['name'],'description':n['description'].split('\n\n',1)[1],'name_en':n['translations']['en']['name'],'description_en':n['translations']['en']['description'].split('\n\n',1)[1]}
                    self.assertEqual(hashlib.sha256(json.dumps(fields,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),baseline[n['ref_id']]['hash'])
                checklist=[n for n in nodes if n.get('assessable') and n not in technical]
                self.assertEqual(len(checklist),66)
                for n in nodes:
                    self.assertFalse(n.get('implementation_groups'))
                    if n.get('parent_urn'):
                        self.assertIn(n['parent_urn'],by_urn)
                        self.assertEqual(n['depth'],by_urn[n['parent_urn']]['depth']+1)
                    self.assertIn('en',n['translations'])
                    self.assertNotIn(n['urn'],all_urns)
                    all_urns.add(n['urn'])
                    if not n.get('assessable'):
                        self.assertFalse(n.get('questions'))
                        continue
                    self.assertEqual(len(n['questions']),1)
                    qurn,q=next(iter(n['questions'].items()))
                    self.assertEqual(q['type'],'unique_choice')
                    self.assertTrue(q['required'])
                    expected_results={'compliant','non_compliant'}|({'not_applicable'} if n in checklist else set())
                    self.assertEqual({c['compute_result'] for c in q['choices']},expected_results)
                    for c in q['choices']:
                        self.assertIsNone(c.get('add_score'))
                        self.assertTrue(c['urn'].startswith(qurn+':choice:'))
                        self.assertIn('en',c['translations'])
                self.assertEqual(sum(n.get('assessable',False) for n in nodes),expected[0]+66)
                for field in ('score','documentation_score'):
                    self.assertEqual(fw['field_visibility'][field],{'auditor':'hidden','respondent':'hidden'})


if __name__=='__main__':
    unittest.main()
