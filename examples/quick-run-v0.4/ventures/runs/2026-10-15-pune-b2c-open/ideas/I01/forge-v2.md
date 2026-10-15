---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: forge
version: 2
created: 2026-10-15T10:49:00Z
---

## Core identity
- customer: an individual student (or the parent paying for one) in Pune who has paid a classroom coaching institute (wedge: MPSC/UPSC institutes in Sadashiv Peth/Navi Peth, course fees about Rs 50,000-1,25,000) and has left, wants to leave, or was hit by a batch change, and has been told the fee is non-refundable
- problem: the institute refuses or ignores a refund request; the student does not know how to compute the pro-rata amount, how to word the demand, or how to file on the National Consumer Helpline (1915)
- revenue model: one-time fee per refund file (working price Rs 799), paid by UPI before delivery; no success fee; no legal advice or representation
- pivot declared: no

## How it works
Unchanged from forge-v1 except one scope narrowing required by fix FM5/FE1 (see Fixes): the deliverable is (a) the pro-rata calculation sheet, (b) a generic, fill-in-the-blanks demand-letter template (English and Marathi) that the student completes and sends, and (c) a step list for 1915 and e-Daakhil. The founder does not write a bespoke letter and does not file on the student's behalf.
1. Finding it: the student sees a Marathi or English Instagram reel or post, or a message in an MPSC/UPSC aspirant WhatsApp/Telegram group, titled around "fee not refunded". A Google Business/Instagram profile gives a WhatsApp number.
2. The student sends photos of the fee receipt, the admission form/terms, dates attended, over WhatsApp (the student starts the conversation; the founder only replies to inbound messages).
3. The founder enters the figures in a Google Sheet template: total fee, non-refundable registration, months or classes consumed, pro-rata balance.
4. Delivery within 48 hours: the calculation sheet, the generic letter template, the 1915 / e-Daakhil step list.
5. Weekly founder work: see the hours table under Path to first 100 customers.
- Tools: Google Sheets, Google Docs templates, WhatsApp Business, Instagram, UPI QR/payment link.
- Boundary: the founder is not an advocate. Files state they are a calculation and a template, not legal advice.

