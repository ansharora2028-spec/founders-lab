---
run_id: 2026-10-15-pune-b2c-open
agent: main
version: 1
created: 2026-10-15T14:30:00Z
---

## Summary
- ideas generated: 3, screened out: 0, killed: 1 (I03), not carried (rank): 2 (I01, I02), pivoted: 0
- Only I03 was forged and judged (quick mode carries one idea). I01 and I02 were never prosecuted, so this run says nothing about whether they would survive.
- Local data coverage was 3/10. All verdict confidence is lowered accordingly.

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I03 | WhatsApp-community resale board for tenants leaving IT-corridor flats in Pune; sellers pay ₹199 per listing | ideas/I03/verdict-v1.md | KILL, confidence 7. "No criterion is MET. Nine of ten are INSUFFICIENT EVIDENCE and KE5 is NOT MET." Demand evidence: "none surviving". The central claim that sellers pay ₹199 when OLX and Facebook are free is forge's own unevidenced ASSUMPTION (forge-v1.md#C10). Moat: "None yet" (forge-v1.md, Moat over time). |
| I01 | ₹499 pay-per-check verification of Pune rent agreements | — | NOT CARRIED (rank): 11/25 behind I03 12/25 (04-screen.md). Not judged. |
| I02 | Marathi/Hindi-first spoken-English practice over WhatsApp at ₹299/month | — | NOT CARRIED (rank): 8/25 (04-screen.md). Not judged. Screen found novelty "crowded" with five named competitors. |

## Estimated savings (ESTIMATE)
- capital saved: ₹10,000–₹25,000
- months saved: 3–6 months of part-time effort
- assumptions:
  - ASSUMPTION: the founder would have spent the modelled ₹10,500 setup (economics-v1.md#C10) plus ₹0–₹15,000 on listing tests or ads before concluding sellers would not pay.
  - ASSUMPTION: at 10 hours/week the community build and first paid-seller test take about 12 weeks (economics-v1.md#C16) and a further 1–3 months to read the result.
  - These are estimates for I03 only. The economics file itself found the idea cash-positive on assumed inputs, so the loss is not certain; the kill is on absent evidence, not on proven failure.

## Patterns across deaths
- Absence of surviving demand evidence, not a broken HARD constraint. The conservative case fit the contract on paper (₹10,500 against ₹1,00,000; first revenue at 2.8 months against 3).
- Thin local data. Pune coverage was 3/10, so Pune willingness-to-pay could not be shown from desk research.
- Process limit that affected this verdict: the evidence auditor's fetch tool was refused by the proxy for every URL. Fourteen claims were struck as UNREACHABLE. The Judge states this "does not show that the sources are wrong" and that "a re-audit with a working fetch tool could change which claims count." The KILL rests on the lack of surviving positive evidence, and on forge's own admissions, not on any source being shown false.
- The decisive structural problem for I03 was that a ₹199 seller fee competes with free channels (OLX, Facebook Marketplace, society groups). The only fix the Judge saw was a commission or buyer fee, which would change the revenue model.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K4 | no-code tools; freelancers within K1 | freelancer hiring, only within K1 | none | No flexible constraint would revive I03. Its failures were missing demand evidence and fee bypass, not capital, hours or skills. |

HARD constraints were not decisive. K6 (3 months) left about one week of slack on I03, which counted against it but was not the reason for the kill.

## Directions for the next run
- Run `/venture:run` again at `standard` depth so I01 and I02 are actually prosecuted. Quick mode killed the top-ranked idea and left the other two untested.
- Re-run the audit with a working fetch tool before treating the 14 UNREACHABLE strikes as final.
- I01 (rent-agreement check) had the only Pune-specific signal (S06) but is contested by free routes (Maharashtra IGR portal, police verification) and has a K3 skills gap. Needs a different wedge or evidence that tenants pay for it.
- Untested manual checks for any future idea: a dated count of used-furniture listings in the six corridor areas, and a small seller-willingness-to-pay test. These are the evidence types desk research could not supply.
