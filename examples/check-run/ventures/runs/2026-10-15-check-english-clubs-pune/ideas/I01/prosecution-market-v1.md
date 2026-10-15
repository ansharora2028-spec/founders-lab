---
run_id: 2026-10-15-check-english-clubs-pune
idea_id: I01
agent: prosecutor-market
version: 1
created: 2026-10-15T10:32:10Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I01/kill-criteria.md
- .../ideas/I01/forge-v1.md
- .../ideas/I01/economics-v1.md

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | NOT MET | 01-local-market.md#C19, 02-signals.md#S06, forge-v1.md#C07, prosecution-market-v1.md#C01 | Zero operators found in Pune or any Indian city with a checkable sign of paying customers. Forge supplies none and itself says the evidence cannot separate "open gap" from "no demand". Existing spend cited (institutes at ₹4,000-15,000, SpeakX) is a different product and does not satisfy the threshold. |
| KM2 | NOT MET | forge-v1.md#C12, 02-signals.md#S01, S02, prosecution-market-v1.md#C04 | Only one example near the band: SpeakX, ₹299/month, which is below the ₹300 floor and is a company claim of 200,000 paying subscribers not broken out by students. No second independent example. The only student-spend figure is a 2011 national ASSOCHAM number (~₹1,500/month, ages 10-17), below the ₹2,000 threshold and too old. |
| KM3 | NOT MET | 01-local-market.md#C15, forge-v1.md#C04, prosecution-market-v1.md#C01, #C02 | No operator of paid live-human English practice at or below ₹1,500/month with 12+ months of operation was found. Pune Toastmasters dues in rupees are still not stated by any source; only the international dues were found. Both halves of the threshold fail. |
| KM4 | INSUFFICIENT EVIDENCE | 01-local-market.md#C09, 02-signals.md#C10, prosecution-market-v1.md#C06 | No documented 5-query graveyard search exists in the inputs (the scout ran two). My searches found no closed offline English club either. Nothing shows failure for demand reasons, but search coverage of Indian micro-ventures is poor and the 5-query log is not delivered. Absence of evidence. |
| KM5 | INSUFFICIENT EVIDENCE | forge-v1.md#C09, prosecution-market-v1.md#C05, #C07 | No Pune district or city student count is sourced. The only sourced enrolment is SPPU's 2010 figure (496,531), which covers Pune, Nashik and Ahmednagar districts. No sourced indicator that 15% of students want to improve spoken English. |

KE* criteria: no direct market evidence to add.

