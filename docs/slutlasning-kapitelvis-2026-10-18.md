# Kapitelvis slutläsning – 18 oktober 2026

Underlag: main vid `3858f436db79e63d2b3cd62376d510162cb8f2da`, projektrevision 68. Hela manuskriptet läses i kapitelordning. Varje steg omfattar löptext, tabeller, sammanfattningar, övergångar och källavsnitt. Bedömning: begriplighet, teknisk precision, terminologi, båda läsarperspektiven och läsarfärdig text. Detta är en redaktionell slutläsning med riktad källkontroll, inte en ny heltäckande faktagranskning eller ett godkännande av ännu obearbetade PDF-/EPUB-exporter.

## Inledning – revision 69

- Förtydligat att självständig driftsättning förutsätter kompatibla gränssnitt och att felisolering inte följer automatiskt av tjänstegränser.
- Kompletterat läsanvisningen med hur boken kan användas vid första läsning och i gemensamma diskussioner.
- Målgrupp, förkunskaper, teknikneutralitet, fiktivt scenario och källavsnitt genomlästa; inga interna arbetsinstruktioner finns i inledningen.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 1. Det välbekanta IT-stödet – revision 70

- Rättat en otydlig syftning i definitionen av monolit och tonat ned ett obelagt generellt påstående om organisationers miljöer.
- Skilt mellan nätverksanrop till databasen och separata tjänsteanrop: en gemensam databas innebär inte att nätverket försvinner.
- Kontrollerat ansvarstabell, transaktionsresonemang, driftperspektiv, långsiktig förvaltning och övergången till dokumenttjänsten; den balanserade jämförelsen bevaras.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 2. Vad händer när systemet delas upp? – revision 71

- Skilt mellan en inkompatibel ändring och en faktiskt samordnad övergång; beskrivit parallellt stöd som ett möjligt sätt att genomföra övergången.
- Förklarat API vid första förekomsten för att stödja läsare från drift- och infrastruktursidan.
- Genomläst partiella fel, inventering, ansvar och jämförelsetabell. De korta tabellrubrikerna från föregående layoutkorrigering bevaras.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 3. Vem ansvarar för vad när systemet blir distribuerat? – revision 72

- Kopplat incidentberedskap till överenskomna tider i stället för att underförstå dygnet-runt-ansvar.
- Förklarat tjänsteupptäckt och timeout i det konkreta felscenariot; markerat att just den observerade felbilden gäller exemplet.
- Genomläst samtliga fyra ansvarsnivåer, fem ansvarsfrågor och ansvarstabellen; mandat, kontroll och skillnaden mot kapitel 18 är tydligt avgränsade.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 4. Hur ska systemet delas upp? – revision 73

- Preciserat invariantscenariot: en synkron kontroll skyddar inte ensam mot att underlaget ändras före beslutet; dokumentversion och uttryckliga mellanlägen konkretiserar avvägningen.
- Rättat formuleringen om interna modulanrop och använt observerbarhet konsekvent.
- Granskat alternativ A–C, bounded contexts, distribuerad monolit och beslutsprovet. Riktad kontroll 2026-10-18 av R3, https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis, stöder resonemanget om verksamhetsförmågor, sammanhållning och omprövbara gränser. Dokumentversionslösningen är bokens eget förklarande exempel, inte ett citat ur källan.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 5. Var ska tjänsterna köras? – revision 74

- Skilt mellan containeravbildning, körande container och tjänsteinstans; en instans kan omfatta samverkande containrar.
- Förtydligat att beständig lagring behöver uttalat informationsansvar, inte bara teknisk lagringskapacitet.
- Genomläst placeringsalternativ, felområden, skalning och hälsokontroller. Riktad primärkällkontroll 2026-10-18: https://kubernetes.io/docs/concepts/workloads/pods/ och R4 om probes. Den teknikneutrala framställningen och reservationerna om isolering och återställning bevaras.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 6. Hur kommunicerar tjänsterna? – revision 75

