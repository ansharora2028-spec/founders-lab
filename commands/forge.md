---
description: venture forge — for every carried idea with locked kill criteria, run forge (sharpen, no persuasion), then the independent market-strategist (full framework check, CARRY or DROP), then economics-modeler (three scenarios plus simulation inputs), then the seeded simulation. Forge and strategist never receive kill-criteria.md.
argument-hint: "[run_id] [idea_id ...] (default: most recent run, all carried ideas not yet forged)"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, Bash(date *), Bash(python3 *)
---

# /venture:forge

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. Read the Visibility matrix in `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`.
2. Arguments: `$ARGUMENTS`. The first argument that matches a folder in `ventures/runs/` is the run id; otherwise `RUN` = the most recent run folder. Remaining arguments are idea ids.
3. Ideas to forge: the given ids, or every `RUN/ideas/<id>/` that has a `kill-criteria.md` and no `forge-v1.md`.
4. **Lock check:** for each idea, confirm `kill-criteria.md` exists and its hash is recorded in `run-log.md` § Locks. If it is not locked, stop: criteria must be locked before forge (rule 2). Run `/venture:generate` first.

This command runs **round 1** only. Round 2 forging happens inside `/venture:kill` on a REVISE verdict.

The ideas file for an idea is `03-ideas.md`, or `03-ideas-pivot<k>.md` for a pivoted idea (`<old-id>-P<k>`).

## 1. Forge (all ideas in parallel)
Progress note: `Forging <n> idea(s) (paid stage: web research).`

In **one message**, for each idea launch `venture:forge` with:

```
Run folder: <absolute RUN path>
Round: 1
Idea id: <id>
Input files (read only these):
- <RUN>/00-contract.md
- <RUN>/00-founder-knowledge.md
- <RUN>/01-local-market.md
- <RUN>/02-signals.md
- <RUN>/<ideas file>
- <project>/ventures/cities/<city>.md      (only if it exists)
Output file (write exactly this one file):
- <RUN>/ideas/<id>/forge-v1.md
Today's date: <YYYY-MM-DD>
Timestamp: <output of date -u +%Y-%m-%dT%H:%M:%SZ, run just before this call>
```

**Never** include `kill-criteria.md`, `criteria-*.md`, or any text from them. Log each call in `run-log.md` with its exact paths.

## 2. Pivot check
If a `forge-v1.md` has `pivot declared: YES`, forge changed the customer, problem or revenue model of the raw idea. Handle it with the pivot procedure in `${CLAUDE_PLUGIN_ROOT}/commands/kill.md` § Pivot procedure (the old idea becomes `PIVOTED`, the new one goes back to Screen) and do not model economics for the old idea.

## 3. Strategy: independent framework check (all ideas in parallel, after forge)
Progress note: `Running the full framework check (competitors, Five Forces, need gap, pricing, customer behaviour, Ansoff…) on <n> idea(s).`

In **one message**, for each non-pivoted idea launch `venture:market-strategist` with inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, the ideas file (+ `Idea id`), `ideas/<id>/forge-v1.md`, and the city memory file if it exists; output `ideas/<id>/strategy-v1.md`. Never criteria, never economics. Log each call.

**If the strategist recommends DROP**, the idea stops here: record `DROPPED (strategist): <reason>` in `run-log.md` § Stages, and don't run economics, prosecution or the judge for it. A DROP is a builder's own call and saves the run money. It can never create a false pass. Tell the user which idea was dropped and the reason in one line.

## 4. Economics (all carried ideas in parallel, after strategy)
Progress note: `Modelling unit economics in three scenarios for <n> idea(s).`

In **one message**, for each idea still carried, launch `venture:economics-modeler` with inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `ideas/<id>/forge-v1.md`, `ideas/<id>/strategy-v1.md`; output `ideas/<id>/economics-v1.md`. No criteria, no prosecutions. Log each call.

## 5. Simulation (main session runs it, not an agent)
For each economics file, run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/simulate.py" "<RUN>/ideas/<id>/economics-v1.md"
```

- **Exit 0:** write `ideas/<id>/simulation-v1.md` with front matter (`agent: main`, the idea id, `version: 1`, `created` from `date -u`) and the script's stdout **verbatim** below it. Never edit, round or summarise the numbers. Log a Stages row with the viable share.
- **Exit 1** (the inputs block is invalid): re-run `venture:economics-modeler` once with the same inputs plus one line, `Your ## Simulation inputs block failed validation: <the script's error line>. Fix only that block.`, then run the script again. If it fails twice, write `simulation-v1.md` with `## Simulation` and `- not run: invalid inputs — <error>`.
- **`python3` not found:** write `## Simulation` and `- not run: python3 unavailable`, and tell the user once that VIABLE ON PAPER verdicts need Python 3. PASS and KILL still work.

## 6. Report
Add a Stages row `forge — round 1 done for <ids>`. Show each agent's summary and each idea's simulated viable share. Flag any idea whose conservative case already breaks a HARD constraint ("this will very likely be killed"). Next step: `/venture:kill`.
