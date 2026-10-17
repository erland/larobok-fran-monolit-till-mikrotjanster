# 1. Det välbekanta IT-stödet

Ett ärende kommer in på måndagsmorgonen. En handläggare öppnar det i webbläsaren, kompletterar uppgifter, lägger till ett dokument och skickar ärendet vidare. För användaren är allt detta delar av ett och samma IT-stöd. För organisationen bakom tjänsten är det också ofta ett sammanhållet objekt att utveckla, driftsätta, skydda och förvalta.

Innan vi undersöker vad mikrotjänster förändrar behöver vi förstå varför den modellen har fungerat så väl – och vilka antaganden som lätt följer med när man lämnar den.

## Ett system, flera tekniska delar

Vårt fiktiva ärendehanteringsstöd har tre tydliga huvuddelar: frontend, backend och en relationsdatabas. Frontend visar ärenden och tar emot användarens inmatning. Backend hanterar regler för till exempel ärendestatus, behörigheter och beslutsfattande. Databasen lagrar ärenden, dokumentmetadata, parter, beslut och historik.

Det betyder inte att systemet är enkelt. Backend kan rymma hundratals moduler, integrationer och affärsregler. Frontend och backend kan driftsättas separat, och databasen kan ligga på andra servrar. Det avgörande i detta exempel är snarare att flera funktioner förvaltas och förändras inom en gemensamt samordnad applikationshelhet.

En *monolit* betyder i arkitektursammanhang vanligen att en större del av applikationens funktioner levereras som en gemensam driftsättningsenhet. Frontend, backend och databas är däremot en beskrivning av tekniska lager, inte i sig ett bevis för att lösningen är monolitisk. Det är inte samma sak som dålig kodstruktur. En modulär monolit kan ha tydliga interna gränser och en välordnad domänmodell. Omvänt kan tre tekniska lager ha omfattande inbördes beroenden även när de körs på skilda servrar.

Vi använder fortsättningsvis det traditionella IT-stödet som jämförelsepunkt, inte som en karikatyr av föråldrad teknik.

## Från användarens funktion till driftens installation

På applikationssidan talar man ofta om funktioner: registrera ärende, fatta beslut, arkivera dokument. På driftsidan talar man ofta om installationer: applikationsserver, databasserver, lastbalanserare och anslutningar genom nätverket. I ett traditionellt system kan dessa två kartor relativt enkelt knytas till samma systemnamn.

En möjlig produktionsmiljö består av två virtuella maskiner för webb och applikation, en separat databasmiljö samt en lastbalanserare framför webbgränssnittet. Databasmiljön kan i sin tur bestå av flera instanser eller en hanterad databastjänst. I praktiken kan det finnas ytterligare noder för hög tillgänglighet, driftövervakning och integrationer. Det är inte antalet maskiner som gör miljön traditionell. Det är att installationen ofta planeras och förändras som en sammanhållen systemmiljö.

Applikationens arkitektur och driftens topologi är två olika bilder av samma lösning. Ett viktigt grundarbete är att kunna översätta mellan dem. En funktion kan köras på flera maskiner; en maskin kan bära flera funktioner. Den relationen är sällan exakt ett till ett, inte ens i en monolit.

## Miljöerna skapar förutsägbarhet

De flesta etablerade organisationer skiljer mellan utveckling, test och produktion. Ibland finns dessutom integrations-, acceptans- och utbildningsmiljöer. Varje miljö har sitt syfte, sina åtkomsträttigheter och sin driftmässiga förvaltning.

Applikationsgruppen kan arbeta i utvecklingsmiljön, sammanställa en release och lämna över den för test. Driftorganisationen kan etablera servrar, öppna nätverksförbindelser, installera certifikat, säkra databaser och planera driftsättningen. Testorganisationen kan verifiera den nya systemversionen mot ett definierat urval av testdata.

Detta behöver inte ske manuellt. Även traditionella system kan använda automatiserade bygg- och leveransflöden, infrastruktur som kod och självbetjäning. Skillnaden som blir viktig senare är att **systemets delar ofta har en gemensam leveransrytm och att miljön ses som en installation av just detta system**.

## Ansvar som löper genom flera organisationer

En vanlig ansvarsfördelning kan se ut så här:

