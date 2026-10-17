# Systematisk faktagranskning, etapp 3 – revision 46

**Omfattning:** kapitel 8–11. **Datum:** 2026-10-17. **Metod:** avgränsade faktastickprov mot originaldokumentation för tekniker, standarder och etablerade leveransprinciper. Ingen systematisk kontroll av varje mening har utförts. Arkitekturval och organisationsansvar behandlas som kontextberoende rekommendationer, inte universella krav.

## Källmatris

| ID | Kapitel | Bedömning | Primärkälla |
|---|---|---|---|
| FV46-01 | 8 | **Stöds med nyans:** lokalt körda beroenden kan underlätta utveckling, men utvecklingsmiljön behöver inte kopiera hela produktionsmiljön. Docker Compose kan definiera flera tjänster och Compose Develop är ett specifikt utvecklingsstöd, inte ett krav för mikrotjänster. | Docker Docs, *Compose Develop Specification*: https://docs.docker.com/reference/compose-file/develop/ |
| FV46-02 | 8 | **Stöds på principnivå:** reproducerbar utveckling underlättas av versionshanterad konfiguration, kontrollerade beroenden och dokumenterade miljöskillnader. Ingen enskild verktygskedja krävs. | Docker Docs, *Compose Specification*: https://docs.docker.com/compose/compose-file/ |
| FV46-03 | 9 | **Stöds:** konsumentdrivna kontraktstester kontrollerar överenskomna interaktioner hos en konsument och verifierar dem mot leverantören. Detta ersätter inte integrerade verksamhetsflöden eller icke-funktionell testning. | Pact Docs, *Verifying Pacts*: https://docs.pact.io/getting_started/verifying_pacts |
| FV46-04 | 9 | **Stöds med nyans:** ett grönt kontraktstest räcker inte utan verifiering mot de tjänsteversioner som faktiskt ska samexistera; resultatet gäller de interaktioner kontraktet omfattar. | Pact Docs, *Provider verification*: https://docs.pact.io/provider |
| FV46-05 | 10 | **Stöds:** en leveranskedja kan byggas i successiva steg med automatiska och manuella kontroller, spårbarhet och olika säkerhetsnivåer. | Martin Fowler, *Deployment Pipeline*: https://www.martinfowler.com/bliki/DeploymentPipeline.html |
| FV46-06 | 10 | **Stöds med viktig distinktion:** continuous delivery innebär att förändringar kan levereras på begäran, men kräver inte automatisk produktionsdriftsättning; continuous deployment är det automatiska fallet. | Martin Fowler, *Continuous Delivery*: https://martinfowler.com/bliki/ContinuousDelivery.html |
| FV46-07 | 11 | **Stöds med nyans:** Kubernetes namespaces delar upp namngivna resurser inom ett kluster, men omfattar inte alla klusterresurser och ger inte ensamt fullständig säkerhetsisolering. | Kubernetes Docs, *Namespaces*: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/ |
| FV46-08 | 11 | **Stöds:** självbetjäning i en delad plattform behöver kompletteras med styrning av behörigheter, nätverk, resurser och driftansvar; isoleringsmodell beror på risk och miljö. | Kubernetes Docs, *Multi-tenancy*: https://kubernetes.io/docs/concepts/security/multi-tenancy/ |

## Reservationer och återstående kontroll

- FV46-01–02: förslag på utvecklingsmiljöer är exempel, inte branschkrav. En god utvecklarupplevelse säger inget säkert om driftsäkerhet i produktion.
- FV46-03–04: kontraktsverifiering ger endast stöd för de uttryckligen testade kontrakten och verkliga versionskombinationer, inte en total kvalitetsgaranti.
- FV46-05–06: skilda begrepp för leveransberedskap och automatisk driftsättning måste bibehållas; utformning av godkännanden är organisationsberoende.
- FV46-07–08: logisk resursscope ska inte beskrivas som en fullständig säkerhetsgräns; kompletterande mekanismer behövs.
- Systematisk genomgång av alla tekniska påståenden, versionsspecifika verktygsdetaljer och organisationens faktiska implementationsval återstår.

**Beslut:** Åtta påståendekluster har faktastickprovskontrollerats utan konstaterade sakfel som kräver ändringar av kapiteltext. Redaktionellt godkända kapitel lämnas oförändrade. Faktagranskningen är **delvis genomförd**, inte publiceringsgodkänd.
