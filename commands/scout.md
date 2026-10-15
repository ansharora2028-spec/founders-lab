---
description: venture scout — launch local-market-scout and signal-scout in parallel on the run's contract and write 01-local-market.md and 02-signals.md.
argument-hint: "[run_id] (default: the most recent run)"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, Bash(date *)
---

# /venture:scout

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. Read `ventures/LEDGER.md` if it exists.
2. Run folder: if `$ARGUMENTS` names a run id, use `ventures/runs/<run_id>/`. Otherwise use the most recent folder in `ventures/runs/` (sorted by name). Call it `RUN`.
3. Confirm `RUN/00-contract.md` exists and its Confirmation section says `confirmed by user: yes`. If not, tell the user to run `/venture:intake` and stop.

## 1. Progress note
Print one line: `Scouting <target market> — 2 research agents in parallel (paid stage: web search).`

## 2. Launch both scouts in ONE message (parallel)
Use the Agent tool twice in the same message:

- `subagent_type: venture:local-market-scout`
- `subagent_type: venture:signal-scout`

Each prompt contains **only** file paths and the output path, in this form (no chat context, no summary of the contract):

```
Run folder: <absolute RUN path>
Input files (read only these):
- <RUN>/00-contract.md
- <project>/ventures/LEDGER.md        (omit this line if the ledger does not exist)
Output file (write exactly this one file):
- <RUN>/01-local-market.md            (signal-scout: <RUN>/02-signals.md)
Today's date: <YYYY-MM-DD>
Timestamp: <output of date -u +%Y-%m-%dT%H:%M:%SZ, run just before this call>
```

If the contract's starting point is path (a), add one line: `Focus: research the market for the user's stated idea in 00-contract.md § Starting point, not a broad search.` For path (b): `Focus: stay within the space stated in 00-contract.md § Starting point.`

## 3. Log and check
1. Append two rows to `RUN/run-log.md` § Agent calls with the exact paths passed and the output path. Add a Stages row `scout — done`.
2. Check both output files exist and have front matter. If one is missing, re-run that agent once; if it fails again, tell the user and stop.
3. Show the user each agent's short summary, and the local coverage score from `01-local-market.md`. If coverage is below 5, say plainly: "Local data is thin for <place>; confidence in later verdicts will be lower."

Next step: `/venture:generate`.
