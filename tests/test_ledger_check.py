#!/usr/bin/env python3
"""Tests for skills/signal-brief/scripts/ledger_check.py. Run: python3 tests/test_ledger_check.py"""
import os
import subprocess
import sys
import tempfile

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "..", "skills", "signal-brief", "scripts", "ledger_check.py")

LEDGER = """# Report

## Figures ledger

| ID | Figure | Value | Unit | USD | As of | Grade | Source URL | Exact sentence |
|---|---|---|---|---|---|---|---|---|
| F1 | Geely stake price | 221000000 | EUR | 248072500 | 2026-07-24 | A | https://example.com/hkex | Geely pays EUR221 million. |
| F2 | Plant use 2025 | 19.74 | % |  | 2025-12-31 | A | https://example.com/a | ran at 19.74%. |
| F3 | US duty on China-built EVs | 127.5 | % |  | 2026-09-01 | A | https://example.com/crs | totals 127.5%. |
| F4 | Plant capacity | 500000 | cars |  | 2026-07-23 | A | https://example.com/b | 500,000 cars. |
| F5 | Cars built 2025 | 98700 | cars |  | 2025-12-31 | A | https://example.com/c | 98,700 cars. |
| F6 | EU duty on Geely | 28.8 | % |  | 2026-01-01 | A | https://example.com/d | 28.8%. |
| F7 | Assumed customs value | 25800 | USD | 25800 | 2026-10-01 | B | https://example.com/e | about $25,800. |
| F8 | ECB rate | 1.1225 | USD per EUR |  | 2026-10-02 | A | https://example.com/ecb | 1.1225 |
| F9 | Geely share | 34 | % |  | 2026-07-23 | A | https://example.com/f | 34%. |
| F10 | Rumored second plant cost | 900000000 | USD | 900000000 | 2026-09-01 | C | https://example.com/g | maybe $900M. |

## Estimates

| ID | Figure | Formula | Result |
|---|---|---|---|
| E1 | Duty avoided per year | F7 * F6 / 100 * 80000 | 594432000 |
"""

GOOD = ("On Sep 29, 2026 Farley spoke. Geely pays $248M for 34% of a plant running at about 20%: "
        "98,700 cars of 500,000. US duty: 127.5%. EU duty 28.8% on a $25,800 car, 80,000 cars, "
        "so about $594M a year (Est). EUR1 = $1.1225 (ECB). Page 1 of 3. In 2027 it opens.")


def run(report_text, brief_text, ext=".txt", pdf_pages=None):
    with tempfile.TemporaryDirectory() as d:
        r = os.path.join(d, "x-report.md")
        open(r, "w").write(report_text)
        b = os.path.join(d, "x" + ext)
        if pdf_pages:
            c = canvas.Canvas(b, pagesize=letter)
            for t in pdf_pages:
                c.setFont("Helvetica", 10)
                c.drawString(50, 700, t)
                c.showPage()
            c.save()
        else:
            open(b, "w").write(brief_text)
        p = subprocess.run([sys.executable, CHECK, r, b], capture_output=True, text=True)
        return p.returncode, p.stdout


CASES = [
    ("good brief passes", LEDGER, GOOD, 0),
    ("untraced number fails", LEDGER, GOOD + " A $300M write-off follows.", 1),
    ("12% trap fails", LEDGER, GOOD + " Chinese brands hold 12% of the market.", 1),
    ("wrong estimate result fails", LEDGER.replace("| 594432000 |", "| 660000000 |"), GOOD, 1),
    ("grade C only fails", LEDGER, GOOD + " A second plant may cost $900M.", 1),
    ("no ledger exits 2", "# Report\nno tables", GOOD, 2),
    ("html input works", LEDGER, "<p>Geely pays <b>$248M</b> for 34%.</p><style>.x{width:999px}</style>", 0),
]


