# 14. Hur felsöker och hanterar vi incidenter?

En morgon går det inte att öppna dokument från ärendehanteringen. Användarna ser meddelandet *Dokumentet kan inte hämtas*. Ärendetjänsten svarar på sina hälsokontroller. Dokumenttjänsten gör det också. Driftcentralens sammanställning är huvudsakligen grön, men arbetet på handläggningsenheten står delvis stilla.

I en traditionell applikation finns ofta en gemensam förvaltnings- och driftkedja som kan samla in loggar från ett begränsat antal servrar och undersöka en gemensam release. I vårt distribuerade system måste en incident i stället undersökas över flera tjänster, nätverksförbindelser och organisatoriska ansvarsgränser. Det betyder inte att incidentledning är något nytt, utan att det blir viktigare att kunna samordna den oavsett vilken del som visar sig orsaka felet.

## Börja med verksamhetspåverkan, inte med den misstänkta komponenten

Den som tar emot larmet vet sällan vilken tjänst som orsakat störningen. Ett alltför tidigt antagande om att det är en applikationsbugg eller ett nätverksfel riskerar att styra felsökningen fel. Börja därför med frågorna: Vilka användare och arbetsmoment påverkas? När började det? Är felet totalt, intermittent eller begränsat till vissa ärenden? Finns risk för informationsförlust eller felaktiga beslut?

Allvarlighetsgrad och första prioritet bör grundas i verksamhetspåverkan, tidskritikalitet och risk för felaktig eller förlorad information, inte bara i antal larm. En dokumenterad tidslinje med klockslag, gjorda ändringar, hypoteser och beslut underlättar både samordningen och efteranalysen.

Den första lägesbilden ska kunna delas mellan applikationsteam, drift, plattform, informationssäkerhet och verksamhetsansvariga. Den behöver vara tillräckligt begriplig för att stödja prioritering, utan att redan innehålla en obestyrkt rotorsak. En incident med få tekniska felmeddelanden kan vara kritisk om ett centralt verksamhetsflöde är blockerat.

