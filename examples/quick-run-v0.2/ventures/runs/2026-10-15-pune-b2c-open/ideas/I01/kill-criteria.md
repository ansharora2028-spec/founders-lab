---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: main
version: 1
created: 2026-10-15T09:28:02Z
locked: true
---

## Raw idea
### I01
- pitch: WhatsApp-based service that drafts and files e-commerce refund and complaint cases for Pune shoppers, flat ₹199 per case.
- customer: individual Pune online shoppers with an unresolved refund, wrong-item or subscription-trap dispute (they pay).
- problem: e-commerce is about 29% of National Consumer Helpline grievances and refund disputes are a large share of them, but a consumer has to work out the right escalation path, wording and evidence alone. The free helpline already exists, so the paid value is only in the drafting, the follow-up reminders and the paperwork. That is the weak point of this idea.
- revenue model: ₹199 flat fee per case, paid by UPI up front. Optional ₹99 add-on for a second escalation letter.
- lens: cheap-now
- signal ids: S01, S02, S09, S04
- platform dependency: relies on a third-party LLM API for Hindi, Marathi and English drafting (S09, prices conflict between sources) and on WhatsApp for delivery. The free National Consumer Helpline is the main substitute. The 2027-01-01 dark-pattern rules (S02) may raise complaint volume, but this is not established.

## Market criteria
### KM1
- dies unless: there is demand evidence that people already pay for help drafting or filing consumer complaints, refund claims or legal notices against online sellers.
- threshold: at least 3 distinct paid services (startups, legal-notice platforms, CA/lawyer marketplaces or freelancers with public price lists) operating in India, each showing a price of ₹99 to ₹999 per complaint or notice, or showing revenue, reviews or testimonials from paying customers dated 2024-10-15 or later. At least 1 must serve Pune or offer remote service to Pune. National services must be labelled (national).
- evidence that satisfies it: live pricing pages, app-store or Google Business review counts with dates, funding or revenue disclosures, archived pages.
- why it matters: Rule 3 demand evidence. Without any existing spend on a worse solution, ₹199 per case is a guess.

### KM2
- dies unless: the free substitutes (National Consumer Helpline 1915 / INGRAM, e-Daakhil, platform grievance officers, bank chargeback) fail often enough that consumers have a reason to pay.
- threshold: a sourced figure showing at least 20% of e-commerce grievances at the NCH or a state consumer commission are unresolved, rejected or time out, OR at least 2 independent sources showing consumers hiring paid intermediaries because the free route failed.
- evidence that satisfies it: Department of Consumer Affairs data or annual report, NCH convergence statistics, press analyses citing official data, consumer-forum studies.
- why it matters: the idea's own pitch concedes the free helpline exists. If the free route resolves most cases, the paid layer has no job.

### KM3
- dies unless: the Pune addressable volume of disputes can reach a viable paid volume.
- threshold: a sourced and shown estimate (Pune or Maharashtra online-shopper count times dispute incidence, labelled by geography) that at 5% or lower capture yields at least 1,000 paid cases per year in Pune. At ₹199 this is about ₹1.99 lakh per year of gross revenue.
- evidence that satisfies it: NCH state-wise e-commerce grievance counts for Maharashtra, online-shopper penetration data for Pune or Maharashtra, survey data on share of orders that have disputes.
- why it matters: at ₹199 per case, small volumes cannot cover the LLM, WhatsApp and payment costs or the founder's 10 hours per week.

### KM4
- dies unless: consumers will pay at this price relative to what is at stake.
- threshold: a sourced median or typical disputed e-commerce order value of at least ₹1,000 (so the fee is at most 20% of the amount recovered), AND at least 1 example of Indian consumers paying ₹199 or more for a comparable low-ticket document or legal service (for example a legal notice, RTI filing or rental agreement draft).
- evidence that satisfies it: NCH refund and complaint values (for example total refunds divided by complaint count), platform price listings of comparable services, order-value data.
- why it matters: many e-commerce disputes concern small orders, and a ₹199 fee on a ₹300 refund is unlikely to be paid.

### KM5
- dies unless: the graveyard shows this model is not already dead for demand reasons.
- threshold: a documented search (at least 5 distinct queries listed) that finds the fate of at least 3 comparable ventures (consumer-complaint or refund-recovery services in India or another emerging market). No more than 1 of them may have shut down or pivoted away because of low willingness to pay, poor unit economics or free-substitute competition.
- evidence that satisfies it: shutdown or pivot announcements, founder post-mortems, Tracxn or CB Insights status pages, news reports with the stated cause.
- why it matters: 01-local-market found no Pune consumer failure analysis from 2023 to 2026. This criterion forces the graveyard to be searched rather than assumed empty.

### KM6
- dies unless: there is a timing reason why demand is rising now and not three years ago or three years from now.
- threshold: confirmation from an official source (Gazette, DoCA or PIB) that the Consumer Protection (E-Commerce) (Amendment) Rules, 2026 take effect 2027-01-01, AND an official or credible year-over-year series showing e-commerce grievances at the NCH grew in at least 2 consecutive years.
- evidence that satisfies it: gazette notification, PIB release, DoCA annual grievance statistics for 2023, 2024 and 2025.
- why it matters: the stated timing signals (S01, S02) come from press and vendor summaries, and no source in the inputs establishes a trend. A flat grievance count and rules that bind sellers rather than consumers give no new reason to pay now.

