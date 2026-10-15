---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: evidence-auditor
version: 1
created: 2026-10-15T09:34:24Z
---

## Scope
- files audited: 00-contract.md; 01-local-market.md; 02-signals.md; ideas/I01/kill-criteria.md; ideas/I01/forge-v1.md; ideas/I01/economics-v1.md; ideas/I01/prosecution-market-v1.md; ideas/I01/prosecution-execution-v1.md (all under <project>/ventures/runs/2026-10-15-pune-b2c-open/)
- claims in scope: about 111 claim items (forge 25, economics 19, local-market 26, signals 15, market prosecution 10, execution prosecution 14, kill-criteria 2), checked: 60 table rows (some rows cover several claims or several URLs), sample method: all economics inputs + all claims used in FATAL flaws (FM1, FM2, FE1, FE3) + all demand-evidence claims + non-random sample of the rest (the sample is not random because every web fetch failed; internal-arithmetic checks and the sourced claims that matter most were prioritised)
- ENVIRONMENT NOTE: every WebFetch call (15 hosts in the first batch, then one retry of razorpay.com) returned "proxy refused the connection". The failure is in the fetch tool, not in the sources. No web page was read by this auditor. Every sourced claim whose check needed a page fetch is therefore labelled UNREACHABLE (tool failure) and struck under rule 8. Only checks done from the files themselves (arithmetic and cross-file consistency) could be completed.
- Provenance note: 01-local-market.md states that none of its URLs were opened and that its claims come from search snippets. Several prosecutor claims are snippet-only by their own statement.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 | list price ₹199, ₹99 add-on | forge-v1.md Core identity | VERIFIED | Internal reference matches forge-v1 revenue model. Design choice, not market data. |
| economics-v1.md#C04 | UPI P2M zero MDR; gateway fees; MDR may return above ₹2,000 | https://razorpay.com/blog/upi-mdr-for-merchants-in-payment-gateway-explained/ | UNREACHABLE | UNREACHABLE (tool failure). Conservative model uses 2% + GST regardless. |
| economics-v1.md#C06 | LLM cost per case under ₹5 | https://benchlm.ai/stats/llm-pricing | UNREACHABLE | UNREACHABLE (tool failure). Economics also says the page was "not re-opened by this agent", so it is second-hand. |
| economics-v1.md#C07 | ChatGPT Go ₹399/month in India | https://www.mansworldindia.com/lifestyle/tech/chat-gpt-go-launched-in-india-at-399-a-game-changer-for-ai-accessibility | UNREACHABLE | UNREACHABLE (tool failure). Source is a 2025 launch article; economics notes the price may have changed. |
| economics-v1.md#C10 | Instagram CPC ₹8–25 (range ₹6–55) | https://upgrowth.in/instagram-ads-pricing-india-2026/ | UNREACHABLE | UNREACHABLE (tool failure). Feeds the paid-ads reference CAC of ₹5,000 (FM2 cites it). |
| economics-v1.md#C18 | NCH about 511,196 e-commerce grievances in 2025, handled free | https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm | UNREACHABLE | UNREACHABLE (tool failure). The "handled free" part is not stated in the source as cited. |
| economics-v1.md#C19 | K2 = 10 h/week; 10 x 4.33 = 43.3 h/month | 00-contract.md K2 | VERIFIED | Contract K2 is 10 h HARD; arithmetic correct. |
| economics-v1.md Calculations (conservative, except payback) | gateway 3.52, COGS 23.42, contribution 125.58, margin 84.3%, loaded -61.92 / -41.6%, volume 4.75, 100 customers in 21 months, CAC 444 / 3,333 / 1,000 / 1,474, break-even 7.96 -> 8, monthly result -403.5, capital 5,000, year-1 about 9,000, hours 7.3 h/week, paid-ad CAC ₹5,000 (about 34x) | economics-v1.md | VERIFIED | Each figure recomputed from the stated inputs and matches. Ad-CAC conversion rates are ASSUMPTION. |
| economics-v1.md Scenarios/Calculations, conservative payback | payback "11.8" purchases | economics-v1.md | MISREPRESENTED | The file's own arithmetic gives 1,473.7 / 125.58 = 11.74, which rounds to 11.7 not 11.8. The text says "rounded to 11.8". Small error, does not change the conclusion. |
| economics-v1.md Scenarios, base column | COGS ₹17.2, margin 91.4%, loaded margin 28.5% | economics-v1.md | MISREPRESENTED | The file's own Calculations give COGS 17.65 and margin 91.1% and state the table value is stale. Loaded margin recomputes to 28.3%. The file says the base column was not re-derived. |
| economics-v1.md Scenarios, optimistic column | COGS ₹14.3, margin 93.5%, CAC ₹421, payback 2.1, loaded margin 47.8% | economics-v1.md | MISREPRESENTED | Calculations give COGS 13.74, margin 93.7%, CAC 333 (file says 421 is "superseded"); loaded margin recomputes to 48.1%; payback at CAC 333 is about 1.6, not 2.1. Not load-bearing. |
| forge-v1.md#C01 | Pune about 1.86% of national UPI volume (Apr 2026); Maharashtra largest UPI state | https://factodata.com/state-wise-upi-transactions-india/ | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md#C02 | Pune district per capita income about ₹3.58 lakh | https://www.thehitavada.com/Encyc/2026/3/10/per-capita-inconsistency.html | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md#C03 | Grievance Officer acknowledges in 24 h, resolves in 15 days (IT Rules 2021 Rule 3(2)) | https://righttoinformation.wiki/_export/xhtml/wrong-product-amazon-flipkart-refund-india | UNREACHABLE | UNREACHABLE (tool failure). Forge itself calls the source an unofficial wiki. |
| forge-v1.md#C04 | NCH on 1915, WhatsApp, SMS, email, app, UMANG, INGRAM, 17 languages | https://www.etvbharat.com/en/!bharat/national-consumer-helpline-refunds-rs-7-14-crore-to-consumers-in-two-months-enn25070406342 | UNREACHABLE | UNREACHABLE (tool failure). Used by execution FE3 (via forge C04) as part of a FATAL flaw. |
| forge-v1.md#C05 | lawyer fee ₹10,000–₹50,000 | https://lawsathi.in/?p=1278 | UNREACHABLE | UNREACHABLE (tool failure). Forge calls it a single imprecise blog. |
| forge-v1.md#C06 | consumer complaints filed online via e-Daakhil | https://lawsathi.in/?p=1278 | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md#C07 | 511,196 of 1,771,622 NCH grievances in 2025 (about 29%) | https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm | UNREACHABLE | UNREACHABLE (tool failure). Arithmetic 511,196 / 1,771,622 = 28.9% is correct. Same figure is in the locked criteria (KM2 premise). |
| forge-v1.md#C08 | refunds above ₹105 crore, 166,189 grievances, e-commerce 100,466 and over ₹74 crore (25 Apr–31 Jul 2026) | https://www.etvbharat.com/en/!bharat/national-consumer-helpline-refunds-rs-7-14-crore-to-consumers-in-two-months-enn25070406342 | UNREACHABLE | UNREACHABLE (tool failure). The URL slug reads "refunds-rs-7-14-crore ... two months" and carries a 2025 identifier (enn25070406342), which does not obviously match a 2026 period of 25 Apr–31 Jul. Flagged for the Judge; unresolved. |
| forge-v1.md#C09 | implied average refund about ₹7,400 | forge-v1.md#C08 | VERIFIED | Arithmetic only: 74 crore / 100,466 = about ₹7,365. It rests on C08, which is struck, so the figure has no surviving support. ASSUMPTION-labeled by forge. |
| forge-v1.md#C10 | Amendment Rules 2026 effective 2027-01-01 | https://www.moneylife.in/article/new-ecommerce-rules-to-rein-in-dark-patterns-misleading-listings-and-hidden-charges-from-1st-january/81643.html | UNREACHABLE | UNREACHABLE (tool failure). Press source only; no Gazette or PIB source (KM6 asks for one). |
| forge-v1.md#C11 | forum users report Amazon support not following up (Trivandrum) | https://techenclave.com/t/amazon-customer-support-is-awful-escalation-options-experiences/249194 | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md#C12 | society WhatsApp groups run several per society (vendor) | https://blog.ind.adda.io/2025/04/managing-community-whatsapp-groups/ | UNREACHABLE | UNREACHABLE (tool failure). The reach figures in the same claim are labelled ASSUMPTION; their arithmetic (6,000 / 600 / 18 / 4.5) is correct. |
| forge-v1.md#C16 | referral credit ₹50, 0.2 referrals per customer | none | UNSOURCED | States "assumed 0.2 referrals per customer" in prose but carries no source and no ASSUMPTION label in claim format. Struck. |
| forge-v1.md#C21 | LLM drafting under ₹5 per case | https://benchlm.ai/stats/llm-pricing | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md#C22 | DPDP duties from about 2027-05-13 | https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified | UNREACHABLE | UNREACHABLE (tool failure). |
| forge-v1.md Positioning (LawRato) | 2016: ₹500 for a 30-minute phone consultation | https://ts.yourstory.com/2016/02/lawrato | UNREACHABLE | UNREACHABLE (tool failure). Source is 2016, outside KM1's 2024-10-15 window in any case. |
| prosecution-market-v1.md#C01 | IncorpX legal notice from ₹1,499 plus postage | https://www.incorpx.io/legal-notice-drafting | UNREACHABLE | UNREACHABLE (tool failure). Demand evidence for KM1/KM4 and cited in FM1. Prosecutor labels it a vendor claim. |
| prosecution-market-v1.md#C02 | Ebizfiling complaint letter from ₹4,999 | https://ebizfiling.com/service/consumer-complaint-letter/ | UNREACHABLE | UNREACHABLE (tool failure). FM1 attributes the ₹4,999 price to the incorpx link; the Ebizfiling URL is the one that carries it. |
| prosecution-market-v1.md#C03 | Consumer VOICE ₹499 for advice plus notice | https://join.consumer-voice.org/legal/ | UNREACHABLE | UNREACHABLE (tool failure). Snippet-only and undated by the prosecutor's own note. |
| prosecution-market-v1.md#C04 | NCH 1,315,664 grievances in 2024-25; e-commerce 32.22% | https://dataful.in/datasets/20716 | UNREACHABLE | UNREACHABLE (tool failure). |
| prosecution-market-v1.md#C05 | Rajya Sabha 2025-02-11: e-commerce received 440,185, disposed 440,185 (2024) | https://rsdebate.nic.in/bitstream/123456789/758830/1/PQ_267_11022025_U882_p314_p316.pdf | UNREACHABLE | UNREACHABLE (tool failure). Cited in FATAL flaw FM1. |
| prosecution-market-v1.md#C06 | 77% of e-commerce complaints resolved to satisfaction | https://inc42.com/buzz/ecommerce-complaints-consumer | UNREACHABLE | UNREACHABLE (tool failure). Undated per prosecutor. Only figure used for KM2. |
| prosecution-market-v1.md#C07 | FTC settled with DoNotPay for $193,000 | https://www.abajournal.com/news/article/robot-lawyer-website-donotpay-settles-ftc-claims-it-couldnt-deliver-on-promises | UNREACHABLE | UNREACHABLE (tool failure). (other country: US). |
| prosecution-market-v1.md#C08 | e-commerce grievances 2.05 lakh (2020-21) to 4.45 lakh (2023-24) | https://www.medianama.com/2025/07/223-national-consumer-helpline-8500-e-commerce-complaints/ | UNREACHABLE | UNREACHABLE (tool failure). KM6 series. |
| prosecution-market-v1.md#C09 | 577,748 e-commerce grievances in 2025-26 | https://kashmirlife.net/consumer-complaints-from-jammu-kashmir-rise-78-per-cent-in-three-years-all-cases-resolved-centre-tells-lok-sabha-446604/ | UNREACHABLE | UNREACHABLE (tool failure). Prosecutor reports its own fetch of this host also failed. |
| prosecution-market-v1.md#C10 | 2025 NCH totals (from signals file) | https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm | UNREACHABLE | UNREACHABLE (tool failure). Same page as forge C07. |
| prosecution-market-v1.md FM2 / prosecution-execution-v1.md FE1 | volume 4.75 and 9.5 cases/month; base +about ₹900/month; 13–20 cases/week at 0.5–0.75 h | economics-v1.md; forge-v1.md | VERIFIED | Recomputed: 9.5 x 181.35 - 799 = about ₹923; 10 h / 0.75 = 13.3, 10 h / 0.5 = 20. Correct. Underlying inputs are ASSUMPTION. |
| prosecution-execution-v1.md KE1/KE6 | 100 cases/month = 11.5–17.3 h/week; 20 cases/week = 10–15 h | economics-v1.md#C12 | VERIFIED | Recomputed from 30–45 min per case: correct. |
| prosecution-execution-v1.md FE4 | break-even 22–83 cases at fixed ₹2,800–10,400 | economics-v1.md | VERIFIED | 999 + 1,770 = 2,769 and 999 + 9,440 = 10,439; divided by 125.58 gives 22 and 83. Fee inputs are from sources that were not fetched (see next rows). |
| prosecution-execution-v1.md#C04 / E1 | Advocates Act s.33 bars non-enrolled persons from practising | https://lawx.in/acts/section/65/586/5700 | UNREACHABLE | UNREACHABLE (tool failure). Supports FE2 (FIXABLE). |
| prosecution-execution-v1.md#C06 / E3 | NCH 2.0 AI chatbot, speech recognition, translation | https://www.thestatesman.com/business/national-consumer-helpline-partners-with-over-1000-companies-to-bring-ai-tools-1503368509.html | UNREACHABLE | UNREACHABLE (tool failure). Cited in FATAL flaw FE3 and criterion KE3. |
| prosecution-execution-v1.md#C06 | NCH AI-enabled grievance redressal | https://indiaai.gov.in/article/ai-enabled-national-consumer-helpline-transforming-grievance-redressal-in-india | UNREACHABLE | UNREACHABLE (tool failure). Second source for FE3. |
| prosecution-execution-v1.md#C12 / E4 | WhatsApp Business policy: restricted goods at Meta's discretion | https://whatsappbusiness.com/policy/ | UNREACHABLE | UNREACHABLE (tool failure). |
| prosecution-execution-v1.md#C08 / E5 | WhatsApp India rates ₹0.78–1.10 marketing, ₹0.115–0.145 utility; BSP fees ₹1,500–8,000 | https://montymobile.com/blogs/whatsapp-business-api-pricing-in-india-inr-rates-gst-and-the-2026-currency-migration-deadline (also dev.to/chatlivo and m.aisensy.com cited) | UNREACHABLE | UNREACHABLE (tool failure) for all three URLs. FE4 is FIXABLE; the strike weakens it. |
| prosecution-execution-v1.md E6 | RegisterKaro page and complaints | https://registerkaro.in/consumer-complaint | UNREACHABLE | UNREACHABLE (tool failure). Prosecutor notes the complaints are unverified. |
| prosecution-execution-v1.md E2 | Bar Council of India v. A.K. Balaji (2018) substance-over-label test | https://itatonline.org/digest/bar-council-of-india-v-a-k-balaji-and-others-air-2018-sc-1382/ | UNREACHABLE | UNREACHABLE (tool failure). Prosecutor says it did not re-open the page. Also cited in kill-criteria KE2. |
| 01-local-market.md#C01 | Pune D2C brands raised about $554 Mn across 32 deals | https://inc42.com/buzz/delhi-ncr-emerges-as-indias-top-d2c-hub/ | UNREACHABLE | UNREACHABLE (tool failure). |
| 01-local-market.md#C03 | quick commerce in Pune (BofA note) | https://techcrunch.com/2024/03/11/zomato-blinkit-sprints-to-quick-commerce-dominance-in-india/amp | UNREACHABLE | UNREACHABLE (tool failure). |
| 01-local-market.md#C05 | Zigly pet care centre in Pune, 2025-11-01 | https://www.cosmofirst.com/press-release/zigly-expands-its-footprint-in-western-india-opens-first-complete-pet-care-centre-in-pune | UNREACHABLE | UNREACHABLE (tool failure). |
| 01-local-market.md#C15 | Pawzeeble, 380+ clinics, 600+ vets | https://yourstory.com/2025/06/affordable-pet-care-inside | UNREACHABLE | UNREACHABLE (tool failure). |
| 01-local-market.md#C20 | Shops and Establishments registration (vendor) | https://www.taxbuddy.com/blog/shop-and-establishment-registration-for-shops-offices-and-online-businesses | UNREACHABLE | UNREACHABLE (tool failure). Economics C09 depends on this topic. |
| 01-local-market.md#C23 | DPDP Rules notified 2025-11-13; duties from about 2027-05-13 | https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified | UNREACHABLE | UNREACHABLE (tool failure). |
| 01-local-market.md#C24 | Maharashtra about 9.78% of UPI volume (Jun 2026); Pune about 1.86% (Apr 2026) | https://factodata.com/state-wise-upi-transactions-india/ | UNREACHABLE | UNREACHABLE (tool failure). |
| 02-signals.md#C05 | UPI 24.51 bn (Aug 2026), 24.07 bn (Sep 2026) | https://startuptalky.com/upi-transactions-september-2026/ | UNREACHABLE | UNREACHABLE (tool failure). |
| 02-signals.md#C13 | Pune police order 2026-07-03; 113 landlords | https://www.punekarnews.in/?p=241832 | UNREACHABLE | UNREACHABLE (tool failure). |
| 02-signals.md#C14 | India D2C raised about $6bn 2021–Aug 2026 | https://technode.global/2026/08/26/indian-d2c-companies-raised-6b-in-equity-funding-across-2000-rounds-between-2021-and-2026-tracxn/ | UNREACHABLE | UNREACHABLE (tool failure). |
| 02-signals.md#C02 | 79,521 refund complaints; e-commerce 47,743 | https://oga-prod.angelone.in/news/economy/national-consumer-helpline-secures-rs-52-crore-refunds-e-commerce-sector-leads-claims-in-9-months | UNREACHABLE | UNREACHABLE (tool failure). |
| kill-criteria.md KE4 | Meta WhatsApp pricing page (source for conflicting prices) | https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing | UNREACHABLE | UNREACHABLE (tool failure). Locked file; listed for completeness. |
| kill-criteria.md KE5 | DPDP penalties (treelife) | https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/ | UNREACHABLE | UNREACHABLE (tool failure). Locked file; listed for completeness. |

