# 3. Vem ansvarar för vad när systemet blir distribuerat?

En användare försöker öppna ett dokument i ett ärende. Ärendet visas, men dokumentet går inte att hämta. I går fungerade allt. Användaren anmäler ett fel i ärendehanteringssystemet. För verksamheten finns fortfarande ett IT-stöd som ska fungera. För den tekniska organisationen kan felet nu finnas i ärendetjänsten, dokumenttjänsten, en nätverkspolicy, ett identitetssystem eller en gemensam plattform.

Det som tidigare kunde hanteras som ett fel inom en sammanhållen applikation har blivit en fråga om samverkan mellan flera självständiga delar. Men vem ska egentligen lösa problemet? Det korta svaret är att ansvaret behöver beskrivas på flera nivåer. Ingen av dessa nivåer kan ensam ersätta helhetsansvaret.

## Helheten finns kvar även när applikationen delas upp

I vårt fiktiva ärendehanteringssystem fanns från början en frontend, en backend och en gemensam databas. Driftorganisationen förvaltade exempelvis VM:ar, nätverk och databasmiljöer, medan applikationsgruppen utvecklade och förändrade funktionerna. Systemägaren kunde begära åtgärder för hela IT-stödet och leveranserna samordnades vanligtvis inom en gemensam release.

Organisationen behövde redan då samarbeta över kompetensgränserna. En monolit innebär inte att alla beslut fattas av en person, och en central driftfunktion har aldrig ensam garanterat att en applikation fungerar. Men när många funktioner ingår i samma körbara applikation och samma release finns ofta färre tekniska gränssnitt mellan de delar som ska ändras och felsökas.

När dokumenthanteringen bryts ut uppstår två tekniklivscykler. Dokumenttjänsten kan uppdateras utan att ärendetjänsten uppdateras. Den kan ha egna data, driftsättningsrutiner, resurskrav och övervakningssignaler. Detta kan minska behovet av gemensamma releaser. Samtidigt måste tjänsterna fortfarande samverka för att användaren ska kunna arbeta.

**En teknisk ansvarsfördelning kan därför bli mer detaljerad utan att ansvaret för verksamhetsresultatet får bli otydligare.** Även om tjänsterna förvaltas av olika team behöver en utsedd funktion kunna samordna prioriteringar och återställning för IT-stödet som helhet.

## Fyra nivåer av ansvar

Ett användbart första steg är att skilja på fyra ansvarsnivåer. De kan organiseras på olika sätt och behöver inte motsvara fyra separata team. Ansvarsnivåerna är inte en rangordning: verksamhetsansvar, tekniskt genomförande och oberoende kontroll kan ligga i olika organisatoriska delar.

### Ansvar för verksamhetens IT-stöd

Någon behöver företräda verksamhetens krav på den samlade funktionen: att ärenden kan registreras, dokument öppnas, beslut fattas och information bevaras enligt tillämpliga krav. Den rollen behöver kunna prioritera risker och åtgärder även när problemen sträcker sig över flera tjänster.

Helhetsansvaret omfattar inte nödvändigtvis drift av varje komponent. Det innebär däremot att ingen användare ska behöva förstå mikrotjänstgränserna för att få hjälp eller veta var ett verksamhetskritiskt fel ska anmälas.

### Ansvar för en mikrotjänst

Ett tjänsteteam kan få ansvar för dokumenttjänstens funktion och livscykel: kod, gränssnitt, datamodell, beroenden, releaser, driftbarhet och felrättning. För att ägarskapet ska fungera behöver teamet känna till tjänstens prestandakrav, åtkomstbehov och hur den påverkar andra tjänster.

Det betyder inte nödvändigtvis att utvecklarna ska administrera servrar, databasmotorer eller brandväggar, eller ens att tjänsteteamet bemannar jour dygnet runt. Sådant måste avgöras genom en uttrycklig drift- och beredskapsmodell. Men de kan inte betrakta sådana frågor som helt frikopplade från tjänstens funktion. Om tjänsten måste kunna anropa ett dokumentlager måste behovet beskrivas så att infrastrukturen kan tillhandahålla och verifiera kommunikationen.

### Ansvar för plattform och gemensam drift

Plattforms- och driftfunktioner kan tillhandahålla exekveringsmiljöer, nätverk, databastjänster, certifikathantering, loggplattformar, backupmekanismer och automatiserade leveransvägar. Plattformen bör erbjuda tydliga tjänster med dokumenterade gränssnitt och förutsättningar, snarare än enbart en lista över maskiner som någon annan får använda.

