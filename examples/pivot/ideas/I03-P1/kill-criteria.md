---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03-P1
agent: main
version: 1
created: 2026-10-15T16:05:00Z
locked: true
---

## Raw idea
### I03-P1
- pitch: A WhatsApp-community resale board for tenants leaving IT-corridor flats in Pune, where the seller pays a 10% commission on each completed sale and listing is free. It holds no inventory and sells used furniture and appliances locally.
- customer: Individual departing tenants (sellers) in Pune IT-corridor flats (Hinjewadi, Wakad, Baner, Kharadi, Viman Nagar, Magarpatta), who pay. Incoming tenants are the free demand side and do not pay.
- problem: A departing tenant has used furniture and appliances to sell on a fixed move-out date and no dedicated local channel; an arriving tenant faces a large upfront furnishing cost. Severity on the seller side is not evidenced for Pune (see Problem severity).
- revenue model: 10% commission on each completed sale, paid by the seller through a UPI collect link after handover; listing is free.
- lens: contrarian
- signal ids: L01, L03
- pivoted from: I03
- pivot reason: revenue model changed (₹199 one-off seller listing fee, optional ₹99 featured upgrade → 10% commission on each completed sale, listing free). Forge-v2 declared `pivot declared: no`; the main session detected the change by comparing Core identity in forge-v1.md and forge-v2.md (rule 5).

## Market criteria
### KM1
- dies unless: there is demand evidence that people in India already pay for, or actively transact in, used furniture and appliances through an intermediary, shown by at least 3 operators or platforms (for example refurbished-goods sellers, buy-back services, classifieds) with documented paying customers or transaction volume.
- threshold: at least 3 named operators, each with one verifiable revenue, GMV, listing-count or customer-count figure dated 2024-01-01 or later; at least 1 of them operating in Pune.
- evidence that satisfies it: company filings or press coverage with revenue or volume figures, public listing counts for Pune on classifieds platforms, funding or Tracxn-type profiles with revenue.
- why it matters: Rule 3 needs existing spending or revenue on a comparable solution, not only a claim that tenants have furniture to sell.

### KM2
- dies unless: the typical used item sold in Pune IT-corridor areas is priced high enough for a 10% commission to be worth collecting.
- threshold: median asking price of used furniture and appliances listed in the six named areas is at least ₹3,000 (10% = ₹300), measured over at least 50 current or last-90-day listings.
- evidence that satisfies it: a counted sample of public Pune listings (OLX, Facebook Marketplace, Quikr, society or Reddit posts) with prices, or published resale-price data for Pune.
- why it matters: at a median under ₹3,000 the commission is below ₹300 per sale, too small to cover payment-collection effort and chasing.

### KM3
- dies unless: there is evidence that sellers of used goods will pay a seller-side commission or fee, and that the free substitutes (OLX, Facebook Marketplace, society WhatsApp groups, brokers, kabadiwalas, giving items to the landlord or incoming tenant) do not already serve this need at zero cost.
- threshold: at least 1 commission or seller-fee used-goods intermediary in India that has operated 24 months or more with paying sellers, and no more than 1 documented closure of a comparable peer-to-peer resale commission business in India attributed to sellers bypassing the platform or refusing fees.
- evidence that satisfies it: operator fee pages and operating history, plus shutdown reports or founder post-mortems from the Indian resale graveyard.
- why it matters: a payment taken only after handover, in a free-listing market, is the point where commission models for low-ticket goods usually leak.

### KM4
- dies unless: the pool of departing IT-corridor tenants is big enough to reach a viable monthly volume.
- threshold: evidence of at least 20,000 renter households per year turning over across Hinjewadi, Wakad, Baner, Kharadi, Viman Nagar and Magarpatta combined (so that 1% capture is at least 200 sales a year), derived from stated renter share, tenure and household counts.
- evidence that satisfies it: census or housing-portal data on renter households, IT-employee counts per area with a stated rental share and average tenure, or co-living and rental operator figures for these areas.
- why it matters: the revenue is a small share of a small ticket, so the pool must be large; local data is currently thin (coverage score 3 in 01-local-market.md).

### KM5
- dies unless: departing-tenant sellers in Pune show a pain that free channels fail to fix, so a paid, commission-based board has a reason to exist.
- threshold: at least 20 distinct public posts, reviews or complaints dated 2025-10-15 or later from Pune tenants trying to sell or dispose of move-out furniture or appliances, of which at least 5 report failure (no buyers, no-shows, lowball offers, items left unsold or dumped).
- evidence that satisfies it: Reddit, Facebook group, Quora, Google review or news posts from Pune, collected with links.
- why it matters: 02-signals.md has no seller-side Pune complaint data, and the pivot itself admits that seller-side severity is not evidenced for Pune.

