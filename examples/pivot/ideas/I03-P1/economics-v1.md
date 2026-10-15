---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: economics-modeler
version: 1
created: 2026-10-15T17:00:00Z
---

## Inputs
Unit = one completed sale of a used furniture/appliance item between two Pune tenants. Customer = the seller. All figures INR. No currency conversion is used.
Local data is thin (01-local-market.md coverage score 3). Ad-cost and payment-fee sources are national or global and were seen only as search-result summaries; the pages could not be opened (proxy refused). Low confidence.

- [C01] Average sale price, conservative ₹3,000, base ₹4,500, optimistic ₹6,000. Low end of forge range ₹3,000-6,000, itself derived from unverified resale ranges (30-60% recovery; wardrobe ₹5,000-9,000). [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1; ASSUMPTION: forge-v1.md#C13 range, single guide site, unverified]
- [C02] Commission rate 10% of sale price. [ASSUMPTION: set by forge-v1 revenue model; no evidence sellers accept it, forge-v1.md#C14]
- [C03] Share of completed sales that pay the commission (leakage): conservative 40%, base 60%, optimistic 85%. [ASSUMPTION: forge-v1.md#C14 says leakage of 30-60% is plausible with no escrow; conservative takes the 60% end; no sourced leakage data]
- [C04] Payment fee via Razorpay payment link: 2% platform fee plus 18% GST = 2.36% effective; UPI bank-account MDR 0%; a first-90-day 0% platform fee may apply. Conservative uses 2.36%. (national) [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/; https://razorpay.com/blog/upi-charges-explained-mdr-vs-platform-fees/; figures from search summary, pages not opened]
- [C05] Tools: WhatsApp groups (manual posting) and Google Form/Sheet at ₹0; SIM, domain, misc ₹1,000/month conservative, ₹700 base, ₹500 optimistic. [ASSUMPTION: free tiers; misc cost is a placeholder]
- [C06] Operator time per completed sale: conservative 2.0 h, base 1.5 h, optimistic 1.0 h. [ASSUMPTION: forge-v1.md#C15 gives 1.5 h; conservative is worse]
- [C07] Value of operator time for the loaded-cost view: ₹150/hour. Not a cash cost; shown because K2 caps hours. [ASSUMPTION: low-end freelance admin/social rate in India; no source found]
- [C08] Meta ad costs in India vary across vendor blogs: CPC ₹0.51-2.26 in one, ₹8-25 in another, ₹34 in a third; CPM ₹50-200 for feed in one; Reels 20-35% below feed; Q4 (Oct-Dec) CPM up 30-60%. Conservative CPM ₹300 (top of range plus Q4 uplift, test runs in Q4 from 2026-10-15); base ₹150; optimistic ₹100. (national) [source: https://insights.vaizle.com/facebook-ads-cost/; https://upgrowth.in/?p=27575; https://owlclaw.com/benchmarks/meta-ads-benchmarks; figures from search summary, pages not opened; ASSUMPTION: pessimistic end chosen]
- [C09] Instagram impressions bought: 60,000 over 3 months. Impression-to-listing: conservative 0.05%, base 0.1% (forge-v1), optimistic 0.15%. Listing-to-completed-sale: conservative 25%, base 33% (forge-v1.md#C12), optimistic 40%. [ASSUMPTION: no Pune social data in 01-local-market.md]
- [C10] WhatsApp/society groups: conservative 30 groups x 150 members = 4,500 reach, 0.5% list, 25% complete. Base 60 x 150 = 9,000, 1%, 33%. Optimistic 9,000, 1.5%, 40%. Cash cost ₹0. [ASSUMPTION: no Pune group data; admin permission unverified (forge-v1.md#C18)]
- [C11] Broker/PG-manager referral fee paid only on a completed sale: conservative ₹150, base and optimistic ₹100. Conservative 7.5 referrals x 25% = 1.9 sales; base 10 sales (forge-v1); optimistic 15. [ASSUMPTION: brokers see move-outs per https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/ (2025-08); fee and response rates assumed]
- [C12] Society notice boards: ₹3,000 conservative (40 societies), ₹2,000 base, ₹2,000 optimistic. Conservative 20 listings x 25% = 5 sales; base 15; optimistic 25. [ASSUMPTION: no price or response data]
- [C13] Maharashtra Shops and Establishments: firms with fewer than 10 workers file an intimation, reported free by compliance sites that conflict on timing and validity. ₹500 allowance conservative. GST not modelled (turnover below threshold at these volumes; threshold not checked). [source: https://www.registerkaro.in/post/gumasta-license-fees; https://www.keka.com/compliance/forms/maharashtra-shop-and-establishment-registration; commercial sites, search summary only]
- [C14] Time to first paid commission: conservative 2.5 months, base 1.5, optimistic 1.0. [ASSUMPTION: weeks 1-3 join groups, first listing about week 4, sale and payment on top of leakage delay; no benchmark]
- [C15] Capital to first revenue (cash spent before the first commission lands): conservative ₹10,500 (Instagram month 1 ₹6,000 + notices ₹3,000 + tools ₹1,000 + registration ₹500); base ₹5,700; optimistic ₹4,500. [ASSUMPTION: spend schedule]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price (avg item sale price) | ₹3,000 | ₹4,500 | ₹6,000 |
| revenue per completed sale (10% x share paying) | ₹120 (₹300 x 40%) | ₹270 (₹450 x 60%) | ₹510 (₹600 x 85%) |
| COGS per unit (payment fee, cash only) | ₹2.83 | ₹6.37 | ₹12.04 |
| gross margin % (cash COGS only) | 97.6% | 97.6% | 97.6% |
| gross margin % incl. operator time at ₹150/h | -152% | 14.3% | 70% |
| CAC: society/tenant WhatsApp groups (cash) | ₹0 (₹804 time-loaded) | ₹0 (about ₹300 time-loaded) | ₹0 |
| CAC: Instagram (paid impressions) | ₹2,400 | ₹450 | ₹133 |
| CAC: broker/PG referral | ₹150 | ₹100 | ₹100 |
| CAC: society notice boards | ₹600 | ₹133 | ₹80 |
| blended CAC (cash) | ₹1,064 | ₹160 | ₹89 |
| blended CAC (time-loaded) | ₹1,627 | about ₹290 | about ₹150 |
| payback period (months) | not reached; needs 9.1 sales per acquired seller, seller is one-time | under 1 month (₹160 / ₹264 = 0.6 sales) | under 1 month |
| break-even volume (completed sales/month, fixed cost only) | 8.5 | 2.7 | 1.0 |
| break-even including CAC | none: contribution ₹117 < CAC ₹1,064 | positive | positive |
| capital to first revenue | ₹10,500 | ₹5,700 | ₹4,500 |
| months to first revenue | 2.5 | 1.5 | 1.0 |

Base and optimistic columns are shown for reference only; they do not count toward a PASS. Their CAC and time-loaded values are rough and not re-derived in Calculations.

## Calculations
Conservative column.

1. Commission per sale: ₹3,000 x 10% = ₹300. Paying share 40%: ₹300 x 0.40 = ₹120 realised per completed sale.
2. Payment fee: ₹300 x 2.36% = ₹7.08 on a paying sale; per completed sale ₹7.08 x 0.40 = ₹2.83. Cash gross margin = (120 - 2.83) / 120 = 97.6%. Contribution per sale ₹117.17.
3. Time-loaded margin: 2.0 h x ₹150 = ₹300; ₹117.17 - ₹300 = -₹182.83; / 120 = -152%.
4. Channels (3-month test):
   - WhatsApp: 4,500 x 0.5% = 22.5 listings; x 25% = 5.6 completed. Cash ₹0. Hours 30. Time-loaded CAC = 30 x 150 / 5.6 = ₹804.
   - Instagram: 60,000 x ₹300 / 1,000 = ₹18,000. Listings 60,000 x 0.05% = 30; x 25% = 7.5 completed. CAC = 18,000 / 7.5 = ₹2,400. Hours 10.
   - Broker: 7.5 referrals x 25% = 1.9 completed; fees 1.9 x ₹150 = ₹281; CAC ₹150. Hours 15.
   - Notice boards: ₹3,000 / 5 = ₹600. Hours 20.
5. Completed total = 5.6 + 7.5 + 1.9 + 5.0 = 20.0. Cash acquisition spend = 0 + 18,000 + 281 + 3,000 = ₹21,281. Blended cash CAC = 21,281 / 20 = ₹1,064. Acquisition hours 75 x ₹150 = ₹11,250; time-loaded blended CAC = (21,281 + 11,250) / 20 = ₹1,627.
6. Payback: ₹1,064 / ₹117 = 9.1 sales per acquired seller. A seller transacts once on leaving (forge-v1 persona), so payback is not reached. Repeat use is not evidenced.
7. Break-even on fixed cost: ₹1,000 / ₹117 = 8.5 completed sales/month. The 3-month mix yields about 6.7 completed sales/month (20 / 3), below 8.5.
8. 3-month cash result: revenue 20 x ₹117 = ₹2,343; spend ₹21,281 + fixed ₹3,000 + registration ₹500 = ₹24,781. Net = -₹22,438. Maximum cash at risk about ₹24,800.
9. Capital to first revenue: ₹6,000 + ₹3,000 + ₹1,000 + ₹500 = ₹10,500.
10. Hours: acquisition 75 h + operations 20 x 2 h = 40 h + admin 5 h = 120 h over 13 weeks = 9.2 h/week.
11. Without paid Instagram (not the conservative case): completed 12.5, cash ₹3,281, blended cash CAC ₹262, still above ₹117 contribution per sale.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | ₹24,781 maximum spend over 3 months; ₹10,500 to first revenue | fits |
| K2 | 10 hours/week HARD | 9.2 h/week (120 h / 13 weeks); thin margin | fits |
| K3 | skills have HARD | uses spreadsheets, social media marketing, languages; no coding | fits |
| K4 | skills can hire/learn FLEXIBLE | no freelancer used | fits |
| K5 | low risk, cannot lose more than ₹1,00,000 HARD | maximum loss about ₹24,800; conservative net -₹22,438, no payback | fits |
| K6 | first revenue within 3 months HARD | 2.5 months; leakage or admin refusal can push past 3 months | fits (thin) |
| K7 | B2C only HARD | seller and buyer are individuals | fits |
| K8 | off-limits categories HARD | used furniture and appliances; Shops and Establishments status unverified (C13) | fits |
| K9 | keeps full-time job HARD | 9.2 h/week outside work | fits |

STRETCH USED: none.

## Verdict inputs
- conservative unit economics positive: no. Cash contribution per sale ₹117; blended cash CAC ₹1,064 (₹262 without paid Instagram); the seller is a one-time user; with operator time at ₹150/h the contribution is -₹183 per sale.
- HARD constraints broken in conservative case: none
- FLEXIBLE stretches required: none
- confidence: low. Every load-bearing input (price, leakage, conversion, completion, CPM) is ASSUMPTION or an unopened search-summary figure; local coverage 3/10.
