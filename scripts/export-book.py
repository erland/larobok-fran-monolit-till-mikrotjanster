#!/usr/bin/env python3
"""Exportera boken till EPUB och PDF i A5-format med godkänt omslag."""
import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

import yaml

root = Path(__file__).resolve().parent.parent
parser = argparse.ArgumentParser()
parser.add_argument("--format", choices=["pdf", "epub", "all"], default="all")
parser.add_argument("--version", default=None, help="Publicerad version, utan v-prefix")
args = parser.parse_args()
book = yaml.safe_load((root / "book.yaml").read_text(encoding="utf-8"))
if not book.get("author") or book["author"] == "Ej fastställd":
    raise SystemExit("Författare saknas.")
if any("planerat men ännu inte skrivet" in (root / p).read_text(encoding="utf-8") for p in book["chapters"][1:]):
    raise SystemExit("Minst ett kapitel är oskrivet.")
if not shutil.which("pandoc"):
    raise SystemExit("Pandoc saknas.")
cover = root / book["cover_image"] if book.get("cover_image") else None
if cover and not cover.is_file():
    raise SystemExit("Omslagsbild saknas: " + str(cover))
(root / "exports").mkdir(exist_ok=True)
formats = ["pdf", "epub"] if args.format == "all" else [args.format]
for fmt in formats:
    output = root / "exports" / ("fran-monolit-till-mikrotjanster." + fmt)
    command = [
        "pandoc", *[str(root / p) for p in book["chapters"]],
        "-o", str(output), "--metadata", "title:" + book["title"],
        "--metadata", "subtitle:" + book.get("subtitle", ""),
        "--metadata", "author:" + book["author"],
        "--metadata", "lang:sv", "--metadata",
        "version:" + (args.version or str(book.get("version", ""))),
        "--toc", "--toc-depth=1"
    ]
    if fmt == "epub":
        command += ["--split-level=1"]
        if cover:
            command += ["--epub-cover-image", str(cover)]
        subprocess.run(command, check=True)
    else:
        for dep in ("xelatex", "pdfunite"):
            if not shutil.which(dep):
                raise SystemExit(dep + " saknas.")
        command += [
            "--pdf-engine=xelatex", "--top-level-division=chapter",
            "-V", "documentclass:report", "-V", "classoption:oneside",
            "-V", "papersize:a5", "-V", "geometry:margin=19mm",
            "-V", "fontsize:10pt"
        ]
        with tempfile.TemporaryDirectory(prefix="book-export-") as folder:
            tmp = Path(folder)
            body = tmp / "body.pdf"
            command[command.index(str(output))] = str(body)
            subprocess.run(command, check=True)
            if cover:
                tex = tmp / "cover.tex"
                tex.write_text(
                    "\\documentclass[a5paper]{article}\n"
                    "\\usepackage[margin=0pt]{geometry}\n"
                    "\\usepackage{graphicx}\n"
                    "\\pagestyle{empty}\n"
                    "\\begin{document}\n"
                    "\\noindent\\includegraphics[width=\\paperwidth,height=\\paperheight]{"
                    + cover.resolve().as_posix() + "}\n"
                    "\\end{document}\n", encoding="utf-8"
                )
                subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "cover.tex"], cwd=tmp, check=True, stdout=subprocess.DEVNULL)
                subprocess.run(["pdfunite", str(tmp / "cover.pdf"), str(body), str(output)], check=True)
            else:
                shutil.copyfile(body, output)
    print(output)
