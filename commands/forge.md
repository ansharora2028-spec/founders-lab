---
description: venture forge — for every carried idea with locked kill criteria, run forge (sharpen, no persuasion) and then economics-modeler (three scenarios, conservative counts). Forge never receives kill-criteria.md.
argument-hint: "[run_id] [idea_id ...] (default: most recent run, all carried ideas not yet forged)"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, Bash(date *)
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
- <RUN>/01-local-market.md
- <RUN>/02-signals.md
- <RUN>/<ideas file>
Output file (write exactly this one file):
- <RUN>/ideas/<id>/forge-v1.md
Today's date: <YYYY-MM-DD>
Timestamp: <output of date -u +%Y-%m-%dT%H:%M:%SZ, run just before this call>
```

**Never** include `kill-criteria.md`, `criteria-*.md`, or any text from them. Log each call in `run-log.md` with its exact paths.

## 2. Pivot check
If a `forge-v1.md` has `pivot declared: YES`, forge changed the customer, problem or revenue model of the raw idea. Handle it with the pivot procedure in `${CLAUDE_PLUGIN_ROOT}/commands/kill.md` § Pivot procedure (the old idea becomes `PIVOTED`, the new one goes back to Screen) and do not model economics for the old idea.

## 3. Economics (all ideas in parallel, after forge)
Progress note: `Modelling unit economics in three scenarios for <n> idea(s).`

In **one message**, for each non-pivoted idea launch `venture:economics-modeler` with inputs `00-contract.md`, `01-local-market.md`, `ideas/<id>/forge-v1.md`; output `ideas/<id>/economics-v1.md`. No criteria, no prosecutions. Log each call.

## 4. Report
Add a Stages row `forge — round 1 done for <ids>`. Show each agent's summary, and flag any idea whose conservative case already breaks a HARD constraint ("this will very likely be killed"). Next step: `/venture:kill`.
