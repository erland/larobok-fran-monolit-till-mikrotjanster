# Källhänvisningar i manus – etapp 2 (revision 51)

**Omfattning:** Kapitel 5–7. **Datum:** 2026-10-17.

## Källor och granskningsmatris

| Referens | Användningsområde | Avgränsning |
|---|---|---|
| R4 | Kubernetes dokumentation för liveness/readiness/startup | Orkestratorbeteende avser Kubernetes, inte alla driftplattformar. Liveness måste utformas för att undvika kaskadfel. |
| R5 | Kubernetes ReplicaSet | Ersättning av instanser förutsätter att resurser, noder och beroenden faktiskt är tillgängliga. |
| R6 | Microsofts vägledning om tjänstekommunikation | Synkrona och asynkrona mönster har olika kompromisser; köleverans betyder inte färdigbehandlad verksamhetsoperation. |
| R7 | Microsofts Saga-mönster | Sekvenser av lokala transaktioner saknar automatisk global isolation; kompensation kräver särskild design. |
| R8 | Microsofts Compensating Transaction-mönster | En åtgärd kan inte alltid rullas tillbaka; kompensation är verksamhetslogik och kan själv misslyckas. |

## Redaktionell kontroll

- Kapitel 5–7 har fått diskreta källmarkörer och källavsnitt. Referenserna är inte en mening-för-mening-verifiering.
- Kapitel 0–4 samt 8–20 har samma innehåll som i revision 50.
- Kontrollen fann inget belagt sakfel som kräver omformulering av befintliga påståenden.
- Fortsatt granskningsbehov: plattformsspecifika inställningar/versioner, lokala behörighetskrav, meddelandesystemets faktiska garantier och databastrx i vald teknik.
- Fiktiva verksamhetsexempel och ansvarsfördelningar är redaktionella illustrationer.

## Källa och åtkomst

- R4 https://kubernetes.io/docs/concepts/workloads/pods/probes/
- R5 https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
- R6 https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication
- R7 https://learn.microsoft.com/en-us/azure/architecture/patterns/saga
- R8 https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction
