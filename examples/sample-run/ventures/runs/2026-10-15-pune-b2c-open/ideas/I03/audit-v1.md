---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: evidence-auditor
version: 1
created: 2026-10-15T13:00:00Z
---

## Scope
- files audited: 00-contract.md; 01-local-market.md; 02-signals.md; ideas/I03/kill-criteria.md; ideas/I03/forge-v1.md; ideas/I03/economics-v1.md; ideas/I03/prosecution-market-v1.md; ideas/I03/prosecution-execution-v1.md (verdict not read)
- claims in scope: about 100 (claim bullets and signal rows, including ASSUMPTION-labeled ones), checked: 18 rows covering 15 distinct URLs plus economics arithmetic and unsourced facts, sample method: all economics inputs with URLs + all FATAL-flaw evidence (FE1: OLX, digirake) + demand-evidence claims + random sample of the rest
- tool failure notice: every WebFetch call this round returned "proxy refused the connection" (17 calls, 15 distinct hosts, plus one retry on 3 URLs). No page content was obtained. No claim could be verified or contradicted by its source. Each URL-backed claim below is labeled UNREACHABLE (tool failure) as the rules require after a second attempt. These labels say nothing about whether the sources are correct. A re-audit with a working fetch tool is the only way to restore any of these claims.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C02 | Razorpay 2% + 18% GST = 2.36% (national) | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ | UNREACHABLE | tool failure, 2 attempts. Economics input. |
| economics-v1.md#C02 | UPI MDR 0% vs 0.4% above ₹2,000 from 2026-10-15 | none | UNSOURCED | Factual statement with no URL and no ASSUMPTION label. The file itself says "not verified". |
| economics-v1.md#C04 | Meta ads CPC India ₹34 (Vaizle) | https://insights.vaizle.com/facebook-ads-cost/ | UNREACHABLE | tool failure, 1 attempt. Economics input (conservative CAC test row). The "about ₹1 to ₹34 range" has no URL. |
| economics-v1.md#C04 | Meta ads CPC ₹8-25 (OwlClaw) | https://owlclaw.com/benchmarks/meta-ads-benchmarks-india | UNREACHABLE | tool failure, 1 attempt. |
| economics-v1.md#C10 | DPDP applies to seller phone numbers and photos (national) | https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/ | UNREACHABLE | tool failure, 1 attempt. Same URL backs forge-v1.md#C16 and 01#C19. The ₹5,000 legal cost is an ASSUMPTION. |
| economics-v1.md#C11 | GST threshold ₹20 lakh for services; Section 24 categories (national) | https://razorpay.com/learn/gst-registration-limits/ | UNREACHABLE | tool failure, 1 attempt. Basis for modelling no GST. |
| economics-v1.md Calculations 1-12, scenario table | Conservative arithmetic | n/a | VERIFIED (arithmetic) | Recomputed: ₹149.25 to ₹149; fee ₹3.52; refund ₹14.90; COGS ₹18.42; margin ₹130.58 (87.6%); 52 customers; cash CAC 3,750/52 = ₹72.1; boost CAC ₹3,400; ₹438 loaded CAC; net ₹1,040; break-even 8 listings and 81 listings. Base and optimistic columns also recompute. |
| economics-v1.md Calculation 13 and K2/K9 rows | Peak load about 6.8 h/week | n/a | MISREPRESENTED | Arithmetic is internally inconsistent. economics-v1.md#C06 puts the 52 customers and #C13 puts the 37.5 acquisition hours in the 8 charging weeks, after the 10-week community build. Calc 13 instead overlays acquisition hours on build weeks 1-10. Charging-window load is 63.5 h / 8 weeks = about 7.9 h/week (also computed by prosecutor-execution). Still under K2's 10 h, but 6.8 is wrong. Struck as a self-contradicting calculation. |
| forge-v1.md#C08, prosecution-execution-v1.md#C01 | OLX free ads capped per category, example 2 furniture ads per 60 days (national) | https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/ | UNREACHABLE | tool failure, 2 attempts. Evidence for FATAL flaw FE1. prosecution-market-v1.md says its own fetch of this page also failed. |
| forge-v1.md#C02/#C03, prosecution-execution-v1.md#C02, prosecution-market-v1.md#C01/#C06 | Pune seller channels (OLX, Quikr, FB, RWA groups, dealers at Bohri Ali, Hadapsar, Camp); tempo cost ₹500-1,500 | https://knowledge.digirake.com/sofa/sell-old-sofa-pune | UNREACHABLE | tool failure, 1 attempt. Evidence for FE1 (FATAL) and several FIXABLE flaws. Source is described by all files as an unverified affiliate blog. |
| 01-local-market.md#C01, forge-v1.md#C01/#C05, kill-criteria raw idea | Rentomojo ₹2,199/month plan, ₹50,000 setup cost, named corridor areas | https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399 | UNREACHABLE | tool failure, 1 attempt. 01-local-market.md states its own fetch failed and the content comes from a search-result summary. Cited as the problem and persona basis. |
| 01-local-market.md#C03 | Co-living demand in Hinjewadi and Kharadi; Metro Yellow Line | https://www.colive.com/blog/blog-pg-in-hinjewadi-pune-cost-guide-2026/ | UNREACHABLE | tool failure, 1 attempt. |
| 01-local-market.md#C13 | Rentomojo ₹2,199 is the only Pune rental price point | none | UNSOURCED | Restates C01 with no URL of its own. Derived from C01, so it follows C01's status. |
| 02-signals.md#C03 | Pune societies report altered or unregistered rent agreements (2025-08) | https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/ | UNREACHABLE | tool failure, 1 attempt. |
| prosecution-market-v1.md#C03 | Paid-listing share of Indian online classifieds 10.0% in 2025 (national) | https://www.kenresearch.com/industry-reports/india-online-classifieds-market | UNREACHABLE | tool failure, 1 attempt. Used as KM1 context; the only listing-fee demand figure in the files. |
| prosecution-market-v1.md#C02 | Zefo buy-back model, Bengaluru; Quikr acquired it April 2019 for about ₹210 crore (other city: Bengaluru) | https://yourstory.com/2017/10/pre-owned-goods-marketplace-zefo-raises-rs-60-crore-series-b | MISREPRESENTED | The cited page is dated 2017-10 and cannot support an April 2019 acquisition or its price. The claim itself says the acquisition detail came from a search summary and was not opened. The 2017 funding and buy-back description could not be fetched (tool failure). Whole claim struck. |
| prosecution-market-v1.md#C05 | Used bed frames resell at 10-15% of purchase price (national) | https://smb.orangeleader.com/article/Rentomojos-Bed-and-Mattress-Rentals-Rise-in-Bangalore-in-2026-as-Renters-Reject-indian-rupee50000-Upfront-Costs-and-Weak-Resale-Probability-for-indian-rupee1000Month-Rentomojo-Plans/6a2f127945b635ab6be4e00a | UNREACHABLE | tool failure, 1 attempt. Basis for FM2. |
| prosecution-market-v1.md#C07 | Move Loot shut down 2016 (global) | https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-sells-customer-list-to-handy | UNREACHABLE | tool failure, 2 attempts. |
| prosecution-market-v1.md#C08 | Kaiyo wind-down Aug 2024 after seller payout complaints (global) | https://www.modernretail.co/operations/online-furniture-platform-kaiyo-says-it-will-wind-down-by-the-end-of-the-month-after-sellers-file-complaints/ | UNREACHABLE | tool failure, 1 attempt. |

