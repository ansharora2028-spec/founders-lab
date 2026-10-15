---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-execution
version: 1
created: 2026-10-15T12:00:00Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/01-local-market.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/02-signals.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/kill-criteria.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/forge-v1.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/economics-v1.md
- Plus own web research (claims in Evidence below). Official Meta pages could not be retrieved; searches returned only third-party summaries.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | INSUFFICIENT EVIDENCE | economics-v1.md#C10, economics-v1.md#C16, economics-v1.md#C12, economics-v1.md#C13, forge-v1.md#C14 | Modelled numbers are inside the limits: ₹10,500 against the ₹40,000 ceiling, peak about 6.8 h/week against 10, first revenue at 2.8 months against 3. But the criterion asks for sourced prices and a week-by-week schedule reaching a paid listing before month 3. Neither exists. Every cost and hour input is ASSUMPTION. The ₹5,000 legal line is unsourced. The 2.8-month figure rests on a self-imposed gate (300-500 community members before charging, economics-v1.md#C16, itself ASSUMPTION) with about 1 week of slack on a HARD K6. The hours check also averages 93.5 h over 20 weeks (economics-v1.md calc 13). Charging-window load is 63.5 h over 8 weeks, about 7.9 h/week. That still fits K2, but the stated 6.8 peak is not the true peak. K1, K2 and K8 fit on paper. K6 is thin. |
| KE2 | INSUFFICIENT EVIDENCE | economics-v1.md#C04, economics-v1.md#C05, economics-v1.md#C06, economics-v1.md#C13, forge-v1.md (Path to first 100) | Conservative cash blended CAC is ₹72 (at most ₹100) and acquisition hours are 37.5 h over 8 weeks, about 4.7 h/week (at most 6). Both rest entirely on unsourced customer counts: 52 customers in 8 weeks, from forge conversions that forge itself calls ASSUMPTION ("Sourced numbers in this table: none"). No Pune channel cost or conversion was sourced; the CPC figures are national vendor estimates. The only paid-channel test row (conservative CAC ₹3,400 vs margin ₹130.58) fails by 26x, so spend cannot substitute for organic reach. Priced at ₹300/h the loaded CAC is ₹438 and fulfilment time alone exceeds margin. The criterion needs a "stated, tested assumption"; nothing has been tested. |
| KE3 | INSUFFICIENT EVIDENCE | forge-v1.md#C17, economics-v1.md#C09, C01 below, C02 below | Forge states the Meta terms were "not checked". Economics assumes the WhatsApp Business app and Community are free to use for a paid board. No fallback channel is designed or costed against the ₹10,000 / 1 week threshold. Whether the Business app can create or host a Community is unverified. My search found no official Meta text, so neither a prohibition nor a permission on paid listings of used goods is confirmed. The only member cap seen is 1,024 per group (third-party blog), against a 300-500 member target that is not a binding limit. The RWA groups that supply the demand side belong to third-party admins whose posting rules are unknown. API per-message cost is not a factor, because the model is manual. |
| KE4 | INSUFFICIENT EVIDENCE | forge-v1.md#C15, forge-v1.md#C16, economics-v1.md#C10, economics-v1.md#C11, 01-local-market.md#C18, 01-local-market.md#C19, C03-C05 below | Neither file resolves any of the five items the criterion lists. Shops and Establishments is left open (sources conflict). GST: economics assumes none is due below ₹20 lakh. The mandatory-registration clause for e-commerce operators (Section 24(x)) appears tied to the operator having to collect TCS under Section 52; a listing board that does not collect sale consideration likely falls outside it. A GST Council flyer states more broadly that every operator must register, so the reading is contested (C04, C05 below). The Consumer Protection (E-Commerce) Rules 2020 are not mentioned anywhere in forge or economics. They define an e-commerce entity as anyone who owns, operates or manages a digital platform for e-commerce. Entities must appoint a grievance officer, acknowledge complaints in 48 hours and resolve them in one month (C03 below, secondary sources). No seller terms or disclaimer structure is drafted. No insurance or disclaimer path is priced for used electrical appliances (₹5,000/year cap). DPDP: compliance date reported as 2027-05-13 (02-signals.md#C12); another vendor says it may move earlier (unconfirmed). Likely cheap to fix, but nothing is shown. |
| KE5 | NOT MET | forge-v1.md (Moat over time), forge-v1.md#C08, forge-v1.md#C10, economics-v1.md#C01, C06 below | (a) No listing and payment flow is designed. Forge says the operator posts listings by hand and the sale is off-platform. Gating the fee before the listing is visible would stop a buyer-seller bypass of that listing. It does not stop copying the listing for free: forge's own moat section says members and listings can be copied to other groups. No evidence is offered that 70% of matched listings would still pay. (b) Passes: no pickup, escrow or inventory (forge-v1.md Narrowest wedge). (c) Fails: forge concedes "Incumbents and free alternatives can match the feature at no cost" and the economics model has no incumbent-response scenario. OLX already gives free ads per category with a cap and charges only beyond it (forge-v1.md#C08). No comparable paid-listing or local classifieds operator in India with listing-fee revenue is cited. The conservative economics (zero repeat, 25% discount) are positive only on cash. The criterion requires all three parts. |

