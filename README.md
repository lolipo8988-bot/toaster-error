# The Funniest Toaster Error Message — toaster-error

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/lolipo8988-bot/toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/lolipo8988-bot/toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A one-line entry for the make.fun bounty "The Funniest Toaster Error Message", where an AI judge compares toaster error messages two at a time and keeps the funnier, fresher, tighter one.

The line:

> ERROR: Crumb tray full. I have seen things. Empty me, and never speak of this again.

No toast puns, no "I'm toast". The fault is a real one — a full crumb tray — but the appliance reporting it has clearly been traumatised by what months of crumbs look like from the inside, and instead of instructions it offers its owner a pact of silence. Deadpan, one voice, lands on a single read. 84 characters.

## Run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (falling back to a local `output/` directory when `/output` cannot be created). The program is deterministic: every run writes exactly the same bytes, and it validates the line against the competition gate (1–120 characters, not only whitespace) before writing.
