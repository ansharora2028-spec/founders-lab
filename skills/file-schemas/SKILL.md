---
name: file-schemas
description: Exact markdown schemas for every file in a venture run folder (contract, scouting, ideas, screen, kill criteria, forge, economics, diff, prosecutions, audit, verdict, blueprint, nothing-passed, run-log, ledger) plus the visibility matrix. Read the schema for your output file before writing it.
user-invocable: false
---

# venture file schemas

Every venture file is markdown with YAML front matter, fixed H2 sections in the order shown, and claims written in the claim format. Do not add, rename or reorder H2 sections. If a section has nothing to say, write `- none` under it. Empty templates for every file live in `templates/` at the plugin root.

## Conventions

### Front matter (all files except LEDGER.md)

```yaml
---
run_id: 2026-01-31-pune-b2c          # <YYYY-MM-DD>-<slug>
idea_id: I03                          # only for per-idea files; omit otherwise
agent: prosecutor-market              # agent name, or "main" for files the main session writes
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
| Global/national signal | `S<nn>` | `S11` |
| Idea | `I<nn>` | `I03` |
| Pivoted idea | `<old-id>-P<k>` | `I03-P1` |
| Market kill criterion | `KM<n>` | `KM2` |
| Execution kill criterion | `KE<n>` | `KE1` |
| Market flaw | `FM<n>` | `FM3` |
| Execution flaw | `FE<n>` | `FE2` |

## Visibility matrix (enforced by the main session)

Paths are relative to `ventures/runs/<run_id>/`. `LEDGER` is `ventures/LEDGER.md`. `raw idea` is the idea's entry in `03-ideas.md` (or `03-ideas-pivot<k>.md`).

| Agent | Mode | Paths it receives | Never receives |
|---|---|---|---|
| local-market-scout | — | 00, LEDGER | everything else |
| signal-scout | — | 00, LEDGER | everything else |
| generator | — | 00, 01, 02, LEDGER | 04, any kill-criteria, prosecutions, audits, verdicts of this run |
| screener | — | 00, 03 (or 03-ideas-pivot<k>), LEDGER | 01, 02 |
| prosecutor-market / -execution | criteria | 00, 01, 02, raw idea file + idea id | forge, economics, the other prosecutor's draft |
| forge | round 1 | 00, 01, 02, 03 (+ idea id) | kill-criteria, criteria drafts, prosecutions, audits, verdicts |
| forge | round 2 | as round 1 + forge-v1 + fixable-flaws-v1 (the Judge's fixable-flaw table, extracted by main) | kill-criteria, prosecutions, audits, the full verdict |
| economics-modeler | — | 00, 01, forge-v<n> (+ economics-v1 in round 2) | kill-criteria, prosecutions, audits, verdicts |
| prosecutor-market / -execution | kill v1 | 00, 01, 02, kill-criteria, forge-v1, economics-v1 | the other prosecutor's file, audit, verdict |
| prosecutor-market / -execution | kill v2 | 00, 01, 02, kill-criteria, diff-v2, economics-v2, own prosecution-v1 | **forge-v2**, the other prosecutor's files, audits, verdicts |
| evidence-auditor | round n | every file for that idea in round n except the verdict: 00, 01, 02, kill-criteria, forge-v<n> (or diff-v2 + forge-v2), economics-v<n>, both prosecution-v<n> | verdict-v<n>, earlier verdicts |
| judge | round n | everything for that idea, plus run-log (for the hash) | — |

In **direct kill mode** (`/venture:kill "<idea>"`) there is no scouting and no forge. `ideas/I01/idea.md` (the idea as the user stated it) stands in for both the raw idea and `forge-v1`:
- prosecutors in criteria mode receive `00` and `idea.md`;
- the economics-modeler receives `00` and `idea.md` and writes `economics-v1.md` (without it a PASS is impossible under rule 3);
- prosecutors in kill mode receive `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`;
- the auditor and judge receive everything for the idea as usual.
There is no revision round in direct mode: REVISE is reported to the user as "would need: <fixable flaws>" and recorded as KILL in the ledger.

---

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
- mode: quick | standard | deep
- ideas to generate: 3 | 8 | 12
- ideas to carry forward: 1 | 3 | 5

## Confirmation
- confirmed by user: yes
- confirmed at: <iso>
- how: <AskUserQuestion | plain chat | arguments (non-interactive)>
```

