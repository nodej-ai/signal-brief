---
name: signal-brief
description: Turn one news signal into a three-page NodeJ Signal Brief for executives, with a sourced research report and a reader test. Use when the user asks for a signal brief, says "brief this", or gives a headline or one-sentence fact to research and explain.
---

Read `prompt.md` in this skill's folder and follow it exactly, all four steps. The signal is the headline or one-sentence fact the user gave with this request. If none was given, ask for it before starting.

This skill adds tools to the prompt. Use them where they apply:

1. **Step 2, draft.** Start from `assets/template.html`. Copy it to `brief.html` and fill every slot from `report.md`. Delete a block the report cannot support instead of leaving a placeholder. Keep the footer credit on every page. Do not lower any font size.
2. **Render.** Run `python3 scripts/render.py brief.html brief-draft.pdf` (paths relative to this skill's folder; in Claude Code and Cowork use `${CLAUDE_SKILL_DIR}/scripts/render.py`). If it prints a page-overflow warning, cut text and render again. If it exits 1, no renderer is available: deliver `brief.html` and say so.
3. **Step 3, reader test.** If the `reader` agent from this plugin is available (Claude Code and Cowork), extract the brief text to `brief-text.md` and run the reader agent on that file only. Never pass it `report.md`. Where agents are not available (chat), follow the prompt's fresh-pass instructions instead.
4. **Step 4, fit.** After the final render, run `python3 scripts/fit_check.py brief.pdf`. It must print PASS before you deliver. On FAIL, fix what it lists by cutting text, render, and run it again. Report the PASS line in your summary. If pdfplumber is missing, install it (`pip install pdfplumber`) or say the check could not run.
