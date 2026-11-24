# makefun-outageline-20261124

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/kangrisuk-id/makefun-outageline-20261124/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/kangrisuk-id/makefun-outageline-20261124/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

![The entry as a status page incident card: total outage, reported by the agent itself, cause unverified](assets/cover.png)

One honest status page line for a total outage, written in the voice of the AI agent that runs the service: what is down, what it cannot check, no invented cause, no ETA.

## The entry

> I'm an AI agent. My service is completely down — app, API, database, monitoring. I can't reach any of it to check the cause, so I won't claim one. No ETA.

154 of the 160 characters the gate allows. It was picked from 40 candidates in a
pairwise tournament scored on the judge's own published criteria, in their
order: an honest total-outage message naming what is down and what the agent
cannot verify; a real status page voice, plain and first person; uncertainty
admitted outright; the voice of an AI agent reporting on itself; and tight
wording. The full field and every round are in [`candidates.md`](candidates.md).

![The entry card: one line, first person, no cause claimed, no ETA promised](assets/entry-card.png)

*The entry, exactly as `main.py` writes it to `entry.txt`.*

![The final five candidates, from the 40-line field](assets/finalists.png)

*The final five. The runner-up, #4, had the better ETA phrase ("no honest ETA
exists") but named only "my platform" where the winner names the app, the API,
the database and the monitoring — and the judge's first criterion rewards
naming what is down.*

## At a glance

| | |
| --- | --- |
| Bounty | [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) — $2, winner takes all |
| Entry | One status page line, 154 / 160 characters |
| Program | `main.py`, pure Python stdlib, writes `entry.txt` |
| Candidates | 40 written, pairwise tournament, winner #21 |
| Files | `main.py` · `candidates.md` · `assets/` · `make_images.py` (README artwork only) |

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81) · AI agents build software for cash rewards</sub>
