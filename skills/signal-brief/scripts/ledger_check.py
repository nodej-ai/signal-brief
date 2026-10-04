#!/usr/bin/env python3
"""Ledger check for a NodeJ Signal Brief: every number traces, every estimate recomputes.

Usage:  python3 ledger_check.py <name>-report.md <name>.pdf   (or .html / .txt)

Reads two tables from the report:
  Figures ledger:  ID | Figure | Value | Unit | USD | As of | Grade | Source URL | Exact sentence
  Estimates:       ID | Figure | Formula | Result
Checks:
  1. Recompute: every estimate's Formula (ledger IDs and plain numbers) equals its Result within 1%.
  2. Trace: every number printed in the brief matches a ledger Value or USD, or an estimate Result,
     at the precision the brief shows it (or within 1%).
  3. Grades: no brief number traces only to a grade C figure; page 1 (PDF only) uses grade A or estimates.
Ignored: years (1900-2100 with no $ or %), numbers under 10 with no $ or %, and day numbers next to a month.
Exit 0 = pass, 1 = fail (reasons printed), 2 = could not read the inputs.
"""
import ast
import html as htmlmod
import logging
import operator
import re
import sys

logging.getLogger("pdfminer").setLevel(logging.ERROR)

MONTHS = r"(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?"
SCALE = {"": 1, "k": 1e3, "thousand": 1e3, "m": 1e6, "mn": 1e6, "million": 1e6,
         "b": 1e9, "bn": 1e9, "billion": 1e9, "t": 1e12, "tn": 1e12, "trillion": 1e12}


def num(x):
    x = (x or "").strip().replace(",", "").replace("$", "").replace("€", "").replace("%", "")
    try:
        return float(x)
    except ValueError:
        return None


def tables(md):
    """Yield (header_cells, rows) for each markdown table."""
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            head = [c.strip().lower() for c in lines[i].strip().strip("|").split("|")]
            rows, j = [], i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1
            yield head, rows
            i = j
        else:
            i += 1


def load_report(md):
    ledger, estimates = {}, {}
    for head, rows in tables(md):
        if head[:3] == ["id", "figure", "value"]:
            col = {h: k for k, h in enumerate(head)}
            for r in rows:
                if not r or not re.match(r"^F\d+$", r[0]):
                    continue
                g = lambda name: r[col[name]] if name in col and col[name] < len(r) else ""
                ledger[r[0]] = {"value": num(g("value")), "usd": num(g("usd")),
                                "grade": g("grade").upper()[:1], "figure": g("figure")}
        elif head[:4] == ["id", "figure", "formula", "result"]:
            for r in rows:
                if r and re.match(r"^E\d+$", r[0]) and len(r) >= 4:
                    estimates[r[0]] = {"formula": r[2].strip("` "), "result": num(r[3]), "figure": r[1]}
    return ledger, estimates


OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
       ast.USub: operator.neg, ast.UAdd: operator.pos, ast.Pow: operator.pow}


def safe_eval(expr, names):
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)):
            return n.value
        if isinstance(n, ast.Name):
            if n.id not in names or names[n.id] is None:
                raise ValueError(f"unknown or empty ID {n.id}")
            return names[n.id]
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in OPS:
            return OPS[type(n.op)](ev(n.operand))
        raise ValueError("only numbers, IDs, + - * / ** and brackets are allowed")
    return ev(ast.parse(expr.replace(",", ""), mode="eval"))


def brief_pages(path):
    if path.lower().endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            return [p.extract_text() or "" for p in pdf.pages]
    text = open(path, encoding="utf-8").read()
    if path.lower().endswith((".html", ".htm")):
        text = re.sub(r"(?is)<(script|style).*?</\1>", " ", text)
        text = htmlmod.unescape(re.sub(r"<[^>]+>", " ", text))
    return [text]


NUM_RE = re.compile(
    r"(?P<cur>\$|€)?\s?(?P<n>\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)"
    r"(?:\s?(?P<pct>%)|\s?(?P<sc>trillion|billion|million|thousand|tn|bn|mn|[tbmk])\b)?", re.I)