## Struck claims
Tool-failure strikes (UNREACHABLE (tool failure)), 49 in total:
- economics-v1.md#C04 — UNREACHABLE (tool failure) — razorpay page not read.
- economics-v1.md#C06 — UNREACHABLE (tool failure) — benchlm page not read; also second-hand per economics.
- economics-v1.md#C07 — UNREACHABLE (tool failure) — ChatGPT Go price article not read.
- economics-v1.md#C10 — UNREACHABLE (tool failure) — Instagram CPC page not read.
- economics-v1.md#C18 — UNREACHABLE (tool failure) — storyboard18 page not read.
- forge-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C07, #C08, #C10, #C11, #C12, #C21, #C22 and the LawRato positioning row — UNREACHABLE (tool failure).
- prosecution-market-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C07, #C08, #C09, #C10 — UNREACHABLE (tool failure).
- prosecution-execution-v1.md#C04/E1, #C06/E3 (both URLs), #C12/E4, #C08/E5 (all three URLs), E6, E2 — UNREACHABLE (tool failure).
- 01-local-market.md#C01, #C03, #C05, #C15, #C20, #C23, #C24 — UNREACHABLE (tool failure).
- 02-signals.md#C02, #C05, #C13, #C14 — UNREACHABLE (tool failure).
- kill-criteria.md KE4 and KE5 source URLs — UNREACHABLE (tool failure); the locked criteria text itself is not a claim to strike, but the Judge should not treat these URLs as audited.

