---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: forge
version: 1
created: 2026-10-15T09:28:59Z
---

## Core identity
- customer: individual online shoppers living in Pune (B2C, they pay) with an unresolved e-commerce refund, wrong/defective-item or return dispute against a large platform (Amazon, Flipkart, Myntra, Swiggy Instamart, Blinkit and similar), where the platform's own in-app support has already failed once.
- problem: the shopper has to work out the escalation sequence (in-app support, platform Grievance Officer, National Consumer Helpline, then consumer commission), the wording, and the evidence bundle alone. Stated plainly: the escalation channels are free, so the paid value is limited to drafting, evidence organisation, deadline reminders and language (English/Hindi/Marathi).
- revenue model: ₹199 flat fee per case, paid by UPI before work starts; optional ₹99 add-on for a second escalation letter. No success fee, no subscription.
- pivot declared: no

## Persona
- [C01] Persona: a Pune salaried IT or services employee or postgraduate student, aged roughly 22–40, who buys online several times a month and pays by UPI. Pune is cited at about 1.86% of national UPI volume in April 2026 (single aggregator); Maharashtra is the largest UPI state. [source: https://factodata.com/state-wise-upi-transactions-india/, 2026-06]
- [C02] Pune district per capita income is about ₹3.58 lakh, fourth in Maharashtra (one secondary news report). [source: https://www.thehitavada.com/Encyc/2026/3/10/per-capita-inconsistency.html, 2026-03-10]
- [C03] Where the persona goes today: the platform's in-app support, then the platform Grievance Officer by email (a guide states acknowledgement within 24 hours and resolution within 15 days under IT Rules 2021 Rule 3(2); the guide is an unofficial wiki, verify). (national) [source: https://righttoinformation.wiki/_export/xhtml/wrong-product-amazon-flipkart-refund-india]
- [C04] Free government route: the National Consumer Helpline runs on 1915, WhatsApp, SMS, email, app, UMANG and the INGRAM portal in 17 languages, forwarding complaints to convergence-partner companies. Cost to the consumer is not stated explicitly in the sources found. (national) [source: https://www.etvbharat.com/en/!bharat/national-consumer-helpline-refunds-rs-7-14-crore-to-consumers-in-two-months-enn25070406342]
- [C05] Paid route: a lawyer. One blog estimates ₹10,000 to ₹50,000 as a lawyer's fee range for a consumer matter (single blog, imprecise). (national) [source: https://lawsathi.in/?p=1278]
- [C06] Consumer-court route: complaints are filed online via e-Daakhil under the Consumer Protection Act, 2019, with a registered account. (national) [source: https://lawsathi.in/?p=1278]
- reasoning: no Pune-specific data on how many shoppers pay for help with refund disputes was found. The persona is inferred from national complaint data and Pune payment/income data.

## Narrowest wedge
- First product: a WhatsApp-delivered "refund escalation pack" for one situation only: a refund or return on a prepaid order of ₹1,500 or more that has been unpaid or rejected for more than 7 days, on Amazon, Flipkart or Myntra. The founder collects order ID, screenshots and a timeline through a WhatsApp Business chat or a Google Form, and delivers within 24 hours: (1) a Grievance Officer email, (2) an NCH complaint text with the facts filled in, (3) a dated follow-up checklist (reminders at day 3, 7, 15).
- Segment: Pune only at first, English and Hindi, Marathi added if requests appear.
- Scope exclusions: no food or medical product disputes (K8 licence line and S03 themes), no legal notices signed by the founder (see Assumptions on unauthorised legal practice), no representation before any commission.
- Minimum order value of ₹1,500 is a design choice: at a ₹199 fee a ₹500 refund is not worth paying for. [ASSUMPTION: the shopper compares fee to refund at risk; no data on this threshold]
- Drafting can be done by the founder using a template library and a low-cost LLM; no custom software needed (K3, K4, K2).

## Problem severity
- [C07] E-commerce accounted for 511,196 of 1,771,622 National Consumer Helpline grievances in 2025, about 29%. (national) [source: https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm]
- [C08] NCH reports facilitating refunds above ₹105 crore across 35 sectors for 25 April to 31 July 2026, through 166,189 refund grievances; e-commerce was the largest share with 100,466 complaints and more than ₹74 crore (ministry-sourced figures as reported, not audited). (national) [source: https://www.etvbharat.com/en/!bharat/national-consumer-helpline-refunds-rs-7-14-crore-to-consumers-in-two-months-enn25070406342]
- [C09] Average implied refund per e-commerce grievance in that period is about ₹7,400 (₹74 crore / 100,466). [ASSUMPTION: arithmetic on C08; refunds recovered may not equal complaints filed, and averages hide a skewed distribution]
- [C10] E-Commerce (Amendment) Rules 2026 take effect 2027-01-01, make dark-pattern compliance mandatory and require NCH convergence. (national) [source: https://www.moneylife.in/article/new-ecommerce-rules-to-rein-in-dark-patterns-misleading-listings-and-hidden-charges-from-1st-january/81643.html]
- [C11] Users on a forum report Amazon support giving timelines and not following up, which points to escalation routes outside the app. Anecdotal, one forum, other city (Trivandrum thread). (other city: Trivandrum) [source: https://techenclave.com/t/amazon-customer-support-is-awful-escalation-options-experiences/249194]
- reasoning: the pain is frequent nationally and the dollar value per case is meaningful. What the data does not show is that complainants pay for help when a free channel exists. The volume of NCH grievances is also evidence that the free channel is used without paid help.
- Pune-specific severity: no Pune complaint counts were found. Confidence in Pune severity is low.

## Path to first 100 customers
Target market: Pune. Every conversion rate below is an ASSUMPTION; no Pune conversion data exists. Sourced items are marked.

- [C12] Channel 1, Pune housing-society WhatsApp groups and society apps (founder posts a short problem-led message and a free "refund escalation checklist" PDF; founder joins via own society and friends). Reach: 40 groups x 150 members = 6,000 people. Of these, 10% see and read the offer = 600; 3% have a stuck refund within a month = 18 leads; 25% convert = about 4–5 customers per month. Pune society group use is not verified; the vendor claim is that societies run several WhatsApp groups each (not Pune data). [source: https://blog.ind.adda.io/2025/04/managing-community-whatsapp-groups/, 2025-04; all numbers ASSUMPTION]
- [C13] Channel 2, Instagram Reels and carousels in English/Hindi ("Amazon refund stuck for 10 days? Here is the order of escalation"), organic, founder has social media marketing skill (K3). Reach: 8 posts/month x 3,000 views = 24,000 views, 0.3% DM or click = 72, 10% convert = about 7 customers per month, but audience is not Pune-limited, so about 40% Pune = 3 Pune customers. [ASSUMPTION: all rates]
- [C14] Channel 3, college and IT-park WhatsApp/Telegram communities in Hinjewadi, Kharadi, Kothrud and Viman Nagar: 20 communities x 300 = 6,000 reach, 5% read = 300, 2% have a case = 6, 30% convert = about 2 per month. [ASSUMPTION: all rates]
- [C15] Channel 4, search: Google queries such as "Flipkart refund not received what to do" are likely competitive with law-firm blogs; no search-volume data was retrieved. Counted as 0 in the plan. [ASSUMPTION]
- [C16] Channel 5, referral from paid customers (₹50 credit): assumed 0.2 referrals per customer.
- Sum: roughly 9–12 paid cases per month across channels 1–3 plus referrals. 100 customers would take about 8–11 months, which exceeds K6's 3-month limit for volume, though not for first revenue. First revenue within weeks is plausible only if one early case is found through personal contacts. [ASSUMPTION: derived from the above assumed rates]
- Conclusion: the 100-customer target is not reached inside 3 months on these assumptions. The 3-month target should be read as first revenue plus about 25–35 customers. Founder time per case (drafting, follow-up) of about 30–45 minutes would be about 5–9 hours per week at 10–12 cases a week and would approach K2 (10 h/week) at 15 cases a week. [ASSUMPTION: time per case]

## Positioning vs named competitors
| competitor | url | their price | our difference | evidence |
|---|---|---|---|---|
| National Consumer Helpline (Govt of India) | https://consumerhelpline.gov.in | Cost not stated in sources found; operated as a public service | Free incumbent that accepts the complaint directly. We add drafting, evidence packaging, follow-up reminders and Marathi/Hindi/English hand-holding. No data that users want this | C04, C08 |
| Platform Grievance Officer (Amazon, Flipkart) | no URL verified; Flipkart address named in source: grievance.officer@flipkart.com | Free | Same: we only prepare the submission | C03 |
| LawSathi (online consumer complaint guide/service) | https://lawsathi.in/?p=1278 | Not retrieved | Unknown product scope; a content site with a service tie-in. Not compared | search result only |
| RegisterKaro consumer complaint service | https://www.registerkaro.in/consumer-complaint | Not retrieved (page fetch failed) | Legal-service seller; likely higher price and legal-notice orientation; unverified | search result only |
| Lawyer via marketplace (LawRato) | https://www.lawrato.com | 2016 report: ₹500 for a 30-minute phone consultation; lawyers set their own fees | We charge less per case but cannot give legal advice or sign notices | https://ts.yourstory.com/2016/02/lawrato (2016, dated) |
| Individual lawyer | n/a | ₹10,000–₹50,000 per one blog (imprecise) | Price gap is large; the gap exists because the product differs (representation vs drafting) | C05 |
| Self-service with free LLM chatbots (ChatGPT, Gemini) | n/a | Free tiers exist [ASSUMPTION: free tiers available as of 2026-10] | The main substitute for the drafting part of our value; our difference is a human-run process, local-language templates, reminders | ASSUMPTION |

## Moat over time
- None yet. A case library (which phrasing and escalation order produced refunds, by platform) could improve with volume, but outcomes would need to be tracked, and the cases are small in number. Platform behaviour changes, and the 2027-01-01 rules (C10) may shift which routes work. A Pune-specific review or referral base could form but is not a moat against free alternatives.

## Assumptions
- [C17] Pune shoppers will pay ₹199 for help on a problem where free channels (NCH, Grievance Officer) exist. [ASSUMPTION: the only support is that lawyers charge much more (C05); no direct evidence of willingness to pay at ₹199. This is the load-bearing assumption]
- [C18] A ₹1,500 minimum refund at stake is the point where the fee becomes rational for the customer. [ASSUMPTION: no data]
- [C19] WhatsApp is acceptable as the delivery and collection channel and complaint volume can be handled by one person at about 10–15 cases a week. [ASSUMPTION]
- [C20] Drafting complaint text and letters for a fee, without signing as an advocate or giving legal advice, is lawful without a licence. [ASSUMPTION: not researched; the Advocates Act position on non-lawyer paid drafting was not checked and should be verified before launch]
- [C21] LLM drafting cost per case is under ₹5. Prices listed at $0.05 per 1M input tokens for a small model, with conflicting figures across sources. (global) [source: https://benchlm.ai/stats/llm-pricing, 2026-09; inference: a case uses under 20,000 tokens, so cost is a fraction of a rupee even at the higher quoted price]
- [C22] Collecting order screenshots and personal data triggers DPDP duties from about 2027-05-13; before then, only minimal data handling and deletion after case closure are planned. (national) [source: https://www.mondaq.com/india/data-protection/1708164/digital-personal-data-protection-rules-2025-notified, 2025-11-13]
- [C23] UPI up-front payment and a refund-if-undeliverable policy keep payment risk low. [ASSUMPTION]
- [C24] Pune housing-society WhatsApp groups tolerate a service post by a resident. [ASSUMPTION: some societies prohibit commercial posts]
- [C25] The share of Pune shoppers with a stuck refund of at least ₹1,500 in any month is about 3%. [ASSUMPTION: no data]

## Fixes (round 2 only)
- none
