---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: judge
version: 2
created: 2026-10-21T10:42:35Z
---

## Hash check
- expected (run-log): ca13d6a56fd70dc049340b284dcb086436ca9e9c673cc9a245caca30f4e2597d
- actual: ca13d6a56fd70dc049340b284dcb086436ca9e9c673cc9a245caca30f4e2597d
- result: MATCH

## Verdict
- verdict: KILL
- round: 2
- confidence: 8

## Criteria (after audit)
| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | audit-v2.md Summary (Success Rs 2,000, 8 yrs; directory listings with tenure only); one verified Satara price, no reviews or batch counts | NOT MET for PASS. Offline-only gap (prices and reviews sit on Justdial/Maps or offline). |
| KM2 | INSUFFICIENT EVIDENCE | prosecution-v2.md#C03 (district primary figure only); diff-v2.md D10 admits not fixed | Desk-fixable and not done, so not an offline-only gap. |
| KM3 | INSUFFICIENT EVIDENCE | diff-v2.md D11 (0 of 5 complaints, 0 verified batch sizes); peer-town data shows no under-supply | Offline-only gap, but the peer-town benchmark points the other way. |
| KM4 | INSUFFICIENT EVIDENCE | prosecution-v2.md#C01, #C04 (Goranga 11 yrs, audit VERIFIED); fee and batch check unchecked | Survival half partly met. The fee and batch half is offline. |
| KM5 | INSUFFICIENT EVIDENCE | diff-v2.md D8 (10.5 min rests on a 60% ASSUMPTION; peer talk, not individual feedback); ChatGPT Go Rs 399 VERIFIED; SpeakX Rs 299 STRUCK | Paper calculation only. |
| KE1 | NOT MET | economics-v2.md "Calculations", "Constraint check": setup Rs 62,000 vs Rs 40,000 limit; Rs 76,600 to first revenue vs Rs 75,000 | NOT MET. Arithmetic VERIFIED by the auditor. The only rent listings (Rs 22,000-25,000, VERIFIED) are far above the founder's Rs 4,000-6,000. |
| KE2 | NOT MET | economics-v2.md "Student path": 5.4 students in the first revenue month vs 10 needed | NOT MET on the conservative path. All conversion inputs are ASSUMPTION. |
| KE3 | NOT MET | economics-v2.md: break-even 14 vs limit 12; path 10.5 at month 12; cumulative -Rs 106,656; simulation-v2.md 0.0% viable | NOT MET. |
| KE4 | NOT MET | prosecution-v2.md#C10 (draft Act, no final text, VERIFIED); class 8-10 is about 60% of the band vs the 80% bar | NOT MET on the strict reading. Parts (c) to (e) are unresolved. |
| KE5 | NOT MET | diff-v2.md D7; economics-v2.md "Verdict inputs": at Rs 600 the model is already below break-even, so a 40% shortfall fails by construction | NOT MET. Admin permission is an offline-only gap. |

I agree with the prosecutor on every status. Against the prosecutor's FM and FE labels, I treat FE2 as FATAL (see reasons).

## Decisive reasons
1. The conservative economics break HARD K1, and K5 if the deposit is lost. Capital to first revenue is Rs 76,600 against Rs 75,000. Cumulative cash at month 12 is -Rs 106,656. Break-even needs 14 students against a path of 10.5. Monthly cash is negative in all 12 months. The auditor re-computed all of this and found it correct. This triggers the KILL rule "conservative economics break a HARD constraint". — economics-v2.md "Calculations", "Constraint check"; audit-v2.md row "conservative arithmetic" (VERIFIED)
2. FE2 survives as FATAL. At the contract price of Rs 600 there is no fix. The only route is Rs 800 or more, and no school-age spoken-English price supports that. The Success Rs 2,000 listing states no target students, and its "1-4 months" course length was STRUCK. The Vallath Rs 1,300 price is national and online. The Rs 800 figure is ASSUMPTION, and a modelling input is not support. Even with all three changes (price, 3-month deposit, cheaper seats), month 12 cumulative is -Rs 68,216, and that works only if the deposit term is obtained. No Satara listing shows such a term, and the rentok source for it was struck. — economics-v2.md "Verdict inputs"; audit-v2.md Struck claims; prosecution-v2.md FE2
3. The simulation is far below the bar. It shows 0.0% viable and 17.6% within capital, against 70% and 90%. The money gate passed only on the unhaircut best case (34.2%). Reach would have to be 7.4 times the haircut value. — simulation-v2.md
4. It is round 2, so REVISE is unavailable. VIABLE ON PAPER fails conditions 1, 2 and 4. KE1 to KE5 are NOT MET on contrary arithmetic, not for lack of findable local data. KM2 is desk-fixable and left unfixed. — prosecution-v2.md Criteria assessment
5. The round 2 fixes did not cure the flaws. D1 to D7, D10 and D11 are rejected as fixes (prosecution-v2.md Round-2 notes). The deposit and rent inputs are ASSUMPTION or rest on struck claims. D3 and D4 raised rather than lowered the cost risk. — diff-v2.md; prosecution-v2.md

