---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: prosecutor
version: 1
created: 2026-10-21T10:22:43Z
---

## Inputs read
- <scratch>/ventures/runs/2026-10-21-check-satara-english/00-contract.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/00-founder-knowledge.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/01-local-market.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/02-signals.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/kill-criteria.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/forge-v1.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/economics-v1.md
- <scratch>/ventures/runs/2026-10-21-check-satara-english/ideas/I01/simulation-v1.md

## Criteria assessment
Market side
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | 01-local-market.md#C01, #C12, #C24-C27, #C46; C03 below | One verified Satara price (Success, Rs 2,000). Breath (9 years) and Success (8 years) show years in business only, not dated price lists, batch counts or 5 reviews. Job 4U and Shivtej show no price. 0 of 4 have reviews. Tenure alone is not a "verifiable paid-service signal" under the threshold. Missing proof is mostly offline (calls, visits, Justdial, Google Maps), and nothing contradicts demand existing. Offline-only gap, but the criterion cannot be MET and a founder call yields FOUNDER-COUNTED only. |
| KM2 | INSUFFICIENT EVIDENCE | 01-local-market.md#C17, #C60; 02-signals.md S07 | No class 6-10 enrolment figure for Satara city exists in any file. Founder counted about 6 schools within 3 km, no student numbers. Population ratio would be ASSUMPTION. Obtainable by desk research (UDISE+ school-level sums). Forge narrowed to class 8-10 (forge-v1.md#C26 text), which cuts the base by about 40% on an equal-cohort ASSUMPTION and makes the 8,000 threshold harder to satisfy, not easier. |
| KM3 | INSUFFICIENT EVIDENCE | 01-local-market.md#C44, #C45, #C46; forge-v1.md#C03, #C04, #C16 | (a) The 30-student bus-stand batch is hearsay, and no second provider's batch size is verified. (b) No parent survey exists. (c) 0 public Satara complaints about missing speaking practice. 02-signals.md C06 also found none. Forge itself labels the gap an ASSUMPTION. Peer-town data shows no under-supply. (b) is an offline-only gap and can reach INSUFFICIENT at best. |
| KM4 | INSUFFICIENT EVIDENCE | 01-local-market.md#C12, #C24, #C26, #C11; C04 below | Survival case: Success (8 years) and Breath (9 years, but address given as Karad/Shnoli) exist. School-age focus is not verified for either. Graveyard: no closed Satara operators found, and the scout states closure status could not be checked. Only national BYJU'S closures were found. The "no provider at Rs 700 or less with batches of 15 or fewer" half rests on hearsay (the Rs 1,000/30-student class) plus unpriced listings. Offline price check needed. |
| KM5 | INSUFFICIENT EVIDENCE | forge-v1.md#C05, #C20, "How it works" step 4; 02-signals.md S05, S10 | Substitute prices are sourced (ChatGPT Go Rs 399, SpeakX Rs 299). The plan gives a format (about 35 min of student talk in pairs and groups, cap 20) but no minutes-per-student calculation, and its own #C20 calls adequacy an ASSUMPTION. Pair arithmetic gives about 17 min of talk per student if all pairs speak at once, but with 10 simultaneous pairs the teacher hears and corrects almost none of it, so "individual speaking time" and feedback are not shown. Parent preference over Rs 0-399 AI is unproven and the only support is vendor blogs, which the criterion excludes. A worked calculation could be written by desk research. Whether parents value it is offline-only. |

