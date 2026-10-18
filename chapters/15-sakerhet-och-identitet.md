# 15. Hur skyddar vi systemet och dess information?

När det traditionella ärendehanteringssystemet ligger bakom en gemensam webbserver, i ett avgränsat nät och med en central databas, är det lätt att tänka på säkerhet som ett skydd runt systemet. Brandväggar, serverhärdning, användarinloggning och databasbehörigheter är fortfarande viktiga. Men när dokumenthanteringen och andra funktioner blir egna mikrotjänster uppstår fler kommunikationsvägar, fler tekniska identiteter och fler ställen där behörighetsbeslut fattas.

Det betyder inte att mikrotjänster per definition är osäkrare än en monolit. Skillnaden är att säkerhetsmodellen måste omfatta **relationerna mellan tjänsterna**, inte bara gränsen mellan användare och system. En intern anropare är inte automatiskt betrodd. En lyckad inloggning innebär inte heller att användaren får läsa varje dokument som en tjänst kan nå.

## Från en skyddad systemgräns till flera tillitsgränser

I vårt exempel loggar en handläggare in i ärendestödet och öppnar ett ärende med tillhörande dokument. Det grafiska gränssnittet kontaktar ärendetjänsten, som i sin tur kan hämta dokumentmetadata från dokumenttjänsten. Själva filen kan ligga i en lagringstjänst som administreras av plattformen.

Varje övergång innebär frågor: Vem gör anropet? Vilket ärende gäller det? Vilket tillstånd har ärendet? Har användaren rätt att se just detta dokument? Vilka tjänster ska kunna begära eller leverera filens innehåll? Och hur upptäcker vi ett otillåtet försök?

En ändamålsenlig utgångspunkt är att identifiera tillitsgränser och hot utifrån informationens skyddsvärde. Nätverkssegmentering kan minska vilka komponenter som når varandra, men den ersätter inte identitetskontroll och behörighetsprövning. Det gäller även trafik som aldrig lämnar det interna nätet. [R17](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)

## Autentisering är inte auktorisation

**Autentisering** handlar om att fastställa vem en användare eller tjänst är. **Auktorisation** handlar om vad den identifierade aktören får göra i det aktuella sammanhanget. De besluten behöver hållas isär.

Användaren kan autentiseras genom en gemensam identitetslösning. Det betyder inte att varje mikrotjänst behöver hantera användarens lösenord. I stället kan tjänsterna få verifierbara uppgifter om identitet och session genom en väl definierad säkerhetsarkitektur. Hur en token verifieras beror på dess typ och det använda säkerhetsprotokollet. En signerad JSON Web Token (JWT) behöver bland annat signaturkontroll; en ogenomskinlig token kan i stället behöva kontrolleras hos en behörig verifieringstjänst. Giltighetstid, utfärdare, avsedd mottagare och relevanta rättigheter ska prövas enligt säkerhetskontraktet. Dessa kontroller måste göras på rätt plats i anropskedjan; att en tidigare tjänst redan har validerat användaren räcker inte utan ett uttryckligt, säkrat tillitskontrakt. Tjänster ska inte godta en token enbart därför att den verkar vara internt utfärdad.

Behörighetsreglerna måste dessutom ta hänsyn till verksamhetens objekt. Dokumenttjänsten får inte lämna ut en fil bara för att den som gör anropet känner till dokumentets identifierare. Åtkomsten kan bero på ärendetillhörighet, användarens roll, sekretessmarkeringar och ärendets aktuella tillstånd. Här behövs överenskommelser mellan verksamhetsansvariga och de team som äger ärende- respektive dokumentinformation.

