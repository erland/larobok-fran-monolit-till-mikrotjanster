# 10. Hur levererar vi förändringar utan att störa helheten?

En ny version av dokumenttjänsten är klar. Den kan lagra fler uppgifter om dokumenten, men den nuvarande ärendetjänsten förväntar sig det gamla svaret. I ett traditionellt IT-stöd hade verksamheten kanske planerat en gemensam release där backend, databas och användargränssnitt uppdaterades samtidigt. Nu vill dokumentteamet gå vidare utan att invänta alla andra team. Går det att göra utan att riskera ärendehandläggarnas arbete?

Svaret beror inte i första hand på hur snabbt vi kan starta en ny container. Det beror på om vi har utformat **förändringen, kontrakten, driftsättningen och återhämtningsförmågan** så att flera versioner kan fungera samtidigt. Oberoende leveranser är en möjlighet, inte ett löfte som automatiskt följer av att en applikation delats upp.

## Från gemensam release till flera förändringstakter

I den traditionella miljön har ett ändringsärende ofta omfattat hela systemet. Utveckling levererar ett samlat paket, test verifierar en bestämd kombination och drift genomför installationen vid ett avtalat tillfälle. Modellen ger en tydlig helhetskontroll, men kan innebära att små ändringar får vänta på stora.

I mikrotjänstmiljön kan ett team leverera dokumenttjänsten medan andra tjänster förblir oförändrade. Det gör det möjligt att minska förändringens storlek och snabbare rätta fel. Samtidigt är den driftsatta helheten en kombination av flera versioner, ofta utan ett enda versionsnummer som beskriver allt. Drift, förvaltning och incidentledning måste därför kunna se **vilken version av vilken tjänst som körs var**, vilka kontrakt den använder och vilka förändringar som nyligen genomförts.

