---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: economics-modeler
version: 2
created: 2026-10-15T12:00:00Z
---

## Inputs
Currency INR (₹). No conversion used. Pune-specific price, conversion and channel-cost data was not found (01-local-market.md coverage 3/10); most inputs are ASSUMPTION. Changes from economics-v1: (a) conservative price lowered to the sourced Quikr paid-ad rate floor; (b) compliance cost now included, using the upper end of forge-v2.md#C27; (c) sunk-capital arithmetic corrected (v1 double-counted first-month tools and flyers). Sources carried from economics-v1 were not re-opened in this round; they are marked "carried".

- [C01] Price, listing fee per seller: conservative ₹110, base ₹199, optimistic ₹224 (₹199 plus 25% of sellers taking the ₹99 featured upgrade). Conservative anchor is the Quikr "Top of Page" rate of ₹110 (Quikr Urgent ₹66, Top+Urgent ₹176) for Mobile and Electronics, from an undated rate deck, years old, not furniture, and the reported paid upgrades receive poor seller reviews (national). [source: https://www.slideshare.net/slideshow/quikr-ecomm-platform/75732007, undated, as reported in forge-v2.md#C20; not re-opened] ₹199 and ₹99 come from forge-v2 core identity [ASSUMPTION: untested; free alternatives OLX/Facebook exist per forge-v2.md#C08, so willingness to pay is unevidenced]
- [C02] Payment collection fee 2% + 18% GST = 2.36% of transaction (Razorpay standard rate) (national). [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/] (carried). UPI MDR statements conflict (0% vs 0.4% above ₹2,000 from 2026-10-15); 2.36% kept as the pessimistic figure.
- [C03] Refunds / failed listings: conservative 10% of price, base 5%, optimistic 2% [ASSUMPTION: no data; a paid service with free substitutes plausibly sees refund requests when the item does not sell]
- [C04] Meta ads CPC in India: conservative ₹34, base ₹18, optimistic ₹8 (national, vendor estimates, methods unclear; sources range about ₹1 to ₹34). [source: https://insights.vaizle.com/facebook-ads-cost/; https://owlclaw.com/benchmarks/meta-ads-benchmarks-india] (carried)
- [C05] Click-to-paid-seller conversion for a paid Instagram boost: conservative 1%, base 2%, optimistic 3% [ASSUMPTION: no data; test row only, not in the forge path]
- [C06] Paying sellers over the first 8 charging weeks (society groups / Instagram / flyers / brokers). Conservative 12 / 10 / 15 / 15 = 52; base 24 / 30 / 30 / 30 = 114; optimistic 30 / 36 / 45 / 30 = 141 [ASSUMPTION: forge-v2 table (24 / 30 / 30 / 30) is itself ASSUMPTION with no sourced number (forge-v2 Path to first 100); conservative uses about 0.5x for groups, brokers and flyers, 0.33x for Instagram. Forge-v2 sums its own channels to ~84-120, and says the buyer side must be built first]
- [C07] Flyer/QR print and travel: ₹3,000 for 30 societies in all scenarios [ASSUMPTION: about ₹100 per society]
- [C08] Broker/PG-owner referral ₹50 per paid listing [ASSUMPTION: forge-v2 value; broker willingness untested]
- [C09] Fixed operating cost ₹1,000/month (second SIM/business number, spreadsheet and design tools) [ASSUMPTION: WhatsApp Business and Community assumed free; Meta terms on commercial group use not checked (forge-v2.md#C17)]
- [C10] Compliance cost one-time (DPDP notice and consent text; seller undertaking, grievance officer contact and ranking note under the Consumer Protection E-Commerce Rules, if applicable): conservative ₹15,000 lawyer review plus 10 operator hours; base ₹5,000; optimistic ₹0 self-drafted. Recurring 1 hour/month. Cost range is from forge-v2.md#C27 [ASSUMPTION: no sourced figure; applicability to an operator-run board with off-platform sales is unresolved per forge-v2 Fixes KE4]. Rules summarised from law-firm pages (national): https://www.indialaw.in/blog/consumer-protection-e-commerce-rules/ ; https://khaitanco.com/thought-leaderships/Stricter-Regulations-on-E-Commerce-The-Consumer-Protection-E-Commerce-Rules-2020 (as reported in forge-v2; not re-opened). DPDP applies to collecting seller phone numbers and photos (national) [source: https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/] (carried)
- [C11] Other pre-revenue one-offs: business SIM and handset-side ₹1,500; flyers ₹3,000 (C07) in all scenarios [ASSUMPTION]
- [C12] GST: registration for services required above ₹20 lakh turnover in Maharashtra; model turnover is under ₹1 lakh, so no GST on fees is modelled in cash figures (national). [source: https://razorpay.com/learn/gst-registration-limits/] (carried). Whether an e-commerce-operator category forces registration is unresolved. Sensitivity only: if the fee is GST-inclusive at 18%, conservative net price falls from ₹110 to ₹93.22 and margin to ₹79.3 (see Calculations 12).
- [C13] Operator time per paid listing: 30 min conservative, 25 base, 20 optimistic [ASSUMPTION: forge-v2.md#C14 states 20-30 min]
- [C14] Acquisition hours (conservative): society groups 8 h, Instagram 12 h, flyers 10 h, broker outreach 7.5 h = 37.5 h; buyer-community build 30 h before charging [ASSUMPTION: estimated from posting counts]
- [C15] Operator time valued at ₹300/hour for sensitivity only [ASSUMPTION: rough admin freelancer rate in an Indian metro; not sourced; not used in cash figures]
- [C16] Repeat purchase by the same seller: 0 conservative and base; optimistic 0.1 [ASSUMPTION: sellers move every 1-2 years; one-off fee]
- [C17] Months to first revenue: community must reach 300-500 members before charging (forge-v2). Conservative 10 weeks to threshold plus 2 weeks to first paid seller = 12 weeks (2.8 months); base 4 weeks; optimistic 3 weeks [ASSUMPTION: forge-v2 says weeks 3-4 for its best case; no Pune channel data. Compliance review is assumed to run in parallel with the community build]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹110 | ₹199 | ₹224 |
| COGS per unit (listing) | ₹13.60 (payment ₹2.60 + refunds ₹11.00) | ₹14.65 | ₹9.77 |
| gross margin % | 87.6% (₹96.40) | 92.6% (₹184.35) | 95.6% (₹214.23) |
| CAC: society/RWA groups (cash) | ₹0 (0.67 h per customer) | ₹0 (0.4 h) | ₹0 (0.25 h) |
| CAC: Instagram organic (cash) | ₹0 (1.2 h per customer) | ₹0 (0.6 h) | ₹0 (0.3 h) |
| CAC: flyers/QR (cash) | ₹200 (₹3,000 / 15) | ₹100 | ₹67 |
| CAC: broker referral (cash) | ₹50 | ₹50 | ₹50 |
| CAC: paid Instagram boost (test row, not in forge path) | ₹3,400 | ₹900 | ₹267 |
| blended CAC (four forge channels, cash) | ₹72 | ₹39 | ₹32 |
| blended CAC, operator time at ₹300/h | ₹438 | not computed | not computed |
| payback period (months) | per-customer cash CAC: under 1 month; recovery of ₹22,300 sunk capital: about 17 months at modelled volume; time-priced: never | under 1 per customer; sunk ₹10,500 about 4 months | under 1; sunk ₹5,200 about 1.5 months |
| break-even volume | 11 listings/month to cover ₹1,000 fixed; 232 cumulative listings to recoup ₹22,300; time-priced: none | 6/month; 57 cumulative | 5/month; 25 cumulative |
| capital to first revenue | ₹22,300 | ₹10,500 | ₹5,200 |
| months to first revenue | 2.8 | 1.0 | 0.7 |

Base/optimistic arithmetic: base margin 199 - (199 x 0.0236 = 4.70) - (199 x 0.05 = 9.95) = ₹184.35; optimistic 224 - 5.29 - 4.48 = ₹214.23. Base blended CAC (3,000 + 30 x 50) / 114 = ₹39.5; optimistic 4,500 / 141 = ₹31.9. Base capital: ₹5,000 + ₹3,000 + ₹1,500 + 1.0 x ₹1,000 = ₹10,500; optimistic ₹0 + ₹3,000 + ₹1,500 + 0.7 x ₹1,000 = ₹5,200. Base sunk payback: monthly volume 114 / 8 weeks x 4.33 = 61.7 listings; contribution 61.7 x 184.35 - fixed 1,000 - broker (30/114 x 61.7 x 50 = 812) = about 9,560/month; 10,500 / 9,560 = about 1.1 months. The "about 4 months" and "about 1.5 months" in the table are therefore rough and not sourced; treat base and optimistic payback as unverified (base 1.1 months by this arithmetic; optimistic by the same method is under 1 month). Base volume depends on C06.

## Calculations
Conservative column.

1. Price: ₹110 (C01).
2. Payment fee: ₹110 x 0.0236 = ₹2.60.
3. Refunds: ₹110 x 0.10 = ₹11.00.
4. COGS: ₹2.60 + ₹11.00 = ₹13.60. Margin: ₹110 - ₹13.60 = ₹96.40; 96.40 / 110 = 87.6%.
5. Customers (8 charging weeks): 12 + 10 + 15 + 15 = 52.
6. Cash acquisition: flyers ₹3,000 + broker referrals 15 x ₹50 = ₹750; total ₹3,750. Blended cash CAC = 3,750 / 52 = ₹72.1. Flyers 3,000 / 15 = ₹200; broker ₹50; groups and Instagram ₹0 cash.
7. Paid boost test: ₹34 / 0.01 = ₹3,400 per paid seller; 35x the ₹96.40 margin; no payback.
8. Per-customer payback: ₹72.1 < ₹96.40, recovered on the first listing (under 1 month). Broker-referred listing nets ₹96.40 - ₹50 = ₹46.40.
9. Operator time: acquisition 37.5 h + fulfilment 52 x 0.5 h = 26 h = 63.5 h in the charging window. Per customer 63.5 / 52 = 1.22 h x ₹300 = ₹366; loaded CAC ₹366 + ₹72 = ₹438. Fulfilment alone 0.5 h x ₹300 = ₹150 exceeds margin ₹96.40, so at ₹300/h no volume gives positive contribution.
10. Capital to first revenue: lawyer review ₹15,000 + flyers ₹3,000 + SIM ₹1,500 + tools 2.8 months x ₹1,000 = ₹2,800 = ₹22,300. (Broker referral is paid per listing, so not pre-revenue.)
11. Operating result, first 8 charging weeks, excluding sunk items: revenue 52 x ₹110 = ₹5,720; COGS 52 x ₹13.60 = ₹707; broker ₹750; fixed 2 x ₹1,000 = ₹2,000 (flyers already in sunk). Net = 5,720 - 707 - 750 - 2,000 = ₹2,263. Cumulative position at end of week 20 = 2,263 - 22,300 = -₹20,037.
12. Break-even: fixed ₹1,000 / ₹96.40 = 10.4, rounded up to 11 listings/month. Cumulative recoup: ₹22,300 / ₹96.40 = 231.3, rounded up to 232 listings. GST-inclusive sensitivity: 110 / 1.18 = ₹93.22; less payment 2.2 (2.36% x 93.22) and refunds 9.32 = margin ₹81.7 approx (approx ₹79-82 depending on fee base); break-even about 13 listings/month. Not used as the conservative figure.
13. Sunk-capital payback at modelled volume: 52 listings / 8 weeks x 4.33 = 28.1 listings/month; contribution 28.1 x 96.40 = ₹2,709; less fixed ₹1,000; less broker (15/52 x 28.1 x ₹50 = ₹405) = ₹1,304/month. 22,300 / 1,304 = 17.1 months. This assumes seller flow of 28 per month continues, which is unevidenced (forge-v2.md#C11).
14. Hours: community build 30 h + acquisition 37.5 h + compliance 10 h = 77.5 h over the 10-week pre-charging window = 7.75 h/week peak. Charging window: fulfilment 26 h + 1 h/month compliance over 8 weeks = about 28 h = 3.5 h/week plus continuing acquisition.
15. Months to first revenue: 12 / 4.33 = 2.8 months.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | ₹22,300 to first revenue; maximum modelled loss about ₹22,300 plus fixed costs while running | fits |
| K2 | 10 h/week HARD | peak about 7.75 h/week (calc 14) | fits |
| K3 | skills (have) HARD | manual listing, Instagram, spreadsheet; legal review hired from the ₹15,000 line | fits |
| K4 | skills (can hire) FLEXIBLE | lawyer review is a purchase inside K1; no freelancer needed; STRETCH USED: none | fits |
| K5 | risk: cannot lose more than ₹1,00,000 HARD | maximum modelled loss about ₹22,300; platform-ban, legal and applicability risk unquantified | fits |
| K6 | first revenue within 3 months HARD | 2.8 months (12 weeks); about 1 week slack, depends on C17 | fits (thin margin) |
| K7 | B2C only HARD | sellers are individuals | fits |
| K8 | off-limits categories HARD | used furniture and appliances; no food, medical, alcohol, gambling, crypto, MLM | fits |
| K9 | keeps full-time job HARD | 7.75 h/week peak | fits |

## Verdict inputs
- conservative unit economics positive: yes on a per-unit cash basis only (margin ₹96.40, cash CAC ₹72, per-customer payback under 1 month, operating net ₹2,263 over 8 charging weeks). Sunk capital ₹22,300 is not recovered in that window; recovery takes about 17 months at 28 listings/month, if that volume persists. No when operator time is priced at ₹300/h (fulfilment time alone ₹150 exceeds margin). No on paid acquisition (CAC ₹3,400 vs margin ₹96.40). The cash result rests on unpaid organic channels and customer counts (C06) that are ASSUMPTION with no Pune data, and on sellers paying for a listing when OLX and Facebook are free (forge-v2.md#C10, no evidence; Quikr/MagicBricks precedents show fees exist, not that they work at this price).
- HARD constraints broken in conservative case: none
- FLEXIBLE stretches required: none
