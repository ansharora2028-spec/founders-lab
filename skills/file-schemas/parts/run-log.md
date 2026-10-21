<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## run-log.md — writer: main

```markdown
---
(front matter, agent: main)
---

## Run
- depth mode: <mode>
- started: <iso>
- finished: <iso>
- pivots used: <n>/2

## Stages
| time | stage | note |
|---|---|---|

## Agent calls
| time | agent | mode | idea | round | paths passed | output |
|---|---|---|---|---|---|---|
| ... | prosecutor | kill | I01 | 2 | 00-contract.md; 01-local-market.md; 02-signals.md; ideas/I01/kill-criteria.md; ideas/I01/diff-v2.md; ideas/I01/economics-v2.md; ideas/I01/simulation-v2.md; ideas/I01/prosecution-v1.md | ideas/I01/prosecution-v2.md |

## Locks
| idea | file | sha256 | locked at |
|---|---|---|---|

## Pivots
| from | to | field changed | counter after |
|---|---|---|---|

## Blindness self-check
- forge-v2.md passed to the prosecutor: never | <violations>
- strategy passed to the prosecutor: never | <violations>
- kill-criteria passed to forge or economics-modeler: never | <violations>
```
