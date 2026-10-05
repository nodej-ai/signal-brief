#!/usr/bin/env python3
"""Examples stay current. Fails the release if any example is stale, missing, unlisted, or broken.

examples/manifest.json records the method version each example was built with ("built_with") and the
oldest version an example may have been built with ("examples_min"). When a release changes what a brief
says or how it is checked (the prompt, the reader or fact-checker agents, or a checker rule that would
change a printed brief), raise "examples_min" to that release. This test then fails until every example
is rebuilt under it and its "built_with" is updated.

Checks: every PDF in examples/ is in the manifest and every manifest entry exists; every built_with is at
least examples_min and no later than plugin.json's version; every example is linked from README.md;
every example passes fit_check.py. Run: python3 tests/test_examples.py"""
import json, os, re, subprocess, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
EX = os.path.join(ROOT, "examples")
FIT = os.path.join(ROOT, "skills", "signal-brief", "scripts", "fit_check.py")
v = lambda s: tuple(int(x) for x in s.split("."))
man = json.load(open(os.path.join(EX, "manifest.json"), encoding="utf-8"))
current = json.load(open(os.path.join(ROOT, ".claude-plugin", "plugin.json"), encoding="utf-8"))["version"]
readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
pdfs = sorted(f for f in os.listdir(EX) if f.endswith(".pdf"))
listed = man["examples"]
fails = []
if v(man["examples_min"]) > v(current):
    fails.append(f"examples_min {man['examples_min']} is later than the plugin version {current}")
for f in pdfs:
    if f not in listed:
        fails.append(f"{f}: in examples/ but not in manifest.json")
for f, meta in listed.items():
    if f not in pdfs:
        fails.append(f"{f}: in manifest.json but not in examples/")
        continue
    b = meta.get("built_with", "0.0.0")
    if v(b) < v(man["examples_min"]):
        fails.append(f"{f}: built with {b}, older than examples_min {man['examples_min']}; rebuild it under the current method")
    if v(b) > v(current):
        fails.append(f"{f}: built_with {b} is later than the plugin version {current}")
    if f"examples/{f}" not in readme:
        fails.append(f"{f}: not linked from README.md")
    r = subprocess.run([sys.executable, FIT, os.path.join(EX, f)], capture_output=True, text=True)
    if r.returncode != 0:
        fails.append(f"{f}: fit_check failed: {r.stdout.strip().splitlines()[0] if r.stdout.strip() else r.stderr.strip()[:200]}")
for link in set(re.findall(r"examples/([\w.-]+\.pdf)", readme)):
    if link not in pdfs:
        fails.append(f"README links examples/{link}, which does not exist")
for f in fails:
    print("FAIL " + f)
print(f"{'PASS' if not fails else 'FAIL'}: {len(pdfs)} examples, examples_min {man['examples_min']}, plugin {current}")
sys.exit(1 if fails else 0)
