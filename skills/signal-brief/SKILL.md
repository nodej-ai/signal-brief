---
name: signal-brief
description: Turn one news signal into a three-page NodeJ Signal Brief for executives, with a sourced research report, a reader test, and a fact check. Use when the user asks for a signal brief, says "brief this", or gives a headline or one-sentence fact to research and explain.
---

Read `prompt.md` in this skill's folder and follow it exactly, all four steps. The signal is the headline or one-sentence fact the user gave with this request. If none was given, ask for it before starting.

This skill adds tools to the prompt. Script paths are relative to this skill's folder; in Claude Code and Cowork use `${CLAUDE_SKILL_DIR}/scripts/...`.

1. **Timing.** At the start and end of every step run `python3 scripts/timing.py <name>-timing.log "<step>" start|end <lookups so far>`. At the end, `python3 scripts/timing.py <name>-timing.log --summary` and include the summary in your reply.
2. **Step 1, research.** Where agents are available (Claude Code, Cowork), launch the four research parts as parallel agents on the Sonnet model (`model: sonnet`), each with its lookup ceiling. Give each part the must-find items for the signal type that fall in its sections, tell it to answer those first, and to stop when its "done when" line is met. Then run the freshness check (up to 3 lookups) and grade upgrades (up to 10) yourself. Stop all searching at 55 lookups.
3. **Step 2, draft.** Make the page-1 picture with `python3 scripts/bar.py --part <value> --whole <value> --part-label "..." --whole-label "..." --rest-label "..."` (add `--est` for an estimate) using two ledger figures, and paste its SVG into the picture slot. Start from `assets/template.html`. Copy it to `<name>.html` and fill every slot from the report, inside the prompt's word budgets. Delete a block the report cannot support. For a statement signal with no dated action, use the template's claim-vs-record block in place of the picture, money walk, alternative, and arithmetic. Keep the footer credit on every page and the "Your judgment" box on page 3 word for word. Do not lower any font size.
4. **Render.** `python3 scripts/render.py <name>.html <name>.pdf`. If it prints a page-overflow warning, cut text and render again. If it exits 1, no renderer is available: deliver the HTML and say so.
5. **Step 3, checks.** Where agents are available, run the `reader` agent (on the brief text only, never the report) and the `fact-checker` agent (on the brief and the report) at the same time. They must be launched from the session that holds the whole run. If you are running this skill as a subagent without the Agent tool, stop after rendering, return the file paths, and say "Step 3 pending: needs an independent reader"; the parent session runs Steps 3 and 4. Never run the reader test on your own draft. In chat, follow the prompt's fallback.
   Give the reader page 1 as its own PDF first, then the full brief. Score its three-sentence page-1 explanation against the report's answer key yourself: right, wrong, or missing for each sentence. If any is wrong or missing, fix page 1 and run a new `reader` agent, at most two reruns.
6. **Step 4, final gates.** After the last render, both must print PASS before you deliver:
   - `python3 scripts/ledger_check.py <name>-report.md <name>.pdf` (every number traces, every estimate recomputes, grades OK)
   - `python3 scripts/fit_check.py <name>.pdf` (three pages, type sizes, credit, footer)
   On FAIL, fix what it lists (correct the number, add a sourced ledger row, or cut the line; never invent a row), render, and rerun. Report both PASS lines and the answer-key score in your summary. If pdfplumber is missing, install it (`pip install pdfplumber`) or say the checks could not run.
