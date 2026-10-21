---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: evidence-auditor
version: 2
created: 2026-10-21T10:38:23Z
---

## Scope
- files audited: 00-contract.md, 00-founder-knowledge.md, 01-local-market.md, 02-signals.md, ideas/I01/kill-criteria.md, diff-v2.md, forge-v2.md, strategy-v1.md, economics-v2.md, simulation-v2.md, prosecution-v2.md (all under <scratch>/ventures/runs/2026-10-21-check-satara-english/). verdict files not read.
- claims in scope: about 230 (sourced and ASSUMPTION/FOUNDER-labelled), checked: 65 checks, many covering several claims, sample method: all economics inputs + all FATAL-flaw (FE2) evidence + all demand evidence + all diff-row evidence + random sample of the rest (local-market, signals, strategy)
- fetch note: several pages were read through a summarising fetch tool, so counts such as listing totals can differ by one from the scout's count. Not a tool failure.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v2.md#C01 | price tiers: Rs 600 contract, Rs 800/1,000 ASSUMPTION | contract + 00-founder-knowledge.md | VERIFIED | Rs 600 matches contract. Rs 800/1,000 honestly labelled ASSUMPTION. C01 tags Rs 600 FOUNDER-ESTIMATE while the simulation block tags price "assumption"; same modelling-only tier, no effect |
| economics-v2.md#C02 | Success Rs 2,000/month, 8 years | https://m.indiamart.com/success-satara | VERIFIED | page shows "Rs 2,000/month" and "8 yrs"; target students not stated, as the claim says |
| economics-v2.md#C02, forge-v2.md#C01 | Success course length "1 to 4 months" | https://m.indiamart.com/success-satara | MISREPRESENTED | page has no course length. 01-local-market.md#C12 itself says "course duration not stated on the page". strategy-v1.md preamble says it "re-confirmed" this; the page does not |
| economics-v2.md#C03 | Vallath online Rs 1,300/month (national) | https://vallath.in/program/speak-english-360online/ | VERIFIED | "Fee: Rs 1300/month", online, group activities |
| economics-v2.md#C03 | tuition Rs 800-1,500 FOUNDER-COUNTED; bus-stand about Rs 1,000 FOUNDER-ESTIMATE | 00-founder-knowledge.md Q9, Q10 | VERIFIED | tiers match: tuition "counted", English class "heard" |
| economics-v2.md#C04 | ChatGPT Go Rs 399/month, launched 2025-08-19 (national) | https://www.exchange4media.com/digital-news/openai-launches-chatgpt-go-in-india-at-rs-399-146540.html | VERIFIED | price, date and UPI confirmed |
| economics-v2.md#C04, prosecution-v2.md#C05, forge-v2.md#C28, strategy-v1.md A3 | SpeakX Rs 299/month | https://www.business-admin.speakx.com/refund-policy | MISREPRESENTED | cited page confirms "strict no refund policy" only; it gives no Rs 299 price. Rs 299 appears at https://www.cxodigitalpulse.com/?p=22137 (2024-09-26), which none of these files cite for it |
| economics-v2.md#C05 | rent Rs 4,000-6,000 FOUNDER-ESTIMATE (heard) | 00-founder-knowledge.md Q7 | VERIFIED | tier correct ("heard") |
| economics-v2.md#C06 | Radhika Road 750 sq ft Rs 25,000; Rs 33/sq ft; 250 sq ft = Rs 8,300 | https://www.realestateindia.com/satara-property/commercial-property-for-rent.htm | VERIFIED | listing confirmed; 25,000/750 = 33.3 and x250 = 8,333 correct |
| economics-v2.md#C07 | Maharashtra no deposit cap; common range 3-6 months | https://wb.rentok.com/wp-content/uploads/2026/07/Security-Deposit-Rules-India-Reference-Sheet.pdf | UNREACHABLE | PDF text could not be decoded; no visible support. Economics itself says "not opened". Not a network failure |
| economics-v2.md#C07, diff-v2.md D4 | Shirwal factory "Deposit 6 months"; no small-room deposit listing | https://www.realestateindia.com/satara-property/commercial-property-for-rent.htm | VERIFIED | "4.Deposit 6 months" present |
| economics-v2.md#C10, forge-v2.md#C17 | S&E intimation, under 10 workers, no fee, within 60 days | https://calcguru.in/?p=1344 | VERIFIED | secondary source, labelled as such |
| economics-v2.md#C12, forge-v2.md#C26 | draft Act: 25-student line, under-13 bar, 5-hour cap, graduate rule, school-teacher bar, fines, 6 months to register | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | VERIFIED | all points confirmed; six months run from commencement, as forge says |
| economics-v2.md#C14 | UPI zero MDR up to Rs 2,000 from 2026-10-15 | https://www.moneylife.in/article/upi-charges-on-transactions-over-2000-from-15th-october-what-new-mdr-framework-means-for-consumers-and-merchants/81663.html | VERIFIED | |
| economics-v2.md#C16 | 300 parents reachable, FOUNDER-COUNTED | 00-founder-knowledge.md Q11, Q5 | VERIFIED | Q11 "counted", 300; Q5 "counted" 60-120 |
| economics-v2.md#C23 | Meta education cost per lead Rs 200-600 | https://megadigital.ai/en/blog/facebook-ad-cost-in-india/ | MISREPRESENTED | page gives education CPC Rs 0.14, CPR 0.75%, conversion 14.14%; no Rs 200-600 per lead |
| economics-v2.md#C23 | Facebook CPC Rs 0.51-2.26 | https://upgrowth.in/facebook-advertising-pricing/ | MISREPRESENTED | page says Rs 4 to Rs 50 per click for India |
| economics-v2.md#C27, forge-v2.md plan | Diwali Sunday 2026-11-08 | https://www.smartpuja.com/blog/diwali-2026-date-lakshmi-puja-muhurat-vidhi/ | VERIFIED | Diwali date confirmed |
| economics-v2.md Calculations | conservative arithmetic | recomputed | VERIFIED | setup 62,000; fixed 7,300; capital to first revenue 76,600; break-even 7,300/544.8 = 13.4 -> 14; path m3 5.4 to m12 10.47 (file 10.48); all monthly cash rows and cumulative -106,656; -70,656 excl. deposit; asymptote cash +872 and about 81 months; rent sensitivity 95,000 and 17.6; fixes -68,216; at Rs 800 break-even 9.8; blended CAC 185.8 |
| economics-v2.md Simulation inputs | evidence tiers per input | economics C01-C27 | VERIFIED | all inputs tagged "assumption"; none upgraded. Ranges match C18-C20, C06, C09. Note: churn high 0.10 vs C20 high 8%, labelled "sim range 4-10%" |
| simulation-v2.md | viable share 0.0%, 17.6% in capital, P50 -96,627, money gate 34.2% | simulation-v2.md vs prosecution-v2.md | VERIFIED | prosecution quotes the same figures. haircut table equals inputs x 0.75 or x 1.25 |
| prosecution-v2.md#C01, diff-v2.md D9, forge-v2.md#C27 | only Goranga names school students (10th); Job 4U adults; Shivtej 11 yrs, Breath 9 yrs; no fee but Success | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | Goranga 11 yrs, Job 4U 15 yrs and target list, Shivtej 11, Breath 9 all confirmed |
| prosecution-v2.md#C02 | Success Rs 2,000, 8 years | https://m.indiamart.com/success-satara | VERIFIED | |
| prosecution-v2.md#C03, diff-v2.md D10 | 2,682 ZP schools, 114,789 students classes 1-8, 2023-24 | https://www.zpsatara.gov.in/?p=6821 | VERIFIED | |
| prosecution-v2.md#C06 | ChatGPT Go Rs 399 | exchange4media URL above | VERIFIED | |
| prosecution-v2.md#C08 | Radhika Rs 25,000, Dahiwadi Rs 22,000, Shirwal 6-month deposit | realestateindia URL above | VERIFIED | Dahiwadi is a basement unit; Tamjai Nagar 220 sq ft "Call for Price" also confirmed |
| prosecution-v2.md#C09 | PW 75+ offline centres FY27 (national) | https://www.storyboard18.com/brand-marketing/physicswallah-ups-marketing-spend-by-50-in-h1-fy26-as-offline-expansion-accelerates-85566.htm | VERIFIED | also 50% marketing rise and Rs 478 crore offline Q2 FY26 |
| prosecution-v2.md#C10 | draft Act status | scconline URL above | VERIFIED | "no final text as of 2026-10-21" is the prosecutor's search result, not checkable here |
| prosecution-v2.md#C11, diff-v2.md D7 | PW Satara: Foundation 8-10 Maths/Science, no English batch | https://www.pw.live/offline-centres/batches/vidyapeeth/satara-mh/satara-vidyapeeth--pathshala-centre--715044 | VERIFIED | Gadoli centre, JEE/NEET 11/12/dropper, Foundation 8-10; no English, no fee |
| prosecution-v2.md#C12 | simulation figures | simulation-v2.md | VERIFIED | |
| prosecution-v2.md#C13 | Vallath Rs 1,300 | vallath URL above | VERIFIED | |
| prosecution-v2.md#C16 (FE2) | economics omits locked stress (20% churn; Diwali/May dips) | economics-v2.md | VERIFIED | economics uses 8% churn and says "omits Diwali, summer and exam-season dips" |
| forge-v2.md#C08, 01-local-market.md#C05 | Satara CBSE private schools Class 10 Rs 18,000-52,000 a year | https://school.careers360.com/schools/private-unaided-schools-in-satara | MISREPRESENTED | page Class 10 fees run Rs 24,000 to Rs 500,000 (e.g. Rs 56,700, Rs 441,920); the Rs 18,000 low and Rs 52,000 cap are not on the page |
| forge-v2.md#C08, 01-local-market.md#C05, D06 | Appasaheb Bhurao Patil EM School Class 10 Rs 26,550 | https://school.careers360.com/schools/appasaheb-bhurao-patil-english-medium-school-satara | MISREPRESENTED | page shows total Rs 13,265 (tuition 11,690 + other 1,575) |
| forge-v2.md#C09, 02-signals.md S06 | 27% take private coaching; Rs 2,409 national; Rs 3,988 urban (national) | https://insights.dataful.in/articles/private-schooling-costs-nearly-9-times-more-than-government-education-nss-survey | VERIFIED | |
| forge-v2.md#C24, 01-local-market.md#C39 | DPDP: parental consent under 18 (national) | https://ssrana.in/?p=45905 | VERIFIED | |
| forge-v2.md#C25, 01-local-market.md#C07 | BYJU'S about 120 of 250 centres, 2024 (national) | https://inc42.com/?p=473439 | VERIFIED | article dated 2024-08-14; "likely" to close |
| forge-v2.md#C30 | GST Rs 20 lakh threshold, normal-category states | https://mybillbook.in/blog/gst-registration-limit/ | VERIFIED | page does not name Maharashtra; inference that it is normal-category is fair |
| diff-v2.md D5 | go4whatsup is a vendor case study, 2,800-lead A/B test vs email | https://go4whatsup.com/case-studies/skilllab-academy/ | VERIFIED | no WhatsApp-group-to-paid figure on page, consistent with forge's "not a benchmark" |
| diff-v2.md D8, forge-v2.md#C28 | SpeakX plans Marathi | https://india.entrepreneur.com/news-and-trends/speakxai-raises-usd-16-mn-to-strengthen-ai-powered-english/498354 | VERIFIED | also USD 16M, 1M learners, 200,000 paying, USD 7.5M ARR |
| forge-v2.md Narrowest wedge, 01-local-market.md City profile | SSC 15 Feb-11 Mar 2027, HSC 8 Feb-16 Mar 2027 | https://news.careers360.com/maharashtra-board-exam-dates-2027-out-hsc-ssc-class-12th-10th-exams-february-march-msbshse-practicals-internal-assessments | VERIFIED | dates tentative; published 2026-09-17 |
| forge-v2.md dated plan | Dhanteras to Bhai Dooj 2026-11-06 to 11-10 | https://www.smartpuja.com/blog/diwali-2026-date-lakshmi-puja-muhurat-vidhi/ | MISREPRESENTED | cited page gives only Diwali 2026-11-08; Dhanteras and Bhai Dooj dates are not on it. Plan-only, no effect on economics |
| 01-local-market.md#C17, #C18, #C21 | Satara 2011 pop 120,079 (61,129 M, 59,066 F); literacy 84/76; district per capita about 1.2x state (2016 source) | https://en.wikipedia.org/wiki/Satara_(city) | VERIFIED | conflicting 137,283 and 179,147 also on page, as the scout says |
| 01-local-market.md#C20 | Karad 53,879; literacy 89.05% | https://www.census2011.co.in/data/town/802870-karad-maharashtra.html | VERIFIED | |
| 01-local-market.md#C60 and Peer-town benchmark (PEER-TOWN) | supplier counts: Karad 15, Phaltan 2, Pandharpur 5, Bhusawal 5 (1 spoken English), Shrirampur 2; per 10,000 and medians | https://m.indiamart.com/city/karad/coaching-classes.html ; .../phaltan/... ; .../pandharpur/... ; .../bhusawal/... ; .../shrirampur/... | VERIFIED | counts match; all per-10,000 values recomputed correct (0.33, 1.50, 0.56, 2.78, 0.38, 0.51, 0.22, 0.05, 0.27); medians 0.00 and 0.38 correct. Population figures for Phaltan, Pandharpur, Shrirampur, Bhusawal were not fetched (see Summary) |
| 01-local-market.md#C02, #C13, #C14, #C46 | 29 listings / 18 Satara city; Siddheshwar Rs 500; Annapurna Rs 500; Dnyandeep 5 stars from 2 | https://m.indiamart.com/city/satara/coaching-classes.html | VERIFIED | fetch read 28 total / 19 Satara city (one-off count difference); Rs 500 prices, Dnyandeep rating confirmed. Annapurna Rs 500 is for online JKG-8th tuition. Peer index for Satara would be 1.58 at 19; verdict unchanged |
| 01-local-market.md#C26 | Breath Institute, Satara, 9 years, no price | https://m.indiamart.com/breathinstitute | VERIFIED | page shows Satara and 9 yrs; the Karad address is from a snippet, labelled so |
| 01-local-market.md#C36 | PTAM about 50,000 members, 8 Sept 2026, threshold above 100, under-13, 11 Sept shutdown | https://www.freepressjournal.in/pune/pune-teachers-body-seeks-consultation-before-maharashtra-coaching-law-is-finalised | VERIFIED | shutdown was a conditional warning, not a firm announcement; fair paraphrase |
| 01-local-market.md#C43 | blog (2012): 10-12 students, 2 minutes speaking | https://www.bodhisutra.com/?p=551 | VERIFIED | includes 60 minutes of travel, as the claim says |
| 01-local-market.md#C04 | PW Satara Vidyapeeth Gadoli | PW URL above | VERIFIED | demand evidence: national brand present, no fee |
| 02-signals.md S11/F02 | PW offline expansion | storyboard18 URL above | VERIFIED | |
| 02-signals.md S03/C01 | PlanetSpark 2.2/5; refund and support complaints; latest 2026-10-20 | https://planetspark.pissedconsumer.com/review.html | VERIFIED | 205 reviews; scout's own tallies ("10 of 16") are labelled inference and not checked |
| 02-signals.md S05 | SpeakX Rs 299/month via UPI autopay, 200,000 paying subscribers (2025) | https://www.business-admin.speakx.com/refund-policy ; https://www.cxodigitalpulse.com/?p=22137 | MISREPRESENTED | refund page has no price; cxodigitalpulse says Rs 299 but "10,000 paid subscribers monthly" and no UPI autopay. The 200,000 figure is on the entrepreneur.com page, which S05 does not cite |
| strategy-v1.md C2 TAM/SAM/SOM | 5,400 students; TAM Rs 48.6 lakh / 81 lakh; SAM 24 lakh; SOM 1.8 lakh | arithmetic | VERIFIED | 120,079 x 4.5% = 5,404; other products recomputed correct |
| strategy-v1.md C6 | "12 in month 1, adding about 3/month at 7% churn gives about 20 by month 3" | arithmetic | MISREPRESENTED | 12 -> 14.2 -> 16.2 by month 3, not about 20. It is the strategy file's own arithmetic |
| diff-v2.md D2, forge-v2.md How it makes money | Rs 8,400 fixed; break-even 11; 30 students Rs 15,600; 40% fewer = 10.5; 18 students Rs 6,000; Rs 600 case 9,600 | arithmetic | VERIFIED | all correct. Rs 8,400 is ASSUMPTION inferred from a judge note |
| diff-v2.md D3, forge-v2.md#C31 | setup Rs 31,000; Rs 49,000 with 3 months; Rs 52,000 at 6-month deposit | arithmetic | VERIFIED | 31,000 and 49,000 and 52,000 correct; the 58,000-70,000 range is not derivable from the file |
| prosecution-v2.md KE2, KE3 | 10/180 = 5.6%; 30 x 560 - 7,300 = 9,500 | arithmetic | VERIFIED | |

