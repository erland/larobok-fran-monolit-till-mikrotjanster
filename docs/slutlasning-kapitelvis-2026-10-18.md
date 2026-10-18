# Kapitelvis slutläsning – 18 oktober 2026

Underlag: main vid `3858f436db79e63d2b3cd62376d510162cb8f2da`, projektrevision 68. Hela manuskriptet läses i kapitelordning. Varje steg omfattar löptext, tabeller, sammanfattningar, övergångar och källavsnitt. Bedömning: begriplighet, teknisk precision, terminologi, båda läsarperspektiven och läsarfärdig text. Detta är en redaktionell slutläsning med riktad källkontroll, inte en ny heltäckande faktagranskning eller ett godkännande av ännu obearbetade PDF-/EPUB-exporter.

## Inledning – revision 69

- Förtydligat att självständig driftsättning förutsätter kompatibla gränssnitt och att felisolering inte följer automatiskt av tjänstegränser.
- Kompletterat läsanvisningen med hur boken kan användas vid första läsning och i gemensamma diskussioner.
- Målgrupp, förkunskaper, teknikneutralitet, fiktivt scenario och källavsnitt genomlästa; inga interna arbetsinstruktioner finns i inledningen.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 1. Det välbekanta IT-stödet – revision 70

- Rättat en otydlig syftning i definitionen av monolit och tonat ned ett obelagt generellt påstående om organisationers miljöer.
- Skilt mellan nätverksanrop till databasen och separata tjänsteanrop: en gemensam databas innebär inte att nätverket försvinner.
- Kontrollerat ansvarstabell, transaktionsresonemang, driftperspektiv, långsiktig förvaltning och övergången till dokumenttjänsten; den balanserade jämförelsen bevaras.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 2. Vad händer när systemet delas upp? – revision 71

- Skilt mellan en inkompatibel ändring och en faktiskt samordnad övergång; beskrivit parallellt stöd som ett möjligt sätt att genomföra övergången.
- Förklarat API vid första förekomsten för att stödja läsare från drift- och infrastruktursidan.
- Genomläst partiella fel, inventering, ansvar och jämförelsetabell. De korta tabellrubrikerna från föregående layoutkorrigering bevaras.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 3. Vem ansvarar för vad när systemet blir distribuerat? – revision 72

- Kopplat incidentberedskap till överenskomna tider i stället för att underförstå dygnet-runt-ansvar.
- Förklarat tjänsteupptäckt och timeout i det konkreta felscenariot; markerat att just den observerade felbilden gäller exemplet.
- Genomläst samtliga fyra ansvarsnivåer, fem ansvarsfrågor och ansvarstabellen; mandat, kontroll och skillnaden mot kapitel 18 är tydligt avgränsade.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 4. Hur ska systemet delas upp? – revision 73

- Preciserat invariantscenariot: en synkron kontroll skyddar inte ensam mot att underlaget ändras före beslutet; dokumentversion och uttryckliga mellanlägen konkretiserar avvägningen.
- Rättat formuleringen om interna modulanrop och använt observerbarhet konsekvent.
- Granskat alternativ A–C, bounded contexts, distribuerad monolit och beslutsprovet. Riktad kontroll 2026-10-18 av R3, https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis, stöder resonemanget om verksamhetsförmågor, sammanhållning och omprövbara gränser. Dokumentversionslösningen är bokens eget förklarande exempel, inte ett citat ur källan.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 5. Var ska tjänsterna köras? – revision 74

- Skilt mellan containeravbildning, körande container och tjänsteinstans; en instans kan omfatta samverkande containrar.
- Förtydligat att beständig lagring behöver uttalat informationsansvar, inte bara teknisk lagringskapacitet.
- Genomläst placeringsalternativ, felområden, skalning och hälsokontroller. Riktad primärkällkontroll 2026-10-18: https://kubernetes.io/docs/concepts/workloads/pods/ och R4 om probes. Den teknikneutrala framställningen och reservationerna om isolering och återställning bevaras.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 6. Hur kommunicerar tjänsterna? – revision 75

- Rättat ett sakligt missvisande motsatspar: ett framgångsrikt API-svar kan innehålla en korrekt tom lista; det är maskering av fel som ska undvikas.
- Förklarat idempotens och preciserat att ett operations-ID kräver faktisk hantering av dubbletter och en bestämd giltighetstid.
- Genomläst synkron/asynkron kommunikation, säkerhetskontroller, ansvarstabell och scenariots lösning. Riktad kontroll 2026-10-18 mot R6 och AWS Builders Library, https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/. Ersatt ett oförklarat matrisnamn med ansvarsmatris.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