## Flaws
### FM1 — FIXABLE
- flaw: No evidence that anyone pays for the product category as specified (recurring, in-person, peer-level, low-price English conversation). Every demand proxy is an adjacent product: ₹4,000-15,000 structured institutes (different job, 8-30x the price) or app subscriptions (different format). The forge's own wording is that the central claim is "ASSUMPTION: no Pune evidence".
- evidence: [C01] No Pune paid café English club found on Meetup, Luma or search [source: 01-local-market.md#C19]. [C02] Forge lists willingness to pay ₹499 as the central untested assumption [source: forge-v1.md#C21].
- what would fix it: at least 2 Pune (or 3 other-city) operators with prices at or below ₹2,000/month and dated attendance or reviews, per KM1. Obtainable by desk research only if such operators exist. Two scouts and this prosecutor found none, so the likelier outcome is that desk research cannot fix it. Primary research (paid pre-sale test) would be needed.
- fix would change customer/problem/revenue model: no

### FM2 — FATAL
- flaw: The price cannot carry anyone other than the founder. At ₹499 and 8-12 paying members per group, a facilitator at the only sourced rate (₹1,000/hour) costs more per member than the fee. Economics shows contribution of -₹783 per member with a hired facilitator and LTV/CAC 0.98 in the conservative case. Growth beyond the founder's own hours therefore requires a higher price or a different delivery model, which changes the revenue model. The rate is dated (about 2016, multi-city) and weakly sourced, but the ₹702/hour Pune tutor average (01-local-market.md#C04) points the same way.
- evidence: [C03] Facilitator rate ₹1,000/hour [source: https://www.britishcouncil.in/about/jobs/freelance-trainer-0, as cited in economics-v1.md#C09]. [C04] Pune tutor average ₹702/hour [source: https://www.superprof.co.in/lessons/english/pune/]. Economics conservative case unit economics: no [source: economics-v1.md Verdict inputs].
- what would fix it: not fixable by evidence at ₹499; needs a different price or group size (for example 25+ per group), which changes the revenue model and the café format.
- fix would change customer/problem/revenue model: yes

### FM3 — FIXABLE
- flaw: Free and cheaper substitutes are not addressed with data. Toastmasters rupee dues are still unknown; no Pune institute weekend or demo-batch prices were found; no data on the college English or communication societies. The forge's "difference" column is assertion.
- evidence: [C02] Searches returned only international Toastmasters dues (USD 60 per six months, rising to USD 72 from 2026-08-03) and no Pune rupee figure [source: https://toastmasters.org/footer/faq/Membership-Dues]. Pune Toastmasters Club lists no fee and admits anyone over 18 [source: https://sites.google.com/view/toastmastersclubofpune].
- what would fix it: dues for 2+ open Pune Toastmasters clubs and weekend or short-plan prices from 3 Pune institutes. Obtainable by desk research or by phoning clubs.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: No sourced evidence on student affordability. The only student-spend figure is 2011 and national, and the forge classes it as unreliable. KM2's affordability question is open.
- evidence: [C04] ASSOCHAM pocket money about ₹1,500/month by 2011, ages 10-17, national [source: https://news.cleartax.in/pocket-money-in-india-how-the-amount-has-risen-over-the-decades/3763/amp]. No 2024-2026 survey surfaced in my search.
- what would fix it: a named-firm student-spend survey with sample and city, or two paid student products at ₹300-1,000 with 1,000+ paying users. Partly obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Market sizing is unsourced and the first-100 path does not reach 100. Forge's channels sum to about 77 in 3-4 months with all conversion rates assumed; economics conservative reaches about 24 in 3 months. SPPU's 600+ colleges span three districts and the Pune-only count is missing.
- evidence: [C05] SPPU enrolment 496,531 in 2010, three-district jurisdiction [source: https://en.wikipedia.org/wiki/Savitribai_Phule_Pune_University]. [C07] Pune district higher-ed institutions: 475 colleges (AISHE 2021-22 via PTI) vs 763 institutions (a consultancy, 2026); sources conflict [source: https://thesouthfirst.com/pti/karnataka-has-3rd-highest-number-of-colleges-in-india-aishe-report/].
- what would fix it: AISHE district tables or SPPU annual report with Pune-district enrolment; a source for the English-confidence share. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Timing and substitution risk. Capital and attention in Indian spoken-English are moving to AI apps at ₹299/month (SpeakX claims 200,000 paying subscribers, EBITDA-positive), which sets the price anchor lower than ₹499 and absorbs the "casual, low-cost practice" need. The forge cites only vendor-written blogs for the "apps lack human practice" gap.
- evidence: [C08] SpeakX 200,000+ paid subscribers, EBITDA positive in FY26, per search summary [source: https://inc42.com/buzz/exclusive-ms-dhoni-joins-edtech-startup-speakxs-cap-table/]; ₹299 price [source: 02-signals.md#S02].
- what would fix it: independent (non-vendor) evidence of learners paying for human, in-person practice after using apps, such as a survey or an operator's retention data. Hard to find by desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Searches for paid recurring English conversation clubs in Indian cities returned no India results; only Moscow, Israel, Latvia and university clubs [source: https://www.meetup.com/ru-ru/yourrealtalk/events/chvtttyjcdbsb/] (other country: Russia). A second city-specific search returned only online programs and Mumbai institute pricing (₹2,950 classroom courses at Let's Talk Institute, vendor-reported) [source: https://engvarta.com/best-english-speaking-courses-in-mumbai/] (other city: Mumbai).
- [C02] Toastmasters International dues USD 60 per six months, USD 72 from 2026-08-03; one-time USD 25 new member fee; Pune clubs' extra charges unconfirmed (global) [source: https://toastmasters.org/footer/faq/Membership-Dues].
- [C03] British Council India freelance trainer posting, INR 1,000/hour, multi-city, dated about 2016 (national) [source: https://www.britishcouncil.in/about/jobs/freelance-trainer-0].
- [C04] ASSOCHAM pocket money about ₹1,500/month by 2011 (national) [source: https://news.cleartax.in/pocket-money-in-india-how-the-amount-has-risen-over-the-decades/3763/amp, 2011 data].
- [C05] SPPU: 612 affiliated colleges; enrolment 496,531 in 2010, covering Pune, Nashik, Ahmednagar [source: https://en.wikipedia.org/wiki/Savitribai_Phule_Pune_University].
- [C06] Search for a shut-down spoken-English club or offline community in India returned no closed offline club; found Speakwell with 100+ centres, Kings Learning, Knudge.me (status unknown) [source: https://yourstory.com/2017/09/english-speaking-course-knudge-me/]. Absence of evidence; the search tool does poorly on micro-ventures.
- [C07] AISHE 2021-22: 4,32,68,181 enrolled nationally; Pune listed among districts with most colleges (475) (national) [source: https://thesouthfirst.com/pti/karnataka-has-3rd-highest-number-of-colleges-in-india-aishe-report/]. A consultancy page cites 763 institutions in Pune district (32 universities, 731 colleges), not official [source: https://www.raysolute.com/education-consulting-pune.html].
- [C08] SpeakX: 2 lakh+ paid subscribers, EBITDA profitable FY26, per search summary (national) [source: https://inc42.com/buzz/exclusive-ms-dhoni-joins-edtech-startup-speakxs-cap-table/].
- [C09] India Skills Report 2025: graduate employability 54.81%; Mercer Mettl 2025: 42.6%. Neither gives a spoken-English confidence share in the summaries seen (national) [source: https://taggd.in/industry-reports/isr/india-skills-report-2025/].

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