## 01-local-market.md — writer: local-market-scout

```markdown
---
(front matter, agent: local-market-scout)
---

## Scope
- city/region researched: <...>
- target market: <...>
- focus: broad | specific idea: "<idea>"
- languages used in queries: <...>

## What is selling now
- [C01] ... [source: ...]

## Launched and failed (last 2–3 years)
- [Cnn] <company/product>, <what happened>, <year> [source: ...]

## Price points and purchasing power
## Local competitors
## Regulation and licensing
## How locals search and buy
(language, platforms, marketplaces, payment habits)

## Distribution channels
| channel | strength (weak/medium/strong) | evidence |
|---|---|---|

## Signals
| id | signal | claim refs | strength | relevance to contract |
|---|---|---|---|---|
| L01 | ... | C03, C07 | medium | ... |

## Coverage
- coverage score: <0-10>
- where data was thin: <plain statement>
- national/global data used in place of local: <list with labels, or 'none'>

## Sources consulted
- <url> — <useful | not useful>
```

## 02-signals.md — writer: signal-scout

```markdown
---
(front matter, agent: signal-scout)
---

## Scope
- window: <from date> to <to date>
- focus: broad | specific idea: "<idea>"
- ledger sources skipped as previously useless: <list or 'none'>

## Signals
| id | signal | source | date | strength | relevance to contract |
|---|---|---|---|---|---|
| S01 | ... | <url> | YYYY-MM-DD | weak/medium/strong | ... |

## Recurring complaints
- [C01] ... [source: ...]
## Search and social momentum
## Newly cheap or possible technology
## Regulatory shifts
## Funding and acquisition flows

## Sources consulted
- <url or community> — <useful | not useful>
```

## 03-ideas.md — writer: generator (also 03-ideas-pivot<k>.md — writer: main)

```markdown
---
(front matter, agent: generator)
---

## Generation notes
- depth mode: <mode>, ideas generated: <n>
- starting path: a | b | c
- ledger ideas avoided: <ids/pitches, or 'none'>

## Ideas

### I01
- pitch: <one line>
- customer: <who pays>
- problem: <the pain>
- revenue model: <how money comes in>
- lens: unbundle | transplant | boring-b2b | unfair-advantage | contrarian | cheap-now | user-original | user-variant
- signal ids: L02, S05
- material change vs ledger (only if it resembles a dead ledger idea): <...>

### I02
...
```

`03-ideas-pivot<k>.md` holds exactly one idea in the same shape, with id `<old-id>-P<k>`, plus `- pivoted from: <old-id>` and `- pivot reason: <field changed and why>`.

## 04-screen.md — writer: screener (also 04-screen-pivot<k>.md)

```markdown
---
(front matter, agent: screener)
---

## Hard-constraint check
| idea | K# checked | result | reason |
|---|---|---|---|
| I01 | K1, K3, K7, K8 | pass / REJECTED | ... |

## Competitors
### I01
- [C01] <competitor> — <what it does, price if known> [source: <url>]
- novelty: crowded | contested | open

## Scores
| idea | signal | constraint fit | novelty | unfair advantage | speed to revenue | total /25 |
|---|---|---|---|---|---|---|

## Ranking
1. I04 — 19/25
2. I01 — 17/25
...
- rejected: I06 (K1), I08 (K8)
```

## ideas/I01/idea.md — writer: main (direct kill mode only)

