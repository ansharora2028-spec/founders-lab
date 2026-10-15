---
run_id: 2026-10-15-pune-b2c-open
agent: main
version: 1
created: 2026-10-15T09:37:59Z
---

## Summary
- ideas generated: 3, screened out: 0, not carried: 1, killed: 2, pivoted: 0   (count each idea once, by its final status)
- Outcome: NOTHING PASSED. Both carried ideas received KILL in round 1 (no revision round, because neither verdict was REVISE).
- Audit caveat: both audits hit a tool failure (proxy refused every fetch). 30 of 34 checked claims for I03 and 49 of 60 table rows for I01 were struck as UNREACHABLE (tool failure). The judges state that neither KILL depends on a struck claim for its decisive reasons, but confidence is lowered (I03: 5/10, I01: 7/10). Local data coverage is 3/10.

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I01 | WhatsApp-based service that drafts and files e-commerce refund and complaint cases for Pune shoppers, flat ₹199 per case. | ideas/I01/verdict-v1.md (KILL, round 1, confidence 7) | KE3 NOT MET on forge's own statement that free general LLMs do the drafting; KE1 and KE6 NOT MET because 20 cases/week and 100 cases/month at 30–45 min per case exceed the HARD 10 h/week (economics-v1.md#C12, #C19); conservative cash result −₹403.5/month (economics-v1.md Verdict inputs). No demand evidence survived the audit. |
| I03 | Tenant protection pack for Pune renters and PG residents: a ₹399 one-time kit (agreement template, move-in condition photo report, deposit-return demand letter). | ideas/I03/verdict-v1.md (KILL, round 1, confidence 5) | FATAL flaw survived the audit: conservative blended CAC ₹1,426 against ₹170 gross profit per kit, one-time purchase so payback never occurs (economics-v1.md Scenarios and Calculations; prosecution-market-v1.md#FM2; prosecution-execution-v1.md#FE1). KE2, KE4, KE6 and KM1 NOT MET. No demand evidence survived. |
| I02 | Paid WhatsApp concierge for Pune housing-society residents that books pre-checked home-service vendors, ₹149 per household per month. | NOT CARRIED (rank), 04-screen.md: 7/25, third of three | Not forged or tried. Screen found Urban Company already has Pune listings across plumbing, electrical and cleaning (04-screen.md#C05, #C06); novelty rated crowded, speed to revenue 1/5 because each society needs committee approval first. The screener rated this on one query. |

## Estimated savings (ESTIMATE)
- capital saved: ₹5,000–₹36,000 per killed idea, so roughly ₹5,000–₹36,000 if the user would have built one of them.
- months saved: about 2–3 months of 7–10 hours per week per idea, which is the time to a first sale plus the period needed to see CAC exceed margin.
- assumptions:
  - ₹5,000 is the economics-v1.md conservative "capital to first revenue" for I01; ₹17,800 for I03, with about ₹35,700 total outlay over three months for I03 (economics-v1.md figures, whose ad-cost and labour inputs are struck as unreachable, so treat the I03 upper end as low confidence).
  - The user would have run the idea to the end of the 3-month contract window before concluding it did not work (ASSUMPTION).
  - The figure is the money spent on the build, not revenue forgone, and not money the user could not have recovered. No resale value of the work is counted.
  - The savings are not independent: the user would likely have built only one idea, not both.

## Patterns across deaths
- No verified demand evidence for either idea. Every competitor price and every grievance statistic that could have supplied it was struck as unreachable in the audit, and both forge files admit willingness to pay is an ASSUMPTION (forge-v1.md#C17 for I01; no tenant-facing price with a review or revenue sign for I03). This is partly a tool failure, so a re-run with network access could change the evidence picture, not necessarily the KILL.
- Low-ticket, one-time B2C products (₹199, ₹399) cannot carry customer-acquisition cost. Both conservative cases are negative: I01 −₹403.5/month cash, I03 blended CAC ₹1,426 against ₹170 gross profit.
- Free substitutes set the price: the National Consumer Helpline, free chatbots and free templates (I01 KE3; I03 KM3 and forge concessions). Both ideas are thin packaging over something free.
- HARD K2 (10 hours/week) was decisive for I01: the locked volume targets could not fit in 10 hours at the file's own minutes-per-case.
- Legal exposure (practice of law under the Advocates Act, 1961) was raised on both and left unresolved, and an advocate opinion is not desk-researchable.
- Local data was thin (coverage 3/10). Pune demand is unverified for all three ideas, and most signals were national.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K4 | no-code tools; can hire freelancers | freelancer spend allowed, only within the ₹1,00,000 capital limit (K1) | none | It would not revive either idea. I01 died on free substitutes and on hours per case, and I03 died on acquisition cost against margin; neither is cured by paying a freelancer. |

- K1, K2, K3, K5, K6, K7, K8 and K9 are HARD. K2 was decisive for I01. Only the user can change a HARD constraint, and this report does not suggest doing so.
- No FLEXIBLE stretch was used anywhere in the run.

## Directions for the next run
- Re-run `/venture:kill 2026-10-15-pune-b2c-open I01 I03` once network access works, so the audit can open sources. That gives a fair audit; it does not change the locked criteria.
- Start from demand that already exists in Pune rather than from a regulation or press signal. Look for a space where Pune people already pay a recurring or higher-ticket price, because a one-time ₹200–400 product failed on CAC twice.
- Prefer ideas where the paid part is something a free chatbot or template cannot do, and where delivery time per customer is roughly fixed, so 10 hours per week is not the cap.
- Signals that held up: UPI usage at a record 24.51 billion transactions in August 2026 (national, S04) and WhatsApp Business billing in INR (S10), both of which lower payment and delivery friction. They support collecting money, not demand for a product.
- Lenses not used this run: unfair-advantage (the contract states none), boring-b2b (excluded by K7) and unbundle (no incumbent found that a segment overpays for). A next run could add a stated advantage, such as a community the user belongs to.
