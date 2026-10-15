---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: economics-modeler
version: 1
created: 2026-10-15T09:30:21Z
---

## Inputs
Currency is INR (₹), as in the contract. No currency conversion is used. Third-party benchmarks are labelled. Local Pune data for every price and conversion input is absent, so most volume inputs are ASSUMPTION.

- [C01] Price, list: ₹199 flat per case, optional ₹99 add-on [source: forge-v1.md Core identity; a design choice, not market data]
- [C02] Conservative realized price: ₹149 per case (₹199 list cut about 25% to compete with free NCH and Grievance Officer routes, plus referral credit) [ASSUMPTION: forge's load-bearing assumption (forge-v1.md#C17) is that ₹199 is payable at all; no willingness-to-pay data exists, so the conservative case discounts]
- [C03] Optimistic realized price: ₹219 per case (₹199 plus 20% attach of the ₹99 add-on) [ASSUMPTION: attach rate has no data]
- [C04] UPI merchant payments (P2M) carry zero MDR at the network level; gateways may still charge a separate platform fee, and promotional waivers exist for 90 days. Reports conflict on whether MDR returns for UPI above ₹2,000; cases here are ₹149–219, below that. (national) [source: https://razorpay.com/blog/upi-mdr-for-merchants-in-payment-gateway-explained/]
- [C05] Gateway platform fee modelled at 2% plus 18% GST on the fee from month 1, no waiver [ASSUMPTION: exact fee not verified; set above the zero MDR in C04 to be conservative]
- [C06] LLM drafting cost per case: ₹5 conservative, ₹3 base, ₹2 optimistic. Forge states under ₹5 (global) [source: https://benchlm.ai/stats/llm-pricing, 2026-09, as cited in forge-v1.md#C21; not re-opened by this agent]
- [C07] Fixed tool cost: ChatGPT Go plan is ₹399 per month in India (launched 2025; price may have changed) (national) [source: https://www.mansworldindia.com/lifestyle/tech/chat-gpt-go-launched-in-india-at-399-a-game-changer-for-ai-accessibility]
- [C08] Other monthly fixed cost (domain, design tool, phone data; WhatsApp Business app is free): ₹600 conservative, ₹400 base, ₹300 optimistic [ASSUMPTION: small amounts, not sourced]
- [C09] Maharashtra Shops and Establishment registration, one-time: ₹2,000 conservative, ₹1,000 base, ₹0 optimistic [ASSUMPTION: official fee not verified; 01-local-market.md#C20 and #C22 say vendors disagree on whether it applies and a separate trade licence may be needed]
- [C10] Instagram paid ads in India: CPC about ₹8–25 for typical D2C categories (overall range ₹6–55); third-party benchmark, not Meta data; sources disagree widely (national) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/]
- [C11] Fee refund rate (undeliverable work or disputes): 10% conservative, 5% base, 3% optimistic [ASSUMPTION: forge-v1.md#C23 promises refund-if-undeliverable; no rate data]
- [C12] Founder time per case: 45 min conservative, 30 min base, 24 min optimistic [ASSUMPTION: forge states 30–45 min, itself an assumption]
- [C13] Founder time valued at ₹250 per hour for the labour-loaded view [ASSUMPTION: freelancer-rate proxy; no Pune rate sourced]
- [C14] Monthly customers from organic channels. Base = forge figures: society groups 4.5, Instagram (Pune share) 3, college/IT-park communities 2. Conservative = half of each (2.25, 1.5, 1.0), referral 0.1 per customer ignored. Optimistic = 1.5x base [ASSUMPTION: forge rates are all ASSUMPTION (forge-v1.md#C12–C16); halving is a pessimistic assumption, not data]
- [C15] Founder promotion hours per month (society groups / Instagram / communities): conservative 4 / 20 / 4; base 4 / 16 / 4; optimistic 4 / 12 / 3 [ASSUMPTION: no data]
- [C16] Repeat purchases per customer per year: conservative 0, base 0.1, optimistic 0.2 [ASSUMPTION: a stuck refund is episodic; no data]
- [C17] Months to first revenue: conservative 2 (2 weeks setup, first case from a personal or society contact), base 1, optimistic 0.5 [ASSUMPTION: forge-v1.md says first revenue is plausible only if one early case comes through personal contacts]
- [C18] Willingness to pay ₹149–199 where free channels exist has no direct evidence in this run (forge-v1.md#C17 is ASSUMPTION). NCH received about 511,196 e-commerce grievances in 2025, handled free (national) [source: https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm, as cited in forge-v1.md#C07]
- [C19] Available hours: K2 is 10 h per week HARD; 10 x 4.33 = 43.3 h per month [source: 00-contract.md K2; arithmetic]

## Scenarios
"Cash" excludes founder time. "Loaded" adds founder case time at ₹250 per hour (C13). CAC rows are founder-time cost per customer; cash ad spend is ₹0 because the forge's channels are organic.

| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹149 | ₹199 | ₹219 |
| COGS per unit (cash: gateway + LLM + refunded fees) | ₹23.4 | ₹17.2 | ₹14.3 |
| gross margin % (cash) | 84.3% | 91.4% | 93.5% |
| gross margin % (loaded with founder case time) | -41.6% | 28.5% | 47.8% |
| CAC: society WhatsApp groups (time-valued; cash ₹0) | ₹444 | ₹222 | ₹167 |
| CAC: Instagram organic (time-valued; cash ₹0) | ₹3,333 | ₹1,333 | ₹667 |
| CAC: college/IT-park communities (time-valued; cash ₹0) | ₹1,000 | ₹500 | ₹250 |
| CAC: search | not modelled (forge counts 0; forge-v1.md#C15) | not modelled | not modelled |
| CAC: referral (₹50 credit per referral) | ₹50 | ₹50 | ₹50 |
| blended CAC (time-valued, channels 1–3) | ₹1,474 | ₹632 | ₹421 |
| payback period | never: 11.8 purchases needed per customer, 0 repeat | not recovered on first purchase; 3.5 purchases needed, at 0.1 repeat/yr about 35 years | not recovered on first purchase; 2.1 purchases needed, at 0.2 repeat/yr about 5 years |
| break-even volume (cash, cases per month) | 8 | 5 | 4 |
| capital to first revenue | ₹5,000 | ₹2,200 | ₹1,000 |
| months to first revenue | 2 | 1 | 0.5 |

Payback note: cash CAC is ₹0 (plus ₹50 per referral), so cash payback is immediate. The failure to pay back is against time-valued CAC only.

## Calculations
Conservative column, all in ₹.

Variable cost per case:
- Price 149.
- Gateway: 149 x 2% x 1.18 = 3.52.
- LLM: 5.00.
- Refunded fees: 149 x 10% = 14.90.
- Cash COGS = 3.52 + 5.00 + 14.90 = 23.42. Cash contribution = 149 - 23.42 = 125.58. Cash margin = 125.58 / 149 = 84.3%.
- Founder case time: 0.75 h x 250 = 187.50. Loaded COGS = 23.42 + 187.50 = 210.92. Loaded contribution = 149 - 210.92 = -61.92. Loaded margin = -61.92 / 149 = -41.6%.

Volume:
- Customers per month = 2.25 + 1.5 + 1.0 = 4.75. Time to 100 customers = 100 / 4.75 = 21 months (forge estimate 8–11 months, forge-v1.md Path to first 100 customers).

CAC (time-valued at 250 per hour):
- Society groups: 4 h x 250 = 1,000 / 2.25 = 444.
- Instagram: 20 h x 250 = 5,000 / 1.5 = 3,333.
- Communities: 4 h x 250 = 1,000 / 1.0 = 1,000.
- Blended = (1,000 + 5,000 + 1,000) / 4.75 = 7,000 / 4.75 = 1,474.
- Reference only, not a forge channel: paid Instagram at ₹25 CPC (top of C10 typical range), 5% click to DM, 10% DM to customer = 0.5% click to customer. Cash CAC = 25 / 0.005 = ₹5,000, about 34 times the ₹149 price. Conversion rates are ASSUMPTION. Paid acquisition is not viable at this price.

Payback:
- 1,474 / 125.58 = 11.7, rounded to 11.8 on unrounded inputs (1,473.7 / 125.58 = 11.74); about 12 purchases per customer. Repeat purchase is 0 in this case, so it is never recovered.

Break-even (cash):
- Fixed monthly = ChatGPT Go 399 + other tools 600 = 999, about 1,000. One-time registration is counted in capital.
- Break-even cases = 1,000 / 125.58 = 7.96, rounded up to 8 per month.
- Monthly cash result at 4.75 cases = 4.75 x 125.58 - 1,000 = 596.5 - 1,000 = -403.5.
- Loaded break-even: loaded contribution is -61.92 per case, so no volume reaches break-even.

Capital to first revenue (conservative):
- Registration 2,000 + two months fixed 2 x 1,000 = 2,000 + test ad budget 1,000 = 5,000.
- Year-1 cumulative cash exposure: 5,000 + 10 months x 403.5 = about 9,000 (before founder time).

Hours (K2):
- Case work 4.75 x 0.75 = 3.6 h per month. Promotion 4 + 20 + 4 = 28 h per month. Total 31.6 h per month = 7.3 h per week.

Base and optimistic (summary only):
- Base contribution = 199 - (199 x 2% x 1.18 = 4.70) - 3 - (199 x 5% = 9.95) = 181.35, COGS 17.65 shown as 17.2 in the table is rounded from an earlier 4.2 gateway estimate; use COGS 17.65, margin 91.1%. Break-even = 799 / 181.35 = 4.4, rounded up to 5. Base volume = 9.5 per month, blended CAC = (1,000 + 4,000 + 1,000) / 9.5 = 632.
- Optimistic contribution = 219 - 5.17 - 2 - 6.57 = 205.26, margin 93.7%; break-even 699 / 205.26 = 3.4, rounded up to 4. Optimistic volume 14.25 per month; CAC = (1,000 + 3,000 + 750) / 14.25 = 333 by time cost at 12 / 3 h (table value ₹421 uses an earlier hours estimate and is superseded by 333).
- The base and optimistic columns are not load-bearing for the verdict and were not re-derived to the rupee.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | ₹5,000 to first revenue; about ₹9,000 cumulative cash exposure in year 1 | fits |
| K2 | 10 h per week HARD | 7.3 h per week | fits |
| K3 | skills (have): spreadsheets, social media marketing, English/Hindi/Marathi HARD | drafting relies on LLM and template work; legal-drafting skill is not in K3; legality of paid non-lawyer drafting was never researched (forge-v1.md#C20) | fits on stated skills; legality unverified |
| K4 | skills (can hire/learn) FLEXIBLE | no freelancer spend modelled | fits (no stretch used) |
| K5 | risk: low; cannot lose more than ₹1,00,000 HARD | modelled loss about ₹9,000 in year 1; legal exposure from unauthorised legal practice not quantified | fits on modelled costs; legal exposure unquantified |
| K6 | time to first revenue 3 months HARD | 2 months | fits (depends on a first case from personal contacts; 100 customers take about 21 months) |
| K7 | B2C only HARD | individual shoppers pay | fits |
| K8 | off-limits categories HARD | food and medical disputes excluded by scope (forge-v1.md Narrowest wedge) | fits |
| K9 | keeps full-time job HARD | 7.3 h per week; the forge's 24-hour delivery promise may conflict with working hours | fits |

## Verdict inputs
- conservative unit economics positive: no. Cash contribution per case is positive (₹125.58, 84.3%), but at conservative volume of 4.75 cases per month the cash result is -₹403.5 per month after ₹1,000 fixed cost (break-even 8 cases). With founder time at ₹250 per hour, contribution per case is -₹61.92. Time-valued blended CAC (₹1,474) is about 12 times cash contribution per case, with no repeat purchases. Willingness to pay ₹149–199 is unsupported by data (C18).
- HARD constraints broken in conservative case: none on modelled numbers. Not modelled and unverified: legality of paid non-lawyer drafting (forge-v1.md#C20) and whether registration or a trade licence is required (C09).
- FLEXIBLE stretches required: none. K4 freelancer spend is not used.
