# Källhänvisningar i manus – etapp 3 (revision 52)

**Omfattning:** Kapitel 8–11. **Datum:** 2026-10-17. **Arbetsnivå:** begränsad källintegration och kompletterande påståendekontroll, inte fullständig faktaverifiering.

| Kapitel | Källa | Stödd huvudprincip | Reservation |
|---|---|---|---|
| 8 | R9 Docker Compose | Deklarativ miljöbeskrivning för flerkontainerapplikationer med tjänster, nätverk och volymer | Reproducerbar konfiguration innebär inte identiskt beteende mellan olika maskiner, data och externa tjänster. |
| 9 | R10 Pact | Kontraktstester av samverkan mellan identifierade konsumenter och leverantörer | Testerna verifierar överenskomna anrop och meddelanden, inte hela verksamhetsflödet, lastkapaciteten eller alla bieffekter. |
| 10 | R11 Martin Fowler | Continuous delivery innebär att mjukvaran kan produktionssättas när så beslutas | Continuous deployment innebär automatisk produktionssättning, och inget av begreppen ger en garanti mot fel. |
| 11 | R12 Microsoft Platform Engineering | Självbetjäning och plattformen som produkt är etablerade vägledningsprinciper | Organisationsmodell och exakt ansvarsfördelning är rekommendationer, inte universella krav. |
| 11 | R13 Kubernetes Multi-tenancy | Isolering mellan team/tenants kräver flera mekanismer | Namespaces ensamma är ingen generell säkerhetsgräns; lämplig isolering beror på hotbild och plattform. |

## Bedömning

- Fem primärkällor ger stöd för valda tekniska påståenden och arkitekturrekommendationer i kapitel 8–11.
- Källmarkörer har satts vid relevanta resonemang och fullständiga adresser har lagts i källavsnitt per kapitel.
- Inga belagda sakfel som tvingar fram en bredare ändring av brödtexten identifierades i detta begränsade urval.
- Kapitel 0–7 och 12–20 är byte-för-byte oförändrade; ändrade kapitel har endast fått referensmarkörer och källavsnitt.
- Fortsatt verifiering: faktisk kontrakttesttäckning, miljöisolering, leveransrättigheter och produktspecifika säkerhetskrav i vald teknisk stack.

## Referensförteckning

- **R9** Docker, Docker Compose documentation. https://docs.docker.com/compose/
- **R10** Pact, When to use Pact. https://docs.pact.io/getting_started/what_is_pact_good_for
- **R11** Martin Fowler, Continuous Delivery. https://martinfowler.com/bliki/ContinuousDelivery.html
- **R12** Microsoft Learn, Platform engineering documentation. https://learn.microsoft.com/en-us/platform-engineering/overview/
- **R13** Kubernetes, Multi-tenancy. https://kubernetes.io/docs/concepts/security/multi-tenancy/
