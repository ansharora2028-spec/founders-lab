---
description: venture blueprint — if any idea passed or is viable on paper, write 90-blueprint.md (best idea, assumptions to confirm for viable-on-paper, 3 cheapest experiments, MVP scope, pricing, first 100 customers, 30-day plan, kill signals); if nothing passed, write 91-nothing-passed.md (deaths with evidence, estimated savings, patterns, constraints worth stretching, next directions). Then append the ledger and the city memory.
argument-hint: "[run_id] (default: the most recent run)"
allowed-tools: Read, Write, Edit, Glob, Bash(date *)
---

# /venture:blueprint

## 0. Load the rules and find the run
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`, and the `90-blueprint.md` and `91-nothing-passed.md` sections of `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`.
2. `RUN` = `ventures/runs/<$ARGUMENTS>` or the most recent run folder.
3. Collect every idea's final status, in this order of precedence:
   1. recorded in `run-log.md` § Pivots as `PIVOTED → <id>` → **PIVOTED** (ignore its leftover verdict file: a round-1 REVISE from a forge pivot, or a KILL that produced a judge pivot candidate);
   2. recorded in § Pivots as `KILLED (pivot limit)` → **KILL**;
   3. recorded in § Stages as `DROPPED (strategist)` → **DROPPED (strategist)**;
   4. otherwise the latest `verdict-v<n>.md`: PASS, VIABLE ON PAPER, KILL or HALTED; REVISE in round 2 = **KILL**;
   5. rejected in `04-screen.md` / `04-screen-pivot<k>.md` → **REJECTED (screen)**; screened but not carried → **NOT CARRIED (rank)**.
   If any carried idea has a round-1 REVISE verdict and is not pivoted, or has no verdict at all, the kill stage is unfinished: tell the user to run `/venture:kill <run_id>` and stop.

You (the main session) write this file. You may read every file in the run. You may not change any verdict. Every factual statement in the blueprint is copied from a surviving (non-struck) claim with its reference, or labeled `ASSUMPTION`.

## 1a. If any idea has a final PASS or VIABLE ON PAPER → `90-blueprint.md`
- **Winning idea:** a PASS always outranks a VIABLE ON PAPER. Among equals, pick the single best by: higher Judge confidence, then stronger verified demand evidence, then larger conservative margin within the contract, then faster time to first revenue. State why it beat the others with refs.
- **How it works / The need gap / How it makes money:** explain the winning idea in plain language for someone with no business background, from `forge-v<n>.md` (How it works, Need gap, How it makes money) and the conservative column of `economics-v<n>.md` (price, cost to deliver, customers needed to break even). Cite refs.
- **Assumptions to confirm first (VIABLE ON PAPER only):** copy the judge's 2–3 assumptions, how to confirm each cheaply, and the "stop if" numbers. Put this before the experiments, and say plainly that demand in this town is not yet proven.
- **This week's 3 cheapest experiments:** each with cost (in contract currency), time (hours), a **success threshold** and a **kill threshold** (numbers). They should test the riskiest surviving assumptions first (smoke-test landing page, 10 customer calls, pre-sales, concierge delivery, a ₹/$ capped ad test…).
- **MVP scope:** in and out.
- **Pricing:** from the conservative-case economics, with refs.
- **Path to first 100 customers** in the user's target market: channel by channel with numbers, from forge and economics.
- **30-day plan:** week by week, with a decision gate at the end of each week.
- **Kill signals:** observable, numeric signals that should make the user stop.
- **Caveats:** this is research assistance, not financial advice; list the load-bearing ASSUMPTIONs still unverified.

## 1b. If nothing passed (no PASS and no VIABLE ON PAPER) → `91-nothing-passed.md`
Nothing passing is a miss for the builders (rule 1). It isn't a disaster, because it saved the founder money and months. Write it plainly, without consolation language and without drama.
- **The ideas, explained:** for every idea (carried or not), in plain language: how it would have worked, the need gap it targeted, and how it would have made money, taken from `03-ideas.md` (and `forge-v<n>.md` where the idea was forged), then what happened to it in one line. A reader should understand each idea before reading why it died.
- **Deaths:** every idea (screen rejections, not carried, killed, pivoted, halted), its decisive evidence, and the verdict file reference.
- **Estimated savings — labeled ESTIMATE:** capital and months the user would plausibly have spent before discovering each fatal problem in the market. Base it on the contract (capital, hours) and the conservative economics (capital to first revenue, months to first revenue). List every assumption. Give ranges, not point values.
- **Why the search missed:** nothing passing is a miss for the builders (rule 1), so diagnose it honestly. For each dead idea, give its cause of death, where in the pipeline it should have been caught (for example "generator: no demand anchor"), and the type: generation, constraint, evidence access or bad luck. Then write 2–4 concrete **generation lessons** for the next run. If most deaths were evidence-access (sources couldn't be opened), say so plainly: the search may not have missed at all.
- **Patterns across the deaths:** e.g. the same constraint breaking, the same missing demand evidence, the same platform risk.
- **Flexible constraints that would most change the outcome:** only within the user's stated stretch ranges and unlock conditions. For each: which ideas it would revive and how. Never suggest changing a HARD constraint — only the user can change the contract; you may note that a HARD constraint was decisive.
- **Directions for the next run:** concrete starting points (a space, a segment, a lens), informed by the signals that held up.

## 2. Append the ledger and the city memory
Append the ledger entry (outcome `PASS (<id>)`, `VIABLE ON PAPER (<id>)` or `NOTHING PASSED`). Then append one dated block to `ventures/cities/<city-slug>.md` (create it with `# <City>, <Country>` if missing) in the schema:
- only claims the audits marked VERIFIED, under Verified facts;
- the peer-town benchmark, big-brand presence and city profile from `01-local-market.md`;
- founder answers, under Founder-reported (unverified);
- sources that proved useless for this town.

Never copy a struck claim. Never edit older blocks.

### Ledger
Follow `${CLAUDE_PLUGIN_ROOT}/commands/ledger.md` § Append.

## 3. Finish the run log
Set `finished:` in `run-log.md`, add a Stages row `blueprint — <PASS (<id>) | NOTHING PASSED>`. Fill § Blindness self-check by reading § Agent calls: confirm no prosecutor call lists `forge-v2.md` or the other prosecutor's file, and no forge/economics call lists `kill-criteria.md` or `criteria-*.md`. Report any violation honestly.

## 4. Report
Tell the user the outcome in two or three sentences and the path of the file. For PASS, list the 3 experiments. For NOTHING PASSED, give the savings estimate range and the top pattern.
