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

## quick-run-v0.2/ — the v0.2.0 plugin, unmodified

The same fictional user on v0.2.0: quick mode now carries two ideas (I01 and I03, both KILLED). Every verdict has a **Pivot candidate** section, and both are `none` with the reason. Timestamps are real (`date -u`).

## quick-run-v0.4/: the "builders aim to pass" version (v0.4)

The same fictional user on v0.4. The money map in `01-local-market.md` lists 13 places where people in Pune already pay, plus complaints about paid options. In `03-ideas.md` the generator longlisted 9 candidates and dropped 6 with reasons. The screen scores market proof. I01 (a ₹799 refund-claim file for coaching students) earned the first **REVISE** in any test run (positive cautious economics, no surviving fatal flaw), went through a full revision round (`diff-v2.md` has 11 rows), and was KILLED in round 2. I03 (a guaranteed deep-clean) was KILLED on negative cautious economics. `91-nothing-passed.md` has the new **Why the search missed** section with generation lessons.

## check-run/: `/venture:check` on a founder's own idea (v0.3)

`/venture:check "Weekend spoken-English conversation clubs for Pune college students, held in cafés, ₹499 per month"`. Only the user's idea is written up (I01). Every detail the user didn't give is marked `not stated by the user, ASSUMPTION`. Verdict: **DON'T DO IT** (KILL, confidence 6): break-even needs two groups and 12 h/week against a HARD 10 h limit, and one group loses money. Read `91-nothing-passed.md` for the plain-language explanation.

## pivot/ — a pivot caught and re-screened

The same REVISE fixture, plus an injected `ideas/I03/forge-v2.md` (marked `TEST FIXTURE`) that changes the revenue model to a commission while claiming `pivot declared: no`. The main session detected it, marked I03 `PIVOTED → I03-P1` (`run-log.md` § Pivots), and wrote `03-ideas-pivot1.md` and `04-screen-pivot1.md`. It then ran I03-P1 from zero: new locked criteria, forge, economics, prosecution, audit, and `verdict-v1.md` (**KILL**).

## small-town-check-v0.5/ — `/venture:check` in a small town, v0.5, open network

A ₹600/month spoken-English batch for class 6-10 in Satara (about 1.2 lakh people), with the founder questionnaire answered (`00-founder-knowledge.md`). It shows the v0.5 additions: `strategy-v1.md` (full framework check, CARRY), `economics-v1.md` with simulation inputs, `simulation-v1.md` (2.6% viable, bar NOT MET), and an audit with real fetches. The verdict is **KILL**, confidence 6. `91-nothing-passed.md` says what would have to change. Also included are the ledger and city memory (`ventures/cities/`).
