---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-execution
version: 2
created: 2026-10-15T10:52:55Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I01/kill-criteria.md (LOCKED)
- .../ideas/I01/diff-v2.md
- .../ideas/I01/economics-v2.md
- .../ideas/I01/prosecution-execution-v1.md (own)
- Two web searches run 2026-10-15 (search-result text only; no page opened by me). forge-v2.md not read.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | diff-v2.md D11, economics-v2.md#C13, economics-v2.md#C14, economics-v2.md Constraint check K2 | Cash fits: Rs 14,500 to first revenue, Rs 19,500 peak, against the Rs 30,000 cap. Time fails the "every week, not an average" wording. D11 itself states heavier weeks reach about 10.5 hours, and economics-v2 says a 5th file in a week takes the week to 11 hours and "breaks K2 unless content hours are cut". The 4-files-a-week cap is a design intent with no mechanism or evidence. The dry run (5 timed files) is not done; D11 carries NONE as evidence. Fixed hours of 6.0 a week are ASSUMPTION (economics-v2.md#C14). The legal-skill limb is not satisfied (see KE2). |
| KE2 | NOT MET | diff-v2.md D5, D6; economics-v2.md#C07, economics-v2.md#C08, E1, E2 | The threshold needs an authoritative source that non-lawyer paid document preparation and procedural guidance is permitted. D6 supplies none: the Balaji summary points toward a case-by-case "pith and substance" test (against the idea), and the only supportive item is one DIY guide that economics-v2 itself calls non-authoritative. D6 confirms no comparable non-lawyer service operates. The advocate opinion (Rs 5,000) is budgeted, not obtained. The scope narrowing in D5 (calculator plus generic fill-in letter, no bespoke drafting, no filing) is a sensible design but is unproven to be outside the Advocates Act. My own search again found no source on whether a paid non-advocate may draft notices (E2). The liability-cap limb (refund within 7 days, loss capped at Rs 799, setup under Rs 10,000) is a design only, with ASSUMPTION costs. |
| KE3 | NOT MET | diff-v2.md D9, economics-v2.md#C09-C11, economics-v2.md Scenarios and Calculations | D9 admits that Rs 150 CAC and 15 paid files a month are "not shown". Paid-ad CAC is Rs 750 on the forge's own inputs and Rs 5,500 in the conservative case, against a conservative contribution of Rs 413. Conservative volume is 24 files in 3 months (8 a month). Group access and rules on paid promotion are unverified (D8: no Pune group found). The WhatsApp policy rests on a vendor summary and Meta's page was not opened. The NCH and e-Daakhil route is documented (economics-v2.md#C16, D2), which is the only limb met. |
| KE4 | INSUFFICIENT EVIDENCE | diff-v2.md D1, D4, D10, economics-v2.md#C01, economics-v2.md#C16 | The comparable paid services (IncorpX Rs 1,499, Ebizfiling from Rs 4,999, RegisterKaro, Consumer Voice Rs 500) are lawyer-issued generic notices, and D1 states that none shows 10+ reviews or a case count and that no evidence exists of buyers paying while NCH 1915 is free. The free route is strong (Rs 1.56 crore recovered for 600+ students). The DPDP limb is not answered: D10 gives only a 30-day receipt deletion rule; no duty list, cost or binding date is shown. The criterion is not shown met, and an outright failure is not proven. |
| KE5 | NOT MET | diff-v2.md D10, D3, D8, economics-v2.md#C11, economics-v2.md#C16 | First paid file within 90 days is plausible (economics: 2.0 months conservative). The day-30 plan (30 inbound students, 3-8 paid files) has no source. Pune dispute volume is unknown (D3 not fixed). The moat is an outcome log with "no external evidence" (D10). The refusal-case offer is now stated (full refund in 7 days if the student cannot use the file; steps kept), which satisfies that single limb on paper. Defensible asset and reachability of 15 files a month are not shown. |

KM comment (execution evidence only): none beyond FE4 below. KM3 and KM4 are owned by the market prosecutor.