Execution side
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C07, #C09, "Calculations" (setup Rs 56,500; capital to first revenue Rs 71,100; peak Rs 79,011); simulation-v1.md (within-capital 69.1% vs 90% bar) | The builders' own conservative case has start-up Rs 56,500 against the Rs 40,000 limit, and start-up plus 3 months of rent plus supplies far above Rs 63,000 (peak outlay Rs 79,011 breaks HARD K1). Base case start-up is about Rs 33,500 (fits) but the criterion and rule 3 use the conservative case. Deposit months are an unsourced ASSUMPTION (rentok sheet not opened; national). No rent quote or listing for any named school. Hours: 11 steady, 12 in launch weeks, zero slack, no hired help. |
| KE2 | NOT MET | economics-v1.md#C17, #C25, student path (9 students in first revenue month); forge-v1.md#C14 | The conservative model reaches 9 paying students against the 10-student threshold, with first revenue at exactly 2.0 months and no slack (Diwali falls in the window). Base case 6% gives 18, but every conversion rate is an ASSUMPTION. The Q11 reach of 300 is FOUNDER-COUNTED. No dated room-to-first-class plan, no pre-enrolments, no peer-town conversion evidence. Forge's own total (8-12 from groups, 10-15 personal) is an ASSUMPTION. |
| KE3 | NOT MET | economics-v1.md "Calculations" (break-even 14; cumulative month 6 about -Rs 78,913; month 12 about -Rs 72,566); simulation-v1.md | Conservative break-even is 14 students against the limit of 12. Six-month cumulative cash is deeply negative after start-up. The locked conservative case (15 average students, 20% churn, no enrolment around Diwali and May) was not run: economics used 8% churn and no seasonal dips, and says the real path is slower. At 30 students, the net on the economics' own costs is 30 x 560 - 7,300 = Rs 9,500 before CAC, under Rs 10,000. The simulation shows 0.0% viable and the viable-on-paper bar NOT MET. A founder at 17.5 students nets about Rs 2,100 a month for 11-12 hours (about Rs 40 per hour). |
| KE4 | NOT MET | 01-local-market.md#C33-C39; 02-signals.md S01, R01, R03; forge-v1.md#C17, #C18, #C26; C01-C03 below | (a) Status checked: no final Act (see C01). (b) Class 8-10 is 3 of 5 classes, about 60% of the target band, under the 80% bar on an equal-cohort ASSUMPTION. Class 8 includes some 12-year-olds, and no parental-consent route is confirmed. (c) Plan is 2-3 batches of 20 for 40-60 students; per-centre counting is unresolved (forge-v1.md#C26), so registration likely applies. It is not budgeted or timed; economics has only Rs 3,000 for paperwork. (d) Shops and Establishments, GST and DPDP are listed but not resolved or costed (sources conflict, 01-local-market.md#C37). (e) Founder's employment status is an ASSUMPTION (forge-v1.md#C18). Under the strict reading no compliant plan at 30+ students is shown. |
| KE5 | NOT MET | forge-v1.md "Path to first 100 customers", "Positioning vs named competitors", "Moat over time"; economics-v1.md "Calculations" | Channels named: WhatsApp groups, personal contacts, referrals, Instagram, so at least 2. But no group-admin permission is confirmed (offline-only gap, FOUNDER-COUNTED at best). There is no written incumbent response plan for a Success/bus-stand price match or small batch, or for PhysicsWallah. Forge says "Moat otherwise: none yet." No 40%-below-plan sensitivity was run, and the conservative model is already below break-even, so a 40% shortfall (about 10.5 students vs 14 needed) fails by construction. |

