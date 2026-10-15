---
run_id: 2026-10-15-check-english-clubs-pune
idea_id: I01
agent: judge
version: 1
created: 2026-10-15T10:35:34Z
---

## Hash check
- expected (run-log): 556239e2f7317b60e74d720a47f503754e16503f1001f4a7b9d15a440da45680
- actual: 556239e2f7317b60e74d720a47f503754e16503f1001f4a7b9d15a440da45680
- result: MATCH

## Verdict
- verdict: KILL
- round: 1
- confidence: 6

## Criteria (after audit)
Where the prosecutors overlap (KM4/KE4 overlap on Toastmasters only), the lower status is used. Where only one prosecutor assessed a criterion, that status stands unless struck evidence was its only support.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | NOT MET | 01-local-market.md#C19 (no paid Pune café English club found); prosecution-market-v1.md FM1. No operator with a checkable sign of paying customers is cited anywhere. Existing-spend claims (01#C01-C03, 02#S01-S02) are struck. | NOT MET |
| KM2 | NOT MET | The only student-spend figure (ASSOCHAM 2011) is struck. SpeakX (₹299, below the ₹300 floor) is struck. No second example exists. | NOT MET |
| KM3 | NOT MET | No operator of paid live-human English practice at or below ₹1,500/month with 12+ months of operation found. Pune Toastmasters dues remain unstated (the international dues claim is struck). | NOT MET |
| KM4 | INSUFFICIENT EVIDENCE | 01-local-market.md#C09 is an ASSUMPTION (no failure data). The 5-query log was not delivered. Absence of evidence only. | NOT MET for PASS; FIXABLE (desk research) |
| KM5 | INSUFFICIENT EVIDENCE | The SPPU enrolment claim (prosecution-market-v1.md#C05) is struck. No sourced Pune student count and no sourced English-confidence share. | NOT MET for PASS; FIXABLE (desk research) |
| KE1 | NOT MET | economics-v1.md Calculations "Founder hours" and Constraint check K2 (12 h/week at the 14-member break-even, against HARD 10 h). Arithmetic VERIFIED in audit-v1.md. The hours are ASSUMPTIONs, stated as such. | NOT MET |
| KE2 | INSUFFICIENT EVIDENCE | 0 of 3 required venues evidenced (01-local-market.md#C23: not researched). | NOT MET for PASS; partly desk-fixable |
| KE3 | INSUFFICIENT EVIDENCE | Only vendor-blog answers (struck in part); no primary source on minors, liability or insurance. | NOT MET for PASS; partly desk-fixable |
| KE4 | INSUFFICIENT EVIDENCE | Toastmasters dues (struck); no prices for 3 Pune institutes; no count of college clubs. | NOT MET for PASS; desk-fixable |
| KE5 | NOT MET | forge-v1.md Moat over time ("None yet", no named barrier against facilitator or member copying). The facilitator-cost half rests on struck rates (economics-v1.md#C09, Superprof ₹702) and is given no weight. | NOT MET |

## Decisive reasons
1. The conservative economics break a HARD constraint. The break-even volume of 14 paying members needs two groups and 12 h/week, against K2 = 10 h (HARD, no stretch). One group fits at 9 h/week but is loss-making (₹1,736/month gross profit against ₹3,000 fixed cost). Arithmetic VERIFIED. The inputs are ASSUMPTIONs, which lowers confidence but does not remove the result. — economics-v1.md Calculations "Founder hours (K2)", economics-v1.md Constraint check K2, 00-contract.md#K2, audit-v1.md (FE1 row), prosecution-execution-v1.md FE1
2. The conservative unit economics are not positive. LTV/CAC is 0.98, payback of 2.56 months exceeds the 2.5-month paying life, and steady-state net is about -₹86/month with unpaid founder time. The arithmetic is verified. It depends on unsourced ASSUMPTIONs (venue fee, churn, funnel, CPC). The economics file says it could flip with a ₹0 venue fee or lower churn, and no evidence supports either. Rule 3 requires positive conservative economics. — economics-v1.md Verdict inputs, audit-v1.md (Calculations row VERIFIED)
3. No demand evidence survived the audit, so PASS is unavailable. Every demand claim (institute spend, SpeakX subscribers) was struck as UNREACHABLE because the auditor's fetch tool failed. The cause is the tool, not the sources. Rule 8 still applies. — audit-v1.md Summary
4. KM1 is NOT MET with no desk-research fix in sight. Two scouts, the forge and the market prosecutor found zero Pune or Indian operators of paid recurring low-price in-person English conversation clubs with checkable customers. The forge says the evidence cannot separate "open gap" from "no demand". The realistic fix is a paid pre-sale test, which is an experiment and not desk research. The rubric makes this unfixable for REVISE purposes. KM2 and KM3 are also NOT MET. — 01-local-market.md#C19, forge-v1.md#C21, prosecution-market-v1.md FM1
5. KE5 is NOT MET because there is no named barrier to copying. The forge states the moat as "None yet". — forge-v1.md Moat over time, prosecution-execution-v1.md FE7

Treatment of FATAL labels:
- FM2 and FE2 (facilitator unaffordable): the rate inputs were struck (economics-v1.md#C09, the Superprof ₹702). The arithmetic is verified, but with no surviving rate their FATAL basis is gone. I treat them as FIXABLE or discard them. They are not a decisive reason.
- FE1 (hours): it survives as arithmetic and is used under reason 1 as a HARD-constraint break, not as a FATAL flaw. A single larger group is a possible fix that changes no customer, problem or revenue-model field, so it does not meet the FATAL definition. The KILL stands on the HARD-constraint rule.

## Demand evidence
- none surviving

## Conservative economics
- fits contract: no — K2 BREAKS (economics-v1.md Constraint check); unit economics not positive (LTV/CAC 0.98, economics-v1.md Verdict inputs). K1, K5, K6 and K7 fit.

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| n/a (verdict is KILL) | n/a | n/a |

## Pivot candidate (KILL only)
- none — the decisive reasons are a HARD-constraint break on hours, non-positive conservative economics, no surviving demand evidence and an unmet KM1. None of these is shown to be fixable only by changing customer, problem or revenue model. The one price-change fix (about ₹1,000 or more per month, prosecution-execution-v1.md FE2) rests on struck facilitator rates and has no surviving grounding evidence. The candidate conditions are not met.

## Ignored as struck
- economics-v1.md#C02, #C03, #C09, #C10, #C13
- prosecution-market-v1.md#C03, #C04, #C05, #C08, and FM2's reliance on the Superprof rate
- prosecution-execution-v1.md#E01
- 01-local-market.md#C01, #C02, #C03, #C04, #C11, #C16, #C27
- 02-signals.md#S01, #S02
- forge-v1.md#C01, #C02, #C03, #C09, #C11, #C12, #C13, and the unsourced "university's own page gives 629" sub-claim of #C09

Confidence note: confidence is held at 6. The KILL rests on verified arithmetic over ASSUMPTION inputs. Local coverage is 3/10 (run-log). The auditor struck 19 claims because of a tool failure, not source failure, which means the demand-evidence gap may partly be a verification artefact. The absence of any found operator for KM1 is independent of that failure.
