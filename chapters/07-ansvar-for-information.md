# 7. Vem ansvarar för informationen?

När ärendehanteringssystemet bestod av en gemensam backend och databas kunde utvecklarna ofta lösa ett nytt informationsbehov genom att lägga till en kolumn, skapa en relation och skriva en SQL-fråga. Det betydde inte att informationsägarskapet var enkelt, men tekniskt låg informationen nära till hands. När dokumenthanteringen blir en separat tjänst förändras förutsättningarna. Ärendetjänsten behöver fortfarande visa vilka dokument som hör till ärendet, men kan inte längre utgå från att den själv kan läsa och ändra dokumenttjänstens tabeller.

Frågan är inte bara var data ska lagras. Den handlar om vem som får definiera dess innebörd, vem som får ändra dess struktur, hur flera tjänster kan ge användaren en korrekt bild och vem som ser till att informationen finns kvar och går att hantera över tid.

## En databas gjorde inte informationen till ett gemensamt ansvar

I vårt traditionella ärendehanteringssystem finns kanske tabeller för ärenden, parter, beslut, dokument och händelser i samma databas. En transaktion kan då uppdatera ett ärende och registrera en dokumentkoppling som en sammanhållen operation. En rapport kan använda en JOIN över tabellerna. Ett DBA-team kan sköta databasplattform, index, kapacitet, behörigheter och backup, medan applikationsteamet arbetar med tabeller och frågor.

Men att flera tabeller råkar ligga i samma databas betyder inte att de bör ha samma verksamhetsansvar. Även i en monolit behöver organisationen veta vem som beslutar vad ett dokument, ett ärende eller ett beslut betyder, vilken information som får lagras och vilka kvalitetskrav som gäller. Mikrotjänster gör bara ansvarsskillnaderna mer synliga – och tekniskt svårare att kringgå.

## Tre ansvar som måste hållas isär

Vi behöver skilja mellan minst tre nivåer.

**Informationsansvar** gäller begrepp, regler, klassificering, gallring, kvalitet och tillåten användning. Verksamheten eller en utsedd informationsansvarig måste kunna avgöra vad ett ärende och dess dokument betyder och vilka krav som gäller. Detta ansvar upphör inte för att en tjänst har en egen databas.

**Tjänstens dataansvar** gäller den datamodell och de gränssnitt som tjänsten använder för att uppfylla sitt uppdrag. Dokumenttjänstens team bör till exempel styra sin interna representation av dokumentmetadata och publicera överenskomna funktioner för att registrera eller läsa dem. Andra tjänster bör normalt inte koppla sin logik direkt till dokumenttjänstens tabellstruktur.

**Databasdrift** gäller den tekniska plattformens tillgänglighet, säkerhetskonfiguration, lagring, övervakning, kapacitet, patchning och mekanismer för backup och återställning. Det kan vara ett centralt DBA-team, ett plattformsteam eller en extern leverantör som utför mycket av detta. Tjänsteteamet måste ändå förstå hur databasen används och vilka risker dess ändringar medför.

Den som ansvarar för teknisk drift bestämmer alltså inte automatiskt informationsbegreppens innebörd. Den som äger datamodellen behöver inte själv administrera databasoperativsystemet. Och den som ansvarar för verksamhetsinformationen behöver inte godkänna varje teknisk schemaändring. Gränserna behöver definieras – inte antas.

## Vad betyder det att en tjänst äger sina data?

Principen om tjänsteägd data innebär att andra tjänster i normalfallet inte ska ändra en tjänsts information genom direkt åtkomst till dess interna lagring. Ägandet handlar framför allt om kontroll över datarepresentation och förändringstakt. Det kräver inte en fysisk databasserver per tjänst. Logisk isolering genom separata scheman och behörigheter kan vara tillräcklig i vissa fall, medan högre säkerhets- eller tillgänglighetskrav kan motivera starkare separation. Separata databaser, scheman eller åtkomstområden kan användas, beroende på risker och plattformsval. En delad databasmotor kan fortfarande drivas centralt, men en gemensam motor får inte bli en genväg till täta kopplingar mellan tjänsternas tabeller.

Tänk att ärendetjänsten behöver visa filnamn, dokumenttyp och skapandedatum. Ärendetjänsten kan hämta uppgifterna från dokumenttjänstens API eller använda en egen läsmodell som uppdateras av publicerade händelser. Det behöver då vara tydligt vilken tjänst som är auktoritativ för respektive uppgift, särskilt om läsmodellen innehåller kopior. Den ska däremot inte i hemlighet bygga sin funktion på att en viss kolumn alltid finns i dokumenttjänstens databas. Om dokumenttjänsten då ändrar sitt schema kan den annars slå sönder ärendehanteringen trots att dess publika gränssnitt är oförändrat.

