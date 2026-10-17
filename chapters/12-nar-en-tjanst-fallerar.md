# 12. Vad händer när en tjänst slutar fungera?

Handläggaren öppnar ett ärende och väntar på att tillhörande dokument ska visas. Ärendeinformationen finns redan på skärmen, men dokumentlistan laddas aldrig färdigt. Efter en stund visar hela sidan ett felmeddelande. Samtidigt rapporterar driftplattformen att både ärendetjänsten och dokumenttjänsten körs. Hur kan IT-stödet ändå upplevas som otillgängligt?

I ett distribuerat system är en grön markering för en process inte samma sak som att ett verksamhetsflöde fungerar. Flera tjänster kan var för sig vara igång, men samspelet mellan dem kan misslyckas. Därför behöver både applikations- och driftorganisationen förstå **partiella fel**: situationer där en del av helheten fungerar medan en annan del är långsam, otillgänglig eller ger ett osäkert resultat. Frågan är inte bara hur felet kan åtgärdas, utan hur systemet ska bete sig medan felet pågår.

## När den lokala felmodellen inte längre räcker

I ett traditionellt ärendehanteringssystem anropar backend ofta sina egna moduler inom samma process. Metodanrop kan misslyckas, men det finns vanligtvis inget separat nätverk mellan två delar av samma program. När en funktion bryts ut till en dokumenttjänst förändras felbilden. Anropet mellan ärendetjänsten och dokumenttjänsten kan misslyckas även om båda programmen fungerar korrekt.

Ett nätverksanrop kan stoppas av brandväggsregler, gå till en instans som håller på att avslutas, fördröjas av överbelastning eller avbrytas när en mellanliggande komponent får problem. Ett svar kan också försvinna *efter* att dokumenttjänsten har utfört begäran. Då kan anroparen inte säkert veta om operationen genomfördes. Detta är en avgörande skillnad mot ett vanligt internt funktionsanrop: osäkerheten gäller ibland inte bara felorsaken utan även resultatet.

Den nya felmodellen innebär inte att monoliter saknar nätverksberoenden. Även en monolit talar med databaser, lagring och andra system. Skillnaden är att mikrotjänstarkitekturen medvetet inför fler anropsgränser mellan delar som tillsammans utför verksamhetsfunktionen. Ju fler beroenden som krävs för ett användarflöde, desto fler platser kan det flödet brytas på.

## Att vänta är också ett beslut

Anta att ärendetjänsten begär en dokumentlista och dokumenttjänsten inte svarar. Om anropet får vänta obegränsat kan användaren, applikationens anropstrådar och anslutningspooler bli upptagna. Vid hög trafik kan ett långsamt beroende på det sättet sprida belastning bakåt i kedjan.

En **timeout** sätter en gräns för hur länge en anropare väntar. Men en alltför kort gräns avbryter även legitima anrop vid tillfälliga toppar; en alltför lång kan låsa resurser och ge användaren oacceptabla väntetider. Tidsgränser behöver därför utgå från tjänstens normala svarstider, verksamhetens krav och hur mycket tid hela anropskedjan får använda. Ett gemensamt tidsutrymme för hela begäran kan behöva fördelas mellan flera underanrop.

Timeout betyder inte att arbete automatiskt avbryts hos mottagaren. Dokumenttjänsten kan fortsätta en operation efter att ärendetjänsten slutat vänta. För ändrande operationer är detta viktigt: ett nytt försök kan annars utföra samma förändring igen. [R14](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)

## Återförsök kan hjälpa – eller förvärra

Om en begäran misslyckas vid ett kort nätverksavbrott kan ett nytt försök vara rimligt. Men om dokumenttjänsten redan är överbelastad och varje anropare försöker flera gånger, kan trafiken öka just när tjänsten minst klarar det. Om flera tjänster i kedjan dessutom gör egna återförsök kan belastningen multipliceras.

Återförsök bör därför användas selektivt, med begränsat antal försök, ökande väntetider och viss slumpmässig variation så att anropare inte försöker samtidigt. Fel som tydligt är permanenta, såsom bristande behörighet eller felaktigt format, ska normalt inte upprepas. Operationer som förändrar data behöver dessutom stöd för **idempotens**, exempelvis en unik operationsidentifierare som mottagaren kan känna igen, eller annan mekanism som förhindrar oönskad dubbel effekt vid upprepning. Detta skydd måste omfatta även fall där ett svar försvinner efter genomförd operation.

