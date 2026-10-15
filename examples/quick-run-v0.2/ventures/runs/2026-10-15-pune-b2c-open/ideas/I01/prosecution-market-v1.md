---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-market
version: 1
created: 2026-10-15T09:32:42Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- .../01-local-market.md
- .../02-signals.md
- .../ideas/I01/kill-criteria.md (LOCKED)
- .../ideas/I01/forge-v1.md
- .../ideas/I01/economics-v1.md
- Own web searches (claims below). Two page fetches (registerkaro.in, kashmirlife.net) failed with a proxy error; their content is used only as shown in search snippets.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | NOT MET | C01, C02, C03, forge-v1.md#C17, economics-v1.md#C18 | Only 1 paid service found inside the ₹99–999 band (Consumer VOICE, ₹499, NGO, undated). Two others are above the band (₹1,499; ₹4,999). No dated revenue, review or testimonial found for any. Forge itself states there is no direct willingness-to-pay evidence. Search was shallow (two fetches failed), so a 2nd or 3rd in-band service could exist, but none is shown. |
| KM2 | INSUFFICIENT EVIDENCE | C04, C05, C06 | Official-style figures show NCH disposes of all e-commerce grievances (440,185 received, 440,185 disposed in 2024), but "disposed" is not "resolved". The only satisfaction figure (77% resolved to satisfaction, so about 23% not) is undated and from Inc42. No source on rejected or timed-out share, and no source of consumers hiring intermediaries. The 20% bar is neither reached nor refuted. |
| KM3 | NOT MET | forge-v1.md#C12–C16, economics-v1.md#C14, C09 | No shopper count x incidence estimate is shown by forge. Forge's own channel model gives 9–12 cases per month (about 110–145 per year); economics conservative gives 4.75 per month (about 57 per year). Threshold is 1,000 per year. No Maharashtra or Pune NCH counts were found by anyone. |
| KM4 | INSUFFICIENT EVIDENCE | forge-v1.md#C08, forge-v1.md#C09, C02, C03 | Part 2 is met in substance: Consumer VOICE ₹499 and IncorpX ₹1,499 show Indians being offered comparable paid notice/advice services above ₹199 (offers, not proven purchases). Part 1 needs a median or typical disputed order of at least ₹1,000. Forge supplies only a mean (about ₹7,400, a refund-recovered average that skews high, labelled ASSUMPTION by forge). No median. Forge's own wedge restricts to orders of ₹1,500+, which implies it does not regard the typical order as clearing the bar. |
| KM5 | NOT MET | C07, forge-v1.md (no graveyard section), 01-local-market.md (no comparable failure analysis) | No documented 5-query search listing the fate of 3 comparable ventures exists in any input. My own searches (4 queries) found no India comparable with a stated cause of death. The criterion requires the search to be documented and the fate of 3 ventures found; that is not satisfied. Absence of a found graveyard is not evidence of survival. |
| KM6 | INSUFFICIENT EVIDENCE | C08, C09, C10, 02-signals.md#S02 | The 2026 Amendment Rules start date rests on a Moneylife press article only; no Gazette or PIB source seen. Series: about 2.05 lakh (2020-21), 4.45 lakh (2023-24), 440,185 (calendar 2024), 511,196 (calendar 2025, per signals), 577,748 (2025-26). Growth looks real over the long run, but 2023-24 to 2024 is roughly flat (mixed fiscal and calendar bases), so "2 consecutive years of growth" is not cleanly shown from official sources. The rules bind sellers; no source says they raise consumer willingness to pay. |

KE criteria: no direct market evidence offered; not assessed.

