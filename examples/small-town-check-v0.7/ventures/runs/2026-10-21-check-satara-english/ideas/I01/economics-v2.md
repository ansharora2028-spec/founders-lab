---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: economics-modeler
version: 2
created: 2026-10-21T10:33:29Z
---

## Inputs
All amounts in INR (contract currency). No currency conversion used. Round 2 changes from economics-v1: customer narrowed to class 8-10 (about 60% of the 6-10 band, per forge-v2.md), batch cap 20, the setup cost itemised as in forge-v2.md C31, the conservative price kept at ₹600 because ₹800 has no school-age price source. Two searches this round (Satara small-room rent and deposit terms; Satara class 8-10 English batch fees) returned no new price, rent or deposit data.

Price
- [C01] Conservative price ₹600 per student per month (the founder's original price and forge-v2's fallback test cell), base ₹800, optimistic ₹1,000. [FOUNDER-ESTIMATE: contract "how they plan to charge" for ₹600; ₹800 and ₹1,000 are ASSUMPTION, see C03]
- [C02] Only visible Satara spoken-English price: Success ₹2,000/month, 8 years in business; target students not stated, course length 1-4 months. [source: https://m.indiamart.com/success-satara]
- [C03] ₹800 and ₹1,000 have no school-age spoken-English price source. Anchors are the founder-counted ₹800-1,500 per subject per month for school tuition (a different product), the heard bus-stand class at about ₹1,000 (batches of about 30) and Vallath online ₹1,300 (national). [FOUNDER-COUNTED: own students, Q9; FOUNDER-ESTIMATE: heard, Q10; ASSUMPTION: the step from tuition to speaking batch] [source: https://vallath.in/program/speak-english-360online/] (national)
- [C04] Substitutes priced below ₹800: SpeakX ₹299/month, ChatGPT Go ₹399/month (both national, apps). [source: https://www.business-admin.speakx.com/refund-policy; https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html] (national)

Costs
- [C05] Room rent for a small room near a school: ₹4,000-6,000 per month. Conservative ₹6,000, base ₹5,000, optimistic ₹4,000. [FOUNDER-ESTIMATE: heard, Q7]
- [C06] Upward rent risk: Satara commercial listings are far higher than the founder's range (750 sq ft shop on Radhika Road ₹25,000, period not stated, about ₹33 per sq ft). A 250 sq ft room at that rate is about ₹8,300. This is a shop on a main road, not a room near a school, and the room size is a guess. It is used only as the "high" fixed-cost value in the simulation block and in the sensitivity line, not in the conservative column. [source: https://www.realestateindia.com/satara-property/commercial-property-for-rent.htm; via forge-v2.md C29; ASSUMPTION: 250 sq ft]
- [C07] Security deposit: no Satara room listing with a stated deposit was found (the one deposit seen is a 6-month industrial factory in Shirwal). Maharashtra sets no cap; the common range is 3-6 months. Conservative 6 months (₹36,000 at ₹6,000), base 3 months (₹15,000), optimistic 2 months (₹8,000). The deposit is refundable at the end of the lease, in principle. [source: https://wb.rentok.com/wp-content/uploads/2026/07/Security-Deposit-Rules-India-Reference-Sheet.pdf (search result, not opened; national); ASSUMPTION: Satara terms unknown]
- [C08] Electricity, fan, internet ₹800 per month; printing and supplies ₹500 per month (all three scenarios). [ASSUMPTION: no local tariff checked]
- [C09] Fit-out, conservative / base / optimistic: whiteboard ₹3,000 / ₹3,000 / ₹2,000; 20 seats and mats ₹12,000 / ₹8,000 / ₹5,000; printing, signage, receipts ₹2,000 / ₹2,000 / ₹1,500; teaching materials ₹3,000 / ₹3,000 / ₹2,000. Base matches forge-v2.md C31 (₹3,000 + ₹8,000 + ₹2,000 + ₹3,000). [ASSUMPTION: no local quotes]
- [C10] Registration and paperwork: conservative ₹3,000, base ₹0 (S&E intimation reported as no fee), optimistic ₹0. [source: https://calcguru.in/?p=1344 (secondary, search snippet, via forge-v2.md); ASSUMPTION: conservative ₹3,000 allowance for agent or notary help]
- [C11] Launch marketing (Instagram page, consent forms, one boost): conservative ₹3,000, base ₹3,000, optimistic ₹2,000. [ASSUMPTION]
- [C12] Draft Maharashtra coaching Act registration: fee not found; forge-v2.md budgets ₹10,000. Not in force (draft 2026-08-20). It applies above 25 students and the conservative path stays at or below 20 students, so it is excluded from the conservative column and shown as a sensitivity. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/; ASSUMPTION: ₹10,000; whether 25 counts per batch or per centre is not stated in the sources]
- [C13] Variable cost per student per month (worksheets, printing): conservative ₹40, base ₹30, optimistic ₹20. [ASSUMPTION]
- [C14] UPI merchant charge ₹0 at payments up to ₹2,000 from 2026-10-15. I did not open this page. [source: https://www.moneylife.in/article/upi-charges-on-transactions-over-2000-from-15th-october-what-new-mdr-framework-means-for-consumers-and-merchants/81663.html, relayed from forge-v2.md C23] (national)
- [C15] Founder time is unpaid and not costed in cash; no wage alternative is in the contract. [ASSUMPTION]

Demand and acquisition
- [C16] Parents the founder can reach in month 1: about 300 (4 WhatsApp groups of 60-120 plus parents of past students). [FOUNDER-COUNTED: Q11, Q5]
- [C17] Class 8-10 share of those parents: 60% (3 of 5 classes), so about 180 eligible in month 1. Classes 6-7 are excluded because of the draft under-13 bar. [ASSUMPTION: equal enrolment per class, forge-v2.md]
- [C18] Eligible parents reached per month after month 1: conservative 60, base 90, optimistic 180 (100 / 150 / 300 total parents x 60%). [ASSUMPTION: no data on how many new parents groups and referrals add]
- [C19] Parent-reached to paying-student conversion: conservative 3% in month 1 and 2% afterwards; base 6% and 4%; optimistic 10% and 7%. forge-v2.md assumes 8% sign-up x 40% demo-to-paid for groups and 10% x 50% for personal contacts. No independent benchmark was found. [ASSUMPTION: every rate]
- [C20] Monthly churn: conservative 8%, base 6%, optimistic 4%; sim range 4-10%. [ASSUMPTION: founder says Diwali and summer are slow]
- [C21] Demo-to-paid: conservative 30% (3.3 demo seats per paid student at about ₹15 each), base 40%, optimistic 50%. [ASSUMPTION]
- [C22] Referral reward of one free week = price / 4: conservative ₹150, base ₹200, optimistic ₹250. [ASSUMPTION: forge-v2.md]
- [C23] Paid Meta/Instagram ads: vendor blogs conflict by an order of magnitude (education cost per lead ₹200-600 on Meta in one; CPC ₹0.51-2.26 in another). None is Satara data. At 10% lead-to-paid [ASSUMPTION] paid ads cost ₹2,000-6,000 per student, so they are not a modelled channel; the Instagram row is organic plus a ₹500 monthly boost. [source: https://megadigital.ai/en/blog/facebook-ad-cost-in-india/; https://upgrowth.in/facebook-advertising-pricing/; search results only, not opened] (national)
- [C24] Instagram row: ₹500 boost over about 0.6 students per month = ₹800 per student conservative; ₹400 base; ₹200 optimistic. [ASSUMPTION]
- [C25] Capacity: batch cap 20 (forge-v2.md); the conservative path stays under 20 students, so one batch. [ASSUMPTION: forge-v2.md]

Time
- [C26] Founder hours per week, conservative steady state: teaching 5 (one batch, 5 sessions), prep 2, marketing 1.5, travel 1.5, fees and WhatsApp 1 = 11; launch weeks 12. [ASSUMPTION: forge-v2.md leaves sessions at 3-5]
- [C27] Months to first revenue: conservative 2.0 (room, deposit and fit-out slip; Diwali 2026-11-08 inside the window), base 1.5, optimistic 1.0. forge-v2.md's dated plan targets the first paid batch on 2026-11-30, about 1.3 months from today, which sits between base and optimistic; none of its dates has a source. [ASSUMPTION: plan dates are not commitments; Diwali date: https://www.smartpuja.com/blog/diwali-2026-date-lakshmi-puja-muhurat-vidhi/ via forge-v2.md]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹600/student/month | ₹800 | ₹1,000 |
| COGS per unit | ₹40 | ₹30 | ₹20 |
| gross margin % (before rent) | 93.3% | 96.3% | 98.0% |
| CAC: WhatsApp parent groups | ₹60 | ₹45 | ₹30 |
| CAC: personal contacts / past students' parents | ₹60 | ₹45 | ₹30 |
| CAC: referrals (free week) | ₹200 | ₹235 | ₹275 |
| CAC: Instagram page + Google Maps (organic + ₹500/mo boost) | ₹800 | ₹400 | ₹200 |
| CAC: school teacher / principal tie-ins | not modelled (no evidence) | not modelled | not modelled |
| blended CAC (cash, excludes founder time) | ₹186 (₹190 used in cash flow) | ₹136 | ₹117 |
| payback period (months) | CAC payback 0.34 months per student; cumulative cash not recovered in 12 months (month-12 cumulative -₹106,656; about -₹70,700 excluding the refundable deposit); at the 15-student asymptote it would take over 5 years | CAC payback 0.18; whole outlay recovered about month 8 (single pass) | CAC payback 0.12; about month 4 (single pass) |
| break-even volume | 14 students/month (path reaches 10.5 by month 12) | 9 students | 6 students |
| capital to first revenue | ₹76,600 | ₹40,450 | ₹25,800 |
| months to first revenue | 2.0 | 1.5 | 1.0 |
| peak cumulative cash out (12 months) | ₹106,656 (still the lowest point at month 12) | about ₹37,300 | about ₹25,800 |

Base and optimistic columns are single-pass estimates, not audited arithmetic. Only the conservative column counts toward the pass.

## Calculations
Conservative column.

Price and margin
- Price ₹600, variable ₹40. Contribution = 600 - 40 = ₹560. Gross margin = 560 / 600 = 93.3%. Rent is fixed and is outside gross margin.

Fixed cost per month = rent 6,000 + electricity/internet 800 + supplies 500 = ₹7,300.

Setup cost = deposit 36,000 (6 x 6,000) + whiteboard 3,000 + seats 12,000 + printing/signage/receipts 2,000 + materials 3,000 + paperwork 3,000 + launch marketing 3,000 = ₹62,000.

Capital to first revenue = setup 62,000 + 2 months x 7,300 (14,600) = ₹76,600. This is ₹1,600 over K1 before any student has paid.

CAC by channel (unchanged from economics-v1; the price is the same ₹600)
- Groups: 3.3 demo seats x ₹15 = ₹50 + ₹10 consent/receipt paper = ₹60. Personal contacts: ₹60. Referrals: ₹150 + ₹50 = ₹200. Instagram/Maps: 500 / 0.6 = about ₹800.
- Weights at 14 students (groups 4, personal 6, referrals 2, Instagram 2) = 0.286, 0.429, 0.143, 0.143. Blended = 17.2 + 25.7 + 28.6 + 114.4 = ₹186; ₹190 used. CAC payback = 190 / 560 = 0.34 months.

Break-even volume
- N x 560 - 7,300 - (8% churn x N x 190 = 15.2N) = 0, so N = 7,300 / 544.8 = 13.4, rounded up to 14 students. One batch of 20 covers it.

Student path (conservative, class 8-10 only)
- Month 3 (first revenue month): 300 x 60% = 180 eligible x 3% = 5.4 students.
- Each later month: previous x 0.92 + 60 eligible x 2% (1.2 new).
- m3 5.4; m4 6.17; m5 6.88; m6 7.53; m7 8.13; m8 8.68; m9 9.18; m10 9.65; m11 10.08; m12 10.48. Asymptote = 1.2 / 0.08 = 15 students.
- The path never reaches the 14-student break-even inside 12 months. This is lower than economics-v1 (17.5 at month 12) because the eligible reach is now 60% of v1's.

Monthly cash = revenue (students x 600) - variable (students x 40) - fixed 7,300 - CAC (new students x 190)
| month | cash flow | cumulative |
|---|---|---|
| m1 | -62,000 - 7,300 = -69,300 | -69,300 |
| m2 | -7,300 | -76,600 |
| m3 | 3,240 - 216 - 7,300 - 1,026 (5.4 new) = -5,302 | -81,902 |
| m4 | 3,702 - 247 - 7,300 - 228 = -4,073 | -85,975 |
| m5 | 4,128 - 275 - 7,300 - 228 = -3,675 | -89,650 |
| m6 | 4,518 - 301 - 7,300 - 228 = -3,311 | -92,961 |
| m7 | 4,878 - 325 - 7,300 - 228 = -2,975 | -95,936 |
| m8 | 5,208 - 347 - 7,300 - 228 = -2,667 | -98,603 |
| m9 | 5,508 - 367 - 7,300 - 228 = -2,387 | -100,990 |
| m10 | 5,790 - 386 - 7,300 - 228 = -2,124 | -103,114 |
| m11 | 6,048 - 403 - 7,300 - 228 = -1,883 | -104,997 |
| m12 | 6,288 - 419 - 7,300 - 228 = -1,659 | -106,656 |

- Month-12 cumulative excluding the refundable deposit: -106,656 + 36,000 = -70,656. At the asymptote (15 students) monthly cash = 15 x 560 - 7,300 - 1.2 x 190 = +872, so recovering 70,656 would take about 81 months.
- The model omits Diwali, summer and exam-season dips, so the real path is slower or equal.

Hours (conservative): 5 + 2 + 1.5 + 1.5 + 1 = 11 steady, 12 in launch weeks.

Sensitivities (not the conservative case)
- Rent at ₹8,300 (C06), 6-month deposit: fixed rises by 2,300 to 9,600; deposit rises by 13,800; capital to first revenue = 76,600 + 13,800 + 2 x 2,300 = ₹95,000. Break-even at ₹600 = 9,600 / 544.8 = 17.6, so 18 students.
- What fixes K1 on the conservative student path: price ₹800 instead of ₹600 adds 200 x 82.2 student-months (m3-m12) = +16,440; deposit 3 months instead of 6 saves 18,000; seats ₹8,000 instead of ₹12,000 saves 4,000. Combined m12 cumulative = -106,656 + 16,440 + 18,000 + 4,000 = -68,216, which is under ₹75,000. The tightest point is m11 at about -68,650 (m12 cash is +437 at ₹800).
- At ₹800 and the conservative fixed cost 7,300: contribution 760 - 15.2 churn = 744.8; break-even = 9.8, so 10 students.
- Draft Act registration ₹10,000 (C12) would add to setup only if the Act is in force and the centre is in scope.

## Simulation inputs
```json
{
  "currency": "INR", "months": 12, "break_even_by_month": 2,
  "capital_limit": 75000, "hours_limit_per_week": 12,
  "inputs": {
    "price": {"low": 600, "likely": 800, "high": 1000, "evidence": "assumption"},
    "units_per_customer_per_month": {"low": 1, "likely": 1, "high": 1, "evidence": "assumption"},
    "variable_cost_per_unit": {"low": 20, "likely": 30, "high": 40, "evidence": "assumption"},
    "fixed_cost_per_month": {"low": 5300, "likely": 6300, "high": 9600, "evidence": "assumption"},
    "setup_cost": {"low": 20500, "likely": 31000, "high": 62000, "evidence": "assumption"},
    "reach_per_month": {"low": 60, "likely": 90, "high": 180, "evidence": "assumption"},
    "conversion_rate": {"low": 0.02, "likely": 0.04, "high": 0.07, "evidence": "assumption"},
    "cac": {"low": 117, "likely": 136, "high": 190, "evidence": "assumption"},
    "monthly_churn": {"low": 0.04, "likely": 0.06, "high": 0.10, "evidence": "assumption"},
    "founder_hours_fixed_per_week": {"low": 7, "likely": 8.5, "high": 10, "evidence": "assumption"},
    "founder_hours_per_unit": {"low": 0.03, "likely": 0.05, "high": 0.07, "evidence": "assumption"}
  }
}
```
Notes: low / likely / high are numerically ordered for every input, so for costs, CAC, churn and hours "high" is the bad end, and for price, reach and conversion "low" is the bad end. Price is labelled assumption (not founder-estimate as in v1) because ₹800 and ₹1,000 have no school-age source (C03). The fixed-cost high of ₹9,600 uses the listing-implied rent of C06; the setup high of ₹62,000 is the conservative column (6-month deposit at ₹6,000) and does not include a 6-month deposit at ₹8,300 (about ₹75,800). Reach is the class 8-10 eligible share (C17); the first 300 parents are founder-counted but the later-month reach is not.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹75,000 HARD | ₹76,600 needed before first revenue (₹1,600 over); cumulative cash out ₹106,656 at month 12 | BREAKS |
| K2 | 12 hours/week HARD | 11 steady, 12 in launch weeks; no slack | fits |
| K3 | skills (have) HARD | English and Marathi teaching, B.Ed; nothing outside it | fits |
| K4 | skills (can learn) FLEXIBLE | basic Instagram only, as stated; no stretch used | fits |
| K5 | cannot lose more than ₹75,000 HARD | month-12 unrecovered ₹70,656 if the ₹36,000 deposit is refunded (and still falling about ₹1,700 per month at month 12); ₹106,656 if the deposit is lost | fits only if the deposit is returned; BREAKS by ₹31,656 if lost |
| K6 | first revenue within 2 months HARD | 2.0 months; no slack, Diwali 2026-11-08 inside the window (forge-v2.md plan targets about 1.3 months) | fits (at the limit) |
| K7 | B2C only HARD | parents pay per student | fits |
| K8 | off-limits: none | none | fits |
| K9 | can rent a room near a school HARD | rent ₹6,000 and deposit ₹36,000 modelled; listing-implied rent could be ₹8,300 | fits (rent risk upward) |

## Verdict inputs
- conservative unit economics positive: no. Contribution per student is positive (₹560 against CAC about ₹190), but at ₹600 the student path reaches 10.5 at month 12 against a 14-student break-even, so monthly cash is negative in all 12 months (month 12: -₹1,659) and cumulative cash is -₹106,656.
- HARD constraints broken in conservative case: K1 (₹76,600 before first revenue, ₹106,656 cumulative at month 12); K5 if the deposit is not returned (₹106,656 vs ₹75,000).
- FLEXIBLE stretches required: none.
- what would have to change for the conservative case to work: (1) price must be ₹800 or more instead of ₹600 (+33%; untested, no school-age source) so that break-even falls from 14 to 10 students and the 10.5-student path covers cost by month 12; (2) the deposit must be 3 months or less instead of 6 (saves ₹18,000, and no Satara listing shows such terms) plus seats at ₹8,000 instead of ₹12,000 (saves ₹4,000). With all three together, month-12 cumulative cash is about -₹68,200, under ₹75,000. Any one alone is not enough: the 6-month deposit alone puts the first-revenue outlay at ₹76,600. If rent is nearer ₹8,300 than ₹6,000 (C06), the same fixes are not enough and capital to first revenue is about ₹95,000 at a 6-month deposit.
