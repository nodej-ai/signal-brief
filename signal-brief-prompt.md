# NodeJ Signal Brief: four-step research prompt

**Version 1.5.0, October 2026.** Created by Julian Tang, NodeJ ([nodej.ai](https://nodej.ai)). Free to use, change, and share under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Credit: "NodeJ Signal Brief method by Julian Tang, nodej.ai."

Paste this whole file into a chat, or into a Claude Project's instructions, using a model that can browse the web, run code, and (ideally) launch a separate agent. Then type your signal: the headline or one-sentence fact you want researched. You get back a sourced research report and a three-page brief that teaches a smart reader outside the industry what happened, how it works, and what to do about it.

---

**Signal:** the headline or one-sentence fact the user gives, typed after this prompt or sent as a message in a project that holds it. If none is given, ask for it before starting.

Run four steps in order. Do not start a step until the one before it is complete and saved. Steps 2 to 4 use only the Step 1 report. No new searching after Step 1.

**File names.** Pick a slug of two to five lowercase words naming the companies and the subject (for example `ford-geely-europe`) and name every file `signal-brief-<slug>-<YYYY-MM-DD>`, shortened below to `<name>`: `<name>-report.md`, `<name>.html`, `<name>.pdf`, `<name>-reader-test.md`, `<name>-fact-check.md`, `<name>-timing.log`.

**Timing.** At the start and end of every step, append one line to `<name>-timing.log`: the current time from the system clock (use code), the step, `start` or `end`, and lookups used so far (a lookup is one web search or one page fetch).

The standard for the finished brief: a senior executive outside this industry reads each page in one minute and can explain the deal to someone else, including why it was done and what it means for them. They never have to ask "I don't get it," "why?", "so what?", or "how did you get that number?"

## Step 1: Research

Write for the next step, not for a reader. Dense paragraphs and tables, no polish.

**Research to a budget, and stop when done.** Each part below has a lookup ceiling and a "done when" line. Each part answers its must-find items first (see "Signal type and must-find" below). Stop a part as soon as its "done when" is met. If it hits its ceiling first, stop, write **GAP** and what is missing, and move on. Never pad. Research budget: 40 lookups. Two small allowances follow at the end of Step 1: up to 3 lookups for the freshness check and up to 10 for grade upgrades. Hard cap for the whole run: 55 lookups.

| Part | Sections | Ceiling | Done when |
|---|---|---|---|
| A. Deals | 1, 7 | 12 | Four to six comparable deals, each with buyer, counterparty, size, term, date, new or existing, from a primary or named source; the normal-company terms are filled |
| B. Mechanism and money | 2, 3, 4, 5, 6 | 10 | The must-find items are answered or marked not disclosed, the money walk is complete, every estimate has its inputs, and the alternative is compared line by line |
| C. History | 8 | 6 | One current everyday version and where it breaks |
| D. Statements | signal type, 9, 10, 11 | 12 | Three dated "not being said" items, two watch dates, and every quote checked as still true |

If you can launch separate agents, run A to D in parallel, one agent each, and have each write its sections in the final report format so joining them needs no rewriting. Then write the Figures ledger, Estimates, Glossary, and Corrections log yourself with no new lookups. If you cannot launch agents, run A to D in order with the same ceilings.

**Signal type and must-find.** First, name the signal type at the top of the report. Then answer that type's must-find items before anything else, and put them in a must-find table at the top of the report: item, answer, and ledger ID (or "not disclosed"). Spend at most 3 lookups on any one item. After that, "not disclosed" is a valid answer, and the brief says so instead of presenting an estimate as fact. One exception: the cost of the alternative is never "not disclosed." If no source states it, build an estimate from public inputs (for example, the statutory severance rule times the headcount), label it Est, and put its formula in the Estimates table.

| Type | What it is | Must-find (answer first) |
|---|---|---|
| Event | Something done: a deal, a filing, a launch, a price change | 1. The price. 2. Who pays and who receives the cash. 3. What each side owns before and after. 4. Term and exit terms. 5. The cost of the alternative (section 4) |
| Statement | Something said: a quote, a forecast, a claim | 1. The verbatim words, speaker, role, venue, audience, and date. 2. The dated action by the speaker's company that the statement defends or is about. 3. That action's money terms (event items 1 to 3). 4. What the speaker's company sells or wants that the statement helps. 5. Whether the record supports the statement |
| Policy | A tariff, rule, law, or ruling | 1. The rate or rule, in its own words. 2. Effective date and any change since. 3. Who is exempt. 4. The first enforcement case. 5. What it stacks on or replaces |
| Market data | A share, price, ranking, or count reaching a level | 1. The exact definition (whole market or one segment) and coverage. 2. The same data series one year earlier. 3. Who publishes it and how often. 4. The driver the publisher names. 5. The nearest competing series and how it differs |

For a statement, research the sections below for the action the statement is about (for example, the partnership behind a chief executive's warning about rivals). If the statement is about a tariff, rule, or law, part D also answers the policy must-finds 2 and 3 for that rule: effective date and any change since, and who is exempt. Exemptions are where the record most often breaks from the statement. If the speaker's company has no concrete, dated action on the subject in the last 12 months, say so at the top of the report; the brief then uses the claim-vs-record layout (Step 2). For market data, use one data series for every point you compare; never mix series.

Cover, in this order:

1. **Deal map.** Everyone who has done the same thing as the signal. For each: buyer, counterparty, size, term, date, and whether the asset is new or already existing.
2. **Mechanism in plain English.** How the deal works, written so a non-specialist can follow it: who owns what before and after, where the money goes, who carries which risk, what triggers payment, what happens if either side walks. Include an everyday analogy (for example, a sale-leaseback of a building).
3. **Money walk.** The deal as numbered steps with dollar amounts: before, deal day, what the cash is used for, each year, the end. Where terms are not public, estimate them, label them Est, and show the arithmetic as an addition column (one line per input, then the total).
4. **The obvious alternative.** What the company would have done with the same asset or decision if this deal had not happened: close it, sell it, keep it idle, borrow, or build alone. Pick a concrete option with a cost, never a strategy label like "compete harder." For a statement, it is the concrete action the opposite stance would require. Compare the same five or six lines side by side: cash in or out, debt on the books, who funds it, what is owned, who carries the risk.
5. **The why ladder.** Why the company does this. Ask "why?" at least three times until you reach a concrete reason backed by a number (for example: lenders near their limit for one company, order books shrinking, room saved for next year). Note the cost of the move against the alternative.
6. **Who pays, who gains.** By group: the buyer, the counterparty, the regulator, the public. Mark every line FACT (a number with a source) or READ (your interpretation).
7. **What it looks like for a normal company.** The terms a non-giant would face if they tried the same thing: minimums, deposits, contract length, exit penalties, borrowing rates by credit quality. If three or more of those would be "not disclosed," research instead what a smaller company pays or must do under the public rules the signal touches: duties, filings, deadlines, penalties, borrowing rates. If no smaller-company version exists (for example, a sovereign policy), research who the move reaches next: suppliers, customers, or the reader's own sector.
8. **History.** If the practice is common, use today's everyday version (who does this routinely now). Add the closest older case only if it teaches something the current version does not. Figures, dates, how it ended, and where the analogy breaks.
9. **What is not being said.** The gap between public statements and the record. Every entry carries a date and one line on what it means for an outsider. Where two or more parties publish competing readings of the signal, each with a number, also record each side's headline claim (quoted, with source) and the report fact it leaves out.
10. **Watch list.** Dated events in the next six months that would confirm or break the read.
11. **Quote bank.** Every usable direct quotation, one row each: the quote verbatim, speaker, role, date said, source URL, context, which claim it supports, and **Still true today?** (yes or no, plus why). Mark each row by age: under 6 months, 6 to 12 months, or older.
12. **Glossary.** Every acronym and technical term the brief might use, with its full name and a one-line plain definition.

Rules for Step 1:

- Every figure carries a source URL and an as-of date. No number without both.
- **Figures ledger.** Put every figure the brief might print in one table with these columns, in this order: `ID | Figure | Value | Unit | USD | As of | Grade | Source URL | Exact sentence`. ID is F1, F2, and so on. Value and USD are plain numbers with no symbols or commas (221000000, not €221M); USD is blank for figures that are not money. Exact sentence is the sentence from the source, word for word, that contains the figure.
- **Grade every figure.** A: a primary source (a filing, the company, a regulator, official statistics) or two independent sources that agree. B: one reputable secondary source. C: one weak source, or not verified. Grade C figures never appear in the brief.
- **Check the current value.** Every figure that could go on page 1 is confirmed current at its primary source, inside the grade-upgrade allowance below.
- **Estimates table.** Every computed figure goes in a second table: `ID | Figure | Formula | Result`. ID is E1, E2, and so on. Formula uses ledger IDs and plain numbers only, for example `F3 * 0.288 * 80000`. Result is a plain number.
- Stamp when each figure was true, not only when it was published. If a price, rate, or term has changed since, show the current value and the date it changed.
- Where sources disagree, show both and say which you trust and why.
- If a widely repeated figure cannot be verified, say so. Do not round it into existence.
- Keep every figure in its original currency. If the figures use any currency other than the reader's (US dollars unless told otherwise), look up one official exchange rate (for example the ECB, or European Central Bank, reference rate), record its source URL and date, and add a conversion table: original, rate, converted. Use that one rate for every figure, even ones published at other dates.
- Finish with a **Corrections log**: figures you expected to be true that the sources did not support, with what the sources said instead.

**Freshness check (up to 3 lookups).** After parts A to D, search for news on every item the report calls pending, proposed, upcoming, or under negotiation, on every watch-list date, and on the signal itself (retracted, clarified, or overtaken). Search from the signal date to today, or the last 7 days if that is longer. Skip this step when the signal is under 48 hours old. A freshness result can add a dated update with its source. It never deletes a primary-source figure. If the update is paywalled or unconfirmed, mark it "unconfirmed as of <date>."

**Grade upgrades (up to 10 lookups).** Then spend at most 10 lookups lifting figures below grade A that page 1 depends on: the Read, the Cost, the money walk, and the picture. Two tries per figure; if it cannot reach grade A, it stays off page 1. When a grade A source and a lower-grade source disagree, the newest primary source wins: use it with its date and log the other in the Corrections log.

**Lookup cap.** Stop all searching at 55 lookups, whatever is left, and record the total in the timing log.

Save the result as `<name>-report.md`. Then stop researching.

## Step 2: Draft the brief

Read `<name>-report.md`. Write a three-page brief for a senior executive outside this industry who will give each page one minute. Use only what is in the report. If a section has no support in the report, leave it out rather than fill it.

Write in teaching order: what happened, how it works, why they did it, what it costs, the insight, what you do.

### Page 1: the learning

- A small brand line at the top (use "Signal Brief" unless told otherwise), then the date.
- **Title.** The read, not the topic. Six words or fewer.
- **Signal.** One sentence: what happened. For a statement, name the speaker, their role, and the date, and let the Read say what the statement does for the speaker.
- **Read.** The motive in plain words, one or two sentences a non-expert understands on first read. Answer "why would they do this?"
- **Cost.** One or two sentences: what the move costs against the obvious alternative. Name who pays whom and how much, or say the amount is not disclosed.
- **The simple version.** Two or three sentences explaining the mechanism, with the everyday analogy.
- **The picture.** One bar that shows the core proportion at a glance: used against capacity, part against whole, or before against after. Both numbers come from the Figures ledger or Estimates. Its heading states the takeaway in eight words or fewer (for example "Four in five slots sit empty"). Draw an estimate hatched, never solid.
- **The money walk.** Four to six numbered steps with dollar amounts, drawn as a row of steps. Label estimates Est.
- **The alternative, side by side.** Two boxes comparing the move with the obvious alternative, same rows in each.
- **The arithmetic.** One strip showing how any estimated number was computed, inputs named.

**Claim-vs-record layout.** Use it only for a statement signal when the report says the speaker's company has no dated action on the subject. Replace the picture, money walk, alternative, and arithmetic with two blocks. **The claim against the record:** three to five rows, each a part of the claim, the dated record that bears on it, and a verdict (supports, contradicts, or silent). **What acting on it would cost:** one strip with the most relevant money figure, its inputs, and its source. Pages 2 and 3 stay the same.

### Page 2: the field

- **Who else.** A table of four to six comparable deals: who, counterparty, size, term, new or existing, and a one-line read per row. Every row must teach something the others do not. If the reader's own industry appears, put that row last and highlight it.
- **What it looks like for you.** The non-giant terms as a short ladder or table: minimum, deposit, term, exit cost, borrowing rate by credit quality. If the report switched section 7 to public-rule costs or to who the move reaches next, use those rows and retitle the section to match. Print "not disclosed" at most once in this section.
- **What each side leaves out** (the method calls this Claims and Omissions). Use it when two or more parties publish competing readings of the signal, each with a number. A table with one row per side (two or three sides) and four columns: Side (named by role, never by party) | Claim (their headline number or line, from the Quote bank or ledger) | Omission (the report fact their claim leaves out, with its source) | What settles it (the one fact or document that would decide it). Each side gets exactly one claim and one omission. The omission states what is missing, never why it was left out. If no two parties publish competing readings, use the next section instead.
- **What is not being said.** Use when "What each side leaves out" does not apply. Three items. Each is a bold one-line insight, then the dated fact behind it, then one closing sentence on the consequence for the reader. Do not label the consequence ("Why it matters" is banned); write it so it stands on its own.

### Page 3: the turn

- **The twist.** The one place where the record and the statements diverge. A horizontal timeline with four to eight dated beats, then one Fact line that adds something new (never a restatement of the beats).
- **The everyday version.** The history from the report in three to five lines, then one line beginning "Where it breaks:".
- **Three questions for an executive.** Each answerable with a number, each traced to a specific section of this brief, and each followed by a "Then:" line saying what the executive does with the answer. No yes/no questions. Cut any question that would fit a different brief.
- **What to watch.** Two dated events that most directly confirm or break the read. Each says which way it moves the read: what result confirms it, what result breaks it.
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

14. **Only graded numbers.** Every number on the page comes from the Figures ledger (grade A or B) or the Estimates table. Page 1 uses grade A figures and estimates only. Fewer numbers are better than weaker ones.

**Word budgets.** Write to these limits the first time; they are sized so each page fits without trimming later. Title 6 words. Signal 35. Read 45. Cost 40. Simple version 60. Picture heading 8. Each money-walk step 18. Each alternative box 5 rows of 6 words. Arithmetic strip 5 inputs. Who-else read 14 per row. Each "not being said" item 45. Each "leaves out" row 45. Claim-vs-record rows 20 words each. Twist beats 6 words each. Everyday version 70. Each question 25, each "Then:" 20. Each watch item 20.

Also:

- Tag lines in the margin only where the tag helps (Signal, Read, Fact, Est). No tag legend.
- Use the Corrections log to decide which figures to trust. Do not print the log.
- No issue number, no editor credit, no mention of models, agents, or process.
- Keep each page to one minute of reading. If a page runs long, cut. Type sizes: body text at least 9.5 point; labels, margin tags, chart text, and table headers at least 8 point; the footer at least 7.5 point. Never shrink type to fit.

### Look

- US Letter, three pages, generous margins, one accent color plus near-black ink and a warm gray.
- A serif display face for the title and big numbers, a clean sans for everything else. Use system fonts if nothing else is available.
- Every visual is drawn with code (SVG or a plotting library).
- Build a single HTML file with inline CSS and SVG, then render to PDF (a headless browser, WeasyPrint, or a print-to-PDF step). If no PDF renderer is available, return the HTML and say so.

Save the draft as `<name>.html` and render `<name>.pdf`.

## Step 3: Reader test and fact check (run both, at the same time if you can)

Two separate checks. The reader tests whether the brief is clear. The fact checker tests whether it is true. Run each as a separate agent if you can, in parallel. If you cannot, run the reader first as a fresh pass that does not look at the report, then the fact check.

### The reader

The reader sees only the brief text, never the report.

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

Save the log as `<name>-reader-test.md`.

### The fact checker

The fact checker sees the brief and the report. For every number and every factual claim in the brief, it finds the ledger row, estimate, or report line behind it and logs each place where:

1. A number has no ledger or estimate row, or does not match it after rounding.
2. A number comes from a grade C row, or page 1 uses a grade B row.
3. A simplification changed the meaning (partly became fully, an estimate reads as a fact, a forecast reads as a done deal).
4. A claim has no support in the report.
5. A date, name, or role differs from the report.
6. The Cost line does not name who pays whom and how much, or say the amount is not disclosed.
7. A must-find answer on page 1 is an estimate presented as fact, or has no source.
8. An item the report calls pending is stated without the freshness-check result, so it may be stale.

Each item names the page, quotes the line, and gives the ledger ID or report line it checked. Save it as `<name>-fact-check.md`.

## Step 4: Fix and fit

For every item in `<name>-reader-test.md` and `<name>-fact-check.md`:

1. Answer it in the brief using only the report. If the report cannot answer it, cut the line that raised it. Fact-check items are fixed or cut, never argued.
2. After all fixes, check every simplified claim against its line in the report. A plain-English version must still be true (partly off the books stays "partly").
3. Recompute every estimate from its formula and confirm the brief shows the same result after rounding.
4. Rebuild and render. Check every page: three pages exactly, nothing overlapping the footer, no type below the sizes above. Cut to fit; never shrink.
5. Run the reader once more only if its three-sentence explanation in round 1 was wrong or missed the motive. Otherwise one round is enough.

Add what was changed for each item to `<name>-reader-test.md` and `<name>-fact-check.md`.

## Deliver

Return six things:

1. `<name>-report.md`
2. `<name>.pdf` (or `<name>.html`)
3. `<name>-reader-test.md`, with what the reader found and what was changed
4. `<name>-fact-check.md`, with what the fact checker found and what was changed
5. `<name>-timing.log`, ending with the lookup total against the 55 cap
6. A four-line summary: the four most important numbers, one per line, each with its ledger ID, grade, and source

---

NodeJ Signal Brief method by Julian Tang, [nodej.ai](https://nodej.ai). Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Latest version and examples: github.com/nodej-ai/signal-brief
