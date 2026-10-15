---
run_id: 2026-10-15-check-english-clubs-pune
idea_id: I01
agent: evidence-auditor
version: 1
created: 2026-10-15T10:33:46Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I01/kill-criteria.md, ideas/I01/forge-v1.md, ideas/I01/economics-v1.md, ideas/I01/prosecution-market-v1.md, ideas/I01/prosecution-execution-v1.md (all under the run folder; verdict not read)
- claims in scope: about 135 (counted by claim id and evidence bullet), checked: 27 rows below, sample method: all economics inputs and arithmetic + all FATAL-flaw evidence (FM2, FE1, FE2) + all demand-evidence claims + non-random sample of the rest (the fetch tool failed, so sampling was limited to hosts attempted)
- fetch environment: every WebFetch call (17 distinct URLs on 16 hosts, one URL retried) returned "proxy refused the connection". This is a tool or environment failure, not evidence about the sources. No live source page was read by this auditor. Rows marked UNREACHABLE (tool failure) are struck under rule 8 even though the cause is the tool.
- internal-only checks (arithmetic, quotes of run files, contract values) were done by reading the files and are labeled VERIFIED with a note.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 | price ₹499/month | 00-contract.md (local file) | VERIFIED | Contract states ₹499 per month. The ₹599 optimistic price is a labeled ASSUMPTION. |
| economics-v1.md#C02 | substitutes: Duolingo ~₹150, SpeakX ₹299, institutes ₹4,000-15,000 | refs to 01#C01/C11/C15/C17, forge#C03 | UNREACHABLE (tool failure) | Run-file refs exist, but the prices rest on third-party URLs I could not open (talkdrill, engvarta, inc42). |
| economics-v1.md#C03 | Razorpay 2% + 18% GST = 2.36% | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ | UNREACHABLE (tool failure) | Economics itself says "not confirmed", seen in a summary only. The 2.36% product is arithmetically right (2% x 1.18). |
| economics-v1.md#C09 | freelance facilitator ₹1,000/hour | https://www.britishcouncil.in/about/jobs/freelance-trainer-0 | UNREACHABLE (tool failure) | Economics itself says about 2016, multi-city, summary only. Load-bearing for FM2 and FE2. |
| economics-v1.md#C10 | Instagram CPC ₹6-55 | https://upgrowth.in/instagram-ads-pricing-india-2026/ | UNREACHABLE (tool failure) | Economics says attribution was inferred and the page not opened. Conservative ₹50 input is labeled ASSUMPTION. |
| economics-v1.md#C10 | Facebook education CPC ~USD 0.09 India | https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/education/india | UNREACHABLE (tool failure) | Not used in the conservative number. |
| economics-v1.md#C13 | GST not due below ₹20 lakh; registration sources disagree | refs 01#C20, 01#C21 | UNREACHABLE (tool failure) | Rests on vendor blogs (kanakkupillai, patronaccounting) I did not fetch. The ₹5,000 amount is an ASSUMPTION. |
| economics-v1.md#C16 | Pune student spend unknown | 01-local-market.md#C14 | VERIFIED | Matches 01#C14, an honest ASSUMPTION-labeled gap. |
| economics-v1.md Calculations | conservative arithmetic (COGS ₹282, margin 43.5%, CAC by channel, blended ₹556, payback 2.56, LTV/CAC 0.98, break-even 14, steady state -₹86, capital ₹13,333, 3-month outlay ₹24,500, hours 9h/12h, facilitator -₹783) | n/a | VERIFIED | Recomputed every line; all correct. Only immaterial rounding: café channel "3 x about 7 = 20" (21 exact) and base/optimistic payback 0.15 vs 0.14. Inputs are mostly ASSUMPTION, so correct arithmetic does not make the inputs sourced. |
| prosecution-market-v1.md#C03 | British Council ₹1,000/hour, about 2016 | https://www.britishcouncil.in/about/jobs/freelance-trainer-0 | UNREACHABLE (tool failure) | Same URL as economics#C09. Basis of FM2 (FATAL). |
| prosecution-market-v1.md FM2 / 01-local-market.md#C04 | Pune tutors average ₹702/hour | https://www.superprof.co.in/lessons/english/pune/ | UNREACHABLE (tool failure) | Attempted twice. Also used by forge#C02, prosecution-execution FE2/KE5. |
| prosecution-execution-v1.md#C01-C03 (FE1) | 9h at one group, 12h at two; K2 BREAKS; K2 HARD at 10h | economics-v1.md; 00-contract.md | VERIFIED | Economics Calculations and Constraint check state this; contract K2 is HARD, no stretch. The hours themselves are ASSUMPTION (forge#C23, economics#C08). |
| prosecution-execution-v1.md#C04 (FE2) | facilitator adds ₹1,000/member; contribution -₹783 | economics-v1.md | VERIFIED | Arithmetic correct: 2,000 x 4 / 8 = 1,000; 217 - 1,000 = -783. Depends on struck input economics#C09. |
| prosecution-execution-v1.md#C06 (FE2) | ₹702 x 1.5 x 4 / 10 = ₹421; +₹32 = ₹453 (91%) | n/a | VERIFIED | Arithmetic correct (421.2; 453/499 = 90.8%). The ₹702 input is struck (superprof). Sentence wording is garbled but the numbers hold. |
| prosecution-execution-v1.md KE5 note | ₹1,282 per member; ₹832 (167%) in base | economics-v1.md | VERIFIED | 282 + 1,000 = 1,282; 2,000 x 4 / 10 + 32 = 832; 832/499 = 167%. |
| 01-local-market.md#C01 | Let's Talk ₹7,000-12,000, Veta ₹5,000-9,000/month | https://www.talkdrill.com/blog/english-speaking-classes/pune/ | UNREACHABLE (tool failure) | Demand evidence (existing spend). Source is a promotional blog per the scout. Also forge#C01. |
| 01-local-market.md#C02 | Engspeak ₹12,000 for 3 months | https://collegedunia.com/institute/9655-engspeak-academy | UNREACHABLE (tool failure) | Demand evidence (existing spend). |
| 01-local-market.md#C03 | IndiaMART Pune course ₹4,000/month; online ₹990 | https://m.indiamart.com/proddetail/development-plan-coaching-classes-7344119412.html | UNREACHABLE (tool failure) | Demand evidence. Attempted in a second batch. Scout rates it low reliability. |
| 02-signals.md#S01 (also forge#C13, #C06) | SpeakX USD 16M, 200,000 paying subs, ~USD 7.5M ARR | https://india.entrepreneur.com/news-and-trends/speakxai-raises-usd-16-mn-to-strengthen-ai-powered-english/498354 | UNREACHABLE (tool failure) | Demand evidence. Signal scout says it saw snippets only. |
| 02-signals.md#S02 (also forge#C03, prosecution-market#C08) | SpeakX ₹299/month; EBITDA positive | https://inc42.com/buzz/exclusive-ms-dhoni-joins-edtech-startup-speakxs-cap-table/ | UNREACHABLE (tool failure) | Demand evidence and price anchor. Also noted: prosecution-market says "EBITDA positive in FY26", 01#C07 says "since April 2025" (different source); not reconciled. |
| 01-local-market.md#C11 (also forge#C11) | Duolingo ~₹150, ELSA ~₹1,000, Speak ₹1,650-2,500, Cambly, EngVarta | https://engvarta.com/tag/spoken-english-app-review-india/ | UNREACHABLE (tool failure) | Vendor-reported by a competitor per the scout. |
| 01-local-market.md#C16 | "commercial blog says Pune has 30+ Toastmasters clubs" | https://mylanguageexchange.com/city/Pune__India.asp | UNREACHABLE (tool failure) | Same URL is cited for C17 (language exchange). Attributing a Toastmasters count to a language-exchange page is doubtful but not checked. |
| forge-v1.md#C09 | SPPU 600+ colleges; university page says 629, Wikipedia 612 | https://en.wikipedia.org/wiki/Savitribai_Phule_Pune_University | UNREACHABLE (tool failure) | Wikipedia figure only. |
| forge-v1.md#C09 (sub-claim) | "the university's own page gives 629" | none | UNSOURCED | No URL for the university page. Also in prosecution-market#C05 (SPPU 2010 enrolment 496,531), UNREACHABLE (tool failure) for Wikipedia. |
| forge-v1.md#C12 (also prosecution-market#C04/FM4) | ASSOCHAM pocket money ~₹1,500/month by 2011 | https://news.cleartax.in/pocket-money-in-india-how-the-amount-has-risen-over-the-decades/3763/amp | UNREACHABLE (tool failure) | Both files already call it old and unreliable. |
| 01-local-market.md#C27 | eChai socials in Baner Jan and Mar 2026 at cafés | https://echai.ventures/pune/communities/recurring-meetup | UNREACHABLE (tool failure) | Supports venue plausibility only. |
| prosecution-execution-v1.md#E01 (FE6) | Toastmasters dues USD 72 per six months, USD 25 new-member fee, from 2026-08-03 | https://www.toastmasters.org/Footer/FAQ/Membership | UNREACHABLE (tool failure) | Prosecution-market#C02 cites a different URL (toastmasters.org/footer/faq/Membership-Dues) with the same figures; not separately fetched. |

