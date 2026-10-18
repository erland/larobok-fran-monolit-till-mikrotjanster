# 20. När är mikrotjänster rätt väg?

Efter att ha följt ärendehanteringssystemet från en sammanhållen applikation till ett system med flera tjänster är det frestande att ställa frågan: Borde vi dela upp resten också? Men bokens viktigaste slutsats är inte att varje monolit bör ersättas. Den är att en uppdelning förändrar vad organisationen behöver kunna utveckla, driva och förvalta – och att dessa konsekvenser måste ingå i beslutet från början.

En mikrotjänstarkitektur kan lösa verkliga problem. Den kan också skapa nya problem som är svårare än dem den var tänkt att undanröja. Valet behöver därför bygga på ett konkret förändringsbehov, inte på vilken arkitektur som för tillfället uppfattas som modern.

## Vilket problem försöker vi egentligen lösa?

I vårt ärendehanteringssystem uppstår kanske ett tryck att modernisera därför att en liten förändring i dokumenthanteringen kräver en stor, gemensam release. Kanske har dokumentfunktionen helt andra krav på lagring, skalning och informationssäkerhet än ärendehanteringen. Eller så hindrar en stor kodbas flera grupper från att arbeta självständigt.

Det är tre olika problem. De behöver inte samma lösning. Innan en tjänst bryts ut behöver vi också kontrollera om problemet främst kommer från arkitekturen eller från exempelvis bristande tester, gemensamma godkännandeflöden eller otillräckliga teammandat.

Om problemet främst är att ändringar i koden påverkar för många delar, kan tydliga moduler i samma applikation räcka. Om problemet är att dokumentlagringen behöver andra resurser, kan en separat lagringskomponent vara relevant utan att hela domänlogiken bryts ut. Om flera självständiga team däremot behöver leverera förändringar i olika takt kan en separat dokumenttjänst ge större nytta.

En användbar första fråga är därför: **Vilken förmåga behöver bli självständig, från vad och varför?** Svaret bör kunna kopplas till mätbara eller åtminstone observerbara problem: ledtid för förändringar, releasekonflikter, återkommande fel, kapacitetsbegränsningar eller svårt delat ägarskap.

## Alternativen är fler än monolit eller mikrotjänster

Det finns ingen skarp linje mellan en traditionell monolit och ett system bestående av många mikrotjänster. En **modulär monolit** kan ha tydliga interna gränser, separat testbar logik och väldefinierade ägarskap, men ändå byggas och driftsättas som en enhet. Den erbjuder ofta enklare lokala transaktioner, färre nätverksberoenden och lägre operativ kostnad än ett distribuerat system. Även en modulär monolit kräver disciplin kring modulgränser och information; annars återkommer den svårföränderliga sammanflätningen inom samma process.

En arkitektur med ett fåtal större tjänster kan vara ett annat rimligt val. Dokumenthanteringen kanske behöver brytas ut, medan handläggning, ärendestatus och arbetsflöde förblir tillsammans. Det behöver inte vara ett misslyckat mellansteg; det kan vara den arkitektur som bäst motsvarar verksamhetens krav under lång tid.

En mikrotjänst är dessutom inte bättre bara för att den är liten. Om varje verksamhetsförändring kräver samtidiga ändringar i fem tjänster har man skapat distribuerad samordning snarare än självständighet. Om tjänsterna delar skrivåtkomst till samma tabeller är gränserna i praktiken svagare än organisationsdiagrammet antyder.

Därför är **oberoende förändringsbarhet och tydligt ägarskap** mer intressanta än antalet tjänster eller deras kodstorlek.

## När nyttan kan överväga kostnaden

Mikrotjänster kan vara väl motiverade när olika verksamhetsförmågor förändras i tydligt olika takt och det finns team som kan ta ett uthålligt ansvar för respektive tjänst. De kan också ge värde när en del av systemet behöver annan kapacitet, särskild säkerhetsisolering eller en egen tillgänglighetsprofil. Men en separat driftsenhet ger inte automatiskt isolering: delad databas, identitetsplattform, nätverk eller kö kan fortfarande skapa gemensamma fel och angreppsvägar.

