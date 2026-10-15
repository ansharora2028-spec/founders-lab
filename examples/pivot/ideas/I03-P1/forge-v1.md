---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: forge
version: 1
created: 2026-10-15T16:00:00Z
---

## Core identity
- customer: Individual departing tenants (sellers) in Pune IT-corridor rented flats, narrowed to two micro-areas for the first test: Hinjewadi/Wakad and Kharadi/Viman Nagar. The seller pays. Incoming tenants are the free demand side. (Same customer as raw idea I03-P1; narrowing only.)
- problem: A departing tenant has a fixed move-out date and used furniture and appliances to dispose of, with no dedicated local channel. Severity on the seller side is not evidenced for Pune (see Problem severity).
- revenue model: 10% commission on each completed sale, paid by the seller via UPI collect link after handover; listing free. (Same as raw idea.)
- pivot declared: no (I03-P1 is itself the declared pivot from I03; no further field changed)

## Persona
- [C01] Persona: a salaried IT/office worker or intern on a rented flat or PG in Hinjewadi, Wakad, Baner, Kharadi, Viman Nagar or Magarpatta, who bought or inherited a wardrobe, fridge, study table or similar and will leave on a known date. [source: https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399, 2026-06; promotional source, content from 01-local-market.md#C01]
- [C02] The arriving-side tenant is priced against Rentomojo rental from ₹2,199/month and an upfront home-setup cost the same promotional piece puts near ₹50,000. [source: same URL as C01, 2026-06; marketing claim]
- [C03] Where the seller sells today: OLX and Quikr as classifieds, Facebook Marketplace, Sulekha and JustDial for local buyers, local second-hand dealers for quick cash. Source is a single Pune resale-guide site with no independent data. [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1]
- [C04] Reported recovery on used furniture is 30-60% of original value; example: Nilkamal Freedom 2-door wardrobe ₹5,000-9,000 resale. Same guide site; estimates unverified. [source: https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1]
- [C05] Appliance resale: Cashify and similar (Selsmart, Digi2L, Zolopik) offer instant quote and free pickup in Pune areas including Hinjewadi, Wakad, Baner, per the same guide network; kabadiwalas pay less but are fastest. [source: https://knowledge.digirake.com/home-living/washing-machine/sell-old-washing-machine-pune?amp=1]
- [C06] Money spent today on the problem by the seller: classifieds listing is free (OLX revenue is advertising and optional paid boosts, indicative ₹150-₹500 for featured listings), so current spend is mostly the seller's time or a discount accepted from a dealer. [source: https://yespress.io/olx-india; indicative figure from search summary, not read on page]

## Narrowest wedge
- Product: one WhatsApp Community (or a set of WhatsApp groups) per micro-area plus a Google Form/Sheet for listings. Seller submits item, photos, ask price, move-out date. Operator posts the listing to the area group, matches buyers, and sends a UPI collect link for 10% after handover.
- Segment: furniture and large appliances (wardrobe, bed frame, fridge, washing machine, study table) from tenants in Hinjewadi/Wakad first. These are items where a dealer or Cashify discounts heavily or does not pick up, and where weight makes a same-building or same-area buyer valuable. [ASSUMPTION: bulky furniture is poorly served by Cashify-type electronics platforms; the guides in C05 cover appliances/electronics and no furniture buyback was found]
- First paid transaction is one completed sale with one 10% collect link. No inventory, no logistics. Delivery is arranged by the buyer.
- No licence needed: used household goods, not food, medical, alcohol or gambling (K8). [ASSUMPTION: Shops and Establishments registration and GST status for a commission business not verified; see 01-local-market.md#C18]

## Problem severity
- [C07] Direct evidence that Pune tenants find disposal painful: none found. The research covered by 01 and 02 has no Pune complaint-volume data on used-furniture disposal. [ASSUMPTION: stated as a gap, not a finding]
- [C08] Indirect evidence: rental furniture is marketed to IT-corridor tenants on the grounds that buying costs about ₹50,000; this implies buyers face high upfront cost, which is the demand-side pain. Promotional source. [source: same URL as C01, 2026-06]
- [C09] Indirect evidence: several resale guides exist for Pune furniture and recommend multi-platform listing and cleaning/photo effort, which suggests selling takes effort. Content-marketing pages, not user complaints. [source: https://knowledge.digirake.com/study-table/sell-old-study-table-pune?amp=1]
- [C10] Value at stake per sale is small: at 30-60% recovery (C04) and a ₹5,000-9,000 wardrobe, a 10% commission is ₹500-900. For a ₹2,000-4,000 study table or chair it is ₹200-400. [source: arithmetic on C04; inference: commission equals 10% of the C04 price range]
- Severity is rated: unproven. The seller-side pain is not documented in the run files.

## Path to first 100 customers
Definition: 100 sellers who each completed one paid sale (commission collected). Target market is Pune.

| channel | reach | conversion | customers | sourced or ASSUMPTION |
|---|---|---|---|---|
| Society and tenant WhatsApp/Telegram groups in Hinjewadi/Wakad/Kharadi (operator joins and posts) | ~60 groups x ~150 members = ~9,000 | ~1.5% list an item = ~135 listings | ~135 listings, ~45 completed (assumed 33% completion) | All ASSUMPTION. No Pune group-size or response data found. |
| Instagram/Reels geo-tagged posts for Pune movers (user has social media skill, K3) | ~20,000 impressions / month for 3 months | ~0.1% listing = ~60 listings | ~20 completed (33%) | ASSUMPTION; Pune social data not found (01-local-market.md channels table: unknown) |
| Flat-broker / PG-owner / co-living referral (leave-and-licence brokers see move-outs) | ~25 brokers or PG managers | ~30% refer 1 mover per month for 3 months = ~22 referrals | ~10 completed | ASSUMPTION; broker-based move-out visibility is plausible per C11 below |
| Offline: notices at society notice boards, with society permission | ~40 societies | ~1 listing per society per month x 2 months | ~15 completed | ASSUMPTION |
| Housing/PG portals | not used | — | 0 | Entry cost unknown (01#channels) |

- [C11] Rent-agreement and move-out processes in Pune run through agents who handle leave-and-licence PDFs, so agents see move-outs. [source: https://www.punekarnews.in/pune-how-to-spot-a-fake-rent-agreement-before-it-lands-you-in-trouble/, 2025-08; inference: agents have move-out visibility]
- Sum of the table: roughly 90 completed sales, with all rates assumed. Reaching 100 within 3 months is not supported by sourced numbers; the realistic first-test target is 10-20 completed sales and a measured completion rate.
- Main structural risk: commission leakage. After the match, buyer and seller can complete the sale off-platform and skip the 10%. The model relies on seller goodwill and on pre-commitment at listing. No sourced data on leakage rates in commission-based classifieds was found. [ASSUMPTION: leakage of 30-60% is plausible for a manual matchmaker with no escrow]
- Payment: UPI collect/payment link after handover; UPI volumes are 24.07 billion transactions in September 2026 (national), so the payment rail exists. [source: https://startuptalky.com/upi-transactions-september-2026/]
- WhatsApp: group posting by hand needs no Business API, so message-fee changes (S01 in 02-signals.md) do not apply at this scale. [ASSUMPTION: manual group posting; broadcast via API would incur per-message fees]

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| OLX India (classifieds) | https://yespress.io/olx-india | Free listing; optional featured listing indicative ₹150-₹500 | Hyper-local (one micro-area), curated by operator, matched to a move-out date; costs the seller 10% on success rather than a flat fee | Search-summary figure; no 2026 commission schedule found |
| Quikr | not opened; no URL | Not found | Same as OLX | No Quikr data found |
| Facebook Marketplace | not opened; no URL | Free (ASSUMPTION) | Same; operator vets buyers and handles price negotiation | Named in https://knowledge.digirake.com/wardrobe/sell-old-wardrobe-pune?amp=1 |
| Cashify and appliance buyback platforms | https://knowledge.digirake.com/home-living/washing-machine/sell-old-washing-machine-pune?amp=1 | Instant quote, free pickup; buyer margin not public | They cover appliances/electronics; furniture coverage not found. Our price is the buyer-to-buyer sale price with no dealer margin | Guide site, not company page |
| Local second-hand dealers and kabadiwalas | https://knowledge.digirake.com/home-living/washing-machine/sell-old-washing-machine-pune?amp=1 | Pay below resale; scrap value for kabadiwalas | Higher seller realisation, slower and uncertain | Guide site, unverified |
| Rentomojo (rental, demand-side substitute) | https://smb.irontontribune.com/article/Rent-Wardrobe-Fridge-and-Study-Table-in-Pune-Instead-of-Buying-in-2026-as-indian-rupee50000-Home-Setup-Costs-Push-IT-Corridor-Tenants-Toward-indian-rupee2199Month-Plans-From-Rentomojo/6a1e0669004597ee6ba14399 | From ₹2,199/month | Incoming tenant buys at 30-60% off new and owns the item; rental has no ownership but zero disposal burden | Promotional source |

## Moat over time
- None yet. A group membership base and a record of completed sales per micro-area could create a trust and liquidity effect (more buyers draw more sellers), but groups are copyable on WhatsApp and nothing prevents a seller or buyer from leaving the group. Local liquidity per micro-area is the only candidate that strengthens with scale; it is unproven. [ASSUMPTION]

## Assumptions
- [C12] Completion rate of listed items to sales is 33% in the first test. [ASSUMPTION: no marketplace completion data for Pune; set low to be conservative]
- [C13] Average sale price is ₹3,000-6,000, so average commission is ₹300-600. [ASSUMPTION: derived from C04's resale ranges, which are unverified]
- [C14] Sellers will pay 10% on a sale they can complete off-platform. [ASSUMPTION: no evidence; the largest load-bearing assumption]
- [C15] Operator time per completed sale is about 1.5 hours (posting, replies, matching, collect link). At ₹300-600 commission, this is ₹200-400 per operator hour. At 10 hours a week that supports about 6-7 sales a week at most. [ASSUMPTION: time estimate; inference from C13]
- [C16] Pune tenants join and respond in WhatsApp groups. [ASSUMPTION: no Pune data in 01 or 02]
- [C17] Used-furniture disposal is a pain strong enough to be solved by a service rather than a free OLX listing. [ASSUMPTION: unproven; see Problem severity]
- [C18] Society admins and group admins permit posting by a third party operator. [ASSUMPTION: none of the groups tested]
- [C19] A commission business needs no licence beyond a Maharashtra Shops and Establishments intimation and, if turnover requires, GST; unverified (01-local-market.md#C18 shows sources conflict). [ASSUMPTION]
- STRETCH USED: none.
