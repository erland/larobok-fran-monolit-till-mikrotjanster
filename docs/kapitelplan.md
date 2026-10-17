# Detaljerad kapitelplan – version 4

## Redaktionella grundregler

Gemensamt case: ärendehanteringssystem med frontend, backend, databas, VM:ar och senare en fristående dokumenttjänst. För varje kapitel prövas relevans ur både applikations- och driftperspektiv. Förklara tekniska konsekvenser utan att anta containrar, Kubernetes eller ett visst organisationsschema. Varje kapitel avslutas med **Vad förändras för vem?**.

## Inledning (00)
- **Budskap:** Läsaren känner redan en traditionell IT-vardag; boken förklarar konsekvenserna av nya ansvarsförhållanden.
- **Innehåll:** målgrupper, terminologi, läsanvisning, bokens jämförande metod och fiktivt system.
- **Status:** planerad; ingen läsarfärdig text skriven.

## Del 1: Från ett system till många tjänster

### 1. Det välbekanta IT-stödet
- **Kärnfråga:** Vad tog vi för givet när ett system hade frontend, backend och databas?
- **Huvudbudskap och innehåll:** Traditionell applikation, VM-topologi, zoner, leverans, förvaltning; monolitens faktiska styrkor.
- **Återkommande fall:** Beskriv nuläget med tre VM:ar och gemensam systemrelease.
- **För applikationsläsaren:** Känna igen design-, test- och releaseansvar.
- **För driftläsaren:** Känna igen server-, nätverks- och databasansvar.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Ingen värdering av mikroservicelösningar eller detaljerad modern plattform ännu.
- **Förslag till figur eller faktaruta:** Traditionell topologi och ansvarskarta (ej godkänd för bildproduktion).
- **Status:** planerad; ej skriven.

### 2. Vad händer när systemet delas upp?
- **Kärnfråga:** Vilka nya egenskaper och problem uppstår i en distribuerad helhet?
- **Huvudbudskap och innehåll:** Självständighet kontra koppling, nätverksfel, flera versioner, ökat antal driftsenheter.
- **Återkommande fall:** Bryt ut dokumentfunktionen; ett ärende kräver nu anrop till annan tjänst.
- **För applikationsläsaren:** Förstår varför intern kod blir fjärrkommunikation.
- **För driftläsaren:** Förstår varför övervaknings- och felbild förändras.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Detaljer om trafik, databaser och tillgänglighet reserveras för senare kapitel.
- **Förslag till figur eller faktaruta:** Översikt över monolit och distribuerad helhet (ej godkänd för bildproduktion).
- **Status:** första utkast skrivet (revision 4); redaktionell granskning återstår.

### 3. Vem ansvarar för vad när systemet blir distribuerat?
- **Kärnfråga:** Kan helhetsansvaret bestå när komponentansvaret fördelas?
- **Huvudbudskap och innehåll:** Verksamhetstjänst, mikrotjänst, plattform, säkerhet; utförare, beslutsfattare och uppföljare.
- **Återkommande fall:** Första ansvarskartan när dokumentfunktionen bryts ut.
- **För applikationsläsaren:** Ser tjänstens livscykelansvar och beroende till drift.
- **För driftläsaren:** Ser kvarstående ansvar och nya plattformsgränser.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Principer och introduktion; komplett RACI och styrning först i kapitel 18.
- **Förslag till figur eller faktaruta:** Ansvarskarta före och efter (ej godkänd för bildproduktion).
- **Status:** första utkast skrivet (revision 6); redaktionell granskning och extern faktakontroll återstår.

## Del 2: Att utforma och placera självständiga tjänster

### 4. Hur ska systemet delas upp?
- **Kärnfråga:** Hur väljer vi gränser som minskar samordning utan att öka komplexiteten i onödan?
- **Huvudbudskap och innehåll:** Verksamhetsförmågor, tjänstegränser, domäner, koppling, distribuerad monolit.
- **Återkommande fall:** Besluta om dokument respektive ärenden ska vara en eller två tjänster.
- **För applikationsläsaren:** Förstår ansvar, beroenden och förändringsbarhet.
- **För driftläsaren:** Förstår konsekvenser för driftsobjekt, larm och incidenter.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Inte kodexempel eller full DDD-metodik.
- **Förslag till figur eller faktaruta:** Alternativa tjänstegränser (ej godkänd för bildproduktion).
- **Status:** första utkast skrivet (revision 8); redaktionell tvåperspektivgranskning och extern faktakontroll återstår.

