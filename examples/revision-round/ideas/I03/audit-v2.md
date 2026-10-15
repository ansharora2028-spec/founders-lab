---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: evidence-auditor
version: 2
created: 2026-10-15T14:00:00Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I03/kill-criteria.md, ideas/I03/diff-v2.md, ideas/I03/forge-v2.md, ideas/I03/economics-v2.md, ideas/I03/prosecution-market-v2.md, ideas/I03/prosecution-execution-v2.md (verdict files not read)
- claims in scope: about 110 (all claim bullets plus economics inputs and diff rows), checked: 28 distinct claim checks (all economics-v2 URL-sourced inputs, the conservative arithmetic, all FATAL-flaw evidence (FE1), all demand evidence (Quikr, MagicBricks/99acres, OLX), all diff-row evidence URLs D2 and D3, plus a sample of other sourced claims)
- sample method: all economics inputs + all FATAL-flaw evidence + all demand evidence + all diff-row URLs + sample of the rest
- fetch environment: every WebFetch call to every host returned "proxy refused the connection", including a retry on two URLs. This is a tool or environment failure, not evidence about the sources. Every URL-backed check below is therefore UNREACHABLE (tool failure) and struck under rule 8.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v2.md#C01 | Conservative price ₹110 from Quikr Top of Page rate (Mobile/Electronics, undated deck) | https://www.slideshare.net/slideshow/quikr-ecomm-platform/75732007 | UNREACHABLE (tool failure) | Retry not different. File itself says "not re-opened" and undated, other category. Conservative price input is struck. |
| economics-v2.md#C02 | Razorpay 2% + 18% GST = 2.36% | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ | UNREACHABLE (tool failure) | Marked "carried", not re-opened by modeler. |
| economics-v2.md#C02 | UPI MDR statements conflict (0% vs 0.4% above ₹2,000 from 2026-10-15) | none | UNSOURCED | Specific factual claim with a date and rate, no URL, no ASSUMPTION label. |
| economics-v2.md#C04 | Meta CPC India conservative ₹34, range ₹1 to ₹34 | https://insights.vaizle.com/facebook-ads-cost/ | UNREACHABLE (tool failure) | Carried. |
| economics-v2.md#C04 | same CPC claim, second source | https://owlclaw.com/benchmarks/meta-ads-benchmarks-india | UNREACHABLE (tool failure) | Carried. |
| economics-v2.md#C10 | Consumer Protection (E-Commerce) Rules duties | https://www.indialaw.in/blog/consumer-protection-e-commerce-rules/ | UNREACHABLE (tool failure) | Not re-opened by modeler. |
| economics-v2.md#C10 | Same Rules, law-firm summary | https://khaitanco.com/thought-leaderships/Stricter-Regulations-on-E-Commerce-The-Consumer-Protection-E-Commerce-Rules-2020 | UNREACHABLE (tool failure) | Not re-opened by modeler. |
| economics-v2.md#C10 (also forge-v2.md#C16) | DPDP applies to collecting phone numbers and photos | https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/ | UNREACHABLE (tool failure) | Carried. |
| economics-v2.md#C12 | GST registration above ₹20 lakh for services | https://razorpay.com/learn/gst-registration-limits/ | UNREACHABLE (tool failure) | Retried once. Carried. |
| economics-v2.md Calculations 1-11, 13-15 and Constraint check | Conservative arithmetic (margin ₹96.40 and 87.6%, 52 customers, CAC ₹72.1, boost ₹3,400, loaded CAC ₹438, capital ₹22,300, net ₹2,263, position -₹20,037, break-even 11 and 232, payback 17.1 months, 7.75 h/week, 2.8 months) | economics-v2.md itself | VERIFIED | Recomputed; all conservative figures reproduce from the stated inputs (rounding only). |
| economics-v2.md Calc 12 vs Inputs C12 | GST-inclusive sensitivity margin | economics-v2.md itself | MISREPRESENTED | Inputs C12 says margin falls to ₹79.3; Calc 12 computes ₹81.7 (and says "approx ₹79-82"). Self-contradiction. Sensitivity only, not the conservative column. |
| economics-v2.md Scenarios, payback row (base and optimistic) | Base sunk payback "about 4 months", optimistic "about 1.5 months" | economics-v2.md itself | MISREPRESENTED | The file's own note computes base about 1.1 months and calls table figures "rough and not sourced". Not the conservative column. |
| prosecution-execution-v2.md#C01 (FE1, FATAL) | Quikr offers free ads and two paid Premium tiers; no price found | https://quikr.com/html/premium_ads.php | UNREACHABLE (tool failure) | FATAL-flaw evidence. |
| prosecution-execution-v2.md#C02 (FE1, FATAL) | Quikr terms: paid monies non-refundable, unused credits forfeited | https://www.quikr.com/services/termsandconditions | UNREACHABLE (tool failure) | Retried once. Also cited by forge-v2.md#C19. |
| diff-v2.md D2 / forge-v2.md#C20 | Quikr ₹199-₹499 per 30 days (about 2018 complaint post) | https://www.linkedin.com/pulse/aware-quikr-fraud-ankit-jain | UNREACHABLE (tool failure) | Demand evidence. Market prosecutor also could not confirm this range. |
| diff-v2.md D2 / forge-v2.md#C21-C22 | MagicBricks about ₹1,463 / 60 days, 99acres about ₹974 / 90 days | https://www.leadsquared.com/real-estate-leads-online-india | UNREACHABLE (tool failure) | Demand evidence; real-estate category, vendor page, undated. |
| diff-v2.md D3 / forge-v2.md#C23, C26 | Marketplace duties; summaries disagree | https://www.mondaq.com/india/dodd-frank-consumer-protection-act/976876/e-commerce-rules-2020 | UNREACHABLE (tool failure) | Diff-row evidence. |
| diff-v2.md D3 / forge-v2.md#C24 | Grievance officer, 48 hours / one month | https://www.indialaw.in/blog/consumer-protection-e-commerce-rules/ | UNREACHABLE (tool failure) | Diff-row evidence. |
| diff-v2.md D3 / forge-v2.md#C25 | Nodal contact, seller undertaking, no auto-consent | https://khaitanco.com/thought-leaderships/Stricter-Regulations-on-E-Commerce-The-Consumer-Protection-E-Commerce-Rules-2020 | UNREACHABLE (tool failure) | Diff-row evidence. |
| forge-v2.md#C08 | OLX limited free ads, example 2 furniture ads per 60 days | https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/ | UNREACHABLE (tool failure) | Free-substitute evidence. |
| forge-v2.md#C02, C03 | Sellers try OLX/Quikr first; FB Marketplace and RWA groups active in Hinjewadi/Magarpatta; dealers pay cash | https://knowledge.digirake.com/sofa/sell-old-sofa-pune | UNREACHABLE (tool failure) | Forge itself calls it an unverified affiliate blog. |
| forge-v2.md#C04 | 30-60% resale recovery, ₹4,000-7,000 study table | https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune | UNREACHABLE (tool failure) | Forge itself notes unsourced figures. |
| forge-v2.md#C01, C05; 01-local-market.md#C01 | Rentomojo from ₹2,199/month; ₹50,000 setup; named clusters | https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399 | UNREACHABLE (tool failure) | 01-local-market.md states its own fetch also failed and used a search summary only. |
| forge-v2.md#C06 | Rentomojo ₹149/month headline vs about ₹600 fridge Pune | https://pr.thebeenews.com/article/Rentomojo-Refrigerator-and-Dining-Table-Rentals-Rise-Across-Pune-as-IT-Professionals-Avoid-EMI-Lock-Ins-and-indian-rupee40000-Setup-Costs/6a28544e5f1a393667890e53 | UNREACHABLE (tool failure) | |
| forge-v2.md#C07 | ₹50,000 furnishing cost; "near-total resale loss" | https://smb.winchestersun.com/article/Dining-Table-Rentals-Rise-Across-Pune-Delhi-and-Noida-in-2026-as-indian-rupee18000-Setup-Costs-and-Near-Total-Resale-Loss-Push-Households-Toward-indian-rupee495-a-Month-Plans-From-Providers-Such-as-Rentomojo/6a7a26652e905784f149ac06 | UNREACHABLE (tool failure) | Headline mentions ₹18,000 dining setup; the ₹50,000 figure is not visible from the URL text. Unconfirmed. |
| prosecution-market-v2.md#C03 | Quikr premium complaint dated 2026-03-09 | https://voxya.com/consumer-complaints/no-premium-service-after-payment/260792 | UNREACHABLE (tool failure) | Prosecutor says seen in search results only. |
| 01-local-market.md#C12 | 82% would not pay over ₹200/hour for instant home services (national) | https://redseer.com/articles/tapping-into-the-everyday-instant-home-services-and-the-next-habit-loop/ | UNREACHABLE (tool failure) | Sample item. |
| 02-signals.md#C05 | UPI 24.07B transactions Sept 2026, +23% YoY (national) | https://startuptalky.com/upi-transactions-september-2026/ | UNREACHABLE (tool failure) | Sample item. |

