---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: judge
version: 1
created: 2026-10-21T10:28:17Z
---

## Hash check
- expected (run-log): ca13d6a56fd70dc049340b284dcb086436ca9e9c673cc9a245caca30f4e2597d
- actual: ca13d6a56fd70dc049340b284dcb086436ca9e9c673cc9a245caca30f4e2597d (sha256sum)
- result: MATCH

## Verdict
- verdict: REVISE
- round: 1
- confidence: 5

## Criteria (after audit)
| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | 01-local-market.md#C12 (Success Rs 2,000, VERIFIED); #C25-C27 listings without price or reviews. #C01 struck as stated. 1 verified price, 0 providers with 5 reviews | FIXABLE (partly offline-only; Justdial/Maps prices partly desk-checkable) |
| KM2 | INSUFFICIENT EVIDENCE | no class 6-10 enrolment figure in any file; 01-local-market.md#C17 (population only) | FIXABLE, desk-researchable (UDISE+) |
| KM3 | INSUFFICIENT EVIDENCE | 01-local-market.md#C46 (no Satara reviews); forge-v1.md#C16 (ASSUMPTION); bus-stand batch of 30 is hearsay | offline-only gap (parent survey); no contrary evidence beyond the peer-town proxy |
| KM4 | INSUFFICIENT EVIDENCE | 01-local-market.md#C12/#C24 (Success 8 years, school-age focus not shown), #C26 (Breath 9 years, no price); no graveyard found | FIXABLE (provider fees and batch sizes need a visit; offline-only) |
| KM5 | INSUFFICIENT EVIDENCE | 02-signals.md S10 (ChatGPT Go Rs 399, VERIFIED); S05 struck; forge-v1.md format has no minutes-per-student calculation | FIXABLE, desk-researchable (worked format calculation) |
| KE1 | INSUFFICIENT EVIDENCE (prosecutor: NOT MET) | Prosecutor's NOT MET rests on the Rs 56,500 setup, which includes a 6-month deposit from economics-v1.md#C07 (struck, UNREACHABLE source). Rent is FOUNDER-ESTIMATE, fit-out ASSUMPTION. Hours 11-12, zero slack | FIXABLE, desk-researchable (rental listings with deposit terms, itemised costs) |
| KE2 | NOT MET on current plan, fixable | economics-v1.md "Student path" gives 9 students against 10; every conversion rate is ASSUMPTION; Q11 reach FOUNDER-COUNTED | FIXABLE (needs peer-town conversion benchmark, dated plan; pre-enrolments offline-only) |
| KE3 | NOT MET | economics-v1.md "Calculations" (verified arithmetic): break-even 14 vs limit 12; 30-student net Rs 9,500 vs Rs 10,000; month-12 cumulative about -Rs 72,566 (deposit-inclusive, deposit assumption struck). Locked stress (20% churn, Diwali/May gaps) not run | FIXABLE only through a price above Rs 600 and a rerun; price is not a customer, problem or revenue-model change |
| KE4 | INSUFFICIENT EVIDENCE (prosecutor: NOT MET) | 01-local-market.md#C33-C35 (VERIFIED draft terms); no final Act found 2026-10-21 (prosecution-v1.md#C01). Class 8-10 share of the band rests on equal-cohort ASSUMPTION; per-batch vs per-centre 25 unresolved; employment status ASSUMPTION | FIXABLE, partly desk (draft text, S&E rules, GST, DPDP); employment status offline-only |
| KE5 | NOT MET | forge-v1.md "Moat otherwise: none yet"; no incumbent response plan; no 40%-shortfall run; group-admin permission unconfirmed | FIXABLE, desk (plan, sensitivity run); admin permission offline-only |

I differ from the prosecutor on KE1 and KE4: the K1 breach depends on a struck deposit assumption, and the KE4 80% test depends on an ASSUMPTION about age cohorts. Neither is contradicted by evidence, so INSUFFICIENT EVIDENCE.

