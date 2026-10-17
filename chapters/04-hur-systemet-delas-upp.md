# 4. Hur ska systemet delas upp?

När ett välbekant IT-stöd ska delas upp är det frestande att börja med det som går att se: en backend, några databastabeller eller en lista med befintliga moduler. Men det svåraste beslutet handlar inte om hur koden ska flyttas. Det handlar om **var gränserna ska gå för självständiga förändringar, tydligt ansvar och rimliga beroenden**.

Det valet påverkar både den som utvecklar funktionerna och den som ska hålla dem tillgängliga. För varje ny tjänst uppstår ett eget logiskt ansvar för version, driftsättning, observerbarhet, skydd och återhämtning. Gemensamma plattformar kan automatisera mycket av arbetet, men de tar inte bort behovet av en identifierbar tjänsteägare. Uppdelningen måste därför motiveras av en verklig nytta som överstiger kostnaden för fler gränser.

## Börja med verksamhetens behov, inte med tekniken

Tänk på det gemensamma ärendehanteringssystemet i tidigare kapitel. En handläggare registrerar ett ärende, bifogar handlingar, fattar beslut och skickar besked till en part. I monoliten kan allt detta genomföras av funktioner i samma backend mot en gemensam databas. Det innebär inte att funktionerna redan utgör lämpliga mikrotjänster.

Ett bättre första steg är att fråga vilken verksamhetsförmåga varje del representerar, vilka regler den ansvarar för och vilken information den behöver kunna förvalta. Ärendehantering och dokumenthantering kan till exempel ha olika regler för förändring, åtkomst, volym och lagring. Det talar för en möjlig gräns. Men om dokumenten endast är bilagor utan egen livscykel eller egna regler kan en separat dokumenttjänst innebära mer arbete än nytta.

En verksamhetsförmåga är inte automatiskt lika med en mikrotjänst. Den ger en utgångspunkt för analysen, inte en formel för antalet tjänster. Verksamhetsprocesser kan dessutom korsa flera sådana förmågor. Att handläggaren upplever ett sammanhängande arbetsflöde betyder alltså inte att alla aktiviteter behöver ligga i samma tjänst – men inte heller att varje aktivitet bör brytas ut.

## Gränser som följer regler och ansvar

En användbar tjänstegräns håller samman sådant som behöver förändras tillsammans. Om flera funktioner delar samma verksamhetsregler, ändras av samma skäl och måste upprätthålla gemensamma invarianta villkor finns det ett starkt argument för att hålla dem nära varandra.

En *invariant* är ett villkor som alltid måste vara sant, till exempel att ett ärende inte får markeras som slutligt avgjort utan ett giltigt beslutsunderlag. Om underlaget kommer från en annan tjänst behöver man avgöra om regeln måste kontrolleras synkront eller kan säkras genom en verksamhetsprocess med definierade mellanlägen. Om ett sådant villkor kräver tätt samordnade ändringar i flera tjänster kan gränsen vara olämplig – eller så måste processen uttryckligen utformas för att hantera flera steg och mellanlägen. Detta är ett arkitekturval, inte bara en implementationsteknik.

Domändriven design erbjuder användbara begrepp som avgränsade kontexter (*bounded contexts*). En avgränsad kontext är ett område där begrepp och regler har en konsekvent betydelse. Den kan hjälpa till att identifiera tjänstegränser, men en kontext kan realiseras av en eller flera tjänster; den behöver inte vara ett driftsatt program i sig.

Tjänstegränsen behöver också ha en rimlig koppling till ett team eller en tydlig ägare. En funktion som ständigt kräver samtidiga ändringar från flera ansvariga team blir inte särskilt självständig bara för att den har ett eget API.

## Tre tänkbara uppdelningar av dokumenthanteringen

Anta att verksamheten vill kunna vidareutveckla dokumentstödet oberoende av ärendehanteringen. Det finns minst tre rimliga lösningar:

**Alternativ A: Behåll dokumenthanteringen som modul i monoliten.** Ärende- och dokumentfunktionerna ligger kvar i samma driftsatta applikation men får tydligare interna gränssnitt och ägarskap. En förändring behöver inte passera ett nätverk och transaktioner kan i vissa fall hållas lokala. Däremot är leveranscykeln fortfarande gemensam om applikationen driftsätts som en enhet. Detta är ofta en bra start när oberoende driftsättning ännu inte ger tillräckligt värde.