```markdown
---
(front matter, idea_id: I01, agent: main, version: 1)
---

## Idea as stated
"<verbatim user text>"

## Parsed
- pitch: <one line, user's words where possible>
- customer: <as stated, or 'not stated'>
- problem: <as stated, or 'not stated'>
- revenue model: <as stated, or 'not stated'>
- budget/constraints mentioned in the idea: <...>
```

The main session parses, it does not improve. Anything the user did not state is written `not stated`.

## ideas/<id>/criteria-market.md and criteria-execution.md — writers: prosecutors (criteria mode)

Drafts. Same shape as one half of `kill-criteria.md`:

```markdown
---
(front matter, idea_id, agent: prosecutor-market | prosecutor-execution, version: 1)
---

## Criteria
### KM1
- dies unless: <specific, testable statement>
- threshold: <number, count, or observable fact>
- evidence that satisfies it: <what kind of source would prove it>
- why it matters: <one line>
```

3–6 criteria per prosecutor.

## ideas/<id>/kill-criteria.md — writer: main (merge), then LOCKED

```markdown
---
(front matter, idea_id, agent: main, version: 1)
locked: true
---

## Raw idea
(verbatim copy of the idea block from 03-ideas.md)

## Market criteria
(verbatim KM blocks from criteria-market.md)

## Execution criteria
(verbatim KE blocks from criteria-execution.md)

## Lock
- locked at: <iso>
- note: hash is recorded in run-log.md, not in this file
```

After writing: `chmod 444`, compute SHA-256, record in `run-log.md` § Locks.

## ideas/<id>/forge-v<n>.md — writer: forge

```markdown
---
(front matter, idea_id, agent: forge, version: n)
---

## Core identity
- customer: <exact segment>
- problem: <exact pain>
- revenue model: <exact model>
- pivot declared: no | YES — <field(s) changed>

## Persona
- [C01] <who, where they are, what they spend money on today> [source: ...]

## Narrowest wedge
## Problem severity
## Path to first 100 customers
(in the target market, channel by channel, with numbers)

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|

## Moat over time
## Assumptions
- [Cnn] ... [ASSUMPTION: ...]

## Fixes (round 2 only)
| flaw id | fix | evidence url |
|---|---|---|
| FM2 | ... | <url or NONE> |
```

## ideas/<id>/economics-v<n>.md — writer: economics-modeler

```markdown
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

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1L HARD | ₹1.4L | BREAKS |

## Verdict inputs
- conservative unit economics positive: yes | no
- HARD constraints broken in conservative case: <list or 'none'>
- FLEXIBLE stretches required: <list with unlock condition status, or 'none'>
```

## ideas/<id>/fixable-flaws-v1.md — writer: main

```markdown
---
(front matter, idea_id, agent: main, version: 1)
---

## Fixable flaws
(verbatim copy of the "Fixable flaws" table from verdict-v1.md — nothing else from the verdict)
```

## ideas/<id>/diff-v2.md — writer: main

```markdown
---
(front matter, idea_id, agent: main, version: 2)
---

## Pivot check
- customer changed: no | yes
- problem changed: no | yes
- revenue model changed: no | yes
- result: NOT A PIVOT | PIVOT → new idea <id>

## Changes
| # | addresses flaw | field | old value | new value | evidence url |
|---|---|---|---|---|---|
| D1 | FM2 | path to first 100 | ... | ... | <url or NONE> |

## Unaddressed flaws
- <flaw ids from verdict-v1 that forge did not fix, or 'none'>
```

Values are copied verbatim from forge-v1 / forge-v2, never paraphrased into stronger language. A row with `NONE` as evidence is a non-fix (rule 4).

## ideas/<id>/prosecution-market-v<n>.md and prosecution-execution-v<n>.md — writers: prosecutors (kill mode)

