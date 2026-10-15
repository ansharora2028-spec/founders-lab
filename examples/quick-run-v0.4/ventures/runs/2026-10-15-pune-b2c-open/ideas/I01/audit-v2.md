---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: evidence-auditor
version: 2
created: 2026-10-15T10:54:13Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I01/kill-criteria.md, ideas/I01/diff-v2.md, ideas/I01/forge-v2.md, ideas/I01/economics-v2.md, ideas/I01/prosecution-market-v2.md, ideas/I01/prosecution-execution-v2.md (verdict not read)
- claims in scope: about 150 (sourced claims and ASSUMPTION claims across the files), checked: 33 (10 arithmetic checks, 23 URL checks)
- sample method: all economics inputs with a URL, all arithmetic in the economics Calculations section, all FATAL-flaw evidence (FE1, FE4), all demand-evidence URLs (diff D1 sellers, NCH figures), all URLs cited as evidence in diff rows D1, D2, D4, D9, plus two prosecutor claims and one 01-local-market claim. No random sample of the remaining sourced claims was possible, because no external page could be opened.
- tool status: every WebFetch call (23 distinct URLs, 3 of them retried, 25 calls in total) failed with "proxy refused the connection", across many different hosts. This is the fetch environment and not the sources. All URL results below are `UNREACHABLE (tool failure)`.
- not attempted (the environment failed on every host, so these remain unchecked and are not struck): amalegalsolutions.com, lawtrend.in, eparlib.nic.in, rsdebate.nic.in, theprint.in, freepressjournal.in (forge-v2.md#C02, #C04, #C09, #C11, #C14, #C24, #C25), and the remaining 01/02 URLs.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v2.md#Calculations (COGS) | gateway 2% x 500 = 10, GST 18% = 1.80, refunds 15% x 500 = 75, COGS 87, contribution 413, margin 82.6% | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (customers) | 10 + 11 + 0 + 3 = 24 (0.15 x 21 = 3.15, rounded to 3) | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (CAC, payback) | Rs 5,000 / 24 = Rs 208; 413 - 208 = 205; payback 0.50 months | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (paid CAC) | 55/0.01 = 5,500; 30/0.01 = 3,000; 15/0.02 = 750; base 15/0.024 = 625 (vs 759 contribution); optimistic 10/0.04 = 250 | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (hours) | 6.0 x 13 = 78; 24 hours production; 102 of 130 = 7.8 hours a week; cap 4 files a week, about 17 a month | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (capital) | 5,000 + 8,000 + 1,000 + 500 = Rs 14,500 | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (3-month ledger) | 12,000 - 2,088 - 5,000 - 1,500 - 5,000 = -1,588; peak cash held 19,500 | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Calculations (break-even) | monthly cash cost 2,584; 6.26 so 7 files; 8 files gives Rs 720; 17 files gives Rs 4,437 | n/a | VERIFIED | arithmetic recomputed. "31 files, 7.5 a week" is rounded loosely (31 / 4.33 = 7.2) but the 31 figure is correct |
| economics-v2.md#Verdict inputs | (10,000 + 2,584) / 17 = 740; price about 830; 13.3% at Rs 55 CPC; 6.1% at Rs 25 | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#Scenarios (base, optimistic) | base margin 95.0%, optimistic 98.0%; blended CAC Rs 43 and Rs 20 | n/a | VERIFIED | arithmetic recomputed; optimistic Instagram CAC Rs 67 cannot be reproduced because the Instagram customer count is not stated. This column is not argued from |
| forge-v2.md#Path (hours table) | 3.0 + 2.0 + 2.5 + 1.0 + 0.5 = 9.0 hours; channel customers sum to about 70 | n/a | VERIFIED | arithmetic recomputed |
| economics-v2.md#C01 | Consumer Voice notice service Rs 500 plus postage | https://join.consumer-voice.org/legal/ | UNREACHABLE (tool failure) | proxy refused; demand-evidence price anchor |
| economics-v2.md#C01 / diff-v2.md#D1 | IncorpX Rs 1,499 plus postage, advocates, 3-5 days | https://www.incorpx.io/legal-notice-drafting | UNREACHABLE (tool failure) | refused twice |
| economics-v2.md#C01 / diff-v2.md#D1 | Ebizfiling consumer complaint letter from Rs 4,999, self-published 4.8 rating | https://ebizfiling.com/service/consumer-complaint-letter/ | UNREACHABLE (tool failure) | proxy refused |
| diff-v2.md#D1 | RegisterKaro consumer complaint, self-published 4.6 Google rating | https://www.registerkaro.in/consumer-complaint | UNREACHABLE (tool failure) | proxy refused |
| economics-v2.md#C03 | UPI payments of Rs 2,000 or less carry zero MDR from 2026-10-15 | https://morungexpress.com/npci-reveals-mdr-on-upi-payments-above-rs-2000-from-oct-15-small-merchants-continue-to-benefit | UNREACHABLE (tool failure) | proxy refused. Not decisive: the conservative case applies a 2% gateway fee anyway |
| economics-v2.md#C08 | Bar Council of India v A.K. Balaji (2018), "pith and substance" test | https://itatonline.org/archives/?p=18108 | UNREACHABLE (tool failure) | proxy refused; supports the FE1 FATAL flaw and the K5 exposure |
| economics-v2.md#C09 | Instagram CPC in India about Rs 6-55, cluster Rs 10-25 | https://upgrowth.in/instagram-ads-pricing-india-2026/ | UNREACHABLE (tool failure) | proxy refused; conservative input Rs 55 |
| economics-v2.md#C09 | Instagram CPC range, Education Rs 15-30 | https://bosswallah.com/blog/creator-hub/instagram-ads-cost-in-india-2026-how-much-should-you-actually-spend/ | UNREACHABLE (tool failure) | proxy refused |
| economics-v2.md#C09 | Meta CPC benchmarks, India | https://owlclaw.com/benchmarks/meta-ads-benchmarks-india | UNREACHABLE (tool failure) | proxy refused |
| economics-v2.md#C16 / forge-v2.md#C08, #C12 | NCH coaching complaints 4,815, 5,351, 16,276 (2021-22 to 2023-24) | https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes | UNREACHABLE (tool failure) | proxy refused; used for pool size and the free substitute |
| economics-v2.md#C16 / forge-v2.md#C07, #C13 | Rs 1.56 crore refunded to 600+ coaching students via NCH | https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres | UNREACHABLE (tool failure) | proxy refused; the Rs 26,000 per student figure is correct arithmetic but rests on this source |
| economics-v2.md#C18 | GST threshold Rs 20 lakh for services | https://www.kanakkupillai.com/gst-registration-online-in-pune | UNREACHABLE (tool failure) | proxy refused |
| prosecution-execution-v2.md#E1 (FE1 FATAL) | Delhi HC 2024 restricts non-advocates on authority letters; Regulations 2014 permit agents | https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024 | UNREACHABLE (tool failure) | proxy refused |
| prosecution-execution-v2.md#E2 (FE1 FATAL) | SC 2011 C. Venkatachalam v. Ajitkumar C. Shah, agents in consumer fora and s.33 | https://www.legalauthority.in/judgement/c-venkatachalam-vs-ajitkumar-c-shah-7906 | UNREACHABLE (tool failure) | proxy refused |
| prosecution-execution-v2.md#E4 (FE4 FATAL) | draft Maharashtra Private Coaching Centers Act 2026 with refund of unused fee; objections to 2026-09-04 | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | UNREACHABLE (tool failure) | refused twice |
| diff-v2.md#D2 | Mumbai District Commission v Rao IIT Academy, Rs 50,000, June 2024 | https://www.livelaw.in/amp/consumer-cases/mumbai-district-commission-rao-iit-academy-refund-coaching-fee-withdrawal-admission-261464 | UNREACHABLE (tool failure) | proxy refused |
| diff-v2.md#D2 / forge-v2.md#C03 | Central Delhi order Rs 62,363, 2024-10 | https://www.business-standard.com/india-news/consumer-forum-asks-coaching-centre-to-refund-fee-for-deficient-services-124100701035_1.html | UNREACHABLE (tool failure) | proxy refused |
| diff-v2.md#D2 / forge-v2.md#C23 | state told Bombay HC about draft coaching bill; MoE guidelines of 2024-01-16 | https://www.livelaw.in/amp/high-court/bombay-high-court/state-tells-court-draft-bill-regulating-coaching-centres-to-be-introduced-in-monsoon-session-287446 | UNREACHABLE (tool failure) | proxy refused |
| diff-v2.md#D9 | WhatsApp 24-hour reply window and opt-in rules | https://www.cm.com/blog/whatsapp-updates-opt-in-and-quality-rating-policy/ | UNREACHABLE (tool failure) | proxy refused; vendor summary |
| diff-v2.md#D4 | free guide does not give a calculator plus letter | https://www.pagalguy.com/articles/how-practical-is-it-to-seek-a-refund-from-your-coaching-institute-the-one-you-left-halfway | UNREACHABLE (tool failure) | proxy refused |
| prosecution-market-v2.md#C03 | Akosha: most revenue from enterprises by 2014, 22 paid brand customers | https://www.medianama.com/2014/07/223-akosha-5-million-onedirect-suite/ | UNREACHABLE (tool failure) | proxy refused; basis of FM1 and FM6 |
| 01-local-market.md#C22, forge-v2.md#C01 | Bhagirath fees Rs 65,000-95,000; registration Rs 5,000 / 10,000 non-refundable | https://collegedunia.com/institute/314-bhagirath-ias-academy-pune | UNREACHABLE (tool failure) | proxy refused. Note: 01-local-market.md states its own page fetches also failed, so this claim rests on search-result text |

## Struck claims
- economics-v2.md#C01 (Consumer Voice Rs 500) — UNREACHABLE (tool failure) — page not opened
- economics-v2.md#C01, diff-v2.md#D1 (IncorpX Rs 1,499) — UNREACHABLE (tool failure) — page not opened
- economics-v2.md#C01, diff-v2.md#D1 (Ebizfiling Rs 4,999, 4.8 rating) — UNREACHABLE (tool failure) — page not opened
- diff-v2.md#D1 (RegisterKaro 4.6 rating) — UNREACHABLE (tool failure) — page not opened
- economics-v2.md#C03 (UPI zero MDR) — UNREACHABLE (tool failure) — page not opened
- economics-v2.md#C08 (Balaji "pith and substance") — UNREACHABLE (tool failure) — page not opened
- economics-v2.md#C09 (Instagram CPC range, three vendor blogs) — UNREACHABLE (tool failure) — pages not opened
- economics-v2.md#C16 and forge-v2.md#C07, #C08, #C12, #C13 (NCH complaint counts and Rs 1.56 crore) — UNREACHABLE (tool failure) — pages not opened
- economics-v2.md#C18 (GST threshold) — UNREACHABLE (tool failure) — page not opened
- prosecution-execution-v2.md#E1, #E2 (FE1 FATAL evidence) — UNREACHABLE (tool failure) — pages not opened
- prosecution-execution-v2.md#E4 (FE4 FATAL evidence) — UNREACHABLE (tool failure) — page not opened
- diff-v2.md#D2 (Rao IIT order, Central Delhi order, Bombay HC bill status) — UNREACHABLE (tool failure) — pages not opened
- diff-v2.md#D4 (PaGaLGuY) and #D9 (cm.com WhatsApp policy) — UNREACHABLE (tool failure) — pages not opened
- prosecution-market-v2.md#C03 (Akosha revenue) — UNREACHABLE (tool failure) — pages not opened
- 01-local-market.md#C22 (Bhagirath fees) — UNREACHABLE (tool failure) — page not opened
- Tool-failure strikes: 23 of 23 URL rows. The Judge must not treat these as proof that the sources are false. The strikes follow rule 8, which has no exception, and the claims could not be confirmed.

## Assumptions in load-bearing positions
- economics-v2.md#C02 — ASSUMPTION used as the basis of the conservative price (Rs 500) and the base price (Rs 799); no buyer evidence
- economics-v2.md#C04, #C05 — ASSUMPTION used as the basis of conservative COGS (gateway 2% plus GST, 15% refund rate)
- economics-v2.md#C10, #C11 — ASSUMPTION used as the basis of the conservative funnel (1% click-to-paid) and the 24-customer volume
- economics-v2.md#C12, #C13, #C14, #C15, #C20 — ASSUMPTION used as the basis of conservative boost spend, time per file, fixed weekly hours, tool cost and months to first revenue (K2 and K6 fit)
- economics-v2.md#C06, #C07 — ASSUMPTION used as the basis of the refund reserve (Rs 8,000) and advocate opinion cost (Rs 5,000) in the K1 capital check
- forge-v2.md#C15 (Rs 799 acceptable), #C16 (30-45 minutes per file), #C17 (scope lawful for a non-advocate), #C18 (volume 15-30 files), #C19 (refund rate), #C21 (free NCH does not make the file redundant), #C26 (receipt deletion rule), #C27 (employment contract permits side work) — ASSUMPTION used as the basis of the economics inputs and of the KM/KE assessments
- forge-v2.md Path table (all conversions) — ASSUMPTION used as the basis of the conservative customer count
- prosecution-execution-v2.md FE1 and FE4 each rest partly on a statement that no authority or final law was found; this is an absence-of-evidence claim, not a sourced fact

## Summary
- verified: 11, misrepresented: 0, unreachable: 23 (of which tool failure: 23), unsourced: 0
- demand evidence surviving the audit: none. All seller-price anchors (Consumer Voice, IncorpX, Ebizfiling, RegisterKaro) and all NCH figures are struck as unreachable. Independently of the audit, diff-v2.md#D1 and prosecution-market-v2.md state that no seller showed paying-customer evidence. Economics arithmetic is correct; every economics input with a URL is struck.