## Execution criteria
### KE1
- dies unless: the full operating load of the board (recruiting sellers and buyers, vetting and posting listings, coordinating handovers, collecting the commission by UPI link) fits within 10 hours/week (K2, HARD, no stretch) at the volume needed to reach first revenue, and the capital needed to reach first commission income is at most ₹1,00,000 (K1, HARD) including any freelancer, tool, WhatsApp Business/API and promotion costs.
- threshold: at most 10 hours/week total, with no more than 1.5 hours of founder time per completed sale at the break-even volume; capital to first revenue at most ₹1,00,000, with the conservative case at or below ₹60,000 so that losses stay within K5 (cannot lose more than ₹1,00,000).
- evidence that satisfies it: a week-by-week hours budget and a cost table (tools, group/API fees, paid promotion, freelancer rates) with sourced prices; per-sale handling time derived from a comparable local resale or listing operation or from a stated, reasonable ASSUMPTION; the monthly volume of completed sales that makes the hours fit.
- why it matters: the contract has HARD limits on hours and capital, and a manually brokered resale board is labour-linear per sale.

### KE2
- dies unless: the first commission is collected within 3 months of today (by 2027-01-15; K6, HARD) with a realistic path to enough completed sales to pay for the founder's time and costs, and the commission is actually collectable once buyer and seller meet.
- threshold: at least 1 paid commission by 2027-01-15; the plan must state the expected completed-sale count and average sale value, and show the commission collection rate (share of completed sales on which the 10% is paid) at or above 60% in the conservative case.
- evidence that satisfies it: a timeline from group creation to first listings to first completed sale; evidence on how comparable local classifieds or resale groups handle payment (escrow, platform-collected payment, or pay-after-handover); a described enforcement mechanism that does not rely on goodwill, such as the platform taking payment from the buyer and releasing the net amount to the seller; a worked example showing commission per sale in ₹ against the hours in KE1.
- why it matters: the revenue model is a 10% commission payable after handover with free listing, so the seller can complete off-platform and not pay, and the time limit leaves little room to learn that late.

### KE3
- dies unless: the board has a defensible reason for a departing tenant to use it instead of free incumbents (OLX, Facebook Marketplace and Facebook/WhatsApp Pune buy-sell groups, Quikr, rental companies' own refurbished-sale channels, and informal sale to the next tenant through the flat owner, broker or society), and that reason survives the incumbents' likely response of staying free or adding a local-move-out feature.
- threshold: at least 3 named incumbent channels used by Pune tenants for used furniture and appliances, each with its price (expected ₹0 for listing) and its stated terms; a named difference (trust, speed, pickup, price floor) that justifies a 10% fee against ₹0 alternatives; and a stated response if a free competing WhatsApp group appears in the same housing society or area.
- evidence that satisfies it: competitor listing pages and fee schedules with URLs; evidence of Pune used-furniture activity on those channels (listing counts, pricing); evidence of a trust or convenience gap that departing tenants would pay about 10% to close, for example commission or convenience fees already paid on resale or pickup services.
- why it matters: both sides can already trade free, and a WhatsApp group has no switching cost or technical barrier to copy.

### KE4
- dies unless: the legal and tax obligations of running a commission-earning marketplace for used goods in Pune are identified, can be met at a cost within the capital in KE1, and need no licence excluded by K8.
- threshold: a checked list covering at least (a) GST registration and GST on commission income, and whether the Central GST rules on e-commerce operators apply to a WhatsApp-based intermediary, (b) the Consumer Protection (E-Commerce) Rules, 2020, including any grievance officer, seller-information and liability duties for a marketplace entity, (c) Maharashtra Shops and Establishments registration (research C18 shows sources conflict), (d) DPDP Act consent, notice and erasure duties for holding phone numbers and listings (C19), and (e) any rules on second-hand goods or electronics (for example e-waste or product-safety exposure for used electrical appliances). Total compliance cost at most ₹15,000 in year one, and no requirement for a food-safety or medical licence.
- evidence that satisfies it: primary or professional sources (CBIC or GST portal, Ministry of Consumer Affairs, Maharashtra Labour Department, MeitY) with dates, plus a cost estimate for registration and any accountant fees; a statement of liability if a buyer is injured by a faulty used appliance, and the insurance or terms-of-service mitigation and its cost.
- why it matters: taking a percentage of sales can make the founder a marketplace or intermediary under Indian tax and consumer law, and the local research says GST, e-commerce rules and sector rules were not researched for any category.

### KE5
- dies unless: the platform and channel risk is bounded, meaning the business can survive a change in WhatsApp's community or group terms, Meta messaging charges, or a ban of the group, and the supply of listings (the harder side) does not rely on a single channel the founder cannot control.
- threshold: the plan names at least 2 channels for acquiring sellers (such as housing society groups, PG/co-living operators, brokers, social posts) with sourced reach or cost evidence; shows what WhatsApp group size, community and business-messaging terms apply and what a ban or terms change would cost; and holds recurring messaging cost at or below 10% of average monthly commission income in the conservative case (WhatsApp India marketing message rate about ₹0.86 to ₹1.09 per message, 02-signals S01).
- evidence that satisfies it: WhatsApp and Meta Business or Community policy pages and pricing pages (with dates); evidence of the member limits and reporting/ban terms for commerce use; a seller-acquisition plan with unit costs; a back-up channel (own contact list, Instagram, a simple web listing) and what it costs.
- why it matters: the whole product lives on a platform the founder does not control, the local research found no Pune data on channel costs or seller reach, and the venture is a two-sided board that fails if either side is too thin in the move-out window.

## Lock
- locked at: 2026-10-15T16:05:00Z
- note: hash is recorded in run-log.md, not in this file
