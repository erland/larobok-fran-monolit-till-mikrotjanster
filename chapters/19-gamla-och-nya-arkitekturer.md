# 19. Hur lever vi med gamla och nya arkitekturer samtidigt?

Det är frestande att beskriva modernisering som ett före och ett efter. Först har organisationen en monolit, sedan har den ett antal mikrotjänster. I praktiken finns det ofta en lång mellanperiod när gammal och ny arkitektur används samtidigt. Ärendehanteringen körs fortfarande som en sammanhållen applikation på sina virtuella servrar, medan dokumenthanteringen har flyttats till en egen tjänst. Båda lösningarna är produktionskritiska. Båda behöver utvecklas, övervakas, skyddas och förvaltas.

Det svåra är inte bara att få det gamla och nya att tala med varandra. Det svåra är att se till att **övergången faktiskt leder mot en enklare och mer ändamålsenlig målbild**, i stället för att skapa två permanenta tekniska världar som måste hållas vid liv.

## Mellanläget är ett riktigt driftläge

När dokumentfunktionen först bryts ut påverkas användaren kanske knappt alls. Hen öppnar fortfarande ett ärende i samma gränssnitt och klickar på samma knapp för att bifoga en fil. Men bakom knappen har ansvaret förändrats. Den äldre ärendeapplikationen anropar dokumenttjänsten över nätverket och kan behöva hantera tidsgränser, identiteter och tillfälliga störningar som tidigare inte fanns mellan funktionerna.

Samtidigt kan det äldre systemet fortsätta vara beroende av den gamla databasen, schemalagda jobb och verktyg för serverdrift. Den nya dokumenttjänsten kan driftsättas via en automatiserad leveranskedja och använda andra mekanismer för loggning, nätverk och hemlighetshantering. Detta är inte nödvändigtvis fel. Olika livscykler är själva poängen med en stegvis förändring. Men olikheterna måste vara synliga och accepterade i organisationens förvaltningsplan.

Mellanläget behöver därför ha en uttrycklig ägare, en riskbild, avtalade integrationsgränser, mätbara kriterier för nästa etapp och en tidshorisont som kan omprövas. Varje omprövning bör redovisa varför gamla beroenden fortfarande behövs, i stället för att automatiskt förlänga övergången. Annars är risken att det beskrivs som tillfälligt år efter år utan att någon finansierar de sista stegen. [R22](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)

## Flytta förmågor stegvis i stället för att skriva om allt

Ett vanligt angreppssätt är att gradvis låta en ny lösning ta över avgränsade funktioner från den gamla. Detta brukar kallas *strangler-mönstret*: nya gränssnitt eller tjänster ersätter delar av en äldre lösning tills de delar som inte längre behövs kan stängas av.

För ärendehanteringen kan första steget vara att en ny dokumenttjänst tar hand om nya uppladdningar. Nästa steg kan vara att också läsa äldre dokument genom samma gränssnitt. Det betyder inte att hela ärendehanteringen behöver delas upp. En lyckad modernisering kan bestå av en begränsad utbrytning där resten av monoliten lever vidare med tydligare interna gränser.

Det viktiga är att varje etapp ger en prövbar verksamhetsnytta och minskar ett identifierat problem. Utan sådana mål kan utbrytningen skapa nya nätverksanrop och mer driftarbete utan att användarna eller teamen vinner tillräckligt mycket.

## Integrationslager som skydd mellan olika modeller

Det äldre systemets datamodell är sällan ett bra kontrakt för en ny mikrotjänst. I monoliten kan ett dokument vara en rad i samma databas som ärendet, med direkt åtkomst till interna tabeller. Den nya dokumenttjänsten behöver i stället ett avgränsat API och egna regler för metadata, åtkomst och lagring.

Ett **översättande integrationslager**, ibland kallat *anti-corruption layer*, kan omvandla äldre begrepp och anrop till den nya tjänstens språk. Det ger ärendeapplikationen en stabil koppling utan att dokumenttjänsten behöver överta alla äldre antaganden. Exempelvis kan en gammal intern statuskod översättas till ett mer uttryckligt dokumenttillstånd. Översättningen bör ha tydlig ägare och egna tester. Det behöver också framgå om lagret är en del av monoliten, en separat adapter eller den nya tjänstens gräns; placeringen påverkar driftsättning, behörigheter och felsökning.

Lagret har samtidigt en kostnad. Om det blir platsen där all ny verksamhetslogik hamnar har man skapat ännu en komponent som behöver förvaltas. Syftet är att skydda gränsen, inte att dölja en permanent oklarhet om vilket system som bestämmer vad.

## Vem äger informationen under flytten?

