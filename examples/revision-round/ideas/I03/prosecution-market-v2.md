---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-market
version: 2
created: 2026-10-15T13:00:00Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I03/kill-criteria.md (locked)
- .../ideas/I03/diff-v2.md
- .../ideas/I03/economics-v2.md
- .../ideas/I03/prosecution-market-v1.md (own)
- ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md and ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md
- forge-v2.md was not read. Own research this round: page fetches of the three D2 URLs failed (proxy refused), so I could not open them; one web search was run.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | diff-v2.md D2, C01, C02, prosecution-market-v1.md#C02 | Threshold is 3 operators of used furniture/appliance resale with paying sellers, 1 in Pune. After D2 there is one operator with seller fees (Quikr, national, general classifieds, undated rates). MagicBricks/99acres are real estate and do not count toward a furniture/appliance intermediary. No Pune operator. Threshold not reached. |
| KM2 | INSUFFICIENT EVIDENCE | prosecution-market-v1.md#C01, C02 | No diff row addresses KM2. v1 status stands: one documented free-channel failure, no named mechanism for a no-logistics board. |
| KM3 | INSUFFICIENT EVIDENCE | prosecution-market-v1.md (KM3 row) | No diff row addresses KM3. No dated listing count exists. Needs manual field count, not desk research. |
| KM4 | INSUFFICIENT EVIDENCE | diff-v2.md D1 | D1 states "not fixed". No search volume and no purchase-share data point exist in any file. The only figures in D1 are global and for other terms. |
| KM5 | INSUFFICIENT EVIDENCE | diff-v2.md D2, prosecution-market-v1.md#C07, C08, C09 | D2 gives no Indian shutdown or pivot with a stated cause. Zero of 3 required Indian comparables with causes are added. Zefo (acquired) and US failures remain the only comparables. No survivor under a paid-seller used-furniture model is shown. |

No criterion is MET. The locked file stays the only standard. KE criteria are not assessed.

## Flaws
### FM1 — FIXABLE
- flaw: Seller willingness to pay ₹199 for used furniture listings remains unevidenced. D2 shows that Quikr sells paid ad upgrades to individual sellers, which is evidence that some sellers pay for visibility. It is not evidence for used furniture in Pune, nor at ₹199 for a no-logistics board. Economics-v2 itself says fees exist but are not shown to work at this price.
- evidence: [C01] [C02] diff-v2.md D2; economics-v2.md#C01.
- what would fix it: 3 dated operator pricing pages or reviews of used furniture/appliance resale with seller fees of ₹100+ or commission of 10%+, 1 in Pune. Pricing pages and reviews are desk-researchable; a Pune willingness-to-pay test is not.
- fix would change customer/problem/revenue model: no (yes if the only viable payer is the buyer or the model moves to commission)

### FM2 — FIXABLE
- flaw: Item value versus fee is unchanged since v1 (bed frames 10-15% of purchase price, pickup ₹500-1,500). No diff row addresses it. The conservative ₹110 price now halves the fee while the unit economics still rest on ASSUMPTION customer counts.
- evidence: prosecution-market-v1.md#C05, C06; economics-v2.md#C06.
- what would fix it: dated listing/asking-price data for Pune-corridor used furniture showing a median at least 10x the fee. Asking prices are desk-researchable; sold prices are not.
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: Size ceiling is unchanged. Economics-v2 shows 28 listings/month at ₹96.40 margin, about ₹2,700/month contribution, and about 17 months to recoup ₹22,300 sunk costs, with zero repeat purchase. The volume is ASSUMPTION. At ₹300/hour operator time, fulfilment alone exceeds margin.
- evidence: economics-v2.md#C06, C16, Calculations 9 and 13.
- what would fix it: measured monthly Pune-corridor listing and move-out volume (KM3 evidence). A manual count, not desk research.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE (unfixed after the single revision round)
- flaw: The buyer side is wholly unevidenced. The contrarian premise (tenants buy used instead of renting) rests on the rental incumbent's marketing, which argues that used goods resell poorly. D1 confirms no search or purchase-share data was found.
- evidence: diff-v2.md D1 (evidence url NONE, "not fixed"); prosecution-market-v1.md#C05, C10.
- what would fix it: 1,000+ combined monthly searches for used furniture Pune-style queries, or 2 sourced purchase-share data points of 10%+. Keyword data needs a free planner that this pipeline did not have; survey data was not found.
- fix would change customer/problem/revenue model: no (yes if buyers are shown not to exist and the model shifts to a seller-to-dealer channel)

