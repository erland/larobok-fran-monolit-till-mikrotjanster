# Faktakontroll

| ID | Kapitel | Påstående | Status | Källa | Datum |
|---|---|---|---|---|---|

Inledning och kapitel 1 är redaktionellt godkända; kapitel 2 är redaktionellt godkänt i revision 5. Extern källverifiering kvarstår.

## Kapitel 2 – öppna verifieringspunkter (kvarstår efter redaktionellt godkännande)

- F002: Oberoende driftsättning och kontraktskompatibilitet – verifiera mot etablerade arkitekturkällor.
- F003: Partiella fel, timeout och resursutarmning – verifiera mot litteratur om distribuerade system.
- F004: Skillnaden mellan logisk tjänst, instans och VM/container – kontrollera formulering mot aktuella tekniska källor.

## Kapitel 3 – öppna kontroller (revision 6)

- [ ] Verifiera etablerade begrepp för tjänsteansvar, gemensam plattform och helhetsansvar mot lämpliga referenskällor.
- [ ] Kontrollera och belägg resonemangen om ansvar för säkerhet, behörighet och databasåterställning i slutlig faktagranskning.
- [ ] Bedöm att exemplen om ansvarsfördelning tydligt framgår som möjliga modeller, inte universella krav.

## Revision 7 – kapitel 3

Redaktionell granskning godkänd, men kvarvarande tekniska påståenden om organisationsmodeller och driftfördelning behöver källverifieras och nyansgranskas före publicering. Se `docs/granskning-kapitel-03.md`.

## Kapitel 4 – öppna kontroller (revision 8)

- [ ] Verifiera sakframställning om avgränsade kontexter (DDD) mot grundläggande primärkällor.
- [ ] Verifiera allmänna påståenden om mikrotjänsters självständighet och koppling mot etablerade arkitekturkällor.
- [ ] Kontrollera termerna distribuerad monolit, invariant och verksamhetsförmåga för konsekvens i hela boken.

## Revision 9 – kapitel 4

Redaktionellt godkänt enligt `docs/granskning-kapitel-04.md`. Öppna verifieringspunkter från revision 8 kvarstår till extern faktagranskning; inte publiceringsgodkänt.

## Kapitel 5 – verifieringsbehov (revision 10)

- [ ] Kontrollera skillnader mellan VM-isolering, containrar och namnrymder mot aktuella plattforms- och säkerhetsreferenser.
- [ ] Verifiera beskrivning av hälsokontroller, instansplacering och skalning mot relevanta tekniska originalkällor.
- [ ] Bekräfta att exempel på plattforms- och applikationsansvar presenteras som möjliga ansvarsfördelningar, inte som universella regler.

## Revision 11 – kapitel 5

Redaktionellt godkänt enligt `docs/granskning-kapitel-05.md`. Extern verifiering av säkerhetsisolering, skalning och hälsokontroller kvarstår; ingen punkt har felaktigt markerats som faktaverifierad.

## Kapitel 6 – öppna verifieringspunkter (revision 12)

- [ ] Verifiera resonemangen om tidsgränser, idempotens och omleverans mot etablerade primärkällor.
- [ ] Kontrollera aktuella beskrivningar av tjänsteupptäckt, lastbalansering och nätverkspolicy mot relevant plattformsdokumentation.
- [ ] Granska formuleringar om TLS/mTLS, certifikat och nätverkssegmentering mot säkerhetsreferenser.
- [ ] Verifiera att illustrerad ansvarsmatris framgår som en möjlig organisationsmodell, inte en norm.

- Kapitel 6 (rev 13): redaktionell granskning godkänd. Kvarstående extern källverifiering av leveransgarantier för asynkrona meddelanden, nätverkspolicyer och certifikatlivscykel.

## Kapitel 7 – verifieringspunkter (revision 14)
- F7-01: Databas-per-tjänst som logiskt ägarskap snarare än krav på separat fysisk databas. **Ej externverifierad.**
- F7-02: Transaktionsgränser, kompensation och eventual consistency vid fördelat dataansvar. **Ej externverifierad.**
- F7-03: Ordning och duplicering av asynkrona meddelanden och åtgärder för avstämning. **Ej externverifierad.**
- F7-04: Stegvis schemaändring vid samtidiga applikationsversioner. **Ej externverifierad.**