## Decisive reasons
1. No FATAL flaw: the prosecutor labelled FM1-FM3 and FE1-FE5 all FIXABLE, and I found nothing contradicting verified evidence or forcing a change of customer, problem or revenue model — prosecution-v1.md#FM1-FE5; audit-v1.md.
2. Not PASS: no locked criterion is MET, and demand evidence is thin: one VERIFIED Satara price (Success, Rs 2,000, school-age focus unshown) — audit-v1.md summary; 01-local-market.md#C12.
3. Not VIABLE ON PAPER: the simulation bar fails at 0.0% viable and 69.1% within capital, against 70% and 90% — simulation-v1.md. Condition 1 alone blocks it. The need-gap is also hearsay, with a peer-town proxy that points the other way (01-local-market.md peer table).
4. Conservative economics at the contract price do not work: break-even 14 students vs 12; month-12 profit about Rs 2,092 for 11-12 hours a week; 30-student net Rs 9,500 — economics-v1.md "Calculations", recomputed VERIFIED by the auditor. The K1 breach (peak Rs 79,011) rests on the struck deposit assumption (economics-v1.md#C07), so I do not rule a HARD-constraint break. It is a gap to repair.
5. A plausible fix exists that stays inside the same customer, problem and revenue model: a price above Rs 600 (the modeller's Rs 800 case gives break-even of 10 students), plus a rent-deposit listing check, UDISE+ enrolment sum, the draft Act text and a worked speaking-time format. All are within a revision round and none changes the customer, problem or revenue model. The Rs 800-1,000 prices are ASSUMPTION and untested (audit-v1.md, economics-v1.md#C05), so Forge needs evidence for them. Without it, round 2 fails.

## Demand evidence
- 01-local-market.md#C12/#C24: Success, Satara, Rs 2,000/month, 8 years (VERIFIED, one price point; school-age focus not shown).
- 01-local-market.md#C25-C27: Job 4U, Shivtej, Breath listed, no price or reviews.
- 01-local-market.md#C13: Siddheshwar Rs 500/person, period unknown.
- 02-signals.md#S06: national private-coaching spend (national, not local).
- Not enough for PASS: no verified revenue, search volume or multi-provider price list for Satara school-age spoken English.

## Conservative economics
- fits contract: no. Break-even 14 students vs the KE3 limit of 12; six-month and twelve-month cumulative cash negative; Diwali/May stress not run; the K1 and K5 breach is unproven because the deposit input is struck — economics-v1.md "Calculations" and "Constraint check"; audit-v1.md "Assumptions in load-bearing positions".

## Simulation
- viable share: 0.0% · within capital: 69.1% · bar: NOT MET — simulation-v1.md. Money gate passed (best case 90.0%).

## Viable-on-paper check
| condition | met? | evidence |
|---|---|---|
| 1. simulation bar met (≥70% viable, ≥90% within capital) | NO | simulation-v1.md: 0.0% and 69.1% |
| 2. no FATAL flaw survived | YES | prosecution-v1.md: none labelled FATAL; none meets the definition |
| 3. gap backed by peer-town, brand absence or founder-counted evidence | NO | gap rests on FOUNDER-ESTIMATE hearsay (forge-v1.md#C16); peer-town data shows no under-supply; PW has no English batch (01-local-market.md#C28), which is not a gap proof |
| 4. every failing criterion is INSUFFICIENT EVIDENCE for lack of findable local data, none contradicted | NO | KE3 and KE5 are NOT MET on the builders' own model; KM2, KM5, KE1 and KE4 are desk-fixable and unfixed |
| 5. fits every HARD constraint; strategist recommends CARRY with no unmitigated critical AGAINST | PARTIAL | strategy-v1.md: CARRY, 0 AGAINST. HARD fit in the conservative case is not shown (K1 and K5 unproven) |

## Assumptions to confirm (VIABLE ON PAPER only)
| # | assumption (from the sensitivity ranking) | how to confirm cheaply | stop if |
|---|---|---|---|
| - | not applicable | - | - |

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| KE3 / FE2 (price, break-even 14 vs 12, founder net about Rs 2,100/month at 17.5 students) | Source URLs for Satara or comparable-town spoken-English prices for school-age students at Rs 800 or more, then rerun the conservative model at the evidenced price with the locked stress (15 average students, 20% churn, no enrolment around Diwali and May). Break-even must be 12 students or fewer, and the 30-student net at least Rs 10,000. A price above Rs 600 must be declared as an offer change within the same revenue model; the Rs 800-1,000 values are currently ASSUMPTION | partly (provider prices); the pre-sale test is offline |
| KE1 / FE1 (setup Rs 56,500 and peak Rs 79,011 rest on an unsourced 6-month deposit) | Two or more published commercial-room listings in Satara or the Pune region with deposit terms, an itemised cost list with setup at most Rs 40,000, and setup plus 3 months of rent and supplies at most Rs 63,000 | yes (rental portals) for listings; room quotes are offline |
| KE2 (9 students vs 10 by day 60, all conversion rates ASSUMPTION) | A PEER-TOWN or published benchmark for WhatsApp-group-to-paid conversion, plus a dated plan from room confirmation to first class by 2026-12-21 with no registration step over 30 days | partly; pre-enrolments are offline |
| KE4 / FE3 (draft Act status, under-13 bar, 25-student counting, S&E, GST, DPDP, employment) | Draft or gazette text of the Act with the status checked at a new date, Labour Department S&E rule page, current CGST turnover rule, DPDP Rules, each with a URL. A plan showing at least 80% of the class 6-10 band servable, or a consent route, and registration budgeted at no more than Rs 10,000 and 30 days. The founder's written employment status is offline | yes, except employment status |
| KE5 / FE4, FE5 (no incumbent response, no 40% sensitivity, no admin permission) | A written response plan for Success, the bus-stand class and PhysicsWallah; a KE3 model run at 40% fewer students that stays at break-even; at least 2 channels with expected enrolments. Admin permission from 3 of 4 groups is offline | yes for the plan and run; admin permission is offline |
| KM5 / FM3 (no minutes-per-student calculation; AI substitutes at Rs 0-399) | A class-format calculation showing at least 10 minutes of individual speaking time per student per hour, with batch size, pair or rotation design and teacher feedback time. Cite the verified substitute prices (02-signals.md S10 and S12) | yes |
| KM2 / FM2 (class 6-10 base unmeasured) | School-level UDISE+ or Maharashtra enrolment sums for Satara city, classes 6-10, by medium, against at least 8,000 total and 1,500 English or semi-English | yes |
| KM1 / KM4 (only 1 verified price, no school-age focus shown) | Dated provider pages, Justdial or Google Maps listings with fees, batch sizes, reviews or years in business and target students for Success, Job 4U, Shivtej and Breath; a named closed-operator search or a sourced "none found" | partly; visits are offline |
| KM3 / FM1 (speaking-time gap is hearsay) | At least 5 public Satara complaints, or two providers' batch sizes verified at 20 or more. A founder-run survey of 10 named parents would give FOUNDER-COUNTED only | survey is offline-only; public evidence is unlikely to exist |

## Pivot candidate (KILL only)
- none — verdict is REVISE, not KILL.

## Ignored as struck
- 01-local-market.md#C01 (as stated), #C02, #C05; D06 and L08 fee support
- forge-v1.md#C08
- 02-signals.md#S05
- strategy-v1.md A1 (Success "course 1-4 months")
- economics-v1.md#C07, #C21
- economics-v1.md Scenarios "month 28" and "Rs 5,100" lines
- economics-v1.md Simulation-inputs price tier label (Rs 800/1,000 treated as ASSUMPTION)
