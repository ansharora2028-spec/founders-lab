---
description: venture generate — run generator then screener, pick the top N ideas by screen score, have both prosecutors write kill criteria from the raw ideas in parallel, merge them into kill-criteria.md and lock it (chmod 444 + SHA-256 in run-log) before any forging.
argument-hint: "[run_id] (default: the most recent run)"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *)
---

# /venture:generate

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. Read `ventures/LEDGER.md` if it exists.
2. Read the `kill-criteria.md` and `run-log.md` sections of `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`, and its Visibility matrix.
3. `RUN` = `ventures/runs/<$ARGUMENTS>` if a run id is given, else the most recent folder in `ventures/runs/`.
4. Require `RUN/00-contract.md`, `RUN/01-local-market.md`, `RUN/02-signals.md`. If scouting is missing, tell the user to run `/venture:scout` and stop.
5. Read the depth mode from the contract: quick → N=2, standard → N=3, deep → N=5, check → N=1, check+variants → N=2.

All agent prompts below use this form and contain nothing else (no chat context, no summaries of other files):

```
Run folder: <absolute RUN path>
Mode: <mode, if any>
Idea id: <id, if any>
Input files (read only these):
- <path>
- ...
Output file (write exactly this one file):
- <path>
Today's date: <YYYY-MM-DD>
Timestamp: <output of date -u +%Y-%m-%dT%H:%M:%SZ, run just before this call>
```

## 1. Generate
Progress note: `Generating <count> ideas (depth: <mode>).`

Agent `venture:generator` with inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, `ventures/LEDGER.md` (if it exists), the city memory file (if it exists), and, in a second wave, the previous run's `91-nothing-passed.md`; output `03-ideas.md`. Log the call in `run-log.md`.

## 2. Screen
Progress note: `Screening <count> ideas against hard constraints and competitors (paid stage: web search).`

Agent `venture:screener` with inputs `00-contract.md`, `03-ideas.md`, `ventures/LEDGER.md` (if it exists); output `04-screen.md`. **Do not** pass `01` or `02`. Log the call.

## 3. Pick the top N
From `04-screen.md` § Ranking, take the top N non-rejected ideas. If fewer than N survive the screen, take all survivors. If **none** survive, skip to the nothing-passed report (`/venture:blueprint`) — that is a valid outcome.

Path (a): the user's original idea always goes through Screen. It is carried forward only if it ranks in the top N, like any other idea; if it is not carried, tell the user its rank and score.

**Check modes** (`check`, `check+variants`, from `/venture:check`): the user's original idea (I01) is always carried forward unless Screen REJECTS it on a HARD constraint, whatever its score. In `check+variants`, also carry the best-ranked non-rejected variant. A rejected I01 is a verdict, not a failure of the run: report which constraint it breaks.

Show the user every idea, in rank order, explained in plain language, using only what `03-ideas.md` and `04-screen.md` say (add no new claims):

```
I03 — <pitch>  (screen 16/25, carried forward | not carried | rejected: <reason>)
  How it works:      <from the idea's "how it works">
  The need gap:      <from "need gap">
  How it makes money: <from "how it makes money">
```

Then one line saying which ideas are carried forward and why (rank).

## 4. Write kill criteria from the raw ideas — before any forge
Progress note: `Locking kill criteria for <N> ideas — 2 prosecutors per idea in parallel (paid stage).`

For each carried idea `<id>`: `mkdir -p RUN/ideas/<id>`.

Then launch, **in one message**, for every carried idea, both:
- `venture:prosecutor-market`, `Mode: criteria`, inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, `03-ideas.md`, `Idea id: <id>`; output `ideas/<id>/criteria-market.md`;
- `venture:prosecutor-execution`, same inputs, `Mode: criteria`; output `ideas/<id>/criteria-execution.md`.

Log every call with its exact paths.

## 5. Merge and lock
For each carried idea:
1. Write `RUN/ideas/<id>/kill-criteria.md` in the schema: the raw idea block copied verbatim from `03-ideas.md`, then the KM blocks verbatim from `criteria-market.md`, then the KE blocks verbatim from `criteria-execution.md`, then the Lock section. Do not edit, merge, soften or drop any criterion. If a draft has fewer than 3 or more than 6 criteria, re-run that prosecutor once with the note `Your previous draft had <n> criteria; write 3–6.`
2. Lock it:
   ```bash
   chmod 444 "RUN/ideas/<id>/kill-criteria.md"
   sha256sum "RUN/ideas/<id>/kill-criteria.md"   # or: shasum -a 256 "<path>"
   ```
3. Append a row to `run-log.md` § Locks: idea, path, sha256, and the time from `date -u +%Y-%m-%dT%H:%M:%SZ`.

Add a Stages row `generate — <n> ideas, <k> carried, criteria locked`.

## 6. Report
Show the carried ideas with their pitches and the number of locked criteria each. Do **not** show the criteria text to the user in a way that will be repeated to Forge; Forge never sees it. Next step: `/venture:forge`.
