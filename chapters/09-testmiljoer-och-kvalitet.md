# 9. Hur förändras testmiljöer och kvalitetssäkring?

En ny version av dokumenttjänsten klarar alla sina egna tester. Den är driftsatt i integrationsmiljön och svarar snabbt. Ändå kan handläggarna inte längre öppna dokument från ett ärende: ärendetjänsten skickar en förfrågan enligt ett äldre gränssnitt, och dokumenttjänsten förväntar sig ett nytt obligatoriskt fält. Varje team kan med visst fog säga att den egna tjänsten fungerar. Men IT-stödet fungerar inte.

Sådana integrationsfel kan även uppstå i traditionella system, men blir särskilt viktiga att hantera när tjänster levereras självständigt. I en monolit kan en gemensam systemversion ofta byggas, installeras och testas som en helhet. Med självständigt utvecklade och driftsatta tjänster finns inte alltid en enda versionskombination som representerar allt som kan möta produktion. Testningen måste därför ge svar på två frågor samtidigt: fungerar tjänsten på egen hand, och fortsätter verksamhetens flöden att fungera när andra tjänster utvecklas oberoende?

## Det välbekanta systemtestet räcker inte ensamt

I vårt traditionella ärendehanteringssystem finns utvecklings-, test- och produktionsmiljöer. En ny release innehåller typiskt sammanhållna ändringar i backend, frontend och databas. Den installeras i en gemensam testmiljö, där systemtest och acceptanstest genomförs innan driftsättning. Metoden har styrkor: en tydlig kandidat till produktionssättning, ett känt installationspaket och möjlighet att pröva användarflöden i en sammanhållen miljö.

När dokumenthanteringen blir en fristående tjänst ändras förutsättningarna. Ärendetjänsten och dokumenttjänsten får egna releaser. En tredje tjänst kanske publicerar händelser när ett beslut fattas. Integrationstestmiljön kan vid varje tidpunkt innehålla en annan kombination av versioner än produktion. Att vänta tills *alla* tjänster kan testas som en enda release skulle i praktiken återinföra ett centralt leveransberoende.