Det centrala är att anropande tjänst behöver avgöra *vilken sorts fel* som inträffat och *vilken konsekvens* ett nytt försök kan få. Ett generellt återförsök på varje fel är ingen robusthetsstrategi.

## Att förhindra att ett fel sprider sig

Feltolerans kan beskrivas som flera kompletterande skydd, inte som en enskild teknisk produkt.

En **circuit breaker** kan tillfälligt sluta skicka anrop till ett beroende som upprepade gånger misslyckas. Det skyddar anroparens resurser och kan ge det felande beroendet utrymme att återhämta sig. Funktionen måste samtidigt kunna pröva när kommunikationen åter kan öppnas. Den reparerar inte det underliggande felet. Trösklar och återöppning behöver anpassas så att skyddet inte blir kvar i ett onödigt blockerande läge.

**Resursisolering** kan begränsa hur många samtidiga anrop eller arbeten ett beroende får belasta. Om dokumentlistan tar lång tid ska den helst inte kunna förbruka alla resurser som behövs för att läsa ärendeinformation eller spara andra uppgifter. Isoleringen kan finnas i applikationens anslutningspooler, arbetsköer och samtidighetsgränser, men också i plattformens resursgränser och kapacitetsregler.

**Belastningsbegränsning** och regler för att avvisa anrop vid överlast kan vara bättre än att acceptera mer arbete än tjänsten kan slutföra. Det förutsätter att klienter och användargränssnitt får begripliga signaler om vad som hände och om ett nytt försök är lämpligt.

Gemensamt för skydden är att de behövs *före* en incident. Ett team som upptäcker behovet av timeout, resursisolering och kontrollerade återförsök först under pågående avbrott får svårare att undvika följdproblem.

## Allt behöver inte sluta fungera samtidigt

I vårt exempel kan ärendeinformation fortfarande visas när dokumenttjänsten inte kan nås. Då kan användargränssnittet visa ärendet och tydligt ange: **”Dokument kan inte hämtas just nu.”** Det är något annat än att visa en tom dokumentlista. En tom lista säger i praktiken att ärendet saknar dokument, vilket kan vara fel och få verksamhetsmässiga följder.

Detta kallas ofta **kontrollerad degradering**: den del av funktionen som är tillgänglig fortsätter att fungera, samtidigt som användaren får korrekt information om begränsningen. I vissa fall kan en tidigare hämtad uppgift visas, men då måste dess ålder och tillförlitlighet vara tydliga. För ett rättsligt eller säkerhetskritiskt beslut kan det vara olämpligt att visa föråldrade data som om de vore aktuella.

Andra funktioner bör däremot stoppa helt när ett beroende fallerar. Om verksamhetsreglerna kräver att dokument verkligen har lagrats och registrerats innan ett ärende skickas vidare, får systemet inte rapportera genomförd registrering på grundval av enbart ett skickat anrop. Valet mellan degradering, köad behandling och stopp beror på verksamhetens krav – inte på att den ena tekniken alltid är bättre.

## När ett meddelande blir liggande

För asynkron kommunikation ser felet annorlunda ut. Ärendetjänsten kan ha skickat en händelse om att ett dokument ska bearbetas, samtidigt som dokumenttjänsten är otillgänglig. Meddelandet kan då ligga kvar i en kö eller ström, under förutsättning att infrastrukturen är byggd för det. Användaren behöver veta om dokumentet väntar på behandling, misslyckats eller är färdigt.

Köer kopplar loss två tjänsters exekveringstidpunkter men tar inte bort fel. En växande kö kan signalera att mottagaren inte hinner med. Vissa meddelanden kan behöva hanteras flera gånger, komma i annan ordning än väntat eller hamna i en särskild hantering för upprepade fel. Systemet behöver bestämda regler för fördröjningar, återförsök, idempotens, felaktiga meddelanden och hur verksamheten kan rätta ett fastnat flöde.

En kö kan alltså förbättra tåligheten vid tillfälliga avbrott, men den introducerar ett annat slags ansvar: att upptäcka och hantera arbete som inte blivit klart. Även meddelandets lagringstid, kökapacitet och återstart efter längre avbrott behöver vara avtalade; annars kan arbete gå förlorat eller ansamlas snabbare än det kan behandlas.

