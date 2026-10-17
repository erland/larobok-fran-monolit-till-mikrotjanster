# Redaktionell kvalitetsgranskning – kapitel 7

- Datum: 2026-10-17
- Revision: 15
- Beslut: **Godkänt redaktionellt för fortsatt bokarbete**. Ej publiceringsgodkänt.

## Bedömning

- **Applikationsperspektiv – godkänt:** skillnaden mellan datamodell, informationsansvar och tjänstekontrakt beskrivs; mellanlägen, dubbletter, migrering och synlig användarstatus exemplifieras.
- **Drift-/DBA-perspektiv – godkänt:** databasplattform, kapacitet, behörigheter, avstämning, övervakning och driftansvar behandlas utan att likställa tjänsteägarskap med fysisk databasdrift.
- **Gemensamt ansvar – godkänt:** ägarskap för information, auktoritativa källor, tjänstebeteende och drift skiljs åt. Exemplet med dokumentregistrering konkretiserar gränssnittet.
- **Teknisk nyansering – godkänt för boknivån:** fysisk kontra logisk separation, eventual consistency utan garanterad tidsgräns, leveransordning beroende på teknik och stegvisa schemamigreringar förtydligas.
- **Läsbarhet och kapitelgräns – godkänt:** samma ärendehanteringsfall används; återställningsprocessens fördjupning lämnas till kapitel 17.

## Genomförda justeringar

1. Förtydligade logisk isolering och när högre krav kan motivera starkare separation.
2. Förtydligade att eventual consistency saknar generell tidsgräns och behöver mätas.
3. Nyanserade meddelandeordning och duplicering samt förklarade idempotens.
4. Förtydligade auktoritativ informationskälla för kopierade läsmodeller.
5. Skilde teknisk backup från ansvar för återläsning och verksamhetsmässig avstämning.

## Kvarstående kontroller före publicering

- F7-01–F7-04 i `docs/faktakontroll.md` kräver oberoende extern källverifiering.
- Samlad faktagranskning, slutkorrektur samt PDF-/EPUB-kontroll återstår.
