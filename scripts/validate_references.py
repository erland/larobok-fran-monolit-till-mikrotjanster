#!/usr/bin/env python3
"""Kontrollera källmarkörer och bibliografier i bokens kapitel."""
from pathlib import Path
import re,sys
root=Path(__file__).resolve().parent.parent
chapter_files=sorted((root/'chapters').glob('[0-2][0-9]-*.md'))
expected={f'R{i}' for i in range(1,24)}
seen={};errors=[]
for path in chapter_files:
 text=path.read_text(encoding='utf-8')
 if '### Källor och vidare läsning' not in text:
  errors.append(f'{path.name}: saknar källavsnitt');continue
 narrative,biblio=text.split('### Källor och vidare läsning',1)
 definitions=re.findall(r'^- \*\*\[(R\d+)\]\((https?://[^)]+)\)\]\*\*',biblio,re.M)
 # actual ref line markup **[R](url)**
 definitions=re.findall(r'^- \*\*\[(R\d+)\]\((https?://[^)]+)\)\*\*',biblio,re.M)
 marks=re.findall(r'\[(R\d+)\]\((https?://[^)]+)\)',narrative)
 if len(definitions)!=len(set(k for k,_ in definitions)):
  errors.append(f'{path.name}: dubbletter i källavsnitt')
 byid=dict(definitions)
 for k,u in marks:
  if k not in byid:errors.append(f'{path.name}: {k} saknar definition')
  elif byid[k]!=u:errors.append(f'{path.name}: {k} har avvikande webbadress')
 for k,u in definitions:
  if k in seen and seen[k]!=u:errors.append(f'{k}: motstridiga webbadresser')
  seen[k]=u
  if not any(x==k for x,_ in marks):errors.append(f'{path.name}: {k} används inte i brödtexten')
if set(seen)!=expected:errors.append(f'saknade/extra ID: {sorted(expected-set(seen))} / {sorted(set(seen)-expected)}')
if errors:
 print('REFERENSKONTROLL MISSLYCKADES:');print('\n'.join(errors));sys.exit(1)
print(f'REFERENSKONTROLL GODKÄND: {len(chapter_files)} manuskapitel, {len(seen)} käll-ID, {len(set(seen.values()))} unika URL:er')
