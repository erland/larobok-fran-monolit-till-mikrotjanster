# Från monolit till mikrotjänster – bokprojekt

Projektet följer Lärobokskaparens uppdelning mellan `book.yaml`, `docs/`, `chapters/`, `publishing/` och `scripts/`. **Detta är en planeringsversion**: kapitel 1–20 är enbart markerade som ej skrivna. Författare och omslag beslutas före publicering.

## Arbetsgång
1. Läs `docs/kapitelplan.md` och `docs/bokspecifikation.md`.
2. Skriv/utveckla inledning och därefter ett kapitel i taget; använd `chapters/kapitelmall-faktabok.md`.
3. Uppdatera faktakontroll, status och revisionslogg.
4. Kör `python3 scripts/project_integrity.py verify` och `python3 scripts/validate_project.py`.
5. När boktext och författare är klara: export med `python3 scripts/export-book.py --format all` (Pandoc och XeLaTeX krävs).

`docs/` är redaktionellt material och exporteras inte. ZIP innehåller inga färdigskrivna kapitel.
