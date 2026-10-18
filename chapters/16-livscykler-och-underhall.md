# 16. Hur hanterar vi livscykler, underhåll och teknisk skuld?

När ärendehanteringssystemet var en sammanhållen applikation kunde organisationen ofta planera ett gemensamt versionsbyte: en ny applikationsversion, ett uppdaterat operativsystem och kanske en databasmigrering inom samma förändringsfönster. Det var inte alltid enkelt, men det fanns en tydlig leverans att förhålla sig till. Efter uppdelningen i ärendetjänst, dokumenttjänst och notifieringstjänst kan komponenterna förändras vid olika tidpunkter. Det är en viktig fördel, men även en förvaltningsutmaning.

Mikrotjänster gör inte underhåll överflödigt. De flyttar en del av ansvaret från en central releaseplan till flera samtidiga livscykler som måste fungera tillsammans. En tjänst kan vara nybyggd och ändå använda ett gammalt bibliotek. Om ingen längre ansvarar för dess underhåll kan dessutom själva tjänsten bli en säkerhetsrisk även om den sällan ändras. En stabil serverplattform kan fortfarande bära en tjänst vars API ingen längre vågar ändra. Frågan är därför inte bara *när* vi uppgraderar, utan **vem som ser helheten och hur vi upptäcker det som håller på att bli oförvaltningsbart**.

## En tjänst har flera samtidiga livscykler

För dokumenttjänsten omfattar livscykeln åtminstone applikationskoden, dess bibliotek, språkets körmiljö, container- eller serveravbildning, operativsystem, databasmotor, API-kontrakt och eventuella meddelandeformat. Den är dessutom beroende av certifikat, identiteter och de plattformstjänster som gör den körbar. Dessa delar kan ha olika leverantörer, supportvillkor och slutdatum för underhåll.

Ett ramverk som fortfarande fungerar kan ha slutat få säkerhetsuppdateringar. En databasversion som stöds av leverantören kanske inte längre stöds av ett drivrutinsbibliotek. Ett API kan vara tekniskt tillgängligt, men ha konsumenter som bygger på beteenden som aldrig dokumenterats. Att bara uppdatera en versionssiffra löser inte de sambanden.

En användbar livscykelöversikt behöver därför visa vilka komponenter som finns, vem som äger dem, vilka beroenden de har och vilka datum eller händelser som kräver beslut. Den måste omfatta både direkta och transitiva beroenden där sådana kan identifieras, och skilja mellan en komponent som finns i en byggartefakt och en som faktiskt körs i produktion. Den bör vara tillräckligt konkret för att driva åtgärder, inte bara en inventering som uppdateras vid en årlig revision.

## Från central patchning till delat underhållsansvar

Tidigare kunde en driftorganisation patcha operativsystem och mellanprogramvara enligt en relativt enhetlig rutin. I en mikrotjänstmiljö kan plattformsteamet fortfarande ansvara för värdoperativsystem, kluster och förvaltade databastjänster. Men bibliotek och applikationsberoenden ligger ofta i varje tjänsts byggkedja. En containeravbildning har dessutom flera lager: en uppdaterad värd gör inte automatiskt en gammal basavbildning säker. Omvänt kan ett applikationsteam inte ensamt åtgärda en brist i den underliggande kluster- eller värdmiljön. Vem som patchar vad måste följa den verkliga driftsmodellen, inte en förenklad uppdelning mellan utveckling och drift.

Anta att tre tjänster använder samma föråldrade bibliotek. Säkerhetsfunktionen upptäcker en sårbarhet, men själva åtgärden kan behöva göras separat i tre kodbaser, testas mot tre uppsättningar beroenden och driftsättas vid tre olika tillfällen. Det gemensamma problemet kräver alltså både central överblick och lokalt genomförande.

En möjlig ansvarsfördelning är att säkerhetsfunktionen anger riskklassning och tidskrav, plattformsteamet erbjuder uppdaterade och godkända baskomponenter, varje applikationsteam uppgraderar och testar sina beroenden och ansvarig för den samlade tjänsten följer upp att inga kritiska luckor återstår. Om ett team inte kan uppgradera direkt måste ett tidsbegränsat undantag ha en utsedd riskägare, kompletterande skyddsåtgärder och en beslutad plan. Ett undantag är inte samma sak som att risken försvunnit. Om en säkerhetsuppdatering innebär en kompatibilitetsrisk behöver riskägaren väga konsekvensen av att avvakta mot konsekvensen av en snabb ändring, med kontrollerade tester och en tydlig omprövningstidpunkt.

