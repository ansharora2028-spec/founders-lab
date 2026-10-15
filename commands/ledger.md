---
description: venture ledger — summarize past venture runs from ventures/LEDGER.md, or search them by location, idea, or cause of death. Also defines how every run appends its ledger entry.
argument-hint: "[search terms, e.g. 'Pune', 'tiffin', 'CAC', 'killed']"
allowed-tools: Read, Write, Edit, Glob, Grep
---

# /venture:ledger

The ledger (`ventures/LEDGER.md`) is the compounding memory of every run in this project: which ideas died where and why, which sources produced real signals, which were useless. Scouts and the generator read it at the start of each run.

## Show or search
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md` and the Ledger section of `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`.
2. If `ventures/LEDGER.md` does not exist: say there are no past runs and suggest `/venture:run`. Stop.
3. Arguments: `$ARGUMENTS`
   - **No arguments → summary:** number of runs; outcomes (PASS vs NOTHING PASSED); a table of runs (run id, location, target market, outcome); the most common causes of death (group decisive reasons into themes such as "no verified demand", "conservative CAC > price", "capital HARD limit", "licensing", "platform dependency"); the sources most often marked useful and useless; average local coverage per location.
   - **Arguments → search:** match terms case-insensitively against location, target market, idea pitches, verdicts, decisive reasons and lenses. Show each matching run and, within it, only the matching idea lines. For each match, give the run folder path so the user can open the verdict files (`ventures/runs/<run_id>/ideas/<id>/verdict-v<n>.md`).
4. Never edit the ledger from this command when showing or searching.

## Append (called at the end of every run by /venture:blueprint and direct /venture:kill)
1. If `ventures/LEDGER.md` does not exist, create it with `# venture ledger` and a blank line.
2. Append **one** entry at the end of the file, in exactly this schema. **Never delete or modify past entries.** If an entry with the same run id already exists (a re-run of blueprint), append a new entry headed `## <run_id> (amended <YYYY-MM-DD>)` instead of editing the old one.

```markdown
## <run_id>
- location: <city, country> | target market: <...>
- contract summary: <one line: capital (HARD/FLEX), hours, B2B/B2C, time to revenue, risk>
- outcome: PASS (<idea_id> — <pitch>) | NOTHING PASSED
- ideas:
  - <idea_id> | <pitch> | <verdict> | <decisive reason> | <lens>
- useful sources: <domains or communities that produced real, verified signals>
- useless sources: <domains or communities that produced nothing, or whose claims were struck>
- local data coverage: <0-10 from 01-local-market.md, or 'n/a (direct kill)'>
- pivots used: <n>
```

- List **every** idea from `03-ideas.md` and any pivot files (for a judge-candidate pivot, the old idea's line reads `KILL → PIVOTED → <id>`), including screen rejections (`REJECTED (screen)`), ideas not carried (`NOT CARRIED (rank)`), pivots (`PIVOTED → <id>`), and halts (`HALTED (tamper)`).
- Decisive reason: one line, from the verdict's first decisive reason (or the screen rejection reason).
- Useful/useless sources: derive from the scouts' "Sources consulted" lists and from the audits (domains whose claims were VERIFIED vs struck).
