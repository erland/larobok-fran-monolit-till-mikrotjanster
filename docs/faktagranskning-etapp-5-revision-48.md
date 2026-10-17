# Systematisk faktagranskning, etapp 5 – revision 48

**Omfattning:** kapitel 16–20. **Datum:** 2026-10-17. **Metod:** avgränsad granskning av centrala påståenden och rekommendationer mot primärkällor (NIST och Microsoft Azure Architecture Center). Slutsatserna innebär inte att varje påstående eller varje teknikversion är verifierad. Redaktionellt godkännande och publiceringsgodkännande är skilda beslut.

## Källmatris

| ID | Kapitel | Bedömning av kontrollerat påstående | Primärkälla |
|---|---|---|---|
| FV48-01 | 16 | **Stöds:** säkerhetsarbete kring programvara och dess beroenden är återkommande livscykelarbete, inte enbart en byggfas. SSDF är ett ramverk av rekommenderade säkra utvecklingsrutiner och föreskriver inte en viss teamorganisation. | NIST SP 800-218 (slutlig v1.1): https://csrc.nist.gov/pubs/sp/800/218/final |
| FV48-02 | 16 | **Stöds med nyans:** SBOM och beroendeförteckningar bidrar till insyn men visar inte ensamma exponering, körningsläge eller faktisk sårbarhet. Kraven måste kompletteras av inventering och analys av användning. | NIST, *Software Security in Supply Chains*: https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity/software-security-supply-chains-guidance |
| FV48-03 | 17 | **Stöds:** kontinuitetsplanering ska utgå från kritiska verksamhetsfunktioner och prioriterad återhämtning, inte bara återstart av maskiner. RTO/RPO är mål som behöver uttryckas för relevant verksamhetsfunktion och information. | NIST SP 800-34 Rev. 1: https://csrc.nist.gov/pubs/sp/800/34/r1/final |
| FV48-04 | 17 | **Stöds med nyans:** beredskaps- och återställningsplaner behöver prövas; teknisk återläsning av en databas räcker inte i sig för att visa fungerande sammanhållen tjänst. Särskilda metoder för tvärgående datakonsistens måste väljas efter implementation. | NIST SP 800-34 Rev. 1: https://csrc.nist.gov/pubs/sp/800/34/r1/final |
| FV48-05 | 18 | **Stöds som rekommendation:** styrning, arkitekturbeslut, teamförutsättningar och förvaltning måste bedömas tillsammans. En specifik RACI eller organisatorisk mandatmodell är däremot ingen generell teknisk standard. | Microsoft, *Microservices Assessment and Readiness*: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/microservices-assessment |
| FV48-06 | 18 | **Stöds med nyans:** självständiga tvärfunktionella team behöver samtidigt gemensamma ramar för säkerhet, observerbarhet och teknikval; exakt ansvarsfördelning beror på avtal och organisation. | Microsoft, *Microservices architecture style*: https://learn.microsoft.com/en-us/azure/architecture/microservices/ |
| FV48-07 | 19 | **Stöds:** Strangler Fig-mönstret möjliggör stegvis ersättning och innebär att gammalt och nytt system samexisterar, med extra integrations- och driftsrisker under övergången. Mönstret passar inte alla migreringar. | Microsoft, *Strangler Fig pattern*: https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig |
| FV48-08 | 19 | **Stöds:** ett anti-corruption layer kan översätta mellan äldre och nya modeller; det ger inte automatiskt korrekt dataflytt eller eliminerar synkroniseringsproblem. | Microsoft, *Strangler Fig pattern*: https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig |
| FV48-09 | 20 | **Stöds:** mikrotjänster ger möjligheter till självständig leverans och skalning men ökar distribuerad komplexitet, beroenden och operativa krav. | Microsoft, *Microservices architecture style*: https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices |
| FV48-10 | 20 | **Stöds med nyans:** arkitekturval bör utgå från mätbara verksamhetsbehov, organisatorisk beredskap och avvägningar. Modulär monolit kan vara ett legitimt alternativ, men ingen källa kan generellt utse en arkitektur som bäst. | Microsoft, *Microservices Assessment and Readiness*: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/microservices-assessment |

## Särskilda reservationer och källstatus

- **NIST SSDF:** Vid granskningstillfället är SP 800-218 v1.1 slutlig. SP 800-218 Rev. 1 (v1.2) finns som utkast, inte som fastställd ersättare: https://csrc.nist.gov/pubs/sp/800/218/r1/ipd.
- **Återställning:** Dokumenterade RPO/RTO-mål säger inte att de kan uppnås; återställning av tillstånd i flera datalager och köer måste övas i den faktiska arkitekturen.
- **Styrning och kostnader:** Praktiker för ägarskap, finansiering och organisation är rekommendationer, inte universella tekniska fakta eller rättsliga krav.
- **Modernisering:** All parallell drift medför inte samma migreringsmönster; kontroll av dataägarskap och faktisk avveckling måste ske i respektive system.
- **Beslutsunderlag:** Arkitekturens lämplighet beror på miljö, förmågor, beroenden och långsiktiga kostnader; dessa kan inte avgöras genom en allmän källmatris.
- **Begränsning:** Här har tio påståendekluster verifierats, inte allt innehåll rad för rad. Inga nya kvantitativa prestandapåståenden eller rättsliga skyldigheter har fastställts.

**Beslut:** Inget belagt sakfel identifierades inom det kontrollerade urvalet som kräver ändring av manus. Samtliga kapiteltexter lämnas oförändrade och behåller redaktionellt godkännande. Hela boken har nu genomgått fem etapper av selektiv, dokumenterad faktagranskning; fullständig publiceringskontroll återstår.