### FM5 — FIXABLE
- flaw: Cold start versus the 3-month HARD limit is unchanged. Conservative first revenue is at 12 weeks (2.8 months) with about 1 week slack. The 300-500 member buyer community has no sourced reason to form and the 52-seller conservative count is ASSUMPTION.
- evidence: economics-v2.md#C06, C17, constraint table K6.
- what would fix it: dated growth data for a comparable Indian local resale community, or a pilot. The pilot is not desk-researchable.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Graveyard coverage is unchanged. No Indian shutdown cause for a seller-fee used-goods board is documented in any file, and no survivor with revenue is shown. D2 adds fee precedents, not a graveyard.
- evidence: diff-v2.md D2; prosecution-market-v1.md#C02, C07, C08, C09.
- what would fix it: 3 Indian comparables with stated shutdown/pivot causes (Inc42, YourStory, Entrackr, Tracxn). Desk-researchable.
- fix would change customer/problem/revenue model: no

### FM7 — FIXABLE
- flaw: The only fee precedent (Quikr) is accompanied by seller complaints that paid upgrades did not produce leads or refunds. This is adverse evidence for repeat willingness to pay, and it is cited in D2 itself as "poor results and sales pressure". The ₹110 conservative price is taken from an undated deck and a different category (Mobile/Electronics).
- evidence: [C03] [C04]; diff-v2.md D2.
- what would fix it: a dated, current rate card for used furniture or appliance seller fees on any Indian classified or resale operator. Desk-researchable.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Quikr is described in D2 as free posting with paid Premium/Top/Urgent ads, with rates of ₹66/₹110/₹176 (Mobile/Electronics) from an undated deck. I could not open the URL (proxy refused). Treated as the forge's report only. (national) [source: https://www.slideshare.net/slideshow/quikr-ecomm-platform/75732007, undated, not opened]
- [C02] MagicBricks and 99acres owner packages of about ₹974-₹1,463 are real estate, from a vendor page I could not open. Not a furniture or appliance precedent. (national) [source: https://www.leadsquared.com/real-estate-leads-online-india, not opened]
- [C03] Individual Quikr sellers file complaints that paid premium ads did not deliver, from 2017 through 2026, including one dated 2026-03-09 reporting no leads after payment. This confirms that sellers do buy Quikr premium services, in a self-selected complaint source with amounts masked. (national) [source: https://voxya.com/consumer-complaints/no-premium-service-after-payment/260792, 2026-03-09, seen in search results only]
- [C04] Further complaints about premium ads not displayed as premium or without refund, dated 2017-04-21 and 2018-04-26. (national) [source: https://voxya.com/consumer-complaints/my-advertisement-didn't-become-'premium'/580; https://voxya.com/consumer-complaints/not-able-to-use-purchased-premium-ad-package/4247, seen in search results only]
- reasoning: I could not confirm the ₹199-₹499 range from the LinkedIn post cited in D2. My search found complaints about Quikr premium ads but no price figures.
- reasoning: Pune and furniture-specific data remain absent (01-local-market.md coverage 3/10). Absence is a research gap, not proof of no demand, and is not a pass.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| D1 | no | Evidence URL is NONE and the new value says "not fixed". No search or purchase-share data supplied. KM4 and FM4 remain open. |
| D2 | no | Has URLs, but they do not support a pass for KM1 or KM5. They show a fee precedent for a general classifieds platform (undated, different category) and real-estate packages. KM1 needs 3 furniture/appliance operators and 1 in Pune; this adds at most 1 non-Pune, non-furniture operator. KM5 needs shutdown causes; none given. I could not open the three URLs, so the exact figures are unverified by me. Partial value: Quikr sellers paying for upgrades is corroborated by complaints (C03), which is context for FM1, not a fix. |
| D3 | no | Targets KE4, owned by the execution prosecutor. It adds a rules summary from law-firm pages, but states cost, hours and applicability as unresolved or ASSUMPTION. I have no market evidence on it and do not rule on KE4. |