## Struck claims
- economics-v2.md#C02, forge-v2.md#C01 (course length "1 to 4 months") — MISREPRESENTED — cited page states no course length
- economics-v2.md#C04, prosecution-v2.md#C05, forge-v2.md#C28, strategy-v1.md A3 (SpeakX Rs 299 at refund-policy URL) — MISREPRESENTED — cited page has no price (load-bearing: substitute price for KM5 and FM3)
- economics-v2.md#C07 (3-6 month deposit norm, rentok PDF) — UNREACHABLE — PDF unreadable, no visible support (the 6-month conservative deposit stays an ASSUMPTION)
- economics-v2.md#C23 (Meta cost per lead Rs 200-600) — MISREPRESENTED — megadigital page says otherwise
- economics-v2.md#C23 (CPC Rs 0.51-2.26) — MISREPRESENTED — upgrowth page says Rs 4-50
- forge-v2.md#C08, 01-local-market.md#C05 (CBSE Class 10 range Rs 18,000-52,000) — MISREPRESENTED — page range is Rs 24,000-500,000 (load-bearing for D06 and L08 indirect willingness-to-pay)
- forge-v2.md#C08, 01-local-market.md#C05 (Appasaheb Rs 26,550) — MISREPRESENTED — page shows Rs 13,265
- forge-v2.md dated plan (Dhanteras to Bhai Dooj 2026-11-06 to 11-10) — MISREPRESENTED — cited page lacks those dates
- 02-signals.md S05 (Rs 299, 200,000 subscribers at cited URLs) — MISREPRESENTED — cited pages do not show these
- strategy-v1.md C6 ("about 20 by month 3") — MISREPRESENTED — arithmetic gives about 16

