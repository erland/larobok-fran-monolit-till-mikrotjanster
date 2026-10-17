# 13. Hur vet vi att hela IT-stödet fungerar?

Alla servrar visar grönt. Ändå kan användarna inte bifoga dokument till sina ärenden. Det är ett scenario som visar varför teknisk övervakning behöver kompletteras med förståelse för verksamhetsflöden. I en distribuerad arkitektur kan varje tjänst fungera tekniskt medan samspelet mellan dem misslyckas.

## Från komponentstatus till verksamhetsfunktion

I ett traditionellt system övervakas ofta webbserver, backend, databas och nätverk. Sådana signaler behövs fortfarande. Men när ärendehantering, dokumenthantering och notifiering blir separata tjänster måste organisationen kunna skilja mellan att en process körs, att en tjänst behandlar anrop korrekt och att användaren faktiskt kan fullfölja sin arbetsuppgift.

I vårt ärendehanteringssystem vill användaren bifoga en fil. Ärendetjänsten registrerar begäran, dokumenttjänsten lagrar filen och en senare händelse uppdaterar ärendets dokumentlista. Alla komponenterna kan rapportera normal status även om uppdateringen är fördröjd och användaren inte kan se sitt dokument. Ett relevant mått på funktionen behöver därför omfatta hela förloppet – inte bara om dess enskilda delar svarar. Det ska dessutom skilja mellan en uppladdning som fortfarande behandlas, en som misslyckats och en som slutförts.

Det är viktigt att inte överdriva skillnaden mot monoliter. Även ett traditionellt system kan behöva övervakning av användarflöden. Mikrotjänster gör behovet mer påtagligt genom fler nätverksberoenden, fler körande instanser och självständiga förändringar.

## Loggar, mätvärden och distribuerade spår

Tre typer av signaler kompletterar varandra. **Mätvärden** visar exempelvis antal begäranden, felandel, svarstid och ködjup över tid. **Loggar** beskriver enskilda händelser, såsom avvisad uppladdning eller misslyckad databasoperation. **Distribuerade spår** följer delar av en begäran när den passerar mellan olika tjänster.

Ett mätvärde kan visa att registreringstiden ökar. Medelvärden kan samtidigt dölja långa väntetider för en mindre grupp användare; därför kan också fördelningar och höga percentiler behövas. ett spår visa att merparten av tiden tillbringas i dokumenttjänstens lagringsanrop och en logg att ett enskilt försök tidsbegränsades. Inget av verktygen ger ensamt hela förklaringen.

