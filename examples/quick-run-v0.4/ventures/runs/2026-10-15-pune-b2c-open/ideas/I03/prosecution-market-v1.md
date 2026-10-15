---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-market
version: 1
created: 2026-10-15T10:44:03Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/01-local-market.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/02-signals.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/kill-criteria.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/forge-v1.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/economics-v1.md
- Own web searches on 2026-10-15 (search-result text only; no page was opened, so every claim below rests on search summaries)

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | NOT MET | forge-v1.md#C03, forge-v1.md#C04, C03, C04 | Threshold is 3 independent Pune providers, each with a published 1 BHK deep-clean price of at least Rs 2,500 and at least 50 dated reviews. The record has one: Ghare (166 Google reviews, 4.8, per forge; no review dates). Ghare publishes per-sq-ft rates, not a 1 BHK price. IndiaMART gives a per-sq-ft range for Pimpri Chinchwad with no providers or review counts. My search of Ghare's Google listing posts returned no prices and no review counts, so I could not reproduce the 166 figure. Demand for the service category is real (D05, Urban Company), but demand for independents is shown for at most 1 provider. |
| KM2 | NOT MET | forge-v1.md#C01, forge-v1.md#C02, C01, C02, C03 | Needs the median of at least 5 Pune listings at or above Rs 3,000, and at least 3 team or vendor per-job rates at or below Rs 2,200. Price side: the record has Urban Company locality pages (Rs 2,999-3,499), which are one seller, not 5 listings, plus Ghare and IndiaMART per-sq-ft rates that give about Rs 3,500-5,600 by arithmetic at 500-700 sq ft (scope not stated). Cost side: zero team or vendor per-job quotes. Economics-v1.md#C06 states no per-job team rate was found. |
| KM3 | INSUFFICIENT EVIDENCE | 01-local-market.md#C44, forge-v1.md#C13, forge-v1.md#C15, C05, C06 | Needs 20 dated Pune complaints on 2 platforms or 5 localities, and no more than 2 of 5 providers offering a re-clean or photo proof. Complaint half: the record has one Pune page (Raviwar Peth) described in prose, plus national material; no count of dated Pune complaints. Forge itself rates severity "moderate", affecting "a minority of bookings". Provider half: only Urban Company was checked, and my search shows it advertises a 3-day service guarantee and damage protection up to INR 10,000 on its Pune pages (C05, C06); the scope of the guarantee is not stated, so I cannot say it includes a free redo. Neither half is demonstrated. |
| KM4 | INSUFFICIENT EVIDENCE | economics-v1.md#C12, economics-v1.md#C13, C07 | No Pune search volume was provided by forge or economics, and my search found none (C07). The only lead-cost evidence is a cross-category vendor range of Rs 200-2,000 per lead (economics-v1.md#C12); the modeler's own conservative figure is about Rs 400 per enquiry, above the Rs 250 threshold. Neither half of the conjunctive test is evidenced. |
| KM5 | INSUFFICIENT EVIDENCE | forge-v1.md#C15, economics-v1.md#C14, C08, C09, C10, C11 | Repeat half: neither forge nor economics cites any repeat or referral rate; forge states repeat is once or twice a year and economics models 0.5 repeat bookings a month in the conservative case. My search found one company claim: Clean Fanatics (Bengaluru, July 2025) says 40% of revenue comes from word-of-mouth referrals (C09). That is a share of revenue, not a share of customers within 6 months, and it is a funded premium operator's own claim, so I do not count it as meeting the threshold. Graveyard half: no Indian home-cleaning closure caused mainly by CAC above per-job margin was found; Housejoy cut 7 of 12 cities in 2017 to tighten costs and acquisition spend but did not close (C08). The graveyard half is not violated, but it is not established either. |

