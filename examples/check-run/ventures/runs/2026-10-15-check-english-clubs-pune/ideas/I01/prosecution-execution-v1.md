---
run_id: 2026-10-15-check-english-clubs-pune
idea_id: I01
agent: prosecutor-execution
version: 1
created: 2026-10-15T10:32:10Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/00-contract.md
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/01-local-market.md
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/02-signals.md
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/ideas/I01/kill-criteria.md
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/ideas/I01/forge-v1.md
- <project>/ventures/runs/2026-10-15-check-english-clubs-pune/ideas/I01/economics-v1.md
- Plus the rules and schema files: ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md, ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md
- Web searches run by this prosecutor (results are search summaries; pages were not opened).

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C08, economics-v1.md Calculations "Founder hours", economics-v1.md Constraint check K2 | The economics modeler's own conservative case needs 12 h/week for two groups, which is the minimum to reach break-even (14 paying members, groups of 8). K2 is HARD at 10 h, so this fails. Spend (about ₹24,500 over 3 months) and first revenue (month 2, an ASSUMPTION) pass, but the hours test fails. The hours table is built on forge-v1.md#C23 (session length and count), which is an ASSUMPTION, not taken from named Pune operators as the criterion requires. At the ~35-50 students the raw idea implies (about 3 groups), hours are about 15 h/week by the same arithmetic (see E04). |
| KE2 | INSUFFICIENT EVIDENCE | forge-v1.md#C22, economics-v1.md#C05, 01-local-market.md#C23, E02 | No Pune café, rate card, quote or minimum-spend figure for a recurring paid group was found by builders or by this prosecutor. 0 of the required 3 venues are evidenced. The criterion says the idea dies unless this is shown, so the judge should treat the absence as a failure to satisfy it. Only a Khed Shivapur (outskirts) venue listing at ₹700 per plate for private gatherings turned up, which is not a student-café rate. |
| KE3 | INSUFFICIENT EVIDENCE | 01-local-market.md#C20-C22, forge-v1.md#C26, E03 | Partial desk answer only: commercial blogs say establishments with under 10 workers file a free one-time intimation, and GST is not triggered below ₹20 lakh. Nothing found on (c) minors and consent, (d) liability, or an insurance quote. The forge's handling of minors is an assumption ("excluded in practice"). No primary source (Maharashtra Labour Department, PMC) was reached. |
| KE4 | INSUFFICIENT EVIDENCE | 01-local-market.md#C15, #C17, forge-v1.md#C04, E01, E05 | Required evidence is missing: prices of at least 3 Pune institutes' shortest or weekend plans (not found), a count of free college English clubs (not found). Toastmasters dues are now partly known (E01): international dues are USD 72 per six months (about USD 12/month) plus any club fee. Open Pune clubs (Pune-West, Aundh) already run in-person group speaking meetings, so incumbent (b) already offers a live in-person group at roughly the same order of price as ₹499 (the INR figure depends on an ASSUMPTION exchange rate). SpeakX appears AI-only (E05), which is mildly favourable. |
| KE5 | NOT MET | economics-v1.md#C09, economics-v1.md Calculations "If a freelance facilitator replaces the founder", forge-v1.md Moat over time, E04 | The threshold is facilitator + venue + fees at or below 50% of ₹499 (₹250) per student at 10 payers and 4 sessions. The modeler's conservative case gives about ₹1,282 per member (₹282 + ₹1,000 facilitator), and even the base-case venue of ₹0 plus a ₹2,000 session facilitator at 10 payers gives ₹800 + ₹32 = ₹832, about 167% of price. Even with the ₹702/hour Superprof rate (01#C04) at 1.5 hours the facilitator costs about ₹421 per student at 10 payers (84%). The forge states the moat as "None yet". No named barrier against a facilitator or member copying the group. |

KM criteria: no comment (the market prosecutor owns them), except the Toastmasters price point noted under KE4, which bears on KM3.

## Flaws
### FE1 — FATAL
- flaw: The idea cannot reach break-even volume within the HARD 10 h/week cap (K2) while the founder is the only facilitator. One group is loss-making (9 h/week, gross profit ₹1,736/month against ₹3,000 fixed boost cost in the conservative case); the second group needed to break even takes 12 h/week.
- evidence: [C01] economics-v1.md Calculations "Founder hours (K2) in conservative case": 9 h at one group, 12 h at two groups. [source: economics-v1.md]
- evidence: [C02] The economics modeler's own constraint check marks K2 as BREAKS in the conservative case. [source: economics-v1.md Constraint check]
- evidence: [C03] K2 is HARD with no stretch range. [source: 00-contract.md K2]
- what would fix it (FIXABLE only): not fixable by evidence alone. It would need a delivery model that cuts weekly hours to 10 or fewer at 14+ payers, such as one larger group of 14-15 with a verified café capacity and a proven session length, which also needs proof that a founder-led group of that size works. Not desk-researchable. A hired facilitator is blocked by FE2.
- fix would change customer/problem/revenue model: no