Not checked (outside the sample): the remaining sourced claims in 01-local-market.md (C02, C05-C08, C10-C12, C14-C22), 02-signals.md (S01-S09 and the other C-claims), forge-v1.md#C06/#C07, prosecution-market-v1.md#C04/#C09/#C10, prosecution-execution-v1.md#C03-C07. They carry no label from this audit. Because all fetches failed, a larger sample would not have produced different results.

## Struck claims
- economics-v1.md#C02 (Razorpay 2.36%) — UNREACHABLE — tool failure, no page content.
- economics-v1.md#C02 (UPI MDR statements) — UNSOURCED — no URL, no ASSUMPTION label.
- economics-v1.md#C04 (Meta CPC ₹34, ₹8-25) — UNREACHABLE — tool failure on both URLs.
- economics-v1.md#C10 (DPDP applicability, Seqrite) — UNREACHABLE — tool failure. Also affects forge-v1.md#C16 and 01-local-market.md#C19 (same URL).
- economics-v1.md#C11 (GST threshold) — UNREACHABLE — tool failure.
- economics-v1.md Calculation 13 and the K2/K9 "6.8 h/week" values — MISREPRESENTED — acquisition hours were placed in the wrong weeks; charging-window load is about 7.9 h/week.
- forge-v1.md#C08 and prosecution-execution-v1.md#C01 (OLX free-ad cap) — UNREACHABLE — tool failure; evidence for FATAL flaw FE1.
- forge-v1.md#C02, #C03, prosecution-execution-v1.md#C02, prosecution-market-v1.md#C01 and #C06 (digirake Pune guide) — UNREACHABLE — tool failure; evidence for FE1 (FATAL) and for FM1, FM2.
- 01-local-market.md#C01, forge-v1.md#C01, #C05 (Rentomojo ₹2,199, ₹50,000) — UNREACHABLE — tool failure; scout also never read the page.
- 01-local-market.md#C03 (Colive) — UNREACHABLE — tool failure.
- 01-local-market.md#C13 — UNSOURCED — no URL.
- 02-signals.md#C03 (Pune rent agreements) — UNREACHABLE — tool failure.
- prosecution-market-v1.md#C02 (Zefo, Quikr acquisition) — MISREPRESENTED — 2017 source cannot support a 2019 deal.
- prosecution-market-v1.md#C03 (Ken Research 10.0%) — UNREACHABLE — tool failure.
- prosecution-market-v1.md#C05 (bed-frame 10-15%) — UNREACHABLE — tool failure.
- prosecution-market-v1.md#C07 (Move Loot) — UNREACHABLE — tool failure.
- prosecution-market-v1.md#C08 (Kaiyo) — UNREACHABLE — tool failure.

