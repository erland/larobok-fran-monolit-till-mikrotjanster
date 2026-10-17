# Slutgranskning – Från monolit till mikrotjänster

**Datum:** 2026-10-17  
**Underlag:** Bifogade `fran-monolit-till-mikrotjanster.pdf` och `.epub`  
**Metod:** Kontroll enligt Lärobokskaparens publiceringsgrind; programmatisk genomgång av PDF:s 146 sidor och EPUB:s struktur och länkar, plus visuell granskning av utvalda PDF-sidor. **Inte** en fullständig manuell korrekturläsning av all löptext.  
**Bedömning:** **Inte publiceringsgodkänd ännu**. Korrigera metadata och bedöm en layoutavvikelse; avsluta innehållslig slutläsning och gör nytt provbygge.

## Verifierade resultat

| Del | Utfall | Evidens |
|---|---|---|
| PDF öppningsbar | Godkänd | 146 sidor, ungefär 170 × 240 mm |
| Omslag och titelsida, PDF | Godkänd | PDF-sidor 1–2 |
| PDF innehållsförteckning | Godkänd | PDF-sida 3: inledning plus 20 huvudkapitel, inga underrubriker |
| PDF-bokmärken | Godkänd | 21 bokmärken i korrekt ordning |
| PDF:s kapitelstarter | Godkänd i stickprov | PDF-sidor 7, 15, 23: nummer och titel på varsin rad |
| PDF-tabeller | Godkända med reservation | Stickprov PDF-sidor 9 och 21; tabellerna får plats men fyrkolumnstabellen på sida 21 är tät, läsbarhet bör kontrolleras i tryckstorlek |
| EPUB-arkiv | Godkänt | ZIP-kontroll utan korrupt post; 31 arkivposter |
| EPUB-navigering | Godkänd | `EPUB/nav.xhtml`: inledning plus 20 huvudkapitel |
| EPUB läsordning | Godkänd | `nav` i OPF-spine är `linear="no"`; omslag, titelsida och 21 manusdelar finns |
| EPUB kapitelstarter | Godkänd strukturellt | `EPUB/text/ch002.xhtml`–`ch021.xhtml` har `span.chapter-number` + `span.chapter-title`; CSS anger `display:block` för båda |
| EPUB-källhänvisningar | Godkänd i strukturell kontroll | XHTML-länkar till de externa källorna finns; navigationslänkar har giltiga mål; externa URL:ers aktuella tillgänglighet är inte live-testad |

## Avvikelser

### A1 – PDF saknar metadata för titel och författare (bör rättas före release)
PDF-dokumentegenskaperna innehåller tomma fält för `title` och `author` trots att uppgifterna finns på titelsidan. Nyckelorden innehåller `Version 0.5.1`. Ange titel, undertitel vid behov, författare, språk och version i PDF:s metadata genom publiceringsmallen/hyperref och verifiera resultatet med `pdfinfo` eller motsvarande. EPUB har däremot ifylld titel, språk och författare.

### A2 – Nästan tom PDF-sida vid källavsnitt (layoutgranskning)
PDF-sida 96 (tryckt s. 93) innehåller enbart rubriken ”Källor och vidare läsning”, en enda källpost och sidnumret. Det uppstår när ett källavsnitt flyter över på nästa sida före nästa kapitel. Det är inte ett tekniskt fel, men ser ofärdigt ut. Undersök om rubrik och källpost kan hållas ihop med föregående avsnitt eller om sidbrytningen kan förbättras utan att skapa sämre änkor på andra sidor.

### A3 – Kompakt tabell (visuell kvalitetskontroll)
PDF-sida 21 (tryckt s. 18): fyrkolumnstabellen ”Vad förändras för vem?” har smala kolumner och många korta radbrytningar. Kontrollera läsbarhet vid faktisk bokstorlek. Överväg bredare lösning eller tabellomformning om läsprovet visar problem. Tabeller på sidorna 9 och 27 är godtagbara i stickprov, men samtliga tabeller har inte visuellt granskats.

### A4 – Käll- och redaktionell slutläsning (återstår)
Källposterna finns i exporterad text, och URL-länkar förekommer i PDF/EPUB. Däremot har ingen fullständig manuell korrekturläsning av alla 20 kapitel utförts i denna genomgång. Kontrollera särskilt arbetsnoteringar, tidsangivelser för källor, språk och terminologi, övergångar och slutkapitlet. Bekräfta att inga redaktionella interna instruktioner finns i själva boktexten.

## Kontroller att göra i nästa provbygge

1. Kontrollera PDF metadata (titel, författare, språk, version) med `pdfinfo`.
2. Inspektera PDF-sida 96 och motsvarande kapitelavslut efter ändring.
3. Granska tabellen på PDF-sida 21 i 100 % / bokstorlek.
4. Öppna EPUB i minst en faktisk läsare och se att kapitelnummer/titel visas på separata rader och att TOC är navigerbar.
5. Klicka ett urval PDF-/EPUB-källhänvisningar, och granska fullständigt källregister mot manusets källpolicy.
6. Gör en redaktionell slutläsning av hela boken.
7. Kör Validate, Build Preview, projektintegritet samt kontrollera checksummor före GitHub Release.

## Rekommenderad status och nästa arbetssteg

**Release: avvakta.** Gör en liten korrektions-PR för A1 och eventuella layoutåtgärder A2/A3. Dokumentera A4 i projektets granskningsunderlag och gör nytt provbygge. Publiceringstaggen ska vara den avsedda versionsbeteckningen för läsarutgåvan; bokprojektets revisionsnummer är separat.