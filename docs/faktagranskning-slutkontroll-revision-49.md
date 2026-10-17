# Samlad slutkontroll av faktagranskningen – revision 49

**Datum:** 2026-10-17  
**Underlag:** fem faktagranskningsprotokoll, revisionerna 44–48, samt samtliga redaktionellt godkända manuskapitel.  
**Beslut:** Den första selektiva faktagranskningen är sammanställd och avslutad. **Manuset är inte fullständigt faktaverifierat eller publiceringsgodkänt.**

## Kontrollens omfattning och evidens

De fem etapperna omfattar tillsammans **41 avgränsade påståendekluster** (7+8+8+8+10) för inledning och kapitel 1–20. Alla kapitel har därmed behandlats, men **inte varje påstående**. Varje tidigare granskningsprotokoll behåller sin egen sakbedömning och sina källhänvisningar. Inga nya kvantitativa prestandaanspråk eller rättsliga krav härleds från dessa stickprov.

Den samlade genomgången av restpunkterna fann **inga nya, styrkta sakfel** som motiverar en förändring av redan godkända manuskapitel. Detta är inte ett intyg om att inga sakfel förekommer.

## Övergripande reservationer att behålla i boken

1. **Arkitektur och ansvar:** Självständig driftsättning, databasseparation, organisationsroller och tillgänglighet är möjliga mål eller designval, inte universella garantier och organisationskrav (kap. 1–7, 18–20).
2. **Tillgänglighet och fel:** Hälsokontroller kan orsaka omstarter; återförsök kan öka överlast; idempotens är inte generell exakt-en-gång-garanti (kap. 5–6, 12).
3. **Konsistens och återställning:** Sagas kompensation är inte traditionell rollback, och en lyckad teknisk återläsning garanterar inte konsistent verksamhetsåterställning (kap. 7, 17).
4. **Kvalitet och driftbarhet:** Kontraktstester täcker endast avtalade interaktioner och relevanta versioner; observerbarhet är inte detsamma som automatiskt korrekt felanalys (kap. 9, 13–14).
5. **Säkerhet och plattform:** Logiska resursscope är inte fullständig säkerhetsisolering; tokenautentisering ersätter inte objekt- och funktionsauktorisation (kap. 11, 15).
6. **Livscykel och modernisering:** SBOM är inventeringsstöd, inte ett mått på faktisk sårbarhet; migrationsmönster passar olika bra beroende på system (kap. 16, 19–20).

## Prioriterade restpunkter inför publiceringsbeslut

| Prioritet | Åtgärd | Godkännandekriterium |
|---|---|---|
| P1 | Integrera spårbara källhänvisningar i boktext, noter eller kapitelslut. | Alla påståenden som kräver externa belägg kan följas till exakt källa med referensdatum. |
| P1 | Slutför kontroll av ej granskade specifika faktapåståenden, versioner och praktiska säkerhetsinstruktioner. | Inventering på påståendenivå och dokumenterad disposition av varje kontrollpunkt. |
| P1 | Säkerställ att illustrationer, förenklade modeller och organisationsförslag inte presenteras som normativa krav. | Alla fallbeskrivningar och rekommendationer är tydligt märkta. |
| P1 | Granska juridiskt färgade påståenden i den avsedda tillämpningskontexten, inklusive datahantering och loggning. | Gällande regler och avgränsningar verifierade eller formuleringarna tonade till generella principer. |
| P2 | Kontrollera terminologi, kapitelövergångar, tabeller och internt korsreferenssystem i slutmanus. | Språkgranskning och teknisk korrekturläsning dokumenterad. |
| P2 | Granska källstatus nära publiceringsdatum och dokumentera eventuella revideringar av standarder och dokumentation. | Versions- och åtkomstdatum dokumenterade. |
| P2 | Generera och granska PDF/EPUB för innehållsförteckning, rubriker, sidbrytning och tillgänglighet. | Provexporter visuellt och tekniskt godkända. |

## Kompletterande kontroll av tre primärkällor

Kontrollerade 2026-10-17:
- NIST, SP 800-218 SSDF v1.1, slutlig utgåva: https://csrc.nist.gov/pubs/sp/800/218/final – bekräftar ramverkets karaktär som rekommenderade utvecklingsrutiner.
- Kubernetes, *Liveness, Readiness, and Startup Probes*: https://kubernetes.io/docs/concepts/workloads/pods/probes/ – stöd för skillnaderna mellan typerna av kontroller.
- Microsoft Azure Architecture Center, *Saga distributed transactions*: https://learn.microsoft.com/en-us/azure/architecture/patterns/saga – stöd för kompensationsmönstrets förbehåll.

## Revisionsbeslut

Det finns inte tillräckligt stöd för att i detta steg ändra redan redaktionellt godkända kapitel. Samtliga manusfiler är därför oförändrade. Källgranskningens **första avgränsade omgång** avslutas; fullständigt faktagodkännande och publiceringsgodkännande **avvaktar** åtgärdslistan ovan.
