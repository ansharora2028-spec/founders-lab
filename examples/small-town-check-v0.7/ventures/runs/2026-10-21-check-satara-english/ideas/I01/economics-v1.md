---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: economics-modeler
version: 1
created: 2026-10-21T10:19:35Z
---

## Inputs
All amounts in INR (contract currency). No currency conversion used. "Conservative / base / optimistic" values are given where they differ.

Price
- [C01] Founder price: ₹600 per student per month, paid by UPI or cash. Used as the conservative price. [FOUNDER-ESTIMATE: contract, "how they plan to charge"]
- [C02] Only visible Satara spoken-English price: Success, ₹2,000/month, 8 years in business (one data point, IndiaMART listing). [source: https://m.indiamart.com/success-satara]
- [C03] Local school-subject tuition ₹800-1,500 per subject per month, from the founder's own students (different product). [FOUNDER-COUNTED: own students, per 00-founder-knowledge.md Q9]
- [C04] Bus-stand spoken-English class about ₹1,000/month, batches of about 30. [FOUNDER-ESTIMATE: heard, Q10]
- [C05] Base price ₹800 and optimistic price ₹1,000 are not tested in Satara; they are anchored on C03 and C04. [ASSUMPTION: the base-case anchor is the low end of C03; a ₹600 vs ₹900 sign-up split is proposed in forge-v1.md and has not been run]

Costs
- [C06] Room rent ₹4,000-6,000/month for a small room near a school; no helper. Conservative ₹6,000, base ₹5,000, optimistic ₹4,000. [FOUNDER-ESTIMATE: heard, Q7]
- [C07] Security deposit: Maharashtra law sets no cap; the common range is 3-6 months, and leave-and-license deposits are often 2-3 months. The source is an unverified directional reference sheet, not Satara data. Conservative 6 months (₹36,000), base 3 months (₹15,000), optimistic 2 months (₹8,000). The deposit is refundable in principle. [source: https://wb.rentok.com/wp-content/uploads/2026/07/Security-Deposit-Rules-India-Reference-Sheet.pdf (search result, not opened); inference: Satara terms unknown, a Satara agent or the landlord must confirm] (national)
- [C08] Electricity, fan, internet: ₹800/month. Printing and supplies: ₹500/month conservative, ₹500 base, ₹500 optimistic. [ASSUMPTION: no local tariff checked; small room with a few hours of evening use]
- [C09] Fit-out: whiteboard ₹2,500 (conservative and base), ₹2,000 (optimistic); 20 seats (second-hand plastic chairs or benches) ₹12,000 conservative, ₹8,000 base, ₹5,000 optimistic. [ASSUMPTION: no local price quotes obtained]
- [C10] Registration and paperwork (shop-establishment, receipt books, fee sheet): ₹3,000 conservative and base, ₹2,000 optimistic. Whether registration is needed is unconfirmed. [ASSUMPTION: scout could not confirm the fee or the requirement; see 01-local-market.md C37]
- [C11] Launch marketing (printing, Instagram page set-up, consent forms, one-month boost): ₹3,000 conservative and base, ₹2,000 optimistic. [ASSUMPTION]
- [C12] Variable cost per student per month (worksheets, printing): ₹40 conservative, ₹30 base, ₹20 optimistic. [ASSUMPTION: about 8-20 printed sheets per student per month]
- [C13] UPI merchant charge ₹0 at ₹600-1,000 per payment (zero MDR up to ₹2,000, stated in forge-v1.md as effective 2026-10-15). I did not open this page. [source: https://www.moneylife.in/article/upi-charges-on-transactions-over-2000-from-15th-october-what-new-mdr-framework-means-for-consumers-and-merchants/81663.html, relayed from forge-v1.md C23] (national)
- [C14] The founder's own time is unpaid and is not costed in cash; it is limited by K2 (12 hours/week). Opportunity cost is not modelled. [ASSUMPTION: contract gives no wage alternative]

Demand and acquisition
- [C15] Parents the founder can reach personally in month 1: about 300 (4 WhatsApp groups of 60-120 members plus parents of past students). [FOUNDER-COUNTED: Q11, Q5]
- [C16] Reach after month 1: new parents reached per month, conservative 100, base 150, optimistic 300. [ASSUMPTION: no data on how many new parents the groups or referrals add after the first 300]
- [C17] Conversion from parent reached to paying student: conservative 3% in month 1 (9 students from 300) and 2% afterwards; base 6% and 4%; optimistic 10% and 7%. forge-v1.md assumes 8% sign-up x 40% demo-to-paid = 3.2% for the groups, and 10% x 50% = 5% for personal contacts. [ASSUMPTION: every rate; no local test done]
- [C18] Monthly churn: conservative 8%, base 6%, optimistic 4% (sim range 4-10%). forge-v1.md assumes 5-8% plus Diwali and summer slowdowns. [ASSUMPTION: C19 in forge-v1.md; founder says Diwali and summer are slow]
- [C19] Demo-to-paid: conservative 30% (3.3 demo seats per paid student), base 40%, optimistic 50%. Demo materials about ₹15 per demo attendee. [ASSUMPTION]
- [C20] Referral reward: one free week = price / 4. Conservative ₹150, base ₹200, optimistic ₹250. [ASSUMPTION: forge-v1.md proposes one free week]
- [C21] Paid Meta/Instagram ads, India: sources conflict by an order of magnitude. One guide gives education/coaching cost per lead of ₹200-600 on Meta and ₹500-1,500 on Google; CPC of ₹5-50 by vertical in another; ₹0.51-2.26 in a third. All are vendor blogs and none is Satara data. At a lead-to-paid rate of 10% [ASSUMPTION], ₹200-600 per lead means ₹2,000-6,000 per paid student, which is 4-11 months of margin at ₹560. I therefore do not model paid ads as a core channel; the Instagram row below is organic posting plus a ₹500/month boost. [source: https://megadigital.ai/en/blog/facebook-ad-cost-in-india/; https://upgrowth.in/facebook-advertising-pricing/; search results only, not opened] (national)
- [C22] Instagram row: ₹500 monthly boost spread over about 0.6 students/month (conservative) = ₹800 per student; base ₹400; optimistic ₹200. [ASSUMPTION: forge-v1.md assumes 1-3 students per month from Instagram and Maps]
- [C23] Capacity: a batch is capped at 20 (forge-v1.md, below the draft Act's 25-student line). Conservative path stays at or below 20 students, so one batch. [ASSUMPTION: forge-v1.md batch cap; draft Act status after 2026-09-08 unchecked, see 01-local-market.md C33-C36]

Time
- [C24] Founder weekly hours, conservative steady state: teaching 5 (one batch, 5 sessions of 1 hour), prep 2, marketing 1.5, travel 1.5, fee collection and WhatsApp 1 = 11. Launch weeks add 1 hour for two Saturday demos = 12. [ASSUMPTION: forge-v1.md leaves sessions per batch at 3-5; the conservative case uses 5]
- [C25] Time to first revenue: conservative 2.0 months (about 3 weeks to find a room, pay the deposit and equip it; demos in weeks 4-6; first fees in week 7-8), base 1.5, optimistic 1.0. Founder says Diwali is slow. [ASSUMPTION: forge-v1.md targets the first paid transaction in 3-4 weeks of the first WhatsApp post; room search time not sourced]

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
| blended CAC (cash, excludes founder time) | ₹186 (rounded to ₹190 in cash flow) | ₹136 | ₹117 |
| payback period (months) | CAC payback 0.33 months per student; cumulative cash not recovered by month 12 (about month 28 for the non-refundable outlay) | CAC payback 0.18; cumulative about month 9 (rough) | CAC payback 0.12; cumulative about month 3 (rough) |
| break-even volume | 14 students/month | 9 students | 6 students |
| capital to first revenue | ₹71,100 | ₹40,950 | ₹24,300 |
| months to first revenue | 2.0 | 1.5 | 1.0 |
| peak cumulative cash out (12 months) | about ₹79,000 | not run | not run |

Base and optimistic cumulative payback, and base/optimistic capital, are single-pass estimates and are not audited arithmetic. Only the conservative column counts toward the pass.

## Calculations
Conservative column.

Price and margin
- Price ₹600, variable cost ₹40. Contribution per student = 600 - 40 = ₹560. Gross margin = 560 / 600 = 93.3%. Rent is a fixed cost and is not in gross margin.
- Margin after fixed costs at 17 students (month 12): revenue 17 x 600 = ₹10,200; variable 17 x 40 = ₹680; fixed ₹7,300; remainder = ₹2,220, or 21.8% of revenue.

Fixed cost per month = rent 6,000 + electricity/internet 800 + supplies 500 = ₹7,300.

Setup cost = deposit 36,000 (6 x 6,000) + seats 12,000 + whiteboard 2,500 + registration 3,000 + launch marketing 3,000 = ₹56,500.

Capital to first revenue = setup 56,500 + 2 months x fixed 7,300 (14,600) = ₹71,100.

CAC by channel
- WhatsApp groups: 3.3 demo seats per paid student x ₹15 = ₹50, plus ₹10 consent and receipt paper = ₹60.
- Personal contacts: same demo path = ₹60.
- Referrals: free week ₹150 + demo materials ₹50 = ₹200.
- Instagram/Maps: ₹500 boost / 0.6 students = about ₹800.
- Month-3 mix (14 students): groups 4, personal 6, referrals 2, Instagram 2 gives weights 0.286, 0.429, 0.143, 0.143.
- Blended = 0.286 x 60 + 0.429 x 60 + 0.143 x 200 + 0.143 x 800 = 17.2 + 25.7 + 28.6 + 114.4 = ₹186. Cash flow below uses ₹190.
- CAC payback = 190 / 560 = 0.34 months.

Break-even volume
- N x 560 - 7,300 - (churn replacement) >= 0, with churn replacement = 8% x N x 190 = 15.2N. N x (560 - 15.2) = 7,300 gives N = 13.4, so 14 students. A single batch of 20 covers this.

Student path (conservative)
- Month 3 (first revenue month): 300 reached x 3% = 9 students.
- Each later month: previous x (1 - 0.08) + 100 reached x 2% = +2.
- Students: m3 9.0; m4 10.3; m5 11.5; m6 12.5; m7 13.5; m8 14.5; m9 15.3; m10 16.1; m11 16.8; m12 17.5.

Monthly cash (revenue - variable 40/student - fixed 7,300 - CAC 190 per new student)
| month | cash flow | cumulative |
|---|---|---|
| m1 | -56,500 - 7,300 = -63,800 | -63,800 |
| m2 | -7,300 | -71,100 |
| m3 | 5,400 - 360 - 7,300 - 1,710 (9 new) = -3,970 | -75,070 |
| m4 | 6,168 - 411 - 7,300 - 380 = -1,923 | -76,993 |
| m5 | 6,876 - 458 - 7,300 - 380 = -1,262 | -78,255 |
| m6 | 7,524 - 502 - 7,300 - 380 = -658 | -78,913 |
| m7 | 8,124 - 542 - 7,300 - 380 = -98 | -79,011 (peak) |
| m8 | 8,676 - 578 - 7,300 - 380 = +418 | -78,593 |
| m9 | +888 | -77,705 |
| m10 | +1,325 | -76,380 |
| m11 | +1,722 | -74,658 |
| m12 | +2,092 | -72,566 |

- Peak cash out = ₹79,011, which is ₹4,011 over K1 (₹75,000).
- Refundable deposit excluded: peak unrecovered outlay = 79,011 - 36,000 = ₹43,011; at month 12 = 72,566 - 36,000 = ₹36,566. At the month-12 run rate of ₹2,092/month that takes 36,566 / 2,092 = 17.5 more months (about month 30).
- Cash flow turns positive in month 8; this model does not include the Diwali, summer, or Feb-March exam-season dips (founder: Diwali and summer slow, Feb-March busy), so the real path is probably slower.

Hours (conservative): steady state 5 + 2 + 1.5 + 1.5 + 1 = 11; launch weeks 12. No slack.

Price sensitivity (one line, not the conservative case): at ₹800 and the same costs and student counts, contribution = 760 per student and break-even = 7,300 / 760 = 9.6, so 10 students.

## Simulation inputs
```json
{
  "currency": "INR", "months": 12, "break_even_by_month": 2,
  "capital_limit": 75000, "hours_limit_per_week": 12,
  "inputs": {
    "price": {"low": 600, "likely": 800, "high": 1000, "evidence": "founder-estimate"},
    "units_per_customer_per_month": {"low": 1, "likely": 1, "high": 1, "evidence": "assumption"},
    "variable_cost_per_unit": {"low": 20, "likely": 30, "high": 40, "evidence": "assumption"},
    "fixed_cost_per_month": {"low": 5300, "likely": 6300, "high": 7300, "evidence": "founder-estimate"},
    "setup_cost": {"low": 19000, "likely": 31500, "high": 56500, "evidence": "assumption"},
    "reach_per_month": {"low": 100, "likely": 150, "high": 300, "evidence": "assumption"},
    "conversion_rate": {"low": 0.02, "likely": 0.04, "high": 0.07, "evidence": "assumption"},
    "cac": {"low": 117, "likely": 136, "high": 186, "evidence": "assumption"},
    "monthly_churn": {"low": 0.04, "likely": 0.06, "high": 0.10, "evidence": "assumption"},
    "founder_hours_fixed_per_week": {"low": 7, "likely": 8.5, "high": 10, "evidence": "assumption"},
    "founder_hours_per_unit": {"low": 0.03, "likely": 0.05, "high": 0.07, "evidence": "assumption"}
  }
}
```
Note: low / likely / high are numerically ordered for every input, so for costs, CAC, churn and hours "high" is the bad end. The first 300 reached parents in month 1 (FOUNDER-COUNTED) are lower than reach_per_month "high"; later-month reach is an assumption, so the input is labelled assumption. The model treats `price` as founder-estimate because the ₹800-1,000 values are untested.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹75,000 HARD | peak cash out about ₹79,000 (₹4,011 over); capital to first revenue ₹71,100 alone fits | BREAKS |
| K2 | 12 hours/week HARD | 11 steady, 12 in launch weeks; no slack | fits |
| K3 | skills (have) HARD | teaching English/Marathi, B.Ed; no skill outside it needed | fits |
| K4 | skills (can learn) FLEXIBLE | basic Instagram only, as stated; no STRETCH USED | fits |
| K5 | cannot lose more than ₹75,000 HARD | unrecovered outlay at peak ₹43,011 if the ₹36,000 deposit is refunded; ₹79,011 if the deposit is lost | fits if deposit refunded; BREAKS by ₹4,011 if it is lost |
| K6 | first revenue within 2 months HARD | 2.0 months; no slack, and Diwali falls inside the window | fits (at the limit) |
| K7 | B2C only HARD | parents pay per student | fits |
| K8 | off-limits: none | none | fits |
| K9 | can rent a room near a school HARD | rent ₹6,000 + deposit ₹36,000 modelled | fits |

## Verdict inputs
- conservative unit economics positive: yes per student (contribution ₹560 against blended cash CAC about ₹190; monthly cash flow positive from month 8 at 14.5 students). The business does not recover its non-refundable outlay within 12 months, and the month-12 cumulative cash is about -₹72,600.
- HARD constraints broken in conservative case: K1 (peak cash out about ₹79,000 vs ₹75,000, driven by the 6-month deposit assumption); K5 only if the deposit is lost.
- FLEXIBLE stretches required: none.
- what would have to change for the conservative case to work: (1) peak cash out must fall by at least ₹4,011. A deposit of 5 months or less (₹30,000, saving ₹6,000) gives a peak of about ₹73,000; cutting seats from ₹12,000 to ₹8,000 saves ₹4,000 and is borderline (₹75,011). A pre-sale before renting the room would lower the risk further. (2) For the business to earn something worth 11-12 hours a week, price ₹600 yields only about ₹2,100/month at 17.5 students; at ₹800 the same 17.5 students give about ₹5,100/month (17.5 x 760 - 7,300 - CAC). The price test (₹600 vs ₹900) is the largest single lever, and the conservative case does not assume it works.