Tjänsteägarskap betyder heller inte att all information ska dupliceras överallt. Kopior kan vara motiverade för snabb läsning eller rapportering, men de innebär frågor om aktualitet, lagringsskydd, rättelse, gallring och vilka uppgifter som är auktoritativa.

## När en SQL-transaktion inte längre räcker

Anta att en handläggare bifogar ett dokument till ett ärende. Tidigare kunde backend skapa en dokumentpost och en kopplingspost inom samma databastransaktion. Efter uppdelningen utförs minst två logiska handlingar: dokumenttjänsten tar emot dokumentet, och ärendetjänsten registrerar kopplingen till ärendet. Om den ena handlingen lyckas och den andra misslyckas uppstår ett mellanläge.

En distribuerad arkitektur kan sällan förutsätta en gemensam, snabb och tillgänglig transaktion över alla berörda tjänster. Det är möjligt att använda samordnade transaktioner i vissa miljöer, men det medför egna beroenden och är inte en generell lösning. Ofta behöver man i stället utforma verksamhetsflödet så att delstegen kan slutföras, upprepas, kompenseras eller markeras för manuell hantering.

Även att spara information och publicera en händelse är två steg som kan skiljas åt av ett fel. Om dokumentposten sparas men händelsen aldrig skickas kan andra tjänsters vyer förbli inaktuella. Lösningen behöver därför säkra att avsedda händelser kan skickas även efter en omstart, exempelvis genom att lagra dem tillsammans med ändringen för senare publicering. Mottagaren behöver fortfarande hantera dubbletter.

En möjlig lösning för dokumentflödet är att dokumenttjänsten först tar emot filen och ger den ett identifierbart tillstånd, exempelvis *mottagen men ännu inte knuten till ärende*. Ärendetjänsten registrerar därefter kopplingen. Om kopplingen misslyckas kan flödet försöka igen, eller låta dokumentet ligga kvar i väntan på kontroll och eventuell borttagning enligt fastställda regler. Vilken ordning som är rätt beror på verksamhetens krav och risken för förlorade respektive felaktigt kopplade dokument.

**Kompensation** innebär inte att tiden vrids tillbaka. Ett redan skickat meddelande eller en gjord extern åtgärd kanske inte kan göras ogjord. Då behövs en ny, spårbar åtgärd som korrigerar resultatet. Systemet bör också kunna förklara för användaren om registreringen är klar, pågår eller kräver åtgärd. [R7](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga) [R8](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)

## Eventuell konsistens – ett medvetet avsteg från omedelbar samtidighet

Om ärendetjänsten har en egen lista över dokument kan den uppdateras genom en händelse från dokumenttjänsten. Listan blir då ibland tillfälligt inaktuell. Detta kallas ofta *eventuell konsistens*: förutsatt att uppdateringarna fungerar och inga nya förändringar sker kan kopiorna så småningom komma överens.

Detta kan vara acceptabelt för en söklista eller en översikt där en kort, överenskommen fördröjning saknar betydelse. Fördröjningen måste mätas och hanteras: eventuell konsistens anger inte i sig någon övre tidsgräns. Det kan vara oacceptabelt om handläggaren måste veta säkert att en handling har registrerats före en tidsfrist, eller om ett beslut får fattas endast när viss information har mottagits. Där krävs en tydlig källa till sanning och en verifierbar bekräftelse på det steg som är avgörande.

Här ligger en viktig arkitekturfråga: *vilka uppgifter måste vara korrekta just nu, och vilka får bli korrekta efter en viss fördröjning?* Svaret måste komma från verksamhetsreglerna. Teknikvalet får inte tyst ändra vad användaren kan lita på.

Beroende på meddelandesystemets och konsumenternas garantier kan meddelanden komma fram flera gånger eller behandlas i annan ordning än de skapades. Begreppet *idempotens* används för operationer där en upprepad begäran inte får skapa ytterligare affärseffekter. Konsumenter behöver därför kunna känna igen upprepade händelser och i relevanta fall hantera versioner eller ordning. Händelsebaserad synkronisering är inte en garanti för att systemet alltid konvergerar; mekanismer för upptäckt, ombearbetning och avstämning måste finnas. [R7](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga)

## Schemaändringar blir en del av tjänstens löpande leverans

När flera funktioner läser samma tabeller kräver en schemaändring ofta samordning av alla användare. Tjänsteägd data kan ge en mer självständig förändringstakt, men bara om den publika informationen hanteras stabilt. Ett internt fältnamn kan bytas utan att andra märker det; ett API-fält som konsumenter använder kan däremot behöva stödjas under en övergångsperiod.

