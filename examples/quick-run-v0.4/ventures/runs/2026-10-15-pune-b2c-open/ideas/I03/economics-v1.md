---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: economics-modeler
version: 1
created: 2026-10-15T10:41:49Z
---

## Inputs
Currency: INR (contract currency). No conversions used. Search tools returned snippets only; pages were not opened except where noted. Confidence is low on every cost line.

- [C01] Price anchor, high: Urban Company Pune apartment deep clean from Rs 3,199 unfurnished and Rs 3,499 furnished (Koregaon Park page) [source: https://www.urbancompany.com/pune-professional-home-cleaning-meera-nagar-koregaon-park, via forge-v1.md#C01]
- [C02] Price anchor, low: Urban Company Deccan Gymkhana page shows Rs 2,999 unfurnished and Rs 3,199 furnished [source: https://www.urbancompany.com/pune-home-cleaning-services, via forge-v1.md#C02]
- [C03] Small-provider anchor: Ghare Facility Cleaning lists Rs 6-7 per sq ft; IndiaMART Pimpri Chinchwad lists Rs 7-8 per sq ft. At 500-700 sq ft this gives about Rs 3,500-5,600 [source: https://dir.indiamart.com/pimpri-chinchwad/deep-cleaning-services.html, via forge-v1.md#C03, C04]
- [C04] Conservative price used: Rs 2,999, the lowest sourced Pune app price. An unreviewed new entrant is assumed unable to charge above the incumbent's lowest locality price [ASSUMPTION: new entrant has 0 reviews against 339K-446K reviews on the incumbent, forge-v1.md#C01]
- [C05] Base price Rs 3,299 (between the two app tiers) and optimistic Rs 3,499 (the furnished-flat app price) [ASSUMPTION: price positioned at the app, not below it, per forge-v1 "How it makes money"]
- [C06] Team labour per job. No per-job deep-clean team rate found. Pune housekeeping pay is about Rs 15,000-20,000 a month, Rs 500-670 a day (search arithmetic) [source: https://apna.co/job/pune/housekeeping-staff-292065227, via forge-v1.md "How it makes money"]. Indeed lists Pune cleaning jobs at Rs 10,488-32,540 a month [source: https://in.indeed.com/explorer/high-paying-cleaning-jobs-pune,-mh]. Per-job team cost: conservative Rs 2,400, base Rs 2,000, optimistic Rs 1,700 [ASSUMPTION: a 2-person independent team for a 4-5 hour job (C01 durations) at Rs 800-1,200 per person per job, above salaried day rates because freelancers carry travel and idle days; the Generator's Rs 2,200 sits inside this range; unsourced]
- [C07] Consumables per job: conservative Rs 250, base Rs 200, optimistic Rs 150 [ASSUMPTION: no per-job figure found. Indicative start-up supply budgets of Rs 2,000-5,000 for floor/bathroom/glass cleaners and disinfectants exist, https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-rajasthan-cost-license-setup-guide and Rs 3,000-8,000 for chemicals, https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-uttar-pradesh-cost-license-setup-guide (other states, lender marketing); divided by an assumed 20-30 jobs per refill]
- [C08] Team travel per job: conservative Rs 200, base Rs 150, optimistic Rs 100 [ASSUMPTION: two riders within one Pune cluster, fuel or auto share]
- [C09] Payment fee: UPI to a bank account has 0% MDR; Razorpay charges a 2% platform fee on UPI via its gateway [source: https://razorpay.com/blog/upi-charges-explained-mdr-vs-platform-fees/ (vendor page)]. Conservative 2% of price, base 1% blended, optimistic 0% (direct UPI QR to a business account) [ASSUMPTION: split between gateway and direct UPI]
- [C10] Re-clean reserve: conservative 10% of jobs re-done at team cost, base 7%, optimistic 5% [ASSUMPTION: no failure-rate data for a new service; the incumbent's one-star share is about 2% (forge-v1.md#C13), which is a minimum for a team with no track record]
- [C11] Damage and theft reserve per job: conservative Rs 100, base Rs 75, optimistic Rs 50 [ASSUMPTION: self-insurance, no insurance priced (forge-v1.md#C22)]
- [C12] Meta (Facebook/Instagram) India CPC: one 2026 benchmark Rs 0.51-2.26; another Rs 3-12 depending on industry and targeting; lead generation for services Rs 200-2,000 per lead; sources conflict and are vendor marketing, none specific to home cleaning [source: https://upgrowth.in/facebook-advertising-pricing/ (via search summary); festive season CPM is 2-3x]
- [C13] Paid-ads funnel used for sensitivity only (ads are not in forge-v1's path): CPC Rs 12 / 6 / 3 (conservative / base / optimistic); click-to-WhatsApp enquiry 3% / 5% / 8%; enquiry-to-booking 25% / 35% / 40% [ASSUMPTION: CPC from the upper, mid and lower of the Rs 3-12 range in C12; conversion rates unsourced, forge-v1.md#C19 also has none]
- [C14] Organic channel yields per month (conservative / base / optimistic): Google Business Profile + Instagram 3 / 6 / 8 bookings; society and tenant groups 2 / 6 / 8; brokers 1 / 6 / 8; repeat and referral 0.5 / 2 / 4 [ASSUMPTION: forge-v1 path table is itself unsourced; base uses forge-v1 numbers (6 / 6 / 6 / ~2); conservative cuts them by 50-85%, optimistic raises them]
- [C15] Boosted-post spend for GBP/Instagram: Rs 3,000 a month in all cases [ASSUMPTION: small test budget]
- [C16] Broker referral fee per job: Rs 500 / 300 / 200 [ASSUMPTION: forge-v1 uses Rs 300, unsourced]
- [C17] Discount on first 10 network jobs (to collect photos and reviews): Rs 1,000 / 600 / 300 per job [ASSUMPTION: forge-v1 "first 10 jobs at a discount or at cost"]
- [C18] Referral reward for repeat/referral channel: Rs 300 / 200 / 100 per booking [ASSUMPTION]
- [C19] Equipment (vacuum, scrubbing kit, ladder, starter chemical stock): conservative Rs 17,000, base Rs 8,000, optimistic Rs 5,000. Indicative vacuum price Rs 3,000-12,000 plus supplies Rs 2,000-5,000 [source: https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-rajasthan-cost-license-setup-guide (other state, lender blog)]; conservative = top of both ranges
- [C20] Fixed monthly cost excluding ad spend (WhatsApp Business free, Sheets free, Instagram free, small misc): Rs 1,000 [ASSUMPTION: no tooling subscription; misc covers printed checklists, phone data]
- [C21] Launch overheads (Udyam, Shop Act, bank account, misc): conservative Rs 3,000, base Rs 1,500, optimistic Rs 1,000 [ASSUMPTION: Shop Act fees disputed across consultancy pages, https://www.patronaccounting.com/shop-act-registration/pune, 2026]
- [C22] Founder time per booking: 4 enquiries per booking at 10 min, plus 20 min scheduling, plus 30 min photo review and follow-up = about 1.5 h; fixed content and outreach 2 h a week [ASSUMPTION: forge-v1.md#C18 gives 30 min per job; enquiry handling added here]. Founder time is not costed (no salary drawn).
- [C23] Team recruitment and ramp time: conservative 8 weeks to first paid job, base 5 weeks, optimistic 3 weeks [ASSUMPTION: forge-v1 says team availability is the main supply risk and has no source]
- [C24] Regulatory exposure (Maharashtra Gig and Platform Workers Bill 2026, pending; aggregator definition not found) is not priced [source: https://teamleaseregtech.com/updates/article/57603/maharashtra-gig-and-platform-workers-rights-and-protection-bill-2026/, via forge-v1.md#C20]

## Scenarios
Per booking, one-time customer. No recurring revenue is modelled; forge-v1 says repeat is once or twice a year and no repeat data exists.

| metric | conservative | base | optimistic |
|---|---|---|---|
| price | Rs 2,999 | Rs 3,299 | Rs 3,499 |
| COGS per unit (team + consumables + travel + payment fee + re-clean + damage) | Rs 3,250 | Rs 2,598 | Rs 2,085 |
| gross margin % | -8.4% (Rs -251 per job) | 21.2% (Rs 701) | 40.4% (Rs 1,414) |
| CAC: friends and network, first 10 jobs (discount cost per job) | Rs 1,000 | Rs 600 | Rs 300 |
| CAC: Google Business Profile + Instagram (Rs 3,000 boost / bookings) | Rs 1,000 | Rs 500 | Rs 375 |
| CAC: society and tenant WhatsApp/Facebook groups (cash) | Rs 0 cash (time only) | Rs 0 cash | Rs 0 cash |
| CAC: broker and landlord referrals (fee per job) | Rs 500 | Rs 300 | Rs 200 |
| CAC: repeat and referral (reward) | Rs 300 | Rs 200 | Rs 100 |
| CAC: paid Meta ads, sensitivity only, not in forge path | Rs 1,600 | Rs 343 | Rs 94 |
| blended CAC, steady state excluding the first 10 network jobs | Rs 562 | Rs 260 | Rs 178 |
| payback period (months) | never (contribution per job is negative before CAC) | under 1 month (CAC Rs 260 is 37% of one job's Rs 701 margin) | under 1 month (CAC 13% of Rs 1,414) |
| break-even volume (jobs per month) | none at any volume | 3 | 1 |
| capital to first revenue | Rs 29,500 | Rs 17,500 | Rs 8,600 |
| months to first revenue | 2 | 1.5 | 1 |

Steady-state bookings per month (C14): conservative 6.5, base 20, optimistic 28. Conservative monthly result after fixed costs: about Rs -6,280.

## Calculations
Conservative column.

COGS per job:
- team 2,400 + consumables 250 + travel 200 = 2,850
- payment fee 2% x 2,999 = 60
- re-clean reserve 10% x 2,400 = 240
- damage reserve 100
- total = 2,850 + 60 + 240 + 100 = 3,250
- margin = 2,999 - 3,250 = -251 per job; -251 / 2,999 = -8.4%

Blended CAC (steady state, conservative bookings per month from C14):
- GBP + Instagram: Rs 3,000 / 3 bookings = Rs 1,000 each
- groups: Rs 0 cash, 2 bookings
- brokers: Rs 500 x 1 booking
- repeat/referral: Rs 300 x 0.5 booking
- total cash = 3,000 + 0 + 500 + 150 = 3,650 over 6.5 bookings = Rs 562 per booking
- network launch: 10 jobs x Rs 1,000 discount = Rs 10,000, one-off

Paid ads sensitivity (conservative): Rs 12 / (3% x 25%) = Rs 12 / 0.0075 = Rs 1,600 per booking. Implied cost per enquiry = 12 / 0.03 = Rs 400, inside the Rs 200-2,000 range in C12. At the top of that range (Rs 2,000 per lead, 25% close) CAC would be Rs 8,000. Not used as the conservative blended figure because the range covers all service categories, but it is the literal pessimistic end of the sourced range.

Contribution per job after blended CAC: -251 - 562 = Rs -813.

Break-even volume: contribution per job is below zero, so fixed cost Rs 1,000 a month is never covered at any volume. Payback is undefined.

Monthly result at 6.5 bookings: 6.5 x (-251) = -1,632; CAC cash -3,650; fixed -1,000; total = -6,282.

Capital to first revenue (conservative):
- equipment 17,000
- launch overheads 3,000
- one month of boost spend 3,000
- team float for 2 jobs paid before the balance is collected: 2 x 3,250 = 6,500 (advance covers part; full float shown as the pessimistic case)
- total = 17,000 + 3,000 + 3,000 + 6,500 = 29,500

Capital at risk at month 3 after first revenue: 29,500 + launch discounts 10,000 + 3 x 6,282 = about Rs 58,300. Month 6 is about Rs 77,000. Capital reaches Rs 1,00,000 at about month 9-10 if nothing changes.

Founder hours (conservative, 6.5 bookings a month): 6.5 x 1.5 h = 9.75 h; plus content 2 h x 4.3 weeks = 8.6 h; total 18.4 h a month = 4.3 h a week.

What would have to change: with price Rs 2,999 and CAC Rs 562, COGS must be at or below 2,999 - 562 = Rs 2,437, a cut of Rs 813 (25%) from Rs 3,250. Team cost alone would need to fall from Rs 2,400 to about Rs 1,600 (holding other lines; re-clean reserve also falls with it, so about Rs 1,650 in practice), a cut of about 30-33%. Alternatively price at Rs 3,812 (+Rs 813), above the incumbent's highest sourced furnished price of Rs 3,499 (C01). At Rs 3,499 with conservative COGS: 3,499 - 3,250 - 562 = Rs -313 per job after CAC. At team cost Rs 2,000 with every other conservative input held: COGS = 2,000 + 250 + 200 + 60 + 200 + 100 = Rs 2,810, margin Rs +189 before CAC and Rs -373 after the Rs 562 CAC.

Base check: COGS = 2,000 + 200 + 150 + 33 + 140 + 75 = 2,598; margin 3,299 - 2,598 = 701 (21.2%). Blended CAC = (6 x 500 + 6 x 0 + 6 x 300 + 2 x 200) / 20 = 5,200 / 20 = 260.

Optimistic check: COGS = 1,700 + 150 + 100 + 0 + 85 + 50 = 2,085; margin 3,499 - 2,085 = 1,414 (40.4%). Blended CAC = (8 x 375 + 0 + 8 x 200 + 4 x 100) / 28 = 5,000 / 28 = 178.

## Constraint check (conservative case only)
| K# | constraint | conservative value | result |
|---|---|---|---|
| K1 | capital Rs 1,00,000 HARD | Rs 29,500 to first revenue; about Rs 58,300 at month 3; reaches Rs 1,00,000 around month 9-10 if losses continue | fits (to first revenue and through month 3); losses continue every month |
| K2 | 10 hours a week HARD | about 4.3 h a week at 6.5 bookings a month; 10 h a week supports about 25 jobs a month (forge-v1 estimate) | fits |
| K3 | skills (have) HARD | spreadsheets, social media, languages; no cleaning skill needed (founder does not clean) | fits |
| K4 | skills (hire/learn) FLEXIBLE | no freelancer hired by the founder beyond per-job teams, already inside COGS | fits (no STRETCH USED) |
| K5 | low risk; cannot lose more than Rs 1,00,000 HARD | maximum loss stays under Rs 1,00,000 only if the founder stops by about month 9; conservative loss is certain, not probable, because margin per job is negative | fits on the cap only; the loss is certain in this case |
| K6 | first revenue within 3 months HARD | 2 months (8 weeks to team and first job, C23) | fits |
| K7 | B2C only HARD | household customers | fits |
| K8 | off-limits categories HARD | cleaning is not alcohol, gambling, crypto, MLM, food or medical licensed | fits |
| K9 | keeps full-time job HARD | weekend jobs; weekday on-site problems and key-holder access are not costed | fits (unverified) |

## Verdict inputs
- conservative unit economics positive: no (gross margin -8.4%, Rs -251 per job before CAC; Rs -813 per job after blended CAC)
- HARD constraints broken in conservative case: none broken on the contract's own terms (K1, K2, K6 fit); K5 fits only as a capped certain loss
- FLEXIBLE stretches required: none
- what would have to change for the conservative case to work: COGS must fall from Rs 3,250 to about Rs 2,437 (-Rs 813, -25%) at price Rs 2,999 and CAC Rs 562, which means a team cost near Rs 1,600-1,650 per job instead of Rs 2,400, or price near Rs 3,812 (+Rs 813), above any sourced Pune price. The per-job team rate (C06) is the unsourced number the result depends on most; a sourced per-job deep-clean team rate in Pune is the evidence that would settle it.
