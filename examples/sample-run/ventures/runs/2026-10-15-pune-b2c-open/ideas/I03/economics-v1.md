---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: economics-modeler
version: 1
created: 2026-10-15T11:00:00Z
---

## Inputs
Currency INR (₹). No currency conversion used. Geography of every input outside Pune is tagged. Pune-specific price, conversion and channel-cost data was not found (01-local-market.md coverage 3/10); most inputs are ASSUMPTION.

- [C01] Price, listing fee per seller: conservative ₹149 effective (₹199 list less a 25% launch/negotiation discount), base ₹199, optimistic ₹224 (₹199 plus 25% of sellers taking the ₹99 featured upgrade) [ASSUMPTION: ₹199 and ₹99 come from forge-v1 core identity; discount and upgrade take-up are untested. Free alternatives OLX/Facebook exist per forge-v1.md#C08, so sellers' willingness to pay is unevidenced]
- [C02] Payment collection fee 2% + 18% GST = 2.36% of the transaction on a payment gateway (Razorpay standard rate) (national) [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/]. The same search showed conflicting statements on UPI MDR (0% vs 0.4% above ₹2,000 from 2026-10-15); not verified; irrelevant at ₹199 ticket if MDR is 0% under ₹2,000, so 2.36% is used as the pessimistic figure.
- [C03] Refunds / failed listings / disputes: conservative 10% of listings, base 5%, optimistic 2% of price refunded [ASSUMPTION: no data; a ₹199 service with free substitutes plausibly sees refund requests when the item does not sell]
- [C04] Meta ads CPC in India: ₹34 per click (Vaizle) at the pessimistic end; ₹8-25 across most industries (OwlClaw 2026 client data) (national, vendor estimates, methods unclear; estimates across sources range about ₹1 to ₹34). Conservative ₹34, base ₹18, optimistic ₹8. [source: https://insights.vaizle.com/facebook-ads-cost/; https://owlclaw.com/benchmarks/meta-ads-benchmarks-india] (national)
- [C05] Click-to-paid-seller conversion for a paid Instagram boost: conservative 1%, base 2%, optimistic 3% [ASSUMPTION: no data. Applies only to the paid-boost test row, which is not in the forge's path; included because organic channels cannot be scaled by spend]
- [C06] Organic channel customer counts over the first 8 weeks of charging, as a fraction of forge-v1's own assumed counts (society groups 24, Instagram 30, flyers 30, brokers 30). Conservative: 12 / 10 / 15 / 15 = 52; base: 24 / 30 / 30 / 30 = 114; optimistic: 30 / 36 / 45 / 30 = 141 [ASSUMPTION: forge-v1 conversions are themselves ASSUMPTION (forge-v1.md#C10-C13); conservative uses about 0.5x for groups and brokers, 0.33x for Instagram, 0.5x for flyers]
- [C07] Flyer/QR notice-board print and travel cost: ₹3,000 for 30 societies in all scenarios [ASSUMPTION: about ₹100 per society for printing, tape and local travel]
- [C08] Broker/PG-owner referral ₹50 per paid listing, from forge-v1's path [ASSUMPTION: forge-v1 value; brokers' willingness untested]
- [C09] Fixed operating costs ₹1,000/month (second SIM / business number, spreadsheet and design tools) [ASSUMPTION: WhatsApp Business app and Community assumed free to use; Meta terms on commercial use of groups not checked (forge-v1.md#C17)]
- [C10] One-off pre-revenue setup: ₹5,000 for privacy notice, consent text and a one-time consultation on DPDP and intermediary rules; ₹3,000 flyers; ₹1,500 business SIM and handset-side costs; ₹1,000 first-month tools. Total ₹10,500 [ASSUMPTION: consultant fee not sourced; DPDP applies to collecting seller phone numbers and photos (national) per source: https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/]
- [C11] GST registration for services is required above ₹20 lakh aggregate turnover in Maharashtra (a normal-category state); model turnover is under ₹1 lakh, so no GST on fees is modelled. Section 24 mandatory-registration categories include e-commerce sales; whether an operator-run listing board falls in them is unresolved. (national) [source: https://razorpay.com/learn/gst-registration-limits/]
- [C12] Operator time: 30 min per paid listing (post, moderate, chat) in conservative; 25 min base; 20 min optimistic [ASSUMPTION: forge-v1 assumes 20-30 minutes, forge-v1.md#C14]
- [C13] Acquisition-side operator hours (conservative): society groups 8 h, Instagram content 12 h, flyers 10 h, broker outreach 7.5 h = 37.5 h; buyer-community build 30 h before charging [ASSUMPTION: forge-v1 offers no hours; estimated from posting counts]
- [C14] Operator time valued at ₹300/hour for a sensitivity line only [ASSUMPTION: rough freelancer rate for admin and community tasks in an Indian metro; not sourced; not used in cash figures]
- [C15] Repeat purchase by the same seller: 0 in the conservative case and base; optimistic 0.1 repeat listings per seller within the window [ASSUMPTION: sellers move every 1-2 years; one-off fee, no subscription]
- [C16] Months to first revenue: buyer community must reach 300-500 members before charging (forge-v1 path). Conservative 10 weeks to reach threshold plus 2 weeks to the first paid seller = 12 weeks (2.8 months); base 4 weeks (1 month); optimistic 3 weeks [ASSUMPTION: forge-v1 estimates weeks 3-4 for the best case; no Pune channel data]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹149 | ₹199 | ₹224 |
| COGS per unit (listing) | ₹18.42 (payment ₹3.52 + refunds ₹14.90) | ₹14.65 | ₹9.77 |
| gross margin % | 87.6% (₹130.58) | 92.6% (₹184.35) | 95.6% (₹214.23) |
| CAC: society/RWA groups (cash) | ₹0 (0.67 h per customer) | ₹0 (0.4 h) | ₹0 (0.25 h) |
| CAC: Instagram organic (cash) | ₹0 (1.2 h per customer) | ₹0 (0.6 h) | ₹0 (0.3 h) |
| CAC: flyers/QR (cash) | ₹200 (₹3,000 / 15) | ₹100 | ₹67 |
| CAC: broker referral (cash) | ₹50 | ₹50 | ₹50 |
| CAC: paid Instagram boost (test row, not in forge path) | ₹3,400 | ₹900 | ₹267 |
| blended CAC (four forge channels, cash) | ₹72 | ₹39 | ₹32 |
| blended CAC, operator time priced at ₹300/h | ₹438 | not computed | not computed |
| payback period (months) | cash: under 1 (recovered on the first listing); time-priced: never | under 1 | under 1 |
| break-even volume | 8 listings/month for ₹1,000 fixed; 81 cumulative listings to recoup ₹10,500 setup; time-priced: no volume breaks even | 6 / 57 | 5 / 49 |
| capital to first revenue | ₹10,500 | ₹8,500 (no consultant overrun; ASSUMPTION) | ₹7,500 (ASSUMPTION) |
| months to first revenue | 2.8 | 1.0 | 0.7 |

Base and optimistic break-even: fixed ₹1,000 / margin ₹184.35 = 5.4, rounded to 6; ₹1,000 / ₹214.23 = 4.7, rounded to 5. Cumulative: ₹10,500 / ₹184.35 = 57; ₹10,500 / ₹214.23 = 49 (base and optimistic capital figures differ, but the same ₹10,500 is used for these ratios).

## Calculations
Conservative column.

1. Price: ₹199 x (1 - 0.25) = ₹149.25, rounded to ₹149.
2. Payment fee: ₹149 x 0.0236 = ₹3.52.
3. Refunds: ₹149 x 0.10 = ₹14.90.
4. COGS: ₹3.52 + ₹14.90 = ₹18.42. Margin: ₹149 - ₹18.42 = ₹130.58; 130.58 / 149 = 87.6%.
5. Customers (8 weeks): 12 + 10 + 15 + 15 = 52.
6. Cash acquisition spend: flyers ₹3,000 + broker referrals 15 x ₹50 = ₹750; total ₹3,750. Blended cash CAC = 3,750 / 52 = ₹72.1. Per channel: flyers 3,000 / 15 = ₹200; broker ₹50; groups and Instagram ₹0 cash.
7. Paid boost test: ₹34 per click / 0.01 = ₹3,400 per paid seller (exceeds margin ₹130.58 by 26x; no payback with a one-off fee and zero repeat).
8. Payback: cash CAC ₹72.1 < margin ₹130.58, recovered on the first listing (under 1 month). Broker-referred listings net ₹130.58 - ₹50 = ₹80.58.
9. Operator hours: acquisition 37.5 h + fulfilment 52 x 0.5 h = 26 h = 63.5 h in the charging window; plus 30 h community build = 93.5 h. Hours per customer in the charging window = 63.5 / 52 = 1.22 h; at ₹300/h = ₹366; plus cash CAC ₹72 = ₹438 loaded CAC. Fulfilment time alone, 0.5 h x ₹300 = ₹150, exceeds margin ₹130.58, so at ₹300/h no volume gives a positive contribution.
10. Operating result, first 8 charging weeks: revenue 52 x ₹149 = ₹7,748; COGS 52 x ₹18.42 = ₹958; acquisition ₹3,750; fixed 2 x ₹1,000 = ₹2,000. Net = 7,748 - 958 - 3,750 - 2,000 = ₹1,040. (The ₹3,000 flyer cost is also in the ₹10,500 setup; counted once here as acquisition, so setup excluding flyers of ₹7,500 is not recovered.)
11. Break-even: fixed ₹1,000 / ₹130.58 = 7.7, rounded up to 8 listings/month. Setup recoup: ₹10,500 / ₹130.58 = 80.4, rounded up to 81 listings.
12. Capital to first revenue: ₹5,000 + ₹3,000 + ₹1,500 + ₹1,000 = ₹10,500.
13. Hours per week: 93.5 h over 12 weeks to first revenue plus 8 charging weeks = 20 weeks gives about 4.7 h/week; peak load in weeks 1-10 is 30 h build / 10 weeks = 3 h/week plus acquisition 37.5 h in the same window (about 3.8 h/week) = about 6.8 h/week.
14. Months to first revenue: 12 weeks / 4.33 = 2.8 months.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | ₹10,500 to first revenue; ₹10,500 maximum loss in the model | fits |
| K2 | 10 h/week HARD | peak about 6.8 h/week (calc 13) | fits |
| K3 | skills (have): spreadsheets, social media, English/Hindi/Marathi HARD | manual listing, Instagram, spreadsheet; DPDP consult hired from the ₹5,000 line | fits |
| K4 | skills (can hire) FLEXIBLE | no freelancer needed; STRETCH USED: none | fits |
| K5 | risk: cannot lose more than ₹1,00,000 HARD | maximum modelled loss ₹10,500; platform-ban and legal risk unquantified | fits |
| K6 | first revenue within 3 months HARD | 2.8 months (12 weeks); about 1 week of slack, depends on assumption C16 | fits (thin margin) |
| K7 | B2C only HARD | sellers are individuals | fits |
| K8 | off-limits categories HARD | used furniture and appliances; no food, medical, alcohol, gambling, crypto, MLM | fits |
| K9 | keeps full-time job HARD | 6.8 h/week peak | fits |

## Verdict inputs
- conservative unit economics positive: yes on a cash basis only (margin ₹130.58 per listing, cash CAC ₹72, payback under 1 month, net ₹1,040 over the first 8 charging weeks, setup of ₹10,500 not recovered in that window). No when operator time is priced at ₹300/h (loaded CAC ₹438; fulfilment time alone exceeds margin). No on the paid-acquisition test (CAC ₹3,400 vs margin ₹130.58). The cash result rests on unpaid organic channels and on customer counts (C06) that are ASSUMPTION with no Pune data; the central input, that sellers pay ₹149-199 when OLX and Facebook are free (forge-v1.md#C10), has no evidence.
- HARD constraints broken in conservative case: none
- FLEXIBLE stretches required: none
