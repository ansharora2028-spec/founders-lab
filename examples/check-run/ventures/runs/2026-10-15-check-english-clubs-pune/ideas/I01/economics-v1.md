---
run_id: 2026-10-15-check-english-clubs-pune
idea_id: I01
agent: economics-modeler
version: 1
created: 2026-10-15T10:30:13Z
---

## Inputs
Pune-specific sourced inputs are scarce (local-market coverage 3/10). Most cost inputs below are ASSUMPTION. Search snippets, not full pages, were read for the sourced external items; this is flagged per claim.

- [C01] price: ₹499 per member per month, paid by UPI; conservative = base = ₹499 (no discount), optimistic ₹599 [source: 00-contract.md "Starting point"; optimistic ₹599 is an ASSUMPTION: placement-prep positioning, untested]
- [C02] Willingness to pay ₹499 is untested. Substitutes: Toastmasters open clubs (dues not found), free language exchange, Duolingo Super about ₹150/month, SpeakX ₹299/month (national). In-person institutes ₹4,000-15,000/month, promotional sources [source: 01-local-market.md#C01, #C11, #C15, #C17; forge-v1.md#C03]
- [C03] Payment fee: Razorpay 2% platform fee on UPI plus 18% GST on the fee = 2.36% of transaction. Seen in search-result summaries of the page, payment-link rate not confirmed. (national) [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/]. Fee on ₹499 = ₹11.78.
- [C04] Materials (printed topic cards, feedback notes): ₹5 per member per session [ASSUMPTION: A4 print cost in India of a few rupees per page; unsourced]
- [C05] Café venue cost per 90-minute weekend session. Conservative ₹500 (hosting fee or minimum-spend shortfall paid by founder); base ₹0 (café gains from members' own orders); optimistic ₹0. No Pune café terms were found in 01-local-market.md#C23 or in a further search (results were non-Pune). [ASSUMPTION: pessimistic case assumes café wants compensation for occupying tables for 90 minutes]
- [C06] Members' own food/drink orders at the café are paid by members and are not a revenue or cost to the founder. [ASSUMPTION: per forge-v1.md#How it works step 3]
- [C07] Session pattern: 4 sessions per month (weekly) in conservative (maximises venue and time cost); 4 in base and optimistic. Paying members per group: conservative 8, base 10, optimistic 12 (trial attendees are not paying and add no revenue). [ASSUMPTION: forge-v1.md#C23 gives 8-12 per group and 2-4 sessions; the paying share of a group is not known]
- [C08] Facilitation by founder: no cash cost, 3 hours per session including travel and setup. [ASSUMPTION: forge-v1.md#How it works step 5]
- [C09] Freelance facilitator cost if hired: ₹1,000 per hour x 2 hours = ₹2,000 per session. The only rate found is a British Council freelance trainer posting at INR 1,000 per hour, about 2016, multi-city, not Pune-specific, read via search summary only (national, dated) [source: https://www.britishcouncil.in/about/jobs/freelance-trainer-0]. Two-hour duration is an ASSUMPTION (90-minute session plus travel).
- [C10] Instagram paid reach, India: CPC ₹6-55 in one 2026 agency guide (attribution to this URL inferred from search result; not opened) (national) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/]. Another guide reports ₹10-50 CPC. Facebook (not Instagram) education CPC in India about USD 0.09 (national) [source: https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/education/india]. Conservative uses ₹50 (top of range); base ₹25; optimistic ₹10 [ASSUMPTION: picks within the cited ranges]. Student-targeted lead-gen CPC in Pune is not sourced.
- [C11] Monthly churn (members not renewing): conservative 40%, base 25%, optimistic 15%. Average paying life = 1/churn: 2.5, 4, 6.7 months. [ASSUMPTION: no benchmark found; forge-v1.md#C25 also labels renewal unknown]
- [C12] Fixed monthly cash cost: conservative Instagram boost ₹3,000/month for 3.33 months (₹10,000 total over launch) plus tools ₹0 (free tiers of Google Forms/Sheets/WhatsApp/Luma). Base ₹2,500/month, optimistic ₹1,500/month [ASSUMPTION: forge-v1.md#C17 mentions ₹5,000-10,000 optional boosting]
- [C13] One-time registration or licence (Gumasta / Shops and Establishments): conservative ₹5,000, base ₹0, optimistic ₹0. Sources disagree on whether it is mandatory for a café-hosted service [source: 01-local-market.md#C21; amount is an ASSUMPTION]. GST is not due below ₹20 lakh turnover (national) [source: 01-local-market.md#C20]
- [C14] Conservative channel funnel (reach, conversion): lower than forge-v1.md#C16-C20, which are themselves all ASSUMPTION with no benchmark. Details in Calculations. [ASSUMPTION: no Pune benchmark]
- [C15] Referral reward: one free month (₹499 forgone) per 3 successful referrals; conservative 0.15 referred members per paying member, base 0.3 (forge-v1.md#C19) [ASSUMPTION]
- [C16] Pune student discretionary spend is unknown, so the ₹499 price cannot be checked against what students can spend [source: 01-local-market.md#C14]
- [C17] Currency is INR; no conversion used.

## Scenarios
| metric | conservative | base | optimistic |
|---|---|---|---|
| price | ₹499/member/month | ₹499 | ₹599 |
| COGS per unit (per member per month) | ₹282 (fee ₹11.78 + materials ₹20 + venue ₹250) | ₹32 (fee ₹11.78 + materials ₹20) | ₹34 (fee ₹14.14 + materials ₹20) |
| gross margin % | 43.5% | 93.6% | 94.3% |
| CAC: college WhatsApp/Instagram communities | ₹150 | ₹32 | ₹15 |
| CAC: Instagram boosted + organic reels | ₹2,721 | ₹625 | ₹250 |
| CAC: café partnership | ₹250 | ₹83 | ₹40 |
| CAC: member referrals | ₹166 (forgone revenue) | ₹166 | ₹100 |
| CAC: Luma/Meetup listings | ₹0 cash | ₹0 | ₹0 |
| blended CAC | ₹556 | ₹160 | ₹80 |
| payback period (months) | 2.6 | 0.3 | 0.15 |
| break-even volume (paying members/month) | 14 (1.75 groups of 8) | 6 | 3 |
| capital to first revenue | ₹13,333 | ₹4,500 | ₹2,500 |
| months to first revenue | 2 | 1 | 0.75 |

Customers acquired in 3 months: conservative about 24, base about 77 (forge-v1.md path, which itself falls short of 100), optimistic not modelled (ASSUMPTION: about 100). First 100 customers within 3 months is not reached in conservative or base.
Base and optimistic columns use unsourced or optimistic assumptions and carry no weight in a verdict.

## Calculations
Conservative column.

COGS per member per month:
- payment fee = 499 x 2.36% = ₹11.78 (C03)
- materials = ₹5 x 4 sessions = ₹20 (C04, C07)
- venue = ₹500 x 4 sessions / 8 paying members = ₹250 (C05, C07)
- COGS = 11.78 + 20 + 250 = ₹281.78, rounded ₹282
- gross profit per member = 499 - 282 = ₹217; gross margin = 217 / 499 = 43.5%

If a freelance facilitator replaces the founder: ₹2,000 x 4 / 8 = ₹1,000 per member per month on top of COGS (C09). Contribution = 217 - 1,000 = -₹783 per member. So groups cannot be scaled past the founder's own hours without losing money per member.

CAC by channel (3-month launch window, cash cost / paying customers; C14, C15):
1. College WhatsApp/Instagram communities: reach 2,000 students x 2% free trial = 40 trial x 25% pay = 10 customers. Cost: posters and QR flyers ₹1,500. CAC = 1,500 / 10 = ₹150.
2. Instagram boosted + organic: paid clicks = ₹10,000 / ₹50 CPC = 200 clicks x 10% register = 20. Organic reels reach 5,000 x 0.3% register = 15. Registrations 35 x 30% attend = 10.5 x 35% pay = 3.675 customers. CAC = 10,000 / 3.675 = ₹2,721.
3. Café partnership: 3 cafés x about 7 trial attendees = 20 trial x 30% pay = 6 customers. Cost: ₹500 goodwill snacks per café = ₹1,500. CAC = 1,500 / 6 = ₹250.
4. Referrals: base of 16 members x 0.15 = 2.4 referred customers. Reward: 2.4 / 3 = 0.8 free months x ₹499 = ₹399. CAC = 399 / 2.4 = ₹166.
5. Luma/Meetup: 2 customers, ₹0 cash CAC.
- Total customers = 10 + 3.675 + 6 + 2.4 + 2 = 24.075
- Total cost = 1,500 + 10,000 + 1,500 + 399 + 0 = ₹13,399
- Blended CAC = 13,399 / 24.075 = ₹556

Payback and lifetime value:
- payback = CAC / gross profit per member per month = 556 / 217 = 2.56 months
- paying life at 40% monthly churn = 1 / 0.40 = 2.5 months (C11)
- lifetime gross profit per member = 217 x 2.5 = ₹542.5
- LTV / CAC = 542.5 / 556 = 0.98. Payback (2.56 months) is longer than the average paying life (2.5 months), so a member does not pay back their CAC on average.

Break-even volume:
- fixed cash cost per month = ₹3,000 boosting (C12); tools ₹0. One-time ₹5,000 registration excluded from monthly figure.
- break-even members = 3,000 / 217 = 13.8, so 14 paying members, about 1.75 groups of 8 (two groups).
- Steady state with churn: holding 16 members (two groups) at 40% churn needs 6.4 new members per month x CAC ₹556 = ₹3,558/month. Gross profit from 16 members = 16 x 217 = ₹3,472/month. Net = 3,472 - 3,558 = -₹86/month before the ₹3,000 boost is separately counted (the boost is already inside CAC). So the model does not break even in steady state at conservative inputs, even with the founder unpaid.

Capital to first revenue (before the first ₹499 arrives):
- posters ₹1,500 + café goodwill ₹1,500 + first-month boost ₹3,333 + registration ₹5,000 + first-month venue 4 x ₹500 = ₹2,000 = ₹13,333
- Cumulative cash through month 3 (rough): costs = ads 10,000 + posters 1,500 + café 1,500 + registration 5,000 + venue 3 months x 2,000 = 6,000 + fees and materials about 500 = ₹24,500. Revenue assumed: month 2 about 6 members, month 3 about 10 members = 16 x 499 = ₹7,984. Net outlay about ₹16,500, maximum cumulative loss under 3 months far below ₹1,00,000. [ASSUMPTION: member ramp]

Months to first revenue (conservative) = 2: month 1 for café negotiation, posters and a free trial session; first UPI payments at the end of the trial in month 2 [ASSUMPTION].

Founder hours (K2) in conservative case:
- one group (8 members): 1 session 3h + prep 2h + marketing 2h + admin 1h + café relations 1h = 9h/week. Gross profit 8 x 217 = ₹1,736/month, below the ₹3,000 fixed boost cost, so loss.
- two groups (needed to pass break-even at 14-16 members): 2 sessions 6h + prep 2h + marketing 2h + admin 1h + café 1h = 12h/week, above 10h.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital ₹1,00,000 HARD | about ₹24,500 gross spend over 3 months, ₹13,333 before first revenue | fits |
| K2 | 10 hours/week HARD | 9h at one group (loss-making); 12h at two groups (needed for break-even 14 members) | BREAKS |
| K3 | skills (have) HARD | spreadsheets, social marketing, language skills are used; no teaching qualification (forge-v1.md#C24 untested) | fits |
| K4 | skills (can hire/learn) FLEXIBLE | hiring a facilitator not used, because it costs ₹1,000 per member and makes margin negative; stretch not used | fits (no stretch used) |
| K5 | risk: cannot lose more than ₹1,00,000 HARD | maximum cumulative loss about ₹16,500-25,000 in 3 months | fits |
| K6 | time to first revenue 3 months HARD | 2 months | fits |
| K7 | B2C only HARD | students pay personally | fits |
| K8 | off-limits categories HARD | none touched; members buy their own food, founder sells no food | fits |
| K9 | keeps full-time job HARD | weekend sessions only; weekday marketing and admin fit outside job hours at 9h but not 12h | fits at 9h, see K2 |

## Verdict inputs
- conservative unit economics positive: no. Gross margin is 43.5%, but blended CAC ₹556 against lifetime gross profit ₹542.5 gives LTV/CAC 0.98, payback 2.56 months exceeds average paying life 2.5 months, and steady-state monthly net is about -₹86 at the 16-member ceiling. Result is close to break-even and depends on unsourced ASSUMPTIONS (venue fee, churn, funnel rates, Instagram CPC), not on sourced figures. The result could flip with café fee ₹0 or lower churn; neither is supported by evidence found.
- HARD constraints broken in conservative case: K2 (12h/week needed to reach break-even volume vs 10h)
- FLEXIBLE stretches required: none (K4 not used)
- load-bearing unverified items: willingness to pay ₹499 (no Pune evidence), café venue terms, renewal rate, student reach and conversion, and whether Instagram boosting reaches Pune students at ₹50 CPC. Demand evidence (existing spend on costlier institutes) lives in 01-local-market.md#L01, not in this file.
