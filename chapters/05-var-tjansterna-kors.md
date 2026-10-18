# 5. Var ska tjänsterna köras?

När dokumenthanteringen i vårt ärendehanteringssystem bryts ut uppstår en fråga som tidigare ofta hade ett enkelt svar: vilken server eller virtuell maskin ska köra den nya delen? En separat tjänst behöver inte en separat VM. Däremot behöver den en tydligt beskriven körmiljö, resurser och ansvar för att fungera säkert och tillförlitligt.

Den här skillnaden är central. Mikrotjänstarkitektur syftar till att göra avgränsade verksamhetsfunktioner möjliga att utveckla och leverera relativt självständigt. Det är en möjlighet som måste understödjas av tjänstegränser, kontrakt och leveransförmåga, inte en automatisk garanti. Det avgör däremot inte automatiskt om de ska köras på virtuella maskiner, i containrar, på en orkestreringsplattform eller som hanterade tjänster. Valet måste följa behovet, inte tvärtom.

## Tjänst, instans och körmiljö är tre olika saker

En *tjänst* är en logisk förmåga med definierade funktioner och kontrakt. En *instans* är en körande kopia av tjänstens program. En *körmiljö* är den tekniska resurs som bär instansen, till exempel en VM, en container på en värd eller en hanterad exekveringstjänst. Samma tjänst kan ha flera instanser; en VM kan samtidigt bära flera tjänsters instanser. En container kör processer i en avgränsad miljö med utgångspunkt i en containeravbildning som paketerar program och beroenden. En tjänsteinstans kan bestå av en eller flera samverkande containrar. Container, tjänsteinstans och fysisk eller virtuell värd är därför inte utbytbara begrepp.

I det traditionella ärendehanteringssystemet kan frontend ligga på en VM, backend på två VM:ar bakom en lastbalanserare och databasen på en särskild databasplattform. VM-indelningen följer då ungefär de tekniska lagren. När dokumenttjänsten bryts ut behöver man i stället fråga vilka krav den har på kapacitet, isolering, tillgänglighet och förvaltning. Antalet mikrotjänster bestämmer inte antalet VM:ar.

## Fyra vanliga alternativ

**En VM per tjänst.** Detta liknar en välbekant driftmodell. Operativsystem, behörigheter och underhåll kan avgränsas tydligt, men tjugo tjänster kan innebära många operativsystem, uppdateringar och övervakningsobjekt. Hög tillgänglighet kan dessutom kräva mer än en VM för samma tjänst.

**Flera tjänster på en VM.** Det kan vara resurssnålt, särskilt vid liten belastning. Samtidigt delar tjänsterna kapacitet och felorsaker: ett värdproblem eller en tung process kan påverka flera tjänster. Det måste finnas tydliga regler för resursanvändning och ansvar för värden.

**Containrar på virtuella eller fysiska värdar.** Containrar gör det möjligt att paketera programmet och dess beroenden på ett mer enhetligt sätt. Det kan underlätta driftsättning och automatisering, men det behövs fortfarande värdar, nätverk, säkerhetsuppdateringar och lagring. En container är inte automatiskt samma säkerhetsgräns som en separat VM.

**Orkestrerad eller hanterad exekvering.** Beroende på plattform kan den placera instanser, starta om dem vid vissa fel och styra resurser. Automatiska omstarter är inte detsamma som att tjänsten eller verksamhetsflödet har återhämtats. Med hanterade tjänster kan den egna organisationen slippa delar av värd- eller klusteradministrationen. Det innebär inte att ansvar för tjänstens funktion, konfiguration, information, kostnad och säkerhet försvinner. Dessutom behöver driftorganisationen förstå vilken funktion plattformen faktiskt garanterar.

En monolit kan köras i containrar. Mikrotjänster kan köras på VM:ar. Teknikvalet i sig säger alltså inte om arkitekturen är bra eller dålig.

## Placering och isolering är arkitekturbeslut

Anta att dokumenttjänsten både tar emot handlingar och framställer förhandsvisningar av stora dokument. Förhandsvisningen kan använda mycket CPU och minne och därmed störa handläggarens uppladdning. Det behöver inte innebära två mikrotjänster, men det kräver kontroll över belastning och resurser.

Placeringen bör bedömas utifrån processor, minne, lagring och nätverksbehov, men också utifrån gemensamma felorsaker. Två instanser på samma värd skyddar inte mot ett värdfel. Två värdar som delar databas, lagringssystem eller nätverk kan fortfarande falla samtidigt. Redundans måste därför bedömas utifrån verkliga felområden och verksamhetens krav på avbrott och dataförlust.

Säkerhetskrav kan också kräva olika grader av fysisk eller logisk separation. Dessa skydd måste bedömas tillsammans med risker för delad värdkärna, administrativa behörigheter och gemensamma plattformskomponenter. Namnrymder och containerskiljelinjer skapar inte automatiskt tillräcklig isolering. Nätverkspolicy, identiteter, behörigheter och ibland separata kluster eller värdar kan behövas. Sådana beslut måste bygga på riskbedömning, inte bara på önskemål om effektiv resursanvändning.

