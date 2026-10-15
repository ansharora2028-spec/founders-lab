---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-execution
version: 1
created: 2026-10-15T09:26:57Z
---

## Criteria
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