Om ärendetjänsten gör anropet å en användares vägnar behöver dokumenttjänsten få tillräckligt underlag för ett korrekt behörighetsbeslut. Det kan ske genom en uttryckligt avgränsad delegering eller genom ett betrott behörighetsbeslut som dokumenttjänsten kan kontrollera. Att okritiskt vidarebefordra en token avsedd för ärendetjänsten till dokumenttjänsten riskerar att bryta mot tokenens mottagarbegränsning. Att vidarebefordra användarkontext är dock inte samma sak som att ge alla interna tjänster samma obegränsade befogenheter. Kontraktet måste ange vem som får anropa, för vilket ändamål och hur rättigheter begränsas. [R18](https://www.rfc-editor.org/rfc/rfc8725.html)

## Tjänster behöver egna identiteter

När en monolit delas upp ökar antalet anrop mellan programkomponenter. Dokumenttjänsten kan behöva läsa från lagring, publicera ett meddelande och anropa en separat skanningstjänst. Dessa anrop bör utföras med identifierbara tjänsteidentiteter och med **minsta nödvändiga behörighet**.

En tjänsteidentitet är inte detsamma som en användares identitet. Den beskriver vilken applikationskomponent som utför ett tekniskt anrop. För vissa flöden behövs båda perspektiven: dokumenttjänsten autentiserar ärendetjänsten som teknisk klient och kontrollerar samtidigt vilken användare eller verksamhetsprocess anropet gäller.

Tekniska identiteter kan bygga på flera olika mekanismer, till exempel kortlivade autentiseringsuppgifter, certifikat eller signerade token. Ömsesidig TLS kan autentisera tjänster och skydda kommunikationen, men löser inte ensam frågan om vilka dokument en handläggare får se. Kryptering, identitet och behörighet är kompletterande skydd, inte utbytbara lösningar.

## Nätverk och kryptering i en distribuerad miljö

Drift- och nätverksorganisationen arbetar traditionellt med separata nät, brandväggsregler, lastbalanserare, DNS och certifikat. De förmågorna finns kvar. Skillnaden är att antalet tjänster och tillåtna kommunikationsrelationer kan förändras oftare. En statisk lista över serveradresser blir då svårare att underhålla än tydliga regler baserade på tjänsternas roller och behov.

Det behöver vara känt vilka anropsvägar som är avsedda: från webbläsare till ingångstjänst, från ärendetjänst till dokumenttjänst och från dokumenttjänst till lagringsresurs. En tjänst ska inte nå alla andra tjänster bara för att de delar samma kluster eller virtuella nät.

Kryptering under överföring skyddar mot insyn och manipulation på vägen, medan skydd av lagrad information hanterar andra risker. Nycklar, certifikat och förtroendekedjor måste kunna förnyas och roteras. Vid planerade byten kan en kontrollerad överlappning mellan gamla och nya uppgifter behövas. Vid misstänkt röjda uppgifter krävs däremot möjlighet till snabb spärr eller återkallelse enligt den valda mekanismen. Rotation och återkallelse ska provas mot beroende tjänster så att både skydd och driftpåverkan är kända. Valet av teknik och kontrollernas omfattning styrs av risk, miljö och organisationens krav, inte av att arkitekturen råkar vara uppdelad i mikrotjänster.

## Hemligheter, konfiguration och leveranskedjor

Lösenord till databaser, API-nycklar och privata nycklar får inte hårdkodas i källkod eller skickas med i en containeravbild. De bör förmedlas genom en kontrollerad mekanism med spårbar åtkomst, definierad livslängd och rutiner för rotation. Att en hemlighet ligger i en miljövariabel eller ett konfigurationslager gör den inte automatiskt säker; åtkomst till körmiljö, loggar och felsökningsverktyg spelar också roll.

Säkerhet behöver också omfatta **hur programvaran byggs och levereras**. Beroenden, byggverktyg, artefaktregister och automatiserade driftsättningar kan annars bli vägar in i produktionsmiljön. Teamen bör kunna se vilken källkod och vilka beroenden en levererad version bygger på, och vilka kontroller den passerat. Kodgranskning, sårbarhetshantering och separerade behörigheter är exempel på kontroller som kan minska riskerna.

Detta är ett gemensamt ansvar. Applikationsteamet väljer och underhåller sina beroenden och sin kod. Plattformen erbjuder skyddade bygg- och körmiljöer. Säkerhetsfunktionen hjälper till att fastställa risknivåer och kontrollkrav. Driftorganisationen bidrar med kontroll över produktionsåtkomst och övervakning av infrastrukturen. Ingen av dessa delar kan ensam garantera en säker leverans.

## Informationens skydd följer med över tjänstegränsen

I det genomgående exemplet kan ett dokument innehålla sekretessbelagda uppgifter även när dess metadata presenteras i ärendelistan. Därför behöver informationsklassning och åtkomstregler följas upp både i ärendetjänstens API och i dokumenttjänstens lagring och nedladdningsväg.

Ett vanligt misstag är att kontrollera åtkomst när en dokumentlänk skapas men inte när filen faktiskt hämtas. Om nedladdning sker via en tidsbegränsad, signerad länk behöver länken ha snäv giltighet och omfattning, och organisationen måste ta ställning till hur återkallelse, vidarebefordran och loggning hanteras. En signerad länk ger inte i sig en ny prövning av användarens aktuella behörighet. En annan risk är att ett meddelande eller en loggrad innehåller mer information än mottagaren behöver. Genom att minimera uppgifter i meddelanden, loggar och tekniska spår minskar den sammanlagda exponeringen.

Även tillfälliga filer, säkerhetskopior och testmiljöer behöver ingå i skyddsmodellen. Det räcker inte att den primära databasen har rätt behörigheter om samma information finns i en oskyddad export eller i en felsökningslogg.

## Hotmodellering och säkerhetstester

När ett nytt kommunikationsflöde införs bör teamen identifiera vad som kan gå fel. Hur skulle en obehörig tjänst försöka läsa ett dokument? Kan en handläggare byta ett dokument-ID i en begäran och därmed nå ett annat ärendes fil? Vad händer om en token stjäls eller en intern komponent får mer behörighet än den behöver?

Sådana frågor är exempel på hotmodellering. Arbetet kan genomföras i olika former, men behöver anknyta till verkliga dataflöden och tillitsgränser. Säkerhetstester bör omfatta både nekad åtkomst, otillåten åtkomst mellan verksamhetsobjekt och felaktiga tjänsteidentiteter. Det är viktigt att verifiera att systemet avvisar förbjudna åtgärder, inte bara att vanliga användarflöden fungerar.

Automatiska tester hjälper, men ersätter inte granskning av arkitektur och driftkonfiguration. En felaktig nätverkspolicy eller överdriven produktionsbehörighet kan ligga utanför applikationens testsvit. Därför behöver provning ske på flera nivåer.

## Säkerhetshändelser och incidenthantering

Om dokumenttjänsten upptäcker upprepade obehöriga nedladdningsförsök behövs loggar som visar förloppet utan att själva exponera innehållet. Säkerhetsrelevanta loggar behöver skyddas mot obehörig ändring, få ändamålsenlig åtkomst- och gallringsstyrning och kunna korreleras över tjänstegränser. Säkerhetsfunktion och driftorganisation kan behöva samordna isolering av en identitet eller en tjänst, medan applikationsteamet analyserar om en behörighetsregel kan kringgås.

Säkerhetsincidenter kräver ibland andra prioriteringar än vanliga driftsstörningar: att omedelbart återställa tillgänglighet är inte alltid rätt första steg om det riskerar att förstöra bevis eller förvärra informationsläckage. Incidentmandat, rapporteringsvägar och ansvar för tekniska åtgärder behöver därför vara överenskomna i förväg. De generella arbetsformerna för samordnade incidenter behandlades i kapitel 14.

## Vem ansvarar för säkerheten i helheten?

Säkerhet i ett distribuerat system blir svag om varje team antar att någon annan ansvarar för gränsen mellan tjänsterna. Ansvarsfördelningen bör därför beskriva både kravställning, genomförande och verifiering.

**Verksamhets- och informationsansvariga** avgör vilken information som är skyddsvärd och vilka åtkomstvillkor verksamheten kräver. **Applikationsteamen** inför kontroller i kod och API:er och säkerställer att behörighet prövas vid relevanta operationer. **Plattforms- och driftfunktioner** tillhandahåller och övervakar nät, identitetsmekanismer för tjänster, hemlighetshantering och säkra körmiljöer. **Säkerhetsfunktionen** stödjer riskanalys, gemensamma principer, oberoende uppföljning och hantering av avvikelser.

Organisationer kan fördela dessa uppgifter på olika sätt. Det avgörande är att beslut om exempelvis tokenvalidering, dokumentbehörighet, certifikatsrotation och loggåtkomst har uttryckliga ägare. För varje kritiskt skydd bör det också vara tydligt vem som verifierar att kontrollen faktiskt fungerar.

## En gemensam säkerhetsmodell, inte en gemensam superbehörighet

När dokumenttjänsten bryts ut ur monoliten kan det vara lockande att ge ärendetjänsten obegränsad åtkomst till alla dokument för att förenkla integrationen. Det skulle minska friktionen på kort sikt men också utöka konsekvensen av ett intrång eller ett programmeringsfel.

En hållbar lösning beskriver i stället vem som får begära vad, hur ett behörighetsbeslut fattas, hur kommunikationen skyddas och hur ett fel upptäcks. Gemensamma plattformsförmågor kan förenkla det arbetet, men ersätter inte verksamhetens regler för informationen.

Det är den centrala förändringen från monolit till mikrotjänster: säkerhet måste fortfarande fungera som en helhet, samtidigt som varje tjänst bär ett tydligt ansvar för sin del av skyddet.

### Källor och vidare läsning

- **[R17](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)** OWASP, API1:2023 Broken Object Level Authorization (kontrollerad 2026-10-17).
- **[R18](https://www.rfc-editor.org/rfc/rfc8725.html)** IETF, RFC 8725 JSON Web Token Best Current Practices (kontrollerad 2026-10-17).
