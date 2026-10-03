#!/usr/bin/env python3
"""Fails if the version is not the same everywhere it is shown.
Run: python3 tests/test_versions.py  (run before every release)"""
import json, os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
found = {
    "plugin.json": json.loads(read(".claude-plugin/plugin.json")).get("version"),
    "prompt header": (re.search(r"\*\*Version ([0-9.]+),", read("signal-brief-prompt.md")) or [None, None])[1],
    "skill prompt.md": (re.search(r"\*\*Version ([0-9.]+),", read("skills/brief/prompt.md")) or [None, None])[1],
    "README badge": (re.search(r"badge/version-([0-9.]+)-", read("README.md")) or [None, None])[1],
    "CHANGELOG top": (re.search(r"^## ([0-9.]+),", read("CHANGELOG.md"), re.M) or [None, None])[1],
}
for k, v in found.items():
    print(f"{k:16} {v}")
ok = len(set(found.values())) == 1 and None not in found.values()
print("PASS: all versions match" if ok else "FAIL: versions differ")
sys.exit(0 if ok else 1)
