---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: forge
version: 1
created: 2026-10-15T10:40:11Z
---

## Core identity
- customer: an individual student (or the parent paying for one) in Pune who has paid a classroom coaching institute (wedge: MPSC/UPSC institutes in Sadashiv Peth/Navi Peth, course fees about Rs 50,000-1,25,000) and has left, wants to leave, or was hit by a batch change, and has been told the fee is non-refundable
- problem: the institute refuses or ignores a refund request; the student does not know how to compute the pro-rata amount, how to word the demand, or how to file on the National Consumer Helpline (1915)
- revenue model: one-time fee per refund file (working price Rs 799), paid by UPI before delivery; no success fee; no legal advice or representation
- pivot declared: no

## How it works
1. Finding it: the student sees a Marathi or English Instagram reel or post, or a message in an MPSC/UPSC aspirant WhatsApp/Telegram group, titled around "fee not refunded". Telegram aspirant channels exist for MPSC (e.g. https://t.me/s/mpsc_sci appeared in a search result; content not opened). A Google Business/Instagram profile gives a WhatsApp number.
2. The student sends photos of the fee receipt, the admission form/terms, dates attended, and any messages from the institute, over WhatsApp.
3. The founder enters the figures in a Google Sheet template: total fee, non-refundable registration, months or classes consumed, pro-rata balance, and the Ministry of Education January 2024 guideline and consumer-commission reasoning that support it.
4. Delivery within 48 hours: (a) the calculation sheet, (b) a refund demand letter in English or Marathi for the student to send by registered post/email, (c) a step list for filing on 1915 and, if the institute refuses, on the e-Daakhil consumer-commission portal, where sources say claims up to Rs 5 lakh carry no filing fee.
5. Weekly founder work (about 10 hours): answer WhatsApp enquiries, produce files (30-45 minutes each, ASSUMPTION), post 2-3 pieces of content, join or answer in aspirant groups, keep a log of outcomes (did the student get a refund) to use as anonymised proof.
- Tools: Google Sheets, Google Docs templates, WhatsApp Business, Instagram, UPI QR/payment link. No inventory, no licence, no physical work.
- Boundary: the founder is not an advocate. Files state they are a calculation and a template, not legal advice. Whether charging for letter drafting by a non-lawyer is permitted was not verified (see Assumptions).

## Need gap
- [C01] Pune MPSC/UPSC classroom courses cost about Rs 50,000-1,25,000, with Rs 5,000-10,000 registration listed as non-refundable (Bhagirath, Dnyandeep, Prithvi) [source: https://collegedunia.com/institute/314-bhagirath-ias-academy-pune ; https://collegedunia.com/institute/4208-dnyandeep-academy-pune-pune ; also in 01-local-market.md#C22-C24]
- [C02] The Ministry of Education coaching guidelines (circulated to states 2024-01-16) provide for an easy exit policy and pro-rata refunds, but they are advisory; enforcement depends on state adoption, which was not verified for Maharashtra (national) [source: https://rsdebate.nic.in/bitstream/123456789/750740/1/PQ_265_31072024_U983_p142_p143.pdf]
- [C03] Consumer commissions have held "non-refundable" clauses untenable and ordered pro-rata refunds, e.g. a New Delhi forum against Brilliant Tutorials and a Central Delhi commission order of Rs 62,363 for unused months (other city: Delhi) [source: https://tribuneindia.com/news/coaching-centres-can-charge-fee-only-for-services-rendered ; https://www.business-standard.com/india-news/consumer-forum-asks-coaching-centre-to-refund-fee-for-deficient-services-124100701035_1.html]
- [C04] A Pune District Consumer Forum order of Rs 25,000 with 9% interest plus Rs 10,000 for a coaching refund exists; the enrolment was in 2014 and the order date is not given [source: https://lawtrend.in/consumer-court-directs-coaching-institute-to-refund-rs-25000-along-with-rs-10000-as-compensation-to-the-student]
- [C05] What it costs the student today: the loss itself (Rs 5,000-10,000 registration up to a large share of Rs 50,000-1,25,000), or a lawyer-drafted notice. Priced notice options found: Consumer Voice "Consumer Mitra" lists drafting and issuing a legal notice at Rs 500 plus postage; IncorpX lists Rs 1,499 plus Rs 60-80 postage (national) [source: https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting]
- [C06] Where that falls short: those offerings are generic national consumer-notice services, not coaching-specific, and none was found that computes the pro-rata amount from a Pune institute's receipt, offers Marathi, or is reachable through aspirant groups. This is an absence in search results, which is weak evidence [ASSUMPTION: gap based on not finding such a service in 6 searches on 2026-10-15]
- [C07] Free route exists: NCH (1915) intervention, and the Department of Consumer Affairs reported Rs 1.56 crore refunded to 600+ coaching students through it as of 2025-02 (national) [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]
- [C08] Why open now: NCH coaching complaints rose from 4,815 (2021-22) to 5,351 (2022-23) to 16,276 (2023-24), and the January 2024 guidelines gave students a document to cite (national, press reports of government statements) [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes ; https://www.etvbharat.com/en/!bharat/secured-over-rs-1-crore-relief-for-students-from-coaching-centres-via-nch-govt-enn25022202697]

## How it makes money
- who pays, for what, how much, how often: the student or parent pays once, about Rs 799 per refund file, before delivery. Price sits between the Rs 500 and Rs 1,499 notice prices found (C05) [ASSUMPTION: Rs 799 is untested].
- other revenue (if any): none planned. Optional later add-on: Marathi/English letter-review for fee disputes at other Pune providers (same customer type, same problem).
- what one sale costs to deliver, and what drives the margin: founder time (30-45 minutes, ASSUMPTION), UPI fee and tools; near-zero cash cost per file. Margin is driven by file volume and by how many enquiries convert, which is limited by the infrequent trigger (a student leaves or is refused).
- (the numbers are modelled in economics-v1.md)

## Persona
- [C09] Student or parent in Pune, usually 20-30 years old for MPSC/UPSC, many from outside the city; Pune's coaching economy is described as smaller than Kota or Delhi, with most students local plus some from Marathwada and Vidarbha. No headcount of Pune MPSC/UPSC aspirants was found [source: https://theprint.in/india/education/punes-rise-as-a-coaching-hub-its-cheaper-than-delhi-more-human-than-kota/2882455/ ; search-result summary only, page not opened]
- [C10] Spends today: Rs 50,000-95,000 per classroom course, plus Rs 3,500-5,500 for online MPSC test series (Drishti) (national for the online price) [source: https://www.drishtiias.com/mpsc-prelims-test-series ; 01-local-market.md#C22-C25]
- [C11] Pune MPSC aspirants are an organised, active group (protests over alleged paper leaks in September 2026), which suggests reachable communities [source: https://www.freepressjournal.in/pune/pune-mpsc-aspirants-to-resume-agitation-from-september-26-says-mla-rohit-pawar]

## Narrowest wedge
- Segment: MPSC/UPSC classroom students in Sadashiv Peth/Navi Peth/Shivajinagar who paid Rs 50,000+ and want to leave or were hit by batch merge/cancellation, within roughly the first 3-4 months of a course when the unused share is large.
- Product: one file (sheet + letter + 1915 steps), Rs 799, delivered over WhatsApp. Nothing else in v1.
- First paid transaction target: a student reached through one aspirant group within weeks 2-4.

## Problem severity
- [C12] NCH coaching complaints: 16,276 in 2023-24 (national), with non-refund of enrolment fee named as a common type [source: https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes]
- [C13] Amounts are material: 600+ students recovered Rs 1.56 crore via NCH, about Rs 26,000 each on average (arithmetic from C07; national) [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]
- [C14] Pune-specific complaint volume was not found. A Pune forum has treated the issue (C04, undated), and 01-local-market.md#C47 cites a Pune consumer forum holding. Frequency per Pune student is unknown.
- Severity is high per incident and low in frequency; the Rs 799 fee is small relative to the sums at stake.

## Path to first 100 customers
Target market: Pune. All conversion numbers below are ASSUMPTION; no Pune conversion data exists.
| channel | reach | conversion | customers | status |
|---|---|---|---|---|
| Instagram reels/posts in Marathi and English on "coaching fee refund" | ~20,000 views over 3 months | 0.1% become paid | ~20 | ASSUMPTION |
| MPSC/UPSC WhatsApp and Telegram groups (answering refund questions, no spam) | 15 groups x ~300 members = 4,500 | 0.5% | ~22 | ASSUMPTION; group access not verified |
| Google search/Google Business profile for "coaching fee refund Pune" | unknown; no search volume found | ~5 files/month | ~15 | ASSUMPTION |
| Referrals from refunded students (they know classmates) | - | 0.3 per customer | ~15 | ASSUMPTION |
- Sum is about 70 over 3 months under these assumptions, which falls short of 100 inside the K6 window. 100 customers is more likely reached in 5-8 months. Revenue at Rs 799: 100 customers = Rs 79,900 total.
- Cost to reach: content time plus Rs 0-5,000 in Instagram boosts (ASSUMPTION).
- Unsourced: reach, conversion, group sizes. Sourced: price anchors (C05), complaint volume nationally (C12).

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| Consumer Voice "Consumer Mitra" | https://join.consumer-voice.org/legal/ | notice drafting and issuing Rs 500 plus postage; a separate page lists Rs 499 registration for advice (page extraction conflicting) | coaching-specific pro-rata calculation, Marathi, same-week delivery; they issue a lawyer notice, we do not | C05 |
| IncorpX legal notice | https://www.incorpx.io/legal-notice-drafting | Rs 1,499 plus Rs 60-80 postage, 3-5 working days | lower price, faster, coaching-specific; they use lawyers, we do not | C05 |
| National Consumer Helpline 1915 | https://consumerhelpline.gov.in | free | we help prepare the case the helpline needs; the free route competes directly | C07 |
| e-Daakhil / district commission | https://edaakhil.nic.in (as named in guides; official site not opened) | no filing fee for claims up to Rs 5 lakh per guides | none in the legal process; we only prepare the documents | search result, https://www.sansalegal.com/post/how-to-file-a-consumer-complaint-online-in-india-through-e-daakhil |
| Free guides (PaGaLGuY, Better India, LawRato Q&A) | https://www.pagalguy.com/articles/how-practical-is-it-to-seek-a-refund-from-your-coaching-institute-the-one-you-left-halfway | free | personalised calculation and a ready letter | 01-local-market.md#C47 |
| A local advocate | not priced | price not found | no court appearance | ASSUMPTION |

## Moat over time
- None initially. Possible slow accumulation: a log of outcomes by institute (which institutes refund after a letter) and Marathi templates. Both are copyable and depend on volume that may not arrive.

## Assumptions
- [C15] Rs 799 is acceptable to the student [ASSUMPTION: about 1% of an Rs 80,000 course and between the Rs 500 and Rs 1,499 notice prices; untested]
- [C16] 30-45 minutes of founder time per file [ASSUMPTION: template-driven]
- [C17] Non-lawyer may sell a calculation and a letter template without breaching the Advocates Act; not researched. A legal-risk check is needed before launch [ASSUMPTION: document-drafting is commonly offered by non-lawyers, not verified]
- [C18] Enough Pune students leave or are refused each month to supply 15-30 files [ASSUMPTION: no Pune volume found]
- [C19] Letters actually produce refunds at a meaningful rate; no success-rate data found. If rates are low, reviews and referrals stall [ASSUMPTION]
- [C20] Aspirant WhatsApp/Telegram groups permit helpful posts [ASSUMPTION]
- [C21] The free government route (NCH, plus PM-announced free online coaching, 01/02 S10) does not make a Rs 799 file redundant; students may prefer the free route [ASSUMPTION; contrary risk acknowledged]
- [C22] Demand evidence here is listing prices and national complaint counts; no revenue data for any seller of this exact service was found.

## Fixes (round 2 only)
- none
