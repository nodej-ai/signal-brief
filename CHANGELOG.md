# Changelog

Each version adds a rule because a real brief broke without it.

## 1.4.1, October 3, 2026
- **Research parts run on Sonnet; the reader and fact checker are pinned to Sonnet.** Drafting, the report, and fixes stay with the main model. A rerun of the Ford signal finished research in 2.8 minutes on 40 lookups (about 10 minutes before) and hit no eval traps after the freshness check and grade upgrades.
- **The cost of the alternative is never "not disclosed."** With no stated figure, research builds an estimate from public inputs and shows the formula. The Sonnet rerun stopped at "not disclosed" for the cost of closing Valencia.
- **Statements about a rule check its exemptions.** Part D answers the policy must-finds for effective date and who is exempt. The rerun missed that Europe's duties exempt plug-in hybrids, the loophole behind most of the Chinese share gain.

## 1.4.0, October 3, 2026
- **Must-find first, by signal type.** Event, statement, policy, and market data each get up to five items answered before anything else, at most 3 lookups each; "not disclosed" is a valid answer. A 1.3.1 run of the Ford signal never found the $248M Geely paid Ford, so its Cost line read "Ford gives Geely 34%."
- **Freshness check.** Up to 3 lookups on every pending item, watch date, and the signal itself, from the signal date to today. The same run called a Senate bill "being negotiated" three days after the vote was put off.
- **Grade-upgrade allowance and a hard cap.** Up to 10 lookups to lift page-1 figures to grade A, two tries each; newest primary source wins a conflict. Whole run capped at 55 lookups.
- **The alternative is a concrete option with a cost** (close, sell, keep idle, borrow, build alone), never a strategy label.
- **"What it looks like for you" adapts.** When three or more terms are not disclosed, the section switches to what a smaller company pays under the public rules, or to who the move reaches next.
- **Claim-vs-record layout** for a statement whose company has taken no dated action: page 1 shows each part of the claim against the dated record.
- **Fact checker gains three checks:** the Cost line names who pays whom and how much; no must-find answer reads as fact when it is an estimate; no pending item goes out without its freshness result.

## 1.3.1, October 3, 2026
- **A picture on page 1.** One bar shows the core proportion at a glance (for Ford, 98,700 cars built against 500,000 of capacity), with a heading that states the takeaway. The Oct 2 Ford brief had one because it was hand-built; the method never asked for it, so later runs came out text only. `bar.py` draws it the same way every time, hatched for estimates, and its numbers come from the ledger so the ledger check traces them.

## 1.3.0, October 3, 2026
- **Every number traces.** The research keeps a Figures ledger: value, source, date, grade, and the exact sentence each figure came from. Estimates carry a formula. `ledger_check.py` fails the brief if a printed number has no ledger row, an estimate does not recompute, or page 1 uses anything below the top grade. Two runs of the Ford signal produced closure costs that barely overlapped; a recomputed formula would have caught it.
- **A fact checker beside the reader.** The reader tests clarity, the fact checker tests truth. They run at the same time, and the reader runs one round unless its explanation of the deal was wrong.
- **Research to a budget.** Four parts, about 40 lookups in all, each stopping when its "done when" line is met. The first measured run used about 350 lookups and 27 minutes.
- **Word budgets per section**, so pages fit on the first render instead of after five rounds of trimming.
- **Named files and a timing log**: `signal-brief-<slug>-<date>`, plus minutes and lookups per step.

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
