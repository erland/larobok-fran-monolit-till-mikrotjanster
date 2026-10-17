# Systematisk faktagranskning, etapp 2 – revision 45

**Omfattning:** kapitel 5–7. **Datum:** 2026-10-17. **Metod:** avgränsad kontroll av centrala tekniska påståenden mot leverantörers och projektens dokumentation. Varje post anger bedömning och reservation. Detta är **inte** en fullständig rad-för-rad-verifiering eller juridisk kontroll.

## Källmatris

| ID | Kapitel | Påstående / bedömning | Källor |
|---|---|---|---|
| FV45-01 | 5 | **Stöds med nyans.** Tjänst, instans och körmiljö är olika begrepp; en tjänst kan köras med flera instanser och olika drifttekniker. Teknikvalet är inte i sig liktydigt med mikrotjänstarkitektur. | Microsoft, *Design a microservices architecture*: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/ |
| FV45-02 | 5 | **Stöds.** Liveness och readiness har olika syften: readiness kan ta en instans ur trafik, liveness kan initiera omstart. Dåligt utformade liveness-kontroller kan förstärka ett fel eller skapa omstartskedjor. | Kubernetes, *Liveness, Readiness, and Startup Probes*: https://kubernetes.io/docs/concepts/workloads/pods/probes/ |
| FV45-03 | 5 | **Stöds på principnivå.** Orkestrering kan hantera instanser och skalning, men återställd container garanterar inte återställt användarflöde. Dokumentets val av två instanser och två noder är **illustrativt**, inte ett universellt hög­tillgänglighetskrav. | Kubernetes, *Configure Liveness, Readiness and Startup Probes*: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ |
| FV45-04 | 6 | **Stöds.** Synkrona API-anrop innebär att anroparen väntar på svar; meddelandebaserad kommunikation kan frikoppla tidsmässigt, men kräver hantering av leverans och fel. En asynkron programmeringsmodell är inte detsamma som asynkront integrationsprotokoll. | Microsoft, *Interservice communication*: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication |
| FV45-05 | 6 | **Stöds med reservation.** Kommunikationsmönster, API-gateway, återförsök och circuit breaker hanterar olika risker. Ingen sådan komponent kan lova fullständig leveranssäkerhet eller eliminera nätverksfel; inställningar och verksamhetskontrakt avgör. | Microsoft, *Design patterns for microservices*: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns |
| FV45-06 | 7 | **Stöds med nyans.** Tjänsteägd information syftar till avgränsad kontroll över data och kontrakt. Egen fysisk databasserver per tjänst är inte en automatisk nödvändighet; delad databasplattform med kontrollerad logisk isolering är ett separat mönsterval med kompromisser. | AWS, *Database-per-service pattern*: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/database-per-service.html ; AWS, *Enabling data persistence in microservices*: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/introduction.html |
| FV45-07 | 7 | **Stöds med viktig begränsning.** Lokal transaktion och kompenserande handlingar kan samordnas i sagor, men kompensation är inte generell rollback, kan själv misslyckas och full isolering följer inte automatiskt. | Microsoft, *Saga distributed transactions*: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga ; AWS, *Saga pattern*: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html |
| FV45-08 | 7 | **Stöds kvalitativt.** Eventuell konsistens och datareplikering innebär avvägningar kring aktualitet, fördröjningar och avstämning. Kapitlets tidsfrister är verksamhetsberoende exempel; ingen generell maximal fördröjning påstås. | AWS, *Enabling data persistence in microservices*: https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/introduction.html ; Microsoft, *Design patterns for microservices*: https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns |

## Bedömning och beslut

Samtliga kontrollerade huvudpåståenden bedöms förenliga med de angivna källorna **med ovanstående förbehåll**. Vid denna etapp framkom inget belagt sakfel som kräver ändring av redan redaktionellt godkända kapiteltexter; därför lämnas kapitel 5–7 och samtliga övriga manusfiler oförändrade.

**Särskilda kontrollpunkter för senare slutredigering:** Var noga med att ingen illustrationslösning presenteras som normativt krav, att hälsokontrollers felbeteenden och samspelet mellan data och meddelanden förblir nyanserade, och att terminologi för konsistens och kompensation är konsekvent.

## Kvarstår före publiceringsgodkännande

- Systematisk kontroll av ytterligare detaljer och eventuella standard-/regelverkskrav i kapitel 5–7.
- Kapitlen 8–20 har ännu inte fått motsvarande systematiska påståendekontroll.
- Källhänvisningar ska konsekvent integreras i publicerad utgåva, och språk- och formgranskning återstår.

**Status:** Etapp 2 genomförd för åtta påståendekluster; detta är inte fullständigt källgodkännande för kapitel 5–7.
