---
run_id: 2026-10-16-check-spoken-english-satara
idea_id: I01
agent: economics-modeler
version: 1
created: 2026-10-16T09:08:44Z
---

## Inputs
All money in INR (₹). Unit = one student-month (one monthly fee from one enrolled student). Student cap and hours follow forge-v1 (3 evenings a week, batch of 25 or fewer).

Price
- [C01] Base price ₹600 per student per month. The user's stated price; no Satara order data confirms parents pay it. [ASSUMPTION: user-stated price from 00-contract.md, untested locally]
- [C02] Conservative price ₹500 effective: sibling discounts, first-month concessions and pauses. [ASSUMPTION: strategist's low case, 15-20% leakage on a new, unproven class]
- [C03] Optimistic price ₹800, anchored on tuition at ₹800-1,500 per subject per month. [ASSUMPTION: anchor is FOUNDER-COUNTED FK Q9; the step to a speaking class at that price is untested]
- [C04] Local reference prices: tuition ₹800-1,500 per subject [FOUNDER-COUNTED: FK Q9]; speaking class near the bus stand about ₹1,000, batches of 30 [FOUNDER-ESTIMATE: FK Q10]; Success, Satara ₹2,000 per month (seller listing, no orders or reviews) [source: https://m.indiamart.com/success-satara].

Variable cost (COGS) per student-month
- [C05] Payment fees: ₹0. UPI person-to-person is free; person-to-merchant payments of ₹2,000 or less carry zero MDR; a ₹500-800 fee is under that line. The 0.4% MDR applies only above ₹2,000. Search results gave an effective date of 2026-10-15 and one unverified headline about a deferral; neither changes the result at this ticket size. [source: https://www.cashfree.com/blog/upi-charges-new-mdr-rules/, 2026-10] [source: https://www.bajajbroking.in/share-market-news/upi-payments-above-rupee2000-to-attract-0-4percent-mdr-]
- [C06] Printed material: 10 pages per student per month at ₹2 per page = ₹20 conservative; ₹10 base; ₹5 optimistic. No page-rate source found. [ASSUMPTION: typical shop printout rate; unverified]
- [C07] No helper wage: the founder teaches alone. [FOUNDER-ESTIMATE: FK Q7 "no helper needed"]
- [C08] The founder's own time is not costed in cash. At the conservative case she earns about ₹0 for 7-8 hours a week. [ASSUMPTION: opportunity cost shown, not charged]

Fixed cost per month
- [C09] Room rent ₹4,000 / ₹5,000 / ₹6,000 (optimistic / base / conservative). [FOUNDER-ESTIMATE: FK Q7, heard]. No portal gave a usable rent for Satara (01-local-market.md#C18).
- [C10] Other monthly costs (electricity, fan/light, phone data, WhatsApp, cleaning): ₹800 conservative, ₹500 base, ₹300 optimistic. [ASSUMPTION: no source]
- [C11] Home or free venue (rent ₹0): used only in the optimistic case. [ASSUMPTION: forge-v1#C31, not researched; the draft Act's rule on premises is unresolved]

Setup cost (one-off, before month 1)
- [C12] Seating: 25 plastic chairs at ₹400 = ₹10,000 conservative; 15 at ₹350 = ₹5,250 base; floor mats ₹2,000 optimistic. [ASSUMPTION: no price source found]
- [C13] Whiteboard, markers, charts, attendance register: ₹3,000 conservative; ₹2,000 base; ₹1,500 optimistic. [ASSUMPTION]
- [C14] Rent deposit: 2 months' rent (₹12,000 conservative, ₹10,000 base, ₹0 optimistic). Refundable on exit, but cash is out. [ASSUMPTION: common Indian rental practice; landlord terms unknown]
- [C15] Registration and compliance paperwork: ₹3,000 conservative, ₹1,000 base, ₹0 optimistic. Fee sources conflict (₹200 to ₹5,000, depending on employee count; some say intimation only below 10 employees). [source: https://www.agileregulatory.com/blogs/maharashtra-shops-and-establishment-act-registration-process-documents-fees] [ASSUMPTION: amount]
- [C16] Launch printing (posters, trial handouts): ₹1,000 conservative, ₹500 base, ₹500 optimistic. [ASSUMPTION]
- [C17] Not in the model: the cost of meeting the draft Maharashtra Act (CCTV, separate toilets, fire and building certificates, 1 sq m per student) if it covers spoken English and the centre has more than 25 students; and fines of ₹1 lakh to ₹50 lakh. A single fine exceeds the ₹75,000 limit. Act status unconfirmed (state, draft). [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/, 2026-08-25]

Reach, conversion, churn
- [C18] Reach: 300 parents in month 1 (counted); 90 / 200 / 300 for month 1 and 20 / 50 / 100 for later months in the strategist's table. The simulator takes one constant monthly figure, so I use the average of months 1-3: 40 / 100 / 170. [FOUNDER-COUNTED: FK Q11 for the 300 ceiling; averaging and lower cuts are ASSUMPTION]
- [C19] Conversion reached to paid: 2% / 5% / 8%. [ASSUMPTION: no benchmark found; strategist-v1 C6 and forge-v1#C26]
- [C20] Monthly churn: 15% / 8% / 5%. Low-ticket after-school class; exam months worse. [ASSUMPTION: strategist-v1 C6]
- [C21] Seasonality (Jan-Mar class 10 exams from 2027-01-28; Diwali; summer) is not modelled in the scenario table. The simulation absorbs part of it through the unit haircut (see Simulation inputs). [FOUNDER-ESTIMATE: FK Q12]
- [C22] Student cap: 25 per centre in the conservative case (draft Act threshold), 75 (three batches) only if the Act counts per batch. The simulator has no hard cap; hours per unit stand in for it. [ASSUMPTION: forge-v1#C28, unresolved]

Acquisition cost (CAC) by channel
- [C23] Meta ad click cost in India: median Facebook CPC about US$0.11-0.20 in 2025-26 (vendor dataset; Instagram uses the same system). Rate US$1 = ₹90. Conservative CPC US$0.20 = ₹18; base US$0.13 = ₹12; optimistic US$0.11 = ₹10. [source: https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/india/traffic] (national; USD figures read from the search summary, not from an opened page) [ASSUMPTION: ₹90 per US$; no rate source opened]
- [C24] Paid-ad funnel: click to trial attendee 3% / 5% / 8%; trial attendee to paid 40% / 60% / 70%. [ASSUMPTION: no benchmark]
- [C25] WhatsApp groups: cash cost is a trial-evening handout and one message per parent; ₹50 / ₹25 / ₹15 per paid customer after trial dropouts. [ASSUMPTION]
- [C26] Referrals: a ₹100 / ₹50 / ₹0 discount to the referring parent per new family. [ASSUMPTION]
- [C27] Shop and tuition-centre notices: 20 posters at ₹10 = ₹200 per month, divided by 1 / 2 / 4 customers. [ASSUMPTION]
- [C28] Channel mix of paying customers. Conservative: WhatsApp 60%, referral 15%, notices 10%, paid Instagram 15% (groups saturate, so paid is needed). Base: 65 / 20 / 10 / 5. Optimistic: 70 / 20 / 5 / 5. [ASSUMPTION]
- [C29] The founder's time is the main acquisition cost and is not in CAC. Instagram skill is basic (K4). [00-contract.md K4]

Strategist data checked
- [C30] strategy-v1.md C6 reports "students in months 1-3: 6 (low)". Its own low inputs give 90 x 2% = 1.8 in month 1 and 20 x 2% = 0.4 in each of months 2-3, about 2.6 in total. I use the computed figure, not 6. [ASSUMPTION: re-derived from strategy-v1.md C6 inputs]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹500 | ₹600 | ₹800 |
| COGS per unit (student-month) | ₹20 | ₹10 | ₹5 |
| gross margin % | 96.0% | 98.3% | 99.4% |
| CAC: WhatsApp groups (per paid customer) | ₹50 | ₹25 | ₹15 |
| CAC: referrals | ₹100 | ₹50 | ₹0 |
| CAC: shop/tuition-centre notices | ₹200 | ₹100 | ₹50 |
| CAC: Instagram / paid ads | ₹1,500 | ₹400 | ₹180 |
| blended CAC | ₹290 | ₹56 | ₹23 |
| payback period (months) | never; per-customer CAC recovered in 0.6 months, but the business loses money every month | about 8 (about 10 with a 20% seasonal drop) | about 1 |
| break-even volume (students per month) | 15 | 10 | 1 (home venue); 6 with a ₹4,000 room |
| capital to first revenue | ₹43,200 | ₹24,800 | ₹4,900 |
| months to first revenue | 2.0 | 1.0 | 0.75 |
| steady students (month 12) | about 2.5 | about 22 | 75 if the Act counts per batch; 25 if per centre |
| monthly profit at month 12 (before founder pay) | about -₹5,700 | about +₹7,300 | about +₹40,000 at 75 students; about +₹19,500 at 25 |
| cumulative cash after 12 months | about -₹99,400 (about -₹87,400 if the deposit is refunded) | about +₹40,000 | positive |

Gross margin is on variable cost only. Rent is fixed and sits in break-even, not in COGS. Optimistic row uses the home venue (fixed ₹300, setup ₹4,000).

## Calculations
Conservative column.

Unit margin
- Price ₹500. COGS = 10 pages x ₹2 = ₹20 printing + ₹0 UPI fee = ₹20.
- Contribution per student-month = 500 - 20 = ₹480. Gross margin = 480 / 500 = 96.0%.

Blended CAC
- Instagram: CPC ₹18 / 3% click-to-trial = ₹600 per trial attendee. ₹600 / 40% trial-to-paid = ₹1,500 per paid customer.
- Blended = 0.60 x 50 + 0.15 x 100 + 0.10 x 200 + 0.15 x 1,500 = 30 + 15 + 20 + 225 = ₹290.
- Per-customer payback = 290 / 480 = 0.6 months. Expected life at 15% churn = 1 / 0.15 = 6.7 months, so lifetime contribution = 480 x 6.7 = ₹3,200, about 11 times CAC. Per-customer economics are positive; the business is not, because of fixed cost.

Fixed cost and break-even volume
- Fixed = ₹6,000 rent + ₹800 other = ₹6,800 per month.
- Break-even = 6,800 / 480 = 14.2, so 15 students. Counting CAC for replacement students at 15% churn (about 2.3 new per month x ₹290 = ₹660), the figure is 7,460 / 480 = 15.5, so 16.

Students reached (conservative funnel)
- Month 1: 90 x 2% = 1.8. Months 2 and later: 20 x 2% = 0.4 new.
- Month n = prior x 0.85 + 0.4. Values: 1.80, 1.93, 2.04, 2.13, 2.21, 2.28, 2.34, 2.39, 2.43, 2.47, 2.50, 2.52. Sum over 12 months = 27.0 student-months. Limit as n grows = 0.4 / 0.15 = 2.7.
- Needed for break-even: 15 students at 15% churn needs 15 x 0.15 = 2.25 new students per month, against 0.4 modelled: 5.6 times too few.

Twelve-month cash
- Revenue = 27.0 x 500 = ₹13,520.
- Variable cost = 27.0 x 20 = ₹540. CAC = 1.8 x 290 + 11 x 0.4 x 290 = 522 + 1,276 = ₹1,798. Fixed = 12 x 6,800 = ₹81,600.
- Operating result = 13,520 - 540 - 1,798 - 81,600 = -₹70,418.
- Setup = 10,000 + 3,000 + 12,000 + 3,000 + 1,000 = ₹29,000.
- Cumulative = -₹99,418 (-₹87,418 if the ₹12,000 deposit is returned).
- Average loss about ₹5,900 per month after setup, so cumulative cash passes -₹75,000 at (75,000 - 29,000) / 5,900 = month 7.8, that is, in month 8.

Capital to first revenue (conservative)
- Setup ₹29,000 + 2 months fixed 2 x 6,800 = ₹13,600 + month-1 CAC 1.8 x 290 = ₹522 (rounded to ₹600) = ₹43,200.
- Months to first revenue: week 1 room, Act check and printing; weeks 2-4 messages and trial evenings, with Diwali on or about 2026-11-08 [ASSUMPTION: festival date from memory, not sourced] slowing replies; first fees collected at the start of batch 1 around week 7. 2.0 months, at the K6 limit with no slack.

Conservative owner income
- Month-12 revenue 2.5 x 500 = ₹1,250 against ₹6,966 of cost. Founder earns nothing and loses about ₹5,700 a month.

What would turn the conservative case positive (each change alone)
- Rent: with ₹0 rent, fixed = ₹800, break-even = 800 / 480 = 1.7, so 2 students. The modelled 2.5-2.7 students then give about +₹150 to +₹300 a month. Rent must fall from ₹6,000 to about ₹0-500.
- Or new paying students: from 0.4 to about 2.3 per month (or reach x conversion from 20 x 2% to about 46 x 5%).
- Or price: at 2.7 students and ₹6,800 fixed, price would need to be above ₹2,500, which is not credible.

Base and optimistic columns use the same method with inputs C01-C28; they are not re-checked line by line here.

## Simulation inputs
Numeric low / high follow the simulator's convention (low <= likely <= high as numbers). For cost, churn and hours inputs the numerically high value is the bad case. The `evidence` tier is the weakest source for each input. `units_per_customer_per_month` is labelled assumption, so the script applies a 25% haircut (0.75 fees collected per student-month); this also stands in for missed months and seasonality. No hard student cap exists in the script: the high-end tail can exceed 25 students and is optimistic if the Act counts per centre.

```json
{
  "currency": "INR", "months": 12, "break_even_by_month": 2,
  "capital_limit": 75000, "hours_limit_per_week": 12,
  "inputs": {
    "price": {"low": 500, "likely": 600, "high": 800, "evidence": "assumption"},
    "units_per_customer_per_month": {"low": 1, "likely": 1, "high": 1, "evidence": "assumption"},
    "variable_cost_per_unit": {"low": 5, "likely": 10, "high": 20, "evidence": "assumption"},
    "fixed_cost_per_month": {"low": 300, "likely": 5500, "high": 6800, "evidence": "assumption"},
    "setup_cost": {"low": 4000, "likely": 19000, "high": 29000, "evidence": "assumption"},
    "reach_per_month": {"low": 40, "likely": 100, "high": 170, "evidence": "assumption"},
    "conversion_rate": {"low": 0.02, "likely": 0.05, "high": 0.08, "evidence": "assumption"},
    "cac": {"low": 20, "likely": 60, "high": 290, "evidence": "assumption"},
    "monthly_churn": {"low": 0.05, "likely": 0.08, "high": 0.15, "evidence": "assumption"},
    "founder_hours_fixed_per_week": {"low": 5, "likely": 6, "high": 7, "evidence": "assumption"},
    "founder_hours_per_unit": {"low": 0.25, "likely": 0.35, "high": 0.5, "evidence": "assumption"}
  }
}
```

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹75,000 HARD | ₹43,200 to first revenue; cumulative cash passes -₹75,000 in month 8 and reaches about -₹99,400 at month 12 if the class is run without a stop rule | fits to first revenue; BREAKS over 12 months |
| K2 | 12 hours per week HARD | 3 h teaching + about 1.5 h prep + 1 h admin + trial evenings in month 1 = about 7-8 h | fits |
| K3 | skills HARD | B.Ed, fluent English and Marathi, 2 years of teaching | fits (the draft Act's graduate-tutor rule is also met) |
| K4 | skills to learn FLEXIBLE | no Instagram learning required for the WhatsApp path; the 15% paid-Instagram share needs basic skill only | fits; no stretch used |
| K5 | risk: cannot lose more than ₹75,000 HARD | continuous loss of about ₹5,900 a month reaches ₹75,000 in month 8; a single Act fine (₹1 lakh minimum) would exceed it | BREAKS if run past month 7; fits if stopped by a stop-loss rule |
| K6 | first revenue within 2 months HARD | 2.0 months | fits, no slack |
| K7 | B2C only HARD | parents pay per child | fits |
| K8 | off-limits none | none | fits |
| K9 | rent a room, only within K1 FLEXIBLE | rent ₹6,000 plus ₹12,000 deposit | STRETCH USED: K9 — condition "only within K1" met because setup plus two months' fixed cost is ₹42,600 (₹43,200 with CAC), under ₹75,000 |

## Verdict inputs
- conservative unit economics positive: no. Per student the contribution is positive (₹480 against CAC ₹290), but at 2.5-2.7 students the class earns ₹1,250 a month against ₹6,966 of cost, a loss of about ₹5,700 a month with no break-even in 12 months.
- HARD constraints broken in conservative case: K5 (cumulative loss passes ₹75,000 in month 8 if not stopped); K1 over a 12-month horizon (about ₹99,400). K1 at first revenue fits.
- FLEXIBLE stretches required: K9 (room rental), condition met (see table).
- what would have to change for the conservative case to work: (1) rent from ₹6,000 to about ₹0-500 a month (home or free venue), which brings break-even to 2 students against 2.5-2.7 modelled; or (2) new paying students from about 0.4 to about 2.3 a month, a 5.6-times increase in reach x conversion (for example 46 parents reached a month at 5% instead of 20 at 2%). Price cannot fix it. Separately, the draft Maharashtra Act's scope over spoken English must be confirmed before any room is rented, since one fine exceeds K5.