| Område | Typiskt ansvar i traditionell organisation | Det som måste samordnas |
|---|---|---|
| Funktion och applikationskod | Utvecklings- och applikationsförvaltning | Krav, kvalitet, felrättningar och release |
| Servrar och virtualisering | Infrastrukturdrift | Kapacitet, operativsystem, tillgänglighet och patchning |
| Nätverk och brandväggar | Nätverksdrift och säkerhetsfunktion | Tillåtna trafikflöden, zoner och felsökning |
| Databasteknik | DBA eller databasdrift | Installation, prestanda, backup och återställning |
| Behörighet och autentisering | Applikationsansvariga tillsammans med identitetsfunktion | Inloggning, roller, åtkomstkontroll och spårbarhet |
| Verksamhetsfunktion och prioritering | Systemägare eller verksamhetsnära förvaltning | Nytta, finansiering och förändringsbeslut |

Tabellen beskriver ett vanligt organisationsmönster, inte en universell ansvarsfördelning. Flera roller kan ligga i samma team, och molntjänster eller externa leverantörer kan flytta det praktiska utförandet. Men ansvar måste ändå vara uttalat. För varje område behöver man skilja på verksamhetens krav, tekniska beslut, den dagliga driften och uppföljningen av att tjänsten fungerar.

Det traditionella systemnamnet fungerar ofta som en gemensam referenspunkt. Systemägaren kan samtidigt ansvara för verksamhetens samlade nytta utan att själv ansvara för exempelvis nätverkskomponenternas tekniska drift. När drift får larm om *ärendehanteringen* finns kända kontaktvägar, systemdokumentation och en avgränsad uppsättning komponenter att undersöka.

## Den gemensamma databasen är både styrka och beroende

En gemensam relationsdatabas gör det ofta enkelt att läsa och uppdatera sammanhängande information i en transaktion. Om ett beslut registreras och ärendets status ska uppdateras kan båda förändringarna i många fall genomföras atomärt: antingen lyckas båda eller också rullas de tillbaka.

Det ger en begriplig konsistensmodell. Databasadministratörer kan arbeta med index, behörigheter, replikering, backup och återställning med kännedom om en gemensam databasinstallation. Utvecklare kan göra sammanställningar över flera tabeller utan att nödvändigtvis använda ett nätverksanrop mellan varje informationsområde.

Samtidigt uppstår kopplingar. Om många funktioner läser direkt ur samma tabeller kan en schemaändring få stora konsekvenser. En långvarig transaktion kan påverka andra delar av systemet. Ett växande databasbehov kan tvinga fram gemensamma prioriteringar. Den gemensamma databasen är därför både en integrationsfördel och en potentiell begränsning för oberoende förändringar. Att samla data i samma databasteknik behöver dock inte innebära att alla moduler tillåts läsa och skriva varandras tabeller.

Här finns en lärdom som blir central senare: att dela upp dataansvaret kan minska vissa kopplingar, men det tar också bort möjligheten att utan vidare förlita sig på en enda databastransaktion för alla verksamhetssteg.

## Nätverk, brandväggar och lastbalansering har tydliga platser

I vår traditionella miljö kan nätverket beskrivas med ett relativt begränsat antal flöden: användare till webbgränssnitt, webb/applikation till databas och anslutningar från applikationen till ett antal externa system. Brandväggsregler och säkerhetszoner kan dokumenteras per systemmiljö och tekniskt lager. Lastbalanseraren styr trafik till tillgängliga applikationsinstanser.

Det betyder inte att nätverket alltid är statiskt eller enkelt. Men antalet kommunikationsparter är ofta hanterbart och förändringar kan kopplas till en samordnad release. Det blir relativt tydligt vilken grupp som hanterar nätverkskomponenten och vilken applikationsgrupp som behöver beskriva sitt trafikbehov. Även i traditionella miljöer kan trafikregler vara automatiserade och åtkomsten styras med identiteter snarare än enbart IP-adresser.

Autentisering kan vara integrerad med organisationens identitetsplattform och auktorisation kan genomföras i backend. Redan här behöver ansvar delas mellan identitetsfunktion, applikation och säkerhetsorganisation. Ett traditionellt system har alltså redan tvärfunktionella beroenden; mikrotjänster skapar inte behovet av samarbete från ingenting.

## Att driftsätta en förändring

Anta att verksamheten vill införa en ny regel: ett ärende får bara avslutas när vissa dokument har granskats. Utvecklare ändrar affärslogiken, kanske databasens schema, och anpassar användargränssnittet. Testarna verifierar att ärendet inte kan avslutas i fel tillstånd. En release förbereds och driftansvariga säkerställer att version, databasförändring och instruktioner passar ihop.

Vinsten med samordningen är att den förväntade systemversionen kan definieras som en helhet. Nackdelen är att även en begränsad ändring ibland måste passera samma bygg-, test- och driftsättningsflöde som större förändringar. Om många team vill leverera i olika takt blir den gemensamma leveransrytmen ett organisatoriskt beroende.

