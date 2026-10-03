#!/usr/bin/env python3
"""Render brief.html to a US Letter PDF.

Usage:  python3 render.py brief.html brief.pdf
Tries, in order: Playwright (Chromium), a Chrome or Chromium binary, WeasyPrint.
Exit 0 = PDF written. Exit 1 = no renderer available (return the HTML instead and
tell the user to print it to PDF from a browser)."""
import os
import shutil
import subprocess
import sys


def with_playwright(src, out):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        kw = {}
        exe = os.environ.get("CHROMIUM_PATH")
        if exe:
            kw["executable_path"] = exe
        b = p.chromium.launch(**kw)
        pg = b.new_page()
        pg.goto("file://" + os.path.abspath(src))
        pg.wait_for_load_state("networkidle")
        over = pg.evaluate("""() => [...document.querySelectorAll('.page')]
            .map((el, i) => ({i: i + 1, over: el.scrollHeight - el.clientHeight}))
            .filter(x => x.over > 1)""")
        for o in over:
            print(f"WARNING: page {o['i']} content is {o['over']}px taller than the page. Cut text; do not shrink type.")
        pg.pdf(path=out, format="Letter", print_background=True, prefer_css_page_size=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        b.close()


def with_chrome(src, out):
    names = ["chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome",
             "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
             "/opt/pw-browsers/chromium"]
    exe = next((n for n in names if shutil.which(n) or os.path.exists(n)), None)
    if not exe:
        raise RuntimeError("no Chrome or Chromium binary found")
    subprocess.run([shutil.which(exe) or exe, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={os.path.abspath(out)}", "file://" + os.path.abspath(src)],
                   check=True, capture_output=True, timeout=120)


def with_weasyprint(src, out):
    from weasyprint import HTML
    HTML(filename=src).write_pdf(out)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    src, out = sys.argv[1], sys.argv[2]
    errors = []
    for name, fn in (("playwright", with_playwright), ("chrome", with_chrome), ("weasyprint", with_weasyprint)):
        try:
            fn(src, out)
            if os.path.exists(out) and os.path.getsize(out) > 0:
                print(f"Rendered {out} with {name}.")
                sys.exit(0)
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: {e}".splitlines()[0][:160])
    print("No PDF renderer available. Return brief.html and tell the user to open it in a browser and print to PDF (US Letter, no margins, background graphics on).")
    for e in errors:
        print("  " + e)
    sys.exit(1)


if __name__ == "__main__":
    main()
