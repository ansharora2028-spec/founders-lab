---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: evidence-auditor
version: 1
created: 2026-10-15T09:34:24Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I03/kill-criteria.md, forge-v1.md, economics-v1.md, prosecution-market-v1.md, prosecution-execution-v1.md (all under <project>/ventures/runs/2026-10-15-pune-b2c-open/)
- claims in scope: about 95 (economics 18, forge 14, 01 26, 02 15, market prosecution 9, execution prosecution 7, plus criteria-file citations), checked: 34, sample method: all economics inputs + all FATAL-flaw evidence + all demand-evidence claims + forge/prosecution sourced claims + 2 from scouting files. Fewer than the full set were checked because of the tool failure below.
- TOOL FAILURE: every WebFetch call (to 16 different hosts, then a retry on 2 of them) returned "proxy refused the connection". No external URL could be opened. Under rule 8 each such claim is struck and labeled `UNREACHABLE (tool failure)`. The strike says nothing about whether the source supports the claim. The main session should re-run this audit once the proxy works.
- Claims about internal files (file#claim refs) were checked by reading the files and are not affected by the proxy.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 | Instagram CPM ₹45–350, CPC ₹6–55 (conservative ₹55) | https://upgrowth.in/instagram-ads-pricing-india-2026/ | UNREACHABLE (tool failure) | Load-bearing: drives ad CAC ₹5,500 |
| economics-v1.md#C02 | Razorpay 2% + 18% GST = 2.36% | https://razorpay.com/blog/razorpay-payment-gateway-pricing-explained/ | UNREACHABLE (tool failure) | Retried once |
| economics-v1.md#C03 | WhatsApp utility message ₹0.115–0.35 | https://whautomate.com/whatsapp-business-api-pricing-india | UNREACHABLE (tool failure) | |
| economics-v1.md#C04 | Freelance designer ₹293/h, range ₹79–808 | https://www.payscale.com/research/IN/Job=Freelance_Graphic_Designer/Hourly_Rate | UNREACHABLE (tool failure) | Load-bearing: ₹300/h sets fulfilment labour ₹100/kit |
| economics-v1.md#C05 | VA data-entry ₹225/h | https://www.payscale.com/research/IN/Job=Virtual_Assistant/Hourly_Rate/24aa8d85/Data-Entry | UNREACHABLE (tool failure) | Base case only |
| economics-v1.md#C06 | Internshala ₹300–2,000/h | https://internshala.com/blog/employer-cost-to-hire-graphic-designer/ | UNREACHABLE (tool failure) | |
| economics-v1.md#C18 | Pune PG rent ₹6,000–18,000 | https://fn.mahacet.org/category-check/blog/cost-of-living-pune-international-students.html | UNREACHABLE (tool failure) | Also cited as forge-v1.md#C02 and 01#C14. Economics says it is not used in the numbers |
| economics-v1.md Calculations | Conservative arithmetic (COGS ₹129.07, margin 56.8%, CACs ₹400/5,500/1,500/50, 17.3 customers, blended ₹1,426, break-even 17/month, capital ₹17,800, outlay ₹35,712, hours 84) | economics-v1.md | VERIFIED | Recomputed every step; all match within rounding. Table COGS ₹129.07 vs text ₹129.08 is rounding, disclosed in the file. Note: "5 utility messages" per kit (₹2.07) appears only in Calculations, not in the Inputs list |
| forge-v1.md#C01 | Sukoon PG tenant complaint 2026-04-19, no written contract | https://voxya.com/consumer-complaints/renter-not-giving-deposit-money/264368 | UNREACHABLE (tool failure) | Same URL as 02-signals S08 and C04. This is the only Pune pain evidence |
| forge-v1.md#C02 | PG rent range gives deposit exposure | https://fn.mahacet.org/category-check/blog/cost-of-living-pune-international-students.html | UNREACHABLE (tool failure) | Deposit multiple is flagged as an inference/ASSUMPTION in the file |
| forge-v1.md#C03 | Kothrud student locality, Hinjewadi IT hub, etc. | https://housing.com/news/top-pg-locations-in-pune/ | UNREACHABLE (tool failure) | |
| forge-v1.md#C04 | Pune police order 2026-07-03, 113 landlords | https://www.punekarnews.in/?p=241832 | UNREACHABLE (tool failure) | Same as 02-signals S07/C13. Retried once |
| forge-v1.md#C05 | Pune law firm: deficiency in service, notice often settles | https://sudhirrao.com/insights/pg-owner-not-returning-security-deposit-legal-remedy, 2026-08-12 | UNREACHABLE (tool failure) | The same firm's article appears in prosecution-market-v1.md#C04 with a different URL slug (`...legal-remedies`) and date (2026-08-06). One of the two may be a wrong slug or date. Not resolvable now |
| forge-v1.md#C06 | Lawrato/Kaanoon PG deposit questions | https://lawrato.com/consumer-court-legal-advice/health-hazard-in-pg-and-them-not-giving-my-deposit-back-255564 | UNREACHABLE (tool failure) | |
| forge-v1.md#C07 | E-commerce 29% of 1,771,622 NCH grievances | https://www.storyboard18.com/how-it-works/government-cracks-down-on-dark-patterns-as-consumer-complaints-surge-on-e-commerce-platforms-86557.htm | UNREACHABLE (tool failure) | (national) |
| forge-v1.md Persona (spend line) | Registered agreement ₹1,500–3,500 | https://www.nobroker.in/forum/how-much-does-online-rent-agreement-cost-in-maharashtra-with-e-registration/ | UNREACHABLE (tool failure) | Price anchor for FM2 and the competitor table |
| forge-v1.md Wedge | Leave and licence must be registered under the Rent Control Act | https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/ | UNREACHABLE (tool failure) | Used for KE4 |
| prosecution-market-v1.md#C01 | Forge names no tenant-facing competitor with price plus review/revenue sign | forge-v1.md Positioning table | VERIFIED | Forge table has no review or revenue figures; prices are "not shown", "not found" or a community estimate. This is a claim about forge-v1, not demand evidence |
| prosecution-market-v1.md#C02 | Paid inspection apps are foreign; RentProof free walkthrough, paid PDF | https://www.producthunt.com/p/rentproof-rental-inspection-reports/rentproof | UNREACHABLE (tool failure) | FATAL flaw FM1 evidence |
| prosecution-market-v1.md#C03 | Only India offer found is a Chennai managed service, no price | https://pixel-perfect-page-450.lovable.app/inspection/move-in-inspection | UNREACHABLE (tool failure) | FATAL flaw FM1 evidence. URL is a lovable.app subdomain of low evidential weight |
| prosecution-market-v1.md#C04 | Law-firm article, Zolo Stays example, 2026-08-06 | https://sudhirrao.com/insights/pg-not-returning-security-deposit-legal-remedies, 2026-08-06 | UNREACHABLE (tool failure) | FM3 evidence. See slug and date mismatch with forge-v1.md#C05 |
| prosecution-market-v1.md#C05 | Search for Pune commission orders returned only MSEDCL orders | https://www.mahadiscom.in/wp-content/uploads/2019/11/Case-No.-48-of-2019.pdf | UNREACHABLE (tool failure) | The cited URL is a 2019 electricity case. It supports only that unrelated results appeared, not that no PG case exists. Absence claim is weak even if reachable |
| prosecution-market-v1.md#C06 | NoBroker Pune guide: duty 0.25%, ₹1,000, ₹700–1,000 | https://www.nobroker.in/lease-agreement/guides/leave-and-license-agreement-pune/ | UNREACHABLE (tool failure) | FM4 evidence. The attached "₹1,500–3,500 forum estimate" is a different URL (forge persona row) |
| prosecution-market-v1.md#C07 | Free deposit-refund letter templates exist in English only | https://chw.dhis2.org/template/deposit-refund-letter-template.html | UNREACHABLE (tool failure) | A DHIS2 community health worker template URL; relevance to Indian tenant letters is doubtful |
| prosecution-market-v1.md#C08 | SECC 751,874 households for Pune district | https://secc.gov.in/getAllCategoryHouseOwnershipStatusDistrictLgdReport.htm/27/490 | UNREACHABLE (tool failure) | FM5 evidence; prosecutor says the column layout is unclear |
| prosecution-market-v1.md#C09 | Settl delayed deposit refunds in 4 other cities | https://inc42.com/buzz/settls-tenants-allege-delay-in-security-deposit-refunds-report/ | UNREACHABLE (tool failure) | (other cities) |
| prosecution-market-v1.md FM2 | Conservative CAC ₹1,426, payback "never", unit economics "no" | economics-v1.md | VERIFIED | Matches the file's Scenarios and Verdict inputs; arithmetic re-verified above |
| prosecution-execution-v1.md#C01 | Conservative price ₹299, GP ₹169.93, CAC ₹1,426, 17.3 customers, outlay about ₹35,700 | economics-v1.md | VERIFIED | FATAL flaw FE1 evidence. Matches the file and the recomputation |
| prosecution-execution-v1.md#C02 | Advocates Act s.33; 2025 draft amendment under consultation | https://www.scconline.com/blog/post/2025/02/24/gcai-recommendations-for-draft-advocates-act-amendment-bill-public-comments-legal-news/, 2025-02-24 | UNREACHABLE (tool failure) | FE2 (FIXABLE) |
| prosecution-execution-v1.md#C03 | Leave and License 2.0 for Mumbai from 2025-05-01; parties register directly | https://housing.com/news/stamp-duty-registration-laws-rentals-maharashtra | UNREACHABLE (tool failure) | FE3. The source is Mumbai-scoped by the prosecutor's own note; Pune not confirmed. Also cited in kill-criteria KE4 and forge competitor table |
| prosecution-execution-v1.md#C04 | WhatsApp enforcement escalates to permanent removal | https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement | UNREACHABLE (tool failure) | FE4 |
| prosecution-execution-v1.md#C05 | Conservative first revenue 2.3 months | economics-v1.md#C16 | VERIFIED | Matches the file |
| prosecution-execution-v1.md#C06 | DPDP main duties around 2027-05-13 | https://treelife.in/compliance/digital-personal-data-protection-dpdp-rules-2025/ | UNREACHABLE (tool failure) | (national). Also 02-signals S05/C11 and 01#C23 give the same date from mondaq |
| 01-local-market.md#C15 | Pawzeeble Pune pet-care aggregator, 380+ clinics | https://yourstory.com/2025/06/affordable-pet-care-inside | UNREACHABLE (tool failure) | Sample item. Not demand evidence for I03 (pet care) |
| 02-signals.md#C13 | Pune police order 2026-07-03, 113 landlords | https://www.punekarnews.in/?p=241832 | UNREACHABLE (tool failure) | Duplicate of forge-v1.md#C04 |

## Struck claims
All struck as UNREACHABLE (tool failure). The sources were not opened, so these strikes do not show the claims are wrong.
- economics-v1.md#C01 — UNREACHABLE (tool failure) — Instagram CPC input; load-bearing for conservative ad CAC
- economics-v1.md#C02 — UNREACHABLE (tool failure) — payment fee input
- economics-v1.md#C03 — UNREACHABLE (tool failure) — WhatsApp message cost input
- economics-v1.md#C04 — UNREACHABLE (tool failure) — fulfilment labour rate; load-bearing for conservative COGS
- economics-v1.md#C05 — UNREACHABLE (tool failure) — base-case labour rate
- economics-v1.md#C06 — UNREACHABLE (tool failure) — upper labour rate range
- economics-v1.md#C18 — UNREACHABLE (tool failure) — Pune PG rent range (context only)
- forge-v1.md#C01 — UNREACHABLE (tool failure) — sole Pune pain anecdote
- forge-v1.md#C02 — UNREACHABLE (tool failure) — PG rent range
- forge-v1.md#C03 — UNREACHABLE (tool failure) — locality descriptions
- forge-v1.md#C04 — UNREACHABLE (tool failure) — police order (the only "why now")
- forge-v1.md#C05 — UNREACHABLE (tool failure) — law-firm article; URL and date also conflict with prosecution-market-v1.md#C04
- forge-v1.md#C06 — UNREACHABLE (tool failure) — Q&A forum questions
- forge-v1.md#C07 — UNREACHABLE (tool failure) — national complaint figure
- forge-v1.md Persona spend line (NoBroker forum ₹1,500–3,500) — UNREACHABLE (tool failure)
- forge-v1.md Wedge (registration required) — UNREACHABLE (tool failure)
- prosecution-market-v1.md#C02 — UNREACHABLE (tool failure) — evidence for FATAL FM1
- prosecution-market-v1.md#C03 — UNREACHABLE (tool failure) — evidence for FATAL FM1
- prosecution-market-v1.md#C04, #C05, #C06, #C07, #C08, #C09 — UNREACHABLE (tool failure) — evidence for FIXABLE flaws FM3 to FM5 and the criteria table
- prosecution-execution-v1.md#C02, #C03, #C04, #C06 — UNREACHABLE (tool failure) — evidence for FIXABLE flaws FE2 to FE4, FE6
- 01-local-market.md#C15 — UNREACHABLE (tool failure) — sample item
- 02-signals.md#C13 — UNREACHABLE (tool failure) — sample item

Not struck: FM2 (prosecution-market) and FE1 (prosecution-execution), the two FATAL flaws that rest on internal file references. Their evidence is economics-v1 numbers, which were re-derived and found arithmetically correct. The economics inputs that drive those numbers (C01, C04) are struck, so the Judge should treat the CAC and COGS figures as unsupported by sourced inputs. The demand-side conversion inputs were already ASSUMPTION.

## Assumptions in load-bearing positions
- economics-v1.md#C07 — price ₹299 conservative, no upsell; basis of the conservative gross profit
- economics-v1.md#C08 — 20-minute fulfilment per kit; basis of the largest COGS item
- economics-v1.md#C10 — 5% refund rate
- economics-v1.md#C12, #C13 — one-off costs ₹13,000 (lawyer review, registration not researched)
- economics-v1.md#C15 — all channel reach and conversion rates; basis of conservative customer count (17.3) and CAC
- economics-v1.md#C16 — time to first revenue 2.3 months; basis of K6 "fits"
- forge-v1.md#C08, #C09 — Pune tenants will pay; the demand premise; basis of prosecutor FM1 and criterion KM1
- forge-v1.md#C10, #C11, #C12, #C13, #C14 — operator acknowledgement, legal-practice exposure, WhatsApp admin acceptance, intake season, deposit size; bases for KE2, KE3, KE6 statuses and FE2, FE4, FE5
- forge-v1.md Path to first 100 customers table — all figures ASSUMPTION (about 103 customers)

## Summary
- verified: 4, misrepresented: 0, unreachable: 30 (of which tool failure: 30), unsourced: 0
- Recomputed economics arithmetic: correct, no errors found.
- Other observations: forge-v1.md#C05 and prosecution-market-v1.md#C04 give different URLs and dates for what appears to be the same law-firm article. prosecution-market-v1.md#C05 cites a 2019 MSEDCL PDF for an absence-of-results claim.
- demand evidence surviving the audit: none. The forge lists no competitor with a verified price and revenue or review sign; the prosecutor's own search (all struck) found no Indian tenant-side seller. The Pune pain anecdote (forge-v1.md#C01) is struck.
