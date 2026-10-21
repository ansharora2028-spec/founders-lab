---
run_id: 2026-10-16-check-spoken-english-satara
idea_id: I01
agent: prosecutor-execution
version: 1
created: 2026-10-16T09:12:26Z
---

## Inputs read
- 00-contract.md
- 00-founder-knowledge.md
- 01-local-market.md
- 02-signals.md
- ideas/I01/kill-criteria.md (LOCKED)
- ideas/I01/forge-v1.md
- ideas/I01/strategy-v1.md
- ideas/I01/economics-v1.md
- ideas/I01/simulation-v1.md
- (all paths under <scratch>/ventures/runs/2026-10-16-check-spoken-english-satara/)
- Own web research on 2026-10-16: the draft Act text as reported by SCC Online, and a status search.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C12, #C13, #C14, #C15, #C16; economics-v1.md Scenarios and Constraint check; simulation-v1.md; C03 below | The threshold is "setup plus deposit at most ₹25,000". The conservative column has setup ₹29,000 (including a ₹12,000 deposit), which is over. Cash to first revenue is ₹43,200, which fits ₹75,000. First revenue is at 2.0 months, with no slack against the 2026-12-16 date. Cumulative cash passes -₹75,000 in month 8 and reaches about -₹99,400 at month 12 in the economics' conservative case. At the criterion's own "about 10 students per batch" the 12-month cash would stay inside ₹75,000 (my arithmetic: ₹29,000 setup plus roughly ₹2,000 a month of loss). So the failure rests on the deposit/setup inputs and on the modeler's 2.5-student path. Every one of those inputs is ASSUMPTION or FOUNDER-ESTIMATE, so this is not a verified failure. It is NOT MET on the locked threshold, and it would flip with a cheaper venue and furniture. |
| KE2 | INSUFFICIENT EVIDENCE | C01, C02, C04 below; forge-v1.md#C14, #C15, #C28-#C30; economics-v1.md#C17 | Branch (a) is unproven: no opened text says whether spoken English is "academic coaching, tuition, instruction or guidance". Branch (b) does not hold as written: the conservative economics are negative even before class 6 and part of class 7 are removed, and the economics never model the under-13 exclusion. Whether the 25 count is per centre or per batch is unknown. The founder's current school employment is unconfirmed (forge-v1.md#C30 is an ASSUMPTION from the past tense). The draft is not in force (C03), so a launch today is not unlawful. The gap can be closed by desk research (official draft text) plus a founder statement (offline-only). |
| KE3 | NOT MET | economics-v1.md Scenarios (break-even 15 conservative, 10 base), economics-v1.md Calculations (15.5 with replacement CAC), economics-v1.md#C30; 01-local-market.md#C25 | The threshold is break-even at 12 students or fewer and at least 10 paying students by month 2, with price held at ₹600. Conservative break-even is 15 (16 with replacement CAC) and modelled students are about 2 at month 2. Base break-even of 10 passes, but only on a heard rent of ₹5,000. All competitor evidence (the ₹1,000 bus-stand class, batches of 30) is FOUNDER-ESTIMATE. No incumbent response was tested. This is the modeler's conservative column, not a verified fact. |
| KE4 | NOT MET | economics-v1.md Scenarios (month-12 profit about -₹5,700, cumulative about -₹99,400), economics-v1.md#C21; simulation-v1.md (P10 month-12 profit -₹2,704) | Part (a) fails: the conservative case never returns to positive monthly cash and passes -₹75,000. Seasonality is not modelled (economics-v1.md#C21; the haircut is a stand-in). Part (b) passes: the schedule is 7-8 hours a week against 12. Part (c) passes: churn is 15% in the conservative case. In the simulation, P50 month-12 profit is +₹766 and P90 is +₹5,097, so even the typical run has no break-even cushion. |
| KE5 | INSUFFICIENT EVIDENCE | 00-founder-knowledge.md Q5, Q11 (counted); forge-v1.md#C26; economics-v1.md#C18, #C23 | At 2-3% of 300 the funnel gives 6-9 sign-ups, so the shortfall is 1-4 students. The conservative paid-Instagram CAC is ₹1,500 (economics-v1.md Calculations), so the gap costs about ₹1,500-6,000, under ₹10,000. That part holds, but the conversion rate has no benchmark. Not shown: whether the 4 group admins allow promotion, whether any school rule or employment contract bars soliciting current or former students, and any pre-enrolment. This is an offline-only gap and nothing contradicts the idea. The economics' conservative reach of 90 is lower than the founder-counted 300 the criterion uses. |
| KM3 (comment, execution evidence only) | INSUFFICIENT EVIDENCE | C01, C02, C03 below | Execution view only. The draft is not in force and its scope over spoken English is unconfirmed, so (a) is open. Under (b), the forge wedge of class 8-10 assumes class 8 pupils are about 13 (forge-v1.md#C27, ASSUMPTION), and the enrolment figure sits with the market prosecutor. |

## Flaws
### FE1 — FIXABLE
- flaw: The conservative unit economics are negative. Fixed cost (room ₹6,000 plus ₹800) is carried by about 2.5 students. The economics report a 12-month cash position of about -₹99,400, and K5 breaks if the class runs past month 7. The simulation viable share is 2.6% (the bar is 70%), and cash stays inside ₹75,000 in 91.5% of runs, only just over the 90% bar. The venue is the swing input: with rent near ₹0-500, break-even falls to about 2 students (economics-v1.md Calculations). Two cautions. First, the 2.6% mostly reflects the schema mapping K6 to "break even by month 2", which almost no rented-room business can meet, so the 91.5% within-capital figure is the fairer execution number. Second, the conservative inputs (2% conversion, 20 new parents reached per month, 25% extra haircut on all inputs, including fixed cost) are all ASSUMPTION with no benchmark. The negative result is therefore only as strong as those guesses.
- evidence: [C05] Economics-v1 conservative column: fixed ₹6,800 a month, 2.5-2.7 steady students, month-12 profit about -₹5,700. [source: economics-v1.md Scenarios and Calculations] (this run)
- evidence: [C06] Simulation: viable share 2.6%, within capital 91.5%, P10 peak cash need ₹72,996, bar NOT MET. [source: simulation-v1.md] (this run)
- what would fix it: (1) a sourced, lawful venue at about ₹1,000 a month or less (home, a school-owned or community hall rented by the hour, outside school premises). This is partly desk-researchable and partly offline (a quote from a landlord or hall). (2) Paid pre-enrolment or a trial cohort of at least 8-10 parents before any rent or deposit is paid. This is offline-only. Either one would have to change the conservative inputs, with a URL or a counted offline quote.
- fix would change customer/problem/revenue model: no

### FE2 — FIXABLE
- flaw: The legal scope is unresolved and the penalty is out of proportion to K5. The draft Maharashtra coaching Act covers "academic coaching, tuition, instruction or guidance to more than 25 students for consideration", bars enrolment under 13, bars operating inside recognised schools, bars employing teachers who work in recognised schools, and fines start at ₹1 lakh. That is above the ₹75,000 K5 limit. No opened text says whether spoken English is covered, or whether the 25 count is per centre or per batch. Forge's "25 per batch, 3 batches" ceiling of 75 students, and the economics' optimistic 75 students, assume a per-batch reading, but the SCC text says only "more than 25 students". On the evidence, a single centre with 3 batches could cross 25. The draft is not in force, so there is no breach today. Final status after the 2026-09-15 deadline is unconfirmed (C03).
- evidence: [C01] The draft covers centres giving "academic coaching, tuition, instruction or guidance to more than 25 students for consideration". Non-academic activities such as sports, dance, theatre, painting and yoga are excluded. The article is silent on language and skill classes. It bars under-13 enrolment, operation inside recognised schools or colleges, and employment of teachers working in recognised schools. Space is 1 sq m per student, with fire certification, CCTV and separate toilets. Fines run ₹1 lakh to ₹5 lakh for minor violations and ₹10 lakh to ₹50 lakh for major ones. It was published 2026-08-20. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/, 2026-08-25] (state; draft)
- what would fix it: the official draft or notified text from the School Education and Sports Department or the gazette, showing the definition of "coaching", the count basis, and the in-force date. Or a written reply from the Satara education office. Desk research can obtain the text; a reply from the office is offline-only. A Shops and Establishments registration quote for a one-room class is also needed. The cost fits the KE1 budget (economics-v1.md#C15 gives ₹200 to ₹5,000, with conflicting sources).
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: The founder's employment status is ambiguous, and it matters. The contract says she "taught at a private school for 2 years". Forge assumes this is past (forge-v1.md#C30, ASSUMPTION). If she still works at a recognised school, the draft's teacher bar and any school code of conduct on private tuition may apply. The economics' hours model (7-8 hours) also leaves out school duties. Soliciting parents of current students could breach the school's rules.
- evidence: [C07] The contract K3 and the founder-knowledge file give only "taught at a private school for 2 years". The employment status is not stated. [source: 00-contract.md K3; 00-founder-knowledge.md] (this run)
- what would fix it: the founder's statement of current employment and, if employed, the staff code or contract clause on tuition. Offline-only; no desk source.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: Distribution depends on a third party and on unmeasured conversion. The first 10 students come from 4 WhatsApp groups run by other admins. Group rules, school rules and admin permission are unknown. The 300 reachable parents overlap (the strategist cut to 90-200 for this). There is no search presence (01-local-market.md#C37) and Instagram skill is basic. Conversion of 2-8% has no benchmark anywhere in the files. If the groups ban promotion, the model has no stated second channel above ₹10,000.
- evidence: [C08] The channel strength table rates the WhatsApp groups "medium" on FOUNDER-COUNTED evidence only and Instagram "weak". [source: 01-local-market.md Distribution channels] (this run)
- what would fix it: admin consent or group rules (offline-only), and a paid pre-enrolment or trial result from at least a few parents. This is not obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Timing and K6 leave no slack, and the calendar hits the first term. First fee is at 2.0 months in the conservative case, with the K6 limit at 2 months (HARD) and a launch period that includes Diwali (the economics date it about 2026-11-08, from memory, [ASSUMPTION]). Class 10 practicals start 2027-01-28 and written exams run 2027-02-15 to 2027-03-11, which is months 3-5 of operation. The economics do not model that dip (economics-v1.md#C21). The K9 stretch ("only within K1") was ticked on first-revenue cash alone, while 12-month cash reaches -₹99,400. The unlock condition is met only if a stop-loss rule is written in, and none is.
- evidence: [C09] SSC class 10 written exams are tentatively 2027-02-15 to 2027-03-11, practicals 2027-01-28 to 2027-02-13. [source: https://news.careers360.com/maharashtra-board-exam-dates-2027-out-hsc-ssc-class-12th-10th-exams-february-march-msbshse-practicals-internal-assessments/amp] (state) (as cited in 01-local-market.md; not re-opened by me)
- what would fix it: a first-fee plan that starts with a paid trial cohort inside a free or already-held venue, so that revenue does not depend on signing a lease, and a written stop-loss rule (for example, stop at cumulative loss of ₹40,000). Desk research cannot supply this; it is a plan change.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: There is no moat, and the response of incumbents is untested. A tuition teacher can add a "speaking hour" at no cost. The bus-stand class can split batches. SpeakX plans to add Marathi (02-signals.md S05) and a free 10 Minute School course targets classes 6-10. The strategist rated the moat AGAINST (strategy-v1.md C7). The revenue ceiling is small: 25 students is ₹15,000 gross, about ₹7,000-10,000 net after rent. The cap is set by the Act's 25 threshold, not by hours, and the 12-hour limit does not bind (7-8 hours used).
- evidence: [C10] Strategist: moat AGAINST; the product is copyable in weeks; the base-case founder income is about ₹7,000-10,000 a month. [source: strategy-v1.md C7 and C2] (this run)
- what would fix it: Satara-specific evidence of how the bus-stand class and tuition teachers behave, and of paid retention for at least 3 months in a trial cohort. A visit or call by the founder (offline-only). The Satara fee data is not on the open web (Justdial returned 403 per 01-local-market.md).
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] The draft Maharashtra Private Coaching Centers (Registration and Regulation) Act, 2026: scope "academic coaching, tuition, instruction or guidance to more than 25 students for consideration"; under-13 bar; school-teacher bar; no operation in recognised schools; space, CCTV, fire and toilet rules; fines ₹1 lakh to ₹50 lakh. The page does not address language classes, per-batch counting or the in-force date. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/, 2026-08-25] (state; draft)
- [C02] Search on 2026-10-16: no report found that the Act was approved by the cabinet, tabled or passed; the consultation deadline was extended to 2026-09-15 after 11,410 suggestions and objections; coverage found stops in early September 2026; the Act would come into force on a date notified separately. The in-force wording comes from the search summary and I did not open that page. [source: https://www.freepressjournal.in/education/maharashtra-receives-over-11000-suggestions-on-draft-law-to-regulate-private-coaching-centres] (state)
- [C03] Because C02 shows no enactment, and a draft has no legal effect, the format is not unlawful on 2026-10-16. The risk is in the launch period and when the Act is notified. [ASSUMPTION: a draft bill has no force until notified; the notification date is unknown]
- [C04] The official draft text was not opened by me, and no agent in this run opened it. All scope statements rest on press summaries. [ASSUMPTION: press summaries may omit definitions]
- [C05] to [C10] are cited inside the flaws above.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