**Alternativ B: Bryt ut en sammanhållen dokumenttjänst.** En tjänst får ansvar för dokumentmetadata, dokumentregler och ett väldefinierat kontrakt mot ärendehanteringen. Själva filinnehållet kan lagras i en gemensamt tillhandahållen objektlagring utan att dokumenttjänsten förlorar sitt informationsansvar. Den kan utvecklas och driftsättas separat, förutsatt att kontrakt och dataägarskap tillåter det. Men en ny nätverksgräns införs, liksom nya krav på hantering av otillgänglighet, loggning och behörighet.

**Alternativ C: Dela upp dokumentområdet ytterligare.** Lagring, metadata, konvertering och sökning blir separata tjänster. Det kan vara rimligt om delarna har tydligt skilda livscykler, belastningsmönster och ägare. Delade tekniska stödfunktioner som sökindex eller konvertering behöver dock inte automatiskt vara separata mikrotjänster med egna produktteam. Men för ett mindre ärendehanteringsstöd kan det skapa fyra driftobjekt och flera nya beroenden utan motsvarande verksamhetsnytta.

Jämförelsen måste även omfatta säkerhetsgränser, kostnader för jour och felsökning samt vilka verksamhetsflöden som försämras om dokumentstödet är otillgängligt. Dessa faktorer väger ibland tyngre än möjligheten till separat driftsättning.

Det avgörande är inte att välja den minsta möjliga tjänsten. Det är att välja **den minsta ändamålsenliga uppdelningen** för den aktuella organisationens behov.

## Hur beroenden avslöjar dåliga gränser

Ett första test är att föreställa sig en vanlig förändring. Verksamheten vill exempelvis införa en ny dokumentkategori med särskilda gallringsregler. Om ändringen kräver samtidiga kod- och databasändringar i ärendetjänsten, dokumenttjänsten och ytterligare en metadatatjänst är det värt att undersöka om ansvaret verkligen har lagts på rätt plats.

Samtidiga ändringar är inte alltid fel. Vissa verksamhetsförändringar berör flera områden och behöver samordnas. Varningssignalen är **återkommande och ofrånkomlig samordning även för små lokala förändringar**.

Ett andra test är att analysera samtalsmönstret mellan tjänsterna. Om en enda användaroperation kräver en lång kedja av synkrona anrop ökar beroendet av att många delar fungerar samtidigt. Om tjänster dessutom frågar direkt efter varandras interna datamodeller är gränserna sannolikt för svaga. Valet mellan synkron kommunikation, händelser och köer fördjupas i kapitel 6; här räcker slutsatsen att **kommunikationsbehovet måste påverka gränsdragningen**.

Ett tredje test handlar om data: vem har rätt att ändra informationen och definiera dess innebörd? En separat tjänst som förutsätter direkt skrivåtkomst till en annan tjänsts interna tabeller blir starkt kopplad till dess förändringar. Hur dataägarskap och konsistens kan lösas förklaras i kapitel 7.

## För driftorganisationen är en tjänstegräns också en driftgräns

Applikationsarkitekten ser ofta tjänstegränsen som en möjlighet att isolera förändringar. Driftorganisationen ser också ett nytt objekt att ta hand om: en komponent med egna versioner, konfigurationer, mätvärden, incidenter, säkerhetsbehov och beroenden.

Det betyder inte att varje mikrotjänst behöver en egen VM eller ett eget driftteam. Flera tjänster kan dela körplattform, automatiserad leveranskedja och övervakningsinfrastruktur. Skillnaden mellan logisk tjänst och exekveringsmiljö behandlas i nästa kapitel. Men även med en gemensam plattform måste det gå att veta **vilken tjänst som påverkar vilken verksamhetsfunktion**, vad den beror på och vart en incident ska eskaleras.

Anta att den nya dokumenttjänsten slutar svara. Ärendehanteringen kan kanske fortfarande visa befintliga ärenden men inte öppna bilagor. Om verksamheten uppfattar hela systemet som felaktigt räcker det inte att driften visar att ärendetjänstens process körs. Tjänstegränserna måste därför kombineras med en bild av användarflöden och beroenden. Metoderna för övervakning och incidenthantering utvecklas i kapitel 13 och 14.

En alltför fin uppdelning kan också skapa många certifikat, nätverksflöden, konfigurationer och larm. Det är legitimt att driftsidan invänder mot komplexiteten, precis som det är legitimt att applikationssidan vill möjliggöra oberoende utveckling. Dessa perspektiv bör vägas samman innan gränserna fastställs.

## Vem fattar beslutet?

