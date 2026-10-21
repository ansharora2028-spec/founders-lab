---
description: Internal pipeline stage (not a slash command), followed by /lab:ideate, /lab:test, /lab:verdict and /lab:resume. forge — for every carried idea with locked kill criteria: forge (sharpen, no persuasion), then economics-modeler (three scenarios plus simulation inputs), then the seeded simulation and the money gate. Ideas whose money doesn't work even on the most generous reading stop here. Forge and economics never receive kill-criteria.md.
argument-hint: "[run_id] [idea_id ...] (default: most recent run, all carried ideas not yet forged)"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, Bash(date *), Bash(python3 *)
---

# Stage: forge

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/rules/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/parts/_visibility.md`. For the files you write, read `parts/simulation-vn.md` and `parts/gate-vn.md` in the same folder.
2. Arguments: `$ARGUMENTS`. The first argument that matches a folder in `ventures/runs/` is the run id; otherwise `RUN` = the most recent run folder. Remaining arguments are idea ids.
3. Ideas to forge: the given ids, or every `RUN/ideas/<id>/` that has a `kill-criteria.md` and no `forge-v1.md`. Ideas that have `forge-v1.md` but no `simulation-v1.md` resume at §3 (or §4 if `economics-v1.md` exists).
4. **Lock check:** for each idea, confirm `kill-criteria.md` exists and its hash is recorded in `run-log.md` § Locks. If it is not locked, stop: criteria must be locked before forge (rule 2). Run `/lab:resume` first.

This stage runs **round 1** only. Round 2 forging happens inside the kill stage on a REVISE verdict.

The ideas file for an idea is `03-ideas.md`, or `03-ideas-pivot<k>.md` for a pivoted idea (`<old-id>-P<k>`).

**Order: money first.** Forge → economics → simulation → **money gate**. The strategist and the prosecutor run in the kill stage, in parallel, and only for ideas that pass the gate. Most doomed ideas fail on money, and the gate catches them before the expensive half of the pipeline.

## 1. Forge (all ideas in parallel)
Progress note: `Forging <n> idea(s) (paid stage: web research).`

In **one message**, for each idea launch `lab:forge` with:

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

**Never** include `kill-criteria.md`, `criteria.md`, or any text from them. Log each call in `run-log.md` with its exact paths.

## 2. Pivot check
If a `forge-v1.md` has `pivot declared: YES`, forge changed the customer, problem or revenue model of the raw idea. Handle it with the pivot procedure in `${CLAUDE_PLUGIN_ROOT}/stages/kill.md` § Pivot procedure (the old idea becomes `PIVOTED`, the new one goes back to Screen) and do not model economics for the old idea.

## 3. Economics (all non-pivoted ideas in parallel, right after forge)
Progress note: `Modelling the money in three scenarios for <n> idea(s).`

In **one message**, for each non-pivoted idea, launch `lab:economics-modeler` with inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `ideas/<id>/forge-v1.md`; output `ideas/<id>/economics-v1.md`. No criteria, no strategy, no prosecutions. Log each call.

## 4. Simulation and money gate (main session runs it, not an agent)
For each economics file, run:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/simulate.py" "<RUN>/ideas/<id>/economics-v1.md"
```

- **Exit 0:** write `ideas/<id>/simulation-v1.md` with front matter (`agent: main`, the idea id, `version: 1`, `created` from `date -u`) and the script's stdout **verbatim** below it. Never edit, round or summarise the numbers. Log a Stages row with the viable share and the gate result.
- **Exit 1** (the inputs block is invalid): re-run `lab:economics-modeler` once with the same inputs plus one line, `Your ## Simulation inputs block failed validation: <the script's error line>. Fix only that block.`, then run the script again. If it fails twice, write `simulation-v1.md` with `## Simulation` and `- not run: invalid inputs — <error>`. The gate can't run, so the idea goes on to the kill stage.
- **`python3` not found:** write `## Simulation` and `- not run: python3 unavailable`, and tell the user once that VIABLE ON PAPER verdicts and the money gate need Python 3. The idea goes on to the kill stage, and PASS and KILL still work.

**The money gate.** Read the `money gate:` line in `simulation-v1.md`.
- `PASS` → the idea goes on to the kill stage.
- `FAIL` → the idea **stops here**: even taking the builders' own numbers at face value, with no evidence haircut, fewer than 20% of simulated runs break even in time within capital.
  - Write `ideas/<id>/gate-v1.md` in its schema, copying verbatim from `simulation-v1.md` and `economics-v1.md`.
  - Record `KILL (money gate)` in run-log § Stages.
  - Run no strategy, prosecution, audit or judge for this idea. It is final, with no revision round and no pivot candidate.
  - Tell the user in one line: `<id>: the money doesn't work (best case <x>% viable). Would need: <the first row of What would have to change>.`

  The gate never creates a pass and never changes the bar for ideas that clear it. It only stops ideas the judge would certainly kill under rule 3 (the conservative economics must work).

## 5. Report
Add a Stages row `forge — round 1 done for <ids>`. Show each agent's summary and, for each idea, the simulated viable share and the gate result. Next step: `/lab:resume`.
