<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ideas/<id>/economics-v<n>.md — writer: economics-modeler

````markdown
---
(front matter, idea_id, agent: economics-modeler, version: n)
---

## Inputs
- [C01] price: ₹499/month [source: ... | ASSUMPTION: ...]
- [C02] COGS per unit ...
(every input sourced or ASSUMPTION with rationale)

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | | | |
| COGS per unit | | | |
| gross margin % | | | |
| CAC: <channel 1> | | | |
| CAC: <channel 2> | | | |
| blended CAC | | | |
| payback period (months) | | | |
| break-even volume | | | |
| capital to first revenue | | | |
| months to first revenue | | | |

## Calculations
(show the arithmetic for the conservative column)

## Simulation inputs
```json
{
  "currency": "INR", "months": 12, "break_even_by_month": 3,
  "capital_limit": 100000, "hours_limit_per_week": 10,
  "inputs": {
    "price": {"low": 249, "likely": 299, "high": 349, "evidence": "verified"},
    "units_per_customer_per_month": {"low": 1, "likely": 1, "high": 1, "evidence": "assumption"},
    "variable_cost_per_unit": {...}, "fixed_cost_per_month": {...}, "setup_cost": {...},
    "reach_per_month": {...}, "conversion_rate": {...}, "cac": {...}, "monthly_churn": {...},
    "founder_hours_fixed_per_week": {...}, "founder_hours_per_unit": {...}
  }
}
```
(the exact keys `scripts/simulate.py` requires; `evidence` is one of verified, peer-town, founder-counted, founder-estimate, assumption; `break_even_by_month` comes from K6, `capital_limit` from K1, `hours_limit_per_week` from K2)

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1L HARD | ₹1.4L | BREAKS |

## Verdict inputs
- conservative unit economics positive: yes | no
- HARD constraints broken in conservative case: <list or 'none'>
- FLEXIBLE stretches required: <list with unlock condition status, or 'none'>
- what would have to change for the conservative case to work: <the one or two numbers, with by how much, or 'nothing — it works'>
````