Målet är inte att alla team måste driftsätta varje dag. Målet är att en förändring ska kunna genomföras när den är tillräckligt säker, utan omotiverade beroenden till andra förändringar. [R11](https://martinfowler.com/bliki/ContinuousDelivery.html)

## En leveranskedja som kan upprepas och granskas

En hållbar leverans börjar innan någon trycker på knappen för driftsättning. Källkod och konfiguration versionshanteras. Bygget ger en identifierbar artefakt som testas, kontrolleras och helst förs vidare oförändrad genom miljöerna. Om samma källa byggs om med andra beroenden vid produktionstillfället är det svårare att veta om man verkligen driftsätter det som testats.

En automatisk leveranskedja (CI/CD) kan exempelvis kontrollera kod, beroenden och sårbarheter, köra relevanta tester, paketera artefakten, dokumentera resultatet och tillämpa de godkännanden som krävs för produktion. Det betyder inte att alla kontroller ska vara automatiska. En verksamhetskritisk ändring kan behöva särskild riskbedömning eller ett tidsatt beslut. Skillnaden är att kontrollerna kan göras **spårbara och återkommande**, i stället för att bero på manuellt återkommande installationssteg.

Även leveranskedjans egna behörigheter, byggberoenden och skyddsmekanismer behöver granskas. Ett godkänt automatiserat flöde innebär inte att varje förändring är riskfri.

Det ska gå att besvara: Vem begärde förändringen? Vad har byggts? Vilka verifieringar passerade? Vilken konfiguration används? Vem godkände produktionssättningen? Vilka tjänster kan påverkas? Hur följs resultatet upp? Dessa uppgifter bör kunna knytas till både ändringen och den faktiska körmiljön.

## Bakåtkompatibilitet är förutsättningen för självständighet

Vi återvänder till dokumenttjänsten. Den nya versionen inför ett nytt fält för dokumentklassificering. Ett säkert första steg kan vara att **lägga till** fältet utan att ta bort något som ärendetjänsten behöver. Dokumenttjänsten börjar stödja både gamla och nya konsumenter. Därefter kan ärendetjänsten uppdateras. Först när ingen längre använder det gamla kontraktet är det lämpligt att avveckla det.

Detta brukar beskrivas som *expandera – migrera – dra tillbaka*. Samma tanke behövs vid databasförändringar: ett nytt schema kan behöva stödja både tidigare och ny applikationsversion under en övergångstid. En ändring som direkt tar bort en kolumn eller byter betydelse på ett fält kan bryta äldre instanser, även om den nya versionen har passerat sina egna tester.

Kompatibilitet måste bedömas utifrån beteende, inte bara datatyper. Ett API som returnerar samma fält men med ändrad betydelse kan vara lika problematiskt som ett borttaget fält. För asynkrona händelser gäller motsvarande krav för producenter och konsumenter, även när meddelanden ligger kvar i köer efter en driftsättning.

Ibland går en förändring inte att göra bakåtkompatibel. Då behöver beroendena kartläggas och en samordnad migrering beslutas. Självständig driftsättning innebär inte att samordning är förbjuden, bara att den används när den faktiskt behövs.

## Att rulla ut utan att byta allt på en gång

En ny version kan ersätta den gamla vid ett enda tillfälle, men det kan innebära ett avbrott. Det finns också gradvisa strategier. Vid **rullande uppdatering** byts instanser stegvis, förutsatt att kapacitet och kompatibilitet räcker under övergången. Med **blue–green** finns två uppsättningar och trafiken kan flyttas mellan dem. Med **canary** får en mindre del av trafiken först gå till den nya versionen medan man följer relevanta signaler.

Strategierna löser olika problem. Blue–green kan ge en tydlig trafikväxling men kräver extra kapacitet och hantering av gemensamma data. Canary ger möjlighet att observera effekter på begränsad trafik, men en andel HTTP-anrop styr inte automatiskt vilka instanser som behandlar meddelanden i köer. För asynkrona konsumenter och gemensamma data krävs därför en särskild strategi för införande och återgång. En rullande uppdatering kräver att gammal och ny version verkligen kan samexistera.

Ingen utrullningsmodell garanterar att verksamheten slipper påverkan. För dokumenttjänsten behöver man exempelvis följa både tekniska fel och om dokument faktiskt går att registrera och hämta. En låg felfrekvens i webbservern är inte tillräcklig om dokumenten inte visas i ärendena.

## Rollback är inte alltid att backa bandet

Om den nya dokumenttjänsten ger fel vill vi snabbt kunna återgå till den tidigare programversionen. Men vad händer om den nya versionen redan har ändrat databasens struktur eller skickat nya händelser? Att återställa en äldre container gör inte dessa förändringar ogjorda. En tidigare version kanske inte ens kan läsa de nya uppgifterna.

Därför behöver beslut om **rollback eller roll-forward** ingå i förändringens design. Teamen behöver i förväg bestämma vad som kan återställas, vilka mätvärden som ska utlösa ett stopp och vem som får fatta beslut om att avbryta införandet. Rollback kan vara lämpligt när gränssnitt och data fortfarande är kompatibla. Roll-forward innebär att felet rättas genom en ny framåtriktad ändring. Vid vissa datamigreringar behövs särskilda återställnings- eller kompensationsåtgärder. Att återläsa en databas är ett annat, större ingrepp som även kan påverka andra tjänster och dataägare.

Förberedda skyddsmekanismer, som funktionsflaggor eller möjlighet att stoppa en ny funktion, kan ibland ge snabbare riskbegränsning än att byta hela programversionen. De kräver i sin tur ansvar för flaggornas livscykel och säkra grundvärden. [R11](https://martinfowler.com/bliki/ContinuousDelivery.html)

## Förändringsstyrning när leveranserna är många

Traditionell förändringshantering har ofta haft fokus på att granska en samlad systemrelease. I en distribuerad miljö kan antalet mindre driftsättningar bli betydligt större. Om varje rutinändring måste hanteras med samma manuella process riskerar styrningen att bli ett hinder utan att öka säkerheten.

Ett alternativ är att skilja **förhandsgranskade standardförändringar** med låg och välkänd risk från förändringar som behöver särskilt godkännande. Automatisk dokumentation av byggen, tester, konfiguration och produktionssättning kan ge bättre revisionsspår än manuellt ifyllda checklistor. Men förutsättningen är att det finns tydliga kriterier för vilka förändringar som får gå genom vilken väg, och att avvikelser verkligen fångas upp.

Här möts applikations- och driftperspektivet. Applikationsteamet kan bedöma beteende, kompatibilitet och funktionella risker. Drift- och plattformsteam kan bedöma kapacitet, utrullningsmetod, teknisk återhämtning och påverkan på gemensamma beroenden. Säkerhetsfunktionen anger nödvändiga kontroller. Verksamhetsansvariga behöver kunna avgöra när en funktionell förändring innebär särskild verksamhetsrisk.

## Vem får göra vad i produktion?

Att en teknisk plattform erbjuder självbetjänad driftsättning betyder inte att varje utvecklare automatiskt ska ha obegränsad produktionsbehörighet. Åtkomst, godkännanden och ansvar behöver utformas efter risk och organisationens styrmodell.

En möjlig uppdelning är att applikationsteamet ansvarar för leveransbarhet, kontrakt, tester och tydliga driftkrav. Plattformsteamet ansvarar för en säker och reproducerbar leveransväg, åtkomstmekanismer och övervakning av plattformens funktion. Driftorganisationen kan ansvara för övergripande produktionsberedskap, förändringssamordning och incidentledning. I en annan organisation kan samma produktteam bära en större del av det operativa ansvaret. Det viktiga är att **mandat och skyldigheter motsvarar varandra**.

Produktionsbehörigheter bör begränsas till det som uppgiften kräver. Automatiska leveransidentiteter behöver egna kontroller och spårbarhet, liksom undantagsåtkomst vid incidenter.

Före driftsättning behöver det exempelvis vara bestämt vem som kan avbryta en utrullning, vem som fattar beslut vid försämrade verksamhetssignaler och vem som ansvarar för kommunikationen om användarna påverkas. Efter driftsättning behövs en överenskommen period eller metod för uppföljning, inte bara ett grönt statusmeddelande från leveransverktyget.

## En förändring i ärendehanteringssystemet

Dokumentteamet vill driftsätta klassificeringsfältet innan ärendeteamet har hunnit uppdatera sin vy. Teamen kommer överens om att dokumenttjänsten först accepterar och returnerar den gamla representationen, samtidigt som den nya representationen kan aktiveras separat. Databasändringen görs additivt. Det finns en plan för när det äldre fältet senare får avvecklas.

En ny artefakt byggs och verifieras. Teamen har i förväg bestämt när den standardiserade förändringsvägen är tillräcklig och när ett särskilt godkännande krävs. Plattformens leveransflöde rullar ut den till en begränsad del av trafiken. Under införandet följer teamen både tekniska fel och om handläggare kan lägga till och öppna dokument. Om något försämras kan den nya funktionen stängas av utan att den gemensamma dokumenthanteringen behöver tas ur drift. Det är ett valt scenario: i verkligheten behöver även händelseflöden, last och datamigrering analyseras innan en liknande metod väljs.

Den viktiga vinsten är inte att uppdateringen sker snabbare, utan att **risken är begränsad, förändringen spårbar och ansvaret tydligt**. Dokumentteamet kan leverera utan att invänta en fullständig systemrelease, samtidigt som driftsidan har möjlighet att förstå, följa och ingripa i vad som händer i produktion.

## Det som faktiskt förändras

I en monolit är det ofta möjligt att pröva och driftsätta en samlad version. I ett distribuerat IT-stöd är leveransförmågan en del av arkitekturen: varje tjänst måste tåla att andra tjänster under en period kör andra versioner, och driftmodellen måste kunna hantera många mindre förändringar utan att tappa helhetskontrollen.

**Oberoende förändring är därför ett gemensamt resultat av kompatibel applikationsdesign, reproducerbar teknisk leverans och tydlig verksamhetsstyrning.** Nästa kapitel behandlar de gemensamma plattformsförmågor som gör detta möjligt i praktiken.

### Källor och vidare läsning

- **[R11](https://martinfowler.com/bliki/ContinuousDelivery.html)** Martin Fowler, Continuous Delivery (kontrollerad 2026-10-17).
