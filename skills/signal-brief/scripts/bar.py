#!/usr/bin/env python3
"""Draw the page-1 proportion bar for a Signal Brief as inline SVG.

Usage:
  python3 bar.py --part 98700 --whole 500000 \
    --part-label "98,700 cars built in 2025" \
    --whole-label "capacity about 500,000 cars a year" \
    --rest-label "empty capacity, about 4 of every 5 slots" [--est] > bar.svg

Both numbers must come from the report's Figures ledger or Estimates, and the
labels must print them the way the brief does, so ledger_check.py can trace them.
--est draws the filled part hatched, for estimates. Paste the output into the
template's picture slot. Exit 2 on bad input."""
import argparse
import html
import sys

W, H, BAR_Y, BAR_H = 640, 64, 24, 26


def build(part, whole, part_label, whole_label, rest_label, est):
    if whole <= 0 or part < 0 or part > whole:
        raise ValueError("need 0 <= part <= whole and whole > 0")
    pw = round(W * part / whole, 1)
    e = html.escape
    fill = "url(#sb-hatch)" if est else "var(--accent, #2B5F8C)"
    rest_x = min(pw + 8, W - 4)
    rest_anchor = "start" if pw < W * 0.6 else "end"
    rest_tx = rest_x if rest_anchor == "start" else W - 8
    out = [
        f'<svg class="sb-bar" viewBox="0 0 {W} {H}" width="100%" role="img" '
        f'aria-label="{e(part_label)} of {e(whole_label)}">',
        '<defs><pattern id="sb-hatch" width="6" height="6" patternUnits="userSpaceOnUse" '
        'patternTransform="rotate(45)"><rect width="6" height="6" fill="#ffffff"/>'
        '<line x1="0" y1="0" x2="0" y2="6" stroke="var(--accent, #2B5F8C)" stroke-width="3"/></pattern></defs>',
        f'<text x="0" y="14" style="font-size:13px;font-weight:600;fill:var(--ink, #1C2329)">{e(part_label)}</text>',
        f'<text x="{W}" y="14" text-anchor="end" style="font-size:12px;fill:var(--gray, #5B6670)">{e(whole_label)}</text>',
        f'<rect x="0" y="{BAR_Y}" width="{W}" height="{BAR_H}" style="fill:var(--soft, #F2F4F6);stroke:var(--rule, #D9DEE2)"/>',
        f'<rect x="0" y="{BAR_Y}" width="{pw}" height="{BAR_H}" style="fill:{fill};stroke:var(--accent, #2B5F8C)"/>',
    ]
    if rest_label:
        out.append(f'<text x="{rest_tx}" y="{BAR_Y + 17}" text-anchor="{rest_anchor}" '
                   f'style="font-size:12px;fill:var(--gray, #5B6670)">{e(rest_label)}</text>')
    out.append("</svg>")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--part", type=float, required=True)
    ap.add_argument("--whole", type=float, required=True)
    ap.add_argument("--part-label", required=True)
    ap.add_argument("--whole-label", required=True)
    ap.add_argument("--rest-label", default="")
    ap.add_argument("--est", action="store_true")
    a = ap.parse_args()
    try:
        print(build(a.part, a.whole, a.part_label, a.whole_label, a.rest_label, a.est))
    except ValueError as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