## Assumptions in load-bearing positions
- economics-v2.md#C01, #C03 — ASSUMPTION used as the basis of the Rs 800/Rs 1,000 price, the only route to a viable case (FATAL FE2)
- economics-v2.md#C05 — FOUNDER-ESTIMATE (heard) Rs 4,000-6,000 rent used as the conservative rent input, against listings at Rs 22,000-25,000
- economics-v2.md#C07 — ASSUMPTION 6-month deposit in the conservative setup cost and K1 breach
- economics-v2.md#C08, #C09, #C11 — ASSUMPTION running and fit-out costs behind the Rs 62,000 setup and Rs 7,300 fixed cost
- economics-v2.md#C17, #C18, #C19, #C20, #C21, #C25 — ASSUMPTION class 8-10 = 60%, reach, conversion, churn behind the student path (break-even 14 vs path 10.5) and FE2
- forge-v2.md#C14, #C15, #C16, #C18, #C19, #C20, #C21, #C31 — ASSUMPTION conversion, willingness to pay, speaking gap, founder employment, churn, 60% effective speaking use, setup cost
- diff-v2.md D5, D7, D8 — ASSUMPTION plan dates, incumbent responses and the 60% effective-use factor behind the KM5 10.5-minute result
- prosecution-v2.md FE2 rests on economics-v2.md#C17-C20 (ASSUMPTION) for the path; it is correct arithmetic on those inputs

