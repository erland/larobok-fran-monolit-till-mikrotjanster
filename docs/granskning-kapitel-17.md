# Redaktionell kvalitetsgranskning – kapitel 17

- Datum: 2026-10-17
- Projektversion: 3.5.0; revision: 35
- Beslut: **Redaktionellt godkänt för fortsatt bokarbete**.
- Omfattning: endast kapitel 17 och tillhörande projektmetadata; tidigare kapiteltexter är oförändrade.

## Bedömning ur två läsarperspektiv

- **Applikation:** Godkänt. Dataägarskap, referensintegritet över tjänstegränser, återuppspelning, idempotens och kompensation förklaras utan att lova automatisk konsistens.
- **Drift och plattform:** Godkänt. Skillnader mellan repliker, kopior och verksamhetsåterställning framgår, liksom krypteringsnycklar, återställningsordning och praktiska övningar.
- **Gemensamt ansvar:** Godkänt. Verksamheten sätter krav och prioriteringar; applikation, drift, plattform och säkerhet måste verifiera samma sammanhållna plan.
- **Röd tråd:** Godkänt. Exemplet med dokumentinformation återställd till annat tillstånd än ärendedata förblir bärande.

## Utförda redaktionella förbättringar

1. Skärpte att RTO och RPO ska definieras per relevant verksamhetsförmåga respektive informationsflöde.
2. Lade till beroendet av kompatibla versioner, schema och dekrypteringsnycklar vid återställning.
3. Klargjorde att meddelandeköer inte automatiskt ger full historik för återuppspelning.
4. Förtydligade skydd mot oavsiktliga externa sidoeffekter vid återuppspelning.
5. Skärpte övningskrav för nycklar och behörigheter under verkliga krisförutsättningar.
6. Skilde löpande driftkostnader, skyddskostnader och avbrottskonsekvenser åt.

## Återstående kontroller

Extern källverifiering av terminologi och tekniska påståenden är **inte utförd**. Slutkorrektur, samlad bokgranskning och publiceringskontroll återstår; detta är inte ett publikationsgodkännande.
