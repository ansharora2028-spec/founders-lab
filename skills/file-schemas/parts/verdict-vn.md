<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ideas/<id>/verdict-v<n>.md — writer: judge

```markdown
---
(front matter, idea_id, agent: judge, version: n)
---

## Hash check
- expected (run-log): <sha256>
- actual: <sha256>
- result: MATCH | MISMATCH — HALTED

## Verdict
- verdict: PASS | VIABLE ON PAPER | REVISE | KILL | HALTED
- round: 1 | 2
- confidence: <1-10>

## Criteria (after audit)
| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | MET | economics-v1.md#C03 | MET |

## Decisive reasons
1. <reason> — <file#claim refs>

## Demand evidence
- <surviving refs, or 'none surviving'>

## Conservative economics
- fits contract: yes | no — <refs>

## Simulation
- viable share: <x%> · within capital: <y%> · bar: MET | NOT MET | not run — simulation-v<n>.md

## Viable-on-paper check
| condition | met? | evidence |
|---|---|---|
| 1. simulation bar met (≥70% viable, ≥90% within capital) | | simulation-v<n>.md |
| 2. no FATAL flaw survived | | |
| 3. gap backed by peer-town, brand absence or founder-counted evidence | | |
| 4. every failing criterion is INSUFFICIENT EVIDENCE for lack of findable local data, none contradicted | | |
| 5. fits every HARD constraint; strategist recommends CARRY with no unmitigated critical AGAINST | | strategy-v1.md |

## Assumptions to confirm (VIABLE ON PAPER only)
| # | assumption (from the sensitivity ranking) | how to confirm cheaply | stop if |
|---|---|---|---|

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|

## Pivot candidate (KILL only)
- none — <reason> | or:
- customer: <new or unchanged>
- problem: <new or unchanged>
- revenue model: <new or unchanged>
- field(s) changed: <customer | problem | revenue model>
- grounded in: <surviving file#claim refs>
- fits HARD constraints: yes — <K# checked>

## Ignored as struck
- <refs>
```

No encouragement. No softening.