def main():
    failed = 0
    for name, rep, brief, want in CASES:
        ext = ".html" if name.startswith("html") else ".txt"
        code, out = run(rep, brief, ext)
        ok = code == want
        failed += not ok
        print(("ok   " if ok else "FAIL ") + f"{name} (exit {code}, want {want})")
        if not ok:
            print(out)
    # page 1 must use grade A: $25,800 is grade B
    code, out = run(LEDGER, None, ".pdf", pdf_pages=["Geely pays $248M. Car value $25,800.", "Footer"])
    ok = code == 1 and "page 1 needs grade A" in out
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"page-1 grade B fails (exit {code})")
    code, out = run(LEDGER, None, ".pdf", pdf_pages=["Geely pays $248M.", "Car value $25,800."])
    ok = code == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade B on page 2 passes (exit {code})")
    # grade R: the signal's headline figure from one original report
    rled = LEDGER.replace("| F7 | Assumed customs value | 25800 | USD | 25800 | 2026-10-01 | B |",
                          "| F7 | Reported deal size | 25800 | USD | 25800 | 2026-10-01 | R:FT |")
    code, out = run(rled, None, ".pdf", pdf_pages=["Geely pays $248M. The FT reports a $25,800 figure.", "Footer"])
    ok = code == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R named on page 1 passes (exit {code})")
    if not ok:
        print(out)
    code, out = run(rled, None, ".pdf", pdf_pages=["Geely pays $248M. A $25,800 figure.", "Footer"])
    ok = code == 1 and "grade R" in out
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R unnamed on page 1 fails (exit {code})")
    noout = rled.replace("R:FT", "R")
    code, out = run(noout, None, ".pdf", pdf_pages=["Geely pays $248M.", "A $25,800 figure."])
    ok = code == 1 and "must name its outlet" in out
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R without outlet fails (exit {code})")
    many = rled
    for fid in ("F2", "F4", "F5"):
        many = many.replace(f"| {fid} |", f"| {fid} |", 1)
    many = many.replace("| 2025-12-31 | A | https://example.com/a |", "| 2025-12-31 | R:Reuters | https://example.com/a |")
    many = many.replace("| 2026-07-23 | A | https://example.com/b |", "| 2026-07-23 | R:Reuters | https://example.com/b |")
    many = many.replace("| 2025-12-31 | A | https://example.com/c |", "| 2025-12-31 | R:Reuters | https://example.com/c |")
    many = many.replace("| 2026-01-01 | A | https://example.com/d |", "| 2026-01-01 | R:Reuters | https://example.com/d |")
    many = many.replace("| 2026-07-23 | A | https://example.com/f |", "| 2026-07-23 | R:Reuters | https://example.com/f |")
    code, out = run(many, GOOD + " Reuters.", ".txt")
    ok = code == 1 and "at most 5" in out
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"more than 5 grade R rows fails (exit {code})")
    # v1.5.2: outlet must sit in the same sentence, not just nearby
    code, out = run(rled, None, ".pdf", pdf_pages=["The FT broke the story. Separately, a $25,800 figure.", "Footer"])
    ok = code == 1 and "same sentence" in out
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R named in another sentence fails (exit {code})")
    code, out = run(rled, None, ".pdf", pdf_pages=["A price of about $25,800, per the\nFT, was reported.", "Footer"])
    ok = code == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R named across a line break passes (exit {code})")
    if not ok:
        print(out)
    # v1.5.2: date ranges, decades, 24/7 and identifiers are not figures
    frag = GOOD + " Season 2025-26 and 2028/29, the 1950s-60s, runs 24/7, docket ER26-3380, from 2020-24."
    code, out = run(LEDGER, frag, ".txt")
    ok = code == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"date and docket fragments are ignored (exit {code})")
    if not ok:
        print(out)
    code, out = run(LEDGER, GOOD + " Output rose 26 points.", ".txt")
    ok = code == 1
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"a real untraced 26 still fails (exit {code})")
    code, out = run(rled, None, ".pdf", pdf_pages=["A $25,800 price, per the FT. Step 1: $25,800.", "Footer"])
    ok = code == 0
    failed += not ok
    print(("ok   " if ok else "FAIL ") + f"grade R repeat after a named first mention passes (exit {code})")
    if not ok:
        print(out)
    total = len(CASES) + 11
    print(f"\n{total - failed}/{total} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
