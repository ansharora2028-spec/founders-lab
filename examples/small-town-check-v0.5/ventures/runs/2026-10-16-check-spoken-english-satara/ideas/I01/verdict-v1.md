---
run_id: 2026-10-16-check-spoken-english-satara
idea_id: I01
agent: judge
version: 1
created: 2026-10-16T09:20:44Z
---

## Hash check
- expected (run-log): a7b86c39668b86f9906183ea131ee77a4baeb0042de6b424ab9fe3c081c63d4a
- actual: a7b86c39668b86f9906183ea131ee77a4baeb0042de6b424ab9fe3c081c63d4a (computed by me with `shasum -a 256` on ideas/I01/kill-criteria.md; not supplied by the main session)
- result: MATCH

## Verdict
- verdict: KILL
- round: 1
- confidence: 6

## Criteria (after audit)
Where the prosecutors overlap (KM3 / KE2), both say INSUFFICIENT EVIDENCE, so I used that. Each other criterion was assessed by one prosecutor only; I read the surviving evidence myself and agree.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | 01-local-market.md#C03 (listing, no customers), prosecution-market-v1.md#C06 | NOT MET for PASS. Partly desk-fixable (Justdial/Maps), partly offline. |
| KM2 | INSUFFICIENT EVIDENCE | only 01-local-market.md#C46, an ASSUMPTION | NOT MET for PASS. Desk-fixable (UDISE+). |
| KM3 | INSUFFICIENT EVIDENCE | 01-local-market.md#C27-C31 (VERIFIED draft terms; language classes not mentioned; under-13 bar) | NOT MET for PASS. Desk-fixable (official text). |
| KM4 | INSUFFICIENT EVIDENCE | none for in-person kids' operators over 24 months; no closure found either | NOT MET for PASS. Partly desk-fixable. |
| KM5 | INSUFFICIENT EVIDENCE | prosecution-market-v1.md#C09 (national only; spend base unclear); 02-signals.md#S08 spend figures struck | NOT MET for PASS. Desk-fixable (MoSPI Maharashtra tables). |
| KE1 | NOT MET | economics-v1.md conservative setup ₹29,000 against the locked ₹25,000 threshold (C12-C16, all ASSUMPTION); cash to first revenue ₹43,200 fits | NOT MET. Rests on ASSUMPTION inputs, so the status is conditional. |
| KE2 | INSUFFICIENT EVIDENCE | 01-local-market.md#C27-C30; official text never opened; employment status unknown | NOT MET for PASS. Desk-fixable (text); offline (employment). |
| KE3 | NOT MET | economics-v1.md Scenarios: conservative break-even 15 (16 with replacement CAC) against threshold 12; about 2 students at month 2 against 10 | NOT MET. Rests on ASSUMPTION conservative inputs. |
| KE4 | NOT MET | economics-v1.md: conservative month-12 profit about -₹5,700, cumulative about -₹99,400; simulation-v1.md P50 month-12 profit +₹766 | NOT MET. Part (a) fails, (b) and (c) pass. |
| KE5 | INSUFFICIENT EVIDENCE | FK Q5, Q11 (counted); admin consent and school rules unknown | NOT MET for PASS. Offline-only gap. |

## Decisive reasons
1. The conservative economics break HARD constraints. They show cumulative cash about -₹99,400 at month 12, over the ₹75,000 K1 and K5 limit. Cash passes -₹75,000 in month 8 unless a stop rule is written in, and none is. Rule 2 makes this a KILL without any fixability test. — economics-v1.md Constraint check (K1, K5) and Verdict inputs; economics-v1.md#C30; audit-v1.md (arithmetic recomputed, VERIFIED)
2. The simulation bar is far from met. 2.6% of runs break even by month 2 within capital, against the 70% bar, and 40.0% never break even in 12 months. Within-capital is 91.5%, which clears the 90% bar only by 1.5 points. P50 month-12 profit is +₹766. VIABLE ON PAPER (condition 1) is therefore unavailable. The prosecutor-execution notes that the "by month 2" mapping depresses the 2.6%, but the P10 and P50 profit and cash rows show thin economics on their own. — simulation-v1.md
3. No PASS is possible. Every market criterion is INSUFFICIENT EVIDENCE, and three execution criteria are NOT MET. Surviving demand evidence is weak only (see below). — prosecution-market-v1.md Criteria assessment; audit-v1.md Summary
4. Both prosecutors state FATAL: none, and I found none that meets the FATAL definition. Nothing contradicts the idea with verified evidence. The negative economics rest on conservative inputs the auditor lists as load-bearing ASSUMPTIONs (reach 40, conversion 2%, churn 15%, rent ₹6,000 from heard FK Q7, deposit ₹12,000). I weigh that when setting confidence. It does not soften the rule, because Rule 2 applies to the conservative scenario as built. — audit-v1.md § Assumptions in load-bearing positions
5. Fixes exist and none is a pivot (venue at ₹0-500, a paid pre-enrolment cohort, official Act text), but a REVISE is unavailable because reason 1 is an independent KILL trigger. Under Rule 6 a revision cannot be offered after a KILL. — economics-v1.md "what would have to change"

