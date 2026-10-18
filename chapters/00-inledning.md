# Inledning

Ett IT-stöd kan se enkelt ut från användarens perspektiv. En handläggare öppnar ett ärende, läser dokument, fattar beslut och skickar ett meddelande. Bakom detta finns emellertid en lång rad tekniska och organisatoriska förutsättningar: applikationer måste samverka, data måste vara tillförlitliga, nätverket måste fungera och någon måste kunna upptäcka och avhjälpa fel.

I ett traditionellt system är mycket av detta samlat. Frontend, backend och databas ingår ofta i en gemensam installation eller åtminstone i en samordnad livscykel. Det finns kända servrar och miljöer, etablerade driftinstruktioner och ofta en tydlig väg från ändringsbeställning till driftsättning. Även när många personer och leverantörer är inblandade finns det ett system att peka på.

När samma verksamhetsstöd delas upp i mikrotjänster förändras förutsättningarna. Funktioner som tidigare anropade varandra inom samma applikation kan behöva kommunicera över nätverk. Information som tidigare uppdaterades i en gemensam databas kan ligga under olika tjänsters ansvar. Tjänster kan driftsättas och uppgraderas var för sig när deras gränssnitt är kompatibla. De kan också sluta fungera var för sig, men fel kan spridas genom beroenden mellan dem. Men användaren förväntar sig fortfarande att *ärendehanteringen* fungerar som en helhet.

Det är denna förskjutning boken handlar om: **från en samordnad applikation till en distribuerad lösning som fortfarande måste leverera ett sammanhållet IT-stöd**.

## Två utgångspunkter, samma helhet

Boken vänder sig till två grupper av erfarna läsare. Den ena kommer från applikationssidan: systemutveckling, applikationsarkitektur, test, integrationer eller applikationsförvaltning. Den andra kommer från driftsidan: server- och virtualiseringsdrift, nätverk, databasadministration, IT-säkerhet, plattformar, övervakning eller teknisk förvaltning. De två grupperna kan redan arbeta nära varandra, och i vissa organisationer tillhör de samma team.

Du behöver inte behärska den andra gruppens hela yrkesområde. Däremot behöver du förstå varför dina egna beslut påverkar andra delar av organisationen. En ny tjänstegräns kan skapa nya kommunikationsvägar och nätverksregler. En ny driftplattform kan förändra hur applikationer måste hantera konfiguration, fel och övervakning. Ingen av dessa förändringar kan beskrivas rättvisande som enbart en utvecklings- eller driftfråga.

## Vad boken inte förutsätter

Du förväntas känna till hur ett traditionellt IT-stöd utvecklas eller förvaltas, men inte ha byggt mikrotjänster tidigare. Centrala begrepp introduceras när de behövs. Boken är inte en programmeringshandledning och inte heller en manual för Kubernetes, molntjänster eller en viss leverantörs produkter.

Mikrotjänster kräver varken containrar, en viss molnplattform eller en bestämd teamorganisation. Sådana lösningar förekommer ofta eftersom de kan underlätta automatisering och oberoende leveranser. De är ändå val, inte definitionen av arkitekturen. Boken skiljer därför på konsekvenserna av ett distribuerat system och på lösningar som en organisation väljer för att hantera konsekvenserna.

## Ett ärendehanteringssystem som följer med

Genom boken följer vi ett fiktivt ärendehanteringsstöd. I utgångsläget har det en frontend, en backend och en gemensam relationsdatabas. Miljöerna är relativt förutsägbara: utveckling, test och produktion, med en uppsättning virtuella maskiner och tydliga driftkontakter.

Verksamheten växer. Dokumenthantering, notifieringar, beslut och partsinformation får nya krav och olika förändringstakt. Organisationen överväger att bryta ut funktioner till självständiga tjänster. För varje steg undersöker vi vad som förändras i programvaran, infrastrukturen och ansvarsfördelningen. Exemplet är avsiktligt förenklat; inga detaljer ska uppfattas som ett påstående att alla organisationer bör välja samma arkitektur.

## Hur boken är upplagd

Först etableras vad vi menar med ett traditionellt IT-stöd och med mikrotjänster. Därefter behandlas hur funktioner delas upp, var de körs, hur de kommunicerar och hur dataansvar fördelas. Vi följer förändringen genom utvecklings- och testmiljöer, leverans, övervakning, incidenthantering och långsiktig förvaltning. Till sist samlas frågorna om styrning, ansvar och valet mellan olika arkitekturer. Läs gärna boken i ordning första gången. Vid senare läsning kan du använda enskilda kapitel som underlag för gemensamma diskussioner mellan applikations- och driftorganisationen.

En återkommande jämförelse visar vad som var bekant tidigare, varför förutsättningarna förändras, vilka alternativa lösningar som finns och vem som behöver ansvara för vad. Ansvar delas upp i att ställa krav, fatta beslut, genomföra, sköta driften och följa upp resultat; det är inte alltid samma funktion som gör allt. Den som kommer från applikationssidan får se driftens konsekvenser av arkitekturbesluten. Den som kommer från driftsidan får se hur applikationens egenskaper avgör vad som faktiskt går att drifta säkert och effektivt.

Syftet är inte att övertyga dig om att mikrotjänster alltid är bättre. En välstrukturerad monolit kan vara både enklare, billigare och säkrare att förvalta. Syftet är att ge underlag för bättre beslut när självständiga tjänster är aktuella – och för bättre samarbete oavsett vilken arkitektur som väljs. [R1](https://martinfowler.com/articles/microservice-trade-offs.html)

### Källor och vidare läsning

- **[R1](https://martinfowler.com/articles/microservice-trade-offs.html)** Martin Fowler, *Microservice Trade-Offs* (2015).
