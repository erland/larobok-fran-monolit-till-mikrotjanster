# Källhänvisningar i manus – etapp 4 (revision 53)

**Omfattning:** Kapitel 12–15. **Datum:** 2026-10-17. **Arbetsnivå:** begränsad källintegration och påståendekontroll, inte fullständig faktaverifiering.

| Kapitel | Källa | Stödd huvudprincip | Viktig reservation |
|---|---|---|---|
| 12 | R14 AWS Prescriptive Guidance | Återförsök efter övergående fel, begränsat antal försök och backoff kan förbättra robusthet | Okontrollerade återförsök kan öka belastningen. Idempotens måste utformas för operationens faktiska sidoeffekter. |
| 13 | R15 OpenTelemetry | Kontextspridning binder samman signaler och spår över tjänstegränser | Telemetri kräver korrekt instrumentering och skydd mot att känsliga data följer med metadata. |
| 14 | R16 Google SRE | Incidenthantering bygger på tydliga roller, samordning och kommunikation | Exakt rollmodell och beslutsmandat beror på verksamhetens organisation och krav. |
| 15 | R17 OWASP | Objektbehörighet ska kontrolleras för varje begäran om skyddad information | Autentiserade användare har inte automatiskt rätt till varje dokument. |
| 15 | R18 IETF RFC 8725 | JWT måste valideras med säker algoritmhantering och korrekt tolkning av tokenanspråk | Validering av en token ersätter inte applikationens objekt- och funktionsbehörighet. |

## Bedömning

- Fem primärkällor är införda som R14–R18 i kapitlen och källförteckningarna.
- Ingen korrigering av tekniskt belagt sakfel behövdes i de kontrollerade exemplen.
- Kapitel 0–11 och 16–20 är byte-för-byte oförändrade. Redaktionellt godkännande kvarstår.
- Återstående detaljgranskning: idempotens och externa bieffekter, spårmetadata, verkliga incidentmandat, rättighetskontroll och tokenvalidering i vald produktionsstack.

## Referensförteckning

- **R14** AWS Prescriptive Guidance, Retry with backoff pattern. https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html
- **R15** OpenTelemetry, Context propagation. https://opentelemetry.io/docs/concepts/context-propagation/
- **R16** Google SRE Workbook, Incident Response. https://sre.google/workbook/incident-response/
- **R17** OWASP, API1:2023 Broken Object Level Authorization. https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/
- **R18** IETF, RFC 8725 JSON Web Token Best Current Practices. https://www.rfc-editor.org/rfc/rfc8725.html
