---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: judge
version: 1
created: 2026-10-15T09:36:45Z
---

## Hash check
- expected (run-log): 927346e2d6c9e298a695f792c7bda063ef7d43ed6ce7222b91f1933309f450bd
- actual: 927346e2d6c9e298a695f792c7bda063ef7d43ed6ce7222b91f1933309f450bd
- result: MATCH

## Verdict
- verdict: KILL
- round: 1
- confidence: 5

Confidence is lowered because 30 of 34 checked claims were struck as UNREACHABLE (tool failure), not because they were shown false; local coverage is 3/10; and the load-bearing demand and conversion inputs are ASSUMPTIONs. The KILL does not depend on any struck claim. It rests on the missing demand evidence, on the arithmetic and internal-file findings the auditor verified, and on forge's own concessions.

## Criteria (after audit)
Where the prosecutors overlap I took the lower status. Struck claims were removed. Absence of evidence is not support for MET.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | NOT MET (prosecutor-market) | forge-v1.md Positioning table has no tenant-facing price with a review or revenue sign (audit VERIFIED prosecution-market-v1.md#C01). The prosecutor's search evidence (#C02, #C03) is struck. | NOT MET. Nothing surviving meets the 3-provider threshold. |
| KM2 | NOT MET (prosecutor-market) | The only Pune dispute (forge-v1.md#C01) is struck. Nothing else survives. | INSUFFICIENT EVIDENCE (desk-researchable). I did not take NOT MET, because that rests on struck search results. |
| KM3 | INSUFFICIENT EVIDENCE | No audit was done. forge-v1.md concedes free checklists and the Registrationwala substitute exist. | INSUFFICIENT EVIDENCE |
| KM4 | INSUFFICIENT EVIDENCE | Forge reach figures are ASSUMPTION. Census and SECC evidence is struck. | INSUFFICIENT EVIDENCE |
| KM5 | INSUFFICIENT EVIDENCE | No graveyard search was done. Absence in a 3/10 search is not a pass. | INSUFFICIENT EVIDENCE |
| KE1 | INSUFFICIENT EVIDENCE | Arithmetic fits (economics-v1.md Calculations, VERIFIED). Lawyer, registration and fulfilment inputs are ASSUMPTION. Translation is not costed. | INSUFFICIENT EVIDENCE |
| KE2 | NOT MET (prosecutor-execution) | economics-v1.md Calculations (VERIFIED): 17.3 orders and ₹5,173 revenue against about ₹35,700 outlay, so about 119 orders would be needed. No channel policy or comparable seller exists. forge-v1.md#C12 is an ASSUMPTION. | NOT MET |
| KE3 | INSUFFICIENT EVIDENCE | forge-v1.md#C11 says "not researched". No written basis exists. | INSUFFICIENT EVIDENCE. The advocate opinion is not desk-researchable. |
| KE4 | NOT MET (prosecutor-execution) | forge-v1.md Narrowest wedge (internal, unstruck): "Not a registered agreement" and "not a substitute". No stamp-duty or registration route is documented. | NOT MET |
| KE5 | INSUFFICIENT EVIDENCE (leans NOT MET) | forge-v1.md Moat: "None yet." forge-v1.md lists no verified competitor price. Zero of the 3 required paid examples exist. | INSUFFICIENT EVIDENCE, treated as NOT MET for PASS |
| KE6 | NOT MET (prosecutor-execution) | No data-handling plan in forge-v1.md or economics-v1.md. The channels are all Meta-owned. | NOT MET |

## Decisive reasons
1. A FATAL flaw survived the audit. FM2 and FE1 rest on internal-file evidence that the auditor recomputed and left unstruck. Conservative blended CAC is ₹1,426 (cash-only ₹872) against ₹170 gross profit per kit. The product is one-time with no repeat, so payback never occurs. Conservative volume is about 17 customers in 3 months against 17 per month break-even before CAC. Both prosecutors state that any fix needs a higher price, repeat revenue or a different payer. That changes the revenue model or the customer, so it meets the FATAL definition. — economics-v1.md#Scenarios, #Calculations, #Verdict inputs; prosecution-market-v1.md#FM2; prosecution-execution-v1.md#FE1; audit-v1.md "Not struck" note
2. Caveat on reason 1. The ad CPC (economics-v1.md#C01) and labour rate (#C04) inputs are struck, and the conversion rates are ASSUMPTION. I do not rely on the ₹5,500 ad CAC. The finding still stands on three points. The group channel is ₹400 CAC on a ₹170 margin even before the ad channel is counted. The 17.3-customer volume against a roughly 119-order requirement is internal arithmetic. Forge's own base-case ad CAC (₹833 against a ₹399 price) is also not recovered. Those figures are low-confidence, but they point the same way and nothing surviving points the other way.
3. No demand evidence survives. Forge names no tenant-facing competitor with a price and a review or revenue sign. The only Pune pain anecdote is struck. The prosecutors' searches found no Indian tenant-side seller, but those results are struck. Rule 3 requires verified demand evidence, and a PASS is impossible. — audit-v1.md Summary; forge-v1.md Positioning table; forge-v1.md#C08, #C09 (ASSUMPTIONs)
4. KE4 (the agreement is not valid or registered), KE6 (no data-handling plan) and KE2 (orders needed to recover capital) are NOT MET on unstruck internal evidence. KM1 is NOT MET. These are more failures than a single revision round can credibly repair without dropping the agreement component or adding a payer. — forge-v1.md Narrowest wedge; economics-v1.md#Calculations
5. REVISE is unavailable. Rule 4 requires every failure to be FIXABLE and no fix to change customer, problem or revenue model. The surviving FATAL flaw requires such a change. KE3 also needs an advocate opinion, which is not desk-researchable.

## Demand evidence
- none surviving

## Conservative economics
- fits contract: no. The conservative case is unit-economics negative (economics-v1.md#Verdict inputs: "conservative unit economics positive: no"; payback never). No HARD constraint is broken: K1 at about ₹35,700, K2 at about 7 h/week, K6 at 2.3 months with a thin margin. K5 legal exposure is unquantified. Several sourced inputs are struck, so the economics are low confidence. They are not positive under any surviving reading.

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| n/a | Verdict is KILL, so no fixable-flaw table applies. | n/a |

## Pivot candidate (KILL only)
- none. Pivots used are 0/2 and the surviving FATAL flaw (FM2/FE1) does point to a change of payer or revenue model. But a candidate must be grounded in surviving, unstruck evidence. No surviving file#claim shows that a PG operator, college, landlord or platform would pay, or that a repeat or higher-price model has demand. forge-v1.md#C04 and the Settl evidence (prosecution-market-v1.md#C09) are struck. A candidate built on assumption would be invented, so I write none. The audit should be re-run once the proxy works. A later pivot would need evidence that survives that re-run.

## Ignored as struck
- economics-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C18
- forge-v1.md#C01, #C02, #C03, #C04, #C05, #C06, #C07; Persona spend line (NoBroker forum ₹1,500–3,500); Wedge registration claim
- prosecution-market-v1.md#C02, #C03, #C04, #C05, #C06, #C07, #C08, #C09
- prosecution-execution-v1.md#C02, #C03, #C04, #C06
- 01-local-market.md#C15; 02-signals.md#C13
- All strikes are UNREACHABLE (tool failure). They show that the sources could not be opened, not that the claims are false.
