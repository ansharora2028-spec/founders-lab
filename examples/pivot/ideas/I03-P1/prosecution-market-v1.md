---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: prosecutor-market
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
- Own web searches (results only; no page was opened, so all figures below come from search-result summaries).
- Local data is thin (01-local-market.md coverage score 3). Most evidence below is national or other-city. No Pune-specific resale data was found.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | INSUFFICIENT EVIDENCE | C01, C02, C03 | Threshold is 3 named operators with a dated 2024+ figure, at least 1 in Pune, in used furniture and appliances through an intermediary. Cashify has a figure (C01) but it is mostly refurbished phones, not furniture or appliances. Furlenco has a figure (C02) but it is a rental business; Furbicle (refurbished sales) has no separate figure. No Pune-operating operator with a figure was found. At most 1-2 of 3 are partially met. Not NOT MET only because the search tool is weak; obtainable by desk research (Tracxn, Entrackr, Quikr/OLX Pune listing counts). |
| KM2 | INSUFFICIENT EVIDENCE | C04, forge-v1.md#C04, forge-v1.md#C13, economics-v1.md#C01 | No counted sample of 50 listings exists. Only guide-site price ranges (undated, content marketing). The ranges straddle the ₹3,000 line: older fridges ₹1,200-3,500, older sofas ₹1,500-4,000, good sofas ₹4,000-15,000. The economics conservative price is exactly ₹3,000 and is an ASSUMPTION. Median cannot be inferred. Obtainable by desk research (manual count of OLX/Quikr/FB Marketplace Pune listings). |
| KM3 | INSUFFICIENT EVIDENCE | C05, C06, C07, forge-v1.md#C06, forge-v1.md#C14 | No seller-side commission operator for used goods that has run 24+ months was found. OLX and Quikr monetise through ads and paid placement, not seller commission (C05). Cashify and Zefo buy outright and resell, which is not a seller-paid commission (C01, C06). Forge-v1.md#C14 labels seller willingness to pay as an unsupported ASSUMPTION. Evidence leans against, but absence in a weak search tool is not proof. Second prong (at most 1 documented peer-to-peer closure) cannot be confirmed either way; see C07, C08 for closures that exist. |
| KM4 | INSUFFICIENT EVIDENCE | C09, 01-local-market.md#C01, 01-local-market.md#C03 | Threshold is 20,000 renter households turning over per year in six areas, derived from renter share and tenure. No renter-household count, rental share or tenure figure exists. The only size figures are employee headcounts from developer marketing blogs (C09), which are not renter households and cover Hinjewadi and Kharadi, not all six areas. Obtainable only partly by desk research (census wards, portal data); a defensible derivation needs assumptions on tenure. |
| KM5 | INSUFFICIENT EVIDENCE | forge-v1.md#C07, forge-v1.md#C09, 02-signals.md#C04 | Threshold is 20 dated public Pune posts from 2025-10-15, 5 reporting failure. Zero were produced. Forge-v1.md#C07 states no direct evidence was found; 02-signals.md#C04 states no Reddit or review data was retrieved. This reflects a tool gap, not a finding of absence. Guide pages (forge-v1.md#C09) are content marketing and do not count. Obtainable by manual desk research (Reddit r/pune, FB groups, Quora, Google reviews). |

