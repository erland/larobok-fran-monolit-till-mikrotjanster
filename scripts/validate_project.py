#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
root=Path(__file__).resolve().parent.parent
meta=yaml.safe_load((root/'book.yaml').read_text(encoding='utf-8'))
assert meta['book_kind']=='factbook'
assert len(meta['chapters'])==21
assert len(set(meta['chapters']))==21
assert all((root/p).is_file() for p in meta['chapters'])
assert (root/'docs/kapitelplan.md').read_text(encoding='utf-8').count('**Status:** planerad; ej skriven.')==1
assert (root/'docs/granskning-kapitel-05.md').is_file()
assert len((root/'chapters/02-nar-systemet-delas-upp.md').read_text(encoding='utf-8').split()) > 1200
print('Projektstruktur OK – kapitel 1–20 skrivna, 1 planstatusmarkering, 1 inledning')
