---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: economics-modeler
version: 1
created: 2026-10-15T10:41:49Z
---

## Inputs
Currency: INR (contract currency). No conversion needed. Search-result text only; pages were not opened by this agent.

- [C01] Price anchors for a notice/drafting service: Rs 500 plus postage (Consumer Voice) and Rs 1,499 plus Rs 60-80 postage (IncorpX); both are lawyer-issued generic notices (national) [source: https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting ; as cited in forge-v1.md#C05, not opened by this agent]
- [C02] Working price Rs 799 is untested; conservative price is set at the bottom anchor Rs 500, base Rs 799, optimistic Rs 1,499 [ASSUMPTION: the only price evidence is the Rs 500-1,499 notice range; no buyer of this exact service was found]
- [C03] UPI payments of Rs 2,000 or less carry zero MDR from the 2026-10-15 framework; eligible small merchants receiving up to Rs 1 lakh a month by UPI QR keep zero MDR; 0.4% applies above Rs 2,000 (national) [source: https://morungexpress.com/npci-reveals-mdr-on-upi-payments-above-rs-2000-from-oct-15-small-merchants-continue-to-benefit ; https://www.bajajbroking.in/share-market-news/upi-payments-above-rupee2000-to-attract-0-4percent-mdr-]
- [C04] Payment-link gateway fee of 2% plus 18% GST on the fee, used only in the conservative case as a worst case if the founder uses a gateway instead of a UPI QR [ASSUMPTION: typical gateway rate; Razorpay pricing was not found]
- [C05] Refund/concession allowance: conservative 10% of files refunded or discounted, base 3%, optimistic 1% [ASSUMPTION: price is paid upfront for a document; no refund data exists]
- [C06] Tools cost: WhatsApp Business app, Google Sheets/Docs, Instagram are free to use; conservative fixed tools/phone/design allocation Rs 500 a month [ASSUMPTION: free-tier tools; the founder already owns a phone and internet]
- [C07] Founder time per file: conservative 45 minutes, base 40, optimistic 30 [forge-v1.md#C16, ASSUMPTION: template-driven; untested]
- [C08] Instagram ad CPC in India in 2026 is about Rs 6-55 across industries, with Education at Rs 15-30 (third-party estimate; no official Meta figure found; sources conflict, one gives Rs 2-6) (national) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/ , April 2026 per search summary; https://bosswallah.com/blog/creator-hub/instagram-ads-cost-in-india-2026-how-much-should-you-actually-spend/]
- [C09] Paid-ad funnel (click to WhatsApp message to paid): conservative 5% x 20% = 1%; base 8% x 30% = 2.4%; optimistic 10% x 40% = 4% [ASSUMPTION: no Pune or niche conversion data found]
- [C10] Organic channel yields over 3 months, from forge-v1.md Path to first 100: Instagram 20 customers, groups 22, Google 15, referrals 15 (all ASSUMPTION in forge-v1). Conservative halves Instagram and groups (10 and 11), sets Google to 0 (a new profile with no search volume evidence will not rank within 3 months), and sets referrals to 0.15 per customer [ASSUMPTION: cautious haircut; group access not verified, forge-v1.md#C20]
- [C11] Instagram boost spend: conservative Rs 5,000 over 3 months (top of the forge range Rs 0-5,000), base Rs 3,000, optimistic Rs 2,000 [forge-v1.md Path to first 100, ASSUMPTION]
- [C12] One-time review by an advocate on whether a non-lawyer may sell calculations and letter templates: conservative Rs 5,000, base Rs 2,500, optimistic Rs 0 [ASSUMPTION: no fee quote found; needed because forge-v1.md#C17 left the legal question unresearched]
- [C13] Legal exposure: the Supreme Court in Bar Council of India v. A.K. Balaji held that practice of law includes non-litigation work such as drafting instruments and giving opinions, and Advocates Act s.29 limits the practice of law to advocates. No source was found on whether a non-advocate may sell a demand-letter template or a pro-rata calculation (national) [source: https://itatonline.org/archives/lawyers-collective-vs-bar-council-bombay-high-court/ ; https://bcajonline.org/?p=16796 ; search-result summaries only]
- [C14] Demand is a trigger event (student leaves or is refused), with no Pune volume data; NCH coaching complaints were 16,276 in 2023-24 nationally (national) [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes ; as cited in forge-v1.md#C08]
- [C15] A free substitute exists: NCH 1915 recovered Rs 1.56 crore for 600+ coaching students (national) [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres ; as cited in forge-v1.md#C07]
- [C16] Business is a one-time purchase, with no repeat or subscription revenue, so lifetime value equals one file's contribution [forge-v1.md Core identity; reasoning, not a sourced fact]
- [C17] Service turnover is far below the Rs 20 lakh GST threshold, so no GST registration is modelled (national rule) [source: https://www.kanakkupillai.com/gst-registration-online-in-pune ; as cited in 01-local-market.md#C35a]
- [C18] Founder time budget: 10 hours a week, about 43 hours a month (K2). A 13-week window is 130 hours [contract K2; arithmetic 10 x 52 / 12]

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | Rs 500 | Rs 799 | Rs 1,499 |
| COGS per unit (cash) | Rs 62 | Rs 27 | Rs 15 |
| gross margin % | 87.6% | 96.6% | 99.0% |
| CAC: Instagram content with boost spend (cash per Instagram customer) | Rs 500 (about 3.9 founder hours per customer) | Rs 150 | Rs 67 |
| CAC: MPSC/UPSC WhatsApp/Telegram groups | Rs 0 cash (about 2.4 founder hours per customer) | Rs 0 cash | Rs 0 cash |
| CAC: Google search/Business profile | no customers within 3 months | Rs 0 cash | Rs 0 cash |
| CAC: referrals | Rs 0 cash | Rs 0 cash | Rs 0 cash |
| CAC: paid Instagram ads (not in forge path; tested because it is the only scalable channel) | Rs 5,500 | Rs 1,250 | Rs 375 |
| blended CAC (organic path, cash) | Rs 208 | Rs 42 | Rs 20 |
| payback period (months) | 0.5 on blended cash CAC; never on paid ads | under 0.1; never on paid ads | under 0.1; 0.3 on paid ads |
| break-even volume (files/month, cash costs only) | 6 | 2 | 1 |
| capital to first revenue | Rs 6,500 | Rs 3,500 | Rs 1,000 |
| months to first revenue | 1.5 | 1.0 | 0.75 |
| customers in first 3 months | 24 | 72 | 100 (ASSUMPTION: forge sum is 72; faster ramp) |
| net cash profit, steady month | Rs 920 | Rs 4,600 | Rs 10,000+ |

Base and optimistic columns are shown for completeness only and are not argued from. Base and optimistic COGS, CAC and profit figures are rough ASSUMPTION-based estimates.

## Calculations
Conservative column.

Price: Rs 500 [C02].

COGS per file:
- gateway 2% x 500 = Rs 10; GST 18% x 10 = Rs 1.80; total Rs 11.80, rounded to Rs 12 [C04]
- refund/concession allowance 10% x 500 = Rs 50 [C05]
- tools per file: Rs 0 [C06, covered in fixed costs]
- COGS = 12 + 50 = Rs 62. Contribution per file = 500 - 62 = Rs 438.
- Gross margin = 438 / 500 = 87.6%.
- Founder time per file 0.75 hour, so contribution per founder production hour = 438 / 0.75 = Rs 584.

Customers in 3 months [C10]: Instagram 10 + groups 11 + Google 0 + referrals 0.15 x 21 = 3 (rounded) = 24.

Blended cash CAC:
- Instagram boost Rs 5,000 [C11] over 10 Instagram customers = Rs 500 per Instagram customer.
- Total cash acquisition spend Rs 5,000 / 24 customers = Rs 208 (rounded).
- Contribution after CAC = 438 - 208 = Rs 230 per customer.
- Payback = 208 / 438 = 0.48 months, so 0.5.

Founder hours (not cash). Content 3 hours a week x 13 weeks = 39 hours over 10 Instagram customers = 3.9 hours each. Group work 2 hours a week x 13 = 26 hours over 11 customers = 2.4 hours each. Production 24 x 0.75 = 18 hours. Total 83 hours of 130 available [C18]. Fits K2.

Paid-ad CAC [C08, C09]: CPC Rs 55 (top of the overall range) / 1% click-to-paid = Rs 5,500. Even at the Education CPC upper end of Rs 30, CAC = 30 / 0.01 = Rs 3,000. Both exceed the Rs 438 contribution, so paid ads are not usable in the conservative case. Base: 30 / 0.024 = Rs 1,250, above the base contribution of Rs 772 (799 - 27). Optimistic: 15 / 0.04 = Rs 375, below the contribution of Rs 1,484 (1,499 - 15). Paid ads work only in the optimistic case.

Capital to first revenue (conservative) [C06, C11, C12]: advocate review Rs 5,000 + first-month boost Rs 1,000 + tools/design Rs 500 = Rs 6,500.

3-month ledger (conservative):
- revenue 24 x 500 = Rs 12,000
- COGS 24 x 62 = Rs 1,488
- boost Rs 5,000
- tools 3 x 500 = Rs 1,500
- advocate review Rs 5,000
- net = 12,000 - 1,488 - 5,000 - 1,500 - 5,000 = -Rs 1,000 over the first 3 months
- Peak cash outlay before revenue offsets: 5,000 + 5,000 + 1,500 = Rs 11,500, well inside K1 Rs 1,00,000.

Break-even volume (conservative), monthly cash costs: tools Rs 500 + boost 5,000 / 3 = Rs 1,667 + advocate review amortised over 12 months 5,000 / 12 = Rs 417 = Rs 2,584. 2,584 / 438 = 5.9, so 6 files a month.

Steady month at the conservative volume of 8 files a month (24 over 3 months): 8 x 438 = 3,504 less costs 2,584 = Rs 920. This is about Rs 11,000 a year for roughly 28 founder hours a month (83 hours / 3).

Founder income check, informational only (the contract states no income target): a net of Rs 10,000 a month needs (10,000 + 2,584) / 438 = 29 files a month. At 0.75 hours each that is 22 production hours a month plus marketing hours, which uses nearly all of the 43 hours. It is about 3.6 times the conservative volume of 8.

Months to first revenue (conservative) [ASSUMPTION]: 2 weeks to set up the sheet template and the Instagram/WhatsApp profile, 1 week for the advocate review, 2 to 3 weeks until a first paid file from the groups. Total about 6 weeks, so 1.5 months.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital Rs 1,00,000 HARD | peak cash outlay about Rs 11,500 (Rs 6,500 to first revenue) | fits |
| K2 | 10 hours a week HARD | about 83 of 130 hours over 13 weeks (6.4 hours a week) | fits |
| K3 | skills (have) HARD: spreadsheets, social media marketing, English/Hindi/Marathi | work is a spreadsheet, templates and social posts; legal calculation and letter drafting are not among the stated skills | fits on listed skills; legal-drafting competence not stated |
| K4 | skills (can hire/learn) FLEXIBLE | advocate review Rs 5,000, inside the Rs 1,00,000 cap | fits. No stretch used |
| K5 | risk appetite low; cannot lose more than Rs 1,00,000 HARD | cash loss capped near Rs 11,500. Legal exposure (C13: drafting for pay may count as practice of law; unresolved by any source) is not capped by the model | fits on cash; legal exposure UNRESOLVED |
| K6 | first revenue within 3 months HARD | 1.5 months (6 weeks) | fits |
| K7 | B2C only HARD | individual students and parents pay | fits |
| K8 | off-limits: alcohol, gambling, crypto, MLM, food-safety or medical licence HARD | none involved | fits |
| K9 | keeps a full-time job HARD | work fits evening and weekend hours; employment-contract clauses on side income are unknown | fits [ASSUMPTION: employer permits side work] |

No FLEXIBLE stretch was used.

## Verdict inputs
- conservative unit economics positive: yes per file (contribution Rs 438 on Rs 500, Rs 230 after blended cash CAC). Monthly profit at steady state is about Rs 920 and the first 3 months net about -Rs 1,000. The result holds only on organic channels; paid ads have a CAC of Rs 5,500 against a contribution of Rs 438, so the business cannot scale by spending money.
- HARD constraints broken in conservative case: none on the model's numbers. K5 legal exposure is unresolved (C13), and K3 does not list legal drafting.
- FLEXIBLE stretches required: none
- what would have to change for the conservative case to work: the per-unit math works; the business-size math does not. Three numbers carry it. (1) Volume: a Rs 10,000 net month needs about 29 files a month against 8 modelled, about 3.6 times the conservative customer flow, with no Pune volume evidence (C14) and a free substitute at Rs 0 (C15). (2) Price: Rs 1,499 would cut the files needed to about 9, but no evidence supports that price. (3) Paid CAC would need to fall from Rs 5,500 to under about Rs 438, which needs click-to-paid conversion of about 12.5% at a Rs 55 CPC (or 6.8% at Rs 30), against 1% assumed. Separately, an advocate's written opinion that a non-lawyer may sell the product is needed before launch.