En av de riskfyllda övergångarna gäller data. Om både monoliten och dokumenttjänsten får skriva samma dokumentmetadata är det svårt att veta vilken version som är rätt vid en konflikt. Det kan fungera under mycket avgränsade kontrollerade former, men delat skrivansvar får inte bli en omedveten standardlösning.

Organisationen behöver fastställa **vilken komponent som är auktoritativ för varje uppgift under varje etapp**. Det räcker inte att ange en ägare för hela dokumentet: dokumentinnehåll, metadata, behörighetsbeslut och kopplingen till ärendet kan ha olika ansvariga. För varje uppgift bör läsare, skrivväg och ansvarig vid avvikelse vara dokumenterade. I ett första steg kan monoliten äga äldre metadata och dokumenttjänsten äga nya uppladdningar. I ett senare steg kan dokumenttjänsten ta över allt dokumentinnehåll och all dokumentmetadata medan ärendetjänsten behåller relationen mellan ärende och dokument. Det senare ansvaret kan uttryckas som ett dokument-ID och ett tillstånd, inte som direkt tillgång till dokumenttjänstens tabeller.

Ibland behöver data kopieras mellan miljöerna under en övergång. Kopiering kan ske som en engångsmigrering, i mindre omgångar eller genom synkronisering av förändringar. Varje metod kräver en verifierbar plan för provmigrering, avstämning, felhantering och beslut om övergång till den nya källan. Är antalet poster rätt? Har filerna korrekt innehåll? Är behörigheterna bevarade? Går det att spåra vad som migrerats och vad som misslyckats? Det räcker inte att databastabellerna ser lika ut om dokument inte längre går att öppna i verksamhetsflödet.

Om data förs över löpande måste man också definiera fördröjning och avstämning. En användare får inte tro att en handling försvunnit bara för att uppdateringen ännu inte har nått lässidan. Därför behövs tydliga tillstånd och ett sätt att upptäcka och rätta avvikelser.

## Undvik att skapa två system som båda bestämmer

Att låta två system parallellt genomföra samma affärsoperation, så kallade dubbla skrivningar, kan verka som en enkel migrationsväg. Men det går inte att anta att två separata skrivningar antingen lyckas eller misslyckas tillsammans. Det ena systemet kan uppdateras medan det andra får ett nätverksfel.

Ett säkrare utgångsläge är att styra varje skrivoperation till en bestämd ägare. Om den andra miljön behöver information kan den få en kopia via händelser eller en kontrollerad synkroniseringsprocess. Då behövs hantering av duplicerade meddelanden, fördröjningar, ordningsföljd och avstämning. Ett händelseflöde är inte i sig en garanti för att den mottagande sidan har en aktuell eller korrekt kopia. Om dubbla skrivningar ändå väljs krävs en medveten strategi för konflikter, återhämtning och beslut om vilket resultat som gäller.

När äldre dokument flyttas behöver cutover – bytet från gammal till ny källa – planeras i förväg. Ett återgångsbeslut är inte automatiskt möjligt efter att data börjat ändras i den nya lösningen. Teamen måste därför veta vilka steg som är reversibla, när återgången stängs och hur felaktiga eller ofullständiga poster hanteras.

## Två driftsmodeller – ett sammanhållet säkerhetskrav

För driftsidan kan övergången innebära att virtuella servrar och traditionell förändringshantering samsas med en plattform för mer självständiga tjänster. Nätverksvägar, namnuppslagning, brandväggsregler, certifikat, reservkopior och övervakning måste fungera i båda miljöerna. Den nya dokumenttjänsten kan behöva anropa en äldre identitetslösning, samtidigt som den gamla ärendeapplikationen behöver tillgång till det nya tjänste-API:t.

Sådana förbindelser bör dokumenteras som namngivna och ägda beroenden. Det är särskilt viktigt om en tillfällig brandväggsöppning eller en övergångsidentitet riskerar att bli kvar med alltför breda rättigheter. Säkerhetskraven ska gälla hela informationsflödet även om tekniken för att uppfylla dem skiljer sig åt. Särskilt behöver teamen verifiera att åtkomst som nekas i det gamla systemet inte av misstag tillåts genom det nya gränssnittet; nätverksåtkomst och tjänsteautentisering ersätter inte användarens behörighetsprövning.

En ny driftsmodell innebär inte heller att det äldre systemet kan sluta underhållas. Så länge det är produktionskritiskt behöver det patchning, kapacitet, backup, återläsningsförmåga och kompetens. Moderniseringsbudgeten måste rymma även detta arbete.

## Testa övergången som en helhet

Ett test av dokumenttjänsten kan vara godkänt utan att användaren kan bifoga dokument från monolitens gränssnitt. Därför måste de kritiska flödena testas över gränsen. Relevanta scenarier är exempelvis uppladdning, läsning, borttagning enligt gällande regler, behörighetsändring och visning av dokument som ännu migreras.

