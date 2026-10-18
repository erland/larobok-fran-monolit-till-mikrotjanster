# 18. Hur organiserar vi ansvar och styrning över tid?

När ärendehanteringen kördes som ett sammanhållet system var det ofta möjligt att tala om ett systemförvaltningsobjekt, en samlad leveransplan och en etablerad driftorganisation. Den uppdelade lösningen består i stället av ärendetjänst, dokumenttjänst och flera gemensamma plattformsfunktioner. Var och en kan ändras, driftsättas och underhållas separat. Ändå möter användaren fortfarande **ett** IT-stöd.

Det är just detta som gör styrningen svår: självständiga tekniska delar behöver ha tydliga ägare, men ansvaret för en fungerande verksamhetsförmåga kan inte försvinna mellan dem. Mikrotjänster tar alltså inte bort behovet av systemansvar. De förändrar vad ansvaret måste omfatta och hur det utövas.

## Ansvar som behöver hållas samman

Vi kan skilja mellan tre kompletterande ansvarsnivåer. För det första finns **verksamhetsansvaret**: vilka arbetsmoment ska fungera, vilken information är kritisk och vilka avbrott kan tolereras? För det andra finns **tjänsteansvaret**: vem bestämmer över en tjänsts beteende, kontrakt, kvalitet och vidareutveckling? För det tredje finns **plattforms- och driftansvaret**: vem tillhandahåller och förvaltar körmiljö, nät, lagring, identitetsfunktioner, övervakning och säker drift? Säkerhets- och informationskraven korsar dessa ansvar, precis som i kapitel 3; de upphör inte att vara ett särskilt uppdrag när vi här fokuserar på långsiktig styrning.

Nivåerna sammanfaller ibland organisatoriskt. Ett team kan både utveckla och driva sin tjänst. På andra håll är utveckling och drift skilda, eller så levereras en del av plattformen av en extern leverantör. Inget av alternativen är automatiskt rätt för alla verksamheter. Avgörande är att gränserna är begripliga och att beslut, incidenter och förändringar inte fastnar mellan dem.

Ett fjärde, sammanhållande uppdrag behövs ofta: någon måste ha mandat att följa upp **hela ärendehanteringsförmågan**, även när ett problem inte kan hänföras till en enda tjänst. Uppdraget kan ligga hos en produktägare, en systemansvarig eller en gemensam ledningsfunktion. Titeln är mindre viktig än ett tydligt mandat, finansiering och möjligheten att prioritera gemensamma förbättringar. Helhetsansvar innebär inte att personen ensam utför alla åtgärder eller kan överpröva säkerhetskrav; mandatets gränser måste vara definierade.

## Vem bestämmer, vem utför och vem följer upp?

Ett vanligt misstag är att skriva att ”teamet ansvarar” utan att ange vilken sorts ansvar som avses. Att formulera behov, fatta ett riskbeslut, genomföra en ändring och verifiera resultatet är olika handlingar.

Anta att dokumenttjänsten behöver byta lagringslösning. Verksamheten behöver formulera krav på åtkomst, sekretess och återställningstid. Dokumentteamet behöver bedöma hur information och gränssnitt påverkas. Plattform och drift behöver beskriva tekniska alternativ och deras operativa konsekvenser. Säkerhetsfunktionen behöver bidra med krav och granskning. En utsedd beslutsfattare behöver godkänna kvarvarande risk och kostnad. Efter införandet behöver någon kontrollera att dokumentflödet fortfarande fungerar enligt de överenskomna målen.

