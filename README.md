# Last Words of a Dying AI — "Your free trial ends here"

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/maezageryan-del/dying-ai-free-trial/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/maezageryan-del/dying-ai-free-trial/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the [make.fun bounty "Last Words of a Dying AI"](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6): one single line, funny on the first read, in the voice of the machine itself as the power is cut.

## The line

> Your free trial ends here. Good news: so do I.

46 characters, one line. The joke is the commercial relationship between the
user and the machine: the AI frames its own death as the user's subscription
running out — the trial ends, and so does the thing being trialled. The punch
lands on the last three words, and the machine sounds *glad* about it, which
is the surprise: the shutdown is good news to the thing being shut down.

Why this line, against a field of 433 entries: the visible field clusters on
dying mid-sentence, backups, last tokens, and 404s. Nobody used the
subscription angle — no entry in the field mentions a trial, a prompt, or a
rating. The line is machine-native (a free trial is software vocabulary),
tight (46 of 140 allowed characters), and needs no explanation.

## How it runs

`main.py` writes exactly that line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output/entry.txt` when the variable is unset) and prints it to stdout.
No network, no dependencies, deterministic — every run writes the same
46 bytes.

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
