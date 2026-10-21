---
run_id: <YYYY-MM-DD>-<slug>
idea_id: <idea-id>
agent: economics-modeler
version: 1
created: <ISO 8601 UTC>
---

## Inputs
- [C01] <claim> [source: <url> | ASSUMPTION: <why>]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | | | |
| COGS per unit | | | |
| gross margin % | | | |
| CAC: <channel> | | | |
| blended CAC | | | |
| payback period (months) | | | |
| break-even volume | | | |
| capital to first revenue | | | |
| months to first revenue | | | |

## Calculations

## Simulation inputs
```json
{"currency": "", "months": 12, "break_even_by_month": 0, "capital_limit": 0, "hours_limit_per_week": 0,
 "inputs": {"price": {"low": 0, "likely": 0, "high": 0, "evidence": "assumption"}}}
```

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|

## Verdict inputs
- conservative unit economics positive: <yes | no>
- HARD constraints broken in conservative case:
- FLEXIBLE stretches required:
- what would have to change for the conservative case to work:
