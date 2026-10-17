# 6. Hur kommunicerar tjänsterna?

När ärendehanteringen och dokumenthanteringen låg i samma backend kunde de dela programkod, anropa varandras funktioner och använda samma databas. När dokumenthanteringen blir en självständig tjänst förändras något grundläggande: även en till synes enkel fråga om ett dokument måste nu passera en gräns där nätverk, kontrakt, säkerhet och driftförutsättningar spelar roll.

Föreställ dig att en handläggare öppnar ett ärende. Ärendetjänsten behöver visa en lista över dokument. I testmiljön fungerar allt, men i produktionen visas inga dokument. Ett tomt resultat får inte förväxlas med ett lyckat API-svar: gränssnittet behöver tydligt skilja mellan att ärendet saknar dokument och att hämtningen har misslyckats. Loggarna visar att ärendetjänsten försöker nå dokumenttjänsten – och får timeout. Är felet i programmet, DNS, lastbalanseringen, en brandvägg, tjänstens hälsa eller i en behörighetskontroll? Och vem ska avgöra det?

Det här kapitlet handlar om hur **tjänsternas kommunikation blir både en arkitekturfråga och en driftfråga**. Val av API eller händelseflöde kan inte göras isolerat från trafikväg, säkerhetsgränser och möjligheten att felsöka helheten.

## Från interna anrop till kontrakt över nätverk

Ett internt metodanrop i en monolit sker ofta inom samma process och kan dela minne och datatyper. Ett anrop till en annan tjänst behöver däremot ett uttryckligt kontrakt: adress, protokoll, meddelandeformat, identitet och hur olika svar ska tolkas. Även om tjänsterna körs på samma fysiska värd måste man tänka på att mottagaren kan startas om, bytas ut eller vara otillgänglig när anropet görs.

Kontraktet är inte bara en teknisk specifikation. Det är en överenskommelse mellan parter som kan utvecklas och driftsättas vid olika tidpunkter. Dokumenttjänsten måste exempelvis kunna ändra sin interna implementation utan att ärendetjänsten går sönder. Därför behöver kontrakten vara stabila, dokumenterade, testbara och utvecklas med medvetenhet om befintliga konsumenter.

Det är lätt att göra misstaget att ersätta interna funktionsanrop med många täta fjärranrop. Om en enda skärmbild kräver en lång kedja av små anrop blir användarupplevelsen känslig för fördröjning och partiella fel. Tjänstegränser bör därför också bedömas utifrån hur ofta och på vilket sätt tjänsterna behöver kommunicera.

## Synkrona anrop när svar behövs direkt

Ett synkront API-anrop passar när ärendetjänsten behöver ett svar för att kunna visa aktuella dokumentmetadata. Ofta används HTTP med ett tydligt definierat gränssnitt. Avsändaren måste veta när den ska sluta vänta och vad som ska hända om svaret uteblir.

Här behöver vi skilja mellan olika fel. Ett nekande svar på grund av saknad behörighet betyder något annat än att tjänsten är överbelastad. Ett timeout-fel betyder inte nödvändigtvis att mottagaren inte utförde åtgärden; svaret kan ha försvunnit på vägen tillbaka. Därför är det riskabelt att automatiskt försöka igen, särskilt för operationer som skapar eller ändrar information. Säker återupprepning kan kräva idempotens, till exempel ett unikt operations-ID som mottagaren kan känna igen.

Även läsanrop behöver välavvägda tidsgränser. Om ärendetjänsten väntar länge på dokumenttjänsten kan dess egna resurser bindas upp och antalet väntande förfrågningar växa. Överbelastning kan då spridas mellan tjänster. Hur sådana fel begränsas fördjupas i kapitel 12; här är poängen att kommunikationsmönstret måste ge utrymme för dem.

## Asynkron kommunikation när arbetet kan ske senare

Alla behov kräver inte ett omedelbart svar. När ett dokument har registrerats kanske andra delar av systemet ska bygga ett sökindex eller skicka en notifiering. Ett meddelande eller en händelse kan göra det möjligt att utföra arbetet senare, utan att den som registrerar dokumentet måste vänta.

Asynkron kommunikation tar inte bort beroenden. Den förändrar dem. Nu måste någon ansvara för köer eller meddelandetjänster, kvarvarande meddelanden, omleverans, felhantering och hur konsumenter hanterar äldre meddelandeformat. En avsändare behöver också förstå vilken garanti transporten erbjuder: ett meddelande kan exempelvis levereras mer än en gång, och ordningen kan variera mellan mottagare eller partitioner. Mottagaren måste kunna hantera sådana situationer.