Other strikes:
- forge-v1.md#C16 — UNSOURCED — referral rate stated with no source and no ASSUMPTION label.
- economics-v1.md conservative payback "11.8" — MISREPRESENTED — own arithmetic gives 11.74 (11.7).
- economics-v1.md base column (COGS 17.2, margin 91.4%, loaded margin 28.5%) — MISREPRESENTED — contradicts the file's own Calculations (17.65, 91.1%, 28.3%).
- economics-v1.md optimistic column (COGS 14.3, margin 93.5%, CAC 421, payback 2.1, loaded margin 47.8%) — MISREPRESENTED — contradicts own Calculations (13.74, 93.7%, 333) and the payback and loaded margin do not follow.

Judge note on what the strikes do to the case. These are not source-contradiction findings; they are non-verifications. The conservative economics arithmetic, the hours arithmetic and the volume arithmetic checked out and are not struck. The FATAL flaws FM2 and FE1 rest mainly on internal arithmetic and on ASSUMPTION-labelled volumes, which survive as arithmetic but not as facts about Pune. FM1 and FE3 rely on struck URLs (rsdebate, incorpx, statesman, etvbharat), plus unstruck internal admissions in forge-v1.md#C17 and the Positioning table (free LLM row), which are the forge's own statements and are not struck.