## Summary
- verified: 54, misrepresented: 10, unreachable: 1 (of which tool failure: 0), unsourced: 0
- demand evidence surviving the audit: 01-local-market.md#C12 and #C24 (Success, Rs 2,000/month, 8 years, own page); 01-local-market.md#C01, #C27 and diff-v2.md D9 (four to five Satara spoken-English directory listings with years in business, Goranga class-10 English); 01-local-market.md#C04 (PW Satara Vidyapeeth, adjacent, no fee); forge-v2.md#C09 and 02-signals.md S06 (national spend). Founder tuition price Rs 800-1,500 stays FOUNDER-COUNTED (VIABLE ON PAPER only). Struck and not usable: Careers360 school-fee figures (D06 indirect proof) and SpeakX Rs 299 as cited. No verified competitor revenue, search volume or Satara spoken-English reviews exist.
- not checked: population sources for Phaltan, Pandharpur, Shrirampur and Bhusawal (01-local-market.md#C56-C59), and the Podar, ALLEN, Urban Company, TalkDrill, Collegedunia and EngVarta sources; these were outside the sample.
- all arithmetic in economics-v2.md is correct; the FATAL flaw FE2 evidence (break-even 14, path 10.5, cumulative -106,656, simulation 0.0% viable) is intact and consistent across economics, simulation and prosecution.