En händelse om att ett dokument har registrerats säger inte automatiskt att alla mottagare har hunnit uppdatera sina vyer. Fördröjningen kan vara acceptabel, men den ska vara ett medvetet verksamhetsbeslut. Informationskonsistens och transaktionsgränser behandlas vidare i kapitel 7. [R6](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication)

## Vägen från tjänst till tjänst

I en traditionell miljö har applikationen ofta ett begränsat antal kända nätverksförbindelser: användare till frontend, frontend till backend och backend till databasen. Dessa kan avspeglas i relativt statiska brandväggsregler och lastbalanseringskonfigurationer.

När fler tjänster samverkar tillkommer fler trafikflöden. De är inte alltid synliga genom att man bara studerar vilka VM:ar som finns. Tjänster kan ha flera instanser som byts ut eller flyttas, samtidigt som deras logiska adresser behöver vara stabila. Därför behöver man skilja mellan **tjänstens namn**, **dess aktuella nätverksändpunkter** och **de nätverksregler som tillåter kommunikationen**.

DNS och tjänsteupptäckt kan hjälpa en klient att hitta rätt mottagare. En lastbalanserare eller annan trafikfunktion kan fördela förfrågningar mellan flera instanser. Vid inkommande användartrafik kan det finnas en ingress eller API-gateway som är en gemensam ingång. Intern kommunikation mellan tjänster kan följa andra vägar. Det finns inte ett enda obligatoriskt mönster; valet beror på plattform, trafik, säkerhet och komplexitet.

Lastbalansering ger inte automatiskt hög tillgänglighet. Om samtliga instanser är beroende av samma trasiga databas eller om trafikstyrningen själv blir en felpunkt kan tjänsten ändå vara nere. Det krävs också rimliga hälsosignaler och kapacitet för att återstående instanser ska klara belastningen. [R6](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication)

## Brandväggar och zoner finns kvar – men gränserna kan förändras

Ett vanligt missförstånd är att brandväggar blir irrelevanta när tjänster körs i containrar. Tvärtom måste organisationen fortfarande bestämma vilka flöden som är tillåtna. Men reglerna kan behöva knytas till logiska tjänster och deras identiteter eller etiketter, snarare än enbart till långlivade serveradresser. Identitetsbaserad åtkomstkontroll kompletterar, men ersätter inte alltid, nätverkssegmentering.

Tänk att ärendetjänsten behöver nå dokumenttjänstens API, men inte direkt dess datalager. En princip om minsta nödvändiga åtkomst innebär då att endast den avsedda trafikvägen ska tillåtas. Det kan uppnås med traditionella brandväggar, nätverkspolicyer på en plattform eller en kombination. Hur reglerna realiseras är inte samma sak som vem som fastställer säkerhetskraven.

Nätverkszoner kan fortsatt vara viktiga, exempelvis för att skilja produktion från test eller särskilt skyddsvärda system från andra resurser. En del organisationer väljer dessutom finmaskig segmentering mellan tjänster inom en zon. Att en tjänst körs i en separat container eller namnrymd bevisar dock inte i sig att nätverket är säkert isolerat.

En praktisk förändring uppstår när applikationsteamet behöver ändra trafikflödet ofta. Det är sällan hållbart att för varje ny tjänsteinstans beställa en manuell regel för en ny IP-adress. I stället kan applikationsteamet beskriva vilket flöde som behövs, en gemensam plattform omsätta beskrivningen till regler och nätverks- eller säkerhetsfunktionen fastställa vilka förbindelser som över huvud taget får öppnas. Denna ansvarsfördelning är ett alternativ, inte ett krav som följer av mikrotjänster.

## Kryptering och identitet längs trafikvägen

Trafik mellan tjänster kan behöva skyddas med TLS, och i vissa miljöer används ömsesidig TLS för att också styrka den anropande tjänstens identitet. Certifikat behöver utfärdas, förnyas och spärras på ett kontrollerat sätt. Automatisering kan minska manuella fel, men skapar samtidigt krav på säkra rutiner för nycklar och tillit.

En krypterad förbindelse säger inte att den anropande tjänsten får utföra varje åtgärd. Nätverksåtkomst, autentisering och auktorisation är olika kontroller som samverkar. Vem användaren är, hur en tjänst styrker sin identitet och hur beslut om rättigheter fattas behandlas mer utförligt i kapitel 15.

## När kommunikationen inte fungerar – vem felsöker?

