# 2. Vad händer när systemet delas upp?

Det är måndag morgon. En handläggare öppnar ett ärende och väljer ett dokument. Tidigare hämtade samma backend både ärendeuppgifter och dokumentinformation ur den gemensamma databasen. Nu har dokumenthanteringen fått en egen tjänst. På skärmen ser arbetet likadant ut. Under ytan har en ny gräns uppstått: ärendehanteringen måste be en annan tjänst om hjälp.

Den skillnaden kan verka liten. Kanske är den nya dokumenttjänsten utvecklad i samma programmeringsspråk som den gamla backendmodulen. Kanske körs båda fortfarande på VM:ar i organisationens datacenter. Ändå förändras flera förutsättningar samtidigt. Två delar kan uppdateras vid olika tidpunkter. Ett anrop kan misslyckas trots att båda programmen var för sig fungerar. Och ett fel som användaren uppfattar som ett enda systemfel kan kräva insatser från flera team.

Detta kapitel handlar om vad uppdelningen *innebär*. Senare kapitel behandlar hur vi väljer tjänstegränser, utformar nätverket, fördelar data och organiserar driften i detalj.

## En uppdelning som börjar med ett verksamhetsbehov

Vårt fiktiva ärendehanteringssystem har vuxit. Dokumenthanteringens förändringstakt skiljer sig från resten av systemet. Verksamheten vill lägga till nya dokumentformat, förbättra sökningen och utveckla externa gränssnitt utan att varje gång behöva samordna en release av hela ärendehanteringen.

Det finns flera möjliga lösningar. Dokumentdelen kan förbättras som en tydligare modul inuti monoliten, eller så kan den skiljas ut som en egen distribuerad tjänst. Vi antar här att organisationen väljer det senare och att dokumenttjänsten får ett separat leveransflöde och en uttalad ägare. Detta är ett *fiktivt arkitekturbeslut*, inte ett påstående om att uppdelningen alltid är bättre.

Förut kunde backend anropa en intern funktion, exempelvis ”hämta dokumentmetadata”. Ett sådant anrop sker i regel inom samma körande program. Efter uppdelningen behöver ärendedelen begära motsvarande information via ett definierat gränssnitt. Förbindelsen kan gå över ett nätverk och beror på att dokumenttjänsten är nåbar, har kapacitet och förstår anropets version.

Den nya gränsen syns i arkitekturen, men även i organisationens vardag. Någon måste avgöra hur länge ärendedelen ska vänta på svar, vad användaren ska få se vid ett avbrott och vem som ska larmas när dokumenttjänsten inte kan leverera. Det är inte längre möjligt att betrakta dokumenthantering enbart som en intern kodstruktur.

## Från gemensam livscykel till flera livscykler

Ett sammanhållet system kan utvecklas modulärt, ha automatiserade tester och skalas med flera instanser. Det som särskiljer vårt nya exempel är inte att det plötsligt blir modernt, utan att dokumenttjänsten har en egen kör- och leveranslivscykel. Den kan i princip byggas, driftsättas och förändras utan att ärendedelen ändras, förutsatt att deras kontrakt förblir kompatibla.

Det ger en möjlig fördel: dokumentteamet kan rätta ett isolerat fel utan att driftsätta resten av ärendehanteringen. Men självständigheten är inte gratis. Om dokumenttjänsten ändrar svarets struktur så att ärendedelen inte längre förstår den, är förändringen i praktiken fortfarande samordnad. Oberoende driftsättning förutsätter alltså gränssnitt som utvecklas med hänsyn till sina användare.

När flera tjänster har skilda versioner finns inte alltid en enda versionsbeteckning som entydigt beskriver hela IT-stödet. Drift, support och felsökning kan behöva veta vilken version av varje berörd tjänst som faktiskt kördes när ett problem uppstod. Leveransinformation och spårbarhet behöver då knyta samman tjänsteversioner, konfiguration och tidpunkt, snarare än enbart hänvisa till en gemensam systemrelease.

För applikationssidan blir kontrakt, kompatibilitet och beroenden centrala designfrågor. För driftsidan blir det viktigt att kunna se den faktiska kombinationen av tjänster och förstå vilka förändringar som genomförts utan att hela systemet har tagits ur drift.

## En ny sorts fel: delar kan fungera samtidigt som helheten inte gör det

Anta att ärendetjänsten fungerar och dokumenttjänstens process är igång, men att nätverksförbindelsen mellan dem bryts. Båda kan svara på var sin enkel kontroll av att processen lever. En sådan kontroll visar inte nödvändigtvis om tjänsten kan utföra hela sin uppgift eller nå sina beroenden. Ändå kan handläggaren inte öppna sina dokument. Det är ett typiskt exempel på ett *partiellt fel*: en del av den distribuerade helheten fungerar inte, medan andra delar fortfarande gör det.