Det går att minska detta med modulär design och god automatisering, utan att omedelbart införa mikrotjänster. Frågan är hur långt behovet av självständighet faktiskt sträcker sig.

## Drift när något går fel

Föreställ dig att användarna inte längre kan öppna ärenden. Driftövervakningen visar kanske hög svarstid i backend och ökad belastning på databasen. En drifttekniker kontrollerar CPU, minne, nätverksförbindelser och databashälsa. En applikationsutvecklare söker i applikationsloggar och jämför med den senaste releasen. DBA granskar frågor och låsningar. Tillsammans avgränsar man felet.

Här finns en viktig styrka: antalet steg mellan användarens begäran och databasen kan vara relativt få. Men inte heller i en traditionell applikation räcker serverstatus som bevis på att verksamhetsfunktionen fungerar. Servern kan vara igång medan ett affärsflöde är trasigt. Det är därför missvisande att framställa verksamhetsnära övervakning som något som först uppfanns med mikrotjänster.

Skillnaden framöver är att ett fel kan uppstå i en tjänst, bero på en annan, förstärkas av en tredje och ändå upplevas av användaren som ett enda fel i ärendehanteringen. Därför blir spårbarhet och tydlig incidentledning ännu viktigare.

## Förvaltning över lång tid

Ett IT-stöd är mer än sin nästa release. Operativsystem ska uppdateras, databasmotorn behöver underhållas, certifikat löper ut och beroenden kan bli osäkra. Kapacitet måste planeras, dokumentation hållas aktuell, backup provas och återställningsrutiner fungera även när ordinarie personal inte är tillgänglig.

I en sammanhållen applikation kan mycket av detta planeras runt systemets gemensamma livscykel. Driftfönster, uppgraderingsprojekt och förvaltningsbudget knyts till ett tydligt objekt. Det gör kostnaderna synliga men kan också innebära att hela systemet måste samordnas för en uppgradering som bara berör en del.

Den löpande förvaltningen visar därmed samma dubbla egenskap som arkitekturen: central samordning gör vissa saker enklare och andra långsammare.

## Det som är värt att behålla

När organisationer moderniserar IT-stöd finns en risk att det invanda beskrivs som felaktigt. Det vore en olycklig utgångspunkt. Tydlig systemdokumentation, kontrollerade förändringar, ansvarig drift, etablerade säkerhetskrav och prövad återställningsförmåga är värdefulla oavsett arkitektur. Mikrotjänster förändrar hur detta genomförs, inte varför det behövs.

Tre styrkor hos en välbyggd monolit förtjänar att lyftas fram. Den kan ha lägre komplexitet i drift eftersom färre självständiga komponenter måste övervakas. Den kan underlätta konsekvent datahantering inom samma transaktionsgräns. Och den kan ge enklare felsökning när ett användarflöde huvudsakligen sker inom en process. Dessa fördelar kan väga tungt i verksamheter där förändringstakten är måttlig eller teamen få.

Det finns samtidigt situationer där en gemensam livscykel blir begränsande: när delområden behöver förändras oberoende, skala på olika sätt eller ha särskilda krav på tillgänglighet och säkerhet. Då kan en uppdelning i självständiga tjänster vara motiverad. Men de nya friheterna kommer med nya beroenden.

## Frågan vi tar med oss

Vårt ärendehanteringsstöd fungerar. Handläggaren kan registrera, bedöma och avsluta ärenden, och organisationen vet i stora drag hur systemet ska förvaltas. Ändå har verksamheten börjat kräva snabbare utveckling av dokumenthantering och notifieringar än resten av systemet kan leverera.

Vad händer om dokumentfunktionen bryts ut till en egen tjänst? Då uppstår frågor som tidigare kunde hanteras inom samma applikation: Hur kommunicerar ärendedelen med dokumentdelen? Vem äger dokumentinformationen? Var körs den nya tjänsten? Hur upptäcks ett avbrott? Vem ansvarar när den samlade ärendehanteringen inte fungerar?

Nästa kapitel börjar med just den förändringen. Poängen är inte att den gamla arkitekturen var fel, utan att en ny arkitektur ändrar vad organisationen måste kunna kontrollera och samordna. [R1](https://martinfowler.com/articles/microservice-trade-offs.html)

### Källor och vidare läsning

- **[R1](https://martinfowler.com/articles/microservice-trade-offs.html)** Martin Fowler, *Microservice Trade-Offs* (2015).