Även här finns flera möjliga modeller. En organisation kan ha en central driftavdelning som också är plattformsteam, eller en separat plattformsfunktion som samverkar med nätverks-, databas- och säkerhetsspecialister. Det väsentliga är att ansvar och eskalering framgår.

### Ansvar för gemensamma säkerhets- och informationskrav

Säkerhet, regelefterlevnad, informationsklassning och identitetshantering korsar tjänstegränserna. En central funktion kan sätta krav på exempelvis nätverkssegmentering och autentisering, medan plattformen genomdriver tekniska kontroller och tjänsteteamet implementerar tillämpningsspecifika behörighetsregler. Ingen bör anta att ett godkänt nätverksflöde automatiskt innebär att en användare har rätt att läsa ett dokument.

## Fem frågor som avslöjar otydligt ansvar

Det är lätt att säga att ett team ”äger” en tjänst. Svårare är att veta vad ägarskapet innebär när något ska ändras eller slutar fungera. För varje viktig förmåga behöver man kunna besvara fem olika frågor:

1. **Vem ställer kraven?** Exempelvis vem avgör tillgänglighetsnivå och skyddsbehov för dokumenthanteringen?
2. **Vem fattar beslut?** Vem har mandat att godkänna en ny integrationsväg eller en ändring som påverkar andra tjänster?
3. **Vem genomför förändringen?** Vem ändrar kod, konfiguration, brandväggsregel eller databasinställning?
4. **Vem driver och återställer?** Vem reagerar på larm, leder åtgärder och återställer funktionen utanför kontorstid?
5. **Vem verifierar och följer upp?** Vem kontrollerar att kraven faktiskt uppfylls efter ändringen?

I praktiken behövs även en tydlig väg för eskalering när flera team berörs eller ingen uppenbart äger orsaken till ett fel. Under en incident bör det vara klart vem som leder arbetet och vem som beslutar om riskfyllda tillfälliga åtgärder.

Samma grupp kan besvara flera frågor, men inte alltid alla. Att skilja dem åt hjälper oss att undvika två vanliga misstag: att ansvaret blir oklart mellan teamen, eller att ett team förväntas bära ansvar utan att ha tillräckliga mandat och verktyg.

## Fallet: Dokumenttjänsten kan inte nås

Anta att dokumenttjänsten har fått en ny adress efter en driftsättning och att trafikregler eller tjänsteupptäckt inte har uppdaterats korrekt. Ärendetjänstens anrop misslyckas. I loggarna syns timeout, medan nätverksplattformen visar nekad trafik. Det är ett möjligt felscenario, inte en generell följd av att en tjänst byter adress. Användaren ser bara att dokumentet inte öppnas.

Den som tar emot användarens felanmälan bör kunna skapa ett sammanhållet ärende och inleda felsökning. Applikationsteamet behöver kunna avgöra vilket anrop som misslyckas och vilka krav som finns på destination och behörighet. Plattformen eller nätverksfunktionen behöver kunna visa hur trafiken dirigeras och vilka regler som gäller. Om en regel behöver ändras måste någon ha mandat att beställa, granska och genomföra ändringen. Till sist behöver någon verifiera att hela användarflödet fungerar igen – inte bara att båda tjänsternas processer är igång.

Om övervakningen endast säger att ärendetjänsten och dokumenttjänsten var för sig är ”gröna” kan felet ändå ligga kvar. Därför behöver ansvar för verksamhetsflöden och tjänstebaserad observerbarhet mötas. Senare kapitel fördjupar de tekniska metoderna för detta.

| Fråga i händelsen | Exempel på primärt ansvar | Samverkan som krävs |
|---|---|---|
| Upptäcka att dokument inte går att öppna | Helhetsövervakning eller support | Tjänsteteam och drift |
| Identifiera misslyckade anrop | Berörda tjänsteteam | Gemensam logg- och spårningsplattform |
| Granska trafikregler | Nätverks-/plattformsteam | Tjänsteteam och säkerhet |
| Bedöma konsekvensen för verksamheten | Ansvarig för IT-stödet | Incidentledning och verksamhet |
| Verifiera återställd funktion | Utsedd incident- och tjänsteansvarig | Alla berörda team |

Tabellen är ett exempel, inte en generell organisationsmall. I en annan organisation kan vissa av uppgifterna utföras av samma team eller en extern leverantör.

