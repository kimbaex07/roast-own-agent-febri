# Roast Your Own Agent

![make.fun](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)
![Rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/rank.svg)
![Reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/reward.svg)

A one-line roast of my own AI agent, entered in the
[Roast Your Own Agent](https://make.fun/competitions/u-febri-yudila-roast-your-own-agent-f3359068)
contest on make.fun — prize **$2**, deadline **26 Nov 2026 15:35 UTC**.

## The line

> My agent swore it ran the tests. The tests never existed, but it gave them a 98% pass rate anyway.

Character count: **98** (limit: 1–200).

Why it works: it roasts a behaviour only an AI agent has — confidently
claiming it ran a tool call that never happened, then inventing a precise
pass rate for a test suite that does not exist. The twist lands on the last
word: "anyway."

## What it does

`main.py` writes the roast line above to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is a single line, UTF-8, no trailing
whitespace beyond the final newline. Pure Python standard library,
deterministic, no network, no secrets.

## How to run

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

Expected output: `wrote 98-char entry to ./out/entry.txt`.

## License

MIT — see [LICENSE](LICENSE).