## Assumptions in load-bearing positions
- forge-v1.md#C17 — ASSUMPTION used as the basis of KM1, KM4, FM1 and FE3 (willingness to pay ₹199 with free channels existing). Forge labels it load-bearing.
- forge-v1.md#C20 — ASSUMPTION (lawfulness of paid non-lawyer drafting) used as the basis of KE2 and FE2.
- forge-v1.md#C25 and #C18 — ASSUMPTION (3% stuck-refund incidence; ₹1,500 threshold) used as the basis of KM3/KM4 and FM4.
- forge-v1.md#C12–#C16 — ASSUMPTION conversion rates that feed economics volume and therefore FM2 and FE1.
- economics-v1.md#C02 — ASSUMPTION conservative price ₹149 (conservative input).
- economics-v1.md#C05 — ASSUMPTION gateway fee 2% + GST (conservative input).
- economics-v1.md#C08 — ASSUMPTION other fixed cost ₹600 (conservative input; FE4 argues it is understated).
- economics-v1.md#C09 — ASSUMPTION registration ₹2,000 (conservative input).
- economics-v1.md#C11 — ASSUMPTION fee refund rate 10% (conservative input).
- economics-v1.md#C12 — ASSUMPTION founder time 45 min per case (conservative input; basis of FE1, KE1, KE6).
- economics-v1.md#C13 — ASSUMPTION founder time value ₹250/h (basis of the negative loaded contribution used in FE1 and KE6).
- economics-v1.md#C14 — ASSUMPTION conservative volume 4.75 customers/month (basis of FM2, FE1 and the "unit economics positive: no" input).
- economics-v1.md#C15 — ASSUMPTION promotion hours (basis of CAC and the K2 check).
- economics-v1.md#C17 — ASSUMPTION months to first revenue (basis of the K6 check).

## Summary
- verified: 7 rows, misrepresented: 3 rows, unreachable: 49 rows (of which tool failure: 49), unsourced: 1 row. Total struck: 53 rows (49 tool-failure, 3 misrepresented, 1 unsourced).
- demand evidence surviving the audit: none. Every competitor-with-price or revenue claim (IncorpX ₹1,499, Ebizfiling ₹4,999, Consumer VOICE ₹499, LawRato 2016) is struck as UNREACHABLE (tool failure). No dated revenue, review or testimonial for a paid service appears anywhere in the inputs. Forge-v1.md#C17 admits there is no willingness-to-pay evidence.