Återvänd till produktionsproblemet: dokumentlistan visas inte. Applikationsteamet kan kontrollera vilket API som anropades, vilken tidsgräns som användes och hur tjänsten hanterade felet. Plattformsteamet kan undersöka tjänsteupptäckt, lastbalansering, instansstatus och eventuella plattformspolicyer. Nätverksfunktionen kan verifiera om trafiken passerar avsedda zoner och brandväggar. Säkerhetsfunktionen kan utreda om en policy ska ändras – eller om blockeringen faktiskt är korrekt.

För att denna samverkan ska fungera behövs gemensamma spår: korrelations-ID i anrop, begripliga felkoder och relevanta loggar från både applikation och trafikkomponenter. Felsökning får inte kräva att någon manuellt gissar vilken VM ett anrop råkade passera. Hur signalerna används i övervakning och incidentarbete fördjupas i kapitel 13 och 14.

Ett viktigt beslut måste vara fattat i förväg: **vem leder felsökningen när flera ansvariga funktioner berörs?** Den som äger nätverket behöver inte äga den verksamhetsincident som användaren upplever. Och den som äger ärendetjänsten behöver inte ha rätt att ändra brandväggspolicyn.

## En möjlig ansvarsfördelning

| Beslut eller uppgift | Applikationsteam | Plattform/drift | Nätverk/säkerhet |
|---|---|---|---|
| Beskriva nödvändiga anrop och API-kontrakt | Huvudansvar | Bidrar med driftskrav | Bidrar med säkerhetskrav |
| Fastställa tillåtna trafikflöden | Föreslår behov | Implementerar enligt modell | Fastställer övergripande policy |
| Driva lastbalanseringsförmåga | Anger tjänstens behov | Huvudansvar i denna modell | Samverkar vid exponeringskrav |
| Hantera timeout och fel i klientkod | Huvudansvar | Tillhandahåller mätvärden | — |
| Felsöka kommunikationsproblem | Undersöker anrop | Undersöker plattform och trafik | Undersöker nätverk och policy |

Tabellen är ett exempel på ansvar för genomförande och samverkan, inte en fullständig RACI-matris. Beslutsmandat för avsteg, driftberedskap och incidentledning behöver dokumenteras separat. En liten organisation kan samla flera roller i samma team, och en större organisation kan separera nätverk, säkerhet, drift och plattform. Det viktiga är att ingen förutsätter att någon annan äger helheten.

## Vårt ärendehanteringssystem – från fel till förbättring

I vårt exempel visar det sig att ärendetjänsten försöker nå dokumenttjänsten via en adress som fungerar i utvecklingsmiljön men inte är avsedd för produktion. Produktionsmiljön har en korrekt nätverkspolicy som blockerar denna väg. Felet är alltså inte att brandväggen behöver öppnas utan att en miljöspecifik adress har hamnat i applikationens konfiguration.

Lösningen är att dokumenttjänsten får en stabil, godkänd tjänsteadress i respektive miljö och att applikationens konfiguration styrs via en kontrollerad leveransprocess. Applikationsteamet ändrar klientkonfigurationen och kompletterar med automatiserade konfigurationskontroller. Ett separat integrationstest i en representativ miljö verifierar adressupplösning, faktisk trafikväg och att blockeringar ger synliga fel i stället för en missvisande tom dokumentlista. Plattformsteamet ser till att den avsedda tjänsteadressen och de dokumenterade trafikreglerna finns. Säkerhetsfunktionen behöver inte godkänna en generell brandväggsöppning för att kompensera för felet.

Detta visar varför arkitektur och drift inte kan behandlas var för sig. Ett litet konfigurationsfel blir ett problem över flera ansvarsgränser, men en fungerande samarbetsmodell gör det möjligt att både åtgärda det och minska risken för upprepning.

## Det som faktiskt förändras

I en monolit var en stor del av kommunikationen ett internt programmeringsproblem. I en mikrotjänstarkitektur blir flera sådana beroenden uttryckliga och går över process- eller nätverksgränser. Det ger möjlighet till självständighet, men ökar behovet av genomtänkta kontrakt, trafikvägar och ansvar.

För **applikationssidan** betyder förändringen att nätverkets beteende och tekniska fel måste påverka hur API:er och klienter byggs. För **driftsidan** betyder den att tjänsternas logiska beroenden behöver synas i nätverkspolicy, trafikstyrning och felsökning – även när instanserna flyttar på sig. För **båda** blir kommunikation en gemensam arkitekturfråga snarare än enbart ett anrop i kod eller en port i en brandvägg.

### Källor och vidare läsning

- **[R6](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/interservice-communication)** Microsoft Learn, Design interservice communication for microservices (åtkomst 2026-10-17).