- Kapitel 7 (rev 15): redaktionellt godkänt; F7-01–F7-04 kvarstår för extern källverifiering.

## Kapitel 8 – öppna verifieringspunkter (revision 16)
- [ ] Verifiera råd om lokala testdubblar, kontrakttester och integrationer mot etablerade originalkällor.
- [ ] Kontrollera uppgifter om miljöisolering, åtkomst och hantering av hemligheter mot aktuella säkerhetsrekommendationer.
- [ ] Kontrollera att olika miljömodeller framställs som alternativ och inte som krav för mikrotjänster.
| F-K08-R17 | 8 | Testdubblar behöver hållas förenliga med verkliga kontrakt; isolering och hantering av utvecklingshemligheter | Ej kontrollerad externt | Kontrollera mot etablerade test- och säkerhetskällor | | Redaktionellt godkänt, källverifiering återstår |

## Kapitel 9 – öppna verifieringspunkter (revision 18)
- F9-01: Kontraktstesters möjligheter och begränsningar vid oberoende releaser. **Ej externt verifierad.**
- F9-02: Riskbaserad testning av kompatibla tjänsteversioner och asynkrona meddelandekontrakt. **Ej externt verifierad.**
- F9-03: Isolering av tillfälliga och delade testmiljöer samt testdatahantering. **Ej externt verifierad.**

Kapitel 9: redaktionellt godkänt i revision 19. Teknisk extern källverifiering kvarstår enligt granskningsprotokoll.

## Kapitel 10 – öppna verifieringspunkter (revision 20)

- F10-01: Kontrollera etablerade tillämpningar och begränsningar för rolling, blue–green och canary. **Ej externt verifierad.**
- F10-02: Verifiera kompatibilitet vid samtidiga API-, händelse- och databasschemaversioner. **Ej externt verifierad.**
- F10-03: Faktakontrollera rollback/roll-forward och förändringsstyrning med relevanta primärkällor. **Ej externt verifierad.**

## Kapitel 10 – redaktionell granskning (revision 21)

Godkänt för fortsatt skrivarbete. Extern källverifiering av CI/CD, strategier för utrullning, behörighetsstyrning och återgång återstår.

## Kapitel 11 – öppna källkontroller

- Verifiera etablerade principer för Infrastructure as Code, självbetjäningsplattformar, plattformskontrakt och ansvarsfördelning.
- Verifiera och nyansera tekniska påståenden om hemlighetshantering, databastjänster och policystyrning mot aktuella originalkällor före publicering.

## Kapitel 11 – revision 23
Redaktionellt godkänt; extern verifiering av sakpåståenden om IaC, plattformskontrakt, databastjänster och plattformens säkerhetskontroller kvarstår inför publicering.

## Öppna kontrollpunkter för kapitel 12 (revision 24)

- F12-01: Verifiera teknikbeskrivningarna av tidsgränser, backoff/jitter och idempotens med aktuella primärkällor. Status: ej kontrollerad.
- F12-02: Verifiera beskrivningen av circuit breakers, beredskapskontroller och felutbredning. Status: ej kontrollerad.
- F12-03: Verifiera terminologi och antaganden om köers leveransordning och dubbletter. Status: ej kontrollerad.

## Redaktionell granskning kapitel 12 (revision 25)

Redaktionellt godkänt; extern verifiering av påståenden om felmönster, timeout, återförsök, circuit breaker och köhantering kvarstår före publicering.

## Kapitel 13 – öppna verifieringar

SLI, SLO, SLA, distribuerad spårning, sampling, loggning och telemetrisäkerhet: extern källverifiering återstår.

## Kapitel 13 – redaktionell kontroll (revision 27)

- Redaktionellt godkänt ur båda läsarperspektiven efter justeringar; samtliga externa verifieringsbehov från revision 26 kvarstår öppna inför publicering.

## Kapitel 14 – verifieringspunkter (revision 28)