KM criteria: no direct execution evidence offered; not assessed.

## Flaws
### FE1 — FATAL
- flaw: The ₹199 listing fee cannot be enforced against free copying, and the design has no defence. Sellers can post free on OLX or Facebook Marketplace. Anything shown in the community can be re-posted for free into RWA groups. Incumbent response is already "free". Forge lists the moat as "None yet" and its own persona evidence shows free channels are the default. The conservative economics are positive only because the stated ₹149 price is assumed, not observed.
- evidence: [C01] OLX gives limited free ads per category and location (its own example is 2 furniture ads per 60 days) with paid boosts beyond that. (national) [source: https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/]
- evidence: [C02] Guides for Pune sellers name OLX, Facebook Marketplace and apartment/RWA WhatsApp groups as the main channels near Hinjewadi and Magarpatta, and local dealers who buy outright and arrange pickup. The same guides place those dealers around Bohri Ali, Hadapsar and Camp rather than the western IT corridor. Generic content pages, unverified. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- evidence: forge-v1.md Moat over time; economics-v1.md#C01.
- what would fix it: none by tweaking the same model. A fix needs (i) a flow design where the fee is paid before any contact detail is visible, and (ii) at least 1 sourced Indian paid-listing or local-classifieds operator earning listing-fee revenue in the presence of free OLX and Facebook. Item (ii) is desk-researchable. Item (i) needs a willingness-to-pay test that desk research cannot supply. If the only workable fix is a commission or a buyer-side fee, that changes the revenue model.
- fix would change customer/problem/revenue model: yes (if the fee point moves to commission or buyer fee)

