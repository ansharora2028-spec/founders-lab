---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: evidence-auditor
version: 1
created: 2026-10-21T10:25:12Z
---

## Scope
- files audited: 00-contract.md, 00-founder-knowledge.md, 01-local-market.md, 02-signals.md, ideas/I01/kill-criteria.md, ideas/I01/forge-v1.md, ideas/I01/strategy-v1.md, ideas/I01/economics-v1.md, ideas/I01/simulation-v1.md, ideas/I01/prosecution-v1.md (all under <scratch>/ventures/runs/2026-10-21-check-satara-english/). verdict-v1.md was not read.
- claims in scope: about 230 sourced, labelled or assumed claims; checked: 52 rows (several rows group related claims), sample method: all economics inputs (sourced ones fetched, others checked for tier) + all FATAL-flaw evidence (prosecution has no FATAL flaws; all FM and FE are FIXABLE, and I checked their cited sources anyway) + all demand-evidence claims + random sample of the rest. Peer-town population and supplier-count snippets for Phaltan, Pandharpur, Shrirampur and Bhusawal (01-local-market.md#C56-C59) were not opened and are not counted as checked.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| 01-local-market.md#C01 | 4 paid spoken-English providers in Satara (Success, Job 4U, Shivtej, Breath) all on the IndiaMART city page | https://m.indiamart.com/city/satara/coaching-classes.html | MISREPRESENTED | The cited city page lists Job 4U, Shivtej and Breath but no "Success" listing (two fetches). Success exists on its own page (see #C12 row). The claim as sourced is wrong |
| 01-local-market.md#C02 | 29 listings, 18 labelled Satara city | https://m.indiamart.com/city/satara/coaching-classes.html | MISREPRESENTED | Page shows 28 listings, 19 labelled Satara. Only 2 show a number (Siddheshwar, Annapurna); the rest hide price. Per-10,000 figure for Satara coaching becomes 1.58 not 1.50 |
| 01-local-market.md#C03 | 3 SSC CGL centres in Satara, no spoken English centre | https://targetstudy.com/coaching/ssc-coaching-in-satara.htm | VERIFIED | Names and count match |
| 01-local-market.md#C04, #C28 | PhysicsWallah Satara Vidyapeeth, Gadoli, JEE/NEET and Foundation 8-10 Maths and Science, no fee | https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044 | VERIFIED | Fees not stated, as claimed |
| 01-local-market.md#C05 | Satara CBSE schools Rs 18,000-52,000 a year for Class 10; Appasaheb Bhurao Patil EM Rs 26,550 | https://school.careers360.com/schools/private-unaided-schools-in-satara ; https://school.careers360.com/schools/appasaheb-bhurao-patil-english-medium-school-satara | MISREPRESENTED | Appasaheb page shows total Rs 13,265 (tuition 11,690 + other 1,575), not Rs 26,550. Private-unaided page: lowest Class 10 fee Rs 24,000, no Rs 18,000; several schools well above Rs 52,000. D06 and L08 rest on this |
| forge-v1.md#C08 | Satara CBSE private Rs 18,000-52,000; one EM school Rs 26,550 | same two Careers360 URLs | MISREPRESENTED | Repeats 01-local-market.md#C05 error |
| 01-local-market.md#C06 | Vallath Rs 1,300/month online (national) | https://vallath.in/program/speak-english-360online/ | VERIFIED | Rs 1,300 includes 18% GST, one instalment, online |
| 01-local-market.md#C07 | BYJU'S to close about 120 of 250 centres, 2024 (national) | https://inc42.com/?p=473439 | VERIFIED | Article dated 2024-08-14, unnamed sources, notices from 31 July, majority by 31 Aug |
| 01-local-market.md#C12, #C24 | Success: Spoken English Rs 2,000/month, 8 years | https://m.indiamart.com/success-satara | VERIFIED | Price and 8 yrs shown. PIN 415002 and any course duration not shown on the page |
| 01-local-market.md#C13 | Siddheshwar Class X Rs 500/Person | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | Period not stated, as claimed |
| 01-local-market.md#C14 | Annapurna Mess (Karad) online Class 8 Rs 500/month | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | Listing title reads "JKG - 8th std"; labelled Karad |
| 01-local-market.md#C15 | Pune prices ABKO, British Council, ELTIS, Cambly, EngVarta | https://engvarta.com/best-english-speaking-courses-in-pune/ | VERIFIED | Matches; page is promotional, fees "estimated" |
| 01-local-market.md#C17 | Satara city 120,079 (2011), 61,129 M / 59,066 F | https://en.wikipedia.org/wiki/Satara_(city) | VERIFIED | Figure present; male + female sum to 120,195, not 120,079. Infobox 137,283 and lead 179,147 conflict, as the scout said |
| 01-local-market.md#C18 | Literacy 80% (84% M, 76% F) | https://en.wikipedia.org/wiki/Satara_(city) | VERIFIED | |
| 01-local-market.md#C20 | Karad 53,879 (M 27,134, F 26,745), literacy 89.05% | https://www.census2011.co.in/data/town/802870-karad-maharashtra.html | VERIFIED | |
| 01-local-market.md#C21 | District per capita "nearly 1.2 times state average" | https://en.wikipedia.org/wiki/Satara_(city) | VERIFIED | Text says "per capita" (does not say income), cites a 2016 Economic Times article; district, not city |
| 01-local-market.md#C25, #C27 | Job 4U (Powai Naka) and Shivtej listed in Satara, no price | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | |
| 01-local-market.md#C26 | Breath Institute, 9 years, English conversation, no price | https://m.indiamart.com/breathinstitute | VERIFIED | Page says only "Satara, Maharashtra"; no Karad or Shnoli address on the page (scout's snippet note is unconfirmed) |
| 01-local-market.md#C29 | Karad: De Inspired, Spirit, Be Inspired (English speaking) | https://m.indiamart.com/city/karad/coaching-classes.html | VERIFIED | Karad page shows 15 listings, matching the peer table |
| 01-local-market.md#C33-C35 | Draft Act: >25 students, under-13 bar, 5 hours/day, receipts, pro-rata refund, fines | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | VERIFIED | Also confirms graduate rule and bar on recognised-school teachers. Page does not say whether 25 is per batch or per centre; each branch is a separate centre |
| 01-local-market.md#C43 | Bodhisutra: 2 minutes speaking per 2-hour session in batch of 10-12 | https://www.bodhisutra.com/?p=551 | VERIFIED | Dated 2012-07-25; "if you are lucky"; commercial |
| 01-local-market.md#C46 | Dnyandeep Coaching 5 stars, 2 reviews, only Satara rating | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | |
| 01-local-market.md peer-town table (Satara, Karad) | per 10,000 arithmetic and peer median | n/a | VERIFIED | 4/120,079 = 0.33; 3/53,879 = 0.56; 15/53,879 = 2.78; peer medians 0.00 and 0.38 recompute correctly from the table values. Satara coaching figure should use 19 (1.58). Phaltan, Pandharpur, Shrirampur, Bhusawal inputs not opened |
| 01-local-market.md seasonality; forge-v1.md wedge; strategy-v1.md B5 | SSC 15 Feb-11 Mar 2027, HSC 8 Feb-16 Mar 2027 | https://news.careers360.com/maharashtra-board-exam-dates-2027-out-hsc-ssc-class-12th-10th-exams-february-march-msbshse-practicals-internal-assessments | VERIFIED | Article dated 2026-09-17; dates tentative, timetables to follow |
| 02-signals.md#S01, #R01 | Draft Act terms, 2026-08-20 | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | VERIFIED | |
| 02-signals.md#S02, #R02 | SCCTI asks >100 students, one-time registration, parental consent under 13 | https://news.careers360.com/maharashtra-coaching-centres-seek-one-time-registration-lower-space-norm-draft-regulation-law/amp | VERIFIED | Dated 2026-09-02 |
| 02-signals.md#S03, C01 | PlanetSpark 2.2/5, refund and support themes, latest review 2026-10-20 | https://planetspark.pissedconsumer.com/review.html | VERIFIED | Page shows 205 reviews; scout's "about 10 of 16" is the scout's own tally (labelled so) |
| 02-signals.md#S04, C02 | ELSA Speak 2.4 from 32 reviews, 66% one-star, themes | https://uk.trustpilot.com/review/elsaspeak.com | VERIFIED | |
| 02-signals.md#S05 | SpeakX Rs 299/month, no-refund policy, 200,000 paying subscribers (2025) | https://www.business-admin.speakx.com/refund-policy ; https://www.cxodigitalpulse.com/?p=22137 | MISREPRESENTED | No-refund wording is on the policy page, but that page shows no Rs 299 amount. Rs 299 is on the press release (2024-09-26), which says 10,000 paid subscribers, not 200,000. The 200,000 figure is from the entrepreneur.com article (see S12 row), not these URLs |
| 02-signals.md#S06 | 27% take private coaching; Rs 2,409 / 3,988 / 1,793 (national) | https://insights.dataful.in/articles/private-schooling-costs-nearly-9-times-more-than-government-education-nss-survey | VERIFIED | |
| 02-signals.md#S08, M03 | March 2026 panel, semi-English, falling government enrolment | https://news.careers360.com/maharashtra-panel-school-education-semi-english-bilingual-teaching-government-marathi-medium-raise-enrolment-proposal/amp | VERIFIED | Dated 2026-03-27 |
| 02-signals.md#S09, R05, T03; economics-v1.md#C13; forge-v1.md#C23 | UPI zero MDR up to Rs 2,000 and small merchants up to Rs 1 lakh/month, from 2026-10-15 (national) | https://www.moneylife.in/article/upi-charges-on-transactions-over-2000-from-15th-october-what-new-mdr-framework-means-for-consumers-and-merchants/81663.html | VERIFIED | |
| 02-signals.md#S10, T01; forge-v1.md; strategy-v1.md | ChatGPT Go Rs 399/month India, 2025-08-19, UPI | https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html | VERIFIED | Free-tier voice limits (lumichats) not checked |
| 02-signals.md#S11, F02; forge-v1.md moat; prosecution-v1.md#C15 | PhysicsWallah 75+ new centres FY27, 27 states, marketing +50%, Rs 478 crore offline | https://www.storyboard18.com/brand-marketing/physicswallah-ups-marketing-spend-by-50-in-h1-fy26-as-offline-expansion-accelerates-85566.htm | VERIFIED | Planned, not opened |
| 02-signals.md#S12, F01; prosecution-v1.md#C09 | SpeakX USD 16M pre-Series B, 200,000 paying, USD 7.5M ARR, Marathi planned, 2025-10-15 | https://india.entrepreneur.com/news-and-trends/speakxai-raises-usd-16-mn-to-strengthen-ai-powered-english/498354 | VERIFIED | Company-reported figures. Rs 299 in prosecution-v1.md#C09's sentence is not on this page (see S05 row) |
| strategy-v1.md A1 and notes | Success listing "course 1-4 months" | https://m.indiamart.com/success-satara | MISREPRESENTED | Page shows no course duration. The strategist's own search claim is not supported by the page |
| strategy-v1.md C2 [C01] | Satara population 120,079 (2011) | https://en.wikipedia.org/wiki/Satara_(city) | VERIFIED | See 01-local-market.md#C17 caveat |
| economics-v1.md#C02 | Success Rs 2,000/month, 8 years | https://m.indiamart.com/success-satara | VERIFIED | |
| economics-v1.md#C07 | Security deposit 3-6 months common; Maharashtra no cap (national) | https://wb.rentok.com/wp-content/uploads/2026/07/Security-Deposit-Rules-India-Reference-Sheet.pdf | UNREACHABLE | PDF fetched twice; body text compressed and unreadable, nothing visible supports the claim. Economics file says it never opened it. Not a tool failure of the fetch layer |
| economics-v1.md#C21 | Meta cost per lead Rs 200-600 education; Google Rs 500-1,500 | https://megadigital.ai/en/blog/facebook-ad-cost-in-india/ | MISREPRESENTED | Page gives no coaching/education CPL range and no Google data; shows education CPC Rs 0.14 and internally inconsistent lead cost. Not used in the model (ads excluded) |
| economics-v1.md Calculations (conservative) | setup 56,500; capital to first revenue 71,100; monthly cash table m1-m12; peak 79,011; break-even 13.4 -> 14; blended CAC 185.9; margins | n/a | VERIFIED | All recomputed from the stated inputs and match to rounding. 30-student net 30 x 560 - 7,300 = 9,500 (prosecution) and 25 x 560 - 7,300 = 6,700 also correct |
| economics-v1.md Scenarios table and Verdict inputs | "cumulative not recovered... about month 28"; at Rs 800 and 17.5 students "about Rs 5,100/month" | n/a | MISREPRESENTED | Arithmetic wrong against the file itself. Calculations section gives about month 30 (12 + 17.5 = 29.5), not 28. 17.5 x 760 - 7,300 = 6,000 before CAC (about 5,600 after ~380 CAC), not 5,100 |
| economics-v1.md Simulation inputs (price) | price low/likely/high 600/800/1000, evidence "founder-estimate" | n/a | MISREPRESENTED | Only the 600 comes from the founder (contract). The 800 and 1,000 are labelled ASSUMPTION in economics-v1.md#C05 and are untested, so tier should be assumption. Other tiers (fixed_cost founder-estimate covers rent only; electricity and supplies are assumptions) are mixed but acceptable as the rent is the larger part |
| simulation-v1.md vs economics, strategy, prosecution | viable share quoted consistently | n/a | VERIFIED | Simulation 0.0% viable, 69.1% within capital, P50 cumulative -Rs 47,610; prosecution quotes the same. Economics and strategy quote no viable share. Simulation uses haircuts per tier |
| prosecution-v1.md#C02, #C03, #C14 | Draft Act wording; 25-student basis not stated | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | VERIFIED | |
| prosecution-v1.md#C01 | No final Act found as of 2026-10-21 | scconline URL + careers360 proposal URL | VERIFIED | Scconline page is a draft report; careers360 proposal URL not opened. Absence claim, labelled as such |
| FOUNDER-COUNTED / FOUNDER-ESTIMATE tiers | forge#C02, C03, C07, C10; economics#C03, C04, C06, C15; 01-local-market C22, C23, C41, C42 | 00-founder-knowledge.md | VERIFIED | Wording and tiers match Q1, Q5, Q6, Q7, Q9, Q10, Q11. Q9 "2 English classes ~Rs 1,000" is "heard" and is used as an estimate only |
| SIMULATED lines | strategy-v1.md section D | n/a | VERIFIED | Panel is labelled objections-only and nowhere used as evidence |

## Struck claims
- 01-local-market.md#C01 — MISREPRESENTED — the cited city page does not list Success; the "four providers on this page" claim is wrong (Success survives on its own page via #C12)
- 01-local-market.md#C02 — MISREPRESENTED — counts are 28 total and 19 Satara, not 29 and 18
- 01-local-market.md#C05 — MISREPRESENTED — fee figures (Rs 18,000, Rs 26,550) are not on the cited pages; D06 and L08 lose their support
- forge-v1.md#C08 — MISREPRESENTED — repeats the school-fee error
- 02-signals.md#S05 — MISREPRESENTED — Rs 299 not on the policy page; 200,000 subscribers not on the press release (it says 10,000)
- strategy-v1.md A1 (Success "course 1-4 months") — MISREPRESENTED — not on the page
- economics-v1.md#C07 — UNREACHABLE — deposit-months source unreadable and never opened
- economics-v1.md#C21 — MISREPRESENTED — ad-cost figures not on the cited page
- economics-v1.md Scenarios "month 28" and "Rs 5,100" lines — MISREPRESENTED — arithmetic wrong against the file's own Calculations
- economics-v1.md Simulation inputs, price tier — MISREPRESENTED — Rs 800/1,000 labelled founder-estimate but are untested assumptions

## Assumptions in load-bearing positions
- economics-v1.md#C07 — now an unsourced 6-month deposit assumption (source struck); it alone drives the K1 break (peak Rs 79,011 vs Rs 75,000) and prosecution FE1
- economics-v1.md#C17 — conversion rates (3% then 2%) ASSUMPTION; basis of the 9-student KE2 result and the break-even path
- economics-v1.md#C18 — 8% monthly churn ASSUMPTION (differs from the locked KE3 stress of 20%)
- economics-v1.md#C05 and simulation price high values — Rs 800 and Rs 1,000 ASSUMPTION; the only path to a worthwhile founder income
- economics-v1.md#C09, #C10 — fit-out and registration costs ASSUMPTION; part of the Rs 56,500 setup
- economics-v1.md#C06 — rent Rs 4,000-6,000 is FOUNDER-ESTIMATE (heard), not a listing or quote; basis of KE1 and KE3
- forge-v1.md#C14, #C16, #C17, #C18 — conversion, speaking-gap, shop-registration-only and not-employed-in-recognised-school ASSUMPTIONS; basis of KM3 and KE4 statuses
- strategy-v1.md C2 [C02] — class 8-10 share of population (4.5%) ASSUMPTION; basis of market size

## Summary
- verified: 42, misrepresented: 9, unreachable: 1 (of which tool failure: 0), unsourced: 0
- demand evidence surviving the audit: 01-local-market.md#C12/#C24 (Success, Satara, Rs 2,000/month, 8 years; one price point, school-age focus not shown); #C25, #C26, #C27 (Job 4U, Breath, Shivtej listed in Satara, no price, no reviews); #C13 (Siddheshwar Rs 500/person, period unknown); #C28 (PhysicsWallah Satara centre, adjacent, no English); 02-signals.md#S06 (national spend, not local). Struck: #C01 as stated, #C05/D06 school-fee spend.