- Verifiera principer om incidentledning, eskalering och efteranalys mot etablerade primärkällor före publicering.
- Verifiera råd om säker återställning, konfigurationsändringar och tekniska felkedjor.
- Redaktionell granskning och extern källverifiering återstår.

## Kapitel 14 – revision 29

Redaktionellt godkänt efter tvåperspektivgranskning. Extern verifiering av råd om incidentledning, incidentprioritering, återställning, beredskap och efteranalys återstår.

## Kapitel 15 – källverifiering återstår (revision 30)

- Kontrollera terminologi och rekommendationer om autentisering, auktorisation, identitets- och tokenkontroller, TLS, hemlighetshantering och leveranskedjans säkerhet mot relevanta primärkällor.
- Kontrollera påståenden om informationsskydd, loggning och riskbaserade skyddsåtgärder mot tillämpliga krav före publicering.
- Inga externa källor är markerade som verifierade i denna revision.

## Kapitel 15 – redaktionellt godkänt i revision 31

Granskning dokumenterad i `docs/granskning-kapitel-15.md`. Extern verifiering av bland annat tokenvalidering, mTLS, delegering, signerade länkar, nyckelrotation och loggskydd återstår före publicering.

## Kapitel 16 – verifieringsbehov (revision 32)

- Verifiera tekniska definitioner av supportlivscykler, SBOM, utfasning av API:er och ansvar vid uppdatering av containerbasbilder inför publicering.
- Kapitlet är första utkast; inga externa källor har markerats verifierade.

## Kapitel 16 – redaktionell kontroll, revision 33

- Godkänt redaktionellt i två läsarperspektiv. Verifiera före publicering påståenden om SBOM, patchansvar, komponentstöd, kontraktskompatibilitet och säkerhetsuppdateringar mot primärkällor.

## Kapitel 17 (revision 34)

- Extern källverifiering återstår för definitionerna av RPO/RTO, skydd mot korruption och radering, återuppspelning samt kostnads- och kontinuitetsavvägningar.
- Kapitel 17 är ett första utkast och ännu inte redaktionellt godkänt.

## Kapitel 17 – redaktionell granskning (revision 35)

Redaktionellt godkänt. Extern källverifiering kvarstår av RPO/RTO, återställningsmetoder, återuppspelning, kopieskydd och kostnadsmodeller. Se `docs/granskning-kapitel-17.md`.

## Kapitel 18 – faktakontroll kvarstår (revision 36)

- Granska terminologi och tillämpning för ansvarsmatriser, tjänstenivåmål, kostnadsfördelning och leverantörsansvar mot relevanta primärkällor.
- Redaktionell granskning och extern faktaverifiering återstår.

## Kapitel 18 – redaktionell kontroll, revision 37

- Tvåperspektivgranskning godkänd. Extern kontroll kvarstår av definitioner och praxis för ansvarsmatriser, produkt-/tjänsteägarskap, riskbeslut och kostnadsfördelning.

## Kapitel 19 – verifieringsbehov (revision 38)

- Verifiera terminologi och etablerad användning av strangler-mönstret och anti-corruption layer mot tekniska primärkällor.
- Verifiera nyanser om parallella skrivningar, datamigrering, återgång och avveckling mot relevanta källor före publicering.
- Kapitel 19 är ett första utkast; inga nya externa faktapåståenden markeras verifierade.

## Kapitel 19 – redaktionell granskning, revision 39

Granskat och redaktionellt godkänt för fortsatt bokarbete. Extern kontroll av tekniska benämningar och rekommendationer om strangler-mönstret, anti-corruption layer, informationsmigrering och avveckling återstår före publicering.

## Kapitel 20 – utkast, revision 40

- Kontrollera definitioner och resonemang kring modulär monolit, mikroservicegränser, dataägarskap och operativ komplexitet mot väl valda källor före publicering.
- Jämförande arkitekturval är situationsberoende; inga externa källor är verifierade i denna revision.

## Kapitel 20 – redaktionellt godkänt revision 41

Tvåperspektivgranskat med sex förtydliganden. Extern faktakontroll av påståenden om arkitekturegenskaper, transaktioner, isolering, kostnader och organisationens mognad återstår.

