---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: prosecutor
version: 2
created: 2026-10-21T10:36:19Z
---

## Inputs read
- <scratch>/ventures/runs/2026-10-21-check-satara-english/00-contract.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/00-founder-knowledge.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/01-local-market.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/02-signals.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/kill-criteria.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/diff-v2.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/economics-v2.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/simulation-v2.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/prosecution-v1.md

## Criteria assessment
Market side
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | C01, C02; diff-v2.md D9; 01-local-market.md#C12, #C24-C27 | Still one verified Satara price (Success, ₹2,000). D9 adds only tenure years (Goranga 11, Job 4U 15, Shivtej 11, Breath 9) and "Best Price" labels. Tenure is not a dated price list, batch count or 5 reviews. Nothing contradicts demand. The missing proof (prices, reviews) is offline or on Justdial/Google Maps, which the scout could not reach: offline-only gap. A founder call can reach FOUNDER-COUNTED only, so MET is not reachable by this route. |
| KM2 | INSUFFICIENT EVIDENCE | diff-v2.md D10; C03 | Not fixed. No Satara city enrolment by class or medium. The only figures are a district primary total and one school. The narrowing to class 8-10 makes the 8,000 (classes 6-10) test harder to read. Obtainable by desk research (school-level UDISE+ sums), so this is not an offline gap and the builders did not do it. |
| KM3 | INSUFFICIENT EVIDENCE | diff-v2.md D11; 01-local-market.md#C44, #C45, #C46 | 0 of 5 public complaints, 0 verified batch sizes of 20 or more. The gap rests on "founder heard". The parent survey (b) is offline-only and gives FOUNDER-COUNTED at best. Peer-town data shows no under-supply. |
| KM4 | INSUFFICIENT EVIDENCE | diff-v2.md D9; C02, C04 | Survival half: Goranga Education (11 years, "English Coaching Classes For 10th Class") is a school-age case, but years are self-reported directory data. Graveyard: none found after searching (stated, not proof of none). The "no provider at ₹700 or less with batches of 15 or fewer" half is unchecked, since prices are hidden and the bus-stand class (₹1,000, 30 per batch) is hearsay. The required check of fees and batch sizes is an offline visit. |
| KM5 | INSUFFICIENT EVIDENCE | diff-v2.md D8; C05, C06 | A minutes-per-student calculation now exists (batch 20, 10 pairs, 17 min equal turns, 10.5 min at 60% use). Substitute prices are sourced (ChatGPT Go ₹399, SpeakX ₹299). The 10.5 minutes clears the 10-minute floor by 0.5 minute and rests on an ASSUMPTION (60% effective use). It is peer-to-peer talk with about 3.5 teacher-listening minutes per pair, not individual speaking time with feedback. No parent-side evidence that the format beats ₹0-399 AI. The calculation is on paper only. |

Execution side
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v2.md#C07, #C09, #C10, #C06, "Calculations", "Constraint check"; diff-v2.md D3, D4 | Conservative start-up is ₹62,000 against the ₹40,000 limit, and capital to first revenue is ₹76,600 against ₹75,000 (HARD K1). The ₹49,000 total in D3 is the base case on a 3-month deposit that no Satara listing supports. The only rent listings found are ₹25,000 for 750 sq ft and ₹22,000 for 800 sq ft, far above the founder's ₹4,000-6,000, and the economics' own rent sensitivity gives about ₹95,000. No room quote near a named school; every cost input is ASSUMPTION. Hours: 11 steady and 12 in launch weeks, zero slack. |
| KE2 | NOT MET | economics-v2.md#C17-C19, "Student path"; diff-v2.md D5; C07 | A dated plan now exists (first paid batch 2026-11-30, pre-sale gate 2026-11-02). The conservative path gives 5.4 paying students in the first revenue month against the 10 needed. With the pool cut to class 8-10 (180 parents), 10 students needs 5.6% conversion, not the 3.3% the criterion assumed. Every conversion rate is ASSUMPTION; D5 found no benchmark. Conservative first revenue sits at exactly 2.0 months with Diwali inside the window. |
| KE3 | NOT MET | economics-v2.md "Scenarios", "Calculations", "Verdict inputs"; simulation-v2.md | Conservative (₹600) break-even is 14 students against the 12 limit. The student path reaches only 10.5 by month 12. Monthly cash is negative in all 12 months, and cumulative cash is -₹106,656. The simulation shows 0.0% viable and 17.6% within capital. The economics still do not run the locked stress (20% churn; no enrolment around Diwali and May): they use 8% churn and omit dips, and they say the real path is slower. The ₹800 case has no school-age price source. At ₹600, 30 students gives 30 x 560 - 7,300 = ₹9,500 before CAC, under the ₹10,000 test. |
| KE4 | NOT MET | C07, C08; diff-v2.md D6; 01-local-market.md#C33-C38 | (a) Done: no final Act as of 2026-10-21; comments closed 2026-09-04. (b) Class 8-10 is about 60% of the band (ASSUMPTION), below the 80% bar, and no parental-consent route is confirmed. (c) Batches are 20, but whether 25 counts per batch or per centre is unresolved; registration (₹10,000, an ASSUMPTION) is not timed. (d) Shops and Establishments and GST rest on secondary snippets; DPDP is not costed. (e) Founder employment status is unconfirmed (offline). Under the strict reading no compliant plan covering 80% of the band is shown. |
| KE5 | NOT MET | diff-v2.md D7; economics-v2.md "Verdict inputs"; C09 | A written response plan exists, but it is reasoned guesses with no evidence ("response plan itself NONE"). Group-admin permission is 0 of 3 required (offline-only gap). The 40% sensitivity gives break-even only at the unsourced ₹800 price and 17.5 students. At the contract price of ₹600 the model is already below break-even, so a 40% shortfall fails by construction. |

