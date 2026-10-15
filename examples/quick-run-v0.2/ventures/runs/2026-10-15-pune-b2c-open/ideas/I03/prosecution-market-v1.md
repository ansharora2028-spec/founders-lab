---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-market
version: 1
created: 2026-10-15T09:32:42Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I03/kill-criteria.md
- .../ideas/I03/forge-v1.md
- .../ideas/I03/economics-v1.md
- (rules and schemas: ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md, ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md)

Research note: my searches returned thin results (one fetch of registrationwala.com was refused by the proxy). Statuses below say so where it matters. Pune data is thin (01-local-market.md coverage 3/10).

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | NOT MET | forge-v1.md#C01, forge-v1.md#C09, C01, C02, C03 | Threshold is 3 named tenant-side providers with a published price of at least ₹199 and 100+ reviews or disclosed revenue. Forge names none with a price or any review or revenue sign. Registrationwala's price is "not shown". NoBroker's agreement is a joint landlord/tenant registered agreement at an estimated ₹1,500–3,500, not a tenant-only product. My search found no Indian tenant-side move-in report or deposit-recovery seller with reviews. The only paid inspection products found are foreign apps (C02) or a Chennai managed service (C03). Rule 3 demand evidence is absent. |
| KM2 | NOT MET | forge-v1.md#C01, forge-v1.md#C05, forge-v1.md#C06, C04, C05 | Threshold is 20 dated Pune disputes in 24 months, or a survey showing 30% or more of tenants have no agreement. Evidence is 1 complaint (2026-04-19). A law-firm article uses an illustrative Zolo Stays case and does not say whether it is real (C04). Q&A forum posts have no Pune counts. My search for Pune consumer commission orders returned only unrelated MSEDCL electricity-deposit orders (C05). The count may exist (Reddit r/pune, commission e-Jagriti), but nobody has produced it. |
| KM3 | INSUFFICIENT EVIDENCE | forge-v1.md (competitor table), C06, C07 | Criterion needs a check of top-10 results in 3 languages plus 6 apps. Nobody has done it. Forge says free checklists are not Hindi or Marathi, but also lists Registrationwala and free lawyer templates as direct substitutes. My single query found no Hindi/Marathi deposit-letter template, but it ran in English only, so it does not show absence. Foreign apps already offer a free walkthrough with a paid PDF export (C02). Desk-researchable. |
| KM4 | INSUFFICIENT EVIDENCE | C08, forge-v1.md#C03 | No count of rented households (Census 2011 tables exist but I could not read the Pune values) and no membership counts of 5 named Pune communities. Forge's "3,000 members across about 15 groups" is an ASSUMPTION. PG residents are not counted as households in the Census, so the 300,000 figure needs another source (C08). Desk-researchable only for households; community counts need manual joining. |
| KM5 | INSUFFICIENT EVIDENCE | 01-local-market.md#C09, C09 | No tenant-side paid-document startup shutdown found in 01, 02, or my search. The one failure found is on the deposit-holding side (Settl, a PG operator, accused of delaying refunds, C09), which is not this category. A threshold of "fewer than 2 found" is met by absence, but the graveyard search was shallow (no Tracxn or CB Insights access). I do not count absence in a 3/10 search as a pass. |