Verksamhetsföreträdare kan beskriva vilka förmågor som behöver utvecklas oberoende och vilka krav som är kritiska. Applikationsarkitekter och utvecklingsteam analyserar verksamhetsregler, data, samspel och förändringsmönster. Drift- och plattformsfunktioner bidrar med konsekvenser för kapacitet, isolering, observabilitet, nätverk och driftkostnad. Säkerhetsfunktionen granskar skyddsbehov och tillitsgränser.

Beslutsmandatet behöver vara uttalat. Det kan ligga hos en ansvarig arkitekt, en produktorganisation eller ett gemensamt arkitekturforum, beroende på styrmodellen. Oavsett modell bör berörda parter förstå avvägningarna och någon ha mandat att väga helhetens kostnader mot de enskilda teamens frihet.

Ett konkret beslutsunderlag för dokumenttjänsten behöver inte vara omfattande. Det bör åtminstone dokumentera varför uppdelningen övervägs, vilka funktioner och data som ingår, vilka beroenden som uppstår, vilka driftskrav som följer, vem som äger tjänsten och under vilka förutsättningar beslutet ska omprövas.

## När uppdelningen blir en distribuerad monolit

En *distribuerad monolit* är en lösning där komponenter är tekniskt separerade men i praktiken så hårt beroende av varandra att de måste förändras, driftsättas eller hanteras som en enda enhet. Då får organisationen kostnaderna för distribution – nätverk, felhantering och fler driftobjekt – utan att få den eftersträvade självständigheten.

Symptom kan vara att många tjänster alltid måste släppas samtidigt, att interna databastabeller delas utan tydliga gränser, att varje enkel användarhandling kräver många tätt kopplade anrop eller att ändringar i ett team ofta blockerar flera andra. Inget enskilt symptom är ensamt avgörande, men mönstret bör granskas.

Den motsatta ytterligheten finns också: en tjänst som blivit så stor att många orelaterade förändringar konkurrerar om samma leveranscykel och team. Målet är inte maximal uppdelning utan **balans mellan sammanhållning inom tjänster och rimliga beroenden mellan dem**.

## Ett praktiskt beslutsprov

Innan dokumenthanteringen bryts ut kan projektgruppen ställa fem frågor:

1. Vilka verksamhetsregler och vilken information behöver hållas samman?
2. Vilka förändringar vill verksamheten och teamen verkligen kunna göra oberoende?
3. Vilka nya beroenden, felmöjligheter och driftobjekt skapar uppdelningen?
4. Vem tar långsiktigt ansvar för tjänsten och dess driftbarhet?
5. Skulle en tydligare modulär monolit uppfylla behoven med lägre komplexitet?

Beslutet blir mer användbart om man även beskriver hur det ska utvärderas: exempelvis minskade samordningsbehov vid ändringar, acceptabel felpåverkan och hanterbar driftkostnad. Sådana mått är exempel och ska väljas utifrån organisationens mål.

Om frågorna inte går att besvara är gränsen sannolikt för tidigt bestämd. En gradvis utbrytning med väl avgränsad modul och mätbara problem kan då vara klokare än ett stort engångsbeslut.

## Vad förändras för vem?

För **applikationssidan** blir tjänstegränsen ett beslut om vilka verksamhetsregler, data och förändringar som ska kunna utvecklas självständigt. Teamet måste samtidigt göra beroenden och felbeteenden begripliga för dem som driver helheten.

För **driftsidan** innebär samma beslut nya logiska driftobjekt, trafikflöden och beroenden att hantera. Det är därför viktigt att bidra till gränsdragningen innan en uppdelning har låsts i kod och leveransstruktur.

Det **gemensamma ansvaret** är att värdera faktisk verksamhetsnytta mot livscykel-, säkerhets- och driftkostnader, och att bestämma vem som får ompröva en olämplig gräns.

## Att ta med sig

En välvald tjänstegräns förenar verksamhetens behov av förändring med ett realistiskt tekniskt och organisatoriskt ansvar. För applikationssidan handlar den om tydliga regler, data och leveransoberoende. För driftsidan handlar den om hanterbara beroenden, diagnos, tillgänglighet och långsiktiga driftobjekt. Båda måste bidra för att gränsen ska ge självständighet i praktiken. [R3](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) [R1](https://martinfowler.com/articles/microservice-trade-offs.html)

I nästa kapitel följer den naturliga följdfrågan: när dokumenthanteringen väl har fått en egen logisk gräns, **var ska den då köras?**

### Källor och vidare läsning

- **[R3](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis)** Microsoft Learn, Azure Architecture Center, *Use domain analysis to model microservices* (åtkomst 2026-10-17).
- **[R1](https://martinfowler.com/articles/microservice-trade-offs.html)** Martin Fowler, *Microservice Trade-Offs* (2015).
