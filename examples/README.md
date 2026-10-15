# examples

Real output from the v0.1 test runs (see `DECISIONS.md` § Test results). The user is fictional; the research is real web research done on 2026-10-15. Absolute paths have been replaced with `<project>` / `<scratch>`.

## sample-run/ — one complete run, unmodified

`/venture:run` in `quick` mode for a fictional user: Pune, India; target market Pune; ₹1,00,000 HARD; 10 hrs/week HARD; B2C; no idea yet; no unfair advantages.

Read it in order:

1. `ventures/runs/2026-10-15-pune-b2c-open/00-contract.md`: the constraint contract
2. `01-local-market.md` (coverage 3/10, and it says why) and `02-signals.md`
3. `03-ideas.md` (3 ideas) and `04-screen.md` (ranking; I03 carried forward)
4. `ideas/I03/kill-criteria.md`: locked before forge (its SHA-256 is in `run-log.md` § Locks; check it with `sha256sum`)
5. `ideas/I03/forge-v1.md` and `economics-v1.md`
6. `ideas/I03/prosecution-market-v1.md`, `prosecution-execution-v1.md`, `audit-v1.md`, `verdict-v1.md` (**KILL**, confidence 7)
7. `91-nothing-passed.md` and `ventures/LEDGER.md`
8. `run-log.md`: every agent call with the exact paths it received

Note: in the test container, the auditor's fetches were blocked by network policy, so many claims were struck as UNREACHABLE. That's visible in `audit-v1.md` and taken into account in the verdict's confidence.

## revision-round/ — what round 2 looks like

The same run, continued after the round-1 verdict was changed to REVISE by the test harness (marked `TEST FIXTURE` in `ideas/I03/verdict-v1.md`). Everything else was produced by the plugin:
`fixable-flaws-v1.md` (the only part of the verdict forge sees) → `forge-v2.md` → `diff-v2.md` (the only part of forge-v2 the prosecutors see) → `economics-v2.md` → round-2 prosecutions, audit, and `verdict-v2.md` (**KILL in round 2**).

## pivot/ — a pivot caught and re-screened

The same REVISE fixture, plus an injected `ideas/I03/forge-v2.md` (marked `TEST FIXTURE`) that changes the revenue model to a commission while claiming `pivot declared: no`. The main session detected it, marked I03 `PIVOTED → I03-P1` (`run-log.md` § Pivots), and wrote `03-ideas-pivot1.md` and `04-screen-pivot1.md`. It then ran I03-P1 from zero: new locked criteria, forge, economics, prosecution, audit, and `verdict-v1.md` (**KILL**).
