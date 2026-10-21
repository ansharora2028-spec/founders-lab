<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ideas/<id>/prosecution-v<n>.md — writer: prosecutor (kill mode)

```markdown
---
(front matter, idea_id, agent: prosecutor, version: n)
---

## Inputs read
- <list of exact paths read>

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | MET / NOT MET / INSUFFICIENT EVIDENCE | C03, forge-v1.md#C05 | ... |
| KE1 | MET / NOT MET / INSUFFICIENT EVIDENCE | ... | ... |

## Market flaws
### FM1 — FATAL | FIXABLE
- flaw: <statement>
- evidence: [Cnn] ... [source: ...]
- what would fix it (FIXABLE only): <exact evidence that would fix it, and whether it is obtainable by desk research>
- fix would change customer/problem/revenue model: no | yes

## Execution flaws
### FE1 — FATAL | FIXABLE
- (same fields)

## Evidence
- [C01] ... [source: ...]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | yes / no | ... |
```

Every `KM*` and `KE*` criterion in `kill-criteria.md` gets a row. The prosecutor may only assess criteria that are in `kill-criteria.md`; it can add flaws but not criteria.