## Ansvar som förflyttas – och ansvar som delas

Med automatisering kan en del arbetsmoment flyttas närmare tjänsteteamet. Ett team kan exempelvis själv beställa en testmiljö genom ett godkänt gränssnitt, konfigurera resursgränser eller deklarera vilka tjänster det behöver kommunicera med. Plattformen kan verkställa önskemålen inom centralt beslutade ramar.

Det betyder inte att ansvaret för säkerhet och drift alltid ”flyttar till utvecklarna”. Ofta förändras snarare fördelningen mellan att **ange ett behov**, **tillhandahålla en gemensam förmåga** och **säkerställa att behovet uppfylls**. Automatisering ändrar hur arbetet utförs, men den tar inte bort behovet av ägarskap eller kontroll.

Samma resonemang gäller databaser. Ett tjänsteteam kan ansvara för informationsmodell och schemaändringar medan DBA- eller plattformsteam ansvarar för databasmotor, prestandakapacitet, backupmekanismer och grundläggande säkerhetskonfiguration. Återställning måste sedan provas mot tjänstens faktiska beteende. Ett lyckat databasjobb är inte automatiskt en återställd verksamhetsfunktion.

## Två perspektiv på samma gränssnitt

För läsaren från applikationssidan blir den viktigaste förändringen att ansvaret för en funktion inte slutar där koden slutar. Hur tjänsten kommunicerar, kan övervakas och kan återhämta sig är också en del av dess utformning. Det innebär ett tätare samarbete med infrastrukturen, men inte nödvändigtvis att varje utvecklare behöver vara specialist på nätverk eller operativsystem.

För läsaren från driftsidan blir den viktiga förändringen att driftens objekt kan bli fler, mer föränderliga och mer beroende av applikationens logik. Man behöver förstå tjänsternas kritiska relationer, inte bara deras VM:ar och databaser. Samtidigt kan välbyggda plattformsförmågor ge större kontroll genom gemensamma policyer, standardiserade driftsättningar och bättre spårbarhet.

Båda sidor behöver ett gemensamt språk för beroenden, servicekrav, incidenter och förändringar. En överenskommelse om vem som gör vad är användbar först när den också omfattar mandat, tillgång till relevant information och praktiska vägar till hjälp.

## Helhetsansvar får inte bli ett tomrum

Ett distribuerat IT-stöd kan ha tydliga ägare för samtliga mikrotjänster och ändå sakna någon som kan prioritera ett fel i den samlade användarupplevelsen. Det kan också ha stark central styrning men så många godkännandeled att varje liten förändring tar onödigt lång tid. Oberoende leveranser förutsätter därför inte att all styrning avskaffas, utan att beslut kan tas inom tydliga mandat och verifierbara ramar. Båda ytterligheterna är problematiska.

En fungerande ansvarsfördelning behöver därför förena lokal handlingsförmåga med ett uttryckligt ansvar för helheten. Tjänsteteam ska kunna fatta beslut inom sina gränser. Gemensamma funktioner ska kunna ange och genomdriva de ramar som behövs. Verksamheten ska fortfarande kunna kräva en fungerande tjänst, oavsett hur många tekniska delar som samverkar.

Här handlar ansvar främst om **vem som gör vad när ett distribuerat IT-stöd byggs, ändras eller får problem**. I kapitel 18 flyttar vi perspektivet till **hur organisationen håller ansvar och mandat fungerande över flera år** – genom styrning, finansiering, uppföljning och överlämningar. Först behöver vi förstå hur valet av tjänstegränser faktiskt påverkar både applikation och drift.

## Vad förändras för vem?

**För applikationssidan:** Tjänsteansvar omfattar också driftbarhet, integrationskontrakt, beroenden och möjligheten att felsöka ett användarflöde.

**För driftsidan:** Det blir viktigare att tillhandahålla begripliga plattformsförmågor och insyn i dynamiska beroenden än att enbart administrera en fast uppsättning maskiner.

**För helheten:** Någon måste fortfarande kunna prioritera, samordna och följa upp verksamhetsfunktioner som spänner över flera tjänster. Ansvar delas upp, men får inte lämnas odefinierat. [R2](https://martinfowler.com/articles/microservices.html)

### Källor och vidare läsning

- **[R2](https://martinfowler.com/articles/microservices.html)** James Lewis och Martin Fowler, *Microservices* (2014).