## Execution criteria
### KE1
- dies unless: a working first version (WhatsApp intake, LLM drafting in English/Hindi/Marathi, payment collection, case tracking in a spreadsheet or no-code tool) can be built and run for the first 3 months within the HARD contract limits (K1, K2, K3/K4, K6).
- threshold: total spend to first paid case and through month 3 of ≤ ₹60,000 of the ₹1,00,000 capital (leaving ≥ ₹40,000 reserve under K5); founder time ≤ 10 hours/week including case handling at 20 cases/week; first paid case within 3 months; no skill required beyond spreadsheets, social media marketing, no-code, or freelancers paid inside the ₹60,000.
- evidence that satisfies it: itemised cost build-up (WhatsApp BSP/API fees incl. 18% GST, LLM API cost per case, no-code tooling, freelancer quote, Razorpay/UPI fees) from vendor pricing pages; an hours-per-case estimate with a stated review step per case.
- why it matters: tests the contract's capital, hours and time-to-revenue limits directly; manual case follow-up scales hours linearly with volume.

### KE2
- dies unless: the service can legally be sold by a non-lawyer to consumers in India without being unauthorised practice of law.
- threshold: a documented position that the offering (drafting complaint text, escalation letters, filing help) falls outside "practice of law" under the Advocates Act, 1961, or can be run within it (for example, a tool that helps the consumer draft and file their own complaint, with no legal advice and no legal-notice drafting on the customer's behalf), at no more than ₹15,000 of the ₹1,00,000 capital for any lawyer review, registrations or insurance.
- evidence that satisfies it: Advocates Act s.29/33 text and case law on non-advocate drafting; Consumer Protection Act 2019 and e-Daakhil rules on who may file or represent; a live Indian paid service (for example RegisterKaro-type providers) operating the same offer, with evidence of its structure; a written lawyer opinion costing within the ₹15,000.
- why it matters: Supreme Court case law (Bar Council of India v. A.K. Balaji, 2018) treats the test as substance over label, so a ₹199 "legal letter" product carries a prosecution or Bar Council complaint risk that has no cap under K5 [source: https://itatonline.org/digest/bar-council-of-india-v-a-k-balaji-and-others-air-2018-sc-1382/]. Applicability to domestic non-lawyers is not settled in that source.

### KE3
- dies unless: the paid layer survives the free substitutes and the platforms' reaction.
- threshold: at least 3 named free or cheaper substitutes (National Consumer Helpline, e-Daakhil, platform grievance officers, paid filing services such as RegisterKaro, general chatbots) are mapped, and the service has one specific, buyer-visible job none performs at ₹199 or less (for example, escalation in Marathi/Hindi with evidence bundling and follow-up). If any free substitute already does drafting, the criterion fails. Also dies if the 2027-01-01 e-commerce rules (S02) or the NCH's own tooling are credibly expected to add drafting or chat assistance within 12 months.
- evidence that satisfies it: feature and price comparison with URLs; the NCH and e-Daakhil feature pages; any announced roadmap; ChatGPT/Gemini free-tier test results on a sample refund dispute.
- why it matters: the idea itself concedes the free helpline is the main substitute; a general LLM that the customer can use free is a second one, and the incumbents control the escalation path.

### KE4
- dies unless: the delivery stack has no single platform dependency that can end the business or push costs past contract limits.
- threshold: unit cost per case (WhatsApp conversation fees with GST, LLM tokens, payment gateway fee of about 2% plus GST, and founder minutes at a ₹0 labour-value assumption) ≤ ₹60 of the ₹199 fee (≥ 70% gross margin) in the conservative scenario; a fallback channel exists (SMS/Telegram/web form) if WhatsApp Business policy or rates change; Meta's Business Messaging policy does not prohibit paid legal or complaint services.
- evidence that satisfies it: Meta WhatsApp Business pricing page and Commerce/Business policy text; LLM vendor pricing pages (the signals file notes conflicting figures); payment gateway fee schedule; a worked per-case cost.
- why it matters: WhatsApp rates and policy, LLM prices and payment-gateway terms are all set by third parties, and the signals file records conflicting prices [source: https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing].

### KE5
- dies unless: the data-handling and consumer-law obligations can be met inside the budget.
- threshold: the service stores order screenshots, phone numbers, addresses and payment details of Pune consumers. A privacy notice, consent capture, retention rule and a deletion process are achievable for ≤ ₹10,000 now, and the DPDP duties (core obligations from about 2027-05-13) do not require a dedicated officer, audit or breach-reporting system beyond what a one-person operator can run. Any refund-guarantee or "we will get your money back" claim must be avoided or shown lawful under the 2026 E-Commerce Rules and Consumer Protection Act advertising rules. GST registration is not required before month 3, or its cost is inside the budget.
- evidence that satisfies it: DPDP Rules text on small-fiduciary obligations; Maharashtra Shops and Establishments and GST thresholds from official portals; a template privacy notice.
- why it matters: a service whose input is dispute evidence holds sensitive personal data, and penalties are large against a ₹1,00,000 loss ceiling [source: https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/].

### KE6
- dies unless: a successful Pune pilot does not collapse into copy, saturation or unmanageable operations.
- threshold: the idea has a defensible reason why a funded legal-tech startup or an existing paid filing service cannot match ₹199 per case in Pune within 6 months of the founder's launch, and the founder can handle 100 cases per month in ≤ 10 hours/week by templating, otherwise price or automation must rise without exceeding the K1 budget.
- evidence that satisfies it: named competitor pricing and funding; an operating-time model with minutes per case; evidence that any incumbent charging more than ₹199 per case would not cut price.
- why it matters: a thin drafting layer has no technical barrier and customers have no repeat need, so growth requires constant acquisition effort inside the 10-hour cap.

## Lock
- locked at: 2026-10-15T09:28:02Z
- note: hash is recorded in run-log.md, not in this file
