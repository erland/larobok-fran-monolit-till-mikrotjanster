# Systematisk faktagranskning, etapp 1 – revision 44

**Omfattning:** inledning och kapitel 1–4. **Datum:** 2026-10-17. **Metod:** kontroll av identifierade tekniska huvudpåståenden mot författarnas/originalleverantörers arkitekturbeskrivningar. Bedömningen avser de specifika påståendena nedan, inte en fullständig rad-för-rad-granskning eller organisationens egna regelverk.

## Källmatris

| ID | Kapitel | Påstående / avgränsning | Bedömning | Primärkälla |
|---|---|---|---|---|
| FV44-01 | Inledning, 1 | En monolit kan omfatta flera lager och flera maskiner; arkitekturbegreppet beskriver framför allt applikationens leverans- och förändringsenhet. | **Stöds med nyans:** monolitens utformning varierar; den behöver inte vara dåligt modulariserad. | Fowler, *Microservice Trade-Offs* (2015): https://martinfowler.com/articles/microservice-trade-offs.html |
| FV44-02 | 1–2 | Mikrotjänster kan driftsättas självständigt, men gränssnittsändringar kan ändå kräva samordning. | **Stöds:** självständighet är en eftersträvad arkitekturegenskap, ingen ovillkorlig garanti. | Lewis & Fowler, *Microservices* (2014): https://www.martinfowler.com/articles/microservices.html |
| FV44-03 | 2 | Fler nätverksbaserade beroenden introducerar partiella fel och kostnader för fjärranrop. | **Stöds på begreppsnivå;** detaljerade återförsöksalgoritmer behandlas och verifieras i senare etapper. | Fowler, *Microservice Trade-Offs*: https://martinfowler.com/articles/microservice-trade-offs.html ; AWS, *Retry with backoff*: https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html |
| FV44-04 | 3 | Tjänsteteam, plattform och helhetsansvar behöver uttryckliga gränssnitt, men det finns ingen universell obligatorisk organisationsmodell. | **Delvis verifierat:** arkitekturlitteraturen beskriver tjänst- och produktägarskap; kapitlets rollfördelningar är illustrativa organisationsförslag, inte generella tekniska fakta. | Lewis & Fowler, *Microservices*: https://www.martinfowler.com/articles/microservices.html |
| FV44-05 | 4 | Bounded context från domändriven design kan användas som grund för att föreslå tjänstegränser. | **Stöds med nyans:** tjänstegränser bestäms iterativt; en bounded context är inte automatiskt en mikrotjänst. | Microsoft Learn, *Use domain analysis to model microservices*: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis |
| FV44-06 | 4 | För små eller hårt kopplade tjänster riskerar att skapa problematisk samordning och distribuerad komplexitet. | **Stöds kvalitativt:** inga universella storleksgränser eller tröskelvärden kan härledas. | Microsoft Learn, *Use domain analysis to model microservices*: https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis ; Fowler, *Microservice Trade-Offs*: https://martinfowler.com/articles/microservice-trade-offs.html |
| FV44-07 | 1–4 | Ansvarsmatriser och det fiktiva ärende-/dokumentexemplet beskriver en möjlig lösning. | **Illustrativt, ej externt faktapåstående:** kontrollera vid slutkorrektur att de inte tolkas som generella krav. | Manusets uttryckliga exempelmarkeringar; ingen extern källa krävs för själva fallbeskrivningen. |

## Editorialt utfall och ändringsbeslut

Kontrollen gav **inget belagt sakfel som kräver ändring av redan godkänd kapiteltext** i denna etapp. Därför görs inga ändringar i inledning eller kapitel 1–4; påståenden som är kontextberoende verifieras endast med uttrycklig reservation. Tidigare redaktionellt godkännande kvarstår. Ingen etapp är härmed helt publikationsgodkänd.

## Återstående faktakontroll

1. **Kapitel 1–4:** kvarvarande detaljerade påståenden och eventuella normativa organisationsråd behöver läsas mot en komplett redaktionell checklista före publicering; denna etapp verifierar sju avgränsade påståendekluster.
2. **Kapitel 5–20:** systematisk påståendenivå-kontroll återstår. Prioritera nätverk/dataintegritet, meddelandeleverans, säkerhet, återställning och migrationsmetoder.
3. **Hela boken:** källhänvisningar måste integreras i det slutliga manusformatet, med åtkomstdatum och konsekvent referensstil. Komplettera senare med utgivnings- och säkerhetskrav där nödvändigt.

**Status:** Etapp 1 utförd med avgränsad verifiering; fortsatt extern faktagranskning krävs.
