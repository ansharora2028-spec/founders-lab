---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-execution
version: 1
created: 2026-10-15T09:32:42Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I03/kill-criteria.md
- .../ideas/I03/forge-v1.md
- .../ideas/I03/economics-v1.md
- ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md and ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md

Thin-data note: Pune-specific legal, channel and competitor data is thin in every input. My own searches (4 queries) returned mostly secondary sources and did not answer the legal-practice or channel-policy questions directly. Confidence is low on those items.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | INSUFFICIENT EVIDENCE | economics-v1.md#C11, #C12, #C08; forge-v1.md#C11 | Arithmetic fits with wide margin: conservative outlay about ₹35,700 vs the ₹60,000 build cap; average 7 h/week, peak 7.5 h vs 10 h. But the criterion requires sourced quotes. Lawyer review ₹5,000, registration ₹3,000 and the 20-minute fulfilment time are all ASSUMPTION. Hindi and Marathi legal translation is not costed at all. If KE3 forces advocate sign-off or per-letter advocate routing, the cost is not in the model. Leans MET if quotes arrive and KE3 is cheap. |
| KE2 | NOT MET | economics-v1.md#C15, #C16; forge-v1.md#C12; 01-local-market.md distribution table | Time to first sale is 2.3 months in the conservative case (inside 90 days, margin 0.7 month). But the threshold also requires the plan to show orders that cover the capital spent by day 90. Conservative: 17.3 orders x ₹299 = ₹5,173 revenue against about ₹35,700 outlay, so about 119 orders would be needed. Required evidence is absent: no platform policy checked, no proof Pune PG/IT-park groups accept paid promotion, no comparable seller found. The channel assumption is forge's own unverified C12. |
| KE3 | INSUFFICIENT EVIDENCE | forge-v1.md#C11 (ASSUMPTION, "not researched"); C01 and C02 below | No written basis is provided. My search found Section 33 text and the 2025 draft amendment debate but nothing on whether drafting of agreements or personalised demand letters by non-lawyers is "practice". Forge only proposes framing the letter as a "tenant-authored template". Unresolved, not cleared. Outcome depends on a paid advocate opinion, which is not desk-researchable. |
| KE4 | NOT MET | forge-v1.md#C01 to #C14 (Narrowest wedge), economics-v1.md#C12; C03 below | Forge concedes the kit's agreement is "not a registered agreement" and "not a substitute". It does not document a leave-and-licence format, the stamp-duty and registration route, or who must register. The state portal has moved registration to tenants and landlords directly (C03), so the kit's agreement component supplies nothing the state route does not. Forge drops the agreement from the first product but still bundles it. |
| KE5 | INSUFFICIENT EVIDENCE | forge-v1 competitor table, forge-v1.md#Moat | Forge lists five substitutes but gives no verified price for NoBroker (Pune), Registrationwala or lawyer notices. Zero of the 3 required paid examples have a listed price, review count or order count. Forge states "Moat: none" and says copy is easy. My search for notice pricing (Registrationwala, Vakilsearch, LegalKart) returned no prices. Named paid differentiator is "localisation and convenience", untested (forge-v1.md#C09). Leans NOT MET. |
| KE6 | NOT MET | forge-v1 wedge, economics-v1.md#C03, #C11 | The wedge makes the founder receive room photos and meter readings by WhatsApp, and the kit handles landlord and tenant details, yet no data-handling plan (storage, consent, deletion, cost) exists in forge or economics. Economics budgets ₹0 for it. No channel split with a 70% cap was shown. Conservative economics has groups at 9.0 of 17.3 customers (52%) and ads at 2.7, all ASSUMPTION; WhatsApp and Instagram are the only channels, both Meta-owned, so a single policy change affects all of them. |

I do not comment on KM* criteria except to note that economics-v1 reports conservative unit economics as negative (blended CAC ₹1,426 vs gross profit ₹170), which is direct evidence on the contract-level viability.

