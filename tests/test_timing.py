#!/usr/bin/env python3
"""Tests for skills/signal-brief/scripts/timing.py --summary. Run: python3 tests/test_timing.py"""
import os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, "..", "skills", "signal-brief", "scripts", "timing.py")
LOG = ("2026-10-05T00:00:00-07:00\tStep 1\tstart\t0\n"
       "2026-10-05T00:01:00-07:00\tStep 1A\tstart\t0\n"
       "2026-10-05T00:03:00-07:00\tStep 1A\tend\t19\n"
       "2026-10-05T00:10:00-07:00\tStep 1\tend\t45\n"
       "TOTAL_LOOKUPS=45_of_55_cap\n"
       "2026-10-05T00:10:00-07:00\tStep 2\tstart\t45\n"
       "2026-10-05T00:15:00-07:00\tStep 2\tend\t45\n")
with tempfile.TemporaryDirectory() as d:
    p = os.path.join(d, "x.log")
    open(p, "w").write(LOG)
    r = subprocess.run([sys.executable, T, p, "--summary"], capture_output=True, text=True)
ok = r.returncode == 0 and "15.0 min" in r.stdout and "45 of 55" in r.stdout
print(("ok   " if ok else "FAIL ") + "summary skips free text and does not double-count nested steps")
if not ok:
    print(r.stdout, r.stderr)
sys.exit(0 if ok else 1)