### 5. Var ska tjänsterna köras?
- **Kärnfråga:** Hur skiljer sig en logisk tjänst från VM, container och fysisk nod?
- **Huvudbudskap och innehåll:** VM per tjänst, delad VM, containrar, orkestrering, HA, placering, isolering.
- **Återkommande fall:** Driftsätt dokumenttjänsten som VM respektive container på delad plattform.
- **För applikationsläsaren:** Förstår resurskrav och vad exekveringsmiljön erbjuder.
- **För driftläsaren:** Förstår VM-drift, plattformslager och säker isolering.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Miljöernas provisionering tas i kapitel 8 och 11; inget Kubernetes-recept.
- **Förslag till figur eller faktaruta:** Jämförande exekveringsmodeller (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 11); extern källverifiering återstår.

### 6. Hur kommunicerar tjänsterna?
- **Kärnfråga:** Vilka arkitektur- och nätverksbeslut krävs när gränssnitt passerar process- och nätverksgränser?
- **Huvudbudskap och innehåll:** API, händelser, kö, kontrakt, timeout, nätverkszoner, brandvägg, DNS, lastbalansering, ingress.
- **Återkommande fall:** Ärendetjänsten hämtar dokumentmetadata när brandväggspolicy blockerar trafiken.
- **För applikationsläsaren:** Specificerar behov, kontrakt och feltåligt klientbeteende.
- **För driftläsaren:** Definierar/policystyr trafikväg, segmentering och trafikhantering.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Identitet och åtkomstbeslut fördjupas i kapitel 15; felmönster i kapitel 12.
- **Förslag till figur eller faktaruta:** Tjänstekommunikation och nätverksväg (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 13); extern källverifiering återstår.