Andra fel kan vara mer svårtolkade. Dokumenttjänsten kanske svarar, men långsamt. Ärendedelen väntar och förbrukar resurser. Om många handläggare samtidigt försöker öppna dokument kan väntande anrop tränga undan annan verksamhetsfunktion. Ett begränsat problem i en tjänst riskerar därmed att sprida sig till andra delar av systemet.

En sådan felkedja är inte oundviklig. Men den behöver motverkas med medveten utformning: rimliga tidsgränser för anrop, begränsad resursförbrukning, försiktigt utformade återförsök (som annars kan förvärra överbelastning) och tydliga beslut om vad som kan fortsätta fungera när dokumenttjänsten är otillgänglig. Dessa tekniker utforskas närmare i kapitel 12.

Det intressanta för verksamheten är oftast inte vilken process som har fallerat. Frågan är om ett ärende går att handlägga. Därför behöver tekniska hälsomätningar kompletteras med förståelse för hela användarflödet. Övervakningen av enskilda komponenter och övervakningen av den samlade tjänsten besvarar olika frågor.

## Fler körande delar betyder fler saker att hålla reda på

En distribuerad arkitektur kan fortfarande drivas på traditionella VM:ar. En mikrotjänst behöver inte ha en egen VM, en egen fysisk server eller ens en egen databasserver. Samma VM kan köra flera tjänster, och en containerplattform kan placera flera instanser på gemensam infrastruktur. Valet påverkar isolering, kostnad och driftsättningssätt, men avgör inte ensamt om arkitekturen är en mikrotjänstarkitektur.

Det som förändras i vårt fall är antalet självständigt hanterade tjänster. Varje tjänst behöver en definierad väg till produktion, konfiguration, övervakning och rutiner för underhåll. Om den kan köras i flera instanser måste man kunna skilja på den logiska tjänsten och de faktiska instanser som för tillfället utför arbetet.

En traditionell inventering av tre VM:ar kan därför vara korrekt som infrastrukturförteckning men otillräcklig som karta över verksamhetsstödets beroenden. Vi behöver också veta vilken tjänst som talar med vilken, vilka gränssnitt de använder och hur beroendena påverkar användarnas arbetsflöden. Det betyder inte att traditionell konfigurationshantering försvinner. Den behöver kompletteras med tjänste- och beroendeinformation, i vissa miljöer automatiskt insamlad.

Här blir samspelet mellan utveckling och drift konkret. Applikationsteamet kan beskriva tjänstens krav på resurser, hälsa och kommunikation. Ett drift- eller plattformsteam kan erbjuda en säker och automatiserad exekveringsmiljö. Vilken grupp som konfigurerar en viss resurs beror på organisationens valda arbetsmodell, inte på ordet mikrotjänst.

## Ett beroende blir ett avtal mellan parter

När dokumenthanteringen låg i samma applikation kunde utvecklare i många fall ändra både anropande och anropad kod i samma ändring. Efter uppdelningen behöver de förhålla sig till ett kontrakt. Det måste vara begripligt för andra team, kunna provas och förändras utan onödiga störningar.

Kontraktet handlar inte bara om vilka fält ett API skickar tillbaka. Det omfattar även förväntat beteende: vad händer om ett dokument saknas, om användaren saknar behörighet eller om tjänsten är tillfälligt överbelastad? Vilka svar ska konsumenten kunna hantera? Och hur länge stöds en äldre variant av gränssnittet?

Dessutom finns ett driftskontrakt i praktisk mening. Vilken tillgänglighet förväntas? Hur snabbt måste fel upptäckas? Vem får förändra de nätverksförbindelser som krävs? Vem kan kontaktas vid problem? Inte allt behöver vara ett formellt avtal. Men utan gemensamma förväntningar uppstår lätt ett glapp mellan teknikens faktiska beteende och verksamhetens krav.

## Självständighet behöver avvägas mot samordning

Det kan vara lockande att anta att fler tjänster automatiskt leder till snabbare leveranser. Så behöver det inte bli. Om varje ny verksamhetsfunktion kräver samtidiga ändringar i fem tjänster, och inget team kan testa dem utan de andra, har uppdelningen inte skapat särskilt mycket självständighet. Organisationen kan då ha fått kostnaden för distribution utan motsvarande nytta.

Ett viktigt mått är därför inte antalet tjänster utan hur väl deras gränser stöder oberoende förändring. Vi behöver även räkna in kostnaden för nätverk, identifiering, övervakning, driftkompetens och incidenthantering. En modulär monolit kan i vissa situationer vara ett bättre svar på samma verksamhetsbehov.