## Flaws
### FM1 — FATAL
- flaw: No demand evidence exists that Indian tenants pay for a tenant-side document, inspection or deposit-recovery product. Forge's own assumption C09 ("tenants will pay when free checklists and letter templates exist") is untested, and its price anchor is a state process costing ₹1,500–3,500 in total, which includes duty the landlord is meant to bear. Rule 3 needs at least one verified demand-evidence item. None is in forge-v1, economics-v1, 01 or 02.
- evidence: [C01] Forge lists no competitor with a tenant-facing price and review or revenue sign. [source: forge-v1.md#C09, forge-v1.md Positioning table]
- evidence: [C02] The paid move-in inspection products I found are foreign (Deposit Defender, RentProof, Move Inspector), and RentProof gives the walkthrough free and charges only for a PDF export. (global) [source: https://www.producthunt.com/p/rentproof-rental-inspection-reports/rentproof]
- evidence: [C03] The only India-specific inspection offer found is a Chennai managed property service, with no price or review data. (other city: Chennai) [source: https://pixel-perfect-page-450.lovable.app/inspection/move-in-inspection]
- fix would change customer/problem/revenue model: yes. The only way to supply demand evidence is a different payer (landlord, operator, platform) or a different model (subscription, commission, or B2B). If the evidence exists for tenants, desk research (app-store review counts, pricing pages) could find it, but 3 targeted searches did not.

### FM2 — FATAL
- flaw: The price ceiling is incompatible with any acquisition channel the plan has. Conservative blended CAC is ₹1,426 against ₹170 gross profit, and even forge's base-case ads CAC (₹833) is about 2x the ₹399 price. The product is a one-time purchase with no repeat, so CAC cannot be repaid. The only channels that work (free WhatsApp groups and referral) are the ones with unverified access (forge-v1.md#C12). This is a demand-side price problem, not an execution one: a tenant who has not had a dispute has no urgency to buy insurance-like paperwork. The pain event (deposit withheld) happens at exit, up to 11 months after the purchase point at move-in.
- evidence: economics-v1.md Scenarios table (conservative payback "never"; blended CAC ₹1,426), economics-v1.md Verdict inputs ("conservative unit economics positive: no").
- fix would change customer/problem/revenue model: yes. Fixing it needs a higher price, repeat revenue or a distribution partner that carries CAC (PG operator, college, society), which changes the customer or revenue model. That is a pivot under rule 5.

### FM3 — FIXABLE
- flaw: Recurrence of the pain in Pune is unproven (KM2). One anecdote and unsourced law-firm marketing do not show frequency.
- evidence: [C04] The Pune-focused law-firm article offers a Zolo Stays PG example with a ₹12,000 deposit and a 45-banking-day refund term, but does not say whether the case is real. [source: https://sudhirrao.com/insights/pg-not-returning-security-deposit-legal-remedies, 2026-08-06]
- evidence: [C05] A search for Pune commission orders on PG deposits returned no case. (Pune) [source: https://sudhirrao.com/insights/pg-not-returning-security-deposit-legal-remedies]
- what would fix it: a dated list of at least 20 Pune disputes (r/pune threads, e-Jagriti/consumer commission orders, local press) from 2024-10 to 2026-10, or a Pune/Maharashtra tenant survey with sample size. Obtainable by desk research: partly (Reddit and commission search are open, but the list takes manual work). It would not by itself fix FM1 or FM2.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: Substitutes are unmeasured and strong. "Do nothing", a free lawyer-written notice template, a registered leave-and-licence agreement via the state/NoBroker route, the tenant's own phone photos, and Registrationwala's notice product all cover parts of the kit. Forge itself concedes the report has free substitutes and that the letter is "not legal advice".
- evidence: [C06] NoBroker's Pune guide puts the registered agreement cost at stamp duty 0.25% of rent plus deposit, a ₹1,000 registration fee and ₹700–1,000 facilitation charges. (Pune) [source: https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/]
- evidence: [C07] Searching for free deposit-refund letter templates returned only English-language generic templates and no Hindi or Marathi versions, so the localisation gap may be real but the search was too weak to establish it. [source: https://chw.dhis2.org/template/deposit-refund-letter-template.html]
- what would fix it: the KM3 audit (top-10 results for three queries in three languages, plus tenant features of NoBroker, Housing.com, MagicBricks and 2 others, each component marked). Desk-researchable: yes. It might confirm a Hindi/Marathi gap, but a language gap does not prove willingness to pay.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Market size and reachable pool are asserted, not counted. Forge's 3,000-member reach and the roughly 100 customers are all ASSUMPTION; economics-v1 conservative case yields 17 customers in 3 months. The date matters: the next large student intake (June–August) is 8 months away from 2026-10-15, so the fixed-calendar demand peak is not in the window (forge-v1.md#C13).
- evidence: [C08] My search for Pune rented households and PG residents found only the Census 2011 table index and an SECC household count of 751,874 for Pune district whose column layout is unclear. No PG or hostel resident count was found. [source: https://secc.gov.in/getAllCategoryHouseOwnershipStatusDistrictLgdReport.htm/27/490]
- what would fix it: Census 2011 H-series table for Pune UA (rented share), a Pune university or AICTE/AISHE enrolment figure for outstation students, and public member counts for 5 named Pune groups. Obtainable by desk research: households and enrolment yes; group counts need manual joining of public groups.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Timing argument is weak. The only "why now" is the Pune police order of 2026-07-03, which targets landlords and PG operators and does not create tenant paperwork needs (forge-v1.md#C04 concedes it burdens landlords). If anything, the order may push operators to formalise agreements themselves, which reduces tenant need for a separate template.
- evidence: forge-v1.md#C04; 02-signals.md#S07.
- what would fix it: a source showing tenant-side demand rising after the order (search trends, complaint volume, operator behaviour). Desk-researchable: weakly (Google Trends for Pune queries could be pulled).
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Forge names no tenant-facing competitor price with a review or revenue sign; Registrationwala price "not shown". [source: forge-v1.md Positioning table, internal file]
- [C02] RentProof offers a free walkthrough with a one-time paid PDF export; Move Inspector charges a one-time fee per inspection; Deposit Defender and PropCheckAI are other rental inspection apps. All are non-Indian or not shown as Indian. (global) [source: https://www.producthunt.com/p/rentproof-rental-inspection-reports/rentproof]
- [C03] A Chennai property-management page offers a move-in inspection with photo or video, meter readings and tenant acknowledgement as a managed service. (other city: Chennai) [source: https://pixel-perfect-page-450.lovable.app/inspection/move-in-inspection]
- [C04] A Pune-focused law-firm article (published 2026-08-06) says a PG operator missing its own refund deadline can be deficiency in service, and that a legal notice often settles the dispute; its Zolo Stays Koregaon Park example is not stated to be a real case. (Pune) [source: https://sudhirrao.com/insights/pg-not-returning-security-deposit-legal-remedies, 2026-08-06]
- [C05] A search for Pune consumer commission orders on PG deposits returned electricity-deposit orders from MSEDCL and no PG case. (Pune) [source: https://www.mahadiscom.in/wp-content/uploads/2019/11/Case-No.-48-of-2019.pdf]
- [C06] NoBroker's Pune leave-and-licence guide lists stamp duty 0.25% of total rent plus deposit, ₹1,000 registration and ₹700–1,000 facilitation charges; a NoBroker forum estimate puts the total at ₹1,500–3,500 for Maharashtra. (Pune / Maharashtra) [source: https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/]
- [C07] Free English deposit-refund letter templates are widely available; no Hindi or Marathi versions surfaced in one English-language query. [source: https://chw.dhis2.org/template/deposit-refund-letter-template.html]
- [C08] An SECC table gives 751,874 total households for Pune district (column layout for rented share unclear); no PG or hostel resident count found. (Pune district, 2011-era data) [source: https://secc.gov.in/getAllCategoryHouseOwnershipStatusDistrictLgdReport.htm/27/490]
- [C09] Settl, a coliving PG operator, was reported to delay deposit refunds to former tenants in Bengaluru, Hyderabad, Gurugram and Chennai. This shows deposit pain at operators but not a tenant-side product failure. (other city: Bengaluru, Hyderabad, Gurugram, Chennai) [source: https://inc42.com/buzz/settls-tenants-allege-delay-in-security-deposit-refunds-report/]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| none | n/a | Round 1 |
