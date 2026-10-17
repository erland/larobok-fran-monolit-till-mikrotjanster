# Samlad manusgranskning – revision 42

**Datum:** 2026-10-17  
**Underlag:** Version 4.1.0, revision 41, inledning och 20 kapitel  
**Beslut:** Helhetsgranskning genomförd. Manusets struktur är godkänd för nästa bearbetningssteg; **inte publiceringsgodkänt**.

## Metod och kontroller

Alla 21 manusfiler har inventerats i ordning, med rubriker, omfång, återkommande begrepp och pedagogisk progression. Bokens två läsarspår (applikationsutveckling respektive drift/plattform) samt det genomgående exemplet (ärendehantering med separat dokumenttjänst) har bedömts. Publicerade primärkällor har kontrollerats stickprovsvis inom arkitekturmönster, observerbarhet, tjänstenivåmål, API-säkerhet och kontinuitetsplanering. En fullständig sats-för-sats-faktakontroll är ännu inte genomförd.

## Samlad redaktionell bedömning

| Aspekt | Bedömning | Kommentar |
|---|---|---|
| Disposition och progression | Godkänd | Utgångsläge → uppdelning → bygg/drift → förvaltning → migration/val; ordningen fungerar. |
| Två läsarperspektiv | Godkänd | Båda perspektiven återkommer; vissa senare kapitel kan vinna på fler illustrationer. |
| Genomgående scenario | Godkänt | Ärendetjänst/dokumenttjänst ger kontinuitet, särskilt i kapitel 7, 12–15 och 17–20. |
| Terminologi | Godkänd med åtgärder | Samlad ordlista kompletterad; skilj verksamhetsfunktion, mikrotjänst och instans. |
| Överlappning | Acceptabel, bevakas | Kap 8/9 om miljöer; 12/13/14 om fel, observerbarhet och incidenter; 3/18 om ansvar. Upprepningarna har olika syften, men kräver slutredigering. |
| Tekniska resonemang | Rimliga i kontrollerade stickprov | Primärkällor stöder mönster och centrala begrepp; kvarstående verifieringspunkter finns nedan. |
| Publiceringsberedskap | Ej godkänd | Extern källgranskning behöver utökas, illustrationer saknas och tryck-/e-boksprov behövs. |

## Kapitelöversikt och avgränsningar

- **Kap 1–4:** Utgångsläge, ansvar och tjänstegränser. Kapitel 3 behandlar operativ ansvarsfördelning; kapitel 18 senare styrning och finansiering.
- **Kap 5–7:** Körmiljö, kommunikation och information. Klargör att tekniska mönster inte är universella krav; faktastickprov mot Azure Architecture Center.
- **Kap 8–10:** Utvecklingsmiljö är inte samma sak som testmiljö; leveranskapitlet beskriver produktionsändring och kontraktskompatibilitet.
- **Kap 11–14:** Plattform, feltolerans, observerbarhet och incidentledning. Behåll distinktionen förebyggande design → upptäckt → samordnad åtgärd.
- **Kap 15–17:** Säkerhet, förvaltning och kontinuitet. Specificera säkerhetsbeslut och återställningsmått utifrån verksamhetens behov.
- **Kap 18–20:** Styrning, migration och arkitekturval. Förklara att migreringsarkitektur är ett faktiskt driftläge och att monolit/modulär monolit kan vara bästa valet.

## Faktastickprov mot externa primärkällor

| ID | Kapitel | Kontrollerat påstående | Resultat | Källhänvisning |
|---|---|---|---|---|
| H-01 | 6, 7, 12, 19 | Retry, circuit breaker, saga och strangler är etablerade mönster men kräver kontextanpassning. | Stöds | https://learn.microsoft.com/en-us/azure/architecture/microservices/design/patterns |
| H-02 | 13 | Loggar, mätvärden och spår är skilda telemetrisignaler som kompletterar varandra. | Stöds | https://opentelemetry.io/docs/concepts/signals/ |
| H-03 | 13 | Spårkontext behöver propageras mellan tjänster för end-to-end-korrelation. | Stöds | https://opentelemetry.io/docs/concepts/context-propagation/ |
| H-04 | 13 | SLI/SLO definierar och följer upp tjänstekvalitet; de bör anknyta till användarupplevelse. | Stöds på begreppsnivå | https://sre.google/resources/book-update/slos/ |
| H-05 | 15 | Objektbehörighet måste kontrolleras även när en användare har en giltig identitet. | Stöds | https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/ |
| H-06 | 17 | Kontinuitetsplanering omfattar verksamhetsanalys, återställningsstrategi och övning. | Stöds | https://csrc.nist.gov/pubs/sp/800/34/final |

Kontrollerna belägger endast dessa angivna avsnitt på en allmän nivå; de ersätter inte granskning av varje formulering, säkerhetsrekommendation eller juridiskt påstående. NIST SP 800-34 som refereras ovan är den äldre utgåvan och ska bedömas för aktualitet vid slutlig referensgranskning.

## Kvarstående publiceringsåtgärder, prioriterade

1. **Hög:** Fortsätt källmatris per kapitel och hänvisa till aktuell primärkälla där texten gör faktapåståenden eller rekommendationer.
2. **Hög:** Genomför sakgranskning av de riskkänsliga delarna: tjänstebehörighet och informationsskydd (15), informationskonsistens (7, 17, 19), och återställning (17).
3. **Medel:** Slutredigera överlappningar 3/18, 8/9 och 12/13/14, utan att ta bort pedagogiskt nödvändig repetition.
4. **Medel:** Skapa och faktagranska arkitekturbilder: före/efter uppdelning, nätverksvägar, ansvar, händelseflöde och återställning.
5. **Medel:** Stäm av avtalad terminologi och avsnittsrubriker mot den utökade ordlistan.
6. **Hög inför publicering:** Kontrollera källhänvisningar, rättigheter, omslag, innehållsförteckning och provrendering av PDF/EPUB på olika läsare.

## Ändringspolicy denna revision

Alla godkända kapitel och inledningen har bevarats byte-för-byte. Inga innehållsliga textändringar i manus gjordes utan särskild ny kapitelgranskning. Dokumentationen har uppdaterats och utgör nu styrande underlag för publikationsfasen. Nya åtgärder ska loggas separat från tidigare redaktionella kapitelgodkännanden.