```markdown
---
(front matter, idea_id, agent: prosecutor-market | prosecutor-execution, version: n)
---

## Inputs read
- <list of exact paths read>

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | MET / NOT MET / INSUFFICIENT EVIDENCE | C03, forge-v1.md#C05 | ... |

## Flaws
### FM1 — FATAL | FIXABLE
- flaw: <statement>
- evidence: [Cnn] ... [source: ...]
- what would fix it (FIXABLE only): <exact evidence that would fix it, and whether it is obtainable by desk research>
- fix would change customer/problem/revenue model: no | yes

## Evidence
- [C01] ... [source: ...]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | yes / no | ... |
```

Prosecutors may only assess criteria that are in `kill-criteria.md`; they can add flaws but not criteria.

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

## ideas/<id>/verdict-v<n>.md — writer: judge

```markdown
---
(front matter, idea_id, agent: judge, version: n)
---

## Hash check
- expected (run-log): <sha256>
- actual: <sha256>
- result: MATCH | MISMATCH — HALTED

## Verdict
- verdict: PASS | REVISE | KILL | HALTED
- round: 1 | 2
- confidence: <1-10>

## Criteria (after audit)
| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | MET | economics-v1.md#C03 | MET |

## Decisive reasons
1. <reason> — <file#claim refs>

## Demand evidence
- <surviving refs, or 'none surviving'>

## Conservative economics
- fits contract: yes | no — <refs>

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|

## Ignored as struck
- <refs>
```

No encouragement. No softening.

## 90-blueprint.md — writer: main

```markdown
---
(front matter, agent: main)
---

## Winning idea
- idea: <id> — <pitch>
- verdict file: ideas/<id>/verdict-v<n>.md
- why it beat the others: <reasons with refs>

## This week's 3 cheapest experiments
| # | experiment | cost | time | success threshold | kill threshold |
|---|---|---|---|---|---|

## MVP scope
### In
### Out

## Pricing
## Path to first 100 customers
## 30-day plan
| week | actions | output | decision gate |
|---|---|---|---|

## Kill signals
- stop if: <observable signal with number>

## Caveats
- research assistance, not financial advice; key ASSUMPTIONs still unverified: <list>
```

## 91-nothing-passed.md — writer: main

```markdown
---
(front matter, agent: main)
---

## Summary
- ideas generated: n, screened out: n, not carried: n, killed: n, pivoted: n   (count each idea once, by its final status)

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|

## Estimated savings (ESTIMATE)
- capital saved: <range>
- months saved: <range>
- assumptions: <list each assumption>

## Patterns across deaths
## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|

## Directions for the next run
```

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
| ... | prosecutor-market | kill | I01 | 2 | 00-contract.md; 01-local-market.md; 02-signals.md; ideas/I01/kill-criteria.md; ideas/I01/diff-v2.md; ideas/I01/economics-v2.md; ideas/I01/prosecution-market-v1.md | ideas/I01/prosecution-market-v2.md |

## Locks
| idea | file | sha256 | locked at |
|---|---|---|---|

## Pivots
| from | to | field changed | counter after |
|---|---|---|---|

## Blindness self-check
- forge-v2.md passed to a prosecutor: never | <violations>
- a prosecutor passed the other prosecutor's file: never | <violations>
- kill-criteria passed to forge or economics-modeler: never | <violations>
```

## ventures/LEDGER.md — writer: main (append only)

The ledger has a single H1 `# venture ledger` and one H2 per run, appended at the end. **Never delete or edit past entries.**

```markdown
## <run_id>
- location: <city, country> | target market: <...>
- contract summary: <one line>
- outcome: PASS (<idea>) | NOTHING PASSED
- ideas:
  - <idea_id> | <pitch> | <verdict> | <decisive reason> | <lens>
- useful sources: <domains or communities that produced real signals>
- useless sources: <...>
- local data coverage: <0-10>
- pivots used: <n>
```

Verdict values in the ledger: `PASS`, `KILL`, `REJECTED (screen)`, `NOT CARRIED (rank)`, `PIVOTED → <new id>`, `HALTED (tamper)`.
