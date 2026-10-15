---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: forge
version: 1
created: 2026-10-15T10:30:00Z
---

## Core identity
- customer: Individual departing tenants (sellers) in Pune IT-corridor flats (Hinjewadi, Wakad, Baner, Kharadi, Viman Nagar, Magarpatta), who pay. Incoming tenants are the free demand side and do not pay.
- problem: A departing tenant has used furniture and appliances to sell on a fixed move-out date and no dedicated local channel; an arriving tenant faces a large upfront furnishing cost. Severity on the seller side is not evidenced for Pune (see Problem severity).
- revenue model: ₹199 one-off listing fee paid by the seller; optional ₹99 featured-listing upgrade. No inventory, no commission, no buyer fee.
- pivot declared: no (narrowed to one micro-cluster and one listing unit; customer, problem and revenue model are those of the raw idea)

## Persona
- [C01] Seller persona: a salaried tenant in a rented flat in a Pune IT-corridor area, leaving at lease end, holding furniture/appliances bought used or new. The corridor areas are named as renter demand clusters in promotional material. [source: https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399, 2026-06] (promotional; page not read directly by the local-market scout, taken from 01-local-market.md#C01)
- [C02] Where they sell today: a Pune guide lists OLX and Quikr as the first place most sellers try, with Facebook Marketplace, local dealers, Sulekha and JustDial also named; the same blog says Facebook Marketplace and apartment WhatsApp/RWA groups are very active in Hinjewadi and Magarpatta township complexes. Commercial affiliate blog; unverified. [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- [C03] Dealers buy used furniture for cash and arrange pickup, at lower offers than a private sale (same blog; no prices verified). [source: https://knowledge.digirake.com/sofa/sell-old-sofa-pune]
- [C04] Resale recovery claimed by the same blog family is 30-60% of original price, with an example of ₹4,000-7,000 for a branded study table. Unsourced figures on a commercial page. [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune]
- [C05] Buyer persona (free side): incoming tenants who the funded rental incumbent targets with plans from ₹2,199/month for a furniture bundle and quotes a ₹50,000 home-setup cost (promotional, 2026-06). [source: https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399, 2026-06]
- [C06] Rental incumbents' appliance entry prices: Rentomojo fridge/washing-machine plans from ₹149/month in a headline claim, about ₹600/month fridge in a June 2026 release for Pune; the gap is unexplained and all are press releases. [source: https://pr.thebeenews.com/article/Rentomojo-Refrigerator-and-Dining-Table-Rentals-Rise-Across-Pune-as-IT-Professionals-Avoid-EMI-Lock-Ins-and-indian-rupee40000-Setup-Costs/6a28544e5f1a393667890e53, 2026-06]

## Narrowest wedge
- Product: one WhatsApp Community (announcement-only, hosted from a business number) for a single micro-cluster, one cluster first: Hinjewadi Phase 1-2 / Wakad (ASSUMPTION: chosen because both are named in the sources as renter-heavy clusters and are geographically adjacent; no Pune data on which cluster has the most move-outs).
- Unit sold: a single seller listing at ₹199 (photo, price, pickup locality, move-out date), posted by the operator by hand to the community and a spreadsheet catalogue. No app, no payments platform beyond UPI collection.
- Unit that is the narrowest transaction: "whole-flat clearance" listing from one seller with a stated move-out date, since the seller has a deadline and a bundle (bed, wardrobe, fridge, washing machine) that lowers the per-buyer search cost. This is a segment narrowing within the same customer, not a pivot.
- Transaction test: first paid transaction = one seller paying ₹199 by UPI. A sale to a buyer happens off-platform; the operator does not take part in the sale (ASSUMPTION: keeps the operator out of payments and delivery).
- Operating load: manual listing and moderation inside K2 (10 h/week) is assumed feasible at 10-20 listings per week (ASSUMPTION: about 20-30 minutes per listing incl. chat).

## Problem severity
- [C07] The up-front furnishing cost cited for IT-corridor tenants is about ₹50,000, and the rental incumbent frames used-purchase resale loss as near-total (headline of a related release: "near-total resale loss"). Promotional framing, not Pune measurement. [source: https://smb.winchestersun.com/article/Dining-Table-Rentals-Rise-Across-Pune-Delhi-and-Noida-in-2026-as-indian-rupee18000-Setup-Costs-and-Near-Total-Resale-Loss-Push-Households-Toward-indian-rupee495-a-Month-Plans-From-Providers-Such-as-Rentomojo/6a7a26652e905784f149ac06]
- [C08] Free general classifieds already exist: OLX gives a limited number of free ads per category and location (its own help page gives an example of 2 furniture ads per 60 days), with paid boosts after that. (national) [source: https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/]
- [C09] No complaint-volume, search-volume, or switching data for the seller problem in Pune was found in 01-local-market.md, 02-signals.md, or in this round's searches. The pain on the seller side is not evidenced as frequent or costly beyond the promotional resale-loss framing. [ASSUMPTION: stated as a gap, not a finding; the likelihood that sellers are unsatisfied with free classifieds is untested]
- Reasoning: the existence of free alternatives (OLX, Facebook Marketplace, society groups, dealers) means the paid claim depends on whether a curated, local, move-out-dated board is worth ₹199 over a free listing. Nothing found shows willingness to pay for listing placement from individual sellers in Pune.

## Path to first 100 customers
Definition: 100 paying sellers at ₹199 each (₹19,900 gross). All conversion numbers are ASSUMPTION; no Pune channel data was found.

| channel | reach | conversion to paid | customers | basis |
|---|---|---|---|---|
| Housing-society/RWA WhatsApp and Facebook groups, Hinjewadi/Wakad (operator posts "move-out sale? list here" in groups where posting is allowed) | 40 groups x ~300 members = ~12,000 [ASSUMPTION: group counts and sizes unknown] | 0.2% posting-to-paid [ASSUMPTION] | ~24 | Groups named as active in C02 (affiliate blog) |
| Instagram local posts / reels about move-out sales (user skill K3) | ~20,000 impressions over 8 weeks [ASSUMPTION] | 0.15% [ASSUMPTION] | ~30 | No Pune Instagram data found |
| Flyers/QR on society notice boards at lease-end clusters | 30 societies [ASSUMPTION] | 1 seller per society per month for 2 months | ~60 gross? counted at 30 [ASSUMPTION] | no data |
| Broker/PG-owner referral (₹50 referral per paid listing) | 15 brokers [ASSUMPTION] | 2 listings each | ~30 | brokers are noted as in the rent-agreement channel in 02-signals.md#C03 (not for resale) |
| Total (summed) | | | ~84-120 | all conversion rates ASSUMPTION |

- Seller count is bounded by buyers: a board with no visible buyer demand gets no sellers. Buyer side must be built first: 300-500 community members before charging (ASSUMPTION; threshold untested). Buyer acquisition uses the same channels above.
- Time to first rupee: seller listings can be charged in week 3-4; inside the K6 limit of 3 months only if the buyer community reaches threshold by about week 3 (ASSUMPTION).
- Sourced numbers in this table: none. The table is a plan to be tested, not an estimate with evidence.

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| OLX (general classifieds) | https://www.olx.in/blog/expert-advice/how-much-does-olx-advertisement-cost/ | Free basic listings with category limits; paid boosts (amounts not retrieved) | Curated, move-out-dated, micro-local; costs sellers ₹199 where OLX is free | [C08]; difference is a hypothesis |
| Quikr | https://www.quikr.com | Free listing with limited exposure; premium credit packs (prices not retrieved) | Same as OLX | listing roundup, https://www.geeksforgeeks.org/?p=1081750 (not read in full) |
| Facebook Marketplace and society WhatsApp/RWA groups | https://www.facebook.com/marketplace | Free | Same; free groups already active in Hinjewadi/Magarpatta townships per affiliate blog | [C02] |
| Local used-furniture dealers (Pune) | none found (no named dealer with URL) | Cash on pickup at below private-sale prices (no figures) | Seller keeps more of sale price; slower than a dealer | [C03] |
| Rentomojo (rental alternative for buyers) | https://www.rentomojo.com | Furniture plans from ₹2,199/month; fridge about ₹600/month (Pune, press release) | Buyer owns item; no recurring payment; no delivery or warranty | [C05], [C06] |
| Furlenco, Cityfurnish (rental) | https://furlenco.com ; https://www.cityfurnish.com | Prices not found | Same as Rentomojo | https://theprint.in/brandit/furniture-rental-market-reshapes-how-young-pune-sets-up-home/3070253/ (search summary only; fetch failed) |

## Moat over time
- None yet. A WhatsApp community list of local buyers and a record of past listings could become a local audience that sellers cannot get from OLX, but members can be copied to other groups and the community sits on a platform the operator does not control (ASSUMPTION). Network effect is single-neighbourhood and weak. Incumbents and free alternatives can match the feature at no cost.

## Assumptions
- [C10] Sellers will pay ₹199 for a listing when OLX and Facebook are free. [ASSUMPTION: no evidence found; this is the core untested claim]
- [C11] Enough move-outs occur in one micro-cluster each month to produce 10-20 listings a week. [ASSUMPTION: no Pune move-out or churn data found]
- [C12] Buyers prefer buying used over renting from Rentomojo/Furlenco/Cityfurnish for a meaningful share of arrivals. [ASSUMPTION: contrarian bet in the raw idea; untested]
- [C13] A WhatsApp Community with 300-500 members can be built in 3-4 weeks via society groups and Instagram. [ASSUMPTION: no Pune channel data]
- [C14] Operator can run listings by hand at 10 h/week alongside a full-time job (K2, K9). [ASSUMPTION: about 20-30 minutes per listing]
- [C15] No licence is needed to operate a classifieds listing board; Shops and Establishments registration status and consumer e-commerce/intermediary rules are unresolved. [ASSUMPTION: 01-local-market.md#C18 shows sources conflict; GST not researched]
- [C16] Collecting seller phone numbers and photos brings DPDP obligations (notice, consent, erasure) (national, vendor commentary). [source: https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/]
- [C17] WhatsApp Community/Business limits and Meta policy on commercial use of groups may restrict a paid board; terms not checked. [ASSUMPTION: platform risk]
- [C18] Resale values (30-60% recovery) are taken as plausible; sources are commercial blogs. [ASSUMPTION]
- STRETCH USED: none. K4 freelancer hiring not needed.