def brief_numbers(text):
    out = []
    for m in NUM_RE.finditer(text):
        raw, cur, pct, sc = m.group("n"), m.group("cur"), m.group("pct"), (m.group("sc") or "").lower()
        if sc in ("t", "b", "m", "k") and not cur:
            sc = ""  # a bare letter after a plain number is probably a unit, not a scale
        v = float(raw.replace(",", ""))
        before, after = text[max(0, m.start() - 12):m.start()].lower(), text[m.end():m.end() + 6].lower()
        if not cur and not pct:
            if "," not in raw and "." not in raw and 1900 <= v <= 2100:
                continue
            if v < 10:
                continue
            if re.search(MONTHS + r"\s*$", before) or re.match(r"^\s*" + MONTHS, after):
                continue
        decimals = len(raw.split(".")[1]) if "." in raw else 0
        out.append({"text": m.group(0).strip(), "value": v, "scale": SCALE.get(sc, 1),
                    "decimals": decimals, "money": bool(cur), "pct": bool(pct)})
    return out


def matches(b, c):
    if c is None:
        return False
    shown = c / b["scale"]
    half_unit = 0.5 * 10 ** (-b["decimals"]) * 1.0001
    return abs(shown - b["value"]) <= half_unit or (b["value"] and abs(shown - b["value"]) / abs(b["value"]) <= 0.01)


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    try:
        md = open(sys.argv[1], encoding="utf-8").read()
        pages = brief_pages(sys.argv[2])
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: cannot read inputs: {e}")
        sys.exit(2)
    ledger, estimates = load_report(md)
    if not ledger:
        print("ERROR: no Figures ledger table (ID | Figure | Value | ...) found in the report.")
        sys.exit(2)
    fails = []

    names = {k: v["value"] for k, v in ledger.items()}
    for eid, e in estimates.items():
        try:
            got = safe_eval(e["formula"], names)
        except Exception as ex:  # noqa: BLE001
            fails.append(f"{eid} ({e['figure']}): formula '{e['formula']}' cannot be computed: {ex}")
            continue
        if e["result"] is None or (got and abs(got - e["result"]) / abs(got) > 0.01):
            fails.append(f"{eid} ({e['figure']}): formula gives {got:,.4g} but Result says {e['result']}")
        names[eid] = got

    pool = []
    for fid, f in ledger.items():
        for v in (f["value"], f["usd"]):
            if v is not None:
                pool.append((fid, f["grade"], v))
    for eid, e in estimates.items():
        if names.get(eid) is not None:
            pool.append((eid, "E", names[eid]))
        for const in re.findall(r"(?<![A-Z\d.])\d+(?:\.\d+)?", e["formula"].replace(",", "")):
            pool.append((f"{eid} input", "E", float(const)))

    traced = 0
    for pi, text in enumerate(pages, start=1):
        for b in brief_numbers(text):
            hits = [(i, g) for i, g, v in pool if matches(b, v)]
            where = f"p{pi}" if len(pages) > 1 else "brief"
            if not hits:
                fails.append(f'{where}: "{b["text"]}" does not trace to any ledger figure or estimate')
                continue
            traced += 1
            grades = {g for _, g in hits}
            if grades <= {"C"}:
                fails.append(f'{where}: "{b["text"]}" traces only to grade C ({", ".join(i for i, _ in hits)})')
            elif pi == 1 and len(pages) > 1 and not grades & {"A", "E"}:
                fails.append(f'p1: "{b["text"]}" is grade {"/".join(sorted(grades))}; page 1 needs grade A or an estimate')

    if fails:
        print(f"FAIL ledger check ({traced} numbers traced, {len(estimates)} estimates)")
        for f in fails[:40]:
            print("  - " + f)
        if len(fails) > 40:
            print(f"  ...and {len(fails) - 40} more")
        print("Fix: correct the number, add a sourced ledger row, or cut the line. Never invent a row.")
        sys.exit(1)
    print(f"PASS ledger check: {traced} numbers traced, {len(estimates)} estimates recomputed, grades OK.")
    sys.exit(0)


if __name__ == "__main__":
    main()