## Market flaws
### FM1 — FIXABLE
- flaw: The speaking-gap differentiator rests on founder hearsay. There are 0 public Satara complaints, 0 verified batch sizes, and the peer-town benchmark shows no under-supply.
- evidence: [C10] The builders report 0 public complaints against a target of 5 [source: diff-v2.md D11]. [C11] No Google/Justdial review of any Satara spoken-English provider was found [source: 01-local-market.md#C46].
- what would fix it (FIXABLE only): at least 10 dated, named parent statements of willingness to pay ₹600 or more for a batch of 25 or fewer with a speaking promise (FOUNDER-COUNTED; offline-only), or 5 public Satara complaints (desk research unlikely). It cannot reach MET.
- fix would change customer/problem/revenue model: no

### FM2 — FIXABLE
- flaw: The Satara class 6-10 base is unmeasured, and the builders narrowed the customer to class 8-10 (about 60% by an equal-cohort ASSUMPTION). Class 10 leaves the market during the SSC exams (15 Feb to 11 Mar 2027). PhysicsWallah sells Foundation classes 8-10 locally.
- evidence: [C03] Only a district primary figure and one school were found [source: https://www.zpsatara.gov.in/?p=6821, via diff-v2.md D10]. [C12] PW Satara lists no English batch, so it is not a direct substitute today [source: https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044].
- what would fix it (FIXABLE only): school-level UDISE+ enrolment for Satara city schools, summed by class and medium. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: AI substitutes at ₹0-399 and the parent-visible value of the format are unproven. The pair-talk format gives students little teacher feedback, and the 10.5-minute result depends on an unobserved 60% factor.
- evidence: [C05] SpeakX ₹299 per month [source: https://www.business-admin.speakx.com/refund-policy]. [C06] ChatGPT Go ₹399 per month [source: https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html].
- what would fix it (FIXABLE only): at least 10 paid pre-enrolments after a demo class (offline-only). The calculation itself is desk work and is done.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: The ₹800 base price is unsupported by any school-age spoken-English price in Satara or a comparable town. The only Satara price is Success at ₹2,000 (target students not stated, course length 1-4 months). The ₹800 anchors are a different product (tuition per subject), hearsay, and a national online course at ₹1,300.
- evidence: [C02] Success ₹2,000 per month, target not stated [source: https://m.indiamart.com/success-satara]. [C13] Vallath online ₹1,300 per month (national) [source: https://vallath.in/program/speak-english-360online/].
- what would fix it (FIXABLE only): 2 or more published school-age spoken-English prices at ₹800 or more in Satara or a peer town, or at least 10 paid pre-enrolments at ₹800 (the pre-sale is offline-only). Desk research has found none so far.
- fix would change customer/problem/revenue model: no (see FE2)

## Execution flaws
### FE1 — FIXABLE
- flaw: The conservative case breaks HARD K1: ₹76,600 is needed before first revenue, and cumulative cash out is ₹106,656. K5 also breaks by ₹31,656 if the deposit is lost. Every setup input is ASSUMPTION. The only Satara rent listings are 5 to 8 times the founder's rent range.
- evidence: [C07] Capital to first revenue ₹76,600; month-12 cumulative -₹106,656 [source: economics-v2.md "Calculations"]. [C08] Radhika Road 750 sq ft shop ₹25,000 and Dahiwadi 800 sq ft ₹22,000; one deposit term found, on an industrial unit [source: https://www.realestateindia.com/satara-property/commercial-property-for-rent.htm]. [C14] The simulation has 17.6% of runs within the capital limit against a 90% bar [source: simulation-v2.md].
- what would fix it (FIXABLE only): two or more published Satara small-room listings near a school with rent of ₹6,000 or less and a deposit of 3 months or less, plus an itemised quote. Listings are partly obtainable by desk research; quotes are offline. A deposit change alone does not fix it, because economics-v2.md shows that all three changes (price, deposit, seats) are needed.
- fix would change customer/problem/revenue model: no

### FE2 — FATAL
- flaw: At the contract's stated price of ₹600, the conservative case has no break-even inside 12 months. Break-even needs 14 students, the path reaches 10.5, the founder's monthly cash is negative every month, and the 15-student asymptote would take about 81 months to recover the outlay. The only route the builders offer is a price of ₹800 or more, which has no school-age source and departs from the price in the contract ("₹600 per student per month"). The customer base was also cut to class 8-10 to fit the draft Act, and that cut lowers the reach that drives both the student path and break-even. If a judge treats ₹800 as an in-model price test, the flaw becomes an unverified price fixable only by an offline pre-sale, and the conservative case still has to pass under rule 3.
- evidence: [C07] [source: economics-v2.md "Calculations": break-even 14, path 10.48 at m12, cumulative -₹106,656]. [C15] 0.0% viable runs, P50 cumulative cash -₹96,627 [source: simulation-v2.md]. [C16] The economics' own conservative case still omits the locked stress (20% churn; Diwali and May dips) and says the real path is slower [source: economics-v2.md "Calculations"].
- what would fix it: none within the contract price. Under the assumption that ₹800 is allowed, 10 paid pre-enrolments at ₹800 (offline-only) plus a 3-month deposit and ₹8,000 seats would be needed, and even then month-12 cumulative cash is -₹68,216, which fits the cap only if every one of the three changes holds.
- fix would change customer/problem/revenue model: yes (at ₹800 the offer differs from the user's stated ₹600 and the customer is narrowed from classes 6-10 to 8-10; the main session's pivot check says NOT A PIVOT, and the judge should weigh that)

### FE3 — FIXABLE
- flaw: Legal status is unresolved against a low-risk, ₹75,000 cap. The draft Act is not in force, but under the strict reading the under-13 bar removes class 6-7 (the plan's own class 8-10 coverage is about 60%, under the 80% bar). Whether the 25-student line is per batch or per centre is unknown, and fines run from ₹1 lakh. The founder's employment status is unconfirmed, and the draft bars teachers at recognised schools.
- evidence: [C07] No final version as of 2026-10-21 (comments closed 2026-09-04) [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]. [C08] Under-13 enrolment bar, and the teacher-hiring bar, in the same draft [same source].
- what would fix it (FIXABLE only): the draft's full text or a gazette notice settling the 25-count basis and parental consent (desk research), and written confirmation of the founder's employment status (offline-only).
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: No evidenced incumbent defence. Success, the bus-stand class and PW can match ₹600 or form small batches; the response plan is reasoned guesses; the moat is "none yet".
- evidence: [C09] PW plans 75+ offline centres in FY27 (national) [source: https://www.storyboard18.com/brand-marketing/physicswallah-ups-marketing-spend-by-50-in-h1-fy26-as-offline-expansion-accelerates-85566.htm]. [C12] PW Satara lists no English batch today [source: https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044].
- what would fix it (FIXABLE only): a visit-based price and batch check of Success, Goranga, Job 4U, Shivtej and the bus-stand class (offline-only), plus a conservative model that holds break-even at 40% fewer students (not achieved at ₹600).
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Acquisition depends on the founder's 4 WhatsApp groups (240-480 members before overlap), with admin permission unobtained. Every conversion rate is ASSUMPTION, and reach and conversion are the two largest sensitivities. The simulation shows that reach would have to be 7.4 times the haircut value for 70% viability.
- evidence: [C15] Sensitivity ranks 1 and 2 are reach and conversion; required change x7.40 [source: simulation-v2.md "Sensitivity", "What would have to change"].
- what would fix it (FIXABLE only): written permission from 3 of 4 admins and a 7-day pre-sale of at least 10 paid sign-ups (both offline-only); a peer-town conversion benchmark by desk research (none found in round 2).
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Of the Satara spoken-English IndiaMART listings, only Goranga Education names school students (10th class), and no listing other than Success shows a fee, rating or batch size. [source: https://m.indiamart.com/city/satara/coaching-classes.html]
- [C02] Success (Satara): ₹2,000 per month, 8 years in business, target students not stated. [source: https://m.indiamart.com/success-satara]
- [C03] The only enrolment data found is a district primary figure (2,682 ZP schools, 114,789 students in classes 1-8, 2023-24), not the city and not classes 6-10. [source: https://www.zpsatara.gov.in/?p=6821]
- [C04] No closed Satara spoken-English operator was found. This is absence of evidence. [source: https://m.indiamart.com/city/satara/coaching-classes.html]
- [C05] SpeakX costs ₹299 per month with a strict no-refund policy. (national) [source: https://www.business-admin.speakx.com/refund-policy]
- [C06] ChatGPT Go launched in India at ₹399 per month. (national) [source: https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html]
- [C07] Conservative economics (₹600): capital to first revenue ₹76,600; break-even 14 students; month-12 path 10.48; cumulative -₹106,656. [source: economics-v2.md "Calculations"]
- [C08] Satara commercial listings: 750 sq ft shop on Radhika Road ₹25,000; 800 sq ft basement shop in Dahiwadi ₹22,000; the only deposit seen is 6 months on a Shirwal industrial unit. [source: https://www.realestateindia.com/satara-property/commercial-property-for-rent.htm]
- [C09] PhysicsWallah plans 75+ new offline centres in FY27. (national) [source: https://www.storyboard18.com/brand-marketing/physicswallah-ups-marketing-spend-by-50-in-h1-fy26-as-offline-expansion-accelerates-85566.htm]
- [C10] Draft Maharashtra coaching Act: not in force; under-13 enrolment bar; 25-student line; bar on hiring teachers at recognised schools; no final text as of 2026-10-21. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]
- [C11] PW Satara Vidyapeeth lists Foundation Maths and Science for classes 8-10 and no English batch. [source: https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044]
- [C12] Simulation v2: 0.0% viable, 17.6% within capital, P50 cumulative cash after month 12 -₹96,627; the money gate passes only on the unhaircut best case (34.2% against a 20% threshold). [source: simulation-v2.md]
- [C13] Vallath online English course: ₹1,300 per month (national, online). [source: https://vallath.in/program/speak-english-360online/]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | no | The ₹800 price has no school-age spoken-English source. The cited Success page shows ₹2,000 with no target, and Vallath is national and online. The builders concede this. Economics-v2 keeps ₹600 as the conservative case, which fails. |
| D2 | no | Arithmetic only, on an ASSUMPTION fixed cost of ₹8,400. No price evidence. Break-even at 11 depends on rent near ₹5,000, which the only listings contradict. |
| D3 | no | Every input is ASSUMPTION. The 3-month deposit is unsupported by any listing. The one deposit listing (industrial, 6 months) supports the adverse case. |
| D4 | no | Accepted as evidence of higher rent, not as a fix. It widens KE1 risk and still gives no small-room quote or deposit term. |
| D5 | no | The dated plan is accepted as a plan, but no permit, quote or conversion evidence supports it. The vendor case study is not a benchmark. The row does not cure the conservative 5.4-student shortfall. |
| D6 | no | The status check (a) is accepted as done, and the answer is "no final version". It fixes none of (b) 60% against 80%, (c), (d) or (e). |
| D7 | no | The plan is reasoned guesses. The PW page supports only "no English batch listed". At ₹600 the 40% sensitivity is below break-even. Admin permission is not obtained. |
| D8 | yes (calculation delivered only) | The format calculation is present and substitute prices are sourced. It does not establish individual speaking time or parent preference, so KM5 stays INSUFFICIENT EVIDENCE. |
| D9 | yes (KM4 survival half only) | Goranga's school-age listing and tenure add a verifiable survival case. The listing gives no price, rating or batch size, so KM1 is unchanged and the KM4 fee and batch check is still open. |
| D10 | no | Admitted not fixed. Desk research was available and was not completed. |
| D11 | no | Admitted not fixed. Offline-only gap. |
