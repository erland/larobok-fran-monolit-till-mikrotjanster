# Samlad referenskontroll – revision 55

Datum: 2026-10-17. Omfattning: Inledning och kapitel 1–20 (inte manusmallen).

## Utförda kontroller

- 23 distinkta referensnummer R1–R23, förekommer i respektive kapitels brödtext och källförteckning.
- 21 unika källadresser eftersom vissa verk återanvänds mellan kapitel.
- Samtliga 21 unika URL:er öppnades som webbsidor i extern kontroll denna dag; ingen gav fel vid uppslagningen. Detta säger inget om framtida länkstabilitet.
- Namn och ämnesrelevans stämde för källorna. Källorna stödjer utvalda arkitekturprinciper – de innebär inte fullständigt belägg för varje textpåstående.
- Hänvisningarna och bibliografiposterna är nu Markdown-länkar, så de kan göras klickbara i en HTML-, EPUB- och PDF-export som stöder länkar. Själva exporterna är ännu inte byggda eller provlästa.
- Ny automatisk kontroll: `python3 scripts/validate_references.py`.
- En samlad förteckning har lagts i `docs/samlad-kallforteckning.md`.

## Redaktionell ändring

Alla 21 manuskapitel har endast fått länkar i redan införda referensmarkörer och källposter. Inga övriga kapitelavsnitt, tekniska slutsatser eller disposition har skrivits om. Redaktionellt godkännande kvarstår. Referensformatets faktiska rendering i PDF och EPUB är ej verifierad.

## Publiceringskritiska restpunkter

1. Fullständig detaljfaktagranskning av påståenden som ännu bara täcks av selektiva kontroller.
2. Kontroll av eventuella rättsliga och versionskänsliga påståenden, särskilt vid säkerhet, integritet och driftmodeller.
3. Provexport och kontroll av klickbarhet, sidbrytning och källutseende i faktiska PDF-/EPUB-läsare.
4. Senare omkontroll av externa länkar vid publiceringsdatum.

## Källor

Se `docs/samlad-kallforteckning.md` för fullständig numrerad källmatris.