### 7. Vem ansvarar för informationen?
- **Kärnfråga:** Vad händer när gemensamma SQL-joiner och transaktioner inte längre är självklara?
- **Huvudbudskap och innehåll:** Tjänsteägd datamodell, schema, migrering, eventual consistency, kompensation, DBA-tjänster.
- **Återkommande fall:** Ärendestatus och dokumentmetadata måste uppdateras i skilda datalager.
- **För applikationsläsaren:** Ansvarar för datakontrakt, modell och migrationsbeteende.
- **För driftläsaren:** Ansvarar för säker och tillgänglig databasplattform.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Backup/katastrofåterställning i kapitel 17, inte detaljer om produkter.
- **Förslag till figur eller faktaruta:** Dataägarskapsmatris och informationsflöde (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt, revision 15; extern källverifiering återstår.

## Del 3: Att utveckla, testa och driftsätta en distribuerad helhet

### 8. Hur förändras utvecklingsmiljöerna?
- **Kärnfråga:** Hur utvecklar vi en tjänst utan att alltid starta hela systemet?
- **Huvudbudskap och innehåll:** Lokalt körläge, mockar, simulerade beroenden, delade utvecklingsmiljöer, konfiguration.
- **Återkommande fall:** Utveckla dokumenttjänsten när ärendetjänsten inte finns lokalt.
- **För applikationsläsaren:** Får snabb återkoppling med relevanta beroenden.
- **För driftläsaren:** Tillhandahåller miljöresurser och säkra utvecklingsgränser.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Teststrategi i kapitel 9 och plattformskatalog i 11.
- **Förslag till figur eller faktaruta:** Lokalt och delat utvecklingsflöde (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt för fortsatt bokarbete, revision 17; extern källverifiering återstår.

### 9. Hur förändras testmiljöer och kvalitetssäkring?
- **Kärnfråga:** Hur vet vi att helheten fungerar utan en enda gemensam version?
- **Huvudbudskap och innehåll:** Kontraktstest, integration, end-to-end, tillfälliga miljöer, testdata, olika tjänsteversioner.
- **Återkommande fall:** Testa ärendeflödet mot dokumenttjänstens nya och gamla API.
- **För applikationsläsaren:** Äger tjänste- och kontraktstester.
- **För driftläsaren:** Äger möjligheten att skapa isolerade testmiljöer och säkra testdata.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Leveranspipeline i kapitel 10; undvik fullt automatiseringsverktygsdjup.
- **Förslag till figur eller faktaruta:** Testpyramid och miljömatris (ej godkänd för bildproduktion).
- **Status:** första utkast, revision 18; redaktionell granskning och extern faktakontroll återstår.

### 10. Hur levererar vi förändringar utan att störa helheten?
- **Kärnfråga:** Hur förändras styrning och tekniska releasemekanismer när versioner driftsätts oberoende?
- **Huvudbudskap och innehåll:** CI/CD, driftsättning, kompatibilitet, canary, rollback kontra roll-forward, revisionsspår.
- **Återkommande fall:** Rulla ut ny dokumenttjänst före ärendetjänstens ändring.
- **För applikationsläsaren:** Äger byggbarhet, test och migreringsstrategi.
- **För driftläsaren:** Äger säkra distributionsförmågor och produktionskontroller.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Undvik att upprepa testmetodik och incidentledning.
- **Förslag till figur eller faktaruta:** Förändringskedja från kod till produktion (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt, revision 20; redaktionell granskning och extern faktakontroll återstår.

### 11. Vem tillhandahåller miljöer och gemensamma förmågor?
- **Kärnfråga:** Vilka återanvändbara förmågor behöver finnas för självständig leverans?
- **Huvudbudskap och innehåll:** IaC, självbetjäning, plattformskontrakt, hemligheter, certifikat, DBaaS, policykontroller.
- **Återkommande fall:** Beställ tjänstemiljö genom deklaration i stället för manuell serverbeställning.
- **För applikationsläsaren:** Följer plattformsgränssnitt och deklarerar behov.
- **För driftläsaren:** Utformar, driver och stödjer plattformens bastjänster.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Val av fysisk exekvering i kapitel 5; IAM och policy i 15.
- **Förslag till figur eller faktaruta:** Tjänstekatalog och ansvar för leveransplattform (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 23); extern källverifiering återstår.

## Del 4: Att hålla en distribuerad helhet fungerande

### 12. Vad händer när en tjänst slutar fungera?
- **Kärnfråga:** Varför kan enskilda delar fungera samtidigt som verksamhetsflödet misslyckas?
- **Huvudbudskap och innehåll:** Partiella fel, retry-stormar, timeout, circuit breakers, degradering, driftbar design.
- **Återkommande fall:** Dokumenttjänsten svarar långsamt och hela ärendevyn hänger.
- **För applikationsläsaren:** Designar rimlig felhantering och användarbeteende.
- **För driftläsaren:** Förstår kapacitet, resursbelastning och felutbredning.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Incidentprocess i 14 och observerbarhet i 13.
- **Förslag till figur eller faktaruta:** Felkedja med och utan skyddsåtgärder (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 25); extern källverifiering återstår.

### 13. Hur vet vi att hela IT-stödet fungerar?
- **Kärnfråga:** Hur skiljer vi fungerande processer från gröna servrar?
- **Huvudbudskap och innehåll:** Mätvärden, loggar, traces, korrelations-ID, SLI/SLO, syntetiska flöden.
- **Återkommande fall:** En ärendeanvändare kan inte bifoga filer trots att alla VM:ar är uppe.
- **För applikationsläsaren:** Instrumenterar tjänsten och definierar betydelsefulla signaler.
- **För driftläsaren:** Tillhandahåller insamling, dashboards och larmroutning.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Felsökningsprocess och jour i 14.
- **Förslag till figur eller faktaruta:** Från servergrön till verksamhetsflöde (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 27); extern källverifiering återstår.

### 14. Hur felsöker och hanterar vi incidenter?
- **Kärnfråga:** Hur hittar vi felorsak och ansvar när flera team och tjänster är inblandade?
- **Huvudbudskap och innehåll:** Incidentledning, on-call, eskalering, spårning, samordnad kommunikation, lärande.
- **Återkommande fall:** Ett avbrott visar sig vara DNS/felkonfigurerad tjänst och inte applikationsbugg.
- **För applikationsläsaren:** Medverkar med domänkunskap och serviceägarskap.
- **För driftläsaren:** Medverkar med plattform, infrastruktur och incidentkoordinering.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Tekniska signaler från kapitel 13 förutsätts, inte återförklaras.
- **Förslag till figur eller faktaruta:** Incidenttidslinje och ansvarsväxling (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 29); extern källverifiering återstår.

### 15. Hur skyddar vi systemet och dess information?
- **Kärnfråga:** Hur fördelas identitet, åtkomst och säkerhetskrav över tjänstegränser?
- **Huvudbudskap och innehåll:** Användarautentisering, tjänsteautentisering, auktorisation, TLS/mTLS, IAM, hemligheter, patchkrav.
- **Återkommande fall:** Ärendetjänsten anropar dokumenttjänsten för en användare med begränsade rättigheter.
- **För applikationsläsaren:** Definierar och tillämpar verksamhetsbehörigheter.
- **För driftläsaren:** Tillhandahåller identitet, nyckelrotation och skyddsmekanismer.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Nätverkspolicy och routing förklaras i kapitel 6.
- **Förslag till figur eller faktaruta:** Åtkomstkedja användare → tjänst → tjänst (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt, revision 31; extern faktakontroll återstår.

## Del 5: Att långsiktigt förvalta tjänster och plattformar

### 16. Hur hanterar vi livscykler, underhåll och teknisk skuld?
- **Kärnfråga:** Vad betyder många självständiga livscykler för ändringskontroll och förvaltningsbarhet?
- **Huvudbudskap och innehåll:** Patchning, beroenden, sårbarheter, CMDB/tjänstekatalog, versioner, ägarskap, teknisk skuld.
- **Återkommande fall:** Tre tjänster använder föråldrat bibliotek och olika API-versioner.
- **För applikationsläsaren:** Ansvarar för egen kod och komponentberoenden.
- **För driftläsaren:** Ansvarar för basbilder, runtime, OS och plattformslivscykel.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Finansiell uppföljning i 17 och ansvarsstyrning i 18.
- **Förslag till figur eller faktaruta:** Livscykelkarta på flera nivåer (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt, revision 33; extern källverifiering och publiceringskontroll återstår.

### 17. Hur säkerställer vi återställning, kontinuitet och kostnadskontroll?
- **Kärnfråga:** Hur återställer vi verksamhetsförmåga när data och resurser är utspridda?
- **Huvudbudskap och innehåll:** Backup, återläsning, RPO/RTO, konsistens, återuppspelning, kontinuitetsövning, kapacitets- och kostnadsägarskap.
- **Återkommande fall:** Återställ dokumentdatabas från gårdagen medan ärenden har uppdaterats i dag.
- **För applikationsläsaren:** Verifierar dataåterhämtning och kompensationsregler.
- **För driftläsaren:** Levererar säkra backuper, återställning och kapacitet.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Datamodell förklarades i 7; håll här fokus på återhämtningsförmåga.
- **Förslag till figur eller faktaruta:** Återställningsövning över två tjänster (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 35); extern källverifiering återstår.

### 18. Hur organiserar vi ansvar och styrning över tid?
- **Kärnfråga:** Vem har mandat och ansvar för en fungerande verksamhetstjänst trots fördelad leverans?
- **Huvudbudskap och innehåll:** RACI, beslut, policy och undantag, SLA/SLO, kompetens, finansiering, samspel arkitektur/drift/säkerhet.
- **Återkommande fall:** Formulera ansvar när dokumenttjänst och nätverksplattform fallerar samtidigt.
- **För applikationsläsaren:** Ansvarar för tjänstens beteende och kontrakt.
- **För driftläsaren:** Ansvarar för plattformens leverans och gemensam incidentmodell.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Knyter ihop tidigare ansvar, inför inte ny plattformsteknik.
- **Förslag till figur eller faktaruta:** Samlad ansvarsmatris och eskaleringsmodell (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 37); extern faktakontroll återstår.

## Del 6: Att välja väg och hantera övergången

### 19. Hur lever vi med gamla och nya arkitekturer samtidigt?
- **Kärnfråga:** Hur undviker vi att en mellanperiod skapar otydliga gränser och permanent dubbel drift?
- **Huvudbudskap och innehåll:** Strangler-mönster, anti-corruption layer, migration, dubbel miljö, övergångsansvar.
- **Återkommande fall:** Dokumenttjänsten flyttas först medan övriga ärenden ligger kvar.
- **För applikationsläsaren:** Hanterar stegvis uppdelning och datakontrakt.
- **För driftläsaren:** Hanterar parallella drifts- och säkerhetsmodeller.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Undvik migreringschecklista på implementationsnivå.
- **Förslag till figur eller faktaruta:** Stegvis transformationskarta (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 39); extern källverifiering återstår.

### 20. När är mikrotjänster rätt väg?
- **Kärnfråga:** När motiverar självständighet den distribuerade komplexiteten?
- **Huvudbudskap och innehåll:** Monolit vs modulär monolit vs mikrotjänster, teamstorlek, risk, kostnad, mognad.
- **Återkommande fall:** Besluta om fler funktioner bör brytas ut eller stanna kvar.
- **För applikationsläsaren:** Värderar förändringsbehov och domängränser.
- **För driftläsaren:** Värderar operativ förmåga och total driftkostnad.
- **Ansvarsperspektiv:** Beskriv för varje relevant beslut vem som anger krav, fattar beslut, realiserar, driver och verifierar; redovisa alternativa organisationsmodeller.
- **Avgränsning/överlapp:** Ingen generell mikroservices-rekommendation.
- **Förslag till figur eller faktaruta:** Beslutsträd med tydliga antaganden (ej godkänd för bildproduktion).
- **Status:** redaktionellt godkänt (revision 41); extern källverifiering återstår.

## Helhetskontroll

- **Röd tråd:** en konkret förändring förklaras i applikation, infrastruktur och ansvar innan nästa förändring introduceras.
- **Balans:** undvik fyra kapitel i rad med isolerat applikations- respektive driftfokus.
- **Överlapp:** dataägande kap. 7 / återläsning kap. 17; kommunikationsnät kap. 6 / identitet kap. 15; utvecklingsmiljö kap. 8 / testmiljö kap. 9 / plattform kap. 11; ansvarskarta kap. 3 / slutlig styrning kap. 18.
- **Faktakontroll:** skilj distribuerade systems egenskaper från valfria metoder och produkter. Kontrollera särskilt säkerhets- och återställningspåståenden.
- **Publiceringsgrind:** text, källförteckning och faktagranskning återstår; bokprojektet är inte en färdig bok.