Struck claims that are load-bearing: every economics input with a URL (C02, C04, C10, C11) and the arithmetic in Calculation 13; the sole evidence for FATAL flaw FE1 (OLX cap, digirake guide). The Judge should note that all strikes except economics Calculation 13, economics#C02 (MDR), 01#C13 and the Zefo claim are tool-failure strikes and do not indicate that the sources are wrong.

## Assumptions in load-bearing positions
- economics-v1.md#C01 — ASSUMPTION (₹149 conservative price, 25% discount) used as the basis of the conservative unit-economics result.
- economics-v1.md#C03 — ASSUMPTION (10% refunds) used as a conservative COGS input.
- economics-v1.md#C05 — ASSUMPTION (1% click-to-paid) used for the paid-acquisition test row.
- economics-v1.md#C06 — ASSUMPTION (52 customers in 8 charging weeks) used as the basis of blended CAC, net result and the cash-positive finding.
- economics-v1.md#C07, #C09, #C10 (setup and fixed costs), #C12 and #C13 (hours), #C16 (12 weeks to first revenue, K6 status) — ASSUMPTION used as conservative inputs and constraint-check results.
- forge-v1.md#C10 (sellers pay ₹199 despite free OLX and Facebook) — ASSUMPTION used as the basis of every market criterion's status and of FM1.
- forge-v1.md#C11, #C12, #C13, #C14 — ASSUMPTION (move-out volume, buyer preference for used, community build rate, handling time) used as the basis of KM3, KM4, FE4 and the path to 100 customers.
- 01-local-market.md#C04 and #C09 — ASSUMPTION; C09 presents a factual figure (Pune GDP and per capita income) with no URL.

## Summary
- verified: 1 (economics arithmetic, scored as a single check), misrepresented: 2, unreachable: 14 (of which tool failure: 14), unsourced: 2
- demand evidence surviving the audit: none. The only candidate items are the Rentomojo rental price point (01#C01, a rental incumbent's marketing, not seller-fee demand), the Ken Research paid-listing share (prosecution-market-v1.md#C03) and the Zefo acquisition (prosecution-market-v1.md#C02). All three are struck.