För applikationssidan innebär detta att instrumenteringen behöver byggas in i tjänsterna. Strukturerade loggar och konsekventa felkoder ska förklara vad tjänsten försökte göra. För driftsidan innebär det att gemensamma system måste kunna samla in, söka och relatera signaler från tjänster som byter instans och adress över tid. [R15](https://opentelemetry.io/docs/concepts/context-propagation/)

## Korrelation mellan tjänster

När en begäran passerar från ärendetjänsten till dokumenttjänsten behöver det finnas ett sätt att koppla samman händelserna. Ett korrelations-ID eller en distribuerad spårkontext kan föras vidare i kommunikationen. Vid asynkrona meddelanden behövs ibland samband mellan ursprunglig begäran och senare arbete, snarare än en enda sammanhängande kedja. Om ett meddelande behandlas flera gånger ska detta kunna följas utan att varje försök felaktigt räknas som en ny verksamhetsoperation.

Detta måste utformas gemensamt. Om varje team hittar på egna fältnamn och identifierare blir felsökning över tjänstegränser besvärlig. Samtidigt ska spårbarhet inte uppnås genom att personuppgifter, dokumentinnehåll eller autentiseringstoken rutinmässigt lagras i loggar.

## Vad är ett fungerande ärendeflöde?

En tjänstenivåindikator (SLI) beskriver något som går att mäta, exempelvis andelen lyckade dokumentuppladdningar eller tiden från uppladdning till synlig dokumentpost. Ett tjänstenivåmål (SLO) anger vilken nivå man eftersträvar under en bestämd period. Ett SLO är inte automatiskt ett avtalsmässigt åtagande (SLA). För ett asynkront flöde kan ett mottagningskvitto vara tekniskt lyckat trots att verksamhetsåtgärden ännu inte är genomförd; båda tillstånden behöver kunna observeras.

Definitionen behöver utgå från verksamheten. Räknas en uppladdning som lyckad när dokumenttjänsten tar emot filen, när den lagrats eller först när användaren ser den i ärendet? Om vi väljer fel definition kan övervakningen visa ett gott resultat samtidigt som användarna upplever återkommande problem.

Alla funktioner behöver inte ha samma mål. För vissa ärendeflöden måste resultat synas omedelbart. För andra kan en fördröjd notifiering vara acceptabel. Verksamhetsansvariga behöver bidra med prioriteringar, medan applikations- och driftansvariga översätter dem till mätbara indikatorer och genomförbara kontroller.

## Syntetiska tester och verkliga användarsignaler

En syntetisk kontroll kan med jämna mellanrum prova ett viktigt arbetsflöde: skapa ett testärende, bifoga en ofarlig fil och kontrollera att den visas. Det gör det möjligt att upptäcka fel som serverövervakningen missar. Testdata behöver dock vara tydligt märkta, begränsade och rensas bort så att kontrollerna inte förorenar den verkliga verksamheten.

Signaler från verkliga användare kan visa hur ofta ett flöde misslyckas och hur länge de får vänta. De måste tolkas med hänsyn till klienter och nätverksförhållanden och hanteras med lämpligt integritetsskydd. Syntetiska och verkliga signaler kompletterar därför varandra.

## När gröna tjänster ger en röd helhet

Anta att dokumenttjänsten tar emot uppladdningar men att kön för efterföljande registrering växer. Ärendetjänsten visar att den får svar och dokumenttjänsten rapporterar att den är igång. Användarna ser ändå inte de uppladdade filerna inom utlovad tid.

Ett övergripande mått på genomförda dokumentregistreringar visar problemet. Kömått visar eftersläpningen, medan spår och loggar hjälper teamen att förstå varför. Applikationsteamet behöver analysera arbetsflödets logik och hur fel eller fördröjningar hanteras. Plattform och drift behöver undersöka resurser, lagring, kommunikation och köernas beteende. Ingen av grupperna kan ersätta den andras kunskap.

Observerbarheten löser inte störningen i sig, men kan göra den upptäckbar och begriplig innan den växer till en större incident.

## Färre men bättre larm

Fler mikrotjänster kan innebära mängder av mätvärden och larm. Om varje tillfällig omstart utlöser ett akut larm riskerar driftorganisationen att drunkna i signaler. Larm bör därför prioriteras efter faktisk eller förväntad påverkan på verksamhetsflöden och efter om någon behöver agera.

Ett användbart larm anger vad som försämrats, vilket mål som hotas, vem som ska ta emot det och vilka första kontroller som är relevanta. Förebyggande tekniska larm kan vara motiverade innan användare hunnit påverkas, men bör ha begripliga åtgärdströsklar och en tydlig mottagare. Tekniska larm är fortfarande nödvändiga, men de behöver relateras till tjänstens och verksamhetens betydelse. Hur larm eskaleras och hur incidenter leds behandlas i nästa kapitel.

## Observerbarhet har också en kostnad och en risk

Att samla allt är inte ett mål i sig. Hög loggvolym, långt bevarande och omfattande spårning kan bli kostsamt. Det kan också skapa säkerhets- och integritetsproblem. Samplingsbeslut bör beakta att sällsynta men allvarliga fel annars riskerar att missas. För kritiska händelser kan separata och mer fullständiga signaler behövas. Organisationen behöver därför besluta vad som är nödvändigt, hur länge det lagras, vilka som får läsa uppgifterna och vad som kan reduceras eller samplas utan att viktiga fel blir osynliga.

Även observabilitetsplattformen kan få störningar. Dess fel bör så långt möjligt inte stoppa verksamhetsfunktionerna, och kritiska larm kan behöva alternativa vägar.

## Vem ansvarar för helhetsbilden?

En möjlig ansvarsfördelning är att tjänsteteamen ansvarar för verksamhetsrelevanta signaler och korrekt instrumentering, att plattformsteamet erbjuder insamling, sökning, lagring och behörighetsstyrning, och att ansvarig för det samlade IT-stödet säkerställer att kritiska användarflöden faktiskt går att följa upp. Driftorganisationen tillför kunskap om underliggande resurser och gemensamma beroenden. Säkerhets- och informationsansvariga anger ramar för känsliga uppgifter.

Det viktiga är inte att placera samtliga uppgifter i en viss organisation, utan att göra varje gränssnitt explicit: vem definierar ett mått, vem implementerar det, vem larmas, vem får ändra larmregler, vem hanterar insamlingsplattformens egna avbrott och vem följer upp att verksamhetsmålet nås?

För **applikationsläsaren** är lärdomen att driftbarhet och synligt beteende måste vara en del av tjänstens design. För **driftläsaren** är lärdomen att status för VM:ar och processer behöver kompletteras med signaler från de faktiska verksamhetsflödena. För båda är den avgörande frågan densamma: kan vi tillsammans avgöra om användarna får den funktion de behöver? **Observerbarheten hjälper oss att upptäcka och avgränsa påverkan**, men är inte samma sak som de felbegränsande mekanismerna i kapitel 12 eller den samordnade incidenthanteringen i kapitel 14. Den övergången är viktig: ett larm blir värdefullt först när någon kan bedöma det och vid behov agera.

### Källor och vidare läsning

- **[R15](https://opentelemetry.io/docs/concepts/context-propagation/)** OpenTelemetry, Context propagation (kontrollerad 2026-10-17).
