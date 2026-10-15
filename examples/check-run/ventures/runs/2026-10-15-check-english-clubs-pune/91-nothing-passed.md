---
run_id: 2026-10-15-check-english-clubs-pune
agent: main
version: 1
created: 2026-10-15T10:36:35Z
---

## Summary
- ideas generated: 1, screened out: 0, not carried: 0, killed: 1, pivoted: 0
- Final status: I01 KILL (round 1, judge confidence 6/10). Local data coverage for Pune was 3/10, and the evidence auditor could not open any external source (tool failure), so the verdict rests mostly on verified arithmetic over ASSUMPTION inputs plus an absence of demand evidence.

## The ideas, explained
### I01 — Weekend spoken-English conversation clubs for Pune college students, held in cafés, ₹499 per month
- how it works: A student pays ₹499 by UPI for a month. On weekends they go to a partner café in Pune and join a group of 8–12 students for about 90 minutes of guided English conversation. The founder finds students through college WhatsApp groups and Instagram, books the café, collects payments and leads the sessions (03-ideas.md I01; session length, number of sessions and who leads are ASSUMPTIONs, the user did not state them).
- need gap: Pune students who want to practise speaking can use paid institutes (listed at roughly ₹4,000–15,000 a month, promotional sources), AI apps (₹150–299 a month), or free options (open Toastmasters clubs, language-exchange matching, WhatsApp groups). The idea targets a human, in-person, casual option priced in between. No paid Pune café English club was found, which can mean an open gap or no demand; the run could not tell which (01-local-market.md#C19, forge-v1.md).
- how it makes money: ₹499 per member per month. In the conservative case it costs about ₹282 per member to deliver (₹250 of that is an assumed ₹500 café fee shared by 8 paying members), leaving about ₹217. About ₹3,000 a month in ads means 14 paying members are needed to break even, which is two groups (economics-v1.md Calculations).
- what happened: KILLED. The conservative case needs about 12 hours a week at break-even, against your HARD limit of 10 (K2), and the conservative unit economics are not positive (verdict-v1.md, reasons 1–2).

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I01 | Weekend spoken-English conversation clubs for Pune college students, held in cafés, ₹499/month | ideas/I01/verdict-v1.md | (1) Break-even of 14 paying members needs two groups and 12 h/week vs K2 = 10 h HARD; one group fits at 9 h but is loss-making (₹1,736/month gross profit vs ₹3,000 fixed cost) — economics-v1.md Calculations "Founder hours", arithmetic VERIFIED in audit-v1.md. (2) Conservative LTV/CAC 0.98, payback 2.56 months vs 2.5-month paying life, steady-state net about -₹86/month — economics-v1.md. (3) No demand evidence survived the audit; KM1, KM2, KM3 and KE5 NOT MET (no operator with checkable paying customers found; no named barrier to copying) — verdict-v1.md Criteria table. |

## Estimated savings (ESTIMATE)
- capital saved: about ₹15,000–25,000 (the conservative model puts cumulative spend through month 3 at about ₹24,500 and the net outlay at about ₹16,500 after about ₹8,000 of revenue; economics-v1.md Calculations)
- months saved: about 3–5 months of part-time effort, about 130–200 hours (10 h/week for 13–20 weeks)
- assumptions:
  - you would have launched as written and run it for about 3 months before seeing that break-even needs more than 10 hours a week
  - the model's own assumptions hold: ₹500 café fee per session, 40% monthly churn, ₹50 per click, 8 paying members per group; these are ASSUMPTIONs, not Pune data, and the real loss could be lower or higher
  - the ₹1,00,000 limit was never at risk in this model; the saving is small in rupees and mostly in time

## Patterns across deaths
- Only one idea was tested, so these are patterns inside I01, not across a set.
- The hours limit is the binding constraint, not the capital. A model where the founder leads every session scales with their hours, and paying a facilitator (about ₹1,000 per member per month at the assumed rate) turns the margin negative at ₹499.
- Demand is unproven rather than disproven. No Pune student spending data, no café terms and no paying-customer example for this format were found; coverage was 3/10.
- Cheap and free substitutes (₹299 app, open Toastmasters clubs, free groups) sit right under the ₹499 price, and the forge named no moat.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K4 | no-code tools; freelancers within ₹1,00,000 | freelancers hired for specific tasks, total spend within K1 | none | Hiring a facilitator was tested in the model and makes each member lose about ₹783 a month at ₹499, so this stretch does not revive I01. |

- The decisive limit is K2 (10 hours a week, HARD). Only you can change the contract; it is noted here as decisive, not as a suggestion.

## Directions for the next run
- Test one variant that fits one group inside 9 hours: a single larger weekly group (for example 15–20 members) at a café with a minimum-spend model, so that gross profit covers a small ad budget. This changes group size, not the customer or the revenue model, so `/venture:check "<revised idea>" --variants` can judge it. The run did not model this; the numbers are not evidence.
- Test willingness to pay before building anything: take paid pre-registrations at ₹499 from Pune students (a UPI link in college WhatsApp groups) and count payers. The run found no evidence on this; a result of fewer than about 10 prepaid members in 2–3 weeks would match the kill.
- If you want to keep the format but raise the margin, a higher price or an annual or term pass changes the revenue model, which makes it a new idea; run it as one.
- Get the missing Pune facts the run could not find: written café terms from 3 cafés, the Pune Toastmasters dues, and prices of 3 Pune institutes' weekend plans.
- Re-run the audit with working network access. The auditor struck 19 claims because of tool failure, not because the sources were wrong, so the demand-evidence gap may be partly an artefact (verdict-v1.md confidence note).
