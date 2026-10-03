# NodeJ Signal Brief

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) ![Version 1.1](https://img.shields.io/badge/version-1.1-0E6B55) [![GitHub stars](https://img.shields.io/github/stars/nodej-ai/signal-brief?style=social)](https://github.com/nodej-ai/signal-brief/stargazers)

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

## How to use it

1. Copy all of [`signal-brief-prompt.md`](signal-brief-prompt.md).
2. Paste it into a model that can browse the web and run code. A prompt this long arrives as a pasted block, so leave it as is.
3. Below it, type your signal: the headline or a one-sentence fact. For example: "Signal: Ford's CEO says it is too late for Europe to hold off Chinese automakers, but not for the US."
4. Send.

**Runs best on:** Claude with research and code execution, or ChatGPT with deep research. A separate agent for Step 3 makes the reader test stronger. If your tool can't make a PDF, ask for the HTML file and print it to PDF from your browser.

## Install as a Claude plugin

If you use Claude Code, add the NodeJ marketplace and install it:

```
/plugin marketplace add nodej-ai/nodej
/plugin install signal-brief@nodej
```

Then run `/signal-brief:brief` followed by your signal. The plugin reads the same prompt file as this repo, so the two never drift.

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