## Demand evidence
- Surviving: Success Rs 2,000 per month, 8 years (01-local-market.md#C12, #C24; economics-v2.md#C02 price and tenure only). Four to five Satara directory listings with tenure (01-local-market.md#C01, #C27; diff-v2.md D9). PW Satara Vidyapeeth, adjacent and with no English batch (01-local-market.md#C04). National coaching spend (02-signals.md S06).
- This is not verified paying-customer evidence for school-age spoken English in Satara. No competitor revenue, search volume or Satara reviews survived. The tuition price of Rs 800-1,500 is FOUNDER-COUNTED only.
- Demand evidence is therefore not positive and VERIFIED as PASS requires.

## Conservative economics
- fits contract: no — economics-v2.md "Constraint check" (K1 BREAKS, K5 BREAKS if the deposit is lost, K6 at the limit with no slack). Rs 106,656 cumulative cash out and a Rs 76,600 outlay to first revenue.

## Simulation
- viable share: 0.0% · within capital: 17.6% · bar: NOT MET — simulation-v2.md

## Viable-on-paper check
| condition | met? | evidence |
|---|---|---|
| 1. simulation bar met (≥70% viable, ≥90% within capital) | NO | simulation-v2.md: 0.0% and 17.6% |
| 2. no FATAL flaw survived | NO | FE2 survived: at the contract price there is no break-even, and the Rs 800 route has no school-age price source |
| 3. gap backed by peer-town, brand absence or founder-counted evidence | NO | The peer-town benchmark (01-local-market.md#C60, VERIFIED) shows no under-supply. The 300 parent reach is FOUNDER-COUNTED but backs reach, not a gap. Hearsay on speaking is FOUNDER-ESTIMATE. PW having no English batch is not a brand-absence gap in this segment. |
| 4. every failing criterion is INSUFFICIENT EVIDENCE for lack of findable local data, none contradicted | NO | KE1 to KE5 are NOT MET on arithmetic. KM2 is desk-fixable and unfixed. |
| 5. fits every HARD constraint; strategist recommends CARRY with no unmitigated critical AGAINST | NO | The strategist said CARRY (strategy-v1.md), but it was written before the round 2 economics, and the conservative case breaks K1. |

## Assumptions to confirm (VIABLE ON PAPER only)
| # | assumption (from the sensitivity ranking) | how to confirm cheaply | stop if |
|---|---|---|---|
| - | not applicable, verdict is not VIABLE ON PAPER | - | - |

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| - | not applicable, round 2 | - |

## Pivot candidate (KILL only)
- none. The conservative case fails at the contract's Rs 600, and the only numerical fix is a price of Rs 800 or more. That price has no surviving school-age source. The audit struck the SpeakX price, the course-length claim and the deposit norm. Narrowing the customer to class 8-10 already lowered reach and made the path worse. No surviving evidence (unstruck file#claim) supports a different customer, problem or revenue model that fits K1, so a candidate would be invented. Pivots used are 0/2, but the grounding condition fails.

## Ignored as struck
- economics-v2.md#C02, forge-v2.md#C01 (Success course length "1 to 4 months")
- economics-v2.md#C04, prosecution-v2.md#C05, forge-v2.md#C28, strategy-v1.md A3 (SpeakX Rs 299 at the refund-policy URL)
- economics-v2.md#C07 (3-6 month deposit norm, rentok PDF)
- economics-v2.md#C23 (Meta cost per lead Rs 200-600; CPC Rs 0.51-2.26)
- forge-v2.md#C08, 01-local-market.md#C05 (CBSE Class 10 fee range Rs 18,000-52,000; Appasaheb Rs 26,550)
- forge-v2.md dated plan (Dhanteras to Bhai Dooj dates)
- 02-signals.md S05 (SpeakX Rs 299 and 200,000 subscribers at the cited URLs)
- strategy-v1.md C6 ("about 20 by month 3")
- Note: none of these struck claims supports a surviving FATAL flaw or the KILL. FE2 rests on economics-v2.md arithmetic that the auditor verified.