## Struck claims
- economics-v1.md#C02 — UNREACHABLE (tool failure) — substitute prices rest on unopened third-party pages
- economics-v1.md#C03 — UNREACHABLE (tool failure) — Razorpay fee page
- economics-v1.md#C09 — UNREACHABLE (tool failure) — British Council ₹1,000/hour facilitator rate (conservative input, basis of FM2 and FE2)
- economics-v1.md#C10 (both URLs) — UNREACHABLE (tool failure) — Instagram and Facebook CPC pages
- economics-v1.md#C13 — UNREACHABLE (tool failure) — GST and registration chain to vendor blogs
- prosecution-market-v1.md#C03 — UNREACHABLE (tool failure) — same British Council URL
- prosecution-market-v1.md#C04 (cleartax) — UNREACHABLE (tool failure)
- prosecution-market-v1.md#C05 — UNREACHABLE (tool failure) — Wikipedia SPPU
- prosecution-market-v1.md FM2 and 01-local-market.md#C04 / forge-v1.md#C02 — UNREACHABLE (tool failure) — Superprof ₹702/hour
- prosecution-market-v1.md#C08 — UNREACHABLE (tool failure) — inc42 SpeakX claims
- prosecution-execution-v1.md#E01 — UNREACHABLE (tool failure) — Toastmasters dues
- 01-local-market.md#C01, #C02, #C03, #C11, #C16, #C27 — UNREACHABLE (tool failure)
- 02-signals.md#S01, #S02 — UNREACHABLE (tool failure)
- forge-v1.md#C01, #C03, #C09, #C11, #C12, #C13 — UNREACHABLE (tool failure), via the same URLs as above
- forge-v1.md#C09 sub-claim "university's own page gives 629" — UNSOURCED