- Rättat ett sakligt missvisande motsatspar: ett framgångsrikt API-svar kan innehålla en korrekt tom lista; det är maskering av fel som ska undvikas.
- Förklarat idempotens och preciserat att ett operations-ID kräver faktisk hantering av dubbletter och en bestämd giltighetstid.
- Genomläst synkron/asynkron kommunikation, säkerhetskontroller, ansvarstabell och scenariots lösning. Riktad kontroll 2026-10-18 mot R6 och AWS Builders Library, https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/. Ersatt ett oförklarat matrisnamn med ansvarsmatris.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 7. Vem ansvarar för informationen? – revision 76

- Rättat en syftning om ärendetjänstens läsmodell och språkformen verksamhetsinformation.
- Kompletterat glappet mellan lagrad data och publicerad händelse med en kort, teknikneutral beskrivning av beständig publiceringsavsikt; behovet av dubbletthantering kvarstår.
- Genomläst informationsansvar, isolering, mellanlägen, kompensation, eventual consistency och migrering. Riktad kontroll 2026-10-18 mot R7 och AWS Prescriptive Guidance, https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html. Det tillagda felscenariot är en förklaring av tillförlitlig händelsespridning, inte ett löfte om exakt-en-gång-leverans.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 8. Hur förändras utvecklingsmiljöerna? – revision 77

- Låtit exemplet gälla dokumenttjänstens egen namnvalidering i stället för en presentationsregel som kunde uppfattas höra till frontend.
- Rättat den sammanblandade formuleringen om konfiguration och hemligheter: okänslig konfiguration kan versionsstyras, autentiseringshemligheter ska hanteras separat.
- Genomläst testdubblar, reproducerbarhet, isolering, syntetiska testdata och rollfördelning. Tagit bort ett överflödigt därför i övergången till kapitel 9.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 9. Hur förändras testmiljöer och kvalitetssäkring? – revision 78

- Rättat kontinuitetsfelet: kapitel 8 låter dokumentteamet simulera ärendetjänsten, inte tvärtom.
- Nyanserat jämförelsen så att integrationsfel inte framställs som unika för mikrotjänster.
- Förtydligat att frivilliga svarsfält inte automatiskt är kompatibla med alla klienter. Genomläst testnivåer, versionskombinationer, data, miljöisolering och acceptanskriterier; standardiserat stavningen dubbletter.
- Utfall: genomläst; 4 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 10. Hur levererar vi förändringar utan att störa helheten? – revision 79

- Förklarat CI och kontinuerlig leverans samt skillnaden mellan leveransberedskap och beslut om produktionssättning.
- Samordnat konfigurationsbeskrivningen med kapitel 8 och skilt programåtergång från återställning av körande container eller data.
- Rättat scenariots hänvisning till ett äldre fält som inte tidigare introducerats; avvecklingen gäller nu det äldre kontraktet.
- Genomläst stegvis utrullning, händelsekonsumenter, rollback/roll-forward, mandat och produktionsuppföljning. Inga löften om riskfri driftsättning införs.
- Utfall: genomläst; 4 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 11. Vem tillhandahåller miljöer och gemensamma förmågor? – revision 80

- Stramat upp den dubblerade beskrivningen av plattformskontrakt utan att ta bort ansvar, support eller versionslöften.
- Samordnat de två instanserna med placeringsbeslutet i kapitel 5.
- Skilt den deklarativa modellen i exemplet från det bredare begreppet infrastruktur som kod. Genomläst plattformserbjudande, självbetjäningsramar, databasansvar och plattformens egen förvaltning.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 12. Vad händer när en tjänst slutar fungera? – revision 81

- Skilt begäran om arbete från händelser om redan inträffade förändringar i det asynkrona exemplet.
- Förtydligat readiness-kontrollen så att den inte förväxlas med organisatorisk beredskap.
- Rättat vilka delar som upprepas vid återförsök: det är begäranden som kan ge dubbel verksamhetseffekt när svar uteblir. Genomläst timeout, återförsök, circuit breaker, resursisolering, kölagring och säker degradering.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 13. Hur vet vi att hela IT-stödet fungerar? – revision 82

