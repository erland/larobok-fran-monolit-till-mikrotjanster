#!/usr/bin/env python3
import json,hashlib,sys
from pathlib import Path
root=Path(__file__).resolve().parent.parent
manifest=root/'project-manifest.json'
def collect():
 return {str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.rglob('*')) if p.is_file() and p.name!='project-manifest.json' and '__pycache__' not in p.parts and not str(p.relative_to(root)).startswith('exports/')}
def main():
 cmd=sys.argv[1] if len(sys.argv)>1 else 'verify'
 if cmd=='init':
  data={'schema_version':1,'template':False,'project_id':'fran-monolit-till-mikrotjanster','project_slug':'fran-monolit-till-mikrotjanster','revision':1,'parent_revision':None,'tracked_files':collect(),'chapters':{},'last_operation':'initial project'}
  manifest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print('Manifest initierat:',len(data['tracked_files']),'filer');return 0
 if cmd=='verify':
  d=json.loads(manifest.read_text(encoding='utf-8'));current=collect();expected=d['tracked_files'];missing=set(expected)-set(current);extra=set(current)-set(expected);changed={k for k in expected.keys() & current.keys() if expected[k]!=current[k]}
  if missing or extra or changed:print('INTEGRITETSFEL:',{'missing':sorted(missing),'extra':sorted(extra),'changed':sorted(changed)});return 1
  print('Integritet OK:',len(current),'filer, revision',d['revision']);return 0
 print('Använd: init | verify');return 2
if __name__=='__main__':raise SystemExit(main())
