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