- Rättat en trasig mening om spår och loggar som saknade både inledande versal och hjälpverb.
- Förklarat percentil med registreringstid som konkret exempel och förtydligat att en tidsgräns överskrids.
- Använt observerbarhet konsekvent. Genomläst korrelation, SLI/SLO/SLA, asynkron status, syntetiska kontroller, larm, sampling, känsliga logguppgifter och plattformens egna avbrott. Kapitlets tidigare layoutanpassade avslut har inte byggts ut.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 14. Hur felsöker och hanterar vi incidenter? – revision 83

- Lagt till att uteblivna loggposter också kan bero på fel i loggning eller insamling; de bevisar inte var anropet stoppades.
- Samordnat åtgärdsförslaget med kapitel 6 och 9: faktisk tjänsteanslutning prövas i integrationstest, inte enbart kontraktstest.
- Rättat två språkformuleringar. Genomläst verksamhetsprioritering, incidentmandat, säkra återställningsbeslut, beredskap, kommunikation och efteranalys; inget utökat produktionsmandat eller universellt jourkrav införs.
- Utfall: genomläst; 4 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 15. Hur skyddar vi systemet och dess information? – revision 84

- Skilt signerade JWT från ogenomskinliga token; JWT-specifika verifieringsråd ska inte läsas som att alla token har samma format.
- Skilt planerad rotation med möjlig överlappning från akut spärr vid röjda uppgifter.
- Riktad källkontroll 2026-10-18 mot R17 (objektspecifik auktorisation) och R18 (JWT-verifiering och mottagarkontroll). Genomläst delegering, tjänsteidentiteter, signerade länkar, skydd av kopior och säkerhetsincidenter. Inga rättsliga tidsfrister eller ogrundade efterlevnadslöften införs.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 16. Hur hanterar vi livscykler, underhåll och teknisk skuld? – revision 85

- Förklarat SBOM och ersatt runtime-versioner med en svensk beskrivning av språkens körmiljöer.
- Skilt genomförd åtgärd från bedömning av kvarstående risk i förvaltningssamtalet.
- Genomläst samtidiga livscykler, patchningsansvar, transitiva beroenden, faktisk produktionsversion, kompatibilitet och avveckling; framställningen lovar inte att inventering eller sårbarhetsskanning ensamt ger säkerhet.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 17. Hur säkerställer vi återställning, kontinuitet och kostnadskontroll? – revision 86

- Förtydligat att mätning av återställningstid behöver definierade start- och slutpunkter.
- Preciserat att tätare kopiering inte ensam ger noll dataförlust och att skyddet måste knytas till bekräftade mottaganden, filer, metadata och definierade felscenarier.
- Begränsat slutsatsen av en återställningsövning till vad den faktiskt prövat. Genomläst kopior/repliker, återuppspelning, sidoeffekter, avstämning, prioriteringsordning och kostnadsavvägningar. Riktad kontroll 2026-10-18 av R20:s publiceringspost och kontinuitetsinriktning; ingen ny heltäckande standardgranskning påstås.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 18. Hur organiserar vi ansvar och styrning över tid? – revision 87

- Samordnat ansvarsmodellen med kapitel 3: säkerhets- och informationskrav är fortsatt tvärgående uppdrag, och helhetssamordningen beskrivs utan en missvisande sifferrubrik.
- Rättat sammansättningen plattforms- och driftansvar och tagit bort ett oförklarat ramverksnamn.
- Genomläst mandat, undantag, finansiering, gemensamma mål, incidentuppföljning, leverantörsgränser och överlämning när team upphör. Avgränsningen mot den praktiska incidenthanteringen bevaras.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 19. Hur lever vi med gamla och nya arkitekturer samtidigt? – revision 88

- Skilt oavsiktligt permanentade övergångslösningar från en medvetet vald, varaktig kombination av monolit och tjänster. Det följer bokens princip att hela monoliten inte måste ersättas.
- Ersatt ett generellt krav på tidsbundet mellanläge med omprövning, avvecklingskriterier och tydligt beslut om bestående delar.
- Genomläst strangler-mönstret, översättningslager, etappvis dataägarskap, dubbla skrivningar, cutover, säkerhet, blandade versioner och avvecklingsprov. Rättat en saknad konjunktion.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## 20. När är mikrotjänster rätt väg? – revision 89