## Hälsa är inte detsamma som verksamhetsförmåga

En plattform kan övervaka om dokumenttjänstens instanser körs och om de kan ta emot trafik. Sådana hälsokontroller är viktiga, men de räcker inte för att avgöra om handläggaren faktiskt kan öppna ett dokument. En instans kan svara på hälsokontroller samtidigt som dess datalager är mycket långsamt eller ett beroende är felkonfigurerat.

Hälsokontroller för **om instansen lever** och **om den bör få trafik** behöver utformas med eftertanke. Om beredskapskontrollen gör varje instans oanvändbar så snart ett gemensamt externt beroende fallerar, kan hela tjänsten tas ur trafik utan att någon annan instans kan hjälpa. Samtidigt får en instans som faktiskt inte kan ta emot begäran inte felaktigt markeras redo.

Utöver tekniska kontroller behöver organisationen följa verkliga verksamhetsflöden: går det att öppna ett ärende, läsa dess dokument och slutföra en registrering? Metoderna för hur detta mäts och visualiseras behandlas i nästa kapitel om observerbarhet.

## Vem ansvarar för att tjänsten klarar störningar?

I en traditionell miljö kan driftorganisationen vara van att hantera tillgänglighet genom redundanta VM:ar, lastbalanserare och omstarter. Dessa åtgärder behövs ofta fortfarande. Men de kan inte på egen hand avgöra hur ett användargränssnitt ska reagera när ett beroende svarar för sent eller när en ändring kanske redan har utförts.

**Applikationsteamet** behöver därför beskriva vilka beroenden som är kritiska, välja tidsgränser och återförsök, utforma ett säkert användarbeteende samt se till att operationer fungerar när svar försvinner eller levereras flera gånger. **Drift- och plattformsteam** behöver bidra med kunskap om verkliga felmoder, kapacitetsgränser, redundans, trafikstyrning, resursisolering och återhämtningsmekanismer. **Verksamhetsansvariga** behöver ange vilka funktioner som måste fungera, hur länge avbrott kan tolereras och när en osäker status är oacceptabel.

Ingen av dessa roller kan ensam garantera helheten. Kraven måste omsättas i gemensamt beslutade scenarier och verifieras genom feltester, exempelvis att stoppa en tjänsteinstans, blockera en anslutning eller begränsa kapaciteten i en kontrollerad miljö. Feltester i produktion kan också vara relevanta, men bara under överenskomna säkerhets- och riskvillkor. Vem som får initiera sådana tester och vem som leder en verklig incident behöver vara explicit bestämt. Det behöver också finnas överenskomna mål för hur mycket funktionalitet som får försämras och hur snabbt normal funktion ska återupptas.

## Tillbaka till ärendehanteringen

När dokumenttjänsten i vårt exempel blir långsam ska ärendevyn inte vänta obegränsat. Ärendetjänsten använder en rimlig tidsgräns och begränsar hur många samtidiga anrop den skickar. Vid tillfälliga fel kan vissa läsanrop göras om enligt en begränsad policy. Om problemen fortsätter visas ärendeuppgifterna, men dokumentavsnittet ersätts av ett tydligt felmeddelande som inte påstår att ärendet saknar dokument.

När dokument ska registreras gäller strängare regler. Ärendehanteringen får inte visa att registreringen är avslutad om resultatet är okänt. I stället kan status vara *behandlas* eller *behöver kontrolleras*, med möjlighet till uppföljning och säker återupptagning. Plattformen bidrar med kapacitets- och nätverksmekanismer; tjänsterna bidrar med korrekt felbeteende. Verksamhetsansvariga avgör vilken begränsad funktionalitet som är acceptabel.

Den stora förändringen är inte att fel plötsligt uppstår – det gjorde de även i den traditionella miljön. Förändringen är att **fel i en del av systemet i större utsträckning måste hanteras som en normal förutsättning för hur hela tjänsten byggs och drivs**. Här har vi behandlat **hur tjänster utformas för att begränsa konsekvenserna**. Nästa kapitel handlar om hur organisationen **upptäcker och mäter påverkan**; först därefter går vi vidare till hur en verklig incident leds och åtgärdas.

### Källor och vidare läsning

- **[R14](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)** AWS Prescriptive Guidance, Retry with backoff pattern (kontrollerad 2026-10-17).
