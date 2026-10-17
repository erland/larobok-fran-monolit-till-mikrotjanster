# Från monolit till mikrotjänster

**Undertitel:** Hur arkitektur, ansvar, utveckling, drift och förvaltning förändras  
**Författare:** Erland Lindmark  
**Projektversion:** 5.7.0 (revision 57)

Detta är en teknisk faktabok med inledning, 20 färdigskrivna kapitel, källhänvisningar och godkänt omslag. Manuskapitlen är redaktionellt godkända. Fullständigt faktakorrektur och publiceringsgodkännande återstår.

## Projektstruktur

- `book.yaml`: metadata, kapitelordning och omslag
- `chapters/`: inledning och kapitel 1–20
- `docs/`: kapitelplan, granskningsprotokoll och faktakontroll
- `assets/cover/omslag.png`: godkänt omslag
- `publishing/`: sättning och exportstöd
- `scripts/`: export- och valideringsverktyg
- `exports/`: **äldre provutgåvor från revision 56**, utan det nya omslaget

## Lokal validering och export

Installera Python 3, PyYAML, Pandoc 3.1.11.1, XeLaTeX och Poppler (`pdfunite`).

```sh
python3 -m pip install PyYAML
python3 scripts/validate_project.py
python3 scripts/project_integrity.py verify
python3 scripts/validate_references.py
python3 scripts/export-book.py --format all
```

EPUB får omslaget via Pandoc. PDF får en separat A5-omslagssida. Exporterna skrivs till `exports/`.

## GitHub Actions

- `01-validate.yml`: struktur, referenser och projektintegritet vid push och PR.
- `02-build-preview.yml`: manuellt PDF-/EPUB-bygge med nedladdningsbara Actions-artefakter.
- `03-release.yml`: PDF-/EPUB-bygge och GitHub Release vid en semantisk `vX.Y.Z`-tagg. Versionen i publicerade filers metadata hämtas från taggen utan att `book.yaml` ändras.

Kontrollera alltid den faktiska PDF- och EPUB-renderingen innan release. De incheckade provutgåvorna är inte publiceringsgodkända.
