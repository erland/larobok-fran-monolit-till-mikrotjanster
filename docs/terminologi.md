# Terminologi – redaktionellt styrd ordlista

Termerna är pedagogiska arbetsdefinitioner. Verksamhets- och organisationsspecifika roller kan ha andra formella benämningar.

| Begrepp | Arbetsdefinition | Särskild avgränsning |
|---|---|---|
| Monolit | Applikation med huvudsakligen sammanhållen leveranslivscykel | Kan vara välmodulariserad internt |
| Modulär monolit | Sammanhållen driftsättning med tydliga interna modulgränser | Ger inte nödvändigtvis självständig driftsättning av moduler |
| Mikrotjänst | Självständigt förvaltad och driftsättningsbar tjänst med avgränsat ansvar och uttryckligt gränssnitt | Kräver inte egen VM eller egen fysisk databasserver |
| Tjänst | Logisk enhet som tillhandahåller funktion via gränssnitt | Skilj från instans och körmiljö |
| Tjänsteinstans | Körande exemplar av en tjänst | Flera instanser kan tillhöra samma tjänst |
| Plattform | Gemensamma drift- och leveransförmågor med dokumenterade gränssnitt | Är inte liktydigt med Kubernetes eller moln |
| Verksamhetsfunktion | Användarorienterat arbetsmoment som kan bero på flera tjänster | Kan fungera dåligt trots gröna hälsokontroller |
| Tjänsteägarskap | Beslutat ansvar för beteende och livscykel inom angivet mandat | Ersätter inte verksamhetens helhetsansvar |
| Kontrakt | Överenskommelse om gränssnitts beteende, format och kompatibilitet | Mer än en API-specifikation |
| Synkron kommunikation | Avsändaren väntar normalt på svar från mottagaren | Fel och svarstider blir direkt kopplade |
| Asynkron kommunikation | Arbete eller meddelande behandlas vid annat tillfälle än initieringen | Medför inte automatiskt exakt-en-gång-behandling |
| Eventuell konsistens | Tillfällig skillnad mellan representationer som kan konvergera efter spridning | Behöver definierade gränser, felhantering och avstämning |
| Idempotens | Upprepad begäran ger inte oavsiktligt upprepad verksamhetseffekt | Är inte samma sak som att varje tekniskt anrop bara sker en gång |
| SLI / SLO / SLA | Mätindikator / intern målnivå / avtalad servicenivå | Bör inte användas som synonymer |
| RPO / RTO | Mål för accepterad dataförlust i tid / mål för återställningstid | Definieras för relevant verksamhetsförmåga och information |
| Observerbarhet | Förmåga att förstå systemets tillstånd med bl.a. loggar, mått och spår | Ersätter inte incidentprocess eller verksamhetsuppföljning |
| Teknisk skuld | Framtida förändrings- och riskkostnad av tidigare tekniska val | Kan finnas i integrationer, plattform och dokumentation |
| Strangler-mönstret | Stegvis ersättning av ett äldre system bakom kontrollerade gränser | Kräver tidsatt avveckling av tillfälliga beroenden |