I ärendehanteringen kan dokumenttjänsten vara ett sådant fall. Den hanterar filer, lagringslivscykler och kanske stora datamängder, medan ärendetjänsten främst hanterar ärendenas status och arbetsflöden. En väl vald gräns kan göra det möjligt att utveckla dokumentfunktionen separat och att anpassa dess bearbetningskapacitet utan att driftsätta resten av ärendehanteringssystemet på nytt. Att enbart skala lagringen kräver däremot inte i sig en separat dokumenttjänst.

Men vinsten uppstår inte automatiskt när processen flyttas till en egen server eller container. Den uppstår först när API-kontrakt, informationsägarskap, driftsättning, testning, incidentberedskap och ansvar gör att teamen faktiskt kan arbeta med mindre inbördes beroenden.

Det är också möjligt att nyttan huvudsakligen finns för en enda funktion. Då är det rimligare att bryta ut just den än att dela upp allt på samma gång.

## När den enklare arkitekturen ofta vinner

Om systemet är relativt litet, förändras långsamt och förvaltas av ett litet team kan en välstrukturerad monolit vara enklare att förstå och säkrare att förändra. Detsamma gäller om verksamhetsreglerna ofta behöver ändras tillsammans eller kräver många starkt sammanhållna transaktioner.

I en monolit är vissa beroenden synliga i kod och databasscheman. I ett distribuerat system blir en del av dem i stället nätverksanrop, tidsberoenden, meddelanden och versionskontrakt. De försvinner inte: de byter form. Om organisationen saknar fungerande leveransautomation, observerbarhet, återställningsövningar och gemensamt incidentarbete kan den operativa komplexiteten snabbt överstiga den arkitektoniska vinsten.