Övergången ger också blandade versionslägen: en äldre ärendeapplikation kan använda en ny dokumenttjänst, och ett gammalt integrationsmeddelande kan behandlas efter att tjänsten har uppdaterats. Kontrakt och kompatibilitet behöver därför provas utifrån de kombinationer som faktiskt kan förekomma under migreringen, inte enbart den senaste versionen av varje komponent.

Drift- och applikationsteam behöver gemensamt genomföra åtminstone några felprov: Vad händer om kommunikationen mellan de två miljöerna bryts? Vad ser användaren? Hur larmas rätt grupp? Och finns dokument som lagrats men ännu inte kopplats till sitt ärende? Svar på de frågorna är en förutsättning för ett säkert etappbyte. Inför varje etapp bör teamen även ha gemensamma kriterier för start, stopp och godkännande, inklusive vilken verksamhetsfunktion som ska återtestas efter en återgång eller korrigering.

## Vem äger övergången?

En stegvis modernisering behöver mer än separata leveransplaner. Någon måste kunna prioritera när arbetet med den nya tjänsten konkurrerar med felrättningar i monoliten eller med plattformsuppgraderingar. Det sammanhållande ansvaret kan ligga hos en systemägare, en produktledning eller ett särskilt moderniseringsprogram. Organisationen kan variera, men mandatet måste täcka helheten.

**Verksamheten** avgör vilka arbetsflöden som inte får störas och vilken informationsförlust eller tillfällig begränsning som kan accepteras. **Applikationsteamen** utformar tjänstegränser, datamigrering, kontrakt och felhantering. **Drift- och plattformsteamen** ansvarar för de förutsättningar de tillhandahåller, inklusive nätverk, identitet, övervakning och återställning. **Säkerhetsfunktioner** bidrar med krav och verifiering utifrån informationsskyddet. För gemensamma förändringar måste det vara klart vem som beslutar om driftsättning, stopp och avveckling.

Det är viktigt att inte fastna i en modell där en projektgrupp lämnar över en halvfärdig integrationslösning till den löpande förvaltningen utan tydligt ägarskap. Övergångskomponenter är också produktionskomponenter och behöver samma grundläggande ansvar för support, incidenter och livscykel.

## Planera för att tillfälliga lösningar ska försvinna

För varje tillfällig adapter, synkronisering eller brandväggsregel bör det finnas ett svar på fyra frågor: Varför behövs den? Vem ansvarar för den? Vilket villkor gör att den kan tas bort? Hur verifieras att borttagningen är säker?

Avveckling kan ske när den sista konsumenten lämnat ett gammalt API, när alla nödvändiga dokument har flyttats och kontrollerats eller när ingen verksamhetsfunktion längre behöver en viss server. Då återstår ändå att stänga konton, ta bort behörigheter och nätverksregler, hantera arkiv- och bevarandekrav, avsluta reservkopieringsrutiner på rätt sätt och uppdatera dokumentation samt kostnadsuppföljning.

Det är lättare att finansiera nyutveckling än att avveckla det sista gamla beroendet. Därför bör avvecklingsarbete vara ett uttryckligt leveransresultat, inte en vag ambition. En planerad avveckling behöver också styrkas i drift: en komponent får inte tas bort enbart därför att inga anrop synts under en kort mätperiod. Sällan använda integrationsvägar, reservrutiner och beroenden vid årsvisa händelser kan annars missas. Mät både vad som tillkommit och vad som faktiskt har försvunnit: kvarvarande äldre integrationer, aktiva synkroniseringsflöden, driftsatta servrar och beroenden som ännu kräver dubbel kompetens.

## Vad förändras för vem?

För **applikationsläsaren** innebär samlevnaden att tjänstegränser och informationsägarskap behöver införas gradvis och att gammal kod inte får styra den nya tjänstens interna modell. För **driftläsaren** innebär den att två tekniska världar måste hållas säkra, övervakade och återställningsbara samtidigt, ibland under flera år.

Den gemensamma lärdomen är att mellanläget inte är ett misslyckande – men det måste styras som ett medvetet och tidsbundet arkitekturtillstånd. När dokumenttjänsten väl är fristående är det inte antalet nya tjänster som visar om moderniseringen lyckats. Det är om verksamheten fått en hållbar lösning med tydliga ansvar, fungerande flöden och färre onödiga beroenden.

I det avslutande kapitlet återstår därför den viktigaste frågan: När motiverar nyttan med mikrotjänster den distribuerade komplexitet som organisationen nu har lärt sig att hantera?

### Källor och vidare läsning

- **[R22](https://learn.microsoft.com/en-us/azure/architecture/patterns/strangler-fig)** Microsoft Azure Architecture Center, Strangler Fig Pattern (kontrollerad 2026-10-17).
