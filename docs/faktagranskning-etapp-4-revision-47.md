# Systematisk faktagranskning, etapp 4 – revision 47

**Omfattning:** kapitel 12–15. **Datum:** 2026-10-17. **Metod:** riktade verifieringar av tekniska påståendekluster mot dokumentation från AWS, OpenTelemetry, Google SRE och OWASP. Bedömningarna gäller huvudresonemangen, inte varje mening i kapitlen. Organisationsrekommendationer förblir kontextberoende.

## Källmatris

| ID | Kapitel | Granskat påstående och bedömning | Primärkälla |
|---|---|---|---|
| FV47-01 | 12 | **Stöds:** timeout och begränsade återförsök med backoff och jitter begränsar risken för resursutmattning; återförsök utan kontroll kan förstärka en störning. | AWS, *Timeouts, retries, and backoff with jitter*: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ |
| FV47-02 | 12 | **Stöds med nyans:** idempotens gör upprepade operationer säkrare men förutsätter entydiga operationer, persistens och rätt avgränsning av sidoeffekter. | AWS, *Making retries safe with idempotent APIs*: https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/ |
| FV47-03 | 13 | **Stöds:** spårkontext följer med mellan processer via propagation; inkommande kontext från opålitliga källor behöver bedömas som säkerhetsindata. | OpenTelemetry, *Context propagation*: https://opentelemetry.io/docs/concepts/context-propagation/ |
| FV47-04 | 13 | **Stöds med nyans:** spårningssampling kan begränsa volym men kan missa enskilda händelser; urvalet måste passa syftet med felsökning och uppföljning. | OpenTelemetry, *Sampling*: https://opentelemetry.io/docs/concepts/sampling/ |
| FV47-05 | 14 | **Stöds:** incidentledning behöver särskilja koordinering, tekniska åtgärder och kommunikation till intressenter. Exakta roller är organisationsberoende. | Google SRE, *Incident Management Guide*: https://sre.google/resources/practices-and-processes/incident-management-guide/ |
| FV47-06 | 14 | **Stöds:** tydlig beredskap, eskalering och kommunikation bör förberedas innan störningar; incidentarbetet prioriterar användarpåverkan. | Google SRE, *Incident Management Guide*: https://sre.google/resources/practices-and-processes/incident-management-guide/ |
| FV47-07 | 15 | **Stöds:** identitetskontroll räcker inte för objektbehörighet. Tjänsten måste kontrollera åtkomst för det begärda dokumentet, inte bara om användaren är inloggad. | OWASP, *API1:2023 Broken Object Level Authorization*: https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/ |
| FV47-08 | 15 | **Stöds:** behörighet måste prövas för funktioner och relevanta attribut; säkerhetskontroller kan inte ersättas av att API:et har svårgissade identifierare. | OWASP, *API5:2023 Broken Function Level Authorization*: https://api-security.owasp.org/editions/2023/en/0xa5-broken-function-level-authorization/ |

## Kritiska nyanser och fortsatt arbete

- **Kapitel 12:** fler återförsök kan förvärra köer och överlast; idempotens ska inte likställas med en generell garanti att alla externa effekter inträffar exakt en gång.
- **Kapitel 13:** spår och korrelations-ID är felsökningshjälpmedel, inte säkra användaridentiteter; baggage kan läcka känslig information. Samplingsstrategier behöver beakta ovanliga fel.
- **Kapitel 14:** incidentledarens samordningsmandat betyder inte automatiskt behörighet att ändra produktionssystem; följ faktiska roller och beslutsvägar.
- **Kapitel 15:** autentisering och tjänsteidentitet ersätter inte objekt- och funktionsspecifik auktorisation. OWASP API Top 10 är en riskkatalog, inte ett komplett regelverk.
- Systematisk verifiering av varje faktapåstående, alla säkerhetsdetaljer, nya plattformsversioner och rättsliga krav har inte genomförts. Vissa källor är vägledning snarare än normativa standarder.

**Beslut:** Åtta avgränsade påståendekluster bedöms förenliga med angivna källor. Inget verifierat sakfel har konstaterats som kräver ändring i manus. Inget kapitel har fått nytt publiceringsgodkännande; redaktionellt godkännande behålls. **Nästa etapp:** kapitel 16–20.