## Flaws
### FM1 — FATAL
- flaw: There is no evidence that consumers pay for drafting help on a dispute where a free, high-volume route exists. The idea's whole revenue rests on a stated assumption (forge-v1.md#C17). The free route handled about 5 lakh e-commerce grievances a year, mostly with no paid help, and the free alternatives (NCH in 17 languages, WhatsApp channel, platform officers, free chatbots) already cover drafting.
- evidence: [C01] Paid offers found are NGO advice at ₹499, legal notice at ₹1,499 and complaint letters at ₹4,999; none in the ₹199 band and none with demand proof. [source: https://www.incorpx.io/legal-notice-drafting] [C02] See Evidence. [C05] NCH e-commerce grievances all disposed in 2024 through the free route. [source: https://rsdebate.nic.in/bitstream/123456789/758830/1/PQ_267_11022025_U882_p314_p316.pdf]
- fix would change customer/problem/revenue model: yes (a fix would need a different payer, a different problem or a success-fee/B2B model)

### FM2 — FATAL
- flaw: Reachable volume in the contract window is a fraction of the minimum. Forge concedes 100 customers take 8–11 months; economics conservative says 21 months, 4.75 cases per month, cash result -₹403.5 per month, and negative loaded contribution per case. Customers do not repeat. At ₹149–199 the business cannot reach even 1,000 cases per year through the founder's channels under K2.
- evidence: forge-v1.md#C12–C16 and "Conclusion" lines; economics-v1.md Calculations (volume 4.75/month, break-even 8/month). Paid acquisition modelled at about ₹5,000 per customer against a ₹149 price (economics-v1.md Calculations; ASSUMPTION rates).
- fix would change customer/problem/revenue model: yes (higher price or different customer)

### FM3 — FIXABLE
- flaw: No Pune or Maharashtra incidence or volume estimate exists (KM3 gap); Pune channel reach is all ASSUMPTION.
- what would fix it: state-wise NCH e-commerce counts for Maharashtra (Lok Sabha/Rajya Sabha replies) plus online-shopper share for Pune, shown with arithmetic. Desk-researchable in part; Pune-level counts may not exist, in which case a labelled Maharashtra proxy is the best available.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: The ₹1,500-minimum wedge shrinks the addressable pool by an unknown factor and the 3% stuck-refund incidence is unsourced (forge-v1.md#C18, #C25). Disputes with the largest counts (food, quick commerce, small-ticket) are excluded by K8 or by the minimum.
- what would fix it: a distribution of refund values at NCH, or survey data on dispute incidence by order value. Partly desk-researchable (NCH reports total refunds and counts; median is rarely published).
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Graveyard not searched by forge (KM5). The closest cautionary case I found is DoNotPay (US), a consumer-complaint/legal-letter AI product that settled with the FTC for $193,000 over unsupported claims of replacing lawyers, which is a regulatory, not demand, failure. No India comparable with a stated cause of death was found.
- evidence: [C07] See Evidence.
- what would fix it: a documented 5-query search with the fate of 3 comparable ventures (Tracxn/CB Insights status pages, shutdown notices). Desk-researchable.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Timing claim overstated. The 2027-01-01 rules bind sellers; forge's own text says they "may shift which routes work". Grievance volume growth is real but a possible rise in free-route use makes the free substitute stronger, not the paid one.
- what would fix it: official Gazette/DoCA notification and a consumer-side demand signal (for example rising paid-service search or revenue). Gazette part is desk-researchable; demand part likely not.
- fix would change customer/problem/revenue model: no

## Evidence
- [C01] IncorpX sells legal notice drafting and delivery from ₹1,499 plus postage, 3–5 working days (vendor claim; outside the ₹99–999 band). (national) [source: https://www.incorpx.io/legal-notice-drafting]
- [C02] Ebizfiling advertises consumer complaint letter drafting from ₹4,999 (vendor claim, snippet only). (national) [source: https://ebizfiling.com/service/consumer-complaint-letter/]
- [C03] Consumer VOICE (NGO) charges ₹499 for basic legal advice and then sends a notice to the company (snippet only; date not shown; not a startup). (national) [source: https://join.consumer-voice.org/legal/]
- [C04] Dataful lists total NCH grievances at 1,315,664 for 2024-25 with e-commerce at 32.22%. (national) [source: https://dataful.in/datasets/20716]
- [C05] Rajya Sabha reply (2025-02-11) table: e-commerce received 440,185, disposed 440,185 (calendar 2024). "Disposed" does not mean resolved. (national) [source: https://rsdebate.nic.in/bitstream/123456789/758830/1/PQ_267_11022025_U882_p314_p316.pdf]
- [C06] Inc42 reports that in 77% of cases complaints against e-commerce firms were resolved to the customer's satisfaction (undated in the snippet). (national) [source: https://inc42.com/buzz/ecommerce-complaints-consumer]
- [C07] FTC settled with DoNotPay for $193,000 over deceptive "robot lawyer" claims; the case is regulatory, not about demand. (other country: US) [source: https://www.abajournal.com/news/article/robot-lawyer-website-donotpay-settles-ftc-claims-it-couldnt-deliver-on-promises]
- [C08] E-commerce grievances at NCH grew from about 2.05 lakh (2020-21) to 4.45 lakh (2023-24), 36.1% of all grievances in 2023-24 (Lok Sabha reply as reported). (national) [source: https://www.medianama.com/2025/07/223-national-consumer-helpline-8500-e-commerce-complaints/]
- [C09] E-commerce stayed the largest source of complaints, with 577,748 in 2025-26 (secondary report of a Lok Sabha reply; overall NCH volume 12.36 lakh in 2023-24, 13.16 lakh in 2024-25, 20.49 lakh in 2025-26). (national) [source: https://kashmirlife.net/consumer-complaints-from-jammu-kashmir-rise-78-per-cent-in-three-years-all-cases-resolved-centre-tells-lok-sabha-446604/]
- [C10] Total NCH grievances in 2025 and e-commerce share from signals file. (national) [source: https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm]

Confidence: low-to-medium. Local Pune data is absent from every input and from my searches; all findings above are national unless labelled. Coverage of paid-competitor pricing is shallow because two fetches failed.

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a | n/a | round 1 |
