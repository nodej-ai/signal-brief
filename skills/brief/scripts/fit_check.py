#!/usr/bin/env python3
"""Fit check for a NodeJ Signal Brief PDF.

Checks the rules a model can talk itself out of:
  1. Exactly N pages (default 3), each US Letter.
  2. No text below the minimum size (default 8 pt; the prompt asks 9.5 pt for body text). The footer line may go
     down to --footer-min (default 7.5 pt).
  3. Every page carries the method credit in its footer.
  4. Nothing overlaps the footer and nothing runs off the page.

Usage:  python3 fit_check.py brief.pdf [--pages 3] [--min-pt 8]
Exit 0 = pass. Exit 1 = fail (the reasons are printed). Exit 2 = could not read.
Needs pdfplumber (pip install pdfplumber).
"""
import argparse
import logging
import sys
from collections import defaultdict

logging.getLogger("pdfminer").setLevel(logging.ERROR)

CREDIT = "Method: NodeJ Signal Brief (nodej.ai)"
LETTER = (612.0, 792.0)


def lines_of(chars, tol=2.0):
    """Group characters into visual lines by their baseline."""
    rows = defaultdict(list)
    for c in chars:
        key = round(c["bottom"] / tol)
        rows[key].append(c)
    out = []
    for key in sorted(rows):
        cs = sorted(rows[key], key=lambda c: c["x0"])
        text, prev = "", None
        for c in cs:
            if prev is not None and c["x0"] - prev["x1"] > 0.2 * c["size"]:
                text += " "
            text += c["text"]
            prev = c
        out.append({
            "text": text.strip(),
            "top": min(c["top"] for c in cs),
            "bottom": max(c["bottom"] for c in cs),
            "min_size": min(c["size"] for c in cs if c["text"].strip()),
            "chars": cs,
        })
    return out


def check(path, pages, min_pt, footer_min, credit):
    try:
        import pdfplumber
    except ImportError:
        print("ERROR: pdfplumber is not installed. Run: pip install pdfplumber")
        return 2
    try:
        pdf = pdfplumber.open(path)
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: cannot open {path}: {e}")
        return 2

    fails = []
    with pdf:
        n = len(pdf.pages)
        if n != pages:
            fails.append(f"page count is {n}, must be exactly {pages}. Cut text to fit; never shrink type.")
        for i, page in enumerate(pdf.pages, start=1):
            w, h = float(page.width), float(page.height)
            if abs(w - LETTER[0]) > 2 or abs(h - LETTER[1]) > 2:
                fails.append(f"p{i}: page size {w:.0f}x{h:.0f} pt, must be US Letter 612x792.")
            chars = [c for c in page.chars if c["text"].strip()]
            if not chars:
                fails.append(f"p{i}: no text found (is the PDF an image?).")
                continue
            lines = lines_of(chars)
            # Footer = the line carrying the credit, else the lowest line on the page.
            squash = lambda t: "".join(t.split())
            with_credit = [l for l in lines if credit and squash(credit) in squash(l["text"])]
            footer = with_credit[-1] if with_credit else max(lines, key=lambda l: l["bottom"])
            if credit and squash(credit) not in squash(footer["text"]):
                full = " ".join(l["text"] for l in lines[-3:])
                if squash(credit) not in squash(full):
                    fails.append(f'p{i}: footer is missing the credit "{credit}". Footer reads: "{footer["text"][:90]}"')
            if footer["min_size"] < footer_min - 0.05:
                fails.append(f"p{i}: footer type is {footer['min_size']:.1f} pt, minimum {footer_min} pt.")
            # Body type size.
            small = [l for l in lines if l is not footer and l["min_size"] < min_pt - 0.05]
            for l in small[:6]:
                fails.append(f'p{i}: {l["min_size"]:.1f} pt type (min {min_pt}): "{l["text"][:70]}"')
            if len(small) > 6:
                fails.append(f"p{i}: ...and {len(small) - 6} more lines under {min_pt} pt.")
            # Overlap with footer and off-page text.
            for l in lines:
                if l is footer:
                    continue
                if l["bottom"] > footer["top"] - 1.0:
                    fails.append(f'p{i}: text overlaps the footer: "{l["text"][:70]}"')
            for c in chars:
                if c["x0"] < -0.5 or c["x1"] > w + 0.5 or c["top"] < -0.5 or c["bottom"] > h + 0.5:
                    fails.append(f"p{i}: text runs off the page near x={c['x0']:.0f}, y={c['top']:.0f}.")
                    break

    if fails:
        print(f"FAIL {path}")
        for f in fails:
            print("  - " + f)
        print("Fix: cut or shorten text, then rebuild. Do not reduce font sizes.")
        return 1
    print(f"PASS {path}: {pages} pages, US Letter, no type under {min_pt} pt, credit on every page, nothing overlaps the footer.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("--pages", type=int, default=3)
    ap.add_argument("--min-pt", type=float, default=8.0)
    ap.add_argument("--footer-min", type=float, default=7.5)
    ap.add_argument("--credit", default=CREDIT, help='footer text that must appear on every page ("" to skip)')
    a = ap.parse_args()
    sys.exit(check(a.pdf, a.pages, a.min_pt, a.footer_min, a.credit))


if __name__ == "__main__":
    main()
