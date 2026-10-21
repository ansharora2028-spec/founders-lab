<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## Visibility matrix (enforced by the main session)

Paths are relative to `ventures/runs/<run_id>/`. Short names:
- `LEDGER` is `ventures/LEDGER.md`;
- `CITY` is the city memory file `ventures/cities/<city-slug>.md`, if it exists;
- `FK` is `00-founder-knowledge.md`;
- `raw idea` is the idea's entry in `03-ideas.md` (or `03-ideas-pivot<k>.md`);
- `strategy` is `ideas/<id>/strategy-v1.md`;
- `simulation-v<n>` is `ideas/<id>/simulation-v<n>.md`, written by main from `scripts/simulate.py` (it includes the money gate).
- `gate-v<n>` is `ideas/<id>/gate-v<n>.md`, written by main only when the money gate fails.

| Agent | Mode | Paths it receives | Never receives |
|---|---|---|---|
| local-market-scout | — | 00, FK, LEDGER, CITY | everything else |
| signal-scout | — | 00, FK, LEDGER | everything else |
| generator | — | 00, FK, 01, 02, LEDGER, CITY (+ the previous run's 91-nothing-passed in a second wave) | 04, any kill-criteria, prosecutions, audits, verdicts of this run |
| screener | — | 00, 03 (or 03-ideas-pivot<k>), LEDGER | 01, 02, FK |
| prosecutor | criteria | 00, FK, 01, 02, raw idea file + idea id | forge, strategy, economics, simulation |
| forge | round 1 | 00, FK, 01, 02, 03 (+ idea id), CITY | kill-criteria, criteria draft, strategy, prosecutions, audits, verdicts |
| forge | round 2 | as round 1 + forge-v1 + fixable-flaws-v1 (the Judge's fixable-flaw table, extracted by main) | kill-criteria, prosecutions, audits, the full verdict |
| economics-modeler | — | 00, FK, 01, forge-v<n> (+ economics-v1 in round 2) | kill-criteria, strategy, prosecutions, audits, verdicts |
| market-strategist | — | 00, FK, 01, 02, 03 (+ idea id), forge-v1, CITY | kill-criteria, criteria draft, economics, simulation, prosecutions, audits, verdicts |
| prosecutor | kill v1 | 00, FK, 01, 02, kill-criteria, forge-v1, economics-v1, simulation-v1 | strategy (it runs in parallel with the strategist), audit, verdict |
| prosecutor | kill v2 | 00, FK, 01, 02, kill-criteria, diff-v2, economics-v2, simulation-v2, own prosecution-v1 | **forge-v2**, strategy, audits, verdicts |
| evidence-auditor | round n | every file for that idea in round n except the verdict: 00, FK, 01, 02, kill-criteria, forge-v<n> (or diff-v2 + forge-v2), strategy, economics-v<n>, simulation-v<n>, prosecution-v<n> | verdict-v<n>, earlier verdicts |
| judge | round n | everything for that idea, plus run-log (for the hash) | — |

In **direct kill mode** (`/lab:verdict "<idea>"`) there is no scouting and no forge. `ideas/I01/idea.md` (the idea as the user stated it) stands in for both the raw idea and `forge-v1`:
- the prosecutor in criteria mode receives `00` and `idea.md`;
- the economics-modeler receives `00` and `idea.md` and writes `economics-v1.md` (without it a PASS is impossible under rule 3), then main runs the simulation and the money gate;
- the prosecutor in kill mode receives `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`, `simulation-v1.md`;
- the auditor and judge receive everything for the idea as usual.
There is no revision round in direct mode: REVISE is reported to the user as "would need: <fixable flaws>" and recorded as KILL in the ledger.
