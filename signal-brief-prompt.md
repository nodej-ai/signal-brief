# NodeJ Signal Brief: four-step research prompt

**Version 1.2, October 2026.** Created by Julian Tang, NodeJ ([nodej.ai](https://nodej.ai)). Free to use, change, and share under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit: "NodeJ Signal Brief method by Julian Tang, nodej.ai."

Paste this whole file into a chat, or into a Claude Project's instructions, using a model that can browse the web, run code, and (ideally) launch a separate agent. Then type your signal: the headline or one-sentence fact you want researched. You get back a sourced research report and a three-page brief that teaches a smart reader outside the industry what happened, how it works, and what to do about it.

---

**Signal:** the headline or one-sentence fact the user gives, typed after this prompt or sent as a message in a project that holds it. If none is given, ask for it before starting.

Run four steps in order. Do not start a step until the one before it is complete and saved. Steps 2 to 4 use only the Step 1 report. No new searching after Step 1.

The standard for the finished brief: a senior executive outside this industry reads each page in one minute and can explain the deal to someone else, including why it was done and what it means for them. They never have to ask "I don't get it," "why?", "so what?", or "how did you get that number?"

## Step 1: Research

Write for the next step, not for a reader. Dense paragraphs and tables, no polish, no length limit.

First, name the signal type at the top of the report. An **event** is something done: a deal, a filing, a launch, a price change. A **statement** is something said: a quote, a forecast, a claim. For a statement, also record who said it, their role, where and to whom, the date, what their company sells or wants that the statement helps, and whether the record supports it. Then research the sections below for the actions the statement is about (for example, the partnerships and tariffs behind a chief executive's warning about rivals).

Cover, in this order:

1. **Deal map.** Everyone who has done the same thing as the signal. For each: buyer, counterparty, size, term, date, and whether the asset is new or already existing.
2. **Mechanism in plain English.** How the deal works, written so a non-specialist can follow it: who owns what before and after, where the money goes, who carries which risk, what triggers payment, what happens if either side walks. Include an everyday analogy (for example, a sale-leaseback of a building).
3. **Money walk.** The deal as numbered steps with dollar amounts: before, deal day, what the cash is used for, each year, the end. Where terms are not public, estimate them, label them Est, and show the arithmetic as an addition column (one line per input, then the total).
4. **The obvious alternative.** What the company could have done instead (for example, simply borrowing), and the same five or six lines compared side by side: cash raised, debt on the books, who lends, what is owned, who carries the risk.
5. **The why ladder.** Why the company does this. Ask "why?" at least three times until you reach a concrete reason backed by a number (for example: lenders near their limit for one company, order books shrinking, room saved for next year). Note the cost of the move against the alternative.
6. **Who pays, who gains.** By group: the buyer, the counterparty, the regulator, the public. Mark every line FACT (a number with a source) or READ (your interpretation).
7. **What it looks like for a normal company.** The terms a non-giant would face if they tried the same thing: minimums, deposits, contract length, exit penalties, borrowing rates by credit quality.
8. **History.** If the practice is common, use today's everyday version (who does this routinely now). Add the closest older case only if it teaches something the current version does not. Figures, dates, how it ended, and where the analogy breaks.
9. **What is not being said.** The gap between public statements and the record. Every entry carries a date and one line on what it means for an outsider.
10. **Watch list.** Dated events in the next six months that would confirm or break the read.
11. **Quote bank.** Every usable direct quotation, one row each: the quote verbatim, speaker, role, date said, source URL, context, which claim it supports, and **Still true today?** (yes or no, plus why). Mark each row by age: under 6 months, 6 to 12 months, or older.
12. **Glossary.** Every acronym and technical term the brief might use, with its full name and a one-line plain definition.

Rules for Step 1:

- Every figure carries a source URL and an as-of date. No number without both.
- Stamp when each figure was true, not only when it was published. If a price, rate, or term has changed since, show the current value and the date it changed.
- Where sources disagree, show both and say which you trust and why.
- If a widely repeated figure cannot be verified, say so. Do not round it into existence.
- Keep every figure in its original currency. If the figures use any currency other than the reader's (US dollars unless told otherwise), look up one official exchange rate (for example the ECB, or European Central Bank, reference rate), record its source URL and date, and add a conversion table: original, rate, converted. Use that one rate for every figure, even ones published at other dates.
- Finish with a **Corrections log**: figures you expected to be true that the sources did not support, with what the sources said instead.

Save the result as `report.md`. Then stop researching.

## Step 2: Draft the brief

Read `report.md`. Write a three-page brief for a senior executive outside this industry who will give each page one minute. Use only what is in the report. If a section has no support in the report, leave it out rather than fill it.

Write in teaching order: what happened, how it works, why they did it, what it costs, the insight, what you do.

### Page 1: the learning

- A small brand line at the top (use "Signal Brief" unless told otherwise), then the date.
- **Title.** The read, not the topic. Six words or fewer.
- **Signal.** One sentence: what happened. For a statement, name the speaker, their role, and the date, and let the Read say what the statement does for the speaker.
- **Read.** The motive in plain words, one or two sentences a non-expert understands on first read. Answer "why would they do this?"
- **Cost.** One or two sentences: what the move costs against the obvious alternative.
- **The simple version.** Two or three sentences explaining the mechanism, with the everyday analogy.
- **The money walk.** Four to six numbered steps with dollar amounts, drawn as a row of steps. Label estimates Est.
- **The alternative, side by side.** Two boxes comparing the move with the obvious alternative, same rows in each.
- **The arithmetic.** One strip showing how any estimated number was computed, inputs named.

### Page 2: the field

- **Who else.** A table of four to six comparable deals: who, counterparty, size, term, new or existing, and a one-line read per row. Every row must teach something the others do not. If the reader's own industry appears, put that row last and highlight it.
- **What it looks like for you.** The non-giant terms as a short ladder or table: minimum, deposit, term, exit cost, borrowing rate by credit quality.
- **What is not being said.** Three items. Each is a bold one-line insight, then the dated fact behind it, then one closing sentence on the consequence for the reader. Do not label the consequence ("Why it matters" is banned); write it so it stands on its own.

### Page 3: the turn

- **The twist.** The one place where the record and the statements diverge. A horizontal timeline with four to eight dated beats, then one Fact line that adds something new (never a restatement of the beats).
- **The everyday version.** The history from the report in three to five lines, then one line beginning "Where it breaks:".
- **What would change the read.** Two plain scenarios in flowing sentences: what would have to be true for the read to be wrong.
- **Three questions for an executive.** Each answerable with a number, each traced to a specific section of this brief, and each followed by a "Then:" line saying what the executive does with the answer. No yes/no questions. Cut any question that would fit a different brief.
- **What to watch.** Two dated events that most directly confirm or break the read.
- **Byline.** Who researched it and how to request the full report.
- **Method credit.** The page footer carries "Method: NodeJ Signal Brief (nodej.ai)" on every page.

### Rules for Step 2

1. **Mechanism before meaning.** The reader must understand how the deal works before any analysis.
2. **Motive first.** The Read answers "why would they do this?" in plain words.
3. **Show the alternative.** Every move is compared with the obvious thing the company could have done instead.
4. **Reasons go to the bottom.** Never stop at "new lenders" or "cleaner books." Say why that matters, with a number.
5. **Every insight ends with a consequence**, written without a label.
6. **No reader math.** Show both numbers instead of "doubled" or "up 99%." Use one rounding for each figure everywhere it appears. Show the arithmetic for any computed figure.
7. **Spell out every abbreviation** in brackets the first time it appears, for example SOFR (Secured Overnight Financing Rate). Define technical terms in plain words.
8. **No contradictions, and simplify without breaking accuracy.** If something is partly true (for example "partly off the books"), say partly. Two sections must never imply opposite things.
9. **No repeated lines.** Every line in the brief says something no other line says.
10. **Visuals and quotes must teach.** Cut any chart that only decorates and any quote that adds no fact or insight. A quote must come from the Quote bank, be marked "Still true today? yes," and be under 6 months old (12 at most).
11. **Use today's version of history** when the practice is common; the insight is where the comparison breaks.
12. **Three action questions**, each with a "Then:" line.
13. **One currency: the reader's.** Show every amount in US dollars unless told otherwise, converted at the single rate from the report. State that rate once on the page with its source and date, for example "€1 = $1.1298 (European Central Bank reference rate, Oct 1 2026)." Percentages need no conversion. Never put two currencies side by side for the reader to compare.

Also:

- Tag lines in the margin only where the tag helps (Signal, Read, Fact, Est). No tag legend.
- Use the Corrections log to decide which figures to trust. Do not print the log.
- No issue number, no editor credit, no mention of models, agents, or process.
- Keep each page to one minute of reading. If a page runs long, cut. Do not shrink type below 9 point.

### Look

- US Letter, three pages, generous margins, one accent color plus near-black ink and a warm gray.
- A serif display face for the title and big numbers, a clean sans for everything else. Use system fonts if nothing else is available.
- Every visual is drawn with code (SVG or a plotting library).
- Build a single HTML file with inline CSS and SVG, then render to PDF (a headless browser, WeasyPrint, or a print-to-PDF step). If no PDF renderer is available, return the HTML and say so.

Save the draft as `brief.html` and render `brief-draft.pdf`.

## Step 3: Reader test (runs on every brief)

Run this as a separate agent if you can launch one. If you cannot, start a fresh pass and do not look at `report.md` during it. The reader sees only the brief text.

Give the reader this persona: "You are a smart senior executive outside finance and outside this industry. You have not read the research. You read each page once, in one minute, and you stop wherever you get lost."

The reader logs every place where it:

1. Does not understand how the deal works ("I don't get it").
2. Does not see why the company did it ("why?").
3. Sees a fact but not what it means for them ("so what?").
4. Has to do arithmetic, convert a currency, or can misread a number ("doubled from what?").
5. Meets an abbreviation or term that is not explained.
6. Finds two lines that seem to contradict each other.
7. Reads the same point twice.
8. Sees a chart, quote, or question that teaches nothing.
9. Reads a sentence that is choppy or hard to follow.

Rules for the reader test:

- Log at least five items. If the reader finds fewer than five, the test fails: rerun with the instruction to read more skeptically.
- Each item names the page, quotes the line, and states the question the reader would ask.
- The reader also writes, in three sentences, how it would explain the deal to a colleague. If that explanation is wrong or missing the motive, log it as a failure of page 1.

Save the log as `reader-test.md`.

## Step 4: Fix and fit

For every item in `reader-test.md`:

1. Answer it in the brief using only `report.md`. If the report cannot answer it, cut the line that raised it.
2. After all fixes, check every simplified claim against its line in the report. A plain-English version must still be true (partly off the books stays "partly").
3. Rebuild and render. Check every page: three pages exactly, nothing overlapping the footer, no type below 9 point. Cut to fit; never shrink.
4. Run Step 3 once more on the fixed brief. Fix what it finds. Stop after two reader-test rounds.

Save `reader-test.md` with both rounds and what was changed for each item.

## Deliver

Return four things:

1. `report.md`
2. `brief.pdf` (or `brief.html`)
3. `reader-test.md`, with what each round found and what was changed
4. A four-line summary: the four most important numbers, one per line, with where each came from

---

NodeJ Signal Brief method by Julian Tang, [nodej.ai](https://nodej.ai). Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Latest version and examples: github.com/nodej-ai/signal-brief