### FE2 — FATAL
- flaw: The model cannot be scaled past the founder's own hours. Hiring a facilitator turns contribution negative at ₹499, and raising the price enough to fix it changes the revenue model.
- evidence: [C04] Facilitator replacing the founder adds ₹1,000 per member per month, contribution ₹217 - ₹1,000 = -₹783. [source: economics-v1.md Calculations]
- evidence: [C05] The only facilitator rate used is a 2016 multi-city British Council posting at INR 1,000/hour, read via search summary. [source: https://www.britishcouncil.in/about/jobs/freelance-trainer-0, as cited in economics-v1.md#C09]. Superprof Pune tutors average ₹702/hour. [source: https://www.superprof.co.in/lessons/english/pune/]
- evidence: [C06] At ₹702/hour, 1.5 hours per session, 10 payers, 4 sessions: ₹702 x 1.5 x 4 / 10 = ₹421 per member per month before venue and fees, which already exceeds the 50% line only after adding venue and fees (₹421 + ₹32 = ₹453, 91% of ₹499). Arithmetic by this prosecutor; the 1.5 h and 10 payers come from forge-v1.md#C23 and kill-criteria KE5.
- what would fix it (FIXABLE only): not fixable at ₹499. Would need a facilitator at or under about ₹120 per hour equivalent (volunteer or student ambassador model) with quality evidence, or a price of roughly ₹1,000 or more per month. A price increase is arguably a revenue-model change, so the main session should check for a pivot.
- fix would change customer/problem/revenue model: yes (price or paid-facilitator structure alters the revenue model)

### FE3 — FIXABLE
- flaw: The conservative case is loss-making at steady state even with unpaid founder time. LTV/CAC is 0.98 and payback (2.56 months) exceeds average paying life (2.5 months). Net at the 16-member ceiling is about -₹86/month.
- evidence: [C07] [source: economics-v1.md Calculations "Payback and lifetime value" and "Break-even volume"]
- what would fix it (FIXABLE only): sourced evidence that churn is below 40% for comparable paid offline clubs, plus a sourced café venue term of ₹0. Churn evidence may exist in press about offline community subscriptions; café terms need calls to cafés, so only partly desk-researchable.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: Venue is unproven. The café is the delivery channel, and no Pune café terms exist. Cafés can refuse a 90-minute group of 8-12 that holds weekend tables on small orders, or demand a fee or revenue share.
- evidence: [C08] No Pune café rate or hosting policy found; the one Pune-area result was a Khed Shivapur listing at ₹700 per plate for 5-60 guests, a private-event price, not a student minimum spend. [source: https://www.venuelook.com/pune/locality/khed-shivapur/venuetype/cafes, search summary]
- evidence: [C09] 01-local-market.md#C23 records café terms as not researched. [source: 01-local-market.md]
- what would fix it (FIXABLE only): 3 Pune cafés with a published event or private-booking rate card or a written minimum-spend quote at ₹150 per head or less. Partly desk-researchable (rate cards on Instagram or Google Maps), otherwise needs phone calls.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Legal exposure is unanswered for liability, minors and safeguarding, and the primary source for Shops and Establishments was not reached. K5 is low risk appetite.
- evidence: [C10] Commercial compliance blogs say establishments with fewer than 10 workers file an intimation (Form F) within 60 days, reportedly free, but give conflicting fees and deadlines and no official page was found; the Keka page gives a 30-day registration. [source: https://www.registerkaro.in/post/gumasta-license-fees ; https://www.keka.com/compliance/forms/maharashtra-shop-and-establishment-registration, search summaries]
- evidence: [C11] The forge assumes no licence is needed and that under-18s are excluded in practice. [source: forge-v1.md#C26]
- what would fix it (FIXABLE only): the Maharashtra Labour Department or Aaple Sarkar rule text for intimation, an insurance quote for event or public-liability cover in Pune, and a written position on under-18 attendance (age gate and consent). Desk-researchable for the first and third items; the insurance quote needs a form submission.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Incumbent price position is weaker than the forge states. Toastmasters is described by the forge as "dues not found". Its international dues are USD 72 per six months per member. Open Pune clubs already run live in-person speaking groups, so the "gap between free and institutes" has a nearby paid substitute and a free-looking one (college clubs, WhatsApp groups) with no cost to copy.
- evidence: [C12] Toastmasters International dues of USD 72 per six-month period plus a USD 25 new-member fee, as shown on the official FAQ in a search summary; club-level fees not shown for Pune clubs. [source: https://www.toastmasters.org/Footer/FAQ/Membership] (global; INR equivalent requires an exchange rate [ASSUMPTION: about ₹85-88 per USD, so about ₹1,000 per month]).
- evidence: [C13] Open Pune clubs exist: Pune-West, Aundh, Pune North East, Pune North West, Pune South. [source: https://www.toastmasters.org/Find-a-Club/01534609-01534609]
- what would fix it (FIXABLE only): Pune club fee pages, price pages for 3 Pune institutes' weekend or demo plans, and a count of free English clubs at the largest Pune colleges. Desk-researchable partly (club pages and institute sites); the college club count needs Instagram or college site checks.
- fix would change customer/problem/revenue model: no

### FE7 — FIXABLE
- flaw: Copy risk with no barrier. The forge's moat is "None yet", the format is a WhatsApp group plus a café, and the economics shows a paid facilitator is unaffordable, so the most capable members or a hired facilitator can run the same group free or cheaper. If it works, a facilitator or ambassador can charge members directly.
- evidence: [C14] Forge states formats can be copied by any person with a café and a WhatsApp group. [source: forge-v1.md Moat over time]
- what would fix it (FIXABLE only): a named, checkable barrier (for example an exclusive café arrangement, a contract with facilitators, a content library with a track record) with evidence that comparable community businesses retained facilitators and members. Little of this is desk-researchable; likely needs an operating pilot.
- fix would change customer/problem/revenue model: no

### FE8 — FIXABLE
- flaw: Acquisition dependence on third-party platforms and an unproven funnel. All reach and conversion figures are ASSUMPTION, the forge path reaches about 77 customers, not 100, and the conservative case reaches about 24 in three months. Instagram, WhatsApp communities and Razorpay or UPI links can change reach, policy or fees. The Instagram channel has a conservative CAC of ₹2,721, about 5.5 times the monthly price.
- evidence: [C15] [source: forge-v1.md Path to first 100 customers and economics-v1.md Scenarios]
- evidence: [C16] Razorpay fee of 2.36% was confirmed only through a search summary. [source: https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/, as cited in economics-v1.md#C03]
- what would fix it (FIXABLE only): a documented comparable launch (Pune or other Indian metro student community or event product) with real conversion data from trial to paid, and a current payment-link fee schedule. Partly desk-researchable.
- fix would change customer/problem/revenue model: no

## Evidence
- [E01] Toastmasters International dues are USD 72 per six-month period (the FAQ summary says this applies from 2026-08-03; older copies show USD 60), prorated mid-cycle, plus a one-time USD 25 new-member fee. Pune club listings show no club dues. [source: https://www.toastmasters.org/Footer/FAQ/Membership] (global)
- [E02] Search for Pune café private-event minimum spend or workshop hosting terms returned overseas venues and one Khed Shivapur listing (Momentt, from ₹700 per plate, 5-60 guests); no Pune student-café rate was found. [source: https://www.venuelook.com/pune/locality/khed-shivapur/venuetype/cafes]
- [E03] Establishments with fewer than 10 workers in Maharashtra reportedly file a one-time intimation instead of full registration, reportedly free, but sources conflict and none is official; confirm on Aaple Sarkar or the Labour Department site. [source: https://www.registerkaro.in/post/gumasta-license-fees] and [source: https://www.keka.com/compliance/forms/maharashtra-shop-and-establishment-registration]
- [E04] Hours arithmetic by this prosecutor from economics-v1.md: one group costs 9 h/week (session 3 h, prep 2, marketing 2, admin 1, café 1); each extra weekly group adds about 3 h of session time. Two groups = 12 h, three groups (the 35-50 students implied by the raw idea) = about 15 h. All hours inputs are ASSUMPTIONs (forge-v1.md#C23). [source: economics-v1.md Calculations]
- [E05] SpeakX presents itself as an AI tutor; a search found no evidence of live group or human sessions in its own materials. The only detailed comparison is by a competitor (EngVarta). [source: https://engvarta.com/engvarta-vs-speakx-indian-english-app-comparison/] and [source: https://www.speakx.com/about]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
