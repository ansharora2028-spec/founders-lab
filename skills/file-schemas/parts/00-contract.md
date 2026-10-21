<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## 00-contract.md — writer: main (intake)

```markdown
---
run_id: <run_id>
agent: main
version: 1
created: <iso>
---

## Starting point
- path: a | b | c            # a = specific idea, b = space/industry, c = nothing yet
- in their words: "<verbatim, or 'none'>"
- how they plan to charge: "<verbatim, or 'not asked' / 'not sure'>"   (asked by /lab:test)

## Location profile
- lives in: <city, country>
- target market: <local: city | national: country | other country: <name> | online/global>
- local language(s) for search: <...>
- currency: <ISO code and symbol>

## Constraints
| # | constraint | value | type | stretch range | unlock condition |
|---|---|---|---|---|---|
| K1 | capital available | ₹1,00,000 | HARD | — | — |
| K2 | hours per week | 10 | FLEXIBLE | up to 15 | only for months 1–2 |
| K3 | skills (have) | ... | HARD | — | — |
| K4 | skills (can hire/learn) | ... | FLEXIBLE | ... | ... |
| K5 | risk appetite | low/medium/high; cannot lose: <...> | HARD | — | — |
| K6 | time to first revenue | ... | ... | ... | ... |
| K7 | B2B / B2C / either | ... | HARD | — | — |
| K8 | off-limits categories | ... | HARD | — | — |
| K9 | other | ... | ... | ... | ... |

## Unfair advantages
- <advantage, or 'none stated'>

## Depth mode
- mode: quick | standard | deep | check | check+variants
- ideas to generate: 3 | 8 | 12 | 1 (the user's idea) | up to 4 (the user's idea + up to 3 variants)
- ideas to carry forward: 2 | 3 | 5 | 1 | 2 (the user's idea + the best-ranked variant)

## Confirmation
- confirmed by user: yes
- confirmed at: <iso>
- how: <AskUserQuestion | plain chat | arguments (non-interactive)>
```