## Struck claims
- economics-v2.md#C01 (conservative price ₹110 anchored to Quikr deck) — UNREACHABLE (tool failure) — price anchor not confirmed; the ₹199/₹99 base is an ASSUMPTION and not struck.
- economics-v2.md#C02 (Razorpay 2.36%) — UNREACHABLE (tool failure) — payment-fee input unconfirmed.
- economics-v2.md#C02 (UPI MDR 0% vs 0.4% from 2026-10-15) — UNSOURCED — dated factual claim with no source.
- economics-v2.md#C04 (Meta CPC ₹34 and range) — UNREACHABLE (tool failure) — both URLs.
- economics-v2.md#C10 (law-firm Rules summaries, DPDP applicability) — UNREACHABLE (tool failure).
- economics-v2.md#C12 (GST ₹20 lakh threshold) — UNREACHABLE (tool failure).
- economics-v2.md Calc 12 / Inputs C12 (GST sensitivity margin ₹79.3 vs ₹81.7) — MISREPRESENTED — contradicts the file's own arithmetic.
- economics-v2.md Scenarios payback row for base and optimistic ("about 4 months", "about 1.5 months") — MISREPRESENTED — contradicts the file's own note (1.1 months).
- prosecution-execution-v2.md#C01, #C02 (FE1 FATAL evidence) — UNREACHABLE (tool failure).
- diff-v2.md D2 evidence (slideshare, linkedin, leadsquared) — UNREACHABLE (tool failure); forge-v2.md#C19-C22 likewise.
- diff-v2.md D3 evidence (indialaw, khaitan, mondaq) — UNREACHABLE (tool failure); forge-v2.md#C23-C26 likewise.
- forge-v2.md#C01-C08 URL-backed claims (irontontribune, digirake x2, thebeenews, winchestersun, OLX) — UNREACHABLE (tool failure).
- 01-local-market.md#C01 and #C12 — UNREACHABLE (tool failure).
- 02-signals.md#C05 — UNREACHABLE (tool failure).
- prosecution-market-v2.md#C03 (voxya) — UNREACHABLE (tool failure). #C04 voxya URLs were not separately opened; same host, treated as UNREACHABLE (tool failure).
- Tool-failure strikes: 24. These stem from a fetch-environment refusal on every host. The Judge applies rule 8 regardless; the main session may re-run the audit with working network access.