## Beroendeförteckningar som faktiskt går att använda

Förvaltningen behöver kunna svara på vilka tjänster som påverkas när en sårbarhet eller en utfasning blir känd. Ett paketregister eller en programvaruförteckning kan visa vilka bibliotek som byggts in i en viss version. En tjänstekatalog kan visa ägare, driftmiljö, kontaktvägar, beroenden och kritikalitet. Den behöver även ange vem som tar vid när ett team upphör, eftersom ett tekniskt beroende ofta lever längre än den ursprungliga organisationen. En konfigurationsdatabas (CMDB) kan vara en del av denna helhetsbild, men den får inte förutsättas innehålla alla detaljer om varje byggartefakt.

Informationskällorna kompletterar varandra. Tjänstekatalogen svarar på *vem och vad*; bygg- och artefaktinformationen svarar på *vilken version*; driftens observationer svarar på *vad som faktiskt körs*. Om katalogen anger en uppdaterad version men produktionsmiljön fortfarande kör den gamla är förvaltningsproblemet inte löst. Därför behöver inventering och uppföljning knytas till verkliga driftsättningar och granskas vid avvikelser.

En programvaruförteckning, en SBOM (Software Bill of Materials), kan ge stöd, men den bevisar inte ensam att programvaran är fri från sårbarheter. Resultaten behöver sättas i relation till hur komponenten används, om den exponerade funktionen faktiskt är nåbar och vilka skydd som finns runt tjänsten.

## API:er och händelser lever längre än en enskild driftsättning

När dokumenttjänsten byter version måste ärendetjänsten fortfarande kunna anropa den. Den tekniska driftsättningen är bara ett steg i livscykeln för tjänstens gränssnitt. Ofta behöver en äldre och en nyare variant samexistera under en övergångsperiod.

Att lägga till ett valfritt fält kan ibland vara bakåtkompatibelt, men bara om konsumenterna hanterar okända fält och de faktiska valideringsreglerna tillåter ändringen. Att ta bort ett fält, ändra dess betydelse eller byta format på en händelse är ofta svårare. Asynkrona meddelanden kan dessutom ligga kvar i köer eller arkiv efter att producenten uppgraderats.

En praktisk modell är att först införa stöd för det nya beteendet, sedan migrera konsumenterna och först därefter ta bort den gamla varianten. För meddelandeflöden måste planen också omfatta meddelanden som producerats enligt äldre scheman men ännu inte behandlats. För databaser kan samma princip innebära att gammal och ny kod tillfälligt måste kunna använda samma datamodell. Under tiden behöver organisationen veta vilka versioner som används, vem som kontaktar beroende team och hur man ser att övergången är färdig. Att en äldre API-version är märkt som *utfasad* betyder inte att den kan stängas samma dag.