Det betyder inte att en organisation måste ha en fullskalig plattform innan den får bygga sin första tjänst. Det betyder att förmågorna måste byggas i takt med den faktiska uppdelningen, och att det måste finnas ett finansierat ansvar för dem. [R23](https://martinfowler.com/articles/microservice-trade-offs.html)

## En jämförelse som omfattar hela livscykeln

Vid ett arkitekturval räcker det inte att uppskatta utvecklingsinsatsen. Utöver programmering behöver vi förstå testmiljöer, nätverks- och identitetslösningar, driftsättning, övervakning, beredskap, återställning, uppgraderingar och avveckling. Dessa aktiviteter pågår så länge tjänsten finns kvar.

För utvecklingsorganisationen kan självständiga releaser ge snabbare förändringar. För driftorganisationen betyder samma självständighet att fler förändringar, versioner och felbilder behöver hanteras. För verksamheten kan snabbare leveranser ge värde, men bara om helheten fortsätter vara tillförlitlig och någon kan ta ansvar när ett arbetsflöde brister.

Jämförelsen behöver därför omfatta tre alternativ: att förbättra den befintliga monoliten, att skapa tydliga moduler inom samma driftsenhet och att bryta ut utvalda tjänster. Bedöm både investering och återkommande kostnad. Räkna inte bara servrar eller molnresurser, utan även samordning, kompetens, säkerhet, jour, testning och förvaltningsarbete. Ta med övergångsperiodens dubbla lösningar, kostnaden för avveckling och riskerna med att under en tid behöva stödja både gamla och nya gränssnitt.

Ett kostnadsunderlag kan inte reducera alla dessa faktorer till ett exakt tal. Men det kan synliggöra var antagandena ligger och vilka osäkerheter som bör testas innan ett stort vägval görs.

## Beslutet prövas mot konkreta förutsättningar

Ett beslutsunderlag kan byggas kring några återkommande frågor:

1. **Verksamhetsnytta:** Vilket konkret problem ska lösas, och hur vet vi om lösningen lyckas?
2. **Gränser och data:** Finns en stabil verksamhetsgräns med tydligt informationsägarskap, eller krävs täta tvärgående uppdateringar?
3. **Team och mandat:** Kan ett team ansvara för tjänstens utveckling, leverans och operativa beteende över tid, samtidigt som helhetsansvaret är tydligt?
4. **Driftförmåga:** Har vi tillräcklig automatisering, övervakning, säkerhet, incidenthantering och återställning för den komplexitet vi inför?
5. **Ekonomi och livscykel:** Vem finansierar gemensamma förmågor, löpande underhåll och en framtida avveckling?
6. **Alternativ:** Kan samma mål nås med förbättrade moduler, ändrade arbetssätt eller en mindre omfattande uppdelning?

Beslutsunderlaget bör ange vilka antaganden som ännu inte är verifierade, vem som fattar beslutet, vilka alternativ som jämförts och när effekterna ska följas upp. Även en rekommendation att behålla monoliten är ett aktivt arkitekturbeslut som kan behöva omprövas.

Frågorna är inte en poängmodell som automatiskt ger rätt svar. De är ett sätt att få utveckling, drift, arkitektur, säkerhet och verksamhet att pröva samma beslut med sina olika kunskaper. Ett svar som inte kan förklaras för någon av dessa grupper är ofta ett tecken på att förutsättningarna ännu inte är tillräckligt genomarbetade.

## Börja litet och kontrollera att nyttan uppstår

Anta att vi ändå väljer att bryta ut dokumenthanteringen. Ett klokt första steg är då att definiera vad som ska bli bättre: kortare ledtid för dokumentrelaterade förändringar, färre gemensamma driftsättningar eller bättre förmåga att hantera stora filer. Samtidigt identifierar vi risker: fel vid nätverksanrop, inkonsekvens mellan dokument och ärenden och oklarheter kring behörigheter.

Därefter kan en begränsad funktion flyttas, med tydliga API-kontrakt och en plan för hur gamla och nya delar ska samverka. Före flytten behöver man bestämma vilka mått som ska jämföras med nuläget och vilka signaler som innebär att arbetet bör stoppas eller omprövas. Uppföljningen behöver mäta både önskad nytta och tillkommande kostnad. Har releaserna verkligen blivit mer självständiga? Har användarnas arbetsflöden blivit stabilare? Har drift- och säkerhetsarbetet fått rimliga förutsättningar? Är ansvarsfördelningen begriplig när en incident inträffar?

Om svaret är nej bör nästa steg inte automatiskt vara att skapa fler tjänster. Det kan vara att förenkla kontrakt, återförena alltför finfördelade funktioner eller förbättra plattformsförmågorna. Arkitektur är ett medel som får omprövas när verkligheten ger ny kunskap.

## Vad förändras för vem?

**För applikationsutveckling** innebär det att arkitekturvalet inte bara handlar om kodens struktur. Teamet måste visa att en tänkt tjänstegräns faktiskt minskar samordning och att det finns ett tydligt ägarskap för data, kontrakt och livscykel.

**För drift och infrastruktur** innebär det att kapacitet, nätverk, identitet, övervakning, återställning och säkerhet behöver vara en del av beslutet, inte något som beställs efter att uppdelningen redan är genomförd. Driftens perspektiv kan också visa när en enklare arkitektur ger bättre robusthet till lägre kostnad.

**För verksamhet och ledning** innebär det att välja vilka problem som är värda att lösa, finansiera de gemensamma förmågorna och säkerställa ett sammanhållet ansvar för det IT-stöd som användarna faktiskt möter.

**Tillsammans** behöver parterna kunna beskriva varför varje gräns finns, vem som ansvarar för den och när beslutet ska omprövas.

## Arkitekturens värde visar sig i vardagen

Bokens resa började med ett välbekant system: frontend, backend, databas och en hanterbar uppsättning servermiljöer. När dokumentfunktionen bröts ut blev flera tidigare interna frågor gemensamma frågor om trafik, information, fel, leverans, drift och ansvar. Ingen enskild teknik löste dem alla.

Det avgörande är därför inte om organisationen kan kalla sin lösning mikrotjänstbaserad. Det avgörande är om systemet går att förändra i den takt verksamheten behöver, om det går att förstå och återställa när något går fel och om ansvaret fungerar under hela dess livslängd.

**Den bästa arkitekturen är inte den mest uppdelade, utan den som ger rätt självständighet till en komplexitet som organisationen kan bära.**

### Källor och vidare läsning

- **[R23](https://martinfowler.com/articles/microservice-trade-offs.html)** Martin Fowler, Microservice Trade-Offs (kontrollerad 2026-10-17).
