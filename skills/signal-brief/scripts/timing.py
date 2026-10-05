#!/usr/bin/env python3
"""Append one line to a Signal Brief timing log.

Usage:  python3 timing.py <name>-timing.log "Step 1" start [lookups]
        python3 timing.py <name>-timing.log --summary
Line format: ISO time<TAB>step<TAB>start|end<TAB>lookups
--summary prints minutes per step, then the run's wall-clock total (first line to last) and the
highest lookup count. Lines it cannot read (free-text notes) are skipped, and nested steps
("Step 1A" inside "Step 1") are listed but never added twice."""
import datetime
import sys


def summary(path):
    starts, rows, stamps, lookups = {}, [], [], []
    for line in open(path, encoding="utf-8"):
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3:
            continue
        try:
            t = datetime.datetime.fromisoformat(parts[0])
        except ValueError:
            continue
        stamps.append(t)
        if len(parts) > 3 and parts[3].strip().isdigit():
            lookups.append(int(parts[3]))
        if parts[2] == "start":
            starts[parts[1]] = t
        elif parts[2] == "end" and parts[1] in starts:
            rows.append((parts[1], (t - starts[parts[1]]).total_seconds() / 60, parts[3] if len(parts) > 3 else ""))
    for step, mins, lk in rows:
        print(f"{step:28} {mins:5.1f} min  {lk and lk + ' lookups'}")
    total = (max(stamps) - min(stamps)).total_seconds() / 60 if stamps else 0
    print(f"{'Total (wall clock)':28} {total:5.1f} min  {max(lookups) if lookups else 0} of 55 lookups")


def main():
    if len(sys.argv) >= 3 and sys.argv[2] == "--summary":
        summary(sys.argv[1])
        return
    if len(sys.argv) < 4 or sys.argv[3] not in ("start", "end"):
        print(__doc__)
        sys.exit(2)
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    lookups = sys.argv[4] if len(sys.argv) > 4 else ""
    with open(sys.argv[1], "a", encoding="utf-8") as f:
        f.write(f"{now}\t{sys.argv[2]}\t{sys.argv[3]}\t{lookups}\n")


if __name__ == "__main__":
    main()