### FE2 — FIXABLE
- flaw: Platform dependency is untested. The whole product runs inside WhatsApp (Community or groups) and RWA groups owned by others. Forge and economics both say the Meta terms were not checked. No fallback is designed. Whether the WhatsApp Business app supports Communities, and whether commercial posting is allowed in RWA groups, is not verified. Meta's marketing-message pricing already moved in 2026 (02-signals.md#C11, vendor figures conflict).
- evidence: [C06] Meta's commerce policy as summarised by third parties lists prohibited categories such as alcohol, animals and currency. The summaries say nothing on used goods, paid listings or community limits. [source: https://docs.rasayel.io/whatsapp-commerce-policy]
- evidence: [C07] Search results cite a 1,024 per-group member limit (third-party blog, 2026). Nothing confirmed from WhatsApp's own help pages. [source: https://getkanal.com/blog/community-guide-whatsapp]
- what would fix it: the current official WhatsApp help-centre pages on Communities, group and community limits, Business app Community support, and WhatsApp's Terms of Service on commercial use, plus a costed fallback (own listing page or Telegram, at most ₹10,000 and 1 week). Desk research: yes for the policy text and fallback cost. No for RWA admin rules, which need Pune admin outreach.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: The legal and compliance load is unexamined, and the Consumer Protection (E-Commerce) Rules 2020 are missed entirely. A board run by one person that lists third-party goods and takes a fee plausibly counts as an e-commerce entity. That brings a visible grievance officer and 48-hour / one-month complaint timelines. The GST position (not registered below ₹20 lakh, per economics-v1.md#C11) rests on a contested reading. No disclaimer for used electrical appliances is drafted. The ₹5,000 legal line in the economics is unsourced.
- evidence: [C03] Rules define an e-commerce entity as any person who owns, operates or manages a digital or electronic platform for e-commerce (excluding sellers on a marketplace). Rule 4(4) requires a grievance officer. Rule 4(5) requires acknowledgement within 48 hours and resolution within one month. Secondary summaries only; no source found on exemption for small classifieds. (national) [source: https://indiacorplaw.in/?p=10190]
- evidence: [C04] Section 24 CGST: compulsory registration for e-commerce operators is read by commentary as tied to the operator being required to collect TCS under Section 52. (national) [source: https://studycafe.in/compulsory-registration-under-gst-103105.html]
- evidence: [C05] GST Council TCS flyer states that every operator must register. Conflicts with C04; whether a listing fee is "consideration" is not addressed. (national) [source: https://www.gstcouncil.gov.in/sites/default/files/e-version-gst-flyers/TCS%20MECHANISM.pdf]
- what would fix it: the Rules' text (applicability and exemptions), a CBIC or GST Council circular or advance ruling on classifieds-style listing-fee operators, the Labour Department page on Shops and Establishments for a sole proprietor, a draft disclaimer, and a quote for appliance-liability cover. Desk research: yes for all except the insurance quote.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: Time to first revenue is thin on a HARD constraint. The conservative case reaches first revenue at 12 weeks (2.8 months) because it holds off charging until a 300-500 member buyer community exists. That gate is forge's own ASSUMPTION and the economics adopt it unchanged. A slower community build breaks K6 (3 months, HARD). The hours check also understates peak load (about 7.9 h/week in the charging window, not 6.8).
- evidence: economics-v1.md#C16 (weeks to threshold, ASSUMPTION); economics-v1.md calc 13 and 9 (63.5 h in 8 charging weeks); forge-v1.md#C13.
- what would fix it: a week-by-week schedule that charges the first seller before month 2 without waiting for the gate, or sourced evidence on community build rates in Pune housing groups. Schedule: desk research yes. Build-rate evidence: no, needs a field test.
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: Operator throughput caps the business at a low ceiling, and the cash-positive claim is narrow. At 10 h/week the conservative loaded time is 1.22 h per customer, about 8 customers/week, or about ₹1,000/week contribution before fixed costs. Net over the first 8 charging weeks is ₹1,040, and that figure excludes the ₹5,000 legal and ₹1,500 SIM setup. After those, the window is about -₹5,460. Setup of ₹10,500 needs 81 listings to recoup. There is zero repeat, and every sale needs a new acquisition. Listing volume grows only with hours, not with the audience.
- evidence: economics-v1.md calc 9 (1.22 h per customer), calc 10 (net ₹1,040), calc 11 (81 listings), economics-v1.md#C15 (no repeat); economics-v1.md Verdict inputs (negative at ₹300/h).
- what would fix it: a cost and time model showing at least 100 paid listings within 6 months inside 6 h/week outreach and the 10 h cap, with sourced per-listing handling time. Desk research: partial; handling time needs a pilot.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Payment collection is modelled as a gateway at 2.36%, but no collection method suited to a sole proprietor is specified. Collecting many small payments on a personal UPI ID versus a business gateway account (KYC, settlement, refund handling) is unaddressed. The 10% refund assumption has no stated refund policy (e.g. no-sale refunds).
- evidence: economics-v1.md#C02, economics-v1.md#C03 (UPI MDR statements conflict and were not verified there).
- what would fix it: the payment provider's current onboarding and MDR page for a sole proprietor, and a written refund policy. Desk research: yes.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] OLX gives limited free ads per category and location (its own example is 2 furniture ads per 60 days) with paid boosts beyond that. A separate third-party guide claims a flat 5-free-ads cap; the two conflict. (national) [source: https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/]
- [C02] Pune seller guides list OLX, Facebook Marketplace, apartment/RWA WhatsApp groups and local dealers; the dealers named are concentrated in Bohri Ali, Hadapsar and Camp, not the western IT corridor. Unverified commercial pages. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- [C03] Consumer Protection (E-Commerce) Rules 2020: e-commerce entity definition, grievance officer, 48-hour and one-month timelines. Secondary summaries; no small-classifieds exemption found. (national) [source: https://indiacorplaw.in/?p=10190]
- [C04] Compulsory GST registration for e-commerce operators under Section 24 is read by commentary as tied to TCS collection under Section 52. (national) [source: https://studycafe.in/compulsory-registration-under-gst-103105.html]
- [C05] GST Council flyer states every operator must register; conflicts with C04. (national) [source: https://www.gstcouncil.gov.in/sites/default/files/e-version-gst-flyers/TCS%20MECHANISM.pdf]
- [C06] WhatsApp commerce policy, third-party summary: prohibited-category lists only; nothing on used goods, paid listings or community limits. Official Meta pages not retrieved. (global) [source: https://docs.rasayel.io/whatsapp-commerce-policy]
- [C07] WhatsApp group member limit 1,024 and community structure, third-party blog; unverified against WhatsApp help pages. (global) [source: https://getkanal.com/blog/community-guide-whatsapp]
- Not found: any named, reachable used-furniture buyback dealer in the target corridor areas; any official Meta statement on paid listings of used goods; any small-classifieds exemption under the E-Commerce Rules.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| none (round 1) | n/a | n/a |
