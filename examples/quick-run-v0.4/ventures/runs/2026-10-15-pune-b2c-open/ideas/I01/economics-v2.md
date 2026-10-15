---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: economics-modeler
version: 2
created: 2026-10-15T10:51:32Z
---

## Inputs
Currency: INR (contract currency); no conversion needed. No new pages were opened in round 2. All sourced inputs are search-result text carried from forge-v2.md and economics-v1.md, and are labeled as such.

- [C01] Price anchors for notice or drafting services: Rs 500 plus postage (Consumer Voice), Rs 1,499 plus Rs 60-80 postage (IncorpX), Rs 4,999 and up (Ebizfiling), Rs 3,000 (one 2026 LawRato advocate answer). All are lawyer-issued generic notices (national) [source: https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting ; https://ebizfiling.com/service/consumer-complaint-letter/ ; as cited in forge-v2.md#C05 and its Positioning table, not opened]
- [C02] Prices by scenario: conservative Rs 500, base Rs 799, optimistic Rs 1,499. Rs 799 is the forge working price and is untested. The conservative price is the lowest anchor [ASSUMPTION: no buyer of this exact service was found; forge-v2.md#C15 also marks Rs 799 untested]
- [C03] UPI payments of Rs 2,000 or less carry zero MDR from 2026-10-15; small merchants receiving up to Rs 1 lakh a month by UPI QR keep zero MDR (national) [source: https://morungexpress.com/npci-reveals-mdr-on-upi-payments-above-rs-2000-from-oct-15-small-merchants-continue-to-benefit ; as cited in economics-v1.md#C03]
- [C04] Payment-link gateway cost of 2% plus 18% GST on the fee, applied in the conservative case only as a worst case [ASSUMPTION: typical gateway rate; no price page found]
- [C05] Money-back guarantee from forge-v2.md Fixes (FE5): full Rs 799 refund within 7 days if the student cannot use the file; loss capped at the file price. Refund rate: conservative 15% of files, base 5%, optimistic 2%. Round 1 used 10% before the guarantee existed [ASSUMPTION: no refund data for any comparable service exists; the guarantee is explicit, so the pessimistic rate is raised]
- [C06] Refund reserve Rs 8,000 held in cash for about 10 refunds [forge-v2.md Fixes FM5, ASSUMPTION there]. Treated here as capital held, not a recurring cost
- [C07] Advocate opinion on whether a non-advocate may sell a calculator and generic template: conservative Rs 5,000, base Rs 2,500, optimistic Rs 0 [forge-v2.md Fixes FM5 gives about Rs 5,000, ASSUMPTION; no fee quote found]
- [C08] Legal background: Bar Council of India v A.K. Balaji (2018) is reported to apply a case-by-case "pith and substance" test to support services. One DIY guide argues Section 30 restricts appearance, not a personal demand notice (single non-authoritative source). No source confirms a comparable non-lawyer service operating (national) [source: https://itatonline.org/archives/?p=18108 ; https://www.amalegalsolutions.com/how-can-i-send-a-legal-notice-online-to-someone-in-india-without-hiring-a-lawyer ; as cited in forge-v2.md Fixes FM5, summaries only]
- [C09] Instagram CPC in India is reported at about Rs 6-55 across sources, clustering at Rs 10-25, and Education at Rs 15-30. These are vendor blogs and the sources conflict (national) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/ ; https://bosswallah.com/blog/creator-hub/instagram-ads-cost-in-india-2026-how-much-should-you-actually-spend/ ; https://owlclaw.com/benchmarks/meta-ads-benchmarks-india ; as cited in forge-v2.md and economics-v1.md#C08]. Conservative uses Rs 55 (top of range), base Rs 15, optimistic Rs 10
- [C10] Paid-ad funnel, click to chat to paid: conservative 5% x 20% = 1%; base 8% x 30% = 2.4%; optimistic 10% x 40% = 4%. Forge-v2.md uses 10% x 20% = 2% [ASSUMPTION: no Pune or niche conversion data found]
- [C11] Organic customers in the first 3 months. Forge-v2.md path table sums to about 70 (Instagram 20, groups 22, Google 15, referrals 15, all ASSUMPTION) and states 100 customers is more likely reached in 5-8 months. Conservative halves Instagram and groups (10 and 11), sets Google to 0, and sets referrals to 0.15 per customer (3), total 24. Base 70. Optimistic 100 [ASSUMPTION: no group access or follower count verified; forge-v2.md Fixes KM5 says none found]
- [C12] Instagram boost spend over 3 months: conservative Rs 5,000, base Rs 3,000, optimistic Rs 2,000 [forge-v1 range Rs 0-5,000 carried via economics-v1.md#C11, ASSUMPTION]
- [C13] Founder time per file: conservative 60 minutes, base 40, optimistic 30. Forge-v2.md states 30-45 minutes with no dry run done, and says heavier weeks reach about 10.5 hours [forge-v2.md#C16, ASSUMPTION; conservative raised above the forge range because no dry run exists]
- [C14] Fixed weekly founder hours independent of file volume, from the forge-v2.md hours table: WhatsApp replies 2.0, content 2.5, group answers 1.0, admin 0.5, total 6.0 [forge-v2.md Path to first 100, ASSUMPTION]
- [C15] Tools cost: WhatsApp Business app, Google Sheets and Docs, and Instagram are free. Conservative allocation Rs 500 a month, base and optimistic Rs 0 [ASSUMPTION: free-tier tools; founder already owns phone and internet]
- [C16] Demand is a trigger event with no Pune volume data. National coaching complaints to NCH were 16,276 in 2023-24. A free substitute exists: NCH 1915 recovered Rs 1.56 crore for 600+ students (national) [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes ; https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres ; as cited in forge-v2.md#C07-C08]
- [C17] Revenue is one-time per customer; lifetime value equals one file's contribution [forge-v2.md Core identity; reasoning, not a sourced fact]
- [C18] Service turnover is far below the Rs 20 lakh GST threshold, so no GST registration is modelled (national rule) [source: https://www.kanakkupillai.com/gst-registration-online-in-pune ; as cited in 01-local-market.md#C35a]
- [C19] Founder time budget is 10 hours a week (K2), 130 hours over 13 weeks [contract K2; arithmetic]
- [C20] Months to first revenue: conservative 2 months (set-up 2 weeks, advocate opinion 2 weeks, possible scope revision, 2-3 weeks to a first paid file); base 1.0; optimistic 0.75 [ASSUMPTION: no data on advocate turnaround]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | Rs 500 | Rs 799 | Rs 1,499 |
| COGS per unit (gateway fee + refunds) | Rs 87 | Rs 40 | Rs 30 |
| gross margin % | 82.6% | 95.0% | 98.0% |
| CAC: Instagram content with boost spend (cash per Instagram customer) | Rs 500 (plus about 3.9 founder hours) | Rs 150 | Rs 67 |
| CAC: MPSC/UPSC WhatsApp/Telegram groups | Rs 0 cash (about 2.4 founder hours) | Rs 0 cash | Rs 0 cash |
| CAC: Google search/Business profile | no customers in 3 months | Rs 0 cash | Rs 0 cash |
| CAC: referrals | Rs 0 cash | Rs 0 cash | Rs 0 cash |
| CAC: paid Instagram ads (not in forge path; tested as the only scalable channel) | Rs 5,500 | Rs 625 | Rs 250 |
| blended CAC (organic path, cash) | Rs 208 | Rs 43 | Rs 20 |
| payback period (months) | 0.5 on blended cash CAC; never on paid ads | under 0.1 blended; 0.8 on paid ads | under 0.1 blended; 0.2 on paid ads |
| break-even volume (files/month, cash costs only) | 7 | 2 | 1 |
| capital to first revenue | Rs 14,500 | Rs 12,000 | Rs 9,000 |
| months to first revenue | 2.0 | 1.0 | 0.75 |
| customers in first 3 months | 24 | 70 | 100 |
| net cash profit, steady month | Rs 720 at 8 files/month; ceiling Rs 4,400 at the K2 cap of 17 files | not computed | not computed |

Base and optimistic columns are shown for completeness and are not argued from. Their figures are rough ASSUMPTION-based estimates.

## Calculations
Conservative column.

Price Rs 500 [C02].

COGS per file [C04, C05]:
- gateway 2% x 500 = Rs 10; GST 18% x 10 = Rs 1.80; total Rs 11.80, rounded to Rs 12
- refund allowance 15% x 500 = Rs 75 (gateway fee is not recovered on refunds)
- COGS = 12 + 75 = Rs 87. Contribution = 500 - 87 = Rs 413. Gross margin = 413 / 500 = 82.6%.

Customers in 3 months [C11]: Instagram 10 + groups 11 + Google 0 + referrals 0.15 x 21 = 3 = 24.

Blended cash CAC [C12]:
- Instagram boost Rs 5,000 over 10 Instagram customers = Rs 500 each
- Rs 5,000 / 24 = Rs 208
- Contribution after CAC = 413 - 208 = Rs 205
- Payback = 208 / 413 = 0.50 months

Paid-ad CAC [C09, C10]: CPC Rs 55 / 1% = Rs 5,500. At the Education upper CPC of Rs 30: 30 / 0.01 = Rs 3,000. At forge-v2.md's own inputs (Rs 15 CPC, 2%): Rs 750. All three exceed Rs 413 contribution. Paid ads are not usable in the conservative case, and the forge's own paid check (Rs 750) also exceeds it. Base: 15 / 0.024 = Rs 625 vs base contribution 799 - 40 = Rs 759. Optimistic: 10 / 0.04 = Rs 250.

Founder hours [C13, C14, C19]:
- fixed activities 6.0 hours a week x 13 = 78 hours
- file production 24 x 1.0 = 24 hours
- total 102 of 130 hours = 7.8 hours a week average
- weekly cap: (10 - 6.0) / 1.0 = 4 files a week = about 17 files a month. A 5th file in a week takes the week to 11 hours, which breaks K2 unless content hours are cut.

Capital to first revenue (conservative) [C06, C07, C12, C15]: advocate opinion 5,000 + refund reserve 8,000 + first-month boost 1,000 + tools 500 = Rs 14,500.

3-month ledger (conservative):
- revenue 24 x 500 = Rs 12,000
- COGS 24 x 87 = Rs 2,088
- boost Rs 5,000
- tools 3 x 500 = Rs 1,500
- advocate Rs 5,000
- net = 12,000 - 2,088 - 5,000 - 1,500 - 5,000 = -Rs 1,588
- peak cash held out: 5,000 + 5,000 + 1,500 + 8,000 reserve = Rs 19,500

Break-even (conservative), monthly cash costs: tools 500 + boost 5,000 / 3 = 1,667 + advocate 5,000 / 12 = 417 = Rs 2,584. 2,584 / 413 = 6.26, so 7 files a month. The reserve is not amortised.

Steady month at 8 files: 8 x 413 = 3,304 - 2,584 = Rs 720. At the K2 cap of 17 files: 17 x 413 = 7,021 - 2,584 = Rs 4,437. This is a ceiling under the K2 limit; no scenario reaches Rs 10,000 a month at Rs 500 (needs (10,000 + 2,584) / 413 = 31 files, 7.5 files a week, against a cap of 4).

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital Rs 1,00,000 HARD | peak cash held out about Rs 19,500 (Rs 14,500 to first revenue) | fits |
| K2 | 10 hours a week HARD | average 7.8 hours a week; capped at 4 files a week by design; 5+ files in a week breaks | fits at the modelled volume of 24 files over 13 weeks (average 1.8 a week); breaks if intake is not capped |
| K3 | skills (have) HARD: spreadsheets, social media marketing, languages | spreadsheet, templates, social posts; legal drafting is not a stated skill, scope is limited to a generic template | fits on listed skills; legal competence not stated |
| K4 | skills (can hire/learn) FLEXIBLE | advocate opinion Rs 5,000, inside the Rs 1,00,000 cap | fits. No stretch used |
| K5 | risk appetite low; cannot lose more than Rs 1,00,000 HARD | cash loss capped at about Rs 19,500. Legal exposure (C08: case-by-case Advocates Act test, no confirming source) is not capped by the model | fits on cash; legal exposure UNRESOLVED until the advocate opinion exists |
| K6 | first revenue within 3 months HARD | 2.0 months | fits |
| K7 | B2C only HARD | individual students and parents pay | fits |
| K8 | off-limits categories HARD | none involved | fits |
| K9 | keeps full-time job HARD | evening and weekend work; employment-contract side-income clause unchecked (forge-v2.md#C27) | fits [ASSUMPTION: employer permits side work] |

No FLEXIBLE stretch was used.

## Verdict inputs
- conservative unit economics positive: yes per file (contribution Rs 413 on Rs 500; Rs 205 after blended cash CAC). Steady month about Rs 720 at 8 files, first 3 months net about -Rs 1,588. Positive only on organic channels. Paid CAC (Rs 3,000-5,500 conservative; Rs 750 on the forge's own inputs) exceeds the Rs 413 contribution, so the business cannot scale by spending money.
- HARD constraints broken in conservative case: none on the numbers. Unresolved: K5 legal exposure (C08), K9 employment clause, K3 legal-drafting competence not listed. K2 breaks if intake exceeds 4 files a week.
- FLEXIBLE stretches required: none
- what would have to change for the conservative case to work: per-unit math works; business size does not. (1) Volume: the K2 cap of about 17 files a month yields at most about Rs 4,400 a month at Rs 500, against 8 files a month modelled and no Pune volume evidence (C16) with a free NCH route at Rs 0. (2) Price: a Rs 10,000 net month at the K2 cap needs contribution of at least (10,000 + 2,584) / 17 = Rs 740 per file, so a price of about Rs 830 at the Rs 87 COGS (Rs 799 gives about Rs 760 only if refunds fall to about 5%), and no buyer evidence supports Rs 799. (3) Paid CAC would have to fall from Rs 5,500 to under Rs 413, which needs 13.3% click-to-paid at Rs 55 CPC, or 6.1% at Rs 25, against 1% assumed. Separately, a written advocate opinion that a non-advocate may sell the product is needed before launch.
