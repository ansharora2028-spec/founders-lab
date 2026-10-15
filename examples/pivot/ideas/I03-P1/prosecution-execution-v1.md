---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: prosecutor-execution
version: 1
created: 2026-10-15T18:00:00Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/01-local-market.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/02-signals.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03-P1/kill-criteria.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03-P1/forge-v1.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03-P1/economics-v1.md
- ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md
- ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C06, economics-v1.md#C15, economics-v1.md Calculations step 10, forge-v1.md#C15 | Capital limb passes (₹10,500 to first revenue, ₹24,781 max spend, under the ₹60,000 conservative ceiling). Hours limb fails the stated threshold: the conservative case uses 2.0 h per completed sale against the KE1 limit of 1.5 h. Total 120 h / 13 weeks = 9.2 h/week leaves 0.8 h/week of slack against K2 (HARD, no stretch). The conservative 3-month mix yields about 6.7 sales/month against a stated break-even of 8.5 (economics-v1.md Calculations step 7), so the hours budget does not reach break-even volume. |
| KE2 | NOT MET | economics-v1.md#C03, economics-v1.md#C14, forge-v1.md#C14 | Timing passes thinly (2.5 months, i.e. about 2026-12-30, against 2027-01-15). The collection-rate limb fails: the conservative case uses 40% against the required 60% or more. No enforcement mechanism is described; forge-v1 states the model "relies on seller goodwill and on pre-commitment at listing" and that sellers will pay on a sale they can complete off-platform is an unevidenced assumption. The criterion names escrow or platform-collected payment as the type of mechanism needed; the plan uses pay-after-handover. |
| KE3 | NOT MET | forge-v1.md Positioning table, forge-v1.md#C03, forge-v1.md#C06, forge-v1.md Moat section | Three incumbents are named (OLX, Quikr, Facebook Marketplace), but Quikr and Facebook Marketplace carry no URL, no price and no terms in forge-v1 ("not opened; no URL"). The OLX figure is a search-summary figure from a third-party press site. No named difference is evidenced as worth 10% against ₹0; forge-v1 Moat section says "None yet" and that groups are copyable. No stated response to a free competing WhatsApp group in the same society. Rental-company resale channels and the informal landlord/broker route named in KE3 are not addressed. |
| KE4 | INSUFFICIENT EVIDENCE | forge-v1.md#C19, economics-v1.md#C13, 01-local-market.md#C18, 01-local-market.md#C19 | Neither forge nor economics contains the checked list (a)-(e). GST is "not modelled", the Consumer Protection (E-Commerce) Rules, DPDP, and used-electrical-appliance liability are not covered at all, and the S&E item is an unverified ₹500 allowance from commercial sites. Counts as unsatisfied for the lock, but the gap is closable by desk research (see FE3). My own partial research is under Evidence. |
| KE5 | INSUFFICIENT EVIDENCE | forge-v1.md Path table, forge-v1.md#C16, forge-v1.md#C18, economics-v1.md#C10, 02-signals.md#S01 | Four seller channels are named, but every reach and conversion figure is ASSUMPTION; no cost or reach is sourced. No WhatsApp group, Community or Business policy page is cited, and no ban or terms-change cost is stated. No back-up channel with a cost is given. The messaging-cost limb (at most 10% of monthly commission) is met only because manual posting costs ₹0 (forge-v1 Path section, ASSUMPTION). Group admin permission (forge-v1.md#C18) is untested. |

Comment on market criteria with direct execution evidence only:
- KM2: forge-v1.md#C10 computes ₹200-400 commission on ₹2,000-4,000 items and economics-v1.md uses a conservative ₹300 commission, which sits exactly at the KM2 threshold. After a 40% collection rate the realised figure is ₹120 per completed sale (economics-v1.md Scenarios). Market prosecutor owns the verdict.
- KM3: forge-v1.md#C14 admits no evidence that sellers pay a commission on a sale they can complete off-platform. Market prosecutor owns the verdict.

## Flaws
### FE1 — FATAL
- flaw: Conservative unit economics are negative and the structure cannot fix itself. Realised revenue per completed sale is ₹120 and contribution ₹117, against blended cash CAC of ₹1,064 (₹262 even with no paid Instagram). The seller is a one-time user (forge-v1 persona), so payback is never reached. Time-loaded margin is -152%. Three-month conservative net is -₹22,438 (economics-v1.md Calculations step 8). At the conservative 6.7 completed sales/month the revenue is about ₹785/month for about 40 hours/month of founder time, under ₹20 per hour. Even the economics-modeler's base case caps operator throughput at 6-7 sales/week at 10 h/week (forge-v1.md#C15), so the labour ceiling is roughly 25-30 sales/month, that is a few thousand to about ₹7,000/month before CAC.
- evidence: [C01] Conservative contribution ₹117/sale vs blended cash CAC ₹1,064 and 9.1 sales needed per acquired seller [source: economics-v1.md Calculations steps 5-6; arithmetic reviewed and consistent]
- what would fix it (FIXABLE only): n/a
- fix would change customer/problem/revenue model: yes (a fix needs a different price, repeat-use customer or channel cost structure)

