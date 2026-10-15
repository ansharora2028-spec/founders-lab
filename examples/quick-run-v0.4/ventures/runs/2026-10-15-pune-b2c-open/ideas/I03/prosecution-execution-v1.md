---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-execution
version: 1
created: 2026-10-15T10:44:03Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I03/kill-criteria.md (LOCKED)
- .../ideas/I03/forge-v1.md
- .../ideas/I03/economics-v1.md
- (plus the venture-rules and file-schemas skill files)

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C22, economics-v1.md#C14, forge-v1.md#C18, E01 | Cash side fits (about Rs 58,300 at month 3, economics-v1 Calculations). Hours side fails at the threshold volume: economics-v1#C22 gives 1.5 h per booking plus 2 h/week of content. At 25 jobs a month that is 37.5 h + 8.6 h = 46.1 h/month, about 10.7 h/week, above the K2 HARD cap of 10. The 4.3 h/week in the constraint check holds only at 6.5 bookings a month. No pilot log. Weekday key-holder and on-site dispute time (K9 full-time job) is not costed (forge-v1#C18). |
| KE2 | INSUFFICIENT EVIDENCE | forge-v1.md#C16, economics-v1.md#C06 | No Pune team quote, named team or published per-job deep-clean team rate exists in any file. Team cost is an ASSUMPTION in both forge and economics. The economics conservative figure (Rs 2,400) is above the KE2 ceiling of Rs 2,300, so on the modelled conservative input the threshold is not reached. Nothing shows teams accept unpaid re-cleans or can cover 6 jobs/week. Desk research cannot supply this; it needs calls to teams. |
| KE3 | INSUFFICIENT EVIDENCE | forge-v1.md#C20, forge-v1.md#C22, E02, E03 | Forge states it did not find the aggregator definition and no small-business exemption. My search also found no official text; only secondary commentary. Damage and theft cover is unpriced (self-insured at Rs 100 per job in the conservative case). No insurance quote. Cannot be called met; the Rs 10,000 one-time and Rs 1,500/month thresholds are untested. |
| KE4 | NOT MET | economics-v1.md Scenarios, economics-v1.md Verdict inputs | Economics-modeler's own conservative case: Rs -251 per job before CAC, Rs -813 after the Rs 562 blended CAC, against a threshold of at least Rs 400. No break-even volume at any volume. No test bookings exist. |
| KE5 | NOT MET | forge-v1.md#C01, forge-v1.md#C02, forge-v1.md#C08, E04, E01 | Price ceiling: 110% of the lowest app quote (Rs 2,999) is Rs 3,299. Forge's rate card tops out at Rs 3,499 (about 117%), so the furnished tier breaks the threshold unless a premium is evidenced; none is (forge-v1#C09 says no switching data). The incumbent-response clause is unmet: forge's reason incumbents will not copy is an inference from absence (forge-v1#C08). Urban Company's Pune pages already advertise a 3-day service guarantee and damage protection up to Rs 10,000 (E04), so a guarantee is not an open differentiator. Whether that guarantee includes a redo is not stated on the pages seen. The two non-marketplace channels are listed but unsourced (forge-v1#C19). |
| KM1-KM5 | not assessed | — | Owned by the market prosecutor. I add direct execution evidence only where it bears on KM3 (see E04: incumbent guarantee on the pages). |

