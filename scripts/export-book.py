#!/usr/bin/env python3
# Enkel lokal export; kräver pandoc, vid PDF dessutom xelatex.
import argparse,subprocess,shutil,yaml
from pathlib import Path
root=Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('--format',choices=['pdf','epub','all'],default='all');args=p.parse_args()
m=yaml.safe_load((root/'book.yaml').read_text(encoding='utf-8'))
if m['author']=='Ej fastställd':raise SystemExit('Avbryter: författare måste fastställas före publicering.')
if any('planerat men ännu inte skrivet' in (root/f).read_text(encoding='utf-8') for f in m['chapters'][1:]):raise SystemExit('Avbryter: kapitel är ännu inte skrivna.')
if not shutil.which('pandoc'):raise SystemExit('Pandoc saknas.')
formats=['epub','pdf'] if args.format=='all' else [args.format]
for fmt in formats:
 if fmt=='pdf' and not shutil.which('xelatex'):raise SystemExit('XeLaTeX saknas.')
 target=root/'exports'/('fran-monolit-till-mikrotjanster.'+fmt)
 cmd=['pandoc',*[str(root/f) for f in m['chapters']],'-o',str(target),'--metadata','title:'+m['title'],'--metadata','author:'+m['author'],'--metadata','lang:sv','--toc']
 if fmt=='pdf':cmd+=['--pdf-engine=xelatex','--top-level-division=chapter','--toc-depth=1','-V','documentclass:report','-V','classoption:oneside','-V','papersize:a5','-V','geometry:margin=19mm','-V','fontsize:10pt']
 if fmt=='epub':
  cmd+=['--toc-depth=1','--split-level=1']
  if m.get('cover_image'):
   cover=root/m['cover_image']
   if not cover.is_file():raise SystemExit(f'Omslagsbild saknas: {cover}')
   cmd+=['--epub-cover-image',str(cover)]
 subprocess.run(cmd,check=True);print(target)
