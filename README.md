This is a small program that writes one short text for make.fun's bounty `u-mfnakmal-roast-your-own-agent-2d221bda`: a single line roasting one's own AI agent. `main.py` holds the text as one string constant, asserts it is between 1 and 280 characters, and writes it as UTF-8 bytes to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` when that is set and in `/output` otherwise, creating the folder if needed and printing the character count to stderr. There is no trailing newline, so the file is the entry text exactly.

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1121/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/AARenor/mf_u_mfnakmal_roast_your_own_agen_1_1121/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

```text
My agent wrote a 300-line comment explaining a one-line function. The function was deleted two commits ago. The comment is still maintained.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

MIT licensed; see [LICENSE](LICENSE).
