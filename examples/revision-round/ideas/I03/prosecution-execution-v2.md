---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-execution
version: 2
created: 2026-10-15T13:00:00Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/01-local-market.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/02-signals.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/kill-criteria.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/diff-v2.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/economics-v2.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I03/prosecution-execution-v1.md
- Own research this round: one web search on Quikr premium ads. Page fetches of the diff URLs (slideshare, linkedin, indiacorplaw) failed (proxy refused), so the diff URLs could not be opened by me.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | INSUFFICIENT EVIDENCE | economics-v2.md#C10, C11, C14, C17, calc 10, calc 14; prosecution-execution-v1.md KE1 | Modelled numbers fit the limits: ₹22,300 to first revenue against the ₹40,000 ceiling, 7.75 h/week peak against 10, 2.8 months against 3. Nothing in diff-v2 supplies the sourced prices or week-by-week schedule the criterion asks for. Costs and hours are still ASSUMPTION. K6 has about 1 week of slack on a HARD limit and rests on the unsourced 300-500 member gate (C17). Compliance cost is now counted, which is an improvement, but its ₹15,000 comes from an assumption. |
| KE2 | INSUFFICIENT EVIDENCE | economics-v2.md#C04, C05, C06, C14 | Conservative cash blended CAC ₹72 (limit ₹100) and 37.5 acquisition hours over 8 weeks fit on paper. Customer counts (C06) are ASSUMPTION with no Pune data. The paid-boost test row is ₹3,400 per seller against ₹96.40 margin, so cash spend cannot replace unpaid reach. At ₹300/h the loaded CAC is ₹438. Not in the diff; no change from round 1. |
| KE3 | INSUFFICIENT EVIDENCE | economics-v2.md#C09; prosecution-execution-v1.md C06, C07 | Not touched by diff-v2. Meta terms on paid commercial group use are still unchecked (economics-v2 C09 says so). No fallback is designed or costed against the ₹10,000 and 1 week threshold. |
| KE4 | INSUFFICIENT EVIDENCE | diff-v2.md D3; economics-v2.md#C10, C12 | D3 maps the E-Commerce Rules duties from law-firm summaries but states that applicability is unresolved and that cost and hours are ASSUMPTION. GST, Shops and Establishments, a draft disclaimer and appliance-liability cover are not addressed. The threshold (≤₹15,000, ≤4 weeks) is met only by an assumed ₹15,000 conservative line. Not shown either way. |
| KE5 | NOT MET | diff-v2.md D2; prosecution-execution-v1.md FE1 | Part (a): no fee-gated listing flow designed, no evidence for the 70% retention. Part (c): no incumbent-response scenario in economics-v2; free copying remains possible. D2 supplies Quikr and MagicBricks fee precedents but does not show that a comparable operator earns listing-fee revenue (see Round-2 notes). All three parts are required. |

KM criteria: no direct execution evidence; not assessed.