## Flaws
### FM1 — FIXABLE
- flaw: The only differentiator (photo checklist and free re-clean) may already be partly offered by the dominant seller. Urban Company advertises a 3-day service guarantee and damage protection up to INR 10,000 on its Pune locality pages. The forge's claim that rivals are not "documented" competing on a deep-clean guarantee is an inference from absence (forge-v1.md#C08).
- evidence: [C05] Urban Company Pune pages advertise a "3-Day Service Guarantee" and "Protection against Damage upto INR 10,000"; the pages do not state what the guarantee covers. [source: https://www.urbancompany.com/pune-professional-home-cleaning-pimple-saudagar, via search summary, 2026-10-15]
- evidence: [C06] The same pages state deep clean excludes walls, ceilings, utensils, floor polishing and wet shampooing, so the scope of what is "missed" is bounded by the incumbent's own terms. [source: https://www.urbancompany.com/pune-professional-home-cleaning-bhawani-peth, via search summary, 2026-10-15]
- what would fix it: The Urban Company guarantee terms and help pages (does the 3-day guarantee include a free redo?), and the terms of at least 4 other Pune providers. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FM2 — FIXABLE
- flaw: Price evidence is single-seller. The idea's price rests on Urban Company's Rs 2,999-3,499 apartment prices, and the forge's cross-check (Ghare, IndiaMART) is per-sq-ft with no stated scope, and the 1 BHK figures are the forge's arithmetic. There is no evidence of what independents actually charge or what teams accept per job. Economics-v1.md shows the conservative case at Rs -251 per job before acquisition, so the price-to-cost spread is the load-bearing market number.
- evidence: [C01] Urban Company Pune apartment deep clean: unfurnished from Rs 3,199, furnished from Rs 3,499 in several localities; Deccan Gymkhana lower at Rs 2,999. Partial home cleaning from about Rs 2,799. [source: https://www.urbancompany.com/pune-professional-home-cleaning-bhawani-peth, via search summary, 2026-10-15]
- evidence: [C02] Urban Company reports average partner net earnings of about Rs 280-300 per hour (2023 reporting) and Rs 26,271 a month (Apr-Dec 2024). At a 4-5 hour job with two people that implies about Rs 2,200-3,000 of partner net earnings per job at app rates. This is an inference, not a team-rate quote; independents may accept less. [source: https://www.outlookbusiness.com/news/urban-company-gig-worker-makes-rs-26271-a-month-on-average-ceo-abhiraj-singh-bhal, via search summary; inference: net hourly rate x 2 people x 4.5 h]
- what would fix it: At least 5 dated Pune provider price sheets with stated scope and at least 3 per-job team quotes for a 1 BHK deep clean. Customer-side prices are obtainable by desk research; team quotes need outreach (phone calls), not desk research.
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: No evidence that customers switch from a 4.8-rated app with hundreds of thousands of reviews to an unreviewed local service for a quality promise. Forge admits this (forge-v1.md#C09, C17). The complaint rate that does exist is small relative to volume (forge-v1.md#C13: about 2% one-star; forge-v1.md#C15: "minority of bookings"). The need gap is a complaint pattern on a service that most customers rate highly.
- evidence: [C03] Urban Company's Pune pages show about 4.80 ratings on roughly 300K-340K reviews (unfurnished) and 600K+ reviews (furnished), with 1.7M bookings reported on the Pimple Saudagar page. [source: https://www.urbancompany.com/pune-professional-home-cleaning-pimple-saudagar, via search summary, 2026-10-15]
- what would fix it: A dated record of at least 20 Pune customer complaints about missed areas plus evidence that complaining customers use alternatives, or a live pilot with prepaid bookings from non-network customers. The pilot part is not desk-researchable.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: Demand is one-time and rare, and the idea's money depends on it recurring. Economics shows the first job does not recover acquisition cost in the conservative case, the forge says repeat is once or twice a year per household, and there is no evidence that independents earn repeat revenue. The tenant "deposit return" wedge rests on a single weak source (forge-v1.md#C23, 02-signals.md#S05).
- evidence: [C09] Clean Fanatics (Bengaluru) claims 40% of revenue from word-of-mouth referrals, and about 2,500 homes served a month, in a July 2025 seed round of INR 17 crore. Company-provided claims repeated in press, not audited. (other city: Bengaluru) [source: https://realtynmore.com/clean-fanatics-raises-2-mn-in-seed-round-led-by-inflection-point-ventures/, 2025-07, via search summary]
- what would fix it: A documented repeat or referral rate from at least one comparable service, expressed as a percentage of customers, plus a sourced link between move-out cleaning and deposit disputes. Partly obtainable by desk research; the deposit link is not.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Graveyard and funded-rival risk is not addressed. Forge contains no failed-startup research. The record shows a long history of venture-backed home-services companies that retrenched, and currently funded rivals (Snabbit, Pronto, Urban Company Insta Help) with capital far above K1. Forge's positioning table lists Snabbit as a different job and does not check Snabbit or Pronto Pune deep-clean prices (KE5 territory, noted only as market context).
- evidence: [C08] Housejoy stopped operations in 7 of 12 cities in 2017 and cut about half its workforce while tightening marketing and acquisition spend (2017); it did not fully close. (national) [source: https://www.medianama.com/2017/05/223-housejoy-shuts-services-in-7-cities/, 2017-05, via search summary]
- evidence: [C10] Homejoy (US, not India) shut down after lawsuits over worker classification. (global) [source: https://www.smartcompany.com.au/startupsmart/the-news-wrap-on-demand-cleaning-startup-homejoy-shuts-down/, via search summary]
- evidence: [C11] One Inc42 dataset cited in a search summary says over 400 hyperlocal startups entered the market from 2011 to 2016, with 100+ shut down. (national) [source: https://inc42.com/?p=25219, via search summary; cause of failure not given]
- what would fix it: A written graveyard section naming at least 3 Indian home-cleaning or home-services companies that failed or retrenched, with dated causes, and a stated difference for this idea. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

No FATAL market flaw is established. The nearest to FATAL is the conservative economics result (economics-v1.md: Rs -251 per job before acquisition at Rs 2,999), which depends on the unsourced team rate and on the price ceiling. I treat the price as a FIXABLE evidence gap (FM2) because the independent per-sq-ft listings suggest independents may charge above the app. If the team-rate and price quotes in FM2 come back at the forge's own assumptions, the idea has no margin.

## Evidence
- [C01] Urban Company Pune apartment deep clean: unfurnished from Rs 3,199 (about 4 hours), furnished from Rs 3,499; Deccan Gymkhana Rs 2,999 unfurnished; partial home cleaning from about Rs 2,799. Prices as seen in search summaries on 2026-10-15. [source: https://www.urbancompany.com/pune-professional-home-cleaning-bhawani-peth]
- [C02] Urban Company partner net earnings about Rs 280-300 per hour (2023) and Rs 26,271 a month on average (Apr-Dec 2024), company-reported. (national) [source: https://www.outlookbusiness.com/news/urban-company-gig-worker-makes-rs-26271-a-month-on-average-ceo-abhiraj-singh-bhal]
- [C03] Urban Company Pune pages show 4.80-4.82 ratings, 300K-850K reviews per package, and 1.7M bookings on one page. [source: https://www.urbancompany.com/pune-professional-home-cleaning-pimple-saudagar]
- [C04] Ghare Facility Cleaning Services advertises deep cleaning in Hinjewadi, Wakad, Baner, Balewadi, Pimple Saudagar, Ravet, Punawale and Tathawade; its Google Business posts show no prices and no review count in search summaries. [source: https://business.google.com/v/ghare-facility-cleaning-services/016890659316125069239/f893/_/lp/4913276866379255105/]
- [C05] Urban Company Pune pages advertise a 3-day service guarantee and damage protection up to INR 10,000; terms not stated. [source: https://www.urbancompany.com/pune-professional-home-cleaning-pimple-saudagar]
- [C06] Urban Company deep clean excludes utensils, walls and ceilings, floor polishing, and wet shampooing of sofas, chairs, blinds and carpets. [source: https://www.urbancompany.com/pune-professional-home-cleaning-bhawani-peth]
- [C07] No Pune monthly search volume for deep-cleaning terms was found in a search for it on 2026-10-15; a 2020 UK-based SEO report says "deep cleaning" is the highest-volume cleaning keyword and grew 44% year on year before 2020. (global, dated) [source: https://2025.hedgehogdigital.co.uk/cleaning-services-search-marketing-report/]
- [C08] Housejoy stopped operating in 7 of 12 cities and cut about half its staff in 2017 to tighten costs. (national) [source: https://www.medianama.com/2017/05/223-housejoy-shuts-services-in-7-cities/]
- [C09] Clean Fanatics (Bengaluru) raised INR 17 crore (about USD 2 million) in July 2025 and claims 40% of revenue from word-of-mouth referrals and Rs 2 crore MRR across about 2,500 homes a month; company claims. (other city: Bengaluru) [source: https://realtynmore.com/clean-fanatics-raises-2-mn-in-seed-round-led-by-inflection-point-ventures/]
- [C10] Homejoy (US) shut down in 2015 after worker-classification lawsuits. (global) [source: https://www.smartcompany.com.au/startupsmart/the-news-wrap-on-demand-cleaning-startup-homejoy-shuts-down/]
- [C11] Over 400 hyperlocal startups entered from 2011 to 2016 and 100+ shut down, per an Inc42 dataset cited in a search summary. (national) [source: https://inc42.com/?p=25219]
- Search coverage limits: Justdial and Google Maps listings for independent Pune cleaners did not surface in my searches; the absence of a third independent provider here is a search gap, not proof that none exists. Local data is thin and every source was read as search-result text.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
