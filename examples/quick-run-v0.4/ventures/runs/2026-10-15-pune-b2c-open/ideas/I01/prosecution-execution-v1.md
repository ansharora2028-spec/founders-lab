---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-execution
version: 1
created: 2026-10-15T10:44:03Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I01/kill-criteria.md (LOCKED)
- .../ideas/I01/forge-v1.md
- .../ideas/I01/economics-v1.md
- Own web searches run 2026-10-15 (search-result text only; no page was opened by me)

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | INSUFFICIENT EVIDENCE | economics-v1.md#C18, economics-v1.md#C07, forge-v1.md#C16, forge-v1.md#C17 | Cash fits: peak outlay about Rs 11,500 against the Rs 30,000 cap. Time is shown only as a 13-week average (83 of 130 hours, about 6.4 h/week at 8 files a month), not at the criterion's 15 files a month and not per week. At 15 files the production load is 15 x 0.75 = 11.25 h/month, and I estimate about 7-8 h/week with 3 h content and 2 h group work, so it probably fits. The threshold says "every week, not an average", and no week-by-week breakdown exists. The 45-minute figure is untested. The criterion also requires evidence that no skill outside K3 is needed. forge-v1.md#C17 says the legal question was "not researched", and the economics file notes that legal drafting is not among the K3 skills. Required evidence is missing, so I cannot rule MET. |
| KE2 | NOT MET | forge-v1.md#C17, economics-v1.md#C13, FE1 | The threshold needs at least one authoritative source showing non-lawyer paid drafting and procedural guidance is permitted. None was supplied. Forge calls it an unverified assumption. Economics cites the Supreme Court holding in Bar Council of India v. A.K. Balaji that practice of law includes non-litigation drafting, and Advocates Act s.29. That source cuts against the idea. My own search found no source that permits it (see E1, E2). The comparable services forge names (Consumer Voice, IncorpX) are lawyer-issued, so they do not show a non-lawyer operating lawfully. The Rs 10,000 liability-limit part is also unsupported: the economics file budgets Rs 5,000 for an advocate review, which is not yet done. |
| KE3 | NOT MET | economics-v1.md#C09, economics-v1.md#C10, economics-v1.md Scenarios, forge-v1.md#C20 | The threshold is at least 15 paid files a month at cash CAC of Rs 150 or less. The economics conservative case gives 24 customers in 3 months, which is 8 a month, and blended cash CAC of Rs 208. The only scalable channel, paid Instagram ads, costs Rs 5,500 per customer in the conservative case, against Rs 438 contribution. Group access and group rules on promotion were not verified (forge-v1.md#C20 is an ASSUMPTION). No conversion data point from a comparable Indian service was supplied. The helpline and e-Daakhil route is documented (forge-v1.md#C07, forge-v1.md Positioning table), which is the only part of the criterion that is satisfied. |
| KE4 | INSUFFICIENT EVIDENCE | forge-v1.md#C05, forge-v1.md#C07, economics-v1.md#C01, economics-v1.md#C15, E3 | Two paid analogues exist (Consumer Voice at Rs 500 plus postage, IncorpX at Rs 1,499). Neither has sales evidence. No reviews, case counts or revenue were supplied, and both are generic lawyer-issued notices, not coaching refund files. The criterion needs a service that still sells while free routes exist. The free route is strong: NCH recovered Rs 1.56 crore for 600+ coaching students. The DPDP duties (notice, consent, retention, breach handling) were not listed or costed in forge or economics. My search confirms core duties start about 18 months after the 2025-11 notification, about May 2027, so the date is after launch, but the cost is unstated (E3). |
| KE5 | NOT MET | forge-v1.md Path to first 100 customers, forge-v1.md#C14, forge-v1.md#C18, forge-v1.md Moat over time, economics-v1.md Scenarios | First paid file within 90 days is plausible (economics: 1.5 months). The other limbs fail. There is no launch plan reaching 30 target students by day 30. The Path table sums to about 70 customers in 3 months on unsourced inputs, and economics cuts that to 24. Pune dispute volume is unknown (forge-v1.md#C14). The forge Moat section says "None initially", and the proposed log and Marathi templates are copyable. The offer does not state what the student gets if the institute still refuses. |

