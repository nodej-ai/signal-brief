#!/usr/bin/env python3
"""Fails if the version is not the same everywhere it is shown, including the
NodeJ catalog (nodej-ai/nodej .claude-plugin/marketplace.json).
Catalog source: a local checkout next to this repo (../nodej) if present,
else the published file on GitHub. If neither can be read, the test FAILS.
Run: python3 tests/test_versions.py  (run before every release)"""
import json, os, re, sys, urllib.request
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
def read(p): return open(os.path.join(ROOT, p), encoding="utf-8").read()
found = {
    "plugin.json": json.loads(read(".claude-plugin/plugin.json")).get("version"),
    "prompt header": (re.search(r"\*\*Version ([0-9.]+),", read("signal-brief-prompt.md")) or [None, None])[1],
    "skill prompt.md": (re.search(r"\*\*Version ([0-9.]+),", read("skills/signal-brief/prompt.md")) or [None, None])[1],
    "README badge": (re.search(r"badge/version-([0-9.]+)-", read("README.md")) or [None, None])[1],
    "CHANGELOG top": (re.search(r"^## ([0-9.]+),", read("CHANGELOG.md"), re.M) or [None, None])[1],
}
CATALOG_LOCAL = os.path.join(ROOT, "..", "nodej", ".claude-plugin", "marketplace.json")
CATALOG_URL = "https://raw.githubusercontent.com/nodej-ai/nodej/main/.claude-plugin/marketplace.json"
def catalog_version():
    try:
        if os.path.exists(CATALOG_LOCAL):
            data, src = json.load(open(CATALOG_LOCAL, encoding="utf-8")), "local ../nodej"
        else:
            with urllib.request.urlopen(CATALOG_URL, timeout=15) as r:
                data, src = json.load(r), "github main"
    except Exception as e:  # noqa: BLE001
        print(f"catalog          could not read ({e})")
        return None, "unreadable"
    entry = next((p for p in data.get("plugins", []) if p.get("name") == "signal-brief"), None)
    return (entry or {}).get("version"), src
cv, csrc = catalog_version()
found[f"catalog ({csrc})"] = cv
for k, v in found.items():
    print(f"{k:28} {v}")
ok = len(set(found.values())) == 1 and None not in found.values()
print("PASS: all versions match" if ok else "FAIL: versions differ")
sys.exit(0 if ok else 1)