## Demand evidence
- none surviving that qualifies as positive and VERIFIED demand evidence.
- Weak items that survived:
  - 01-local-market.md#C03: Success, Satara, ₹2,000/month. A seller listing with no age group, orders or reviews.
  - 01-local-market.md#C01: IndiaMART listings of Satara spoken-English sellers.
  - 01-local-market.md#C06: PW Pathshala present, no price.
  - 02-signals.md#S05: SpeakX, company-claimed subscribers, national and online.
  - 02-signals.md#C02: PlanetSpark customers exist, national and online.
  - prosecution-market-v1.md#C07, #C08: other-city operators.
- The FOUNDER-COUNTED tuition spend of ₹800-1,500 per subject (FK Q9) and the FOUNDER-ESTIMATE ₹1,000 bus-stand class (FK Q10) cannot support a PASS.
- The strongest quantified claim, PlanetSpark FY25 revenue, was struck.

## Conservative economics
- fits contract: no. K1 and K5 break over 12 months at about -₹99,400 without a stop rule (economics-v1.md Constraint check). K6 fits with zero slack (2.0 months). Cash to first revenue (₹43,200) fits K1. The K9 stretch is used, with its "only within K1" condition met on first-revenue cash only. The conservative unit economics are negative: break-even 15 students against about 2.5 modelled (economics-v1.md Verdict inputs).

## Simulation
- viable share: 2.6% · within capital: 91.5% · bar: NOT MET — simulation-v1.md

## Viable-on-paper check
| condition | met? | evidence |
|---|---|---|
| 1. simulation bar met (≥70% viable, ≥90% within capital) | NO (2.6%; 91.5% within capital) | simulation-v1.md |
| 2. no FATAL flaw survived | YES | prosecution-market-v1.md, prosecution-execution-v1.md (FATAL: none) |
| 3. gap backed by peer-town, brand absence or founder-counted evidence | NO. Peer-town table shows supply "in line" (audit: imprecise, not reversed). No brand-absence evidence. Founder-counted items cover reach and tuition spend, not the gap. The gap itself is hearsay. | 01-local-market.md peer-town benchmark; audit-v1.md; strategy-v1.md B2 |
| 4. every failing criterion is INSUFFICIENT EVIDENCE for lack of findable local data, none contradicted | NO. KE1, KE3 and KE4 are NOT MET. KM2, KM3 and KM5 are desk-fixable and unfixed. | verdict Criteria table |
| 5. fits every HARD constraint; strategist CARRY with no unmitigated critical AGAINST | PARTIAL. Strategist said CARRY with 0 critical AGAINST. The conservative case breaks K1 and K5 over 12 months. | strategy-v1.md E; economics-v1.md |

## Assumptions to confirm (VIABLE ON PAPER only)
| # | assumption (from the sensitivity ranking) | how to confirm cheaply | stop if |
|---|---|---|---|
| - | not applicable: verdict is KILL | - | - |

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| - | not applicable: verdict is KILL, no revision round | - |

## Pivot candidate (KILL only)
- none. The run has used 0 of 2 pivots and every HARD constraint is satisfiable by a candidate. But the reason for the KILL is not that the only fix changes customer, problem or revenue model. The plausible fixes (a venue at ₹0-500, paid pre-enrolment before renting, Act text) leave all three fields unchanged, so the pivot condition in the rubric is not met. The same customer, problem and revenue model could be re-proposed as a new run with a zero-rent venue and a pre-enrolled cohort if the founder chooses, but that is not a Judge candidate.

## Ignored as struck
- 01-local-market.md#C02, #C05, #C22, #C09, #C13, #C24, #C41 (anchor D08)
- 02-signals.md#S04, #S08 (spend figures), #S09
- forge-v1.md#C07, #C08, #C24
- economics-v1.md#C15 (cited support only; the ₹3,000 / ₹1,000 / ₹0 inputs stay as ASSUMPTION)
- strategy-v1.md A3 online rungs, and C6 "6 / 15 / 24" students in months 1-3

Confidence is 6: coverage is thin (3/10), 14 of 58 audited rows were struck, and the KILL rests on conservative ASSUMPTION inputs and on a literal application of Rule 2. The verdict would not change on the evidence of record: the simulation bar fails by a wide margin, and no market criterion is MET.
