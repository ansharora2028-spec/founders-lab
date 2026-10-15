---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: economics-modeler
version: 1
created: 2026-10-15T09:30:21Z
---

## Inputs
Geography: no Pune-specific ad cost, payment, or demand data was found. All sourced cost inputs are national (India) and labeled so. Confidence in every demand/conversion input is low (01-local-market.md coverage 3/10; forge-v1 states Pune demand is unverified). Currency is INR; no conversion needed.

- [C01] Instagram ad cost in India 2026: CPM about ₹45–350, CPC ₹6–55. Other vendor blogs give narrower or conflicting ranges (₹0.45–3 and ₹2–6 CPC; ₹36.69–146.75 for "average sponsored ad" CPC). Vendor sources, no primary Meta data. Conservative uses the ₹55 high end of the first range. (national) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/, 2026-04]
- [C02] Razorpay domestic UPI/cards/netbanking fee is 2% plus 18% GST on the fee, i.e. 2.36% of transaction value. Vendor-published. (national) [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/]
- [C03] WhatsApp Business API utility template messages: estimates ₹0.115 to ₹0.35 per message, free inside an open 24-hour service window; GST 18% applies; BSP markups and platform fees are extra. Sources conflict. Conservative uses ₹0.35 per message. (national) [source: https://whautomate.com/whatsapp-business-api-pricing-india]
- [C04] Freelance graphic designer hourly rate in India: Payscale average about ₹293, middle 80% ₹79–808. Conservative uses ₹300/hour. (national) [source: https://www.payscale.com/research/IN/Job=Freelance_Graphic_Designer/Hourly_Rate]
- [C05] Virtual assistant (data entry) hourly rate in India: Payscale average about ₹225. Base uses ₹225/hour. (national) [source: https://www.payscale.com/research/IN/Job=Virtual_Assistant/Hourly_Rate/24aa8d85/Data-Entry]
- [C06] Indian freelancer-designer range quoted by Internshala is ₹300–2,000 per hour, which is above Payscale; shows conservative ₹300/hour may be low for a quality designer. (national) [source: https://internshala.com/blog/employer-cost-to-hire-graphic-designer/]
- [C07] Price ₹399 one-time kit (with ₹149 optional exit letter) is the forge's price. Conservative price is ₹299 and no upsell. [ASSUMPTION: free checklists and letter templates exist (forge-v1.md#C09 untested), so a pessimistic case assumes discounting to about 25% below list; no willingness-to-pay data exists]
- [C08] Fulfilment time per kit: 20 min conservative, 15 min base, 10 min optimistic (photo report formatting, letter in the right language, delivery). [ASSUMPTION: no benchmark; first-order manual workflow]
- [C09] LLM drafting cost per kit: ₹5 conservative, ₹3 base, ₹2 optimistic. [ASSUMPTION: forge-v1 notes LLM prices conflict; amounts are small relative to labour]
- [C10] Refund/chargeback rate: 5% conservative, 2% base, 1% optimistic; payment fee not recovered on refund. [ASSUMPTION: untested product with no operator acknowledgement (forge-v1.md#C10)]
- [C11] Fixed monthly costs: WhatsApp BSP platform fee ₹1,500 plus domain/form hosting ₹300 = ₹1,800 per month conservative (base ₹1,800, optimistic ₹1,750). [ASSUMPTION: BSP platform fees vary; C03 says they are extra]
- [C12] One-off costs conservative: no-code tooling and printing ₹5,000 (forge-v1 figure), lawyer review of templates ₹5,000, Shops and Establishments / Gumasta registration ₹3,000 = ₹13,000. Base the same. Optimistic ₹10,000. [ASSUMPTION: lawyer review and registration fees not researched; forge-v1.md#C11 flags legal-practice risk, so a review is included; 01-local-market.md#C20 says registration is unverified]
- [C13] One-offs amortised over 12 months for break-even: ₹13,000 / 12 = ₹1,083 per month (conservative). [ASSUMPTION: 12-month horizon is a convention]
- [C14] Founder time valued at ₹300/hour in acquisition cost (same as C04). [ASSUMPTION: opportunity-cost proxy; the founder has a full-time job]
- [C15] Channel reach and conversions: forge-v1 figures are the base case. Conservative applies: WhatsApp groups 3,000 reach x 0.3% (forge 1.5%); Instagram ad conversion 1% of clicks (forge 3%) at CPC ₹55; organic reels 20,000 views x 0.02% (forge 0.1%); referral 0.1 referrals per buyer (forge 0.5). Optimistic: groups 3%, ads CPC ₹6 and 3% conversion, reels 0.2%, referral 100 customers. [ASSUMPTION: no Pune funnel data; pessimistic values are 5x lower than the forge's, which are themselves unsourced (forge-v1 Path table)]
- [C16] Time to first revenue conservative: 3 weeks build, 3 weeks for WhatsApp group admin permissions and legal review, about 4 weeks to the first paid sale given 0.3% conversion and no June–August student intake = about 10 weeks (2.3 months). Base 6 weeks, optimistic 4 weeks. [ASSUMPTION: forge-v1.md#C13 states intake season is outside the window]
- [C17] Referral credit ₹50 per converting referred buyer (forge-v1 channel table). [ASSUMPTION: forge design]
- [C18] Pune rent in PGs ₹6,000–18,000, so deposit exposure is roughly ₹6,000–36,000 (deposit multiple is an ASSUMPTION). Not used in the numbers; context for price. [source: https://fn.mahacet.org/category-check/blog/cost-of-living-pune-international-students.html; inference: deposit multiple not in source]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹299 | ₹399 | ₹428.80 (₹399 plus 20% buying the ₹149 letter) |
| COGS per unit | ₹129.07 | ₹77.30 | ₹45.90 |
| gross margin % | 56.8% | 80.6% | 89.3% |
| CAC: WhatsApp/Telegram groups (time-loaded) | ₹400 (9.0 customers) | ₹80 (45) | ₹40 (90) |
| CAC: Instagram ads | ₹5,500 (2.7 customers) | ₹833 (18) | ₹200 (75) |
| CAC: Instagram organic reels (time-loaded) | ₹1,500 (4.0 customers) | ₹300 (20) | ₹150 (40) |
| CAC: referral / roommate sharing | ₹50 (1.6 customers) | ₹50 (20) | ₹50 (100) |
| blended CAC (time-loaded) | ₹1,426 (17.3 customers) | ₹249 (103) | ₹97 (305) |
| blended CAC (cash only, no founder time) | ₹872 | ₹155 | ₹61 |
| payback period (months) | never: gross profit per customer ₹170 vs CAC ₹1,426; one-time purchase, no repeat | under 1 month (CAC ₹249 vs gross profit ₹322 per customer; one-time purchase) | under 1 month |
| break-even volume | 17 customers/month before CAC; no volume breaks even after CAC at ₹1,426 | 9 customers/month before CAC | 7 customers/month before CAC |
| capital to first revenue | ₹17,800 | ₹16,800 | ₹12,500 |
| months to first revenue | 2.3 | 1.4 | 0.9 |

Base and optimistic capital to first revenue: one-offs + one month platform fee + ads test tranche of ₹2,000 (base) and ₹1,000 (optimistic) [ASSUMPTION].

## Calculations
Conservative column.

COGS per unit at price ₹299:
- Payment fee: 299 x 2.36% = ₹7.06 (C02).
- WhatsApp messages: 5 utility messages x ₹0.35 x 1.18 GST = ₹2.07 (C03).
- LLM drafting: ₹5.00 (C09).
- Fulfilment labour: 20 min = 1/3 hour x ₹300 = ₹100.00 (C08, C04).
- Refunds: 5% x ₹299 = ₹14.95 (C10).
- COGS = 7.06 + 2.07 + 5.00 + 100.00 + 14.95 = ₹129.08 (₹129.07 in the table from unrounded inputs).
- Gross profit per unit = 299 - 129.07 = ₹169.93. Gross margin = 169.93 / 299 = 56.8%.

Customers by channel (C15):
- Groups: 3,000 x 0.3% = 9.0. Cost: 12 hours (7.5 h approaching ~15 admins at 0.5 h each, 4.5 h posting) x ₹300 = ₹3,600. CAC = 3,600 / 9.0 = ₹400.
- Ads: ₹15,000 / CPC ₹55 = 272.7 clicks x 1% = 2.73 customers. CAC = 15,000 / 2.73 = ₹5,500.
- Reels: 20,000 x 0.02% = 4.0 customers. Cost: 8 reels x 2.5 h = 20 h x ₹300 = ₹6,000. CAC = 6,000 / 4.0 = ₹1,500.
- Referral: 0.1 x (9.0 + 2.73 + 4.0) = 1.57 customers x ₹50 credit = ₹78.65. CAC = ₹50.
- Total customers = 9.0 + 2.73 + 4.0 + 1.57 = 17.30 in the 3-month window.
- Total acquisition cost = 3,600 + 15,000 + 6,000 + 78.65 = ₹24,678.65. Blended CAC = 24,678.65 / 17.30 = ₹1,426.
- Cash-only: (15,000 + 78.65) / 17.30 = ₹872.

Contribution per customer after CAC = 169.93 - 1,426 = -₹1,256. Payback does not occur. The model has no repeat purchase in the conservative case (C07: no upsell).

Break-even volume (before CAC): monthly fixed = ₹1,800 (C11) + ₹1,083 (C13) = ₹2,883. 2,883 / 169.93 = 16.97, so 17 customers per month. Conservative expected volume is 17.3 customers over three months, about 5.8 per month, about one third of break-even before CAC.

Capital to first revenue: one-offs ₹13,000 (C12) + first month platform fee ₹1,800 (C11) + first ad tranche ₹3,000 (ASSUMPTION: one-fifth of the ₹15,000 test spent before first sale) = ₹17,800.

Total capital outlay over the 3-month window:
- one-offs ₹13,000 + platform fees 3 x ₹1,800 = ₹5,400 + ads ₹15,000 + referral credits ₹78.65 + variable COGS 17.30 x ₹129.07 = ₹2,233 = ₹35,712.
- Revenue 17.30 x ₹299 = ₹5,173 (refunds already in COGS).
- Net cash burn about ₹30,540. Founder time for groups and reels (₹9,600) is excluded from cash.

Hours (K2) conservative: build 30 h + legal coordination 5 h + groups 12 h + reels 20 h + ad management 12 weeks x 1 h = 12 h + customer support about 5 h = 84 h over 12 weeks, 7 h per week average. Fulfilment is hired (C04). Peak in build weeks: 30 h / 4 weeks = 7.5 h per week.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | about ₹35,700 outlay in 3 months; ₹17,800 to first revenue; net burn about ₹30,500 | fits |
| K2 | 10 hours per week HARD | about 7 h per week average, 7.5 h peak | fits |
| K3 | skills (have) HARD | social media marketing and languages used; legal-template drafting and no-code build are not listed skills and are covered by hiring (K4) | fits via K4 |
| K4 | skills can hire/learn, FLEXIBLE | freelancer fulfilment ₹100 per kit plus lawyer review ₹5,000 | fits; STRETCH USED: K4 — condition "only within the ₹1,00,000 capital limit (K1)" met because total conservative outlay including all freelancer spend is about ₹35,700, below ₹1,00,000 |
| K5 | risk: cannot lose more than ₹1,00,000 HARD | maximum financial loss about ₹36,000 (all outlay lost). Legal exposure from selling a demand-letter template and from any operator-reputation data is unresearched and not quantified (forge-v1.md#C11) | fits on capital; legal exposure unquantified |
| K6 | first revenue within 3 months HARD | 2.3 months; margin 0.7 months; a slip of 3 weeks in build or admin permission breaks it | fits (thin margin) |
| K7 | B2C only HARD | customer is an individual tenant paying by UPI | fits |
| K8 | off-limits categories HARD | not alcohol, gambling, crypto, MLM, food or medical | fits |
| K9 | keeps full-time job HARD | 7 h per week, fulfilment hired | fits |

## Verdict inputs
- conservative unit economics positive: no. Gross margin is positive (56.8%, ₹170 per kit) but blended CAC of ₹1,426 (cash-only ₹872) exceeds gross profit per customer by 5 to 8 times, payback never occurs, and the 3-month volume of about 17 customers is about one third of the 17-per-month break-even before CAC. Instagram ads at ₹5,500 per customer are 18 times the price.
- HARD constraints broken in conservative case: none (K6 fits by 0.7 months; K5 legal exposure unquantified)
- FLEXIBLE stretches required: K4 freelancer spend, unlock condition "only within the ₹1,00,000 capital limit (K1)" met (see Constraint check)
- note: every demand and conversion input is ASSUMPTION; sourced inputs are national ad, payment, messaging and labour costs only. The base and optimistic columns are for reference and do not count toward a PASS.
