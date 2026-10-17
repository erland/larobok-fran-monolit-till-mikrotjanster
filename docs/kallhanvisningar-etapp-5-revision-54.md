# Källhänvisningar i manus – etapp 5 (revision 54)

**Omfattning:** Kapitel 16–20. **Datum:** 2026-10-17. **Nivå:** källintegration för utvalda huvudprinciper, inte fullständig faktaverifiering.

| Kapitel | Källa | Stödd princip | Reservation |
|---|---|---|---|
| 16 | R19, NIST SSDF | Säker utveckling och kontinuerligt arbete med risker och sårbarheter över livscykeln | SSDF föreskriver inte en särskild mikrotjänsteorganisation eller viss uppgraderingsfrekvens. |
| 17 | R20, NIST SP 800-34 Rev. 1 | Kontinuitetsplanering, verksamhetskrav och återställningsstrategier | Publikationen avser amerikanska federala informationssystem; organisationens RPO/RTO måste härledas ur egna behov. Den äldre SP 800-34 utan revisionsnummer är indragen och används inte här. |
| 18 | R21, Lewis och Fowler | Organisering kring förmågor och decentraliserat tjänsteansvar | Bokens föreslagna finansierings- och beslutsstruktur är en möjlig modell, inte en tvingande arkitekturstandard. |
| 19 | R22, Azure Architecture Center | Successiv extraktion med strangler-mönstret | Mellanarkitektur och migrering medför egna driftsrisker; inte varje system lämpar sig för mönstret. |
| 20 | R23, Fowler | Avvägningar mellan självständighet och distribuerad komplexitet | Inget universellt beslutskriterium eller garanterad ekonomisk vinst följer av arkitekturvalet. |

## Bedömning

- R19–R23 infogade i kapitel 16–20 och deras källavsnitt.
- Inga nya belagda sakfel har identifierats i det avgränsade källurvalet. Kapitel 0–15 är byte-för-byte oförändrade.
- Alla kapitel innehåller nu källavsnitt, men en samlad referenskontroll och fördjupad detaljfaktagranskning återstår.
- Källmarkörerna avser stödda huvudresonemang, inte alla meningar i tillhörande kapitel.

## Källor

- **R19** NIST SP 800-218, Secure Software Development Framework (SSDF). https://csrc.nist.gov/pubs/sp/800/218/final
- **R20** NIST SP 800-34 Revision 1, Contingency Planning Guide for Federal Information Systems (updated 2010). https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
- **R21** James Lewis och Martin Fowler, Microservices. https://martinfowler.com/articles/microservices.html
- **R22** Microsoft Azure Architecture Center, Strangler Fig Pattern. https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig
- **R23** Martin Fowler, Microservice Trade-Offs. https://martinfowler.com/articles/microservice-trade-offs.html
