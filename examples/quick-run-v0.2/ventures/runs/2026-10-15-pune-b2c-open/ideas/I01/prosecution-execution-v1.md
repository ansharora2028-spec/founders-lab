---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-execution
version: 1
created: 2026-10-15T09:32:42Z
---

## Inputs read
- 00-contract.md
- 01-local-market.md
- 02-signals.md
- ideas/I01/kill-criteria.md (LOCKED)
- ideas/I01/forge-v1.md
- ideas/I01/economics-v1.md

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KE1 | NOT MET | economics-v1.md#C12, economics-v1.md#C15, economics-v1.md#C19, forge-v1.md Path to first 100 customers, C1, C2 | Cash spend passes (about ₹5,000 to first revenue vs ≤₹60,000). The hours test fails. The criterion requires ≤10 h/week including case handling at 20 cases/week. The documents' own per-case time is 30–45 min (forge-v1.md; economics-v1.md#C12), so 20 cases/week is 10–15 h/week for case work alone, before promotion (economics-v1.md#C15: 28 h/month = 6.5 h/week). Economics reaches "7.3 h/week" only at 4.75 cases/month (about 1 case/week). The cost build-up also omits BSP fees and WhatsApp message fees with GST (see FE4). |
| KE2 | INSUFFICIENT EVIDENCE | forge-v1.md#C20, economics-v1.md Constraint check K3/K5, E1, E2 | No documented position exists. Forge labels it an unresearched ASSUMPTION. No lawyer opinion, no live comparable provider structure, and no cost estimate are on file. My search did not settle whether paid non-advocate drafting is "practice" (E1). Not shown to be legal and not shown to be illegal. |
| KE3 | NOT MET | forge-v1.md Positioning table (free LLM row), forge-v1.md#C04, E3 | The criterion fails if any free substitute already does drafting. Forge itself names free ChatGPT/Gemini tiers as "the main substitute for the drafting part of our value", and the only difference claimed is human-run process, local templates and reminders, with no evidence anyone wants that. The NCH has announced an AI chatbot under NCH 2.0 (E3), a second route for the 12-month expectation test. Forge also did not retrieve prices for LawSathi or RegisterKaro, so the "at ≤₹199 none performs the job" comparison was not done. |
| KE4 | INSUFFICIENT EVIDENCE | economics-v1.md#C05, economics-v1.md#C06, 02-signals.md#S10, E4, E5 | Per-case variable cost passes: ₹23.4 conservative vs ≤₹60. Three parts are missing. (a) No fallback channel (SMS/Telegram/web form) is stated by forge or economics. (b) Meta policy: I found no named prohibition on legal or complaint services, but the policy reserves "regulated goods and services" to Meta's sole discretion and I saw only third-party mirrors, not the official text (E4). (c) Rates conflict across sources (₹0.78–₹1.10 marketing; ₹0.115–₹0.145 utility) and BSP platform fees are excluded from economics (E5). |
| KE5 | INSUFFICIENT EVIDENCE | forge-v1.md#C22, economics-v1.md#C09, 01-local-market.md#C23 | Forge plans "minimal data handling and deletion after case closure". No privacy notice, consent capture or retention cost is priced against ≤₹10,000. No analysis of DPDP small-fiduciary duties. Economics treats registration as an unverified ASSUMPTION (₹0–2,000). Forge's "refund-if-undeliverable" is not tested against advertising rules. |
| KE6 | NOT MET | forge-v1.md Moat over time, forge-v1.md Path to first 100 customers, economics-v1.md#C12, economics-v1.md Calculations | Forge states "None yet" for moat, so no defensible reason is given why a funded startup or existing filing service cannot match ₹199. The 100 cases/month in ≤10 h/week test fails on the documents' own inputs: 100 x 30–45 min = 50–75 h/month = 11.5–17.3 h/week before any promotion. Economics also shows loaded contribution of -₹61.92 per case in the conservative case. |

KM criteria: no comment. The market prosecutor owns them.

