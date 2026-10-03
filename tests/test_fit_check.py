#!/usr/bin/env python3
"""Tests for skills/brief/scripts/fit_check.py. Run: python3 tests/test_fit_check.py
Builds small PDFs with reportlab and checks that each rule passes and fails when it should."""
import os
import subprocess
import sys
import tempfile

from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "..", "skills", "brief", "scripts", "fit_check.py")
CREDIT = "Method: NodeJ Signal Brief (nodej.ai)"


def make(path, pages=3, size=letter, body_pt=10, footer=True, overlap=False, offpage=False):
    c = canvas.Canvas(path, pagesize=size)
    w, h = size
    for n in range(1, pages + 1):
        c.setFont("Helvetica", body_pt)
        for i in range(20):
            c.drawString(50, h - 60 - i * 16, f"Body line {i} on page {n} with enough words to be real text.")
        if overlap:
            c.drawString(50, 33, "This body line sits on top of the footer.")
        if offpage:
            c.drawString(w - 20, 400, "This line runs off the right edge of the page.")
        if footer:
            c.setFont("Helvetica", 8)
            c.drawString(50, 30, f"{CREDIT}   Page {n} of {pages}")
        c.showPage()
    c.save()


CASES = [
    ("good brief passes", {}, 0),
    ("four pages fails", {"pages": 4}, 1),
    ("two pages fails", {"pages": 2}, 1),
    ("7 pt body fails", {"body_pt": 7}, 1),
    ("A4 fails", {"size": A4}, 1),
    ("missing credit fails", {"footer": False}, 1),
    ("footer overlap fails", {"overlap": True}, 1),
    ("off-page text fails", {"offpage": True}, 1),
]


def main():
    failed = 0
    with tempfile.TemporaryDirectory() as d:
        for name, kw, want in CASES:
            p = os.path.join(d, "t.pdf")
            make(p, **kw)
            r = subprocess.run([sys.executable, CHECK, p], capture_output=True, text=True)
            ok = r.returncode == want
            failed += not ok
            print(("ok   " if ok else "FAIL ") + f"{name} (exit {r.returncode}, want {want})")
            if not ok:
                print(r.stdout)
        p = os.path.join(d, "missing.pdf")
        r = subprocess.run([sys.executable, CHECK, p], capture_output=True, text=True)
        ok = r.returncode == 2
        failed += not ok
        print(("ok   " if ok else "FAIL ") + f"unreadable file returns 2 (exit {r.returncode})")
    print(f"\n{len(CASES) + 1 - failed}/{len(CASES) + 1} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