KM comment (execution evidence only): see FE4. A pending Maharashtra statute bears on KM3 and KM4, which the market prosecutor owns.

## Flaws
### FE1 — FATAL
- flaw: The product as specified is paid, bespoke drafting of a demand letter plus a computed claim for each customer. No source shows a non-advocate may lawfully sell this. The one relevant authority in the file (Balaji, via economics-v1.md#C13) treats non-litigation drafting as practice of law. The 2024 Delhi High Court order bars non-advocates from appearing before consumer fora on authority letters, which shows how strictly courts and bar bodies police this area. Exposure is a bar-council or court complaint, or a consumer claim if a file fails. This sits against K5 (low risk; cannot lose more than Rs 1,00,000). The economics file leaves legal exposure "UNRESOLVED" and does not cap it.
- evidence: [E1] Delhi High Court (December 2024, Anuj Kumar Chauhan v. Lieutenant Governor NCT of Delhi, W.P.(C) 17737/2024) ordered that non-advocates or agents must not be allowed to appear before consumer courts on authority letters issued by advocates. Outcome after 2025-03-18 not found. (other city: Delhi) [source: https://www.livelaw.in/amp/high-court/delhi-high-court/delhi-high-court-bars-non-advocates-from-appearing-before-consumer-courts-279456]
- evidence: [E2] Search for authority on non-advocate drafting of notices or complaints under Advocates Act ss.29 and 33 returned no source addressing it either way. One summary says s.29 reserves law practice to advocates. Secondary source. (national) [source: https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024]
- Fixing this needs a written advocate opinion or statute and court text. A desk search found none, so it is not obtainable by desk research alone. The product's lawful scope (calculator and generic template versus bespoke letter) is a design choice that has not been made. I rate it FATAL on the v1 evidence because the criterion's burden of proof is unmet and the risk lands on a HARD constraint.
- fix would change customer/problem/revenue model: no

### FE2 — FATAL
- flaw: The conservative case cannot reach the contract-relevant scale. The model gives about 8 files a month, a steady net of Rs 920 a month for about 28 founder hours a month. The idea's own volume (15 files) is not reached in the conservative case, and the only scalable channel loses money per customer (paid CAC Rs 5,500 against Rs 438 contribution). The trigger is infrequent, Pune volume is unknown (forge-v1.md#C14), and a free official route exists. The unit economics are positive, but the business at conservative volume does not return a meaningful amount on 10 hours a week.
- evidence: economics-v1.md Calculations ("Steady month at the conservative volume of 8 files a month ... Rs 920"); economics-v1.md Verdict inputs ("paid ads have a CAC of Rs 5,500 against a contribution of Rs 438, so the business cannot scale by spending money"); forge-v1.md#C14.
- This is not a breach of a HARD constraint, and the contract states no income target. I list it as FATAL because it is the direct failure of KE3 and KE5 and cannot be repaired by desk research: it needs real conversion data.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: Acquisition channel risk. Plan relies on posting in aspirant WhatsApp and Telegram groups the founder does not own, and on WhatsApp Business outreach. Meta's stated position is that businesses need prior opt-in before messaging, and repeated violations or high block rates can lead to restriction. Search found no official 2026 India policy text.
- evidence: [E4] Coverage of WhatsApp Business policy: opt-in required, caps on promotional messages, escalating restrictions for violations (national) [source: https://www.businesstoday.in/amp/technology/news/story/whatsapp-sharpens-focus-on-business-chats-with-new-controls-and-broadcast-tools-470514-2025-04-03]
- what would fix it: the current Meta Business Messaging Policy page, written rules of at least 3 named Pune MPSC/UPSC groups on paid promotion, and a design where the founder only replies to inbound messages. Desk research can supply the policy page. Group rules need membership, so only partly obtainable.
- fix would change customer/problem/revenue model: no

### FE4 — FATAL
- flaw: The strongest free substitute may become a statutory right. Maharashtra's draft Private Coaching Centers (Registration and Regulation) Act, 2026 provides pro-rata refund for students who leave midway, within about 10 days, and requires centres to publish fees and refund policies. Objections closed 2026-09-04, and no finalisation was found. If enacted, the refund claim becomes easier to enforce and institutes must publish terms, which weakens the need for a Rs 799 paid file. If not enacted, the "pro-rata refund" basis rests on advisory 2024 central guidelines that forge-v1.md#C02 says were not verified as adopted in Maharashtra. Either branch hurts the idea's durability, and neither is addressed in forge or economics.
- evidence: [E5] Draft law provisions on pro-rata refund, mandatory registration and disclosure of refund policy; draft status; objection date 2026-09-04 (Maharashtra) [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ ; https://www.freepressjournal.in/mumbai/maharashtra-proposes-mandatory-registration-fee-caps-counselling-rules-for-coaching-centres]
- Rated FATAL as an incumbent and regulatory second-order effect: the product's value rests on a gap that regulation is moving to close. Desk research can partly check status, but cannot show people would still pay.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Liability and outcome risk are not designed. The offer has no stated policy for a file that fails, no refund guarantee (KE5 requires one), and a 10% refund allowance that is an ASSUMPTION (economics-v1.md#C05). The fee is paid in advance, and the student may lose the chance to claim through a wrong calculation. Consumer-protection exposure for a deficient paid service is not analysed. Student ID, receipts and contact data are collected over WhatsApp with no retention policy.
- what would fix it: a written refund policy capping loss at the fee, disclaimers reviewed by the advocate (same review as FE1), and a retention and deletion rule for receipts. Desk research can produce a draft and a DPDP duty list (E3). A cost is needed.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Unverified timing and time inputs. Founder time per file (45 minutes) and the ability to answer enquiries within 48 hours alongside a full-time job (K9) are untested. Employer permission for side income (K9) is an ASSUMPTION in economics-v1.md Constraint check.
- what would fix it: a timed dry run of 5 files on real or sample receipts, and a check of the founder's employment contract. The dry run is the founder's own action, not desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [E1] Delhi High Court ordered in December 2024 that non-advocates or agents must not appear before consumer courts on authority letters from advocates (other city: Delhi) [source: https://www.livelaw.in/amp/high-court/delhi-high-court/delhi-high-court-bars-non-advocates-from-appearing-before-consumer-courts-279456]
- [E2] No source found on whether a non-advocate may be paid to draft a demand notice or consumer complaint. One summary says Advocates Act s.29 limits practice to advocates (national) [source: https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024]
- [E3] DPDP Rules 2025: Rules 1, 2 and 17-21 effective on publication in November 2025; core data fiduciary duties (Rule 3 notice and others) apply 18 months after publication, about May 2027. Search returned nothing on any small-business exemption (national) [source: https://www.taxmann.com/post/blog/analysis-indias-dpdp-act-and-rules/ ; https://www.medianama.com/2025/11/223-dpdp-rules-2025-data-fiduciary-obligations/]
- [E4] WhatsApp Business: opt-in expected before promotional messages, caps and escalating restrictions on violations (national) [source: https://www.businesstoday.in/amp/technology/news/story/whatsapp-sharpens-focus-on-business-chats-with-new-controls-and-broadcast-tools-470514-2025-04-03]
- [E5] Maharashtra draft coaching law, August 2026: pro-rata refund on leaving midway, refund within about 10 days, mandatory registration, online disclosure of fees and refund policy, objections to 2026-09-04, no finalisation found (Maharashtra) [source: https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ ; https://news.careers360.com/maharashtra-proposes-law-regulate-coaching-centres-cap-class-hours-seeks-objections-till-september-4-fee-refund-rules-counselling]
- Limit: all of the above rests on search-result text. No page was opened. Confidence is lowered accordingly.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a | n/a | round 1 |