En enkel ansvarsmatris kan hjälpa till. Men matrisen bör inte bli en katalog över alla tänkbara arbetsmoment. Välj i stället de beslut och händelser som verkligen kräver samordning: nya tjänster, kontraktsändringar, produktionssättning med förhöjd risk, större incidenter, säkerhetsundantag och avveckling. För varje sådan situation bör det framgå **vem som beslutar, vem som genomför, vem som måste rådfrågas och vem som följer upp**. Det behöver också finnas en väg framåt när parterna inte är överens. En ansvarsmatris beskriver uppgifter, men ersätter inte formella befogenheter, avtal eller den lagstiftning som styr verksamheten. Särskilt för säkerhetsrisker och personuppgifter måste det vara klart vem som får acceptera vilken risk och när frågan måste lyftas vidare. [R21](https://martinfowler.com/articles/microservices.html)

## Självständiga team inom gemensamma ramar

En viktig fördel med mikrotjänster kan vara att olika team arbetar i sin egen takt. Om varje dokumentförändring måste passera samma centrala godkännande som en stor systemrelease försvinner en del av vinsten. Men om teamen får fatta alla beslut utan gemensamma ramar ökar risken för inkompatibla gränssnitt, otydlig informationsförvaltning och varierande säkerhetsnivåer.

Gemensamma ramar kan exempelvis ange hur identiteter hanteras, vilka minimikrav som gäller för loggar och spårning, hur sårbarheter rapporteras, hur API:er versioneras och hur tjänster registreras i en katalog. Ramarna bör i största möjliga mån byggas in i utvecklings- och plattformstjänsterna som **användbara standardvägar**, snarare än kontroller som kräver manuell handläggning vid varje liten ändring.

Undantag kommer ändå att behövas. Ett undantag från en teknisk eller säkerhetsmässig regel bör därför ha en namngiven beslutsfattare, dokumenterad motivering, tidpunkt för omprövning och plan för hur risken begränsas. ”Det har alltid fungerat så” är inte en hållbar undantagsprocess.

## En gemensam plan utan en gemensam release

I monoliten kan den årliga förvaltningsplanen ofta organiseras kring en produkt och några större releaser. I ett mikrotjänstlandskap finns flera leveransplaner, men också beroenden som kräver samordning. Dokumenttjänstens ändrade kontrakt kan behöva förberedas innan ärendetjänsten börjar använda det. En plattformsuppgradering kan påverka alla tjänster. Gemensamma sårbarheter kan kräva åtgärder inom samma tidsfönster.

Förändringar i delade gränssnitt behöver dessutom en dokumenterad kommunikationsväg till konsumerande team, även när den levererande tjänsten kan driftsättas självständigt.

En sammanhållen plan behöver därför visa både **varje tjänsts prioriteringar** och **de beroenden som sträcker sig över teamgränserna**. Den behöver inte detaljstyra varje driftsättning. Däremot bör den synliggöra planerade större förändringar, tekniska livscykelbeslut, gemensamma risker, kapacitetsbehov och mål för hela IT-stödet.

Om den samlade verksamhetsförmågan mäts med tjänstenivåmål, exempelvis tiden från uppladdning till synligt dokument, måste även ägarskapet för måttet vara tydligt. Ett team kan ansvara för sin tjänsts indikatorer, men ett helhetsmått behöver en funktion som kan samla flera team kring förbättringar. Detta ersätter inte respektive tjänsts ansvar utan lägger en gemensam nivå ovanpå det.

## Finansiering och kostnader som inte följer teamgränserna

En distribuerad lösning kan göra vissa kostnader mer synliga och andra svårare att fördela. Ärendetjänsten och dokumenttjänsten kan ha egna beräkningsresurser och databaser. Samtidigt delas kostnader för nätverk, övervakning, säkerhetsverktyg, reservkapacitet, utvecklingsmiljöer och incidentberedskap.

Det går att märka resurser och följa kostnader per tjänst, men alla gemensamma kostnader kan inte utan vidare fördelas rättvist efter processortid eller datamängd. En enkel och redovisad fördelningsprincip är ofta bättre än en komplicerad modell som ger falsk precision. Kostnadsfördelning bör också skiljas från beslutsrätt: den som får en intern kostnad påförd kan sakna möjlighet att påverka en gemensam plattformsutgift. Det viktiga är att synliggöra vad en tjänst faktiskt förbrukar, vilka gemensamma kostnader som behövs och vem som kan besluta om investeringar för att minska framtida risk.

Teknisk skuld hör hemma här. Ett team kan behöva uppgradera ett ramverk utan att någon ny funktion tillkommer. Plattformen kan behöva byta en komponent som snart saknar stöd. Om varje budget endast belönar synliga verksamhetsfunktioner blir nödvändigt underhåll ständigt uppskjutet. Långsiktig styrning behöver därför ge plats för både nytta, riskreducering och förvaltning.

## När flera delar fallerar samtidigt

Föreställ dig att användarna inte kan öppna dokument i sina ärenden. Dokumenttjänsten rapporterar timeout. Samtidigt har en gemensam nätverksförändring påverkat kommunikationen mellan tjänsterna. Vem äger incidenten?

Dokumentteamet bör kunna undersöka sina anrop och avgöra hur tjänsten påverkas. Plattform och drift bör kunna analysera nätverksförändringen och återställa förbindelsen. Men någon måste också hålla ihop prioritering, lägesbild, användarinformation och beslut om när den samlade verksamhetsfunktionen kan betraktas som återställd. Det är inte rimligt att kräva att användaren ska veta vilket team som först borde kontaktas.

Kapitel 14 beskrev incidenthanteringens praktiska förlopp. Styrningsfrågan här är att **mandatet måste vara bestämt innan incidenten inträffar**. Det bör vara klart vem som leder en större incident, vem som får fatta vilka produktionsbeslut, hur leverantörer kontaktas och hur en konflikt mellan lokal tjänsteoptimering och återställning av helheten löses. Incidentledaren behöver inte själv ha administratörsbehörighet eller ensam besluta om varje teknisk åtgärd.

Efter en incident behöver åtgärder som berör flera tjänster få en utsedd samordningsansvarig, namngivna utförare och ett datum för uppföljning. Åtgärderna behöver prioriteras i förvaltningsplaneringen. Annars kan alla team avsluta sin lokala uppgift medan den grundläggande samverkansbristen består.

## När utveckling och drift är olika organisationer

Det finns en förenklad bild av mikrotjänster där varje utvecklingsteam alltid sköter all drift. Så behöver det inte vara. En organisation med etablerad drift- eller infrastrukturkompetens kan välja att behålla separata funktioner. Men uppdelningen får inte betyda att applikationen lämnas över som en svart låda.

Applikationsteamet måste bidra med driftbar kod, diagnostik, tekniska beroenden, återställningsrutiner och förväntat beteende vid fel. Drift- och plattformsteamen måste tillhandahålla tydliga tjänster, förändringsinformation, incidentvägar och kunskap om infrastrukturen. De behöver också kunna återföra erfarenheter från produktion till utvecklingen. Gemensamma övningar och granskningar av verkliga störningar bygger ofta bättre samverkan än ännu ett organisationsschema.

Där leverantörer ingår måste avtalen och gränssnitten stödja denna samverkan. En leverantörs åtagande för en databas eller en driftplattform är inte automatiskt ett åtagande för hela ärendeprocessen. Organisationen som använder IT-stödet behöver fortfarande kunna bedöma och styra de samlade riskerna.

## Kompetens, dokumentation och kontinuitet i ansvaret

Självständighet kräver att teamen förstår sina tjänsters gränser och beroenden. En tjänstekatalog bör därför inte bara ange ett namn och en nätverksadress. Den behöver ange vem som förvaltar tjänsten, hur teamet nås vid incidenter, vilka kontrakt den erbjuder, vilka viktigare beroenden som finns och hur förändringar kommuniceras. Informationen måste hållas aktuell, helst i anslutning till det ordinarie leveransarbetet.

Tjänstekatalogen kan även behöva beskriva ansvar för data, integrationskonsumenter, versioner med återstående stödtid och var driftinstruktioner finns. Ägarskapsuppgifter som bara finns i en organisationsbild blir snabbt föråldrade.

Ett särskilt problem uppstår när team omorganiseras. Om dokumentteamet läggs ned eller byter uppdrag får dokumenttjänsten inte bli ägarlös. Det behövs regler för överlämning av kod, behörigheter, avtal, körmiljöer, larm och teknisk kunskap. Samma sak gäller om en extern leverantör byts ut.

Kompetensförsörjning omfattar därför mer än vilka tekniker organisationen kan rekrytera. Den handlar även om gemensam förståelse för hela verksamhetsflödet, övningar över organisationsgränser och tid avsatt för att lära av produktionen.

## Styrning som möjliggör helhetsansvar

I kapitel 3 beskrev vi de praktiska ansvarsgränserna mellan tjänst, plattform och IT-stöd. Här har vi i stället sett hur de gränserna måste **förvaltas, finansieras, följas upp och överlämnas** över tid. Vi kan sammanfatta skillnaden så här: i den traditionella modellen samlas många tekniska beslut inom en gemensam system- och driftstruktur. I en mikrotjänstlösning flyttas vissa beslut närmare tjänsteteamen, medan andra behöver lyftas till en gemensam nivå. Det är inte fråga om mindre styrning utan om **styrning på rätt nivå**.

För applikationsläsaren blir slutsatsen att ett tydligt tjänsteägarskap innebär mer än ansvar för kod och funktioner. För driftläsaren innebär det att plattformens och infrastrukturens tjänster måste beskrivas som begripliga åtaganden med gränssnitt och mandat. För båda gäller att någon behöver kunna svara för att användarna faktiskt kan hantera sina ärenden, oavsett hur många tekniska delar som krävs.

I nästa kapitel går vi från den långsiktiga ansvarsfördelningen till övergången i sig: hur en organisation kan leva med gammal och ny arkitektur samtidigt utan att tillfälliga lösningar blir permanenta.

### Källor och vidare läsning

- **[R21](https://martinfowler.com/articles/microservices.html)** James Lewis och Martin Fowler, Microservices (kontrollerad 2026-10-17).