## Skalning är mer än fler instanser

Den gamla backendservern kunde få mer minne eller kompletteras med en till server. En separat dokumenttjänst kan på motsvarande sätt få fler instanser utan att ärendetjänsten behöver skalas. Det förutsätter att flaskhalsen faktiskt finns i den del som får fler instanser. Men vinsten uppstår först när tjänsten är byggd för det. Om sessionsinformation bara finns i en instans eller om alla anrop stoppas av en gemensam databas blir det svårt att tillgodogöra sig extra kapacitet.

Automatisk skalning behöver rimliga resurströsklar, marginaler och mätvärden. Skalar man för sent kan köer och svarstider växa; skalar man för aggressivt kan kostnaderna bli höga och systemet instabilt. En driftplattform kan utföra skalningen, men applikationsteamet måste kunna beskriva tjänstens belastningsmönster och hur den reagerar vid överbelastning.

## Hälsokontroller, omstarter och tillstånd

Att en process körs betyder inte att den kan ta emot trafik. En tjänst kan exempelvis vara igång men sakna anslutning till ett nödvändigt beroende. Plattformen behöver därför signaler som skiljer mellan att instansen lever och att den är redo att hantera nya anrop. Samtidigt måste kontroller utformas så att problem i en annan tjänst inte leder till onödiga omstarter i hela kedjan.

Kortlivade instanser gör det särskilt viktigt att inte lagra oersättlig information enbart på deras lokala filsystem. Dokumenttjänstens filer behöver till exempel lagras i en beständig lagringstjänst med uttalat ansvar för informationen, återställningskrav och åtkomstskydd. Detta gäller även om applikationsteamet inte självt administrerar lagringen. Beständig lagring är dock inte liktydig med backup eller verifierad återställningsförmåga; dessa behandlas senare i boken. [R4](https://kubernetes.io/docs/concepts/workloads/pods/probes/) [R5](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)

## Ansvar mellan applikation och drift

Anta att dokumenttjänsten plötsligt börjar svara långsamt. Plattformsteamet ser att instanserna når minnesgränsen; applikationsteamet upptäcker att senaste versionen håller kvar stora dokument i minnet. Åtgärden kräver båda perspektiven, även om ägarskapet för felsökning och ändring måste vara bestämt i förväg.

En möjlig ansvarsfördelning är att applikationsteamet beskriver kapacitetsbehov, hälsokontroller, start- och stoppbeteende samt programberoenden. Plattformsteamet erbjuder tillförlitlig exekvering, placering, automatisering, resurskontroll och gemensam övervakningsinfrastruktur. Infrastruktur- och säkerhetsfunktioner beslutar om de övergripande regler som måste gälla. Vem som får förändra resursgränser, vem som godkänner avvikelser från isoleringskrav och vem som leder en incident ska vara uttryckligt överenskommet, inte bero på organisationsnamn. Det behöver även vara tydligt vem som följer upp att vald körmiljö levererar överenskomna förutsättningar.

För **applikationsläsaren** är den nya insikten att driftsättning inte bara är att lämna över ett program: tjänstens resurs- och felbeteende är en del av leveransen. För **driftläsaren** är insikten att traditionell kompetens om servrar, virtualisering och kapacitet fortfarande behövs, men i kombination med dynamisk placering, automatisering och förståelse för tjänsteberoenden. [R4](https://kubernetes.io/docs/concepts/workloads/pods/probes/)

## Vi väljer körmiljö för dokumenttjänsten

I vårt fortsatta exempel låter vi dokumenttjänsten köras som två containerinstanser på en gemensamt förvaltad plattform, fördelade på skilda noder. Dokumenten lagras utanför instanserna. Det är ett illustrativt val, inte ett påstående om den enda rätta lösningen. Teamen testar hur tjänsten påverkas av omstart, otillräckligt minne och fördröjd lagring. De kontrollerar också att instanserna verkligen placeras på skilda noder och att trafik kan ledas bort från en instans som inte är redo. Om två noder ändå delar ett kritiskt beroende dokumenteras den kvarstående risken.

Härifrån återstår en avgörande fråga: hur når ärendetjänsten dokumenttjänsten och hur tillåts, säkras och styrs trafiken mellan dem? Det blir nästa kapitels ämne.

## Det vi behöver tänka annorlunda kring

Övergången till mikrotjänster tar inte bort servrar, lagring eller nätverk. Den gör **tjänstens logiska ansvar** mindre bundet till **en bestämd teknisk körplats**. Det kan ge snabbare förändringar, flexiblare resursutnyttjande och bättre felisolering, men endast om tjänster och plattformar utformas för det och deras ansvarsfördelning fungerar.

### Källor och vidare läsning

- **[R4](https://kubernetes.io/docs/concepts/workloads/pods/probes/)** Kubernetes, Liveness, Readiness, and Startup Probes (åtkomst 2026-10-17).
- **[R5](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)** Kubernetes, ReplicaSet (åtkomst 2026-10-17).