## Helhetsgranskning – revision 42

Sex avgränsade tekniska faktastickprov med primärkällor är dokumenterade i `docs/helhetsgranskning-revision-42.md` (H-01–H-06). Tidigare öppna verifieringspunkter är **inte** generellt avklarade. Uppdatera kapitelvis faktakontroll efter ytterligare källgranskning före publicering.

## Manusjustering revision 43

Redaktionell avgränsning av kapitel 3/18, 8/9 och 12–14; inga nya externa faktakällor har verifierats genom dessa ändringar. Tidigare kvarstående faktakontroll gäller oförändrat.

## Etapp 1 – revision 44: inledning och kapitel 1–4

Sju avgränsade påståendekluster har kontrollerats mot primärkällor, med särskilda reservationer där påståenden gäller exempel, organisation eller arkitekturavvägningar. Detaljerade poster, exakta URL:er och återstående granskningsbehov finns i `docs/faktagranskning-etapp-1-revision-44.md`. **Detta är inte fullständig faktaverifiering av något kapitel.**

## Faktagranskning etapp 2 – revision 45

Kapitel 5–7 kontrollerade i åtta centrala påståendekluster, med källor och reservationer i `docs/faktagranskning-etapp-2-revision-45.md`. Ingen manusändring motiverad. Detaljverifiering återstår före publicering.

## Etapp 3 – revision 46, kapitel 8–11

Åtta avgränsade påståendekluster har verifierats mot Docker, Pact, Martin Fowler och Kubernetes. Se `docs/faktagranskning-etapp-3-revision-46.md`. Inga belagda sakfel krävde kapiteländring. Fullständig kontroll återstår.

## Faktagranskning etapp 4 (revision 47)
Kapitel 12–15: åtta verifierade påståendekluster med källor och reservationer. Se `docs/faktagranskning-etapp-4-revision-47.md`. Fullständig radvis faktaverifiering återstår.

## Faktagranskning etapp 5 – revision 48
Kapitel 16–20: tio källkontrollerade påståendekluster; se `docs/faktagranskning-etapp-5-revision-48.md`. Den första selektiva faktagranskningen täcker nu kapitel 1–20. Detta är inte fullständig rad-för-rad-verifiering; slutligt publiceringsgodkännande återstår.

## Samlad restpunktskontroll – revision 49

Den första selektiva faktagranskningen (41 påståendekluster i fem etapper) är sammanställd. Se `docs/faktagranskning-slutkontroll-revision-49.md` för kvarstående P1/P2-arbete. Detta är inte fullständigt faktagodkännande eller publiceringsgodkännande.
## Källintegration revision 50

Referensmarkörer och källavsnitt tillagda i inledningen och kapitel 1–4; se `docs/kallhanvisningar-etapp-1-revision-50.md`. Källintegration i kapitel 5–20 samt detaljfaktaverifiering återstår.

## Källhänvisningar etapp 2 – revision 51

Kapitel 5–7 har källmarkörer och källavsnitt; ingen fullständig detaljfaktakontroll eller publiceringsgodkännande. Se docs/kallhanvisningar-etapp-2-revision-51.md.

## Källhänvisningar etapp 3 – revision 52

Kapitel 8–11 har fått referenser R9–R13. Avgränsad verifiering, inte heltäckande. Se `docs/kallhanvisningar-etapp-3-revision-52.md`.

## Källhänvisningar etapp 4 – revision 53

Kapitel 12–15 har fått referenser R14–R18. Avgränsad verifiering, inte heltäckande. Se `docs/kallhanvisningar-etapp-4-revision-53.md`.

## Källhänvisningar etapp 5 – revision 54

Referenser R19–R23 har införts i kapitel 16–20. Se `docs/kallhanvisningar-etapp-5-revision-54.md`. Värdera källornas räckvidd och rättslig tillämplighet före publicering.

## Samlad referenskontroll – revision 55

Se `docs/samlad-referenskontroll-revision-55.md` och `docs/samlad-kallforteckning.md`. Referensstrukturen är verifierad; fullständig beläggskontroll av varje detaljpåstående återstår.