## Flaws
### FE1 — FATAL
- flaw: Legal permission to sell the product is still unestablished. D5 narrows the scope (calculator, generic template, no bespoke letter, no filing, no merits advice). That lowers the exposure but no authority was found showing it is lawful for a non-advocate to charge for it. The one case cited is reported to apply a case-by-case test, and the exposure (bar-council complaint, consumer claim for a failed file) sits against K5. The economics file leaves legal exposure "UNRESOLVED until the advocate opinion exists" (economics-v2.md Constraint check K5).
- evidence: [E1] No source was found on whether a non-advocate may be paid to draft a demand notice or consumer complaint; results cover only appearance of agents in consumer fora, where Consumer Commission Regulations 2014 permit authorised agents and a Delhi High Court 2024 order restricts non-advocates on advocate authority letters (national; other city: Delhi) [source: https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024]
- evidence: [E2] Search returned the 2011 Supreme Court C. Venkatachalam v. Ajitkumar C. Shah holding that authorised agents appearing in consumer fora is not inconsistent with s.33 Advocates Act; it addresses appearance, not paid drafting (national) [source: https://www.legalauthority.in/judgement/c-venkatachalam-vs-ajitkumar-c-shah-7906]
- Not obtainable by desk research. It needs a written advocate opinion (budgeted Rs 5,000, not obtained). Status at v1 was FATAL; the diff adds no authority. FATAL is kept.
- fix would change customer/problem/revenue model: no

### FE2 — FATAL
- flaw: The business does not reach a meaningful size under the contract. Economics-v2 conservative gives a steady net of about Rs 720 a month at 8 files, and a ceiling of Rs 4,437 a month at the K2 cap of 17 files. The only scalable channel loses money per customer. There is no Pune volume data and a free official route exists. Per-unit economics are positive; the business size is not. No contract clause sets an income target, so this is not a HARD breach, but it makes KE3 and KE5 unmet and cannot be repaired by desk research.
- evidence: economics-v2.md Calculations ("Steady month at 8 files: ... Rs 720"; "no scenario reaches Rs 10,000 a month at Rs 500"); economics-v2.md Verdict inputs; diff-v2.md D3, D9.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: Acquisition channel dependence (WhatsApp opt-in rules, aspirant groups the founder does not own) is only partly addressed by an inbound-only design (D9).
- evidence: [E3] D9 cites a vendor summary of WhatsApp policy; Meta's page not opened. No group rules gathered (D8).
- what would fix it: Meta's Business Messaging Policy page text, and written paid-promotion rules of at least 3 named Pune MPSC/UPSC groups. The policy page is obtainable by desk research; group rules need membership.
- fix would change customer/problem/revenue model: no

### FE4 — FATAL
- flaw: The free substitute is moving toward a statutory right in Maharashtra. The draft Private Coaching Centers (Registration and Regulation) Act, 2026 provides for refund of the unused fee portion for students who leave and public disclosure of refund policies. Diff-v2 D2 confirms the draft is not passed. If enacted, the refund claim becomes easier and institutes must publish terms, weakening the need for a Rs 799 file. If not enacted, the refund basis rests on advisory central guidelines. Neither branch is answered in the diff.
- evidence: [E4] Draft published with objections due 2026-09-04; no cabinet approval or final notified version found in my 2026-10-15 search (Maharashtra) [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ ; https://news.careers360.com/maharashtra-proposes-law-regulate-coaching-centres-cap-class-hours-seeks-objections-till-september-4-fee-refund-rules-counselling]
- Desk research can track the status but cannot show people would still pay. FATAL is kept as a second-order regulatory effect.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Liability design is now written (7-day full refund, loss capped at Rs 799, Rs 8,000 reserve, 30-day receipt deletion) but every cost is ASSUMPTION and the DPDP duty list and cost are absent. The conservative refund rate of 15% is itself an ASSUMPTION.
- what would fix it: the advocate-reviewed disclaimer and refund terms, plus a DPDP duty list for a sole proprietor with cost. Desk research can produce the DPDP list; the disclaimer review needs the advocate.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Time inputs are untested. Founder time of 30-60 minutes per file and 6.0 fixed hours a week are ASSUMPTION; the timed dry run and the employment-contract check (K9) are not done (D11).
- what would fix it: a timed dry run of 5 files and a read of the employment contract. Both are the founder's own actions, not desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [E1] Delhi High Court (December 2024) restricted non-advocates appearing before consumer fora on authority letters; Consumer Commission Regulations 2014 permit authorised agents (national; other city: Delhi) [source: https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024]
- [E2] Supreme Court (2011) held that agents appearing in consumer fora is not inconsistent with s.33 Advocates Act; says nothing on paid drafting (national) [source: https://www.legalauthority.in/judgement/c-venkatachalam-vs-ajitkumar-c-shah-7906]
- [E3] WhatsApp policy evidence in D9 is a vendor summary only (national) [source: https://www.cm.com/blog/whatsapp-updates-opt-in-and-quality-rating-policy/, as cited in diff-v2.md D9, not opened]
- [E4] Maharashtra draft coaching law, status draft, objections to 2026-09-04, no finalisation found (Maharashtra) [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/]
- Limit: all external evidence is search-result text; no page was opened by me.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | no | Row states "Not fixed to the stated bar". Sellers are lawyer-issued; no 10+ review counts; no evidence of buyers paying while NCH is free. Market prosecutor owns KM1. For KE4 it shows analogues exist but not that they sell. |
| D2 | no | Enforceability is KM4 (market). Execution relevance: no Maharashtra order on a non-refundable clause, and the draft Act is unpassed, which keeps FE4 open. |
| D3 | no | NONE evidence; row says not fixed. |
| D4 | no | Row says free guides were not opened, so absence of a free calculator and letter is not established. |
| D5 | no | Scope narrowing is a design change and the URLs (a tax-law archive page and a DIY guide) do not show a non-advocate may lawfully charge for the narrowed product. Reduces exposure; does not satisfy KE2. |
| D6 | no | The authority found points to a case-by-case test and a single non-authoritative DIY guide. No comparable non-lawyer service confirmed. The refund-cap design is useful but costs are ASSUMPTION and the advocate opinion is not obtained. |
| D7 | no | NONE evidence; no cause of death found. |
| D8 | no | NONE evidence; no Pune community or complaint posts found. |
| D9 | no | CPC sourced, but the row itself shows Rs 750 CAC against Rs 150 threshold and no volume of 15 files. WhatsApp policy from a vendor summary only. |
| D10 | no | NONE evidence (rule 4). The guarantee wording is accepted as stated design for the refusal limb of KE5 only; it is not a fix because it has no evidence URL. |
| D11 | no | NONE evidence; the 10.5-hour week stated in the row breaks the every-week threshold; dry run and contract check not done. |
