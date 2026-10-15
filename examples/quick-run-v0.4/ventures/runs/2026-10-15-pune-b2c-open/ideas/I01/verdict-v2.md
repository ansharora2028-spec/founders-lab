---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: judge
version: 2
created: 2026-10-15T10:55:55Z
---

## Hash check
- expected (run-log): 408e341c3ad727bab4fc63f71770f5e4267f5de6079ecad526adff66d0d95af9
- actual: 408e341c3ad727bab4fc63f71770f5e4267f5de6079ecad526adff66d0d95af9
- result: MATCH

## Verdict
- verdict: KILL
- round: 2
- confidence: 7

## Criteria (after audit)
Rule used where the prosecutors differ or where evidence is struck: the lower status, because no surviving evidence clearly supports a higher one. The auditor struck 23 of 23 URL rows as UNREACHABLE; all are fetch-tool failures (proxy refusal), not source failures. The Judge ignores them anyway (rule 8). The outcome does not depend on the strikes: the prosecutors' own round-2 assessments, which the diff itself confirms ("Not fixed to the stated bar"), reach the same statuses.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | NOT MET | diff-v2.md#D1 concedes "Not fixed to the stated bar". All seller prices and ratings are struck; no seller shows paying customers; no Maharashtra seller; no cause-of-death evidence (diff-v2.md#D7, NONE). | NOT MET |
| KM2 | INSUFFICIENT EVIDENCE | diff-v2.md#D3 (NONE, "not fixed"). National NCH counts are struck. No Maharashtra or Pune figure. | NOT MET for PASS |
| KM3 | INSUFFICIENT EVIDENCE | diff-v2.md#D4 concedes free guides were not opened; no paid-uptake evidence. | NOT MET for PASS |
| KM4 | NOT MET | diff-v2.md#D2: guidelines advisory in Maharashtra, state Act only a draft, 0 confirmed Maharashtra orders on a non-refundable clause. Limb 2 fails on the diff's own text. | NOT MET |
| KM5 | INSUFFICIENT EVIDENCE | diff-v2.md#D8 (NONE). No Pune community verified, no dated complaint posts. | NOT MET for PASS |
| KE1 | NOT MET | economics-v2.md Constraint check K2 and diff-v2.md#D11: heavier weeks reach about 10.5 hours, which fails "every week, not an average"; dry run not done; D11 carries NONE. Cash limb fits (economics-v2.md, capital Rs 14,500, arithmetic VERIFIED). | NOT MET |
| KE2 | NOT MET | diff-v2.md#D6: no authoritative source that paid non-lawyer drafting is permitted; advocate opinion budgeted, not obtained; no comparable non-lawyer service confirmed. | NOT MET |
| KE3 | NOT MET | diff-v2.md#D9 concedes Rs 150 CAC and 15 files a month "not shown". economics-v2.md Calculations (VERIFIED arithmetic): paid CAC Rs 750 to Rs 5,500 against Rs 413 contribution; conservative volume 24 files in 3 months. | NOT MET |
| KE4 | INSUFFICIENT EVIDENCE | diff-v2.md#D1, #D10: paid analogue prices struck; no sales evidence; DPDP duties not listed or costed. | NOT MET for PASS |
| KE5 | NOT MET | diff-v2.md#D10 (NONE), #D3, #D8: day-30 plan unsourced, Pune volume unknown, no external evidence for a moat. Only the refusal-terms limb is met on paper. | NOT MET |

## Decisive reasons
1. This is round 2. PASS requires every locked criterion MET and verified demand evidence. Six criteria are NOT MET (KM1, KM4, KE1, KE2, KE3, KE5) and four are INSUFFICIENT EVIDENCE, which counts as NOT MET for PASS. A REVISE in round 2 is a KILL (rule 6; rubric rule 5). — prosecution-market-v2.md#Criteria assessment; prosecution-execution-v2.md#Criteria assessment; diff-v2.md#D1-D11
2. Rule 4: rows D3, D7, D8, D10 and D11 carry evidence NONE and score as no fix. The other rows are marked "partly fixed" or "not fixed" by the diff itself, and both prosecutors accepted none of D1-D11. Round 1's fixable list was largely not resolved by desk research, so the "no plausible fix" limb of the KILL rule also applies to KM1, KM4, KE2 and KE3. — diff-v2.md#Unaddressed flaws; prosecution-market-v2.md#Round-2 notes; prosecution-execution-v2.md#Round-2 notes
3. No demand evidence survives. All seller-price anchors and NCH figures are struck as unreachable. Independently of the audit, the diff and the market prosecutor state that no seller shows paying customers and no evidence of buyers paying while free NCH 1915 exists. Rule 3 is unmet. — audit-v2.md#Summary; diff-v2.md#D1; prosecution-market-v2.md#FM1
4. Scale. The conservative case gives about Rs 720 net a month at 8 files and a ceiling of about Rs 4,437 at the K2 cap of 17 files; paid acquisition loses money per customer; Rs 10,000 net a month is out of reach at Rs 500. Arithmetic is VERIFIED. The contract states no income target, so this is not a HARD breach and is not treated as FATAL. It makes KE3 and KE5 unreachable by desk research. — economics-v2.md#Calculations; audit-v2.md#Checked claims
5. FATAL flags not accepted. FE1 (legal permission) rests on E1 and E2, both struck, and on an absence-of-authority statement; it fails the FATAL definition on surviving evidence and is treated as FIXABLE, though KE2 is NOT MET independently because the burden of proof is on the idea. FE4 (draft Maharashtra Act) rests on E4, struck; discarded as FATAL. FE2 breaks no HARD constraint; treated as FIXABLE. The KILL does not rest on any FATAL flaw. — prosecution-execution-v2.md#FE1, #FE2, #FE4; audit-v2.md#Struck claims

## Demand evidence
- none surviving

## Conservative economics
- fits contract: yes on cash and hours at the modelled volume (K1 peak Rs 19,500; K2 7.8 hours average; K6 2.0 months; K7, K8) — economics-v2.md#Constraint check. K2 breaks if intake exceeds 4 files a week; K5 legal exposure unresolved; K9 employer permission is an ASSUMPTION. Per-file contribution is positive (Rs 413). Business size is not viable (reason 4), and the economics cannot compensate for the absent demand evidence.

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| n/a | Verdict is KILL; no revision round remains. | n/a |

## Pivot candidate (KILL only)
- none — the KILL does not rest on a fix that would change customer, problem or revenue model; every listed fix leaves those three fields unchanged (diff-v2.md#Pivot check). The rubric condition for a candidate is not met. Pivots used: 0/2, but no candidate is grounded in surviving evidence.

## Ignored as struck
- economics-v2.md#C01, #C03, #C08, #C09, #C16, #C18
- forge-v2.md#C07, #C08, #C12, #C13 (dependent on struck NCH sources)
- diff-v2.md#D1 (seller prices and ratings), #D2 (order and bill reports), #D4, #D9 (URL-backed content)
- prosecution-execution-v2.md#E1, #E2, #E4
- prosecution-market-v2.md#C03
- 01-local-market.md#C22
- carried from round 1: forge-v1.md#C01, #C02, #C04, #C05, #C07, #C08; 01-local-market.md#C23, #C37, #C38, #C47; 02-signals.md#S10
