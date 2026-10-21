<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->

## Conventions

### Front matter (all files except LEDGER.md)

```yaml
---
run_id: 2026-01-31-pune-b2c          # <YYYY-MM-DD>-<slug>
idea_id: I03                          # only for per-idea files; omit otherwise
agent: prosecutor                     # agent name, or "main" for files the main session writes
version: 1                            # round number for per-idea files (1 or 2); 1 otherwise
created: 2026-01-31T10:42:00Z         # ISO 8601 UTC: main session = output of `date -u +%Y-%m-%dT%H:%M:%SZ`; agents = the Timestamp line of their prompt
---
```

### Claim format

Every factual claim is one bullet:

```
- [C07] <claim> [source: <url>]
- [C08] <claim> [ASSUMPTION: <why it is reasonable>]
```

- `C07` is a claim id, unique **within the file**. Other files reference it as `<filename>#C07`, e.g. `economics-v1.md#C07`.
- A claim with both a source and an inference may write `[source: <url>; inference: <one line>]`.
- Geography tag when not the target market: append `(national)`, `(global)` or `(other city: <name>)` before the bracket.
- Dates of sources go inside the bracket when known: `[source: <url>, 2026-03-14]`.
- Opinions, judgements and reasoning that are not facts are written as plain prose or as `- reasoning: ...` lines, never as claims.

### Ids

| Thing | Format | Example |
|---|---|---|
| Run | `<YYYY-MM-DD>-<slug>` | `2026-01-31-pune-b2c` |
| Local-market signal | `L<nn>` | `L04` |
| Demand anchor (money already moving) | `D<nn>` | `D03` |
| Global/national signal | `S<nn>` | `S11` |
| Idea | `I<nn>` | `I03` |
| Pivoted idea | `<old-id>-P<k>` | `I03-P1` |
| Market kill criterion | `KM<n>` | `KM2` |
| Execution kill criterion | `KE<n>` | `KE1` |
| Market flaw | `FM<n>` | `FM3` |
| Execution flaw | `FE<n>` | `FE2` |