## Flaws
### FE1 — FATAL
- flaw: The idea cannot produce meaningful income inside the HARD 10 h/week cap (K2). At forge's per-case time, the hours cap limits case work to roughly 13–20 cases/week even if promotion took zero time. In the documents' modelled volume, income is about -₹404/month (conservative) and roughly +₹900/month (base, after ₹799 fixed cost; my arithmetic from economics-v1.md Calculations). The only way to scale is to leave the cap or raise price, and neither is allowed. Founder time valued at ₹250/h makes conservative contribution negative at any volume.
- evidence: [C01] Economics conservative cash result at 4.75 cases/month is -₹403.5/month, break-even 8 cases; loaded contribution -₹61.92 per case [source: economics-v1.md Calculations]. [C02] Forge: 100 customers take 8–11 months, which exceeds the 3-month window for volume [source: forge-v1.md Path to first 100 customers]. Economics says 21 months at conservative volume [source: economics-v1.md Calculations].
- what would fix it (FIXABLE only): n/a
- fix would change customer/problem/revenue model: yes (a fix needs a higher price or less founder time per case, that is a different revenue model)

### FE2 — FIXABLE
- flaw: The legality of a non-lawyer selling complaint and escalation-letter drafting for a fee is unresolved. Forge marks it an unchecked ASSUMPTION. The locked criterion's cited case (Bar Council of India v. A.K. Balaji, 2018) applies a substance-over-label test. The liability is uncapped, which conflicts with K5 (cannot lose more than ₹1,00,000) and low risk appetite.
- evidence: [C03] Forge: "Drafting complaint text and letters for a fee ... is lawful without a licence" is an ASSUMPTION, "not researched" [source: forge-v1.md#C20]. [C04] Section 33 of the Advocates Act bars non-enrolled persons from practising before courts or authorities; secondary commentary says drafting instruments and giving legal opinions fall inside the regulated zone for advocates, but does not settle the question for non-advocates [source: https://lawx.in/acts/section/65/586/5700].
- what would fix it (FIXABLE only): a written opinion from an Indian advocate (within the ₹15,000 cap in KE2) that a self-help drafting and filing-assistance service, with no advice and no legal-notice drafting, is outside "practice"; or a live paid Indian service with the same offer and evidence of its structure. Partly desk-researchable (statute, case law, comparable providers). The opinion needs a paid lawyer.
- fix would change customer/problem/revenue model: no

### FE3 — FATAL
- flaw: The paid layer is a thin wrapper over free alternatives. Free general LLM tiers do the drafting. The government helpline accepts complaints directly through WhatsApp, 1915 and an app, and has announced an AI chatbot. Forge's differentiation (human-run process, templates, day 3/7/15 reminders) is a calendar reminder plus a template, which has no technical barrier, and the customer has no repeat need. Forge's own file says no evidence exists that anyone pays at ₹199.
- evidence: [C05] Forge lists free ChatGPT/Gemini tiers as the main substitute for drafting, labeled ASSUMPTION [source: forge-v1.md Positioning table]. [C06] NCH 2.0 includes an AI-enabled chatbot, with speech recognition and translation also in rollout [source: https://www.thestatesman.com/business/national-consumer-helpline-partners-with-over-1000-companies-to-bring-ai-tools-1503368509.html; also https://indiaai.gov.in/article/ai-enabled-national-consumer-helpline-transforming-grievance-redressal-in-india]. [C07] NCH accepts complaints via WhatsApp, SMS, email, app, UMANG and INGRAM in 17 languages, so the Hindi/Marathi language gap is partly covered [source: forge-v1.md#C04].
- what would fix it (FIXABLE only): n/a. A fix needs a buyer-visible job that a free chatbot and the NCH do not perform. No desk research can create that. A test with a free chatbot on a sample dispute would confirm rather than fix.
- fix would change customer/problem/revenue model: yes

### FE4 — FIXABLE
- flaw: The economics cost build-up understates fixed and platform costs. Day-3/7/15 reminders sent to customers after the 24-hour window need business-initiated template messages through a WhatsApp Business Platform provider (BSP). Economics assumes the free WhatsApp Business app (no automation) and ₹1,000/month fixed cost. BSP platform fees are separate from Meta message fees and carry 18% GST. At ₹1,500–8,000/month, conservative fixed cost rises from about ₹1,000 to about ₹2,800–10,400 with GST, and break-even moves from 8 cases/month to about 22–83 (my arithmetic on ₹125.58 contribution), against 4.75 modelled.
- evidence: [C08] Sources disagree on 2026 India marketing rates (₹0.78 to ₹1.10) and utility rates (₹0.115 to ₹0.145); GST 18% applies to Meta charges and BSP fees; BSP fees typically ₹1,500–8,000/month in one guide; service conversations started by the customer are free [source: https://montymobile.com/blogs/whatsapp-business-api-pricing-in-india-inr-rates-gst-and-the-2026-currency-migration-deadline; https://dev.to/chatlivo/whatsapp-business-api-pricing-2026-india-rates-free-tier-21ed; https://m.aisensy.com/blog/whatsapp-api-new-pricing/]. [C09] Economics fixed monthly costs are ChatGPT Go ₹399 plus ₹600 other [source: economics-v1.md Calculations].
- what would fix it (FIXABLE only): a redesigned flow with no BSP (customer-initiated chats only, reminders as manual messages inside open windows, or SMS/web form), or a priced BSP quote from a vendor page. Desk-researchable. Costs for the manual path would also add founder hours (affects FE1).
- fix would change customer/problem/revenue model: no

### FE5 — FIXABLE
- flaw: The acquisition plan depends on rules set by others. Society WhatsApp groups and apps are the lead channel (about 4.5 of 9.5 base customers/month), and forge's own assumption is that some societies prohibit commercial posts. Platform Grievance Officers and the NCH may require the account holder to file or verify, which limits a third party's role to preparation only. Meta can also restrict a WhatsApp number for spam reports. A banned or restricted number would cut both acquisition and delivery.
- evidence: [C10] Forge: "some societies prohibit commercial posts" [source: forge-v1.md#C24]. [C11] Society-group usage in Pune is not verified; the supporting source is a vendor blog and not Pune data [source: 01-local-market.md#C25]. [C12] Meta policy lets Meta decide on restricted goods and services at its sole discretion [source: https://whatsappbusiness.com/policy/].
- what would fix it (FIXABLE only): evidence of Pune society rules on commercial posts (sample of 10 society bylaws or admin statements), and the filing-authority rules of one platform Grievance Officer and the NCH on third-party submissions. Partly desk-researchable; society rules need local contact.
- fix would change customer/problem/revenue model: no

### FE6 — FIXABLE
- flaw: Data protection and registration costs are unpriced. The service holds order screenshots, phone numbers and addresses. DPDP core duties start about 2027-05-13, inside the first year. The Maharashtra Shops and Establishments registration (and possible municipal trade licence) is an unverified ASSUMPTION of ₹0–2,000 and vendors disagree on applicability.
- evidence: [C13] DPDP core duties apply from about 2027-05-13 [source: 01-local-market.md#C23]. [C14] Vendors disagree whether under-10-worker businesses need full registration or only intimation; a separate municipal trade licence may be needed [source: 01-local-market.md#C20, 01-local-market.md#C22].
- what would fix it (FIXABLE only): official Maharashtra labour department fee and applicability text; a template privacy notice and retention rule with cost; DPDP Rules text on small-fiduciary duties. Desk-researchable.
- fix would change customer/problem/revenue model: no

## Evidence
- [E1] Section 33 of the Advocates Act, 1961 requires enrolment for persons entitled to practise in any court or before any authority; whether paid non-advocate drafting is "practice" is not answered in the source found. [source: https://lawx.in/acts/section/65/586/5700]
- [E2] The Bar Council of India v. A.K. Balaji (2018) is cited by kill-criteria.md as a substance-over-label test; not re-opened by this agent. [source: https://itatonline.org/digest/bar-council-of-india-v-a-k-balaji-and-others-air-2018-sc-1382/, as cited in kill-criteria.md KE2]
- [E3] NCH has announced an AI-enabled chatbot, speech recognition and a translation system under NCH 2.0; a Statesman report describes parts as still in progress; no complaint-drafting feature is mentioned. [source: https://www.thestatesman.com/business/national-consumer-helpline-partners-with-over-1000-companies-to-bring-ai-tools-1503368509.html] (national)
- [E4] The WhatsApp Business Policy bars trading in restricted goods and services as determined in Meta's sole discretion; the named categories in third-party mirrors do not include legal services; I did not see the official text of every clause. [source: https://whatsappbusiness.com/policy/] (global)
- [E5] WhatsApp India rates for 2026 conflict: marketing ₹0.78–₹1.10, utility ₹0.115–₹0.145; billing is per delivered template message; BSP fees are separate; GST is 18%; customer-initiated service conversations are free. None of the sources is Meta's own rate card. [source: https://montymobile.com/blogs/whatsapp-business-api-pricing-in-india-inr-rates-gst-and-the-2026-currency-migration-deadline] (national)
- [E6] RegisterKaro's consumer-complaint page says it helps with filing cases in consumer court; no price was found; 2025–2026 customer complaints about RegisterKaro fees and refunds exist on a third-party complaint site, unverified. [source: https://registerkaro.in/consumer-complaint] (national)

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| none (round 1) | n/a | n/a |
