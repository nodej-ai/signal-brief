#!/usr/bin/env python3
"""Tests for skills/signal-brief/scripts/bar.py. Run: python3 tests/test_bar.py"""
import os
import re
import subprocess
import sys

BAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills", "signal-brief", "scripts", "bar.py")


def run(*args):
    return subprocess.run([sys.executable, BAR, *args], capture_output=True, text=True)


def main():
    failed = 0
    r = run("--part", "98700", "--whole", "500000", "--part-label", "98,700 cars built in 2025",
            "--whole-label", "capacity about 500,000 cars a year", "--rest-label", "four in five slots empty")
    widths = [float(w) for w in re.findall(r'<rect x="0" y="24" width="([\d.]+)"', r.stdout)]
    checks = [
        ("valid input exits 0", r.returncode == 0),
        ("filled width is part/whole of 640", len(widths) == 2 and abs(widths[1] - 640 * 98700 / 500000) < 0.1),
        ("labels printed as given", "98,700 cars built in 2025" in r.stdout and "capacity about 500,000" in r.stdout),
        ("solid fill when not an estimate", "url(#sb-hatch)" not in r.stdout.split("</defs>")[1]),
    ]
    e = run("--part", "1", "--whole", "2", "--part-label", "a", "--whole-label", "b", "--est")
    checks.append(("estimate drawn hatched", "fill:url(#sb-hatch)" in e.stdout))
    x = run("--part", "<b>", "--whole", "2", "--part-label", "a", "--whole-label", "b")
    checks.append(("non-number rejected", x.returncode != 0))
    bad = run("--part", "5", "--whole", "2", "--part-label", "a", "--whole-label", "b")
    checks.append(("part larger than whole exits 2", bad.returncode == 2))
    esc = run("--part", "1", "--whole", "2", "--part-label", "A & <B>", "--whole-label", "b")
    checks.append(("labels are escaped", "A &amp; &lt;B&gt;" in esc.stdout))
    for name, ok in checks:
        failed += not ok
        print(("ok   " if ok else "FAIL ") + name)
    print(f"\n{len(checks) - failed}/{len(checks)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