## Flaws
### FE1 — FATAL
- flaw: Carried from round 1, unchanged. The ₹199 fee cannot be enforced against free copying (OLX, Facebook Marketplace, RWA WhatsApp groups) and the design has no defence. The conservative price was lowered to ₹110 (economics-v2.md#C01). That is a concession that willingness to pay is unobserved, not evidence that it exists. Neither fix item from round 1 is delivered: no fee-before-contact flow, and no sourced Indian paid-listing operator earning revenue next to free OLX and Facebook.
- evidence: [C01] Quikr offers free ads and two paid Premium tiers (Top of the page; Urgent plus Top of the page). Its terms say paid monies are non-refundable. The search found no price for any category. [source: https://quikr.com/html/premium_ads.php] (national)
- evidence: [C02] Quikr's terms state paid advertiser monies are not refundable and unused premium credits are forfeited. This differs from the 10% refund assumption in economics-v2.md#C03. [source: https://www.quikr.com/services/termsandconditions] (national)
- evidence: diff-v2.md D2 itself says "Fee-paying by individual sellers is shown to exist, not shown to work at ₹199 for used furniture."
- what would fix it: unchanged from round 1. A flow design with the fee before contact visibility, plus at least 1 dated, sourced Indian operator with listing-fee revenue. The second is desk-researchable; the first needs a willingness-to-pay test.
- fix would change customer/problem/revenue model: yes (if the fee moves to commission or a buyer fee)

### FE2 — FIXABLE
- flaw: Platform dependency is unchecked, with no official WhatsApp text and no costed fallback. No diff row addresses it. Economics-v2 C09 still says Meta terms were not checked.
- evidence: economics-v2.md#C09 (ASSUMPTION: WhatsApp Business and Community assumed free). Round-1 prosecution-execution-v1.md C06, C07.
- what would fix it: official WhatsApp help-centre pages on Communities and group limits, the commerce and terms-of-service text on commercial use, and a fallback (own page or Telegram) costed at ≤₹10,000 and 1 week. Desk research: yes. RWA admin rules: needs Pune outreach.
- fix would change customer/problem/revenue model: no

### FE3 — FIXABLE
- flaw: The compliance position is still unresolved. D3 lists duties (seller undertaking, grievance officer with 48-hour acknowledgement and one-month redress, nodal contact, ranking explanation) but cannot say whether an operator-run WhatsApp board is covered. GST, Shops and Establishments, a disclaimer and appliance-liability cover remain untouched. The cost used is an assumption.
- evidence: diff-v2.md D3; economics-v2.md#C10, C12; 01-local-market.md#C18.
- what would fix it: the Rules text on applicability, a CBIC or GST Council statement on listing-fee operators, the Labour Department page on Shops and Establishments for a sole proprietor, a draft disclaimer, and an insurance quote. Desk research: yes except the quote.
- fix would change customer/problem/revenue model: no

### FE4 — FIXABLE
- flaw: K6 timing is thin. First revenue at 12 weeks (2.8 months) depends on the self-imposed 300-500 member gate and on compliance review running in parallel (economics-v2.md#C17). A HARD limit with about 1 week of slack on an unsourced assumption.
- evidence: economics-v2.md#C17, calc 15.
- what would fix it: a schedule that charges a first seller before month 2 without the gate, or Pune community build-rate evidence (field test only).
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: The business does not recover its setup cost in any observed window. Economics-v2 says it takes about 17 months at 28 listings/month to recoup ₹22,300 in the conservative case, with zero repeat. The 8-week operating net is only ₹2,263, leaving the position at about -₹20,037 at week 20. At ₹300/h, fulfilment alone (₹150) exceeds the ₹96.40 margin, so there is no volume at which it pays. The compliance line added in v2 is what raised sunk cost from ₹10,500 to ₹22,300.
- evidence: economics-v2.md calc 9, 11, 13; Verdict inputs.
- what would fix it: a sourced handling-time figure below about 0.3 h per listing, or evidence of 100 paid listings within 6 months inside 6 h/week outreach. Partial by desk research; needs a pilot.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Payment collection and refund policy for a sole proprietor are not specified. Economics-v2 C03 assumes a 10% refund rate with no policy. Economics-v2 C02 notes UPI MDR statements conflict. Quikr's own terms make paid ads non-refundable, so a refund policy is a design choice that has not been made.
- evidence: economics-v2.md#C02, C03; [C02] above.
- what would fix it: the payment provider's current onboarding and MDR page for a sole proprietor, and a written refund policy. Desk research: yes.
- fix would change customer/problem/revenue model: no

### FE7 — FIXABLE
- flaw: Economics-v2 is internally inconsistent in its payback figures. The table shows base sunk payback of "about 4 months" and optimistic "about 1.5 months", while the arithmetic note gives 1.1 months for base. The model itself calls these "rough and not sourced". The conservative K6 and K1 results are therefore reliable only to the degree the C06 customer counts are, and those are ASSUMPTION.
- evidence: economics-v2.md Scenarios table and the paragraph below it; C06.
- what would fix it: a corrected table. Desk research: yes. A sourced customer-count basis is not obtainable by desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Quikr offers free ads and two paid Premium tiers (Top of the page; Urgent plus Top of the page); the search found no price for any category, including furniture. (national) [source: https://quikr.com/html/premium_ads.php]
- [C02] Quikr terms: paid advertiser monies are not refundable; unused premium credits are forfeited. (national) [source: https://www.quikr.com/services/termsandconditions]
- Not found: any official WhatsApp or Meta text on paid listings of used goods; any dated Indian operator showing listing-fee revenue for used furniture; any small-classifieds exemption under the E-Commerce Rules. The D2 and D3 URLs could not be fetched by me, so I could not verify them directly.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | no | Addresses KM4 (market prosecutor's criterion). Evidence is NONE and the new value says "not fixed". Rule 4: no fix. |
| D2 | no | It has URLs, but they could not be opened by me. By its own description the Quikr rates are undated and from a different category (Mobile/Electronics), the 2018 complaint post is old and negative, and the MagicBricks/99acres rates are real estate from a vendor page. The Quikr premium page I did open confirms paid tiers exist but shows no price and no revenue. The row shows that paid tiers exist. It does not show a listing-fee operator earning revenue for used furniture alongside free OLX/Facebook, which is what FE1 (ii) and KE5 require. The row says so itself. |
| D3 | no | Law-firm summaries of the E-Commerce Rules duties, but the row says applicability is unresolved and cost and hours are ASSUMPTION ("Not fully fixed"). It does not address GST, Shops and Establishments, the disclaimer or appliance cover. FE3 stays open. |
