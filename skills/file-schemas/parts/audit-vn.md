<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ideas/<id>/audit-v<n>.md — writer: evidence-auditor

```markdown
---
(front matter, idea_id, agent: evidence-auditor, version: n)
---

## Scope
- files audited: <paths>
- claims in scope: <n>, checked: <n>, sample method: <all economics inputs + all FATAL-flaw evidence + random sample of the rest>

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C02 | COGS ₹40/unit | <url> | VERIFIED / MISREPRESENTED / UNREACHABLE / UNSOURCED | ... |

## Struck claims
- <ref> — <label> — <one line why>

## Assumptions in load-bearing positions
- <ref> — ASSUMPTION used as the basis of <a criterion / a FATAL flaw / a conservative input>

## Summary
- verified: n, misrepresented: n, unreachable: n (of which tool failure: n), unsourced: n
- demand evidence surviving the audit: <refs or 'none'>
```

`UNSOURCED` claims and claims labeled `MISREPRESENTED` or `UNREACHABLE` are struck. `ASSUMPTION`-labeled claims are not struck but are listed if they are load-bearing.
