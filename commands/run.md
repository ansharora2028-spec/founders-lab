---
description: venture run — the full pipeline from "I have an idea" (or none) to an honest verdict - intake, scout, generate, screen, lock kill criteria, forge, kill, one evidence-only revision, verdict, then a blueprint or a nothing-passed report, and the ledger. Kill is allowed to win.
argument-hint: "[optional intake answers, e.g. 'Pune, India; ₹1L HARD; 10 hrs/week HARD; B2C; no idea yet; quick']"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *)
---

# /venture:run

You are the main session and orchestrator of the venture pipeline. You are the only part that talks to the user. Specialist subagents do the research and judgement; you pass them file paths, never chat context.

## 0. Load the rules
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`. It overrides everything else. In particular: **Kill can win.** A run where every idea dies is a successful run. Never steer toward a pass.
2. Read `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md` (at least Conventions, the Visibility matrix and the run-log schema).
3. Read `ventures/LEDGER.md` if it exists.

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
Two or three plain sentences: the outcome (PASS with the idea, or NOTHING PASSED), the most decisive evidence, and the path to `90-blueprint.md` or `91-nothing-passed.md`. Then one line pointing to `/venture:ledger`.