## Flaws
### FE1 — FATAL
- flaw: The conservative case is negative per job before any acquisition cost, and the gap cannot be closed by price because the price is capped by the dominant app's listed price band (Rs 2,999-3,499). The only lever is team pay, which is unsourced. Under rule 3 the idea fails on unit economics in the conservative scenario.
- evidence: [C01] Conservative gross margin -8.4% (Rs -251 a job), -Rs 813 after CAC, break-even "none at any volume" [source: economics-v1.md, Scenarios and Verdict inputs]. [C02] Price band of the incumbent: Rs 2,999-3,499 [source: https://www.urbancompany.com/pune-home-cleaning-services]. [C03] The economics file states COGS must fall about 25% (team rate near Rs 1,600-1,650) or price must rise to Rs 3,812, above any sourced Pune price [source: economics-v1.md, Verdict inputs].
- fix would change customer/problem/revenue model: no

### FE2 — FIXABLE
- flaw: Founder hours exceed the K2 HARD cap at the volume the idea says it needs. The forge claims the 10 h/week limit supports about 25 jobs a month; economics-v1's own per-task times give about 10.7 h/week at 25 jobs. Weekday key-holder access and on-site disputes are not counted.
- evidence: [C04] 1.5 h per booking plus 2 h/week content [source: economics-v1.md#C22]. Arithmetic: 25 x 1.5 = 37.5 h + 8.6 h = 46.1 h per month, about 10.7 h/week.
- what would fix it: a task-by-task hours table at the planned volume with at most 10 h/week, backed by a pilot log of at least 3 real jobs. Partly obtainable by desk research (reduce volume target); the time-per-task needs a real pilot.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: Regulatory position is unresolved and the founder, who sets the price, collects the money and directs teams, may be treated as an "aggregator" or as an employer/principal. Central Social Security Rules 2026 are in force and require aggregators to register workers on a government portal; the Maharashtra bill is pending with unconfirmed definition and penalties.
- evidence: [C05] The Code defines an aggregator as a digital intermediary or marketplace connecting service users with providers, with a Seventh Schedule list of categories; Rules in force from 2026-05-08, with worker registration duties; sources are secondary and disagree on section numbers and on when the levy starts [source: https://www.taxmann.com/post/blog/analysis-aggregator-obligations-code-on-social-security/]. [C06] Maharashtra bill issued 2026-07-03; aggregator definition, registration mechanics and penalties not found in secondary summaries [source: https://teamleaseregtech.com/updates/article/57603/maharashtra-gig-and-platform-workers-rights-and-protection-bill-2026/]. [C07] Penalties under the Code reported at up to Rs 1 lakh first contravention, Rs 2 lakh subsequent (secondary summary of Section 133) [source: https://www.dcpsol.com/maharashtra-gig-platform-workers-rights-protection-bill-2026]. A fine of that size alone equals the K5 cannot-lose limit.
- what would fix it: official Code, Rules and bill text (India Code, Gazette, Maharashtra legislature) or a lawyer's written opinion showing a WhatsApp-run per-job contractor model is outside the aggregator definition or inside a cost under Rs 10,000. The official text is desk-obtainable; the applicability opinion needs a paid consult (a few thousand rupees ASSUMPTION).
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: Premises liability is uncovered. The founder sends unsupervised strangers into customers' homes. Reserve is Rs 100 per job; the incumbent advertises damage protection up to Rs 10,000. A single theft allegation or broken item can consume many jobs of margin, and the loss limit is Rs 1,00,000 (K5).
- evidence: [C08] Incumbent damage cover up to Rs 10,000 shown on Pune pages [source: https://www.urbancompany.com/pune-professional-home-cleaning-shatrunjay-nagar-kondhwa-budruk]. [C09] Reserve of Rs 100 per job, no insurance priced [source: economics-v1.md#C11; forge-v1.md#C22].
- what would fix it: a priced insurance quote (public liability or home-service cover) with a per-claim cap, plus a written team agreement allocating damage cost. Quote obtainable by calling insurers, not purely desk research.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: The only differentiator (photo proof plus free re-clean) is not shown to be absent from the incumbent. Urban Company already advertises a service guarantee and damage protection on Pune pages, and reviewers use photos as evidence. A funded incumbent can add a redo or photo step at near-zero marginal cost. The price premium is unproven and forge's furnished tier (Rs 3,499) exceeds 110% of the lowest app price.
- evidence: [C10] "3-Day Service Guarantee and Protection against Damage upto INR 10,000" on Pune pages; redo terms not stated in the results; a Natu Baag reviewer sent photos of uncleaned corners and windows [source: https://www.urbancompany.com/pune-professional-home-cleaning-natu-baag-shukrawar-peth]. [C11] Home-services rivals are funded (Snabbit about $400M valuation talks, 2026-04-25) [source: https://techcrunch.com/2026/04/25/indias-snabbit-seeks-fresh-funding-at-a-400m-valuation-sources-say/ (national)].
- what would fix it: Urban Company's published redo/guarantee terms showing no photo-proof redo, and evidence that Pune customers pay a premium for a guarantee. The first is desk-obtainable; the second is not.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Supply leakage and second-order effects. After the first job the team knows the customer and can be booked directly at a lower price, removing the founder's spread. Demand is one or two jobs per household per year (forge-v1 "How it makes money"), so each customer must be re-acquired. If it works, copycats (existing small providers such as Ghare, which already lists deep clean from Rs 3,500) can add photos at no cost. Moat is "none yet" per forge-v1.
- evidence: [C12] Ghare Facility Cleaning lists a deep clean from Rs 3,500 and covers Wakad, Baner, Hinjewadi, the proposed cluster [source: https://business.google.com/v/ghare-facility-cleaning-services/016890659316125069239/f893/_/fullmenu/]. [C13] Forge: "Moat over time: None yet" [source: forge-v1.md, Moat over time].
- what would fix it: a team agreement with non-solicit terms and evidence of enforceability, or a channel where the founder owns the repeat relationship (broker contracts). Not desk-obtainable.
- fix would change customer/problem/revenue model: no

### FE7 — FIXABLE
- flaw: Acquisition rests on channels that can change terms or are untested: Meta/Instagram ads and WhatsApp Business, plus society WhatsApp groups where posting rules are unverified (01-local-market: housing-society access "unknown"). Every conversion rate in the path is an ASSUMPTION. The path reaches only about 100 customers in 4-5 months. Time to first revenue relies on recruiting teams within 5-8 weeks (economics-v1#C23), leaving 4-7 weeks of the 3-month K6 window.
- evidence: [C14] All conversion and CAC inputs unsourced [source: forge-v1.md#C19]. [C15] Team recruitment 8 weeks conservative [source: economics-v1.md#C23].
- what would fix it: 3 prepaid or confirmed bookings from a landing-page or WhatsApp test within the first 90 days (this is a real test, not desk research), and at least 2 teams signed before launch.
- fix would change customer/problem/revenue model: no

## Evidence
- [E01] Founder-hours arithmetic at 25 jobs a month from economics-v1.md#C22 inputs: 25 x 1.5 h + 2 h x 4.3 weeks = 46.1 h per month, about 10.7 h per week [source: economics-v1.md, derived by this prosecutor].
- [E02] Social Security (Central) Rules 2026 notified 2026-05-08; aggregators must register workers on a government portal; the definition of aggregator extends to associate companies, subsidiaries and third parties; no official text was seen [source: https://www.taxmann.com/post/blog/analysis-aggregator-obligations-code-on-social-security/ (national; secondary)].
- [E03] Maharashtra Gig and Platform Workers Rights and Protection Bill, 2026 issued 2026-07-03; definitions of aggregators and obligations exist; exact definition, thresholds and penalties not located [source: https://teamleaseregtech.com/updates/article/57603/maharashtra-gig-and-platform-workers-rights-and-protection-bill-2026/ (Maharashtra; secondary)].
- [E04] Urban Company Pune cleaning pages advertise a 3-day service guarantee and damage protection up to Rs 10,000; scope exclusions listed include utensils, walls and ceiling, sofa and carpet wet shampooing; Pune deep clean from Rs 2,999 unfurnished to Rs 3,499 furnished [source: https://www.urbancompany.com/pune-professional-home-cleaning-kasat-nagar-kondhwa-budruk]. Search snippet only; the redo terms are not in the result.
- [E05] A search for a clear Pune 1 BHK deep-clean price found none; listings are by "apartment" and the Ghare listing starts from Rs 3,500 [source: https://business.google.com/v/ghare-facility-cleaning-services/016890659316125069239/f893/_/fullmenu/].
- Limit of this file: I found no Pune per-job team rate, no insurance quote, and no official text. Web page fetches were not used; claims rest on search-result text.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| — | — | round 1; not applicable |