## Flaws
### FE1 — FATAL
- flaw: At the stated ₹399 (conservative ₹299) price, no paid acquisition can pay back, and the only channels that could (free group posting and referrals) are unverified. The conservative case never pays back, and 3-month volume is about one third of monthly break-even before CAC.
- evidence: [C01] Economics-v1 conservative blended CAC ₹1,426 (cash-only ₹872) vs gross profit ₹170 per kit; Instagram ads ₹5,500 per customer; 17.3 customers in 3 months vs 17 per month break-even [source: economics-v1.md#Scenarios and #Calculations]. The product is one-time, so there is no repeat purchase to amortise CAC.
- fix would change customer/problem/revenue model: yes (any fix needs a different price point, repeat revenue, or a different buyer)

### FE2 — FIXABLE
- flaw: Legal exposure from selling a personalised deposit-return letter and an agreement template by a non-lawyer is unresolved, and the economics carries no cost for advocate routing or sign-off. Per-letter advocate routing would break the conservative unit cost (₹129 COGS at ₹299 price).
- evidence: [C02] The Advocates Act Section 33 bars non-enrolled persons from practising before courts or authorities, with exceptions; search found no source clarifying drafting-service status for non-lawyers, and the 2025 amendment draft is under discussion (status unchecked) [source: https://www.scconline.com/blog/post/2025/02/24/gcai-recommendations-for-draft-advocates-act-amendment-bill-public-comments-legal-news/, 2025-02-24]. Forge-v1.md#C11 states this is "not researched".
- what would fix it: a written advocate opinion or fixed-fee engagement covering the exact deliverables, with its cost added to economics; or a named Indian incumbent selling personalised letters to consumers without being a law firm, with a date. Partly desk-researchable (incumbent), the opinion is not.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: The agreement-template component has no standalone value and carries liability. Registration of leave-and-licence agreements is now done by parties on the state portal, and an unregistered template is weak evidence.
- evidence: [C03] IGR rolled out Leave and License 2.0 for Mumbai city and suburban districts from 2025-05-01, cancelled Authorised Service Providers, and parties register directly; secondary sources disagree on the stamp duty rate; Pune coverage of 2.0 is not established in the source [source: https://housing.com/news/stamp-duty-registration-laws-rentals-maharashtra]. Forge-v1 itself says the template is "not a substitute".
- what would fix it: remove the agreement from the bundle, or link tenants to the official portal with a statute-checked explainer; evidence is the Bombay Stamp Act and Maharashtra Rent Control Act text and the IGR portal page for Pune. Desk-researchable.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: The two core channels (PG, college and IT-park WhatsApp groups; Instagram) are unverified for third-party sellers. Group admins are the gatekeepers, and Meta enforcement escalates for unsolicited messaging.
- evidence: [C04] WhatsApp Business Platform policy enforcement escalates from 1 to 30-day blocks to indefinite locks and permanent removal for violations [source: https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement]. A secondary vendor source ties violations to messaging without opt-in; group posting rules were not found. 01-local-market.md lists Instagram and offline networks as "not researched".
- what would fix it: written admin acceptance from at least 5 named Pune groups with member counts, Meta ad policy text for the category, and a comparable seller with visible orders. Group acceptance needs outreach; policy text is desk-researchable.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Thin timing margin to K6 (HARD). Conservative first revenue at 2.3 months leaves 0.7 months, includes 3 weeks for admin permissions and legal review, and the June to August intake is outside the window.
- evidence: [C05] Economics-v1 conservative time to first revenue 2.3 months, "a slip of 3 weeks ... breaks it" [source: economics-v1.md#C16 and Constraint check]. Forge-v1.md#C13 puts the main intake outside the window.
- what would fix it: a dated plan with a presale to a named group before build completion, and evidence of off-cycle move-in volume in Pune (IT joiner dates). Partly desk-researchable, mostly a founder test.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: The condition report is only as strong as the operator's acknowledgement; forge assumes operators will sign and offers a possible operator-reputation dataset, which adds defamation and DPDP exposure for a seller with ₹1,00,000 and a full-time job.
- evidence: [C06] Forge-v1.md#C10 is an ASSUMPTION; forge-v1 Moat section names the operator dataset and its consent and DPDP duties (around 2027-05-13) [source: https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/]. Economics budgets nothing for this.
- what would fix it: drop the dataset from the plan, and show one Pune PG operator or consumer-forum ruling accepting tenant-dated photos as evidence. Ruling search is desk-researchable.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Economics-v1 conservative case: price ₹299, gross profit ₹169.93, blended CAC ₹1,426, 17.3 customers in 3 months, break-even 17 per month, outlay about ₹35,700 [source: economics-v1.md#Scenarios, #Calculations; file in this run]
- [C02] Advocates Act Section 33 restricts practice to enrolled advocates, subject to exceptions; no source found on non-lawyer drafting services; a draft Advocates (Amendment) Bill 2025 is under consultation, status unchecked [source: https://www.scconline.com/blog/post/2025/02/24/gcai-recommendations-for-draft-advocates-act-amendment-bill-public-comments-legal-news/, 2025-02-24]
- [C03] Maharashtra Leave and License 2.0 available for Mumbai city and suburban from 2025-05-01; service providers cancelled, parties register directly; duty rate sources disagree; unregistered agreements carry evidentiary risk (Maharashtra; Pune not confirmed) [source: https://housing.com/news/stamp-duty-registration-laws-rentals-maharashtra]
- [C04] WhatsApp Business Platform enforcement escalates from temporary blocks to permanent removal [source: https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement]
- [C05] Economics-v1 time to first revenue and K6 margin [source: economics-v1.md#C16; file in this run]
- [C06] DPDP Rules notified 2025-11-13, main duties around 2027-05-13 (national) [source: https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/]
- [C07] Search for security-deposit legal notice prices (Registrationwala, Vakilsearch, LegalKart) returned no prices; competitor pricing for KE5 remains unverified. Search result pages that appeared: https://housing.com/news/laws-related-to-security-deposit-in-india/ and https://www.sansalegal.com/post/how-to-recover-your-security-deposit-from-a-landlord-in-india-rights-and-legal-steps (neither gives notice prices)

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
