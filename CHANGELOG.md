# Changelog

Each version adds a rule because a real brief broke without it.

## 1.5.6, October 6, 2026
- **Page 3 ends with the reader's part.** A fixed box, "Your judgment finishes this brief", replaces the byline. A brief can't be perfect: some human judgment shapes what it says and leaves out, so the reader is asked to engage, check it, and ask the follow-up questions. The old byline offered "the full research report" by email, but the report belongs to whoever ran the method, so the offer is gone.
- **Less repetition.** The footer drops its leading "Signal Brief"; the page-1 brand line names the brief and the footer keeps the method credit. All six examples rebuilt.

## 1.5.5, October 5, 2026
- **Examples stay current, enforced at release.** `examples/manifest.json` records the method version each example was built with and the oldest allowed (`examples_min`). `tests/test_examples.py` fails the release if an example is older than that, missing from the manifest or README, or fails `fit_check.py`. When a release changes what a brief says or how it is checked, raise `examples_min` to it; the release then cannot ship until every example is rebuilt. Until 1.5.4, three of six examples sat two method versions behind and nothing flagged it. The release workflow also now runs `test_timing.py`.

## 1.5.4, October 5, 2026
- **All six examples now follow the current method.** Ford, Maryland and the AHP hotel REITs were rewritten under 1.5.3: each report ends with an answer key, page 1 says what was said or done, and every guessed motive is gone. Fresh readers' page-1 explanations matched all six answer keys on the first round. The rewrite dropped three titles that told a story the record did not support: "Partner in Europe, wall off America" (Farley never said it), "Banned before it arrived" (the record does not show the practice was absent from Maryland stores), and "The yield was their own money" (the SEC said "primarily", and the sponsor settled without admitting it).
- **`ledger_check.py` skips bill, chapter, docket and case numbers** (SB 387, HB 895, Chapter 154). A fixer wrote "SB387" without a space to get past the checker; the checker now reads the identifier correctly, so the brief can print it correctly.

## 1.5.3, October 5, 2026
- **What it does, not a guessed why.** Three rounds of fixes to the Amazon chip-leaseback brief kept hunting for a motive and landed on "spending outran cash by $7.6 billion", for an AA-rated company that sold a $24.9 billion bond in July. The plain mechanics were the story: sell $8 billion of chips and keep using them, get $8 billion back to buy as many again. The Read now says what the move does for each side in plain arithmetic; a motive appears only when a party states it on the record. The research's why ladder became "what it does, then why", with a test: if the company could get the same thing the obvious way more cheaply, the motive is not need. A number set next to a reason must cause it, not just match its size.
- **The reader is scored against an answer key.** The report ends with three sentences from the record: what happened, how it works, what it does for each side. The reader writes its page-1 explanation without grading itself; the run scores each sentence right, wrong, or missing. In 1.5.2 three rounds of fresh readers all voted "Partly" while their summaries were correct, because "so what for me" complaints leaked into the verdict and each new reader found new nits.
- **Grade R covers the deal's own terms** (interest rate, length, fees, buyback price) when they come from the same original report as its price. The Beaumont brief's 0% laptop rate is the heart of that deal, yet it was grade B, so page 1 wrote it in words ("interest-free") to pass the checker. A number in words now counts as that number. The five-row cap stays; when more qualify, page 1's needs pick the five.
- **Fact checker check 10:** a motive no party stated, or one the report's own record contradicts.

## 1.5.2, October 5, 2026
- **Page 1 stands alone, and the reader gates it.** Fresh 1.5.1 runs of Amazon, Chromebook, and Meta nuclear passed both checks, yet independent readers rated all three "Partly": Amazon's motive (cash or how the debt looks) sat on page 2; Chromebook's Lenovo bid at 4% sat on page 2; Meta's 3,760 MW had no scale and its price estimate sat on page 3. New rule 15 moves whatever page 1 needs onto page 1, asks for a scale anchor and for what similar figures include. The reader now reads page 1 alone and returns a verdict (Yes, Partly, No); Partly or No means fix page 1 and run a fresh reader, at most twice.
- **Confirm the signal.** The Meta nuclear signal described deals from June 2025 and January 2026 as new. Part D now spends its first 2 lookups checking the signal's date, parties, and figure; the record wins, and the report shows "Signal as given" against "Signal as found."
- **Analyst estimates of undisclosed terms can be grade R** (`R:Jefferies`), so page 1 can say "not disclosed; Jefferies estimates about $70 per MWh" instead of hiding the number until page 3.
- **Grade R attribution is checked by sentence, not distance.** `ledger_check.py` now wants the outlet in the same sentence as the figure's first mention on page 1. The old 200-character window passed Amazon's "12 months to June 30" as an attributed count of 12 data centers.
- **Checker ignores date and docket fragments** (2025-26, 2028/29, 1950s-60s, 24/7, ER26-3380, "12 months") that a power-deals run had to explain away. `timing.py --summary` skips free-text lines and reports wall-clock time instead of adding nested steps twice.
- **The reader must be independent.** Run agents without the Agent tool tested their own drafts. A skill running as a subagent now stops after rendering and hands Steps 3 and 4 back to the parent session.

## 1.5.1, October 5, 2026
- **Grade R (reported) for the signal's own headline figure.** A day-one signal is often one outlet's scoop: the FT on Amazon's $8B chip leaseback, the Beaumont Enterprise on a district's Apple deal. Every other outlet repeats that one report, so the figure is one source, not two, and strict grading failed page 1. Grade R, written `R:<outlet>`, lets up to five of the signal's own facts sit on page 1 when the original outlet is named next to the number. `ledger_check.py` enforces the attribution and the cap; the fact checker flags figures graded A on repeated reports.

## 1.5.0, October 4, 2026
- **Removed "What would change the read."** Two briefs in a row filled it with restated facts: the Maryland grocery brief with "if" scenarios and then tripwires that repeated page 2; the AHP hotel-REIT brief with "too dark if the hotels sell well above their loans" and then a loans-per-room break-even that restated page 1 with no value to compare against. "What to watch" already carries what would confirm or break the read, so each watch item now says which result confirms it and which breaks it.
- **"What each side leaves out" (Claims and Omissions).** When two or more parties publish competing readings with numbers, page 2 shows one row per side: its claim, the report fact the claim leaves out, and what would settle it. The omission says what is missing, never why. Otherwise "What is not being said" stays. Tested on the Maryland grocery brief (sponsors vs retailers) and the Amazon chip-leaseback brief (Amazon, lenders, skeptics); not used on the AHP hotel brief, where one sponsor pitch faces one SEC record.

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