## Flaws
### FM1 — FATAL
- flaw: The revenue is a 10% commission collected after handover in a market where listing and contact are free. Buyer and seller meet in a free group and can close without paying. Forge-v1 admits that willingness to pay is "the largest load-bearing assumption" and that leakage of 30-60% is plausible with no data. The only fixes (escrow or platform-held payment, or a flat upfront fee) change the revenue model and, for a 0-transaction-history operator with no payment-aggregator licence, are heavy. A flat upfront fee is the already-abandoned I03 model, so reverting is a second pivot and a loop.
- evidence: [C10] Forge-v1 conservative leakage and economics-v1 conservative 40% payment share are both ASSUMPTIONS with no data. [source: forge-v1.md#C14; economics-v1.md#C03]
- evidence: [C05] OLX and Quikr leave negotiation, advance and transaction between buyer and seller, and monetise through ads and paid placement; Quikr later launched Quikr Doorstep to address trust, payment and logistics in consumer-to-consumer transactions, which indicates that the free listing model did not capture the transaction. (national) [source: https://uniquebusinessmodels.substack.com/p/23-how-do-used-good-marketplaces]
- evidence: [C11] Economics-v1 conservative case: contribution ₹117 per completed sale against blended cash CAC ₹1,064; payback "not reached". [source: economics-v1.md Scenarios and Calculations]
- fix would change customer/problem/revenue model: yes

### FM2 — FATAL
- flaw: The paying customer is a one-time user (a leaving tenant transacts once), selling an item with a small ticket, so there is no repeat revenue to pay back acquisition cost. Conservative CAC of ₹1,064 exceeds contribution of ₹117 on a single sale; even without paid Instagram it is ₹262 against ₹117 (economics-v1.md Calculations step 11). Forge-v1.md#C10 gives ₹200-400 commission on a ₹2,000-4,000 item. Fixing this needs a different payer (brokers, PG operators, landlords, repeat sellers) or a higher-ticket category, which changes customer or revenue model.
- evidence: [C12] Forge-v1 states the seller transacts once on leaving. [source: forge-v1.md#C01; economics-v1.md Calculations step 6]
- evidence: [C13] Resale price ranges used by forge and economics come from one content-marketing guide site, undated and unverified. [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1, via forge-v1.md#C04]
- fix would change customer/problem/revenue model: yes

### FM3 — FIXABLE
- flaw: Demand and pain on the seller side are not evidenced for Pune, and the demand-side substitutes are strong and growing. Forge-v1 admits severity is "unproven" and C17 is an ASSUMPTION. Rental companies are growing: Furlenco total revenue rose about 59% to roughly ₹240 crore in FY25 and turned profitable, which shows spending moving to rental (zero disposal burden) rather than buying used. Cashify serves appliance and electronics sellers with pickup and instant quotes in Pune areas, so a large part of the seller's pain (appliances) already has a paid, funded solution. Free substitutes (OLX, Quikr, FB Marketplace, kabadiwalas, giving to the next tenant or landlord) cost ₹0.
- evidence: [C02] Furlenco FY25 total revenue about ₹240 crore (+59%), net profit ₹3.1 crore, rental the bulk. (national) [source: https://startupfeed.in/furlenco-turns-profitable-fy25-rs-240-crore-revenue/]
- evidence: [C01] Cashify FY25 operating revenue about ₹1,096 crore, net loss about ₹10.5 crore. (national) [source: https://inc42.com/buzz/cashify-trims-loss-by-80-to-inr-11-cr-in-fy25/]
- what would fix it: at least 20 dated Pune seller-side posts (KM5), and a named reason the seller pays 10% when OLX and Cashify are available. Obtainable by desk research, but only partly; willingness to pay needs a live test, not desk research.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: Market size in the six target areas is not established. The only figures are developer-blog headcounts and the forge's path-to-100 table is entirely ASSUMPTION (about 90 completed sales from assumed rates). Forge-v1 itself says 100 is not supported and that the realistic target is 10-20 sales. At 10-20 sales and ₹120 realised per sale, 3-month revenue is under ₹3,000 (economics-v1 Calculations step 8: revenue ₹2,343).
- evidence: [C09] Hinjewadi plus Kharadi IT parks "over 400,000 professionals" per a developer blog; a second blog gives over 200,000 for Hinjewadi alone; no renter-household or tenure figure. (other: marketing blogs) [source: https://www.sobha.com/blog/pune-workforce-residential-housing-demand/]
- what would fix it: renter share and average tenure from census, PMC, or a portal report with stated methodology, giving annual turnover of at least 20,000 households. Obtainable by desk research, with moderate effort; the answer may well be that the pool is large, so this is not a kill by itself.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: The forge did not address the graveyard. Comparable ventures failed or returned little: Move Loot (US furniture resale) pivoted to peer-to-peer as it ran out of cash and shut down in 2016. Shopo (India) shut in 2017 citing a consumer-to-consumer market that was not economically viable (handicrafts, not furniture). Zefo (India, managed used-goods resale for furniture and appliances, Bengaluru, Delhi-NCR, Mumbai, no Pune) raised about $16-19 million and was acquired by Quikr in 2019 at a reported ₹200 crore, mostly in stock, a modest return. No Pune furniture-resale startup history was found.
- evidence: [C07] Move Loot, YC-backed furniture resale marketplace, shut down in 2016 and sold its customer list to Handy. (other: US) [source: https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-sells-customer-list-to-handy]
- evidence: [C08] Shopo announced shutdown effective 2017-02-10, citing a consumer-to-consumer market that was not robust enough to be economically viable. (national) [source: https://www.businessinsider.in/snapdeals-shopo-shuts-down-roposo-kraftly-see-surge-in-sellers/articleshow/57208653.cms]
- evidence: [C06] Zefo funding and Quikr acquisition in 2019 (about $16-19M raised; reported ₹200 crore, mainly stock). (national) [source: https://inc42.com/buzz/ecommerce-used-goods-zefo]
- what would fix it: a post-mortem or sourced explanation of why a manual WhatsApp board avoids the failure causes (payment leakage, low-ticket economics, no repeat use). Obtainable by desk research.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] Cashify FY25 operating revenue about ₹1,096 crore (+17% from ₹935 crore); refurbished-product sales about ₹999 crore; net loss about ₹10.5 crore; revenue is dominated by used phones and devices, not furniture. (national) [source: https://inc42.com/buzz/cashify-trims-loss-by-80-to-inr-11-cr-in-fy25/, FY25]
- [C02] Furlenco FY25 total revenue about ₹240 crore (+59%), net profit ₹3.1 crore, rental the bulk, furniture sales about ₹21 crore; parent runs refurbished brand Furbicle with no separate figure. (national) [source: https://startupfeed.in/furlenco-turns-profitable-fy25-rs-240-crore-revenue/, FY25]
- [C03] A Rentomojo FY25 revenue figure of ₹266 crore appeared on a Furlenco page without clear attribution; treat as unverified. (national) [source: https://indianretailer.com/news/furlenco-reports-strong-growth-and-profit-turnaround-fy25]
- [C04] Pune sofa resale guide ranges: 3-6 year sets ₹4,000-15,000, 6+ year ₹1,500-4,000; fridges 5-10 years ₹2,800-7,500, 10+ years ₹1,200-3,500; buyer usually arranges tempo at ₹500-1,500. Undated content-marketing guide, not marketplace data. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune?amp=1; https://knowledge.digirake.com/refrigerator/sell-old-refrigerator-pune?amp=1]
- [C05] OLX and Quikr act as catalysts; negotiation, advance and transaction stay between buyer and seller; Quikr was free for three years and then charged for premium placement; launched Quikr Doorstep for trust, payment and logistics. (national) [source: https://uniquebusinessmodels.substack.com/p/23-how-do-used-good-marketplaces]
- [C06] Zefo: Bengaluru-based used-goods marketplace for furniture and appliances, bought from households, refurbished and resold with warranty; operated in Bengaluru, Delhi-NCR, Mumbai, not Pune in reported sources; acquired by Quikr in April 2019 for a reported ₹200 crore. (national) [source: https://inc42.com/buzz/ecommerce-used-goods-zefo]
- [C07] Move Loot (YC-backed furniture resale marketplace) shut down in 2016 after pivoting to peer-to-peer. (other: US) [source: https://techcrunch.com/2016/06/29/move-loot-a-yc-backed-furniture-resale-marketplace-shuts-down-sells-customer-list-to-handy, 2016-06-29]
- [C08] Shopo (Snapdeal-owned) shut 2017-02-10, citing a consumer-to-consumer market not robust enough to be economically viable; handicrafts, not furniture. (national) [source: https://www.businessinsider.in/snapdeals-shopo-shuts-down-roposo-kraftly-see-surge-in-sellers/articleshow/57208653.cms, 2017]
- [C09] Hinjewadi and Kharadi IT hubs: over 400,000 professionals combined per a developer blog; another blog says over 200,000 in Hinjewadi; no renter-household counts or official figures found. (marketing blogs, not official) [source: https://www.sobha.com/blog/pune-workforce-residential-housing-demand/]
- [C10]-[C13] are referenced in flaws above and cite forge-v1 and economics-v1 claim ids directly.
- Coverage note: search results only, no page opened; Tracxn/Entrackr/Quikr/OLX Pune listing counts were not reached. Statuses of INSUFFICIENT EVIDENCE reflect that gap and are not an endorsement.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| none (round 1) | n/a | n/a |