Versionshantering löser inte alla förändringsproblem: även samma version kan ändra svarstid, felmönster eller verksamhetsregler. Därför måste förändringsbedömningen omfatta både kontrakt och observerat beteende. Principerna för testning och kompatibilitet har behandlats i kapitel 9 och 10; här är frågan hur sådana gränssnitt **förvaltas över år**, även när ursprungsteamet ändras eller en leverantör lämnar organisationen. [R19](https://csrc.nist.gov/pubs/sp/800/218/final)

## Uppgraderingar som återkommande arbete

Om varje uppgradering skjuts upp tills något gått sönder byggs en skuld som blir svårare att hantera. Samtidigt kan helautomatiska uppdateringar av alla beroenden skapa en annan risk: kompatibilitetsbrott som upptäcks först vid körning. Automatisering behöver därför förenas med tester, stegvis införande och en möjlighet att stoppa en osäker förändring. Ett stort versionssprång kan kräva ändringar i kod, konfiguration, datamodell och driftsättningssätt samtidigt. Många mindre, kontrollerade uppgraderingar kan minska den risken, förutsatt att organisationen har fungerande automatiska tester, överblick över beroenden och tid avsatt för arbetet.

Det behövs därför en återkommande rytm för att granska uppdateringsbehov, planera underhåll och genomföra de förändringar som inte kan ske helt automatiskt. Vissa säkerhetsuppdateringar behöver hanteras snabbt; andra uppgraderingar kan samordnas med ordinarie utveckling. Risk, exponering, kompatibilitet och verksamhetens tolerans för avbrott avgör prioriteringen, inte en enda generell regel för alla tjänster.

Ett team som äger en mikrotjänst behöver ha utrymme att avsätta tid för denna sorts arbete. Annars kan självständiga team optimera för nya funktioner medan kostnaden för föråldrade komponenter hamnar hos framtida förvaltare eller hos driftorganisationen vid nästa incident.

## Teknisk skuld är mer än gammal kod

Teknisk skuld kan bestå av otydliga tjänstegränser, manuella driftsättningar, svagt teststöd, odokumenterade beroenden och provisoriska undantag i nätverksregler eller behörigheter. En tjänst som kräver en unik och gammal körmiljö kan hindra en gemensam plattformsuppgradering. Ett nätverksundantag som skapades för en felsökning kan bli kvar tills ingen längre vet varför det finns.

Det betyder att teknisk skuld inte enbart kan prioriteras av applikationsutvecklare. Drift och plattform måste kunna synliggöra kostnaden för speciallösningar, blandade versioner av språkens körmiljöer, avvikande övervakning eller manuella åtgärder. Säkerhetsfunktionen behöver visa vilka avvikelser som höjer risken, och verksamheten behöver förstå hur skulden påverkar leveransförmåga och kontinuitet.

Ett bra beslutsunderlag beskriver *konsekvensen* av att låta skulden ligga kvar: längre ledtider för uppgraderingar, högre sårbarhet, större incidentrisk eller svårare återställning. Det är mer användbart än en lista som bara säger att något är ”gammalt”.

## När något ska avvecklas

Självständiga tjänster bör också kunna tas bort. Men avveckling är inte samma sak som att stänga en server eller radera ett repository. Först måste man veta vilka användare och tjänster som fortfarande använder gränssnitten, var data finns, om information ska bevaras och vilka drift- och säkerhetsfunktioner som kan tas bort.

För dokumenttjänstens gamla API-version kan avvecklingsplanen innebära att identifiera konsumenter, annonsera sista stöddatum, migrera ärendetjänsten, övervaka återstående trafik och först därefter stänga gränssnittet. Loggning och telemetri kan behövas under en övergångsperiod för att upptäcka användning som inte finns dokumenterad. Avveckling av en hel tjänst kan dessutom kräva export, arkivering eller gallring av information enligt verksamhetens beslut och gällande regler.

Om en plattformstjänst ska upphöra måste plattformsteamet erbjuda en fungerande migreringsväg. Om en applikation inte kan följa med behöver orsaken och det tidsbegränsade ansvaret dokumenteras. Annars skapas nya tekniska särlösningar i försöket att bli av med gamla.

## Ett gemensamt förvaltningssamtal

Tänk dig ett kvartalsvis livscykelmöte för ärendehanteringsstödet. Dokumentteamet visar att ett bibliotek måste bytas innan stödet upphör. Driftteamet visar att den nuvarande körmiljön behöver uppgraderas. Ärendeteamet redovisar att det fortfarande använder ett äldre dokument-API. Säkerhetsfunktionen pekar på en känd sårbarhet och verksamheten informerar om en period när större förändringar bör undvikas.

Mötet behöver inte detaljstyra varje uppgradering. Syftet är att identifiera beroenden och beslut som inget team kan lösa ensamt. Vem äger åtgärden? Vilken sista tidpunkt gäller? Vad händer om den missas? Vilken åtgärd måste genomföras först? Vem finansierar arbetet och vem accepterar kvarstående risk? Vilket underlag visar att åtgärden är genomförd och att kvarstående risk är bedömd? Sådana frågor skapar en gemensam plan utan att återinföra en enda stor release för allt.

**För applikationssidan** innebär livscykelansvaret att kod, bibliotek, kontrakt och datamigreringar måste kunna vidareutvecklas utan långa stopp. **För driftsidan** innebär det att operativsystem, baskomponenter, databaser och plattformstjänster behöver uppdateras med kända beroenden och stödperioder. **För den samlade systemförvaltningen** handlar det om att se när en åtgärd korsar dessa gränser och säkerställa ett beslut, en ägare och en verifierbar slutpunkt.

En arkitektur med många tjänster blir inte långsiktigt hållbar bara för att varje tjänst kan driftsättas självständigt. Den blir hållbar när organisationen också klarar att uppgradera, ersätta och avveckla delarna utan att tappa kontrollen över helheten. I nästa kapitel förflyttas perspektivet från underhåll till den särskilda frågan om återställning, kontinuitet och kostnader när flera tjänster och datalager samverkar.

### Källor och vidare läsning

- **[R19](https://csrc.nist.gov/pubs/sp/800/218/final)** NIST SP 800-218, Secure Software Development Framework (SSDF) (kontrollerad 2026-10-17).