## Market flaws
### FM1 — FIXABLE
- flaw: The central differentiator (a speaking-practice gap in Satara) rests entirely on founder hearsay. No public Satara review, search trend or survey shows it, and the peer-town benchmark shows no under-supply. Forge calls it an ASSUMPTION.
- evidence: [C05] Forge labels the speaking-time gap "ASSUMPTION: founder hearsay only" [source: forge-v1.md#C16]. [C06] No Google/Justdial review of any Satara spoken-English provider was found [source: 01-local-market.md#C46].
- what would fix it (FIXABLE only): at least 10 dated, named parent statements of willingness to pay at a stated speaking promise (FOUNDER-COUNTED, offline-only), or 5 public Satara complaints (desk research unlikely in a small town). Desk research alone cannot close this.
- fix would change customer/problem/revenue model: no

### FM2 — FIXABLE
- flaw: The Satara addressable base is unmeasured, and the forge has already cut it to class 8-10, where class 10 drops out around the Feb-Mar 2027 board exams and PhysicsWallah sells Foundation batches. Price evidence is one listing (Rs 2,000) plus hearsay.
- evidence: [C07] No class-wise Satara enrolment retrieved [source: 01-local-market.md#C17; coverage section]. [C08] PhysicsWallah Satara centre sells Foundation for classes 8-10 [source: https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044].
- what would fix it (FIXABLE only): school-level UDISE+ enrolments for Satara city schools summed for classes 6-10 and by medium. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: Cheap and free substitutes undercut the value claim. AI practice costs Rs 0-399 and SpeakX has about 200,000 paying subscribers and plans Marathi. The Rs 600 price sits below every visible Satara price, which signals a weaker product, while the parent-visible differentiator is untested. Local tuition at Rs 800-1,500 per subject is a different product, so it does not anchor a spoken-English price.
- evidence: [C09] SpeakX Rs 299/month, company-reported 200,000 paying subscribers, Marathi planned [source: https://india.entrepreneur.com/news-and-trends/speakxai-raises-usd-16-mn-to-strengthen-ai-powered-english/498354, 2025-10-15] (national). [C10] ChatGPT Go Rs 399/month in India [source: https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html, 2025-08-19] (national).
- what would fix it (FIXABLE only): a worked class format with measured minutes per student plus a pre-sale at Rs 600 vs Rs 900 with at least 10 paid pre-enrolments. The calculation is desk work. The pre-sale is offline-only.
- fix would change customer/problem/revenue model: no

## Execution flaws
### FE1 — FIXABLE
- flaw: In the conservative case the plan breaks HARD K1: peak cash out is about Rs 79,000 against Rs 75,000. K5 (loss cap) breaks too if the deposit is lost. The cause is the 6-month deposit assumption, which no Satara source supports. The simulation puts only 69.1% of runs within capital, against a 90% bar.
- evidence: [C11] Peak cumulative cash -Rs 79,011 [source: economics-v1.md "Calculations"]. [C12] Simulation within-capital share 69.1% [source: simulation-v1.md].
- what would fix it (FIXABLE only): two or more published Satara or Pune-region commercial room listings with deposit terms showing a deposit of 3 months or less, an itemised cost list, and a pre-sale before renting. Listings are obtainable by desk research (Maharashtra rental portals), and quotes are offline.
- fix would change customer/problem/revenue model: no

### FE2 — FIXABLE
- flaw: At the contract price of Rs 600 the founder earns very little for 11-12 hours a week with zero slack. Conservative month-12 cash is about Rs +2,092, cumulative -Rs 72,566, and the unrecovered non-refundable outlay is about 30 months from recovery. The business only becomes worth running at an untested Rs 800-1,000 price. Under the strict-law cap of 25 students per centre, the Rs 600 price tops out at about 25 x 560 - 7,300 = Rs 6,700 a month, under the Rs 10,000 KE3 test.
- evidence: [C13] Conservative month-12 cash flow +Rs 2,092 [source: economics-v1.md "Calculations"]. [C14] Draft threshold "more than 25 students for consideration" [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/].
- what would fix it (FIXABLE only): verified evidence that Satara parents pay Rs 800 or more for a small-batch speaking class (provider pages with prices, or at least 10 paid pre-enrolments at Rs 800+). Desk research can find provider prices only partly. The test is offline. Note that the contract price is Rs 600, and a higher price is a different offer from the one the user stated.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: Legal exposure is unresolved against a low-risk, Rs 75,000 cap. The draft Act bars enrolment under 13, caps at 25 students per centre (counting basis unclear), requires registration, and carries fines of Rs 1 lakh to Rs 50 lakh. The plan of 40-60 students across batches of 20 likely exceeds the line. The forge cuts class 6-7, which cuts the market. Founder's current employment is not stated, and the draft bars teachers of recognised schools. DPDP parental consent applies to the Instagram clips.
- evidence: [C01] Draft not final as of search on 2026-10-21 [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]. [C02] Teacher rule and under-13 rule wording [same source]. [C03] The article does not say whether 25 is per batch or per centre [same source, read 2026-10-21].
- what would fix it (FIXABLE only): the draft's full text or gazette notification, the Labour Department rule page for Shops and Establishments registration, and the founder's written employment status. The first two are obtainable by desk research. The third is offline-only. Until then the strict reading is the one to plan on.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: There is no incumbent response plan, and a copyable format. Success (Rs 2,000), the bus-stand class and PhysicsWallah can each match the price or form small batches. The forge states the moat is "none yet". PhysicsWallah plans 75+ new offline centres in FY27.
- evidence: [C15] PhysicsWallah plans 75+ offline centres in FY27 (national) [source: https://www.storyboard18.com/brand-marketing/physicswallah-ups-marketing-spend-by-50-in-h1-fy26-as-offline-expansion-accelerates-85566.htm, 2025-12-09].
- what would fix it (FIXABLE only): a written response plan, a 40%-shortfall sensitivity run, and a visit-based price and batch check of Success, Job 4U, Shivtej and the bus-stand class. The plan and run are desk work. The visits are offline-only.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Acquisition rests on the founder's 4 WhatsApp groups (FOUNDER-COUNTED, likely overlapping, 240-480 members before overlap), and group admins' permission for paid promotion is unconfirmed. Platform dependency on WhatsApp and Instagram is not addressed. Conversion rates are all ASSUMPTION, and the simulation shows reach and conversion as the two largest sensitivities.
- evidence: [C16] Reach and conversion rank 1 and 2 in sensitivity (swing about Rs 14,600 and Rs 13,700) [source: simulation-v1.md "Sensitivity"].
- what would fix it (FIXABLE only): written permission from at least 3 of 4 admins, and a 7-day demo pre-sale showing at least 10 paid sign-ups. Both are offline-only. A peer-town conversion benchmark could come from desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] No final version of the Maharashtra Private Coaching Centers Act was found as of 2026-10-21. Latest coverage describes a draft published 2026-08-20 with objections until 2026-09-04, and the search returned no news dated after late August 2026. A September/October development cannot be ruled out. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/; https://news.careers360.com/maharashtra-proposes-law-regulate-coaching-centres-cap-class-hours-seeks-objections-till-september-4-fee-refund-rules-counselling/amp]
- [C02] The draft covers coaching for "more than 25 students for consideration", bars enrolment below 13, and bars hiring graduates below graduate level and teachers working in recognised schools or junior colleges. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]
- [C03] The SCC Online article does not say whether the 25-student line counts per batch or per centre, and does not address sole tutors or rented premises. [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]
- [C04] Graveyard search result: no closed Satara or Karad spoken-English operator was found in the scout's files. The scout could not confirm current status of any listed provider. This is absence of evidence, not evidence of survival. [source: 01-local-market.md#C11]
- [C05] 3 of 4 listed Satara spoken-English providers show no price, 0 of 4 show reviews, and the only Satara rating found concerns a chemistry class. [source: https://m.indiamart.com/city/satara/coaching-classes.html]
- [C06] The simulation reports 0.0% viable runs, 69.1% within capital, and P50 cumulative cash after month 12 of -Rs 47,610. [source: simulation-v1.md]
- [C07] Economics conservative case omits the locked KE3 stress (20% churn, Diwali and May zero-enrolment windows) and uses 8% churn. [source: economics-v1.md#C18]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| - | - | Round 1. Not applicable. |
