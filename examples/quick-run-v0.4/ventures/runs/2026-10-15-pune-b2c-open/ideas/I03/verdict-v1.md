---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: judge
version: 1
created: 2026-10-15T10:47:33Z
---

## Hash check
- expected (run-log): 273037359ce441b3befa000eb65cb84b75b2a3aca8ff7db008f9cd54e9a129ad
- actual: 273037359ce441b3befa000eb65cb84b75b2a3aca8ff7db008f9cd54e9a129ad
- result: MATCH

## Verdict
- verdict: KILL
- round: 1
- confidence: 5

## Criteria (after audit)
Where the prosecutors overlap I took the lower status. KM criteria come from prosecution-market-v1.md and KE criteria from prosecution-execution-v1.md, so they do not overlap. Struck claims were removed before reading the status.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | NOT MET | The Ghare price and 166 reviews (forge-v1.md#C03) are struck. The prosecutor found at most one independent, and no third provider surfaced. | NOT MET |
| KM2 | NOT MET | No team or vendor per-job quote exists (economics-v1.md#C06 is an ASSUMPTION). The Urban Company prices are struck, so there is no multi-listing median. | NOT MET |
| KM3 | INSUFFICIENT EVIDENCE | The Raviwar Peth complaint evidence (01-local-market.md#C44) is struck. Neither half of the test is evidenced. | NOT MET for PASS. Desk-researchable in part, but the complaint count and provider-policy checks alone would not settle it. |
| KM4 | INSUFFICIENT EVIDENCE | The Meta CPC and lead-cost range (economics-v1.md#C12) is struck. No Pune search volume was found. | NOT MET for PASS. Keyword volume is desk-researchable. |
| KM5 | INSUFFICIENT EVIDENCE | The Clean Fanatics claim (prosecution-market-v1.md#C09) is struck. No repeat rate was shown. | NOT MET for PASS. Desk-researchable. |
| KE1 | NOT MET | The economics-v1.md Calculations were verified by the auditor. At 25 jobs a month the hours are about 10.7 per week (prosecution-execution-v1.md#E01, arithmetic recomputed in audit-v1.md), which exceeds the K2 HARD cap of 10. | NOT MET. Fixable by lowering the volume, but then the thin margin is not covered. |
| KE2 | INSUFFICIENT EVIDENCE | There is no Pune team quote or named team anywhere in the record. The modelled conservative rate of Rs 2,400 is above the KE2 ceiling of Rs 2,300. | NOT MET for PASS. Not desk-researchable, because it needs calls to teams. |
| KE3 | INSUFFICIENT EVIDENCE | The Maharashtra bill source (economics-v1.md#C24) is struck. There is no official text and no insurance quote. | NOT MET for PASS. The official text is desk-researchable. The insurance quote and the applicability opinion are not. |
| KE4 | NOT MET | The verified conservative arithmetic gives Rs -251 per job before CAC and Rs -813 after it (economics-v1.md Scenarios and Calculations). The threshold is at least Rs 400. No test bookings exist. | NOT MET. The inputs behind it are ASSUMPTIONs, so the result is weakly grounded but is the only surviving estimate. |
| KE5 | NOT MET | The Rs 3,499 tier is about 117% of Rs 2,999. The Rs 2,999 and Rs 3,499 figures are struck sources, so the 110% test rests on struck evidence. No premium evidence, no incumbent-response evidence, and the two non-marketplace channels are unsourced (forge-v1.md#C19). | NOT MET. The status stands on the absence of positive evidence, not on the struck prices. |

## Decisive reasons
1. PASS is unavailable. It needs every criterion MET. Only the economics arithmetic survived the audit (1 of 23 claims checked verified). Five criteria are NOT MET and four are INSUFFICIENT EVIDENCE — audit-v1.md#Summary; prosecution-market-v1.md#Criteria assessment; prosecution-execution-v1.md#Criteria assessment.
2. Demand evidence is none surviving. D05, the Urban Company reviews and prices, and the Ghare listing were all struck as UNREACHABLE (tool failure). This is an environment failure, not a finding that the sources are false. Rule 3 still requires verified demand evidence, so PASS is unavailable on this ground alone — audit-v1.md#Summary; 01-local-market.md#C32, #C34; forge-v1.md#C01-C04.
3. The conservative economics are negative and the surviving estimate does not fit the contract. The result is Rs -251 per job before CAC, Rs -813 after CAC, no break-even at any volume, and a certain loss — economics-v1.md#Scenarios, #Verdict inputs; audit-v1.md#Checked claims (arithmetic VERIFIED). The result depends on the unsourced team rate (economics-v1.md#C06 ASSUMPTION), so I do not treat it as a settled fact. I use it as the best surviving estimate. The sourced conservative inputs themselves were struck, so the negative result is a modelled outcome, not a verified one.
4. FE1 is not FATAL. Its price evidence (prosecution-execution-v1.md#FE1 C02) was struck. FE1 itself states that the fix does not change customer, problem or revenue model. It does not contradict verified evidence. It fails the FATAL definition, so I treat it as FIXABLE: a team rate near Rs 1,600-1,650 or a higher achievable price would close the gap — prosecution-execution-v1.md#FE1; audit-v1.md#Struck claims.
5. REVISE is unavailable. REVISE needs every failure to be FIXABLE. KE2 (INSUFFICIENT) can only be settled by calling Pune cleaning teams, which is not desk research. KE3's insurance quote and applicability opinion are not desk-researchable. KM3 needs a live pilot to show customers switch (prosecution-market-v1.md#FM3). FE6 (supply leakage) is not desk-obtainable either. Under the rubric these count as NOT MET, not FIXABLE. Rule 5 (otherwise KILL) applies — scoring-rubric Part 2 rules 4-5; prosecution-execution-v1.md#KE2, #FE4, #FE6.
6. The idea has no verified margin and no verified demand, and the local data is thin (coverage 4/10, every fetch failed). The kill is for lack of positive evidence, not because a decisive contradiction was proved. The idea is not shown to be impossible.

## Demand evidence
- none surviving. Every candidate was struck as UNREACHABLE (tool failure): D05, forge-v1.md#C01-C04, and the Raviwar Peth reviews.

## Conservative economics
- fits contract: no. Unit economics are not positive (Rs -251 per job before CAC, Rs -813 after) — economics-v1.md#Scenarios, #Verdict inputs; audit-v1.md#Checked claims (arithmetic verified).
- The capital HARD constraints themselves are not broken (K1: Rs 29,500 to first revenue and about Rs 58,300 at month 3; K6: 2 months). The failure is rule 3 (positive economics), not a HARD-constraint breach.
- Hours: about 10.7 h/week at the 25 jobs needed (prosecution-execution-v1.md#E01), against the K2 cap of 10.

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| n/a — verdict is KILL | n/a | n/a |

## Pivot candidate (KILL only)
- none — the decisive reasons are missing verified evidence and negative conservative economics, not a fix that changes customer, problem or revenue model. Every flaw in both prosecutions is marked "fix would change customer/problem/revenue model: no". Pivot conditions in the rubric are not met. Pivots used are 0/2.

## Ignored as struck
- economics-v1.md#C01, #C02, #C03, #C06 (apna and Indeed), #C07, #C09, #C12, #C19, #C21, #C24
- forge-v1.md#C01, #C02, #C03, #C04, #C05, #C07, #C08, #C13
- 01-local-market.md#C32, #C34, #C44
- 02-signals.md#C02, #S07
- prosecution-market-v1.md#C02, #C08, #C09
- prosecution-execution-v1.md#E02, FE3 C05, FE1 C02
- Unaudited and treated with caution: prosecution-market-v1.md#C01, #C03, #C05, #C06 and prosecution-execution-v1.md#FE4 C08, #E04, FE3 C06/C07. I did not rely on them for any status.
