<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## ventures/LEDGER.md — writer: main (append only)

The ledger has a single H1 `# venture ledger` and one H2 per run, appended at the end. **Never delete or edit past entries.** (The heading keeps its pre-0.6 name so existing ledgers stay valid.)

```markdown
## <run_id>
- location: <city, country> | target market: <...>
- contract summary: <one line>
- outcome: PASS (<idea>) | VIABLE ON PAPER (<idea>) | NOTHING PASSED
- ideas:
  - <idea_id> | <pitch> | <verdict> | <decisive reason> | <lens>
- useful sources: <domains or communities that produced real signals>
- useless sources: <...>
- local data coverage: <0-10>
- pivots used: <n>
- generation lessons: <from 91-nothing-passed.md § Why the search missed, or 'n/a (passed)'>
```

Verdict values in the ledger: `PASS`, `VIABLE ON PAPER`, `KILL`, `KILL (money gate)`, `DROPPED (strategist)`, `REJECTED (screen)`, `NOT CARRIED (rank)`, `PIVOTED → <new id>`, `HALTED (tamper)`.