## Assumptions in load-bearing positions
- economics-v1.md#C04, #C05, #C07, #C08, #C11, #C12, #C14, #C15 — ASSUMPTION used as conservative inputs (materials ₹5, venue ₹500/session, 8 paying per group, 3h per session, 40% churn, ₹3,000/month boosting, funnel rates, referral rate). The economics file states the result flips with café fee ₹0 or lower churn.
- economics-v1.md#C08 and forge-v1.md#C23 — ASSUMPTION (session length, count, group size) is the sole basis for the FE1 FATAL flaw (12h/week vs 10h cap) and the KE1 NOT MET status. FE1 survives the audit only as arithmetic on assumed hours.
- forge-v1.md#C21 — ASSUMPTION (students will pay ₹499 despite free and cheaper substitutes) is the basis of FM1 and the KM1/KM2 statuses.
- 01-local-market.md#C09, #C14, #C22 — ASSUMPTION (no failure data, no student spend data, no regulatory finding) underlie KM2, KM4 and KE3 statuses.
- economics-v1.md#C09 is a sourced claim (now struck), so FM2 and FE2 have no surviving sourced facilitator rate. Their direction rests on the economics arithmetic with the struck input.

## Summary
- verified: 7, misrepresented: 0, unreachable: 19 (of which tool failure: 19), unsourced: 1
- demand evidence surviving the audit: none (every demand-evidence claim in 01 C01-C03, 02 S01-S02, forge C13 was UNREACHABLE due to tool failure; no external source was read)