Det betyder inte att systemtester och acceptanstester ska överges. Det betyder att de behöver kompletteras med snabbare och mer avgränsade kontroller, tydliga kontrakt och verifiering av de risker som uppstår i samspelet mellan tjänster. [R10](https://docs.pact.io/getting_started/what_is_pact_good_for)

## Flera testnivåer besvarar olika frågor

Ett vanligt misstag är att välja antingen många isolerade tjänstetester eller omfattande end-to-end-tester. Det behövs normalt flera testnivåer med olika syften.

**Tester inom en tjänst** prövar affärsregler, validering och felhantering utan att alla beroenden behöver startas. Dokumenttjänsten kan till exempel verifiera att filformat och dokumentstatus hanteras korrekt. Dessa tester kan köras snabbt och ger ofta tydliga felmeddelanden. Men de visar inte att två tjänster tolkar ett gränssnitt likadant.

**Kontraktstester** prövar överenskommelsen mellan en tjänst som anropar ett gränssnitt och en tjänst som tillhandahåller det. Kontraktet kan gälla HTTP-anrop, meddelanden eller händelser: fältnamn, format, tillåtna värden, felkoder och ibland beteenden. Om ärendetjänsten behöver ett dokument-ID och en status ska en ändring hos dokumenttjänsten inte oväntat ta bort eller omdefiniera dessa uppgifter. Tester bör omfatta de konsumentkrav som faktiskt finns; ett godkänt kontraktstest är inte en garanti för hela verksamhetsflödet.

**Integrationstester** använder verkliga beroenden där det är motiverat: databas, kö, identitetsfunktion eller en annan tjänst. De fångar till exempel fel i serialisering, nätverkskonfiguration eller transaktionshantering. Sådana tester blir dyrare och svårare att felsöka ju fler komponenter som kopplas in samtidigt. Därför bör varje test ha en tydlig fråga.

**End-to-end-tester** följer ett användarflöde genom flera tjänster. Handläggaren registrerar ett ärende, bifogar ett dokument och öppnar dokumentet igen. Testet kan upptäcka att helheten brister trots att varje enskild tjänst verkar korrekt. Men ett stort antal sådana tester kan bli långsamma och instabila, särskilt när delade miljöer och asynkrona processer är inblandade. Ett mindre urval kritiska flöden ger ofta större nytta än att försöka testa alla variationer via användargränssnittet.

**Icke-funktionella tester** prövar andra egenskaper: kapacitet, svarstider, återhämtning, behörigheter, loggning och beteende vid bortfall. De är särskilt viktiga när en nätverksanslutning eller extern tjänst blir ett nytt felställe. Belastningstester ska även beakta gemensamma resurser, exempelvis databaser och köer, som flera tjänster kan överbelasta samtidigt.

Fel som uppstår på grund av fördröjningar, timeout och otillgängliga beroenden bör också testas avsiktligt. För asynkrona flöden behöver testen kunna vänta på ett definierat resultat med en rimlig tidsgräns, i stället för att förutsätta att händelsen hanteras omedelbart.

Testnivåerna kompletterar varandra. De är inte en universell pyramid med fasta procentsatser; sammansättningen bör styras av systemets risker, förändringstakt och kostnaden för att upptäcka fel sent. [R10](https://docs.pact.io/getting_started/what_is_pact_good_for)

## Hur vet vi att olika versioner fungerar tillsammans?

Anta att dokumenttjänstens API har version A i produktion. Teamet vill införa version B med en ny egenskap. Ärendetjänsten behöver fortfarande kunna använda de uppgifter den tidigare fått. Ett praktiskt mål är att kunna driftsätta B utan att samtidigt behöva ändra och driftsätta ärendetjänsten.

Det kan uppnås genom bakåtkompatibel förändring: lägg till ett frivilligt fält i stället för att omedelbart kräva det, behåll tidigare beteenden under en övergångsperiod och använd kontraktstester för att se att befintliga konsumenter fortfarande fungerar. I andra fall behövs parallella gränssnitt eller planerade migrationer. Även ett nytt frivilligt svarsfält kan störa en konsument som avvisar okända fält. Kompatibiliteten måste därför prövas mot faktiska konsumenter. Versionering är ett verktyg, inte en ersättning för att förstå konsumenternas verkliga beroenden.

En integrationsmiljö med enbart de *senaste* tjänsteversionerna fångar inte alla problem. Kontraktsverifieringen behöver dessutom använda de kontrakt som faktiskt representerar konsumenter i drift och under den planerade utrullningen; annars kan ett nytt kontrakt felaktigt se kompatibelt ut när en äldre konsument fortfarande använder gränssnittet. Det kan behövas tester mot kombinationer som faktiskt kan förekomma, exempelvis den gamla ärendetjänsten tillsammans med den nya dokumenttjänsten. Det är sällan rimligt att testa varje matematisk kombination av alla tjänsteversioner. Välj i stället kombinationer utifrån uttalade kompatibilitetslöften, beroendekartor, planerad utrullning och identifierade risker.

Samma resonemang gäller händelser i meddelandeköer. Ett nytt fält eller en ändrad tolkning kan påverka konsumenter som uppdateras långt senare. En producent behöver därför känna till vilka kontrakt som måste fortsätta fungera och hur gamla meddelanden hanteras under en övergång.

## Vad är en testmiljö i ett distribuerat system?

Tidigare kunde ett testmiljönamn peka på en avgränsad uppsättning VM:ar, applikationer och databaser. Med mikrotjänster kan samma namn avse en logisk miljö som delar fysisk kapacitet med andra miljöer. Man behöver skilja mellan *vilka tjänster och data som hör till miljön*, *vilken infrastruktur som kör dem* och *vilka säkerhetsgränser som faktiskt finns*.

Tre modeller kan användas, var för sig eller tillsammans:

- **Delad integrationsmiljö.** Flera team provar samspel i en gemensam uppsättning tjänster. Den kan ge realistiska beroenden och underlätta gemensam felsökning, men kräver styrning av ändringar, versionsspårbarhet, testdata och konflikter mellan tester.
- **Tillfällig miljö för en förändring.** En ändring får en kortlivad uppsättning relevanta tjänster eller resurser, ibland med simulerade beroenden. Det kan minska köer till en gemensam miljö, men kostar kapacitet och måste städas bort. En tillfällig miljö är inte automatiskt en fullständig kopia av produktion.
- **Separat miljö för kritisk helhetsverifiering.** Särskilda prestanda-, säkerhets- eller acceptanstester kan kräva mer stabil konfiguration, bestämda versioner eller starkare isolering. En sådan miljö kan vara dyr men motiverad av riskerna.

En miljö som delar kluster med andra får inte beskrivas som isolerad bara för att den har ett eget namn eller en egen namnrymd. Behörigheter, nätverkspolicyer, resurstilldelning, åtkomst till hemligheter och separation från produktion måste utformas och kontrolleras utifrån kraven.

## Testdata måste fungera över tjänstegränser

När den traditionella databasen delas upp kan ett ärende finnas i ärendetjänstens datalager samtidigt som dokumentets metadata och filinnehåll finns någon annanstans. Ett enkelt utdrag ur en databas är då inte säkert ett användbart testfall. Testdata behöver representera ett sammanhängande verksamhetstillstånd även om informationen ägs av flera tjänster.

I dokumentexemplet måste testmiljön kunna skapa ett ärende, koppla det till ett dokument och kontrollera vad som händer om uppladdningen misslyckas efter att ärendet registrerats. Testerna bör omfatta både lyckade flöden och situationer med fördröjda händelser, dubbletter, ogiltiga referenser och avbrott.

För testdata som bygger på produktionsinformation gäller särskilda krav på integritet, sekretess, åtkomst och gallring. Anonymisering eller maskning behöver bedömas utifrån om uppgifterna faktiskt går att återidentifiera. Syntetiska data är ofta lämpliga, men måste täcka tillräckligt realistiska variationer. Vid flera datalager behövs dessutom kontroller för hur data skapas och städas bort utan att lämna inkonsekventa rester i andra tjänster. Det finns ingen allmän regel om att en kopia av produktionsdatabasen är det bästa testunderlaget.

## Simulerade beroenden och verkliga integrationer

Kapitel 8 beskrev hur dokumentteamet kan arbeta lokalt med en simulerad ärendetjänst. För kvalitetssäkringen uppstår en ny fråga: hur vet vi att simuleringen fortfarande beskriver verkligheten? Om testdubbeln alltid svarar snabbt och aldrig returnerar fel kan den dölja precis de problem som är viktigast att förstå.

En bra strategi är att använda simuleringar för snabba och avgränsade tester, samtidigt som kontrakt och vissa integrationer verifieras mot verkliga implementationer. Testdubblar bör täcka överenskomna felbeteenden och uppdateras när kontrakten ändras. Den övergripande teststrategin behöver också bestämma var verkliga nätverkspolicyer, autentisering och köer ska ingå; annars kan en tjänst se felfri ut i laboratoriet men stoppas i produktion.

## När ett test misslyckas – vem agerar?

Ett end-to-end-test som inte kan öppna ett dokument ger inte automatiskt svar på vilket team som orsakat felet. Felet kan ligga i ärendetjänstens anrop, dokumenttjänstens kontrakt, nätverkspolicyn, identitetsinställningen eller testmiljöns data. Det bör därför finnas gemensam spårbarhet från testets körning till tjänsteversioner, anropsidentifierare och miljökonfiguration.

En möjlig ansvarsfördelning är att varje **applikationsteam** ansvarar för tester av den egna tjänstens regler och gränssnitt, inklusive relevanta kontrakt. **Plattforms- och driftfunktioner** tillhandahåller testmiljöernas exekvering, isolering, gemensam diagnostik och resurshantering enligt överenskomna förutsättningar. **Test- och verksamhetsfunktioner** bidrar med kritiska verksamhetsflöden, acceptanskriterier och bedömning av kvarstående risker. I delade miljöer behöver någon även ha mandat att prioritera miljöstabilitet och hantera tester som påverkar andra team. Vem som felsöker gemensamma tester, godkänner undantag eller beslutar om produktionssättning behöver anges uttryckligen; ingen av dessa arbetsfördelningar följer automatiskt av mikrotjänstarkitekturen.

För applikationsläsaren innebär förändringen att kontrakt, felbeteenden och testbarhet måste byggas in i tjänsterna, inte läggas till vid en gemensam sluttestvecka. För driftläsaren innebär den att miljön inte bara ska kunna etableras på ett reproducerbart sätt, som i kapitel 8, utan också **ge tillförlitliga och spårbara testresultat**. Det kräver kända tjänsteversioner, avgränsad testdata, gemensam diagnostik och tydliga regler när olika teams tester delar resurser.

## Vad vårt ärendehanteringssystem behöver verifiera

Inför nästa förändring av dokumenttjänsten väljer teamen ett begränsat antal tydliga kontroller. De provar dokumenttjänstens egna regler, kör kontraktstester mot ärendetjänstens förväntningar och testar verklig kommunikation via plattformens identitets- och nätverksfunktioner. Ett litet antal helhetstester verifierar att handläggaren kan lägga till och öppna ett dokument. Testerna dokumenterar också vilka delar av produktionsmiljön som inte efterliknas, så att kvarstående risker inte döljs av ett grönt testresultat. Ett feltest låter dokumenttjänsten bli otillgänglig och kontrollerar att gränssnittet visar ett begripligt fel i stället för en falskt tom dokumentlista.

Man testar inte alla tänkbara versionskombinationer, utan de kombinationer som kan uppstå under den planerade förändringen. I testresultatet anges vilken dokumenttjänst, ärendetjänst, konfiguration och testdatamängd som användes. När ett test misslyckas kan teamen därför börja med gemensamma fakta i stället för att gissa vem som ska ta ärendet.

I nästa kapitel följer vi själva leveransen. Hur kan en godkänd förändring driftsättas utan att kräva en samtidig gemensam release, och hur kan organisationen återgå eller gå vidare när något ändå går fel?

### Källor och vidare läsning

- **[R10](https://docs.pact.io/getting_started/what_is_pact_good_for)** Pact, When to use Pact (kontrollerad 2026-10-17).
