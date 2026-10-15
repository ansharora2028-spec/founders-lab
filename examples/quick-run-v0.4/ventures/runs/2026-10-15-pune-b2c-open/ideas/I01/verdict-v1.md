---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: judge
version: 1
created: 2026-10-15T10:47:33Z
---

## Hash check
- expected (run-log): 408e341c3ad727bab4fc63f71770f5e4267f5de6079ecad526adff66d0d95af9
- actual: 408e341c3ad727bab4fc63f71770f5e4267f5de6079ecad526adff66d0d95af9
- result: MATCH

## Verdict
- verdict: REVISE
- round: 1
- confidence: 4

## Criteria (after audit)
Rule used where the prosecutors differ: the lower status, because no surviving evidence clearly supports the higher one. The auditor struck 22 claims as UNREACHABLE, all from a fetch-tool failure, not a source failure. The Judge treats them as struck all the same.

| criterion | market/exec status | surviving evidence | counts as |
|---|---|---|---|
| KM1 | NOT MET (market prosecutor) | Price anchors (forge-v1.md#C05, economics-v1.md#C01) are struck. No named seller with a customer count or review count survives. The Akosha 2011 listing is outside the 24-month window. | NOT MET. FIXABLE by desk research (seller listings, review counts) |
| KM2 | INSUFFICIENT EVIDENCE | National NCH figures (forge-v1.md#C08, economics-v1.md#C14) are struck. No Maharashtra or Pune count exists. | NOT MET for PASS. FIXABLE: state-level data is partly desk-researchable (an RTI request would be too slow) |
| KM3 | INSUFFICIENT EVIDENCE | The documented free-resource search was never run. The NCH recovery figure (forge-v1.md#C07) is struck. | NOT MET for PASS. FIXABLE by desk research |
| KM4 | NOT MET | The MoE guideline claim (forge-v1.md#C02) is struck. prosecution-market-v1.md#C03 (advisory status; Maharashtra bill still a draft) is not struck but was not individually checked. No Maharashtra adoption of the guidelines is shown. | NOT MET. FIXABLE by desk research (dated orders, Maharashtra bill status) |
| KM5 | INSUFFICIENT EVIDENCE | No dated complaint posts. Channel sizes are unverified third-party figures (prosecution-market-v1.md#C07). | NOT MET for PASS. FIXABLE by desk research |
| KE1 | INSUFFICIENT EVIDENCE | The economics arithmetic is VERIFIED (83 of 130 hours; peak outlay Rs 11,500). The 45 minutes per file is an ASSUMPTION. There is no per-week breakdown at 15 files a month and no skills evidence. | NOT MET for PASS. FIXABLE: the breakdown is on paper; the timed dry run is the founder's own task |
| KE2 | NOT MET | No authoritative source permitting paid non-lawyer drafting was supplied (forge-v1.md#C17 is an ASSUMPTION). The adverse authority (economics-v1.md#C13, prosecution-execution-v1.md#E1, #E2) is struck. The unmet burden of proof stands without it. | NOT MET. FIXABLE: statute text plus a reduced product scope (calculator and generic template) plus a refund policy; the advocate review costs about Rs 5,000 |
| KE3 | NOT MET | Verified arithmetic from the conservative column: about 8 files a month, blended cash CAC Rs 208, against the threshold of 15 files and Rs 150. The inputs are ASSUMPTIONs (economics-v1.md#C09, #C10, #C11). | NOT MET. FIXABLE by redesign and desk evidence (a conversion data point from a comparable Indian service, current WhatsApp Business policy, group rules) |
| KE4 | INSUFFICIENT EVIDENCE | The paid analogues' prices are struck. No sales evidence for any. The DPDP duties are not costed (the 01#C37 date is struck). | NOT MET for PASS. FIXABLE by desk research |
| KE5 | NOT MET | forge-v1.md Moat ("None initially"). There is no day-30 launch plan and no stated outcome if the institute refuses. | NOT MET. FIXABLE by design: a launch plan, refund-guarantee terms, a defensible asset |

## Decisive reasons
1. PASS is unavailable. All ten locked criteria count as NOT MET for PASS, and no demand evidence survives the audit. Every demand item (fees, notice prices, NCH recoveries) rests on a struck URL, and both prosecutors report no seller shown with paying customers. — audit-v1.md#Summary; forge-v1.md#C22; prosecution-market-v1.md#FM1
2. KILL is not warranted. No FATAL flaw survives.
   - FE1 rests only on struck E1, E2 and economics-v1.md#C13. It also names no fix that changes customer, problem or revenue model. Treated as FIXABLE: the legal scope is a design choice.
   - FE4 rests only on struck E5. Discarded as FATAL. Maharashtra draft-bill status is a FIXABLE item under KM4.
   - FE2 does not break a HARD constraint. The contract states no income target. The economics are positive per unit and the arithmetic is verified, so FE2 does not meet the FATAL definition. Treated as FIXABLE, with a caveat in reason 4. — prosecution-execution-v1.md#FE1, #FE2, #FE4; audit-v1.md#Struck claims
3. Conservative economics are positive and inside every HARD cap. Per-file contribution is Rs 438; peak outlay is about Rs 11,500 against Rs 1,00,000; hours are 6.4 a week; first revenue comes at about 1.5 months. — audit-v1.md#Checked claims (arithmetic VERIFIED); economics-v1.md#Constraint check
4. The business size at the conservative case is about Rs 920 net a month. A Rs 10,000 month needs about 29 files a month, and paid ads fail at a CAC of Rs 5,500. The CPC input is struck and the conversion input is an ASSUMPTION, so this stays a warning, not a kill. If desk research cannot show volume and an acquisition route, round 2 should end in KILL. — economics-v1.md#Calculations; prosecution-execution-v1.md#FE2
5. REVISE conditions are met: round 1; no surviving FATAL flaw; no listed fix changes customer, problem or revenue model (a narrowed product scope keeps the same customer, problem and one-time fee). A real conversion test is not desk research and cannot be required in round 2. Confidence is low because 22 strikes come from tool failure, not from source failure.

## Demand evidence
- none surviving

## Conservative economics
- fits contract: yes on cash and hours (K1, K2, K6, K7, K8) — economics-v1.md#Calculations, #Constraint check. K5 legal exposure is unresolved and K9 employer permission is an ASSUMPTION. Per-file economics are positive; scale is not demonstrated (decisive reason 4).

## Fixable flaws (REVISE only)
| flaw id | what evidence would fix it | desk-researchable |
|---|---|---|
| FM1 / KM1 / KE4 | Opened, dated pages (within 24 months) for at least 3 Indian sellers charging individuals Rs 500 or more for refund, legal-notice or consumer-complaint drafting, at least 1 in Maharashtra. At least 2 of them need 10 or more customer reviews or a stated case count. Also name any shut-down Indian consumer-grievance startup with its cause of death. Also name at least one paid comparable service that still sells while free NCH 1915 exists. | yes (listings, review counts); the evidence may not exist |
| FM2 / KM4 | At least 3 consumer commission or court orders from the last 36 months ordering a coaching refund despite a non-refundable clause, at least 1 from Maharashtra. A Maharashtra government source stating whether the MoE guidelines of 2024-01-16 or the Private Coaching Centers bill apply, with its current status. | yes |
| FM3 / KM2 | A Maharashtra or Pune count of at least 2,000 education or coaching grievances a year, or a figure of at least 50,000 paying Pune coaching enrolments a year, from a government, industry or credible press source. | partly (published dashboards or press; an RTI request is too slow) |
| FM4 / KM3 | A documented search, with URLs, of free Pune-accessible resources offering both a pro-rata calculation and a ready letter. If 2 or more exist, evidence that buyers still pay for comparable kits. An itemised table of what the Rs 799 file does that NCH and free guides do not. | yes |
| FM5, FE1 / KE2 | An authoritative source (Advocates Act text, Bar Council or court position, or a comparable non-lawyer service operating in India) on paid document preparation and procedural guidance by a non-advocate. The product scope must be redefined to what that source permits (for example a calculator plus generic template, with no bespoke letter). A refund-policy design capping loss at the Rs 799 fee, costing Rs 10,000 or less. | partly: statute and case text yes; a written advocate opinion (about Rs 5,000) is not |
| FM6 | Named Indian consumer-complaint or legal-document startups with revenue or shutdown evidence and cause of death. | yes |
| KM5 | URLs and follower counts for at least 3 Pune-based or Marathi MPSC/UPSC communities (5,000 or more combined), plus at least 10 dated public posts in the last 12 months complaining about coaching fees, refunds or batch changes. | yes |
| FE2, FE3 / KE3 | An acquisition route reaching at least 15 paid files a month at cash CAC of Rs 150 or less. Sourced inputs: a conversion or reply-rate data point from a comparable Indian service, a current CPC figure from an opened page, the current Meta Business Messaging policy page, and a design in which the founder only replies to inbound messages. | partly: policy and benchmark yes; group rules and a real conversion rate need an experiment |
| FE5 / KE5 | A dated launch plan with numbers reaching the first 30 target students by day 30. Written refund-guarantee terms stating what the student gets if the institute refuses. One defensible asset buildable inside the budget. A retention and deletion rule for receipts. | yes (as written design); the moat itself is unproven |
| FE6 / KE1 | A week-by-week hours table at 15 files a month, including marketing, showing 10 hours or fewer in every week. The 45-minute-per-file input needs a timed dry run of 5 sample files. K9 employer permission needs a check of the founder's employment contract. | partly: the table yes; the dry run and the contract check are the founder's own actions, not desk research |

## Pivot candidate (KILL only)
- none — verdict is REVISE, not KILL.

## Ignored as struck
- economics-v1.md#C01, #C03, #C08, #C13, #C14, #C15, #C17
- forge-v1.md#C01, #C02, #C04, #C05, #C07, #C08 (and #C12, #C13, which depend on #C07 and #C08)
- 01-local-market.md#C22, #C23, #C37, #C38, #C47
- 02-signals.md#S10
- prosecution-execution-v1.md#E1, #E2, #E5