För ärendehanteringen fastställer incidentledaren exempelvis att dokument inte kan öppnas för en viss grupp användare, medan registrering av nya ärenden fungerar. Det ger en konkret avgränsning: funktionell åtkomst till dokument är problemet, inte allmän serverdrift. [R16](https://sre.google/workbook/incident-response/)

## Incidentledning är ett eget ansvar

Flera team kan arbeta samtidigt utan att någon av dem ensam har mandat att prioritera helheten. Därför behöver en utsedd incidentledare hålla samman lägesbild, beslut, resursfördelning, eskalering och kommunikation. Rollen kan ligga hos en central driftfunktion, en tjänsteorganisation eller en särskilt utsedd beredskapsfunktion. Det avgörande är att mandatet är tydligt innan störningen inträffar. Incidentledningen samordnar prioritering och riskbeslut men ska inte ge sig själv obegränsad rätt att ändra produktionssystem; behörigheter och tekniskt verkställande ansvar behöver vara uttryckligen delegerade.

Incidentledaren måste inte vara den tekniskt skickligaste felsökaren. Tvärtom är det ofta en fördel om tekniska experter kan koncentrera sig på diagnos och återställning medan incidentledningen dokumenterar beslut, säkerställer kommunikation och avgör när ytterligare kompetens ska kallas in.

Ett möjligt upplägg skiljer på tre roller: incidentledare, tekniska felsökare och ansvarig för kommunikation till användare och verksamhet. I mindre organisationer kan samma person fylla flera roller, men uppgifterna bör fortfarande vara uttalade. Vid en säkerhetsincident kan ytterligare besluts- och rapporteringsvägar behövas; detta ersätter inte organisationens säkerhetsrutiner.

## Felsökning över tjänste- och plattformsgränser

I vårt exempel rapporterar ärendetjänsten att anrop till dokumenttjänsten misslyckas. Dokumenttjänstens egna loggar visar emellertid inte motsvarande begäranden. En sådan skillnad är värdefull information: felet kan ligga före dokumenttjänstens applikationskod, exempelvis i DNS, trafikstyrning, certifikathantering, en nätverkspolicy eller ett felaktigt tjänstenamn. Kontrollera samtidigt att loggningen och insamlingen fungerar; frånvaro av en loggpost bevisar inte att begäran aldrig nådde tjänsten.

Teamet bör kontrollera händelsekedjan systematiskt. Har användarens begäran nått ärendetjänsten? Vilken adress försökte ärendetjänsten använda? Blev namnet uppslaget och anslutningen etablerad? Har en lastbalanserare skickat trafiken vidare? Har målinstansen tagit emot anropet och returnerat ett svar? Observerbarheten från föregående kapitel hjälper här, men är ingen ersättning för kunnande om applikationsprotokoll och infrastruktur.

Anta att en nyligen genomförd ändring har pekat ärendetjänsten mot ett äldre tjänstenamn som inte längre finns i den aktuella miljön. Felet visar sig då vara en felkonfiguration i tjänstens kommunikationsadress – inte en bugg i dokumenthanteringen och inte nödvändigtvis ett fel i DNS-tjänstens tillgänglighet. Vilket team som genomför rättningen beror på vem som äger konfigurationen och förändringsflödet. Ansvar för att användarna får tillbaka funktionen får däremot inte försvinna under diskussionen om felorsaken.

Samma princip gäller andra typer av incidenter. En överfull meddelandekö kan vara följden av långsam applikationsbehandling eller resursbrist på plattformen. Ett högt antal databasanrop kan orsakas av en ny applikationsversion trots att databasservern fungerar enligt sina egna driftmått. Felsökningen behöver därför pröva hypoteser mot fakta snarare än följa organisatoriska gränser. Den senaste driftsättningen är en viktig ledtråd, men tidsmässigt samband är inte bevis på orsak. Kontrollera också miljöförändringar, certifikat, routing och beroenden som kan ha ändrats oberoende av applikationsreleasen.

## Återställ tjänsten innan alla orsaker är kända

Under en pågående incident är målet först att begränsa skadan och återställa acceptabel verksamhetsfunktion. En fullständig rotorsaksanalys kan komma efteråt. Möjliga åtgärder är att återställa en tidigare fungerande konfiguration, styra om trafik, minska belastning, skala en resurs eller tillfälligt stänga av ett icke-kritiskt flöde.

Men varje åtgärd har risker. Att starta om alla instanser samtidigt kan öka avbrottet. Att automatiskt försöka om ett misslyckat kommando kan ge dubbel behandling om operationen redan utförts. Att återställa en äldre programversion kan vara olämpligt efter en icke-bakåtkompatibel datamigrering. En säker återställningsstrategi måste därför vara förberedd och prövad i förväg, inte uppfinnas under press. Om flera team arbetar parallellt bör varje planerad ändring ha en ansvarig utförare, en tydlig förväntad effekt och ett sätt att verifiera utfallet innan nästa riskfyllda åtgärd görs.

För dokumentincidenten väljer teamen att återställa den tidigare fungerande tjänsteadressen via det ordinarie konfigurationsflödet. De kontrollerar därefter både den tekniska anslutningen och att en användare faktiskt kan öppna dokument från ett ärende. Ett grönt hälsotest räcker inte för att avsluta incidenten. Kontrollera också om misslyckade eller uppskjutna dokumentoperationer behöver återköras, stämmas av eller hanteras manuellt så att informationsläget blir korrekt. Återställd åtkomst och avslutad incident betyder inte alltid att allt efterarbete är avslutat.

## Beredskap, eskalering och vägar in till rätt kompetens

När tjänster utvecklas av olika team kan ett fel inträffa utanför deras ordinarie arbetstid. Organisationen måste därför välja en tydlig beredskapsmodell. Ett tjänsteteam kan ha egen jour, en central funktion kan vara första linjen med eskalering till tjänsteexperter, eller flera team kan dela en beredskapstjänst. Ingen modell följer automatiskt av att applikationen består av mikrotjänster.

Vilken modell som är rimlig påverkas av tillgänglighetskrav, kompetens, personberoende, kostnad och hur väl systemet kan återhämta sig automatiskt. Om applikationsteamet förväntas svara på produktionsincidenter måste detta stödjas av avtalade arbetstider, åtkomst till relevant telemetri, utbildning, fungerande beredskapsrutiner och mandat att genomföra säkra åtgärder. Det räcker inte att skriva *teamet äger tjänsten*.

Eskaleringen bör bygga på vilket problem som behöver lösas, inte enbart på vilket team ett larm först träffar. Säkra kontaktvägar, tjänstekatalog, beroendekarta och aktuell information om ansvariga behöver vara åtkomliga även när delar av den ordinarie IT-miljön är nere.

## Kommunikation och ansvar gentemot användarna

Användarna behöver sällan känna till om avbrottet orsakas av dokumenttjänsten, nätverket eller plattformen. De behöver veta vad som inte fungerar, vilka tillfälliga arbetssätt som finns, vilken risk som föreligger och när en ny lägesrapport kommer. Därför behöver verksamhetskommunikationen vara samlad även om den tekniska felsökningen är fördelad.

Incidentledningen ska undvika tvärsäkra orsaksbeskrivningar innan de är verifierade. Det är bättre att säga att dokumentåtkomst är störd och att berörda team undersöker sambandet mellan tjänsterna än att tidigt peka ut en viss leverantör eller teknik. Om data kan ha gått förlorade eller behandlats felaktigt behöver dessa risker hanteras separat, med rätt verksamhets- och informationsansvariga.

## Lärande efter incidenten

När dokumentåtkomsten åter fungerar behöver organisationen förstå varför felet kunde uppstå, varför det inte upptäcktes tidigare och varför återställningen tog den tid den gjorde. En efteranalys bör omfatta både tekniska och organisatoriska faktorer: en saknad kontroll av tjänsteadresser, ett otydligt ägarskap för konfigurationen, bristande test av miljöändringar eller svårigheter att nå rätt kompetens.

En bra analys söker förbättringar av systemet och arbetssättet framför att leta syndabockar. Det kan innebära ett automatiserat integrationstest av tjänsteanslutningen, en säkrare konfigurationsvalidering, en förbättrad larmregel eller en förändrad eskaleringsrutin. Efteranalysen bör skilja på säkerställda fakta, rimliga hypoteser och sådant som fortfarande är okänt. Varje åtgärd behöver en ansvarig och en uppföljning; annars riskerar slutsatserna att stanna i mötesanteckningarna.

Det bör också finnas en gräns mot förändringshantering. Ett akut återställande ska dokumenteras, men inte nödvändigtvis tvingas genom samma beslutsförfarande som en planerad större ombyggnad. Förhandsbeslutade nödrutiner kan förena handlingsförmåga med kontroll och efterföljande granskning.

## Vad behöver applikations- och driftsidan göra annorlunda?

För **applikationssidan** innebär distribuerad incidenthantering att teamen måste kunna beskriva sina beroenden och deras felbeteenden, bidra med verksamhetsnära diagnostik och delta i återställning när den egna tjänsten eller dess kontrakt är inblandade. Det gäller även om infrastrukturen sköts av ett annat team.

För **driftsidan** innebär det att felsökningen inte kan stanna vid att varje server och plattformsdel är tekniskt frisk. Drift- och plattformsexperter behöver förstå användarflöden, tjänsteadresser, trafikvägar och förändringar som införts av olika leveransteam. Deras erfarenhet av strukturerad incidentledning och infrastrukturella beroenden blir därför fortsatt central.

Det **gemensamma ansvaret** är att utse vem som leder en incident, vem som kan ändra vad, vem som kommunicerar med verksamheten och hur man verifierar att hela funktionen återställts. Dessa beslut måste finnas före incidenten, även om den exakta tekniska felorsaken inte kan förutses.

## En fungerande helhet även under störning

De skyddsmekanismer vi beskrev i kapitel 12 kan begränsa ett fel, och signalerna från kapitel 13 kan visa dess påverkan. Men **under en pågående incident behövs dessutom samordnade beslut**, eftersom flera team kan behöva agera samtidigt. Mikrotjänster kan göra felsökningen mer komplicerad även när de enskilda tjänsterna återhämtar sig självständigt. Det avgörande är inte om varje team har kontroll över sin egen komponent, utan om organisationen som helhet kan upptäcka påverkan, samordna åtgärder och återställa det IT-stöd som användaren är beroende av.

Nästa kapitel fördjupar en närliggande fråga: hur säkerställer vi att kommunikation och informationsåtkomst är säkra när identiteter och behörigheter behöver fungera över flera tjänstegränser?

### Källor och vidare läsning

- **[R16](https://sre.google/workbook/incident-response/)** Google SRE Workbook, Incident Response (kontrollerad 2026-10-17).
