# 11. Vem tillhandahåller miljöer och gemensamma förmågor?

I det traditionella ärendehanteringssystemet kan en ny miljö kräva beställningar av VM, databas, DNS-namn och brandväggsöppning innan applikationen installeras. Varje leverans kan fungera väl, men de manuella överlämningarna styr tiden från idé till körbar miljö.

När dokumenthanteringen blir en självständig tjänst förändras förutsättningarna. Fler tjänster kan behöva utvecklas, provas, uppdateras och driftsättas vid olika tillfällen. Om varje tjänst behöver en lång kedja av specialbeställningar förlorar arkitekturen en del av den självständighet den var avsedd att skapa. Lösningen behöver inte vara att alla utvecklare blir serveradministratörer. Den kan vara att organisationen bygger gemensamma **plattformsförmågor** som gör beprövade driftlösningar enkla att använda utan att ansvar och säkerhet går förlorade. [R12](https://learn.microsoft.com/en-us/platform-engineering/overview/)

## Plattformen är ett erbjudande, inte bara ett kluster

En plattform erbjuder dokumenterade sätt att skapa miljöer, driftsätta program, ansluta databaser, hantera hemligheter och följa tjänsternas funktion. Servrar och containrar räcker inte som erbjudande: användarna behöver också känna till förmågornas krav, garantier och begränsningar.

Det kan beskrivas som ett **plattformskontrakt**. Det anger vad applikationsteamet behöver deklarera, vilka kontroller som görs automatiskt och vem som godkänner undantag. Det beskriver också erbjuden tillgänglighet, kontaktvägar, incidentansvar, stödda versioner och hur plattformsförändringar meddelas. Kontraktet behöver inte vara ett juridiskt dokument. Poängen är att beroendet mellan utveckling och plattform blir begripligt och styrbart.

En väl vald plattformsförmåga minskar det arbete som varje team annars måste uppfinna på nytt. Samtidigt är en förmåga som döljer för mycket farlig: om applikationsteamet inte kan förstå hur tjänstens data lagras, hur den återställs eller hur nätverkstrafiken tillåts uppstår nya ansvarsglapp.

## Från serverbeställning till deklarerat behov

I vårt exempel behöver dokumenttjänsten en körmiljö med två instanser, lagring för uppladdade dokument, ett sätt att nå ärendetjänsten och ett sätt att få sina loggar och mätvärden insamlade. Tidigare kunde vart och ett av dessa behov leda till en separat beställning. I en mer automatiserad modell beskriver applikationsteamet sina behov i versionsstyrd konfiguration, varefter plattformen skapar eller uppdaterar de resurser som krävs.

Detta är ett deklarativt sätt att arbeta med **infrastruktur som kod** (Infrastructure as Code, IaC): önskat tillstånd beskrivs i versionsstyrda definitioner. IaC kan också använda instruktioner för vilka steg som ska utföras. Gemensamt är att etablering och ändring av infrastrukturen kan granskas, automatiseras och upprepas; infrastrukturen blir inte därmed applikationskod. En deklaration anger önskat läge men garanterar inte att verkligheten alltid överensstämmer med det; avvikelser mellan deklarerat och faktiskt tillstånd behöver upptäckas och hanteras. Automatisering kan minska manuella skillnader mellan miljöer, men en felaktig mall eller för omfattande behörighet kan sprida ett fel mycket snabbt. Därför behövs granskning, versionskontroll, ändringsspår och kontroll av vad som faktiskt har blivit installerat.

Automatisering betyder heller inte att varje team får beställa obegränsade resurser. Organisationen behöver standardiserade resursklasser, kvoter, säkerhetsregler, kostnadsgränser och rutiner för undantag. Den självbetjäning som fungerar bäst är ofta **självbetjäning inom överenskomna ramar**.

## Vilka gemensamma förmågor behövs?

Det är frestande att bygga en stor plattform innan de första tjänsterna har några tydliga behov. Ett bättre tillvägagångssätt är att utgå från återkommande uppgifter och göra dem lätta att utföra på ett säkert sätt.

För dokumenttjänsten kan ett första gemensamt erbjudande omfatta:

- **Körning och driftsättning:** en godkänd väg från byggd artefakt till körande instans, med versioner, resursgränser och återstartsmekanismer.
- **Konfiguration och hemligheter:** separering av kod och miljöspecifika värden, skydd för lösenord och nycklar samt kontrollerad rotation.
- **Nätverk och trafik:** namnuppslagning, trafikvägar, nätverkspolicyer och certifikathantering enligt beslutad säkerhetsmodell.
- **Databas och lagring:** standardiserad provisionering, övervakning, säkerhetskopiering och återställningsförutsättningar för godkända datatjänster.
- **Observerbarhet:** central insamling av loggar, mätvärden och spår, med gemensamma begrepp och åtkomstregler.
- **Policy och efterlevnad:** kontroller som upptäcker otillåtna inställningar eller osäkra beroenden innan förändringen når produktion.
- **Miljöernas livscykel:** möjlighet att skapa, uppdatera och avveckla utvecklings- och testmiljöer utan att kvarlämnade resurser växer okontrollerat.

Att flera funktioner finns i samma katalog innebär inte att de drivs av ett enda team. En databastjänst kan exempelvis levereras av en DBA-funktion, medan en gemensam plattform gör beställning, behörigheter och övervakning enhetliga. Det behöver vara tydligt om ett löfte om tillgänglighet gäller databasfunktionen, hela dokumenttjänsten eller den verksamhetsprocess som använder dem.

## Databastjänst utan förlorat dataansvar

Anta att dokumenttjänsten får sin databas genom en gemensam databastjänst. DBA- eller plattformsteamet kan ansvara för motorns patchning, kapacitet, krypteringsinställningar, backupfunktioner och teknisk övervakning. Dokumenttjänstens team ansvarar fortfarande för datamodellen, schemaförändringar, rimliga frågor och att applikationens data går att tolka vid återställning. Verksamhetens ansvar för informationens riktighet och hantering försvinner inte.

Här räcker det inte att säga att plattformen tar backup. Det måste vara dokumenterat vad som säkerhetskopieras, hur ofta, vilka återställningspunkter som är möjliga och om dokumentfiler och metadata kan återställas så att de passar ihop. En tekniskt fungerande databasåterläsning är inte automatiskt en återställd verksamhetsprocess. Den större frågan om samordnad kontinuitet behandlas längre fram i boken.

## Hemligheter, certifikat och identiteter

I en traditionell installation kan en drifttekniker manuellt lägga in ett certifikat eller ett lösenord på en server. När många tjänster startas om och byter instanser blir den modellen svår att skala och lätt att glömma bort. Plattformen kan i stället tillhandahålla tjänsteidentiteter, säker lagring och distribution av hemligheter samt automatiserad certifikathantering.

Men automatisering av förvaring och rotation är inte samma sak som beslut om åtkomst. Applikationsteamet behöver beskriva vilka tjänster och data det faktiskt behöver nå. Säkerhetsfunktionen kan fastställa krav på separation, minsta behörighet och spårbarhet. Plattformen genomdriver delar av dessa krav. Ansvarsfördelningen behöver vara tydlig även när en central identitetsleverantör används. Frågor om autentisering och auktorisation utvecklas i kapitel 15. [R13](https://kubernetes.io/docs/concepts/security/multi-tenancy/)

## Vem får ändra vad?

En modell där utvecklare kan driftsätta självständigt kan skapa oro för att drift tappar kontroll. Automatiserad självbetjäning är dock inte liktydig med att varje tjänsteteam får administrativa rättigheter till den underliggande infrastrukturen. En modell där varje resursändring kräver ett manuellt ärende kan å andra sidan omöjliggöra den förändringstakt arkitekturen bygger på. Det är inte nödvändigt att välja mellan gränslös frihet och total centralisering.

En möjlig uppdelning är att applikationsteamet får ändra sin tjänst inom en godkänd resursprofil och ett publicerat plattformskontrakt. Plattformsteamet bestämmer hur profilen omsätts till resurser och hur plattformen uppgraderas. Säkerhetsfunktionen bestämmer krav och vilka avvikelser som behöver godkännas. En funktion med helhetsansvar följer upp att verksamhetens krav på tillgänglighet och kontinuitet uppnås.

Denna uppdelning behöver kompletteras med beslut om vem som får öka kvoter, byta databasprodukt, ändra nätverkspolicyer och stoppa driftsättningar under störningar. Mandat ska finnas före incidenten, inte uppfinnas under den.

Det är också möjligt att samma team har flera roller i en mindre organisation. Poängen är att ansvaren ska vara identifierade, inte att varje ansvar kräver en egen avdelning.

## Plattformen måste själv förvaltas som en produkt

En gemensam plattform ger standardisering men blir också ett beroende för många tjänster. En felaktig uppdatering av ett gemensamt certifikatflöde eller en ändrad nätverkspolicy kan få större spridning än ett fel i en enskild mikrotjänst. Plattformens egna ändringar behöver därför testas, kommuniceras och driftsättas kontrollerat. Tjänsteteam behöver veta vilka delar som är stabila, vilka som är på väg att avvecklas och hur länge kompatibilitet upprätthålls.

Plattformen behöver ägarskap, användarstöd, utrymme för förbättringar och en plan för äldre gränssnitt. Utöver upptid bör kvaliteten följas genom miljöernas leveranstid, behovet av undantag och möjligheten att felsöka. Säkra standardlösningar ska vara lätta att använda; annars kan självbetjäningen bara flytta komplexiteten till utvecklaren.

För driftsidan innebär detta en förskjutning från att utföra samma manuella moment upprepade gånger till att utveckla och förvalta gemensamma automatiserade förmågor. Det är ett kvalificerat driftuppdrag, inte en avveckling av driftkompetensen. För applikationssidan innebär det att kunna formulera sina behov i standardiserade termer och ta ansvar för hur den egna tjänsten använder plattformens erbjudande.

## När en ny dokumentmiljö ska skapas

Vi återvänder till ärendehanteringssystemet. Dokumentteamet vill starta en tillfällig utvecklingsmiljö för en ny förhandsvisningsfunktion. Teamet väljer en godkänd miljötyp och beskriver vilken tjänsteversion, databasprofil och resursnivå som behövs. Plattformen kontrollerar kvot, identitet och nätverkspolicy, skapar resurser och kopplar på standardövervakning. Miljön får ett ägarskap, en kostnadsmarkering och en regel för automatisk avveckling.

Otillåten trafik ska ge en begriplig felrapport och hänvisning till det beslutade undantagsflödet, inte en automatisk öppning. Dokumentteamet ska följa samma princip för resursgränser: avvikelser hanteras öppet, utan dolda manuella ändringar.

Självständiga mikrotjänster kräver inte att varje utvecklingsteam driver sin egen infrastruktur. De kräver en **tydlig relation mellan tjänstens krav och plattformens erbjudande**, med ansvar som håller ihop verksamhetens IT-stöd.

### Källor och vidare läsning

- **[R12](https://learn.microsoft.com/en-us/platform-engineering/overview/)** Microsoft Learn, Platform engineering documentation (kontrollerad 2026-10-17).
- **[R13](https://kubernetes.io/docs/concepts/security/multi-tenancy/)** Kubernetes, Multi-tenancy (kontrollerad 2026-10-17).