Det betyder inte att varje tjänst måste vara fullständigt oberoende. Gemensamma krav på identitet, säkerhet, loggformat och leveransplattform kan ge bättre förutsättningar för självständighet, eftersom varje team slipper uppfinna samma lösningar. Skillnaden är mellan samordning som möjliggör självständighet och koppling som tvingar fram gemensamma ändringar.

## Ansvar följer inte automatiskt med när koden flyttas

I det gamla systemet kunde en förvaltningsansvarig samordna ändringar i dokumentdelen och driftorganisationen hantera den gemensamma miljön. När dokumentdelen blir en egen tjänst behöver det uttalas vem som ansvarar för dess funktion, säkerhetskrav, leveranser och driftbarhet. Men det betyder inte att ett utvecklingsteam automatiskt tar över brandväggar, databasserver, backup eller beredskap.

Ansvar behöver delas upp efter vad som faktiskt ska göras. Verksamhetsansvariga anger vilka funktioner och kvaliteter som krävs. Applikationsansvariga utformar tjänstens beteende och gränssnitt. Infrastruktur- och plattformsansvariga tillhandahåller överenskomna förmågor för körning, nätverk och drift. Säkerhetsfunktioner sätter och följer upp relevanta kontrollkrav. Organisationen måste dessutom utse ett tydligt ansvar för att den *samlade* ärendehanteringen fungerar.

Tänk på ett avbrott då handläggaren inte kan öppna ett dokument. Det räcker inte att ärendeteamet säger att dess tjänst fungerar och dokumentteamet säger att dess process är igång. Någon behöver leda felsökningen över gränserna och ta ansvar för användarpåverkan. Vem som gör vad fördjupas i kapitel 3 och senare i kapitlen om övervakning och incidenthantering.

## Två perspektiv på samma förändring

För den som kommer från applikationsutveckling innebär uppdelningen ett större ansvar att beskriva beroenden och utforma hur tjänsten beter sig när omvärlden inte svarar som väntat. Ett internt metodanrop har blivit en kommunikationsrelation som måste fungera under verkliga driftsförhållanden. Det ger möjlighet till självständigare leveranser men ställer också krav på kompatibilitet, tydliga gränssnitt och en överenskommen hantering av behörighetsbeslut över tjänstegränser.

För den som kommer från drift och infrastruktur är själva verksamhetsstödet fortfarande en helhet, men dess tekniska delar kan förändras oberoende och ha olika egenskaper. Driftsättningsobjekt, larm och samband blir fler. Samtidigt kan standardiserad plattformsteknik och automatisering minska det manuella arbetet per tjänst – om ansvar och verktyg är genomtänkta.

Båda perspektiven möts i samma fråga: Vilka delar måste vara självständiga, vilka gemensamma funktioner behövs och hur ser vi till att ansvar inte faller mellan teamen?

## Vad förändras för vem?

| Fråga | Applikation | Drift och infrastruktur | Gemensamt |
|---|---|---|---|
| Förändringar | Hantera kontrakt och kompatibilitet | Se faktisk version och konfiguration i drift | Leverera självständigt utan att bryta helheten |
| Fel | Hantera väntan, avbrott och degraderat beteende | Knyta tekniska signaler till tjänsteberoenden | Förstå användarpåverkan vid partiella fel |
| Miljöer | Beskriva resurs- och kommunikationsbehov | Erbjuda säker placering, åtkomst och övervakning | Skapa fungerande gränssnitt för självbetjäning och kontroll |
| Ansvar | Äga överenskommet tjänstebeteende | Äga överenskomna drifts- och plattformsförmågor | Utse ansvar för verksamhetsstödets funktion |

## När vi fortsätter

Utbrytningen av dokumenthanteringen har synliggjort något som förut låg inuti en sammanhållen applikation: beroenden, förändringar och fel passerar nu gränser mellan självständiga tekniska delar. Därför behöver ansvarsfördelningen bli tydligare, inte otydligare.

Nästa kapitel undersöker vem som faktiskt äger olika delar av den distribuerade lösningen – och varför ansvaret för användarens fungerande ärendehantering inte kan delas upp på samma sätt som koden. [R2](https://martinfowler.com/articles/microservices.html) [R1](https://martinfowler.com/articles/microservice-trade-offs.html)

### Källor och vidare läsning

- **[R2](https://martinfowler.com/articles/microservices.html)** James Lewis och Martin Fowler, *Microservices* (2014).
- **[R1](https://martinfowler.com/articles/microservice-trade-offs.html)** Martin Fowler, *Microservice Trade-Offs* (2015).
