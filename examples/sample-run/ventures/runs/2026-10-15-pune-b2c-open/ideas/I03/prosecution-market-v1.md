---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: prosecutor-market
version: 1
created: 2026-10-15T12:00:00Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I03/kill-criteria.md (locked)
- .../ideas/I03/forge-v1.md
- .../ideas/I03/economics-v1.md
- plus ${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md and ${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md
- Own web research this round (claims below). Coverage of Pune-specific data is thin: 01-local-market.md scores 3/10, and my searches returned no Pune-named dealer, no Pune listing counts and no Pune search volumes.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | C01, C02, C03, forge-v1.md#C03, forge-v1.md#C10 | Needs 3 operators with paying sellers, 1 in Pune. Found: unnamed Pune "juna furniture" dealers (blog only, no pricing, no reviews), Zefo (Bengaluru, buy-back model, acquired 2019, 2017-era data). Zero operators charging sellers a listing fee at 100 rupees or more. Threshold of 3 not reached; forge itself labels seller willingness to pay "no evidence found". |
| KM2 | INSUFFICIENT EVIDENCE | forge-v1.md#C08, C04, forge-v1.md#C02 | Only one documented seller-side friction of free channels (OLX free-ad cap, national, forge-v1.md#C08) and buyer pickup logistics from one affiliate blog. Not 2 independent sources documenting failure, and the board has no logistics, so the named mechanism for fixing pickup/no-show failure is absent. |
| KM3 | INSUFFICIENT EVIDENCE | forge-v1.md#C11, economics-v1.md#C06 | No listing count was made in 01, 02, forge or economics. forge-v1.md#C11 (10-20 listings per week in one micro-cluster) is an ASSUMPTION. The 500 listings per month threshold across six areas is unverified. Desk research cannot do the count without manual screenshots. |
| KM4 | INSUFFICIENT EVIDENCE | C05, C06, forge-v1.md#C12 | No keyword-planner volume and no survey with a used-furniture purchase share. Found only an unquantified franchise-guide statement that buyers are students and young professionals. Contrarian buyer claim is an ASSUMPTION in forge-v1.md#C12. |
| KM5 | INSUFFICIENT EVIDENCE | C03, C07, C08, C09 | Criterion requires 3 Indian comparables with causes. I found 1 Indian comparable (Zefo, acquired, not shut) and 2 US failures (Move Loot, Kaiyo; wrong geography, cannot satisfy the India test). No India shutdown cause could be tallied. Direction of the US evidence (logistics, seller payout) is adverse. |

No criterion is MET. Under the locked criteria, a MET status requires positive evidence that does not exist in the files; the honest label is INSUFFICIENT EVIDENCE, not NOT MET, because the desk-research gaps for KM1/KM4/KM5 have not been exhausted by a tool-limited search. KM2 and KM3 need manual field work.

## Flaws
### FM1 — FIXABLE
- flaw: The only revenue assumption (sellers pay 199 rupees when OLX, Facebook Marketplace, society groups and dealers are free) has no evidence in any file. Economics-v1 prices at 149 rupees conservative, still untested. The demand-evidence requirement in venture-rules rule 3 is unmet: no competitor with revenue from used-furniture seller fees, no search volume, and no existing spend on a worse solution has been shown.
- evidence: forge-v1.md#C10 and forge-v1.md#C09 (own admission); [C01] a Pune guide says dealers pay cash and arrange pickup, free classifieds yield better prices.
- what would fix it: at least 3 dated operator pricing pages or reviews showing sellers paying a fee of 100 rupees or more or a 10% commission, 1 in Pune. Partly desk-researchable (pricing pages, Justdial/Google Maps reviews); a Pune willingness-to-pay test (e.g. 10 sellers asked to pay) is not desk-researchable.
- fix would change customer/problem/revenue model: no (if evidence exists); yes if the only viable payer is the buyer or a commission

### FM2 — FIXABLE
- flaw: Low item values cap the fee the seller can bear. The 199 rupee fee is a large share of the proceeds from typical items. Sources aimed at the rental market state used bed frames recover roughly 10-15% of purchase price; the forge's own 30-60% recovery claim is from an unsourced commercial blog. At buyer pickup cost of 500-1,500 rupees (tempo/Porter) per piece, per [C06], the seller or buyer already bears a bigger cost than the fee.
- evidence: [C05] bed-frame resale 10-15% of purchase price claim (rental-company-adjacent, sales argument); [C06] tempo/Porter cost 500-1,500 rupees within the city (affiliate blog); forge-v1.md#C04 (30-60% recovery, unsourced).
- what would fix it: dated sold-price data for used furniture and appliances on OLX/Quikr in Pune corridor, showing median sold price at least 10x the fee (about 2,000 rupees). Obtainable by desk research only partly (listing prices are visible; sold prices are not).
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: Size ceiling under the plan's own numbers is tiny. The forge path targets about 100 paying sellers (19,900 rupees gross) over roughly 6 months; KM3's own arithmetic gives about 9,950 rupees per month at 500 listings and 10% conversion. Seller fee is one-off (economics-v1.md#C15: zero repeat), so recurring revenue per seller is zero and each month requires fresh acquisition of movers. Economics-v1 itself shows net 1,040 rupees in the first 8 charging weeks in the conservative case and negative economics at 300 rupees/hour operator time.
- evidence: forge-v1.md Path to first 100 customers; economics-v1.md#C15 and Calculations item 10; kill-criteria KM3 threshold text.
- what would fix it: measured monthly Pune corridor move-out volume and listing counts (KM3 evidence). Obtainable by a manual count, not by desk search.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: The demand side is promotional-source only and the contrarian premise is contradicted by the same source. Forge-v1 cites rental-incumbent press releases (Rentomojo) for both the 50,000 rupee setup cost and "near-total resale loss". The same releases are the evidence that used goods do not resell; they cannot also prove a used-buyer market exists. No buyer-side purchase share or search volume exists anywhere in the run files.
- evidence: forge-v1.md#C07, forge-v1.md#C12; 01-local-market.md#C01 (promotional, June 2026); [C05].
- what would fix it: keyword volumes of at least 1,000 monthly searches for used furniture Pune style queries, or 2 sourced purchase-share data points at 10% or more. Keyword data is obtainable from a free planner; survey data was not found in my search.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Cold-start order of operations conflicts with a hard time limit. The buyer community of 300-500 must exist before sellers are charged (forge-v1 path), yet the buyer side pays nothing and has no demonstrated reason to join a Pune WhatsApp group when OLX, Facebook Marketplace and society groups already circulate the same listings (forge-v1.md#C02). Economics-v1 conservative first revenue at 12 weeks leaves about 1 week of slack to the 3-month HARD limit and rests on ASSUMPTION C16.
- evidence: forge-v1.md#C02, forge-v1.md#C13; economics-v1.md#C16 and constraint table K6.
- what would fix it: evidence of a comparable local community reaching 300 members in under 10 weeks in an Indian city (dated group or channel growth data), or a measured pilot. Pilot is not desk-researchable.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Graveyard analysis is absent from forge-v1. No dead or surviving comparable (India or elsewhere) is named in forge-v1, and 01-local-market.md#C04 found no Pune consumer shutdown only because coverage is thin. The relevant failures I found are in resale marketplaces with logistics (Move Loot, Kaiyo, US) and Zefo (India) which held inventory, the opposite of this idea. No evidence that a listing-fee-only furniture board has ever earned revenue in India.
- evidence: [C07] [C08] [C09]; 01-local-market.md#C04.
- what would fix it: 3 Indian comparables with stated causes of shutdown or pivot (Inc42, YourStory, Entrackr, Tracxn) and at least 1 surviving operator with revenue under a paid-seller model. Obtainable by desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Pune "juna furniture" dealers around Bohri Ali, Hadapsar and Camp are said to buy sofas outright and arrange pickup; OLX, Facebook Marketplace and society WhatsApp groups give better prices but the seller arranges pickup. Affiliate blog, unverified, no dealer named, no prices. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- [C02] Zefo (Bengaluru, also Delhi NCR and Mumbai) bought used goods from households and resold them with its own refurbishment; Quikr acquired it in April 2019 in a deal reported at about 210 crore rupees. Buy-back, not a seller-fee model. (other city: Bengaluru) [source: https://yourstory.com/2017/10/pre-owned-goods-marketplace-zefo-raises-rs-60-crore-series-b, 2017; acquisition detail from search summary, not opened]
- [C03] Ken Research puts the paid-listing share of Indian online classifieds at 10.0% in 2025. Market-research estimate, methodology not seen. (national) [source: https://www.kenresearch.com/industry-reports/india-online-classifieds-market, 2025]
- [C04] Quikr charges advertisers and earns from featured listings; OLX's core site was mainly monetised through Google text ads in the period of that report. Dated, not current. (national) [source: https://www.outlookbusiness.com/enterprise/trend/online-bargain-231]
- [C05] Used bed frames are said to sell for about 10-15% of purchase price on second-hand marketplaces; the claim comes from rental-company-adjacent content. (national) [source: https://smb.orangeleader.com/article/Rentomojos-Bed-and-Mattress-Rentals-Rise-in-Bangalore-in-2026-as-Renters-Reject-indian-rupee50000-Upfront-Costs-and-Weak-Resale-Probability-for-indian-rupee1000Month-Rentomojo-Plans/6a2f127945b635ab6be4e00a, 2026]
- [C06] Buyer pickup by tempo or Porter within Pune is said to cost 500-1,500 rupees. Affiliate blog, unverified. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- [C07] Move Loot, a YC-backed used-furniture resale marketplace in the US, shut down in 2016 and sold its customer list to Handy. (global) [source: https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-sells-customer-list-to-handy, 2016-06-29]
- [C08] Kaiyo, a US secondhand furniture platform, announced it would wind down in August 2024 after sellers filed complaints about delayed payouts. (global) [source: https://www.modernretail.co/operations/online-furniture-platform-kaiyo-says-it-will-wind-down-by-the-end-of-the-month-after-sellers-file-complaints/, 2024-08]
- [C09] Mebelkart (India online furniture marketplace) ceased operating in early 2017 after failing to close a funding round; the results do not say whether it dealt in used goods. (national) [source: https://en.wikipedia.com/wiki/Mebelkart]
- [C10] No survey measuring the share of Indian renters buying used furniture was found in my search; a franchise guide lists students, young professionals and rental-property preparers as buyers with no figures. (national) [source: https://www.franchiseindia.com/index.php/insights/en/article/how-to-open-a-second-hand-furniture-shop-in-india.58019]
- reasoning: the OLX help-page fetch failed (proxy refusal), so forge-v1.md#C08 (OLX free-ad cap) is used as the forge states it, not independently confirmed by me.
- reasoning: the run has thin local data (coverage 3/10). Absence of Pune evidence is a research gap, not proof that demand does not exist; it is also not a reason to treat the criteria as satisfied.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| none (round 1) | n/a | n/a |
