---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: forge
version: 1
created: 2026-10-15T09:28:59Z
---

## Core identity
- customer: tenants in Pune who rent a bed in a PG or a room in a shared flat (students and early-career IT workers), paying individually.
- problem: tenants hand over a deposit with no written terms and no dated record of the unit's condition at move-in, so they hold little proof if the deposit is withheld at exit.
- revenue model: ₹399 one-time kit paid by UPI up front (move-in condition photo report, agreement template, deposit-return demand letter in English, Hindi or Marathi). Optional ₹149 personalised exit letter.
- pivot declared: no

Thin-data note: Pune demand is unverified. 01-local-market.md coverage is 3/10 and the only Pune tenant-side evidence is one anecdote. Confidence in every Pune-specific number below is low.

## Persona
- [C01] A Pune PG tenant, Sukoon PG, filed a consumer complaint on 2026-04-19 about a withheld deposit with no written contract. Single anecdote, not recurrence evidence. [source: https://voxya.com/consumer-complaints/renter-not-giving-deposit-money/264368, 2026-04-19]
- [C02] Rent in Pune PGs is cited at ₹6,000–18,000 per month, so a deposit of one to two months' rent is roughly ₹6,000–36,000 (inference: deposit size is an ASSUMPTION, not sourced). [source: https://fn.mahacet.org/category-check/blog/cost-of-living-pune-international-students.html; inference: deposit multiple not in source]
- [C03] Kothrud is described as a student locality, Hinjewadi as an IT hub with students and professionals, and Kharadi and Viman Nagar as corporate-park stay areas. No headcounts were found. [source: https://housing.com/news/top-pg-locations-in-pune/]
- [C04] Pune police ordered on 2026-07-03 that PG operators and landlords submit tenant details; 113 landlords and PG operators faced action. This burdens landlords, not tenants. [source: https://www.punekarnews.in/?p=241832]
- Where they spend today on this problem: the free route is a lawyer-written notice template or a consumer complaint (no fee quoted in sources found); paid lawyer notice prices were not found. Registered agreements cost roughly ₹1,500–3,500 in stamp duty and fees, per a community answer. [source: https://www.nobroker.in/forum/how-much-does-online-rent-agreement-cost-in-maharashtra-with-e-registration/]

## Narrowest wedge
- First product: the move-in condition photo report only, delivered as a PDF through a WhatsApp flow. The tenant sends room photos and meter readings on move-in day; the founder or a no-code form returns a dated, itemised report with a signature line for the PG operator. Price ₹399 includes the demand-letter template for later use.
- First segment: one micro-segment, women and men newly joining PGs near a single college cluster or IT park (for example Kothrud colleges or Kharadi/Hinjewadi), during an intake month. The segment choice is an ASSUMPTION; no data ranks the areas.
- Paid transaction path: move-in is a dated, concentrated event (June–August student intake, and IT joining dates). [ASSUMPTION: intake seasonality is common knowledge, not sourced for Pune]. Today is 2026-10-15, so the next large student intake is outside the 3-month first-revenue window (K6); the IT-joiner and mid-year-move population is the available base.
- Not a registered agreement: a leave and licence agreement must be registered under the Maharashtra Rent Control Act to be valid [source: https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/]. The template in the kit is not a substitute and must say so.

## Problem severity
- [C05] Consumer-court write-ups from Pune law firms describe PG deposit non-refund as a deficiency-in-service claim and state that a written notice often settles the matter. Marketing content, not statistics. [source: https://sudhirrao.com/insights/pg-owner-not-returning-security-deposit-legal-remedy, 2026-08-12]
- [C06] Q&A forums carry multiple PG deposit-refund questions (Lawrato, Kaanoon), none with Pune counts or dates sorted by city. [source: https://lawrato.com/consumer-court-legal-advice/health-hazard-in-pg-and-them-not-giving-my-deposit-back-255564]
- [C07] Rent-deposit disputes are not separated in the national complaint data in 02-signals; e-commerce is about 29% of 1,771,622 National Consumer Helpline grievances in 2025. This does not measure tenancy pain. (national) [source: https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm]
- reasoning: frequency, cost and urgency are all unquantified for Pune. Severity per incident (₹6,000–36,000 at risk, ASSUMPTION on deposit size) is moderate; incident rate is unknown. This is the weakest part of the idea.

## Path to first 100 customers
All conversion figures are ASSUMPTION; no Pune funnel data exists in the inputs.

| channel | reach | conversion | customers | basis |
|---|---|---|---|---|
| College, PG and IT-park WhatsApp/Telegram groups (founder posts; admin permission needed) | 3,000 members across ~15 groups | 1.5% | ~45 | ASSUMPTION; group access and reach unverified (L02 is weak) |
| Instagram ads, Pune 18–30, move-in/PG interest, ₹15,000 spend | ~60,000 reached, 1% click | 3% of clicks | ~18 | ASSUMPTION; CPM and conversion not sourced |
| Instagram organic/reels in English, Hindi, Marathi (K3 skill) | 20,000 views | 0.1% | ~20 | ASSUMPTION |
| Referral / PG-roommate sharing (₹50 credit) | 40 buyers x 0.5 referrals | 100% | ~20 | ASSUMPTION |
| Total | | | ~103 | all ASSUMPTION |

- Channel risk: no Pune data on group sizes or ad cost. If WhatsApp group posting is restricted by admins, the first channel falls to near zero.
- Payment rail: UPI is near-universal at the national level. [source: https://startuptalky.com/upi-transactions-september-2026/, 2026-09] (national)
- Estimated cost: ₹15,000 ads + ~₹5,000 tooling and printing + LLM drafting at cents per document (S09 prices conflict). Within K1 (ASSUMPTION).

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| NoBroker rental agreement (Pune) | https://www.nobroker.in/rental-agreement-in-bavdhan-pune/ | Pune price not shown in results; community estimate ₹1,500–3,500 total including stamp duty and registration | They produce a registered, legally valid agreement for landlord and tenant. We do not; we add a condition record and an exit letter. Overlap on the agreement template. | https://www.nobroker.in/forum/how-much-does-online-rent-agreement-cost-in-maharashtra-with-e-registration/ |
| Maharashtra IGR e-registration portal | https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/ (guide; portal URL not opened) | Stamp duty 0.25% of rent plus ₹1,000 registration fee | Official route, free of service fee. We do not compete on registration. | https://housing.com/news/stamp-duty-registration-laws-rentals-maharashtra |
| Free generic checklists (Jotform, FormBuilder, iOS inspection apps) | https://formbuilder.ai/templates/free-apartment-move-in-inspection-checklist-template | free / free with in-app purchases | They are not India-specific or in Hindi/Marathi. A free substitute exists for the report; the paid part is localisation and the letter. | https://jotform.com/app-templates/move-in-checklist-app |
| Lawyer-written legal notices (Lawrato, Kaanoon, local advocates) | https://lawrato.com/consumer-court-legal-advice/health-hazard-in-pg-and-them-not-giving-my-deposit-back-255564 | not found | A lawyer's notice carries legal weight; our letter is a template and not legal advice. | https://sudhirrao.com/insights/pg-owner-not-returning-security-deposit-legal-remedy |
| Registrationwala security deposit refund legal notice | https://www.registrationwala.com/legal-docs/security-deposit-refund-legal-notice | not shown in snippet | Direct substitute for the demand letter; price unchecked. | https://www.registrationwala.com/legal-docs/security-deposit-refund-legal-notice |

- No Pune competitor selling a tenant-side kit was found; absence in a 3/10 coverage search is not proof of absence.

## Moat over time
- None yet. Templates and photo reports are copyable.
- Possible, unproven: a dated dataset of Pune PG operators' deposit behaviour from kit users (operator-level reputation), which grows with users but raises consent and DPDP obligations (full duties around 2027-05-13) and defamation risk. (national) [source: https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/]

## Assumptions
- [C08] Deposit-withholding is frequent enough among Pune PG tenants for 1–3% of reached tenants to pay ₹399. [ASSUMPTION: only one Pune anecdote and law-firm marketing support it]
- [C09] Tenants will pay for a kit when free checklists and free letter templates exist. [ASSUMPTION: localisation and convenience are the paid value; untested]
- [C10] A PG operator will sign or acknowledge a tenant-prepared condition report. [ASSUMPTION: if not, the report is only the tenant's own photos]
- [C11] A template demand letter, sold without a lawyer, does not breach rules on legal practice or unauthorised legal advice. [ASSUMPTION: not researched; the letter should be framed as a tenant-authored template]
- [C12] WhatsApp group admins in Pune colleges and PG communities allow promotional posts. [ASSUMPTION: L02 is weak and unverified for Pune]
- [C13] Next large intake season (June–August) is outside the K6 window, so first revenue depends on IT joiners and off-cycle movers. [ASSUMPTION]
- [C14] Deposit size is one to two months' rent. [ASSUMPTION]

## Fixes (round 2 only)
- none
