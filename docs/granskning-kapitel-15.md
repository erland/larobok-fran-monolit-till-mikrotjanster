# Redaktionell kvalitetsgranskning – kapitel 15

- Datum: 2026-10-17
- Underlag: revision 30, projektversion 3.0.0
- Beslut: **Redaktionellt godkänt för fortsatt bokarbete (revision 31)**
- Källverifiering och publiceringsgodkännande: **återstår**

## Applikationsperspektiv

Godkänt efter förtydliganden av tokenvalidering, mottagarbegränsning, delegerad åtkomst och kontroll av dokumentbehörighet även vid nedladdning. Kapitlet skiljer teknisk tjänsteidentitet från användarens verksamhetsrättigheter.

## Drift- och plattformsperspektiv

Godkänt efter förtydliganden av säker certifikat- och nyckelrotation samt skydd för säkerhetsrelevanta loggar. Infrastrukturens kontroller beskrivs som komplement till applikationens behörighetsprövning, inte som ersättning.

## Genomförda justeringar

1. Kompletterad tokenvalidering med utfärdare, mottagare och tillitskontrakt.
2. Förtydligad delegering mellan ärende- och dokumenttjänsten, utan okritisk tokenvidarebefordran.
3. Tillagd riskbedömning för signerade dokumentlänkar och frånvaro av automatisk behörighetsomprövning.
4. Förtydligad rotation av nycklar och certifikat med kontrollerad överlappning.
5. Förtydligat skydd, åtkomst, gallring och korrelation för säkerhetsloggar.

## Bedömning

Texten är begriplig för de båda läsargrupperna, följer ärende- och dokumentexemplet och klargör delat ansvar. Tidigare kapitel ändras inte. Extern verifiering av tekniska råd och tillämpliga säkerhetskrav samt slutkorrektur kvarstår före publicering.