## Need gap
Unchanged from forge-v1 (C01-C08), plus additions:
- [C01] Pune MPSC/UPSC classroom courses cost about Rs 50,000-1,25,000, with Rs 5,000-10,000 registration listed as non-refundable (Bhagirath, Dnyandeep, Prithvi) [source: https://collegedunia.com/institute/314-bhagirath-ias-academy-pune ; https://collegedunia.com/institute/4208-dnyandeep-academy-pune-pune ; also in 01-local-market.md#C22-C24]
- [C02] The Ministry of Education coaching guidelines (circulated 2024-01-16) provide for an easy exit policy and pro-rata refunds, but are advisory (national) [source: https://rsdebate.nic.in/bitstream/123456789/750740/1/PQ_265_31072024_U983_p142_p143.pdf]
- [C03] Consumer commissions have held "non-refundable" clauses untenable and ordered pro-rata refunds, e.g. a New Delhi forum against Brilliant Tutorials and a Central Delhi commission order of Rs 62,363 for unused months (other city: Delhi) [source: https://tribuneindia.com/news/coaching-centres-can-charge-fee-only-for-services-rendered ; https://www.business-standard.com/india-news/consumer-forum-asks-coaching-centre-to-refund-fee-for-deficient-services-124100701035_1.html]
- [C04] A Pune District Consumer Forum order of Rs 25,000 with 9% interest plus Rs 10,000 exists; enrolment 2014, order date not given [source: https://lawtrend.in/consumer-court-directs-coaching-institute-to-refund-rs-25000-along-with-rs-10000-as-compensation-to-the-student]
- [C05] Priced notice options: Consumer Voice "Consumer Mitra" Rs 500 plus postage; IncorpX Rs 1,499 plus Rs 60-80 postage (national) [source: https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting]
- [C06] No coaching-specific pro-rata calculator plus ready letter was found in 6 searches on 2026-10-15 and 1 further search on the same date; the search summary stated no ready-made calculator or template surfaced. Absence in search results is weak evidence [ASSUMPTION: gap based on searches, pages not opened]
- [C07] Free route: NCH (1915); Department of Consumer Affairs reported Rs 1.56 crore refunded to 600+ coaching students as of 2025-02 (national) [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]
- [C08] NCH coaching complaints rose from 4,815 (2021-22) to 5,351 (2022-23) to 16,276 (2023-24) (national) [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes]
- [C23] Maharashtra status of the 2024-01-16 MoE guidelines: the state told the Bombay High Court that the Union issued guidelines on 2024-01-16 asking states to frame a legal framework; Maharashthra's own draft "Maharashtra Private Coaching Centers (Registration and Regulation) Act, 2026" invited objections until 2026-09-04, is described as a proposal not yet passed, and one report says it would be tabled in the winter session. Coaching associations oppose it, and an earlier 2017 draft never reached the legislature (Maharashtra; search-result summaries, pages not opened) [source: https://www.livelaw.in/amp/high-court/bombay-high-court/state-tells-court-draft-bill-regulating-coaching-centres-to-be-introduced-in-monsoon-session-287446 ; https://news.careers360.com/maharashtra-proposes-law-regulate-coaching-centres-cap-class-hours-seeks-objections-till-september-4-fee-refund-rules-counselling ; https://www.deccanchronicle.com/nation/maharashtra-to-introduce-law-regulating-private-coaching-classes-1969073]

## How it makes money
- who pays, for what, how much, how often: the student or parent pays once, about Rs 799 per refund file, before delivery [ASSUMPTION: Rs 799 untested].
- other revenue (if any): none planned.
- what one sale costs to deliver, and what drives the margin: founder time and UPI fee; near-zero cash cost per file. Added cost line from fix FM5: a refund reserve for the money-back guarantee (see Fixes).
- (the numbers are modelled in economics-v2.md)

## Persona
- [C09] Student or parent in Pune, usually 20-30 years old for MPSC/UPSC, many from outside the city [source: https://theprint.in/india/education/punes-rise-as-a-coaching-hub-its-cheaper-than-delhi-more-human-than-kota/2882455/ ; search-result summary only]
- [C10] Spends today: Rs 50,000-95,000 per classroom course, plus Rs 3,500-5,500 for online MPSC test series (national for the online price) [source: https://www.drishtiias.com/mpsc-prelims-test-series ; 01-local-market.md#C22-C25]
- [C11] Pune MPSC aspirants are organised (protests over alleged paper leaks, September 2026) [source: https://www.freepressjournal.in/pune/pune-mpsc-aspirants-to-resume-agitation-from-september-26-says-mla-rohit-pawar]
- [C24] An aspirant quoted by Free Press Journal estimated 1.5 to 2 lakh MPSC/UPSC aspirants in Pune; this is one person's estimate, not an official count [source: https://www.freepressjournal.in/amp/pune/mpsc-aspirants-in-pune-struggle-with-high-rents-poor-living-conditions-exam-delays-govt-should-focus-on-us-too ; search-result summary only]
- [C25] SPPU's free UPSC/MPSC coaching centre received 1,631 applications for 2025-26 (one programme) [source: same Free Press Journal search result, summary only]

## Narrowest wedge
Unchanged: MPSC/UPSC classroom students in Sadashiv Peth/Navi Peth/Shivajinagar who paid Rs 50,000+ and want to leave or were hit by batch merge/cancellation within about the first 3-4 months. Product: one file (sheet + generic letter template + 1915 steps), Rs 799, over WhatsApp.

## Problem severity
- [C12] NCH coaching complaints: 16,276 in 2023-24 (national) [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes]
- [C13] 600+ students recovered Rs 1.56 crore via NCH, about Rs 26,000 each (arithmetic; national) [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]
- [C14] Pune-specific and Maharashtra education/coaching grievance counts were not found in a further search on 2026-10-15; only all-category figures (Maharashtra district commissions 2018: 14,963 filed) surfaced [source: https://eparlib.nic.in/bitstream/123456789/991527/1/AU185.pdf ; search-result summary only; all categories, 2018]
- Severity is high per incident and low in frequency.

## Path to first 100 customers
Target market: Pune. Conversion numbers are ASSUMPTION; no Pune conversion data exists.
| channel | reach | conversion | customers | status |
|---|---|---|---|---|
| Instagram reels/posts in Marathi and English on "coaching fee refund" | ~20,000 views over 3 months | 0.1% paid | ~20 | ASSUMPTION |
| MPSC/UPSC WhatsApp and Telegram groups (answering refund questions) | 15 groups x ~300 = 4,500 | 0.5% | ~22 | ASSUMPTION; no Pune group with a verified follower count was found |
| Google search/Google Business profile | unknown | ~5 files/month | ~15 | ASSUMPTION |
| Referrals from refunded students | - | 0.3 per customer | ~15 | ASSUMPTION |
- Sum is about 70 over 3 months under these assumptions, below 100 inside the K6 window. 100 customers is more likely reached in 5-8 months.
- Day-30 plan (design, not evidence): week 1 build sheet, letter template, Instagram and Google Business profile, 5 timed dry-run files from sample receipts; week 2 publish 6 posts/reels and answer questions in groups the founder can join; week 3 same plus ask first customers for referral; week 4 review. Target by day 30: 30 students who have sent an inbound message and ~3-8 paid files [ASSUMPTION: 10-25% enquiry-to-paid]. Reaching 30 inbound enquiries needs about 1,500-3,000 targeted views at 1-2% message rate [ASSUMPTION].
- Paid acquisition check (FE2/FE3): Indian Instagram CPC is reported at roughly Rs 6-55, with most sources clustering Rs 10-25 (vendor blogs) [source: https://upgrowth.in/instagram-ads-pricing-india-2026/ ; https://owlclaw.com/benchmarks/meta-ads-benchmarks-india ; search-result summaries]. At Rs 15 per click, 10% of clicks starting a chat and 20% of chats paying (both ASSUMPTION), cash CAC is Rs 750, above a Rs 150 target. A Rs 150 cash CAC is only reachable through unpaid channels, whose conversion is unmeasured. The 15 paid files per month at Rs 150 CAC is not supported by evidence.
- WhatsApp rule: vendor guides state that replies to an inbound message are allowed in a 24-hour customer-service window and that business-initiated messages outside it need prior opt-in and approved templates; Meta's own policy page was not opened [source: https://www.cm.com/blog/whatsapp-updates-opt-in-and-quality-rating-policy/ ; search-result summary]. Design: the founder only replies to inbound messages and never messages first.
- Weekly hours at 15 files a month (about 4 files a week), using the 45-minute-per-file input [ASSUMPTION; dry run not yet done]:
| activity | hours per week |
|---|---|
| file production (4 x 0.75) | 3.0 |
| WhatsApp replies and enquiries | 2.0 |
| content (2-3 posts/reels) | 2.5 |
| group answers | 1.0 |
| outcome log and admin | 0.5 |
| total | 9.0 |
- This table is under 10 hours in every week only if file time is 45 minutes or less and replies stay at 2 hours. Weeks with 6 files (24 min of extra production per file beyond the table) reach about 10.5 hours [arithmetic]. The check is a design, not a measurement.
- Revenue at Rs 799: 100 customers = Rs 79,900 total.

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| Consumer Voice "Consumer Mitra" | https://join.consumer-voice.org/legal/ | notice drafting and issuing Rs 500 plus postage | coaching-specific pro-rata sheet, Marathi; they issue a lawyer notice, we do not | C05 |
| IncorpX legal notice | https://www.incorpx.io/legal-notice-drafting | Rs 1,499 plus Rs 60-80 postage | lower price, coaching-specific; they use lawyers, we do not | C05 |
| Ebizfiling consumer complaint letter | https://ebizfiling.com/service/consumer-complaint-letter/ | from Rs 4,999; self-published 4.8 rating | lower price; generic template only | search-result summary, page not opened |
| RegisterKaro consumer complaint | https://www.registerkaro.in/consumer-complaint | price not extracted; self-published 4.6 Google rating | coaching-specific | search-result summary, page not opened |
| LawRato advocate answers | https://lawrato.com/documentation-legal-advice/legal-notice-typical-service-fee-237671 | one 2026 answer quotes Rs 3,000 for a money-recovery notice | no advocate | search-result summary |
| National Consumer Helpline 1915 | https://consumerhelpline.gov.in | free | we only prepare inputs; free route competes directly | C07 |
| e-Daakhil / district commission | https://www.sansalegal.com/post/how-to-file-a-consumer-complaint-online-in-india-through-e-daakhil | no filing fee up to Rs 5 lakh per guides | none in legal process | search result |
| Free guides (PaGaLGuY, Better India, righttoinformation.wiki) | https://www.pagalguy.com/articles/how-practical-is-it-to-seek-a-refund-from-your-coaching-institute-the-one-you-left-halfway | free | personalised sheet; guides describe the method in prose (pages not opened this round, so whether they contain templates is unknown) | C06 |
- Itemised difference of the Rs 799 file versus NCH and free guides [ASSUMPTION: from product design, unverified with buyers]: (1) arithmetic on the student's own receipt, (2) Marathi/English fill-in letter, (3) step list tied to the student's institute, (4) 48-hour turnaround; NCH provides none of (1)-(3) as documents and the free guides were not shown to provide (1).

## Moat over time
- None initially. Possible: an anonymised outcome log by institute and Marathi templates, both copyable. Buildable inside budget: the outcome log (cost: founder time; consent wording needed). Unproven.

## Assumptions
- [C15] Rs 799 is acceptable to the student [ASSUMPTION: about 1% of an Rs 80,000 course; untested]
- [C16] 30-45 minutes per file [ASSUMPTION: no dry run yet]
- [C17] Scope limited to calculator plus generic template is permissible for a non-advocate [ASSUMPTION: see Fixes FM5; no authoritative text opened]
- [C18] Enough Pune students leave or are refused each month to supply 15-30 files [ASSUMPTION: no Pune volume found]
- [C19] Letters produce refunds at a meaningful rate [ASSUMPTION: no success-rate data]
- [C20] Aspirant groups permit helpful posts [ASSUMPTION]
- [C21] The free NCH route does not make a Rs 799 file redundant [ASSUMPTION; contrary risk acknowledged]
- [C22] Demand evidence is listing prices and national complaint counts; no revenue data for any seller of this exact service was found.
- [C26] Receipts are deleted from the founder's devices 30 days after delivery [ASSUMPTION: design rule; Indian data protection law not researched]
- [C27] The founder's employment contract permits the side business (K9) [ASSUMPTION: contract not checked]

## Fixes (round 2 only)
| flaw id | fix | evidence url |
|---|---|---|
| FM1 / KM1 / KE4 | Partly fixed. Sellers found (all search-result summaries, pages not opened, none dated within 24 months by the summary, none in Maharashtra, review counts not obtained): IncorpX Rs 1,499 (advocates, 3-5 days), Ebizfiling consumer complaint letter from Rs 4,999 (self-published 4.8 rating), RegisterKaro consumer complaint (self-published 4.6 Google rating), LawRato advocate quote Rs 3,000 (2026). Fewer than 2 with 10+ reviews or a stated case count. No shut-down consumer-grievance startup with a cause of death was found (Akosha 2011 and Resolver 2019 profiles found, status unknown). No evidence found on buyers paying while free NCH 1915 exists. Not fixed to the stated bar. | https://www.incorpx.io/legal-notice-drafting ; https://ebizfiling.com/service/consumer-complaint-letter/ ; https://www.registerkaro.in/consumer-complaint |
| FM2 / KM4 | Orders in last 36 months (news summaries, orders not opened): Mumbai District Commission v Rao IIT Academy, June 2024, Rs 50,000 fee kept after student withdrew (Maharashtra); Nagpur commission ordered Rs 1.35 lakh refund from an IIT coaching centre, reported July 2026 (Maharashtra; ground was non-start of classes, not a non-refundable clause); Delhi State Commission upheld refund of about Rs 60,750 against Fitjee, reported January 2025; Central Delhi order Rs 62,363, 2024-10 (C03); a Delhi commission found Fitjee's enrolment form without an exit clause one-sided and unconscionable. Maharashtra status of the MoE guidelines: advisory, state draft Act 2026 not passed (C23). Count of orders on a non-refundable clause specifically, in the last 36 months: 2-3 from Delhi, 0 confirmed from Maharashtra. Partly fixed. | https://www.livelaw.in/amp/consumer-cases/mumbai-district-commission-rao-iit-academy-refund-coaching-fee-withdrawal-admission-261464 ; https://www.business-standard.com/india-news/consumer-forum-asks-coaching-centre-to-refund-fee-for-deficient-services-124100701035_1.html ; https://www.livelaw.in/amp/high-court/bombay-high-court/state-tells-court-draft-bill-regulating-coaching-centres-to-be-introduced-in-monsoon-session-287446 |
| FM3 / KM2 | not fixed. No Maharashtra or Pune count of 2,000 coaching grievances per year and no count of 50,000 paying Pune enrolments was found. Only an anecdotal 1.5-2 lakh aspirant estimate (C24), which is not enrolments and not a source meeting the stated bar. | NONE |
| FM4 / KM3 | Partly fixed. A search found no ready-made coaching refund calculator or template; free guides describe the process in prose (pages not opened). An itemised difference table is in Positioning. Whether buyers pay for comparable kits: no evidence found. The free guides' content was not opened, so "no free calculator plus letter exists" is not established. | https://www.pagalguy.com/articles/how-practical-is-it-to-seek-a-refund-from-your-coaching-institute-the-one-you-left-halfway |
| FM5, FE1 / KE2 | Partly fixed. Authority found: Bar Council of India v A.K. Balaji (2018) is reported to say that support services may fall under the Advocates Act if "in pith and substance" they amount to practice of law, a case-by-case test (summary; judgment not opened; the case concerned foreign lawyers). One DIY guide argues that Section 30 restricts appearance, not sending a personal demand notice (single non-authoritative source). Scope redefined to calculator plus generic fill-in template, no bespoke letter, no filing on behalf, no advice on merits. Refund policy: full Rs 799 refund within 7 days if the student cannot use the file; loss capped at Rs 799 per file; reserve of Rs 8,000 for about 10 refunds [ASSUMPTION: reserve size]; advocate opinion budgeted at about Rs 5,000 [ASSUMPTION per Judge's figure]. Total under Rs 10,000. No comparable non-lawyer service confirmed operating. | https://itatonline.org/archives/?p=18108 ; https://www.amalegalsolutions.com/how-can-i-send-a-legal-notice-online-to-someone-in-india-without-hiring-a-lawyer |
| FM6 | not fixed. Akosha (consumer legal services, 2011 profile) and Resolver (consumer grievance, founded 2019) found; no revenue or shutdown evidence, no cause of death. | NONE |
| KM5 | not fixed. No Pune-based or Marathi MPSC/UPSC community with verified follower counts was found. The only count is a Maharashtra-wide Telegram/YouTube channel "Mpsc Point" at about 111K on a PlayBoard index (may be outdated; not Pune-specific; not a complaints forum). No set of 10 dated public posts about coaching refunds was found. | NONE |
| FE2, FE3 / KE3 | Partly fixed. CPC figure sourced (Rs 10-25 cluster, vendor blogs). WhatsApp policy sourced from a vendor summary only; Meta's page not opened. Inbound-only design stated. Computed cash CAC for paid ads is about Rs 750 under assumed conversion, so Rs 150 CAC and 15 paid files per month are not shown. No comparable Indian service conversion data found. | https://upgrowth.in/instagram-ads-pricing-india-2026/ ; https://www.cm.com/blog/whatsapp-updates-opt-in-and-quality-rating-policy/ |
| FE5 / KE5 | Partly fixed as written design: day-30 plan with numbers (30 inbound students, 3-8 paid files) in Path section; guarantee terms: Rs 799 refunded within 7 days if the student cannot use the file, and the file's value does not depend on the institute paying; if the institute refuses, the student keeps the 1915 and e-Daakhil steps and no further payment is due; retention rule: receipts deleted after 30 days (C26); asset: outcome log by institute. No external evidence supports the moat. | NONE |
| FE6 / KE1 | Partly fixed. Hours table at 15 files a month in Path section: about 9 hours per week, with the stated limit that heavier weeks reach about 10.5 hours. The timed dry run of 5 files and the employment-contract check (C27) are the founder's own actions and are not done. | NONE |
