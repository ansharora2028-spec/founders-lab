<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ventures/cities/<city-slug>.md — writer: main (append only)

City memory: what venture has learned about one town across runs. Main appends one dated block per run at blueprint time. Scouts, the generator, forge and the strategist read it. **Never delete or edit past blocks.**

```markdown
# <City>, <Country>

## <run_id> (<YYYY-MM-DD>)
### Verified facts
- <claim> [source: <url>] (VERIFIED in ideas/<id>/audit-v<n>.md)
### Peer-town benchmark
- <category>: <n> per 10,000 vs peer median <m> → under-served | in line | over-served
### Big-brand presence
- <brand>: present | absent (<evidence>)
### City profile
- <one line per parameter, with its label>
### Founder-reported (unverified)
- <answer> [FOUNDER-COUNTED | FOUNDER-ESTIMATE]
### Useless sources for this town
- <domain>
```

Only VERIFIED claims go under Verified facts. Struck claims never go in.