### FE2 — FATAL
- flaw: Commission leakage is built into the model. Listing is free, the buyer and seller are introduced by the operator, and the 10% is requested by UPI link after handover, so either side can complete off-platform. No escrow, no platform-held payment, no lock-in. Forge itself assumes 30-60% leakage with no data and calls seller willingness to pay "the largest load-bearing assumption" (forge-v1.md#C14). KE2 requires 60% collection in the conservative case; the model's own conservative input is 40%. Enforcement by taking payment from the buyer and releasing the net amount to the seller changes the revenue model (payment intermediary) and brings in RBI payment aggregator exposure.
- evidence: [C02] Economics uses 40% paying share, conservative; forge-v1 uses 30-60% leakage [source: economics-v1.md#C03; forge-v1.md#C14]
- evidence: [C03] RBI payment aggregator norms exist and the 01 research notes an RBI breather only for small-merchant UPI [source: 01-local-market.md#C20; https://www.business-standard.com/topic/upi]; whether a founder-held escrow of buyer money is a payment aggregator activity is not established here. [ASSUMPTION: flagged as a risk to verify, not a finding]
- what would fix it (FIXABLE only): n/a
- fix would change customer/problem/revenue model: yes (revenue model: upfront fee or escrow-collected commission)

### FE3 — FIXABLE
- flaw: Legal and tax position of a commission-earning marketplace is unresearched, so the cost and licence ceiling in KE4 cannot be confirmed. Specific open items: (a) whether the founder is an "e-commerce entity" under the Consumer Protection (E-Commerce) Rules 2020, which cover any person who owns, operates or manages a digital or electronic platform and, per the summaries seen, require a grievance mechanism and officer with 48-hour acknowledgement and one-month resolution; a Google Form plus WhatsApp groups may or may not be a "platform"; (b) GST: Section 24 lists e-commerce operators and agents supplying on behalf of taxable persons as compulsory registrants regardless of threshold; secondary sources say service suppliers otherwise use the ₹20 lakh threshold; sellers here are non-taxable individuals, so the agent limb may not apply, but this is not settled; (c) S&E intimation status (sources conflict, 01#C18); (d) DPDP duties for holding phone numbers and photos (01#C19; 02#S08); (e) liability for a faulty used appliance (fire, electric shock) when the operator matches and takes a fee.
- evidence: [C04] The Rules define an e-commerce entity as any person who owns, operates or manages a digital or electronic facility or platform, and require a grievance officer [source: https://www.lkslaw.com/insights/news/e-commerce-consumer-protection-e-commerce-rules-2020-notified; seen as a search-result summary only, page not opened]
- evidence: [C05] Section 24 CGST Act compulsory registration categories include agents and e-commerce operators; service-supplier threshold ₹20 lakh per secondary sources [source: https://www.knowyourgst.com/gstlaw/cgst-act/24-compulsory-registration-in-certain-cases-24/; https://learn.quicko.com/?p=1370; search summaries only, not primary CBIC text]
- evidence: [C06] A proposed 2021 amendment would make DPIIT registration of e-commerce entities mandatory; the search results did not confirm notification [source: https://www.bananaip.com/?p=77645; unverified]
- what would fix it (FIXABLE only): primary-source checklist (CBIC/GST portal, Ministry of Consumer Affairs, Maharashtra Labour Department, MeitY) covering items (a)-(e) with dates, an accountant fee quote, and a ToS/liability mitigation with insurance cost, total at most ₹15,000 in year one. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: Channel dependency and supply-side cold start. The plan joins about 60 society and tenant WhatsApp groups to post third-party listings and take a commission. Group admins control access; unsolicited commercial posting by an outsider is likely to be removed or blocked, and a ban of the operator's number removes the product. Every reach and conversion figure is ASSUMPTION. Group size limits seen are 1,024 per group and 5,000 per Community (vendor blog, unverified against WhatsApp help pages), which bounds a single owned Community far below the roughly 9,000 reach the plan assumes, so the plan depends on groups the founder does not control. The 30-60 groups x 30 hours of joining and posting is also the largest unfunded hours item in the 10 h/week budget.
- evidence: [C07] WhatsApp group limit 1,024 members; Community up to 5,000 members across groups [source: https://getkanal.com/blog/community-guide-whatsapp; vendor blog, search summary only]
- what would fix it (FIXABLE only): WhatsApp help-centre and Business/Community policy pages (desk research), plus evidence from a field test that at least some admins accept the posts (not desk-obtainable): e.g. a written yes from at least 10 society admins and a costed back-up channel.
- fix would change customer/problem/revenue model: no

### FE5 — FATAL
- flaw: No defensible reason to pay 10% against free incumbents, and no incumbent-response plan. OLX, Facebook Marketplace and society WhatsApp groups are free; the operator adds no escrow, delivery, inspection or guarantee ("No inventory, no logistics. Delivery is arranged by the buyer."). The only differentiator is curation and move-out-date timing, which any society admin can copy at zero cost by pinning a "move-out sale" post. Forge-v1 admits the moat is "None yet". Appliance sellers also have Cashify-type buyback with free pickup (forge-v1.md#C05), which leaves only bulky furniture of ₹2,000-9,000 where a ₹200-900 fee competes with ₹0. Seller-side pain in Pune is "unproven" per forge-v1 itself.
- evidence: [C08] Forge-v1 states moat none, severity unproven and seller willingness to pay unevidenced [source: forge-v1.md Moat over time; forge-v1.md#C07; forge-v1.md#C14; forge-v1.md#C17]
- what would fix it (FIXABLE only): n/a; a fix requires adding a paid service (inspection, pickup, guarantee), which changes the core problem and cost structure.
- fix would change customer/problem/revenue model: yes

### FE6 — FIXABLE
- flaw: Labour-linear scaling and thin hours slack. Operations are manual per sale (post, reply, match, collect link). At the conservative 2.0 h/sale, 9.2 of 10 hours per week are used for only about 20 sales in three months. Success (more sales) raises hours: 25 sales/month at 2.0 h is 50 h/month of operations alone plus acquisition. K2 is HARD with no stretch. Seasonality is also unaddressed: move-outs cluster (assumed) at lease and job-change dates, so sales bunch into weeks that exceed 10 hours. [ASSUMPTION: move-out seasonality is plausible, not evidenced]
- evidence: [C09] 120 hours over 13 weeks = 9.2 h/week conservative [source: economics-v1.md Calculations step 10]
- what would fix it (FIXABLE only): a sourced or measured per-sale handling time at or under 1.5 h and a week-by-week hours budget showing at most 10 h at the break-even volume. Obtainable only by a field trial of about 10 sales, not by desk research.
- fix would change customer/problem/revenue model: no

### FE7 — FIXABLE
- flaw: Capital-use numbers are low-confidence inputs. Meta CPM of ₹300, the ₹1,000/month placeholder, the ₹150 broker fee, the ₹3,000 notice-board cost and the Razorpay fee all come from search summaries or ASSUMPTION; several pages were not opened. The capital limb of KE1 passes by a wide margin (₹24,781 against ₹1,00,000), so this does not decide the case, but the conservative case is not sourced.
- evidence: [C10] Ad cost sources are vendor blogs read only as search summaries, ranges ₹0.51-34 CPC [source: economics-v1.md#C08]
- what would fix it (FIXABLE only): open the Meta, Razorpay and notice-board price pages and quote dated figures. Obtainable by desk research, except notice-board and broker fees, which need phone quotes.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Conservative contribution ₹117/sale, blended cash CAC ₹1,064, ₹262 excluding paid Instagram, seller one-time [source: economics-v1.md Calculations steps 5, 6, 11]
- [C02] Conservative collection (paying share) input 40% [source: economics-v1.md#C03]
- [C04] Consumer Protection (E-Commerce) Rules 2020: e-commerce entity definition and grievance officer duty [source: https://www.lkslaw.com/insights/news/e-commerce-consumer-protection-e-commerce-rules-2020-notified, search summary only]
- [C05] CGST Section 24 compulsory registration categories and secondary-source threshold for service suppliers [source: https://www.knowyourgst.com/gstlaw/cgst-act/24-compulsory-registration-in-certain-cases-24/; https://learn.quicko.com/?p=1370, search summaries only]
- [C06] Proposed 2021 DPIIT registration amendment, notification status unconfirmed [source: https://www.bananaip.com/?p=77645]
- [C07] WhatsApp group (1,024) and Community (5,000) member limits per a vendor blog [source: https://getkanal.com/blog/community-guide-whatsapp, search summary only]
- [C11] Pune resale guide names OLX and Facebook Marketplace as top furniture channels and local dealers for quick cash; buyer usually arranges transport at ₹500-1,500 for bulky items; single commercial blog [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1]
- Local data on Pune seller behaviour, society-admin policies, WhatsApp policy text, and Meta's commerce terms was not found; coverage remains thin (01-local-market.md coverage 3/10). No national claim is presented as local.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a (round 1) | n/a | n/a |
