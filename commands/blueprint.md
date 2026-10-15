---
description: venture blueprint — if any idea passed, write 90-blueprint.md (best idea, 3 cheapest experiments, MVP scope, pricing, first 100 customers, 30-day plan, kill signals); if nothing passed, write 91-nothing-passed.md (deaths with evidence, estimated savings, patterns, constraints worth stretching, next directions). Then append the ledger.
argument-hint: "[run_id] (default: the most recent run)"
allowed-tools: Read, Write, Edit, Glob, Bash(date *)
---

# /venture:blueprint

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`, and the `90-blueprint.md` and `91-nothing-passed.md` sections of `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`.
2. `RUN` = `ventures/runs/<$ARGUMENTS>` or the most recent run folder.
3. Collect every idea's final status: for each `RUN/ideas/<id>/`, the latest `verdict-v<n>.md` (REVISE in round 2 = KILL); plus screened-out ideas from `04-screen*.md`, ideas not carried (rank), and pivots from `run-log.md`.

You (the main session) write this file. You may read every file in the run. You may not change any verdict. Every factual statement in the blueprint is copied from a surviving (non-struck) claim with its reference, or labeled `ASSUMPTION`.

## 1a. If any idea has a final PASS → `90-blueprint.md`
- **Winning idea:** if several passed, pick the single best by: higher Judge confidence, then stronger verified demand evidence, then larger conservative margin within the contract, then faster time to first revenue. State why it beat the others with refs.
- **This week's 3 cheapest experiments:** each with cost (in contract currency), time (hours), a **success threshold** and a **kill threshold** (numbers). They should test the riskiest surviving assumptions first (smoke-test landing page, 10 customer calls, pre-sales, concierge delivery, a ₹/$ capped ad test…).
- **MVP scope:** in and out.
- **Pricing:** from the conservative-case economics, with refs.
- **Path to first 100 customers** in the user's target market: channel by channel with numbers, from forge and economics.
- **30-day plan:** week by week, with a decision gate at the end of each week.
- **Kill signals:** observable, numeric signals that should make the user stop.
- **Caveats:** this is research assistance, not financial advice; list the load-bearing ASSUMPTIONs still unverified.

## 1b. If nothing passed → `91-nothing-passed.md`
Nothing passing is a successful run (rule 1). Write it plainly, without consolation language.
- **Deaths:** every idea (screen rejections, not carried, killed, pivoted, halted), its decisive evidence, and the verdict file reference.
- **Estimated savings — labeled ESTIMATE:** capital and months the user would plausibly have spent before discovering each fatal problem in the market. Base it on the contract (capital, hours) and the conservative economics (capital to first revenue, months to first revenue). List every assumption. Give ranges, not point values.
- **Patterns across the deaths:** e.g. the same constraint breaking, the same missing demand evidence, the same platform risk.
- **Flexible constraints that would most change the outcome:** only within the user's stated stretch ranges and unlock conditions. For each: which ideas it would revive and how. Never suggest changing a HARD constraint — only the user can change the contract; you may note that a HARD constraint was decisive.
- **Directions for the next run:** concrete starting points (a space, a segment, a lens), informed by the signals that held up.

## 2. Append the ledger
Follow `${CLAUDE_PLUGIN_ROOT}/commands/ledger.md` § Append.

## 3. Finish the run log
Set `finished:` in `run-log.md`, add a Stages row `blueprint — <PASS (<id>) | NOTHING PASSED>`. Fill § Blindness self-check by reading § Agent calls: confirm no prosecutor call lists `forge-v2.md` or the other prosecutor's file, and no forge/economics call lists `kill-criteria.md` or `criteria-*.md`. Report any violation honestly.

## 4. Report
Tell the user the outcome in two or three sentences and the path of the file. For PASS, list the 3 experiments. For NOTHING PASSED, give the savings estimate range and the top pattern.