Även inom en tjänst kan nya och gamla applikationsinstanser köra samtidigt vid driftsättning. Databasmigreringar behöver därför ofta ske stegvis: först läggs en kompatibel struktur till, sedan börjar tjänsten använda den och först senare tas den gamla bort. Man behöver också tänka igenom om en misslyckad release kan rullas tillbaka när datamodellen redan förändrats. En återgång av programkod är inte samma sak som en säker återgång av databasen.

Det innebär att applikationsteam och databasansvariga behöver ett gemensamt arbetssätt för riskbedömning, migrering, kapacitet och verifiering. Även om en automatisk databasbackup finns måste ansvar för återläsning och verksamhetsmässig avstämning vara uttryckligt; samordnad katastrofåterställning behandlas närmare i kapitel 17. Centrala regler kan fortfarande vara nödvändiga, men manuella databasköer för varje rutinändring kan bli ett hinder om många tjänster levereras självständigt. Automatisering, tydliga godkännanden och spårbara migreringar är ofta bättre än osynliga genvägar.

## Hur påverkas drift och förvaltning?

För driftläsaren är den viktigaste förändringen att *verksamhetsinformationen inte längre nödvändigtvis finns i en enda databas med ett enda återställningsögonblick*. Flera datalager, händelseströmmar och kopior kan behöva samverka. En databas kan vara tekniskt frisk medan användaren ser en gammal dokumentlista eller saknar ett registrerat dokument. Övervakningen behöver därför följa både tekniska resurser och informationsflöden – exempelvis växande köer eller uteblivna uppdateringar.

Det betyder inte att DBA-kompetensen blir mindre värdefull. Tvärtom behövs den för dimensionering, tillförlitlig databasdrift, indexering, säkerhetskonfiguration och vägledning om databasernas beteende. Skillnaden är att databastekniskt ansvar ofta behöver paketeras som en gemensam plattformsförmåga med tydliga tjänstegränser och självbetjäning där det är lämpligt.

För applikationsläsaren blir konsekvensen att informationsflödet över tjänstegränser är en del av funktionens korrekta beteende. Det räcker inte att spara data i den egna tjänsten. Teamet måste även veta vad som händer om ett meddelande fastnar, hur en dubblerad begäran hanteras och hur ett påbörjat arbetsflöde slutförs eller synliggörs.

Verksamhetens informationsansvariga måste samtidigt kunna bestämma bevarande, skydd, spårbarhet och kvalitet för informationen oavsett hur många tjänster som behandlar den. Skyldigheterna försvinner inte för att data kopieras till en ny läsmodell.

## Ett gemensamt beslut om dokumentinformationen

I vårt exempel fastställer verksamheten vilka uppgifter som utgör en registrerad handling, när registreringen räknas som klar och hur länge dokumentinformation ska bevaras. Dokumenttjänstens team ansvarar för sin datamodell, de publicerade kontrakten och hur registreringens olika tillstånd hanteras. Ärendetjänstens team ansvarar för att användaren får en begriplig status och för att en möjlig läskopia inte framställs som om den alltid vore aktuell. Databas- eller plattformsteamet tillhandahåller de tekniska mekanismer som lösningen behöver och följer upp deras drift.

Teamens ansvar överlappar i frågor som kräver gemensamma beslut. Ett exempel är hur länge en utebliven uppdatering får pågå innan en incident ska utlösas. Verksamheten anger konsekvenserna, applikationsteamen definierar informationens synliga tillstånd och driftfunktionen säkerställer att avvikelsen kan upptäckas och hanteras. Ansvar behöver dokumenteras på den nivån, inte bara med en rad som säger ”databasen – drift”.

## Från delad lagring till uttryckligt informationsansvar

Det avgörande skiftet är inte att varje mikrotjänst ska få sin egen databasserver. Det är att **informationens betydelse, tekniska representation och drift måste ha uttalade ansvariga**. När vi inte längre kan förlita oss på en gemensam transaktion eller en direkt SQL-fråga blir det viktigare att synliggöra mellanlägen, dataflöden och krav på aktualitet.

Det är först då självständiga tjänster kan förändras utan att verksamheten förlorar kontrollen över den information som gör IT-stödet användbart.

### Källor och vidare läsning

- **[R7](https://learn.microsoft.com/en-us/azure/architecture/patterns/saga)** Microsoft Learn, Saga distributed transactions pattern (åtkomst 2026-10-17).
- **[R8](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction)** Microsoft Learn, Compensating Transaction pattern (åtkomst 2026-10-17).