- Samordnat nyttan med separat dokumenttjänst med kapitlets tidigare avvägning: skalning av lagring ensam kräver inte att domänlogiken bryts ut.
- Rättat böjningen ändrade arbetssätt.
- Genomläst hela slutkapitlet inklusive beslutsfrågor, alternativ, kostnader, stegvis prövning och slutord. Avslutningen återknyter till båda målgrupperna och rekommenderar inte fler tjänster som självändamål.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – Inledning – revision 90

- Sammanhållen efterkontroll av ändringarna: tagit bort ett upprepat men i samma stycke.
- Utfall: genomläst; 1 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 1. Det välbekanta IT-stödet – revision 91

- Sammanhållen efterkontroll: förklarat DBA vid första förekomsten i ansvarstabellen.
- Utfall: genomläst; 1 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 7. Vem ansvarar för informationen? – revision 92

- Sammanhållen efterkontroll: gjort även den efterföljande syftningen till ärendetjänsten uttrycklig.
- Utfall: genomläst; 1 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 12. Vad händer när en tjänst slutar fungera? – revision 93

- Sammanhållen efterkontroll: förenklat meningen om kontrollen av trafikberedskap.
- Utfall: genomläst; 1 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 16. Hur hanterar vi livscykler, underhåll och teknisk skuld? – revision 94

- Sammanhållen efterkontroll: rättat kongruensen efter ändringen till en programvaruförteckning i singular.
- Utfall: genomläst; 1 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## Samlad efterkontroll och källregister

- Samtliga 21 manusdelar har lästs i ordning, med 59 riktade justeringar i första genomgången och fem mindre rättningar vid gemensam efterkontroll. Varje kapitelsteg har egen commit och egen integritetsverifierad projektrevision.
- Inledning, tabeller, övergångar, slutord och samtliga källavsnitt ingår. Granskningen hittade både språkliga fel och tekniska precisionsproblem, inte bara formalia.
- Målgrupp, omfattning, kapitelordning, omslag och befintliga käll-ID har bevarats. Inga interna illustrationer eller nya kapitel har skapats.
- Källregistret har lästs och kapitelkolumnen rättats för källor som förekommer i flera kapitel. R1 hör till inledningen och kapitel 1, 2 och 4; R2 till kapitel 2 och 3. Övriga poster har också stämts av.
- Den nya förklaringen om ogenomskinliga token har kompletterande primärkällstöd i IETF RFC 7662, https://www.rfc-editor.org/rfc/rfc7662.html, kontrollerad 2026-10-18. Distinktionen kontinuerlig leverans/automatisk produktionssättning har kontrollerats mot R11 samma datum.
- Sökning efter separat rubricerade redaktionella granskningsavsnitt, TODO/FIXME och formuleringarna ”inför publicering” respektive ”det fortsatta bokarbetet” gav inga träffar i de exporterade manuskapitlen. Kontextuell slutläsning har också utförts; legitim vägledning till läsaren och organisationen har bevarats.
- README, projektstatus, projektindex och bokspecifikation har uppdaterats; historiska arbetsnoteringar och granskningsprotokoll har bevarats och märkts som historik.
### Efterkontroll – 11. Vem tillhandahåller miljöer och gemensamma förmågor? – revision 95

- Provexportens korta kapitelavslut har åtgärdats genom att koncentrera två upprepande slutstycken. Samtliga sakkrav om undantag, resursgränser, självständighet och plattformskontrakt bevaras.
- Utfall: genomläst; 2 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 17. Hur säkerställer vi återställning, kontinuitet och kostnadskontroll? – revision 96

- Provexporten gav en sida med enbart källrubrik och R20. Tre upprepande stycken har koncentrerats utan att ta bort återställningskrav, nyckelberoenden, användarinformation eller begränsningen till prövade scenarier. Omexport används för att kontrollera att källposten ryms med kapitelavslutet.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

### Efterkontroll – 11. Vem tillhandahåller miljöer och gemensamma förmågor? – revision 97

