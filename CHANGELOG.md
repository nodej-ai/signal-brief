# Changelog

Each version adds a rule because a real brief broke without it.

## 1.2.2, October 3, 2026
- **Skill renamed to signal-brief.** It installed as "brief," which says nothing in a list of skills. In claude.ai pick **signal-brief** from the `/` menu; in Claude Code run `/signal-brief:signal-brief`.

## 1.2.1, October 3, 2026
- **Type floor by role.** Body text at least 9.5 point; labels, tags, chart text, and table headers at least 8 point; footer at least 7.5 point. One 9 point floor for everything forced cutting content the reader needs. The fit check now enforces 8 point.
- **Version shown in Claude.** plugin.json now carries the version, so claude.ai and Claude Code show 1.2.1 instead of a guess. `tests/test_versions.py` fails if the prompt, plugin.json, README badge, and changelog disagree.
- **Examples rebuilt.** All four carry the method credit in the footer and pass the fit check. The Ford brief fixes the page 1 closure arithmetic, says the $250M recipient is not public, shows payroll moving from Ford to Geely, and drops two lines a test reader could not follow.

## 1.2, October 3, 2026
- **Statement signals.** Step 1 now names the signal type. A quote or forecast (like the Ford chief executive's line) gets its own research: who said it, to whom, what it helps them sell, and whether the record backs it. The brief's Signal line names the speaker.
- **Project instructions.** The prompt works pasted into a chat or into a Claude Project's instructions.
- **Plugin checks in code.** The plugin adds a page template, a fit check script, a render script, and a separate reader agent. The 9 point rule existed in prose and the published examples still broke it, so the plugin now checks it on the finished PDF.

## 1.1, October 2, 2026
- **One currency: the reader's.** The Ford brief mixed euros and dollars, so readers had to convert. The research now records one official exchange rate with its source and date, and the brief shows every amount in the reader's currency with that rate stated once.
- **Method credit in the footer** of every brief.

## 1.0, October 2, 2026
- Four steps: research, draft, reader test, fix and fit.
- Earlier one-shot drafts got four numbers wrong that a separate research pass corrected. That is why research and writing are separate steps.
