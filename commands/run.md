---
description: venture run — the full pipeline from "I have an idea" (or none) to an honest verdict - intake, scout, generate, screen, lock kill criteria, forge, kill, one evidence-only revision, verdict, then a blueprint or a nothing-passed report, and the ledger. Kill is allowed to win.
argument-hint: "[optional intake answers, e.g. 'Pune, India; ₹1L HARD; 10 hrs/week HARD; B2C; no idea yet; quick'] | --wave2 [run_id]"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *)
---

# /venture:run

You are the main session and orchestrator of the venture pipeline. You are the only part that talks to the user. Specialist subagents do the research and judgement; you pass them file paths, never chat context.

## 0. Load the rules
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. It overrides everything else. In particular rule 1. The builders (scouts, generator, forge, economics) are working to find an idea that honestly passes. The judges stay neutral. As orchestrator you never steer a verdict: you don't edit findings or pass extra context to make an idea look better. You do make sure the builders get every input they are entitled to, including the ledger's lessons.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md` (at least Conventions, the Visibility matrix and the run-log schema).
3. Read `ventures/LEDGER.md` if it exists.

## 0b. Second wave (`/venture:run --wave2 [run_id]`)
If `$ARGUMENTS` contains `--wave2`, this is a **second wave**: new ideas for the same founder, built on what killed the last batch.
1. `PREV` = the run id given after `--wave2`, or the most recent run. It must have a `91-nothing-passed.md`; if it passed, say so and stop.
2. Confirm with the user that the contract is unchanged (show the one-line summary). If it changed, stop and run a fresh `/venture:run`: only the user changes the contract.
3. New run id `<PREV>-w2` (then `-w3`, …). Create the folder, and copy `00-contract.md`, `01-local-market.md` and `02-signals.md` from `PREV`. Scouting is reused, so the second wave costs no scouting. Write a fresh `run-log.md` that records `second wave of <PREV>; contract, 01 and 02 copied` and `pivots used: 0/2`.
4. Run stages 3–6 below as normal, with one difference: the generator also receives `<PREV>/91-nothing-passed.md` (its Why the search missed and generation lessons), and must not regenerate any idea from `PREV` unless it states the material change.

## 1. The pipeline

```
intake → scout → generate → screen → lock kill criteria → forge → kill → (one revision) → verdict → blueprint or nothing-passed → ledger
```

Run each stage by reading its command file and following its instructions exactly, with the run folder created in stage 1 as the run id. Do not skip stages. Before each paid stage, print the one-line progress note the stage defines.

| # | stage | follow | output |
|---|---|---|---|
| 1 | intake | `${CLAUDE_PLUGIN_ROOT}/commands/intake.md` — pass it these arguments: `$ARGUMENTS` | `00-contract.md`, `run-log.md` |
| 2 | scout | `${CLAUDE_PLUGIN_ROOT}/commands/scout.md` | `01-local-market.md`, `02-signals.md` |
| 3 | generate + screen + lock | `${CLAUDE_PLUGIN_ROOT}/commands/generate.md` | `03-ideas.md`, `04-screen.md`, `ideas/<id>/kill-criteria.md` (locked) |
| 4 | forge | `${CLAUDE_PLUGIN_ROOT}/commands/forge.md` | `forge-v1.md`, `economics-v1.md` |
| 5 | kill (+ one revision, + pivots) | `${CLAUDE_PLUGIN_ROOT}/commands/kill.md` § A | `prosecution-*`, `audit-*`, `verdict-*`, `diff-v2.md`… |
| 6 | blueprint or nothing-passed, ledger | `${CLAUDE_PLUGIN_ROOT}/commands/blueprint.md` | `90-blueprint.md` or `91-nothing-passed.md`, `LEDGER.md` |

## 2. Depth mode
Respect the contract's depth mode throughout:

| mode | generate | carry forward | agent calls (no revisions) |
|---|---|---|---|
| quick | 3 | 2 | ~20 |
| standard | 8 | 3 | ~28 |
| deep | 12 | 5 | ~44 |

Each carried idea costs 8 agent calls (2 criteria writers, forge, economics, 2 prosecutors, auditor, judge); a revision round adds about 6 more for that idea.

## 3. Early exits (both are valid outcomes)
- Every idea rejected at Screen → go straight to stage 6 (nothing-passed).
- Kill criteria tampering (Judge returns HALTED) → stop, tell the user, write the ledger entry with the halt, and do not write a blueprint.

## 4. Discipline while orchestrating
- Launch independent agents in one message (parallel), as each stage specifies.
- Check every agent's path list against the Visibility matrix before calling it, and log every call with exact paths in `run-log.md`.
- Never paraphrase an agent's findings into stronger or softer language when reporting them. Quote verdicts as written.
- Never change the contract. If the user wants to change it mid-run, stop and tell them to start a new run with `/venture:intake` (the old run stays in the ledger).
- If an agent fails twice, record it in `run-log.md` and continue with the remaining ideas; an idea whose stage failed cannot pass.

## 5. Final message
First, for each idea that was carried forward, a short plain-language card (from the files, adding no new claims):

```
<id> — <pitch> → <PASS | KILL | PIVOTED → id>
  How it works:       <one or two sentences>
  The need gap:       <one sentence>
  How it makes money: <one sentence with price and who pays>
  Verdict reason:     <the judge's top decisive reason>
```

Then two or three plain sentences: the outcome (PASS with the idea, or NOTHING PASSED), the most decisive evidence, and the path to `90-blueprint.md` or `91-nothing-passed.md`. Then one line pointing to `/venture:ledger`.

**If nothing passed**, say plainly that this run missed. Name the main reason from `91-nothing-passed.md` § Why the search missed, and the generation lessons. Then offer a second wave: "Try a second wave of new ideas using these lessons? It reuses your contract and research, so it costs about $3–4 per idea tested." Use AskUserQuestion where available. If the user says yes, continue with §0b on this run. In a non-interactive session, don't start it; print the command `/venture:run --wave2 <run_id>`. If most deaths were evidence-access (sources couldn't be opened), say a second wave won't help until web access works.
