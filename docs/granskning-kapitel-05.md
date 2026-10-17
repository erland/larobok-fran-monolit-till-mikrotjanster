# Redaktionell kvalitetsgranskning – kapitel 5

- Revision: 11 (2026-10-17)
- Kapitel: `chapters/05-var-tjansterna-kors.md`
- Beslut: **Redaktionellt godkänt för fortsatt bokarbete**. Inte slutligt faktagranskat eller publiceringsgodkänt.

## Perspektivgranskning

| Perspektiv | Resultat | Motivering |
|---|---|---|
| Applikationsläsare | Godkänt | Logisk tjänst, instans och värd skiljs åt; skalning och hälsobeteende knyts till tjänstens utformning. |
| Driftläsare | Godkänt | VM, containrar, felområden, kapacitet, värdansvar och operativ uppföljning förklaras utan verktygsfixering. |
| Gemensamt ansvar | Godkänt | Krav, genomförande, ändringsmandat, incidentledning och uppföljning separeras tydligt. |
| Saklighet/nyansering | Godkänt redaktionellt | Ingen likställning mellan mikrotjänster och Kubernetes; ingen garanti om autonomi eller automatisk återhämtning. |
| Avgränsning och läsbarhet | Godkänt | Placering och exekvering behandlas här; nätverkstrafik i kapitel 6, testmiljöer i 8–9, återställning i 17. |

## Utförda justeringar

1. Nyanserat att oberoende leveranser är ett arkitekturmål, inte en automatisk egenskap.
2. Skärpt distinktionen tjänst–instans–container–värd och plattformens återstart kontra verksamhetsåterhämtning.
3. Förtydligat gemensamma felorsaker, isoleringsrisker och kontroll av faktisk instansspridning.
4. Förklarat att extra instanser bara förbättrar kapacitet om rätt flaskhals angrips.
5. Skilt beständig lagring från backup och återställning, och preciserat ansvar för säkerhetsavvikelser.

## Kvarstående publiceringskontroller

- Extern kontroll av säkerhetsisolering, hälsokontroller, skalning och plattformars specifika garantier mot tekniska originalkällor.
- Terminologikontroll mot hela färdigställda boken, slutkorrektur samt faktisk PDF-/EPUB-granskning.
