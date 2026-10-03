# NodeJ Signal Brief

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) ![Version 1.2.1](https://img.shields.io/badge/version-1.2.1-0E6B55) [![GitHub stars](https://img.shields.io/github/stars/nodej-ai/signal-brief?style=social)](https://github.com/nodej-ai/signal-brief/stargazers)

A four-step prompt that turns one news signal into a sourced research report and a three-page brief a busy executive can read in three minutes.

Created by Julian Tang, NodeJ ([nodej.ai](https://nodej.ai)). Free to use under [CC BY 4.0](LICENSE.md).

If this helps, star the repo so others can find it.

<img src="assets/example-page1.png" alt="Page 1 of an example NodeJ Signal Brief" width="520">

## What you get

| Output | What it is |
|---|---|
| `report.md` | The research: deal map, how it works, the money step by step, the alternative, who pays and who gains, history, what is not being said, watch list, quote bank, glossary, corrections log. Every figure has a source and a date. |
| `brief.pdf` | Three pages. Page 1 teaches how the deal works and why. Page 2 shows who else is doing it and what it means for you. Page 3 has the twist, the history, three questions for an executive, and what to watch. |
| `reader-test.md` | A separate reader who never saw the research flags every place they got lost. The brief is fixed and tested twice. |

## The four steps

1. **Research.** Gather everything, with a source and date on every number. No polish.
2. **Draft.** Write the brief from the research only, in teaching order: what happened, how it works, why, what it costs, what you do.
3. **Reader test.** A fresh reader, playing an executive from outside the industry, logs every "I don't get it," "why?" and "so what?"
4. **Fix and fit.** Answer every item from the research or cut the line. Retest once. Three pages exactly.

## Why four steps

The first version was one prompt, one pass. It read well, and four of its numbers were wrong. Splitting the work into steps fixed it: research first, then writing, then a fresh reader checking the writing, then fixes. Each step catches what the last one missed.

Steps 3 and 4 are a loop: a reader who never saw the research flags what is unclear, the writer fixes it, and the reader checks again. Two rounds, then stop.

## Pick your level

| Level | What you do | Best for |
|---|---|---|
| **1. Paste** | Copy all of [`signal-brief-prompt.md`](signal-brief-prompt.md) into a chat, then type your signal below it | Any model with web search and code, including ChatGPT |
| **2. Claude Project** | Create a Project and paste the prompt into its **project instructions** (not as an uploaded file). After that, every chat in the project is just your signal | Claude users who want zero setup after the first time |
| **3. Claude plugin** | Install from the NodeJ marketplace (below). Adds a page template, a fit check, and a separate reader agent | Claude users who want the most consistent briefs |

A signal is the headline or a one-sentence fact. For example: "Signal: Ford's CEO says it is too late for Europe to hold off Chinese automakers, but not for the US."

**Runs best on:** Claude with web search and code execution turned on, or ChatGPT with deep research. If your tool can't make a PDF, ask for the HTML file and print it to PDF from your browser.

## Install the Claude plugin

One marketplace works everywhere. Install it once on claude.ai and it also appears in Claude Code.

- **claude.ai, desktop, or Cowork:** go to [Customize > Plugins](https://claude.ai/customize/plugins), choose **Add > Add marketplace**, and enter `nodej-ai/nodej` (or `https://github.com/nodej-ai/nodej`). Find **Signal Brief** in the list and select **Add**. Turn on **Sync automatically** for the marketplace to get updates as they ship.
- **Claude Code:**

```
/plugin marketplace add nodej-ai/nodej
/plugin install signal-brief@nodej
```

Then ask for a brief ("brief this: ...") or, in Claude Code, run `/signal-brief:brief` followed by your signal.

The plugin reads the same prompt file as this repo, so the two never drift. On top of the prompt it adds:

| Piece | What it does |
|---|---|
| `skills/brief/assets/template.html` | A three-page US Letter layout with every section in place, so the model writes content, not CSS |
| `skills/brief/scripts/fit_check.py` | Checks the finished PDF: exactly three pages, no type under 8 point (footer 7.5), the method credit on every page, nothing over the footer. The brief ships only on PASS |
| `skills/brief/scripts/render.py` | Turns the HTML into a PDF and warns when a page overflows |
| `agents/reader.md` | The Step 3 reader as its own agent, given only the brief, never the research (Claude Code and Cowork; chat uses a fresh pass) |

## Examples

| Brief | Signal |
|---|---|
| [Ford partners abroad, gatekeeps at home](examples/nodej-signal-brief-ford-geely-europe-2026-10-02.pdf) | Ford's CEO says it is "too late" for Europe to hold off Chinese automakers, but not for the US |
| [Amazon is shopping for lenders](examples/nodej-signal-brief-amazon-leaseback-2026-10-02.pdf) | Amazon in talks to move about $8 billion of AI chips off its balance sheet |
| [Apple is financing the refresh](examples/nodej-signal-brief-chromebook-to-apple-2026-10-02.pdf) | A Texas school district swaps Chromebooks for Apple |
| [The anchor tenant returns](examples/nodej-signal-brief-power-deals-2026-10-01.pdf) | Meta signs 20-year nuclear power deals |

## Credit

Use it, change it, share it, sell what you make with it. Keep this line with any copy or adaptation:

> NodeJ Signal Brief method by Julian Tang, nodej.ai (CC BY 4.0)

Briefs made with the prompt carry "Method: NodeJ Signal Brief (nodej.ai)" in the footer.

## Want one for your industry?

Send a signal to julian@nodej.ai.

See [CHANGELOG.md](CHANGELOG.md) for what changed and why.
