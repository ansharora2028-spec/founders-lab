---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: evidence-auditor
version: 1
created: 2026-10-15T19:00:00Z
---

## Scope
- files audited: 00-contract.md; 01-local-market.md; 02-signals.md; ideas/I03-P1/kill-criteria.md; forge-v1.md; economics-v1.md; prosecution-market-v1.md; prosecution-execution-v1.md (all under <project>/ventures/runs/2026-10-15-pune-b2c-open/). The verdict was not read.
- claims in scope: about 95 (approximate count of claim bullets), checked: 47 rows below, sample method: all economics inputs + all FATAL-flaw evidence + all demand-evidence claims + all sourced claims in forge and both prosecutions + a sample of 01/02 claims
- ENVIRONMENT NOTE: every WebFetch call in this session (about 25 calls, 22 distinct URLs on about 17 hosts, with a second attempt on two of them) returned "proxy refused the connection". This is a tool failure, not evidence about the sources. Under rule 8 these claims are struck anyway. No source text was read, so no claim could be marked VERIFIED on the strength of a source page. Rows marked VERIFIED are checks of arithmetic or file-internal references only.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 | conservative avg sale price ₹3,000; resale ranges | https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1 | UNREACHABLE (tool failure) | Economics itself also labels it ASSUMPTION; load-bearing (sets commission at ₹300) |
| economics-v1.md#C04 | Razorpay 2% + 18% GST; UPI MDR 0%; 90-day 0% fee | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ ; https://razorpay.com/blog/upi-charges-explained-mdr-vs-platform-fees/ | UNREACHABLE (tool failure) | Economics admits pages were never opened |
| economics-v1.md#C08 | Meta India CPC/CPM ranges, Q4 uplift 30-60%, Reels cheaper | https://insights.vaizle.com/facebook-ads-cost/ ; https://upgrowth.in/?p=27575 ; https://owlclaw.com/benchmarks/meta-ads-benchmarks | UNREACHABLE (tool failure) | Economics admits pages never opened; basis of ₹300 CPM and ₹2,400 Instagram CAC |
| economics-v1.md#C11 | brokers see move-outs (agents handle leave-and-licence PDFs) | https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/ | UNREACHABLE (tool failure) | Retried once |
| economics-v1.md#C13 | S&E: under 10 workers file intimation, free | https://www.registerkaro.in/post/gumasta-license-fees ; https://www.keka.com/compliance/forms/maharashtra-shop-and-establishment-registration | UNREACHABLE (tool failure) | Economics admits search summary only |
| economics-v1.md Calculations steps 1-11 (conservative) | commission ₹120/sale, margin 97.6%, -152% time-loaded, CAC ₹1,064 / ₹1,627, payback 9.1, break-even 8.5, net -₹22,438, capital ₹10,500, 9.2 h/week, ₹262 without Instagram | economics-v1.md | VERIFIED | Recomputed by hand: every conservative figure is correct (e.g. 21,281/20 = 1,064; 2,343 - 24,781 = -22,438; 120/13 = 9.2). Inputs are assumptions; the arithmetic is sound |
| economics-v1.md Scenarios, optimistic column | optimistic gross margin incl. time 70%; blended cash CAC ₹89; Instagram CAC ₹133 | economics-v1.md | MISREPRESENTED | Recomputed: (497.96 - 150)/510 = 68.2%, not 70%. From the file's own optimistic inputs, cash CAC is about ₹73 (9,500/130 sales) and Instagram CAC about ₹167 (6,000/36). File says optimistic is rough and not counted toward PASS. Not load-bearing; conservative column unaffected |
| economics-v1.md Calculations step 6 | "A seller transacts once on leaving (forge-v1 persona)"; payback not reached | economics-v1.md | UNSOURCED | Forge-v1 persona (#C01) does not state one-time use; no source and no ASSUMPTION label. Load-bearing for the "payback not reached" result. Cash contribution (₹117) vs CAC (₹1,064) arithmetic itself stands |
| forge-v1.md#C01 | persona: IT/office tenants in six areas; Rentomojo article | https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399 | UNREACHABLE (tool failure) | 01-local-market.md also reports its own fetch of this page failed |
| forge-v1.md#C02 | Rentomojo from ₹2,199/month; ~₹50,000 setup cost | same URL | UNREACHABLE (tool failure) | Same page as above |
| forge-v1.md#C03 | sellers use OLX, Quikr, FB Marketplace, Sulekha, JustDial, dealers | https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1 | UNREACHABLE (tool failure) | |
| forge-v1.md#C04 | 30-60% recovery; Nilkamal wardrobe ₹5,000-9,000 | same URL | UNREACHABLE (tool failure) | Basis of price range used by economics and KM2 |
| forge-v1.md#C05 | Cashify and others offer quote and free pickup in Pune areas | https://knowledge.digirake.com/home-living/washing-machine/sell-old-washing-machine-pune?amp=1 | UNREACHABLE (tool failure) | |
| forge-v1.md#C06 | OLX revenue is ads; featured listing ₹150-₹500 | https://yespress.io/olx-india | UNREACHABLE (tool failure) | Forge says figure came from a search summary, not the page |
| forge-v1.md#C09 | Pune resale guides exist, advise multi-platform listing | https://knowledge.digirake.com/study-table/sell-old-study-table-pune?amp=1 | UNREACHABLE (tool failure) | |
| forge-v1.md#C10 | commission ₹500-900 on ₹5,000-9,000 wardrobe; ₹200-400 on ₹2,000-4,000 study table/chair | cites "arithmetic on C04" | UNSOURCED | The wardrobe arithmetic is correct. The ₹2,000-4,000 study table/chair price has no source in C04 and no ASSUMPTION label |
| forge-v1.md#C11 | agents handle leave-and-licence PDFs so see move-outs | https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/ | UNREACHABLE (tool failure) | Retried once |
| forge-v1.md Path section | UPI 24.07 bn transactions Sept 2026 | https://startuptalky.com/upi-transactions-september-2026/ | UNREACHABLE (tool failure) | Same figure appears in 02-signals S02/C05 |
| forge-v1.md Path table | channels sum to roughly 90 completed sales | forge-v1.md | VERIFIED | 44.6 + 19.8 + 10 + 15 = about 90; all inputs ASSUMPTION |
| forge-v1.md#C14, #C17, #C07, Moat (used by prosecution-execution#C08) | seller willingness to pay unevidenced; severity unproven; moat "None yet" | forge-v1.md | VERIFIED | Text present in forge-v1 as quoted |
| prosecution-market-v1.md#C01 | Cashify FY25 operating revenue ~₹1,096 cr, net loss ~₹10.5 cr | https://inc42.com/buzz/cashify-trims-loss-by-80-to-inr-11-cr-in-fy25/ | UNREACHABLE (tool failure) | Retried once. Demand-evidence candidate (also dominated by phones per the claim itself) |
| prosecution-market-v1.md#C02 | Furlenco FY25 revenue ~₹240 cr (+59%), profit ₹3.1 cr | https://startupfeed.in/furlenco-turns-profitable-fy25-rs-240-crore-revenue/ | UNREACHABLE (tool failure) | Demand-evidence candidate (rental, not resale) |
| prosecution-market-v1.md#C03 | Rentomojo FY25 revenue ₹266 cr (unattributed) | https://indianretailer.com/news/furlenco-reports-strong-growth-and-profit-turnaround-fy25 | UNREACHABLE (tool failure) | Prosecutor already calls it unverified |
| prosecution-market-v1.md#C04 | Pune sofa/fridge resale ranges | https://knowledge.digirake.com/sofa/sell-old-sofa-pune?amp=1 ; https://knowledge.digirake.com/refrigerator/sell-old-refrigerator-pune?amp=1 | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C05 | OLX/Quikr catalysts; Quikr Doorstep for trust/payment/logistics | https://uniquebusinessmodels.substack.com/p/23-how-do-used-good-marketplaces | UNREACHABLE (tool failure) | Evidence for FATAL FM1 |
| prosecution-market-v1.md#C06 | Zefo raised $16-19M, acquired by Quikr 2019 for ~₹200 cr | https://inc42.com/buzz/ecommerce-used-goods-zefo | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C07 | Move Loot shut 2016 | https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-sells-customer-list-to-handy | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C08 | Shopo shut 2017-02-10 | https://www.businessinsider.in/snapdeals-shopo-shuts-down-roposo-kraftly-see-surge-in-sellers/articleshow/57208653.cms | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C09 | Hinjewadi+Kharadi 400,000 professionals | https://www.sobha.com/blog/pune-workforce-residential-housing-demand/ | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C10 | conservative leakage inputs are assumptions (forge#C14, economics#C03) | forge-v1.md; economics-v1.md | VERIFIED | Both labeled ASSUMPTION in source files |
| prosecution-market-v1.md#C11 | conservative contribution ₹117 vs CAC ₹1,064, payback not reached | economics-v1.md | VERIFIED | Matches economics; arithmetic verified above. "Payback not reached" depends on the unsourced one-time-user premise |
| prosecution-market-v1.md#C12 | "forge-v1 states the seller transacts once on leaving" | forge-v1.md#C01 | MISREPRESENTED | Cited forge-v1.md#C01 does not say this. Economics step 6 asserts it without source. Evidence for FATAL FM2 |
| prosecution-market-v1.md#C13 | resale ranges from one undated content-marketing guide | https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1 | UNREACHABLE (tool failure) | Evidence for FATAL FM2 |
| prosecution-execution-v1.md#C01 | conservative ₹117 vs CAC ₹1,064, ₹262 without Instagram | economics-v1.md | VERIFIED | Matches economics; arithmetic verified |
| prosecution-execution-v1.md#C02 | economics uses 40% paying share; forge 30-60% leakage | economics-v1.md#C03; forge-v1.md#C14 | VERIFIED | Both present. Evidence for FATAL FE2 |
| prosecution-execution-v1.md#C04 | Consumer Protection (E-Commerce) Rules entity definition, grievance officer | https://www.lkslaw.com/insights/news/e-commerce-consumer-protection-e-commerce-rules-2020-notified | UNREACHABLE (tool failure) | Prosecutor read search summary only |
| prosecution-execution-v1.md#C05 | CGST s.24 categories; ₹20 lakh threshold | https://www.knowyourgst.com/gstlaw/cgst-act/24-compulsory-registration-in-certain-cases-24/ ; https://learn.quicko.com/?p=1370 | UNREACHABLE (tool failure) | |
| prosecution-execution-v1.md#C06 | proposed 2021 DPIIT registration amendment | https://www.bananaip.com/?p=77645 | UNREACHABLE (tool failure) | Prosecutor already says unverified |
| prosecution-execution-v1.md#C07 | WhatsApp group 1,024 / Community 5,000 limits | https://getkanal.com/blog/community-guide-whatsapp | UNREACHABLE (tool failure) | |
| prosecution-execution-v1.md#C11 | Pune guide names OLX/FB as channels; transport ₹500-1,500 | https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1 | UNREACHABLE (tool failure) | |
| prosecution-execution-v1.md FE2 C03 | RBI breather for small-merchant UPI | https://www.business-standard.com/topic/upi | UNREACHABLE (tool failure) | Same URL as 01-local-market.md#C20; the RBI point is also labeled ASSUMPTION as a risk, not a finding |
| prosecution-execution-v1.md#C09 | 120 h / 13 weeks = 9.2 h/week | economics-v1.md Calculations step 10 | VERIFIED | Arithmetic correct. Evidence for FE6 |
| prosecution-execution-v1.md#C10 | ad-cost sources are search summaries, CPC ₹0.51-34 | economics-v1.md#C08 | VERIFIED | Matches economics#C08 (the underlying figures are struck above) |
| 01-local-market.md#C01 / #C14 | Rentomojo plan from ₹2,199/month; Pune clusters | https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399 | UNREACHABLE (tool failure) | Scout reports its own fetch failed and used a search summary; promotional source. Demand-evidence candidate |
| 01-local-market.md#C11 | PG rent ₹4,750-12,000 Hinjewadi/Kharadi | https://housing.com/news/top-pg-locations-in-pune/ | UNREACHABLE (tool failure) | |
| 02-signals.md#C08 | Sarvam speech ₹30/hour, TTS ₹20 per 10,000 chars | https://docs.sarvam.ai/api-reference-docs/pricing.md | UNREACHABLE (tool failure) | |
| 02-signals.md#C11 | WhatsApp India marketing rate ₹0.7846 to ₹0.8631 | https://montymobile.com/blogs/whatsapp-business-api-pricing-in-india-inr-rates-gst-and-the-2026-currency-migration-deadline | UNREACHABLE (tool failure) | |

## Struck claims
- economics-v1.md#C01 — UNREACHABLE (tool failure) — conservative price ₹3,000 source not readable
- economics-v1.md#C04 — UNREACHABLE (tool failure) — Razorpay fee figures
- economics-v1.md#C08 — UNREACHABLE (tool failure) — Meta ad cost figures (all three URLs)
- economics-v1.md#C11 — UNREACHABLE (tool failure) — broker move-out visibility
- economics-v1.md#C13 — UNREACHABLE (tool failure) — S&E intimation free
- economics-v1.md Scenarios optimistic column (gross margin 70%, blended CAC ₹89, Instagram CAC ₹133) — MISREPRESENTED — not reproducible from the file's own inputs (68.2%, about ₹73, about ₹167)
- economics-v1.md Calculations step 6 (seller transacts once) — UNSOURCED — no source, no ASSUMPTION label
- forge-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C09, #C11 — UNREACHABLE (tool failure) — sources not readable
- forge-v1.md Path section UPI figure — UNREACHABLE (tool failure)
- forge-v1.md#C10 — UNSOURCED — study table/chair ₹2,000-4,000 price has no source
- prosecution-market-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C07, #C08, #C09, #C13 — UNREACHABLE (tool failure) — sources not readable
- prosecution-market-v1.md#C12 — MISREPRESENTED — cited forge-v1.md#C01 does not state one-time use
- prosecution-execution-v1.md#C04, #C05, #C06, #C07, #C11 and the RBI/business-standard claim in FE2 — UNREACHABLE (tool failure) — sources not readable
- 01-local-market.md#C01, #C14, #C11 — UNREACHABLE (tool failure) — sources not readable
- 02-signals.md#C08, #C11 — UNREACHABLE (tool failure) — sources not readable
- Note for the Judge: prosecution-execution-v1.md#C10 and the economics inputs it echoes are internally consistent but rest on struck sources. FATAL flaws FE1, FE2 and FE5 rest on economics arithmetic and forge's own admissions, both VERIFIED. FM1 and FM2 rest partly on struck claims (market C05, C12, C13), and their remaining support is the same VERIFIED economics and forge text.

## Assumptions in load-bearing positions
- economics-v1.md#C01 — ASSUMPTION (also a struck source) used as the basis of the conservative price and KM2 threshold position
- economics-v1.md#C03 — ASSUMPTION: 40% paying share, the conservative input and the basis of FATAL FE2 and the KE2 collection-rate result
- economics-v1.md#C06 — ASSUMPTION: 2.0 h per sale, the basis of the KE1 hours result
- economics-v1.md#C09, #C10, #C11, #C12 — ASSUMPTION: conversion and reach figures behind blended CAC ₹1,064
- economics-v1.md#C14, #C15 — ASSUMPTION: time and capital to first revenue (KE2, K6)
- forge-v1.md#C12, #C13, #C14, #C15, #C17 — ASSUMPTION: completion rate, price, willingness to pay on off-platform-completable sales, operator time, pain strength
- forge-v1.md#C07 — ASSUMPTION stating a gap: basis of KM5 INSUFFICIENT EVIDENCE
- prosecution-execution-v1.md FE2 C03 and FE6 seasonality — ASSUMPTION: used inside FATAL FE2 (RBI exposure) and FE6

## Summary
- verified: 9, misrepresented: 2, unreachable: 34 (of which tool failure: 34), unsourced: 2
- tool-failure strikes: 34. Every external fetch in this session was refused by the proxy, so the 34 strikes say nothing about whether the sources are accurate. A re-run with a working fetch tool is advisable before the Judge relies on the strikes.
- demand evidence surviving the audit: none (Cashify, Furlenco and Rentomojo revenue figures and the Rentomojo ₹2,199/month price all struck as UNREACHABLE (tool failure))