## Assumptions in load-bearing positions
- economics-v2.md#C01 — ₹199 / ₹99 prices are ASSUMPTION; the file states willingness to pay is unevidenced (basis of conservative input and of KM1/FE1).
- economics-v2.md#C06 — conservative paying-seller counts (52) are ASSUMPTION; basis of CAC, operating net and payback.
- economics-v2.md#C03 — 10% refund rate is ASSUMPTION; conflicts with Quikr's non-refundable terms per prosecution-execution-v2.md#C02 (itself struck here).
- economics-v2.md#C09, #C11, #C13, #C14, #C15, #C16 — fixed cost, one-offs, handling time, acquisition hours, operator rate, repeat rate are all ASSUMPTION.
- economics-v2.md#C10 and forge-v2.md#C27 — compliance cost (₹15,000 lawyer, 10 hours) is ASSUMPTION; drives sunk capital ₹22,300 and KE4.
- economics-v2.md#C17 and forge-v2.md#C13 — 300-500 member gate and 12-week timeline to first revenue are ASSUMPTION; basis of K6 "fits (thin margin)".
- forge-v2.md#C10, #C11, #C12 — seller willingness to pay, move-out volume, buyer preference for used over rental are ASSUMPTION; basis of KM1, KM3, KM4 status.
- forge-v2.md#C15, #C17 — no licence needed; WhatsApp commercial-group terms unchecked (ASSUMPTION), basis of KE3/KE4.
- forge-v2.md Path to first 100 customers — all conversion rates ASSUMPTION; no sourced numbers.
- 01-local-market.md#C04 — absence of Pune shutdowns is ASSUMPTION.

## Summary
- verified: 1, misrepresented: 2, unreachable: 24 (of which tool failure: 24), unsourced: 1
- the one VERIFIED item is the internal arithmetic of the conservative column in economics-v2.md; no external URL could be verified.
- demand evidence surviving the audit: none (Quikr paid-tier rates, MagicBricks/99acres packages and Quikr complaint posts are all UNREACHABLE (tool failure); MagicBricks/99acres are also a different category and Quikr rates are undated and not furniture)