- Andra layoutprovet visade att R12/R13 fortfarande låg på en egen sida. Tre upprepande förklaringar har koncentrerats med bevarade krav på plattformens erbjudande, gränssnitt, ägarskap och kvalitetsuppföljning.
- Utfall: genomläst; 3 riktade textjusteringar. Befintliga käll-ID och kapitelavgränsning bevarade.

## Slutlig verifiering – revision 98

| Kontroll | Resultat | Omfattning/begränsning |
|---|---|---|
| Kapitelvis slutläsning | Genomförd | Inledning och kapitel 1–20 i ordning; efterkontroll och koncentration efter provexport i revision 90–97 |
| Projektstruktur | Godkänd | Projektets validate_project.py |
| Referensvalidering | Godkänd | 21 manusdelar, 23 käll-ID, 21 unika URL:er; samma URL kan ha flera befintliga käll-ID |
| Python-syntax och Git-diff | Godkända | Befintliga skript kompilerar; inga whitespacefel i slutdiffen |
| Redaktionella arbetsnoteringar | Inga kvarvarande fynd | Full slutläsning plus avgränsad mönstersökning av exporterade manusdelar |
| Provexport | Godkänd | Befintlig build_book.py, Pandoc 3.1.11.1, XeLaTeX, TeX Gyre Pagella; ingen ändring av exportkoden |
| PDF-struktur | Godkänd | 144 sidor, 21 bokmärken, titel/författare/undertitel/version ifyllda |
| PDF-geometri och text | Godkänd automatiskt | 170 × 240 mm; inga extraherade textspann utanför sidan, inga ersättningstecken |
| PDF-kapitelstarter och tabeller | Visuellt granskade | Renderade kapitelstarter för inledning och alla 20 kapitel; tabeller i kapitel 1, 2, 3 och 6; omslag och innehållsförteckning. Efter sista omexporten kontrollerades ändrade kapitel 11 och 17 på nytt. Inte en visuell granskning av samtliga 144 sidor. |
| Korta källsidor | Rättade och återkontrollerade | Inga inlagessidor med mindre än 350 texttecken; ingen inlagessida börjar nu med enbart källrubriken. Källorna till kapitel 11 och 17 ligger tillsammans med respektive avslut. |
| EPUB-struktur | Godkänd | ZIP CRC, manifest/spine och interna länkmål; 24 XHTML-dokument, 48 interna länkar; nav är inte en vanlig lässida |
| EPUB-navigation och rubriker | Godkända strukturellt | 21 TOC-poster i kapitelordning; 20 kapitel med separata nummer-/titelspann och CSS för blockvis visning |
| Källor i provexporterna | Godkända strukturellt | Samtliga 21 käll-URL:er finns som externa länkar i både PDF och EPUB; alla URL:ers aktuella tillgänglighet har inte testats på nytt |
| Integritet och paketering | Godkända | Manifestkontroll samt verifiering av committade revisionssnapshots; komplett projektarkiv testat för CRC och filöverensstämmelse |

### Kvar inför publiceringsbeslut

- Granska den samlade PR:en och CI-resultatet.
- Öppna den nya EPUB-utgåvan i en faktisk läsare, exempelvis Apple Böcker, och kontrollera navigation, kapitelrubriker och läsflöde. Strukturell kontroll ersätter inte det läsprovet.
- Bedöm PDF-tabellernas läsbarhet i avsedd bokstorlek och gör ett sista läsarprov av de faktiska leveransfilerna. Layouten har kontrollerats i specificerade stickprov, inte sida för sida.
- Ta ställning till publiceringsgodkännande och avsedd läsarversion. Ingen release eller publicering har utförts; vid release styr taggen versionsmetadata.

Den redaktionella restpunkten A4 i den tidigare leveransgranskningen är åtgärdad i den omfattning som redovisas här. Tidigare avgränsningar av faktagranskningen och kraven på faktiska läsarprov gäller fortsatt.

### Checksummor för de lokalt verifierade provfilerna

```text
bca10244484ab4bb6d3aa14670089e6aead41d8be806ed796407adc7241a2470  fran-monolit-till-mikrotjanster.epub
b6d1eb41ee6b0d8efa4f157c915205c36469c8f3cb495d0a62c74f59607d86ab  fran-monolit-till-mikrotjanster.pdf
```
