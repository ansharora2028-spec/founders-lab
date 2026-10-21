---
description: Stopped partway? Continues a Founders Lab run (from /lab:ideate or /lab:test) from the first stage that isn't finished. Also runs a second wave of ideas with --wave2.
argument-hint: "[run_id] (default: the most recent run)  |  --wave2 [run_id]"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *), Bash(python3 *)
---

# /lab:resume

Arguments: `$ARGUMENTS`

1. Read `${CLAUDE_PLUGIN_ROOT}/skills/rules/SKILL.md`. It overrides everything else.
2. If the arguments start with `--wave2`, follow `${CLAUDE_PLUGIN_ROOT}/commands/ideate.md` §0b and stop here.
3. `RUN` = `ventures/runs/<run_id>` if given, else the most recent folder in `ventures/runs/`. If there is none, say so and suggest `/lab:ideate` or `/lab:test "<idea>"`.
4. Read `RUN/run-log.md` (Stages, Locks, Pivots) and list the files in `RUN`. Direct-mode runs (`-kill-` in the id) can't be resumed: suggest re-running `/lab:verdict`.
5. Find the **first unfinished stage** and follow its stage file with `RUN` as the run, then each later stage in order, exactly as `${CLAUDE_PLUGIN_ROOT}/commands/ideate.md` §1 runs them. Each stage file already skips work that is done.

   | stage is unfinished when | follow |
   |---|---|
   | `00-contract.md` is missing or not confirmed | `${CLAUDE_PLUGIN_ROOT}/stages/intake.md` |
   | `01-local-market.md` or `02-signals.md` is missing | `${CLAUDE_PLUGIN_ROOT}/stages/scout.md` |
   | `04-screen.md` is missing, or a carried idea has no locked `kill-criteria.md` | `${CLAUDE_PLUGIN_ROOT}/stages/generate.md` |
   | a carried idea has no `simulation-v1.md` (and isn't DROPPED) | `${CLAUDE_PLUGIN_ROOT}/stages/forge.md` |
   | a carried idea has no final verdict, or a round-1 REVISE that isn't pivoted | `${CLAUDE_PLUGIN_ROOT}/stages/kill.md` §A |
   | neither `90-blueprint.md` nor `91-nothing-passed.md` exists | `${CLAUDE_PLUGIN_ROOT}/stages/blueprint.md` |

6. If everything is finished, say so, show the verdict line from the report, and give its path.
7. Tell the user which stage you are resuming from before the first paid agent call. End with the same final message as `/lab:ideate` §5 (or `/lab:test` §4 for a `-check-` run).
