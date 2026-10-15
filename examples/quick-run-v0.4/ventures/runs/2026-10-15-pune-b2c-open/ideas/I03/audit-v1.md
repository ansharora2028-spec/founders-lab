---
run_id: 2026-10-15-pune-b2c-open
idea_id: I03
agent: evidence-auditor
version: 1
created: 2026-10-15T10:45:52Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I03/kill-criteria.md, ideas/I03/forge-v1.md, ideas/I03/economics-v1.md, ideas/I03/prosecution-market-v1.md, ideas/I03/prosecution-execution-v1.md (all under <project>/ventures/runs/2026-10-15-pune-b2c-open/). verdict files not read.
- claims in scope: about 150 sourced or assumption-labelled claims across the files; checked: 23 rows below (every sourced economics input, the economics arithmetic, the evidence behind the only FATAL flaw FE1, the demand evidence, and a sample of the rest). Distinct URLs attempted: 28.
- sample method: all economics inputs + all FATAL-flaw evidence + all demand evidence + non-random-but-spread sample of the rest (one from each file), because the fetch tool failed for every host.
- tool note: WebFetch returned "proxy refused the connection" on every one of 28 distinct hosts and URLs, including a second attempt on 2 URLs (urbancompany.com, techcrunch.com). No page could be opened. This is a tool or environment failure, not evidence that the sources are bad. Per rule 8, these claims are struck anyway.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 (= forge-v1.md#C01) | UC Pune apartment deep clean Rs 3,199 unfurnished / Rs 3,499 furnished (Koregaon Park) | https://www.urbancompany.com/pune-professional-home-cleaning-meera-nagar-koregaon-park | UNREACHABLE (tool failure) | proxy refused twice-class failure; price ceiling for the idea |
| economics-v1.md#C02 (= forge-v1.md#C02, prosecution-execution-v1.md FE1 C02) | UC Deccan Gymkhana Rs 2,999 / Rs 3,199 | https://www.urbancompany.com/pune-home-cleaning-services | UNREACHABLE (tool failure) | retried once; same failure. Conservative price input. Also: execution FE1 cites this page for a "Rs 2,999-3,499 band", but the 3,499 figure is attributed by forge to a different page |
| economics-v1.md#C03 | IndiaMART Pimpri Chinchwad Rs 7-8 per sq ft; 500-700 sq ft gives Rs 3,500-5,600 | https://dir.indiamart.com/pimpri-chinchwad/deep-cleaning-services.html | UNREACHABLE (tool failure) | arithmetic of the range is correct (500x7=3,500; 700x8=5,600); source text unchecked. Note the claim also credits Ghare Rs 6-7 to this URL, which is Ghare's own listing, not IndiaMART |
| economics-v1.md#C06 (apna) | Pune housekeeping Rs 15,000-20,000 a month | https://apna.co/job/pune/housekeeping-staff-292065227 | UNREACHABLE (tool failure) | only sourced basis for team-cost range; per-job team cost itself is ASSUMPTION |
| economics-v1.md#C06 (Indeed) | Pune cleaning jobs Rs 10,488-32,540 a month | https://in.indeed.com/explorer/high-paying-cleaning-jobs-pune,-mh | UNREACHABLE (tool failure) | |
| economics-v1.md#C07 | Start-up supplies Rs 2,000-5,000 (Rajasthan) | https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-rajasthan-cost-license-setup-guide | UNREACHABLE (tool failure) | other state, lender blog |
| economics-v1.md#C07 | Chemicals Rs 3,000-8,000 (Uttar Pradesh) | https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-uttar-pradesh-cost-license-setup-guide | UNREACHABLE (tool failure) | other state |
| economics-v1.md#C09 | UPI 0% MDR; Razorpay 2% platform fee on UPI | https://razorpay.com/blog/upi-charges-explained-mdr-vs-platform-fees/ | UNREACHABLE (tool failure) | |
| economics-v1.md#C12 | Meta India CPC Rs 0.51-2.26 / Rs 3-12; leads Rs 200-2,000 | https://upgrowth.in/facebook-advertising-pricing/ | UNREACHABLE (tool failure) | file itself says "via search summary" |
| economics-v1.md#C19 | Vacuum Rs 3,000-12,000, supplies Rs 2,000-5,000 | https://www.iifl.com/blogs/gold-loan/how-to-start-a-cleaning-service-in-rajasthan-cost-license-setup-guide | UNREACHABLE (tool failure) | same URL as C07 row; the conservative Rs 17,000 equipment figure is the sum of range tops (12,000 + 5,000) |
| economics-v1.md#C21 | Shop Act fees disputed across consultancy pages | https://www.patronaccounting.com/shop-act-registration/pune | UNREACHABLE (tool failure) | |
| economics-v1.md#C24 (= forge-v1.md#C20) | Maharashtra gig bill 2026, aggregator definition not found | https://teamleaseregtech.com/updates/article/57603/maharashtra-gig-and-platform-workers-rights-and-protection-bill-2026/ | UNREACHABLE (tool failure) | |
| economics-v1.md Calculations (conservative column) | COGS 3,250; margin -251 (-8.4%); blended CAC 562; contribution -813; monthly -6,282; capital to first revenue 29,500; month-3 exposure about 58,300; hours 4.3 h/week | economics-v1.md itself | VERIFIED | recomputed: 2,400+250+200+60+240+100=3,250; 3,650/6.5=561.5; -251-562=-813; -1,632-3,650-1,000=-6,282; 17,000+3,000+3,000+6,500=29,500; 29,500+10,000+3x6,282=58,346; (9.75+8.6)/4.3=4.27 h. Base (COGS 2,598, CAC 260) and optimistic (2,085, 178) and the paid-ads CACs (1,600 / 343 / 94) also recompute. No arithmetic error found. Hours caveat from prosecution-execution E01 (25 jobs = about 10.7 h/week) also recomputes, 25x1.5+8.6=46.1 h/month |
| forge-v1.md#C03 | Ghare: Rs 7 / Rs 6 per sq ft, Google 4.8 from 166 reviews | https://business.google.com/v/ghare-facility-cleaning-services/016890659316125069239/f893/_/fullmenu/ | UNREACHABLE (tool failure) | demand-evidence for independents. Note: prosecution-market-v1.md#C04 reports the same listing shows no prices or review count, and prosecution-execution-v1.md#E05 says it starts "from Rs 3,500": the three files disagree about this one page |
| 01-local-market.md#C34 (D05) | UC Pune cleaning, 4.8 rating, 220,000-260,000 reviews per locality page | https://www.urbancompany.com/pune-home-cleaning-services | UNREACHABLE (tool failure) | demand anchor D05. Forge cites 339K-446K reviews on other pages |
| 01-local-market.md#C32 (D05) | Cleaning help Rs 402 an hour in Pune | https://expatistan.com/price/cleaning-help/pune | UNREACHABLE (tool failure) | demand anchor D05 |
| 01-local-market.md#C44 (= forge-v1.md#C05, C13) | Raviwar Peth reviews: skipped areas, grease, extra fee; about 4,000 one-star ratings | https://www.urbancompany.com/pune-professional-home-cleaning-raviwar-peth | UNREACHABLE (tool failure) | basis of the "need gap" |
| 02-signals.md#C02 (= forge-v1.md#C07) | NCH Jan-Jul 2025 Urban Company: 97 delayed, 52 not provided, 36 damage | https://consumerhelpline.gov.in/public/dashboard/sectorcompanyNatureWise/20/2825 | UNREACHABLE (tool failure) | national |
| 02-signals.md#S07 (= forge-v1.md#C08) | Snabbit about $400M valuation talks; UC Insta Help 1M bookings | https://techcrunch.com/2026/04/25/indias-snabbit-seeks-fresh-funding-at-a-400m-valuation-sources-say/ | UNREACHABLE (tool failure) | retried once; same failure |
| prosecution-market-v1.md#C02 | UC partner net earnings Rs 280-300/hour, Rs 26,271/month | https://www.outlookbusiness.com/news/urban-company-gig-worker-makes-rs-26271-a-month-on-average-ceo-abhiraj-singh-bhal | UNREACHABLE (tool failure) | file says search summary only |
| prosecution-market-v1.md#C08 | Housejoy stopped in 7 of 12 cities, 2017 | https://www.medianama.com/2017/05/223-housejoy-shuts-services-in-7-cities/ | UNREACHABLE (tool failure) | |
| prosecution-market-v1.md#C09 | Clean Fanatics INR 17 crore seed, 40% revenue from referrals | https://realtynmore.com/clean-fanatics-raises-2-mn-in-seed-round-led-by-inflection-point-ventures/ | UNREACHABLE (tool failure) | |
| prosecution-execution-v1.md#E02 / FE3 C05 | Social Security (Central) Rules 2026 in force 2026-05-08; aggregator duties | https://www.taxmann.com/post/blog/analysis-aggregator-obligations-code-on-social-security/ | UNREACHABLE (tool failure) | |

Not fetched (no budget reason, same host class failed): prosecution-market-v1.md#C01, C03, C05, C06 (urbancompany.com locality pages, same host as failing rows) and prosecution-execution-v1.md#FE4 C08, E04 (urbancompany.com), FE3 C06/C07 (teamlease, dcpsol). These were not checked and are not counted in the totals. The Judge should treat them as unaudited.

## Struck claims
All 22 rows labelled UNREACHABLE (tool failure) are struck:
- economics-v1.md#C01 — UNREACHABLE (tool failure) — Koregaon Park UC price
- economics-v1.md#C02 — UNREACHABLE (tool failure) — Deccan Gymkhana UC price; this is the conservative price input
- economics-v1.md#C03 — UNREACHABLE (tool failure) — IndiaMART per-sq-ft prices
- economics-v1.md#C06 (apna) — UNREACHABLE (tool failure) — housekeeping pay
- economics-v1.md#C06 (Indeed) — UNREACHABLE (tool failure) — cleaning job pay
- economics-v1.md#C07 (both iifl URLs) — UNREACHABLE (tool failure) — supply budgets
- economics-v1.md#C09 — UNREACHABLE (tool failure) — payment fees
- economics-v1.md#C12 — UNREACHABLE (tool failure) — Meta CPC and lead cost
- economics-v1.md#C19 — UNREACHABLE (tool failure) — equipment cost
- economics-v1.md#C21 — UNREACHABLE (tool failure) — Shop Act fees
- economics-v1.md#C24 — UNREACHABLE (tool failure) — Maharashtra bill
- forge-v1.md#C01, #C02 — UNREACHABLE (tool failure) — UC prices (same URLs as economics C01, C02)
- forge-v1.md#C03 — UNREACHABLE (tool failure) — Ghare price and 166 reviews; also contradicted in wording by prosecution-market-v1.md#C04
- forge-v1.md#C04 — UNREACHABLE (tool failure) — same URL as economics C03
- forge-v1.md#C05, #C13 and 01-local-market.md#C44 — UNREACHABLE (tool failure) — UC Raviwar Peth reviews
- forge-v1.md#C07 and 02-signals.md#C02 — UNREACHABLE (tool failure) — NCH data
- forge-v1.md#C08 and 02-signals.md#S07 — UNREACHABLE (tool failure) — Snabbit funding
- 01-local-market.md#C32, #C34 — UNREACHABLE (tool failure) — D05 evidence
- prosecution-market-v1.md#C02, #C08, #C09 — UNREACHABLE (tool failure)
- prosecution-execution-v1.md#E02, FE3 C05 — UNREACHABLE (tool failure)
- prosecution-execution-v1.md#FE1 C02 — UNREACHABLE (tool failure) — evidence for the FATAL flaw FE1 (price band); also the cited page supports only the Rs 2,999 / 3,199 prices per forge, not a 3,499 ceiling

Not struck: economics-v1.md Calculations (VERIFIED arithmetic). prosecution-execution-v1.md#FE1 C01 and C03 are restatements of economics-v1.md Scenarios and Verdict inputs, whose arithmetic is verified; the numbers inside them that rest on struck inputs (price Rs 2,999, team Rs 2,400 ASSUMPTION) remain only as strong as those inputs.

## Assumptions in load-bearing positions
- economics-v1.md#C04 — ASSUMPTION used as the basis of the conservative price (Rs 2,999)
- economics-v1.md#C06 (per-job team cost Rs 2,400 / 2,000 / 1,700) — ASSUMPTION used as the basis of the conservative COGS and of FE1 (the largest cost line; no per-job team rate sourced)
- economics-v1.md#C07, #C08, #C10, #C11, #C16, #C17, #C18, #C20, #C21 — ASSUMPTION used as conservative cost inputs
- economics-v1.md#C13, #C14, #C15 — ASSUMPTION used as the basis of conservative CAC (every conversion rate and channel yield is unsourced)
- economics-v1.md#C22 — ASSUMPTION used as the basis of the founder-hours calculation (KE1, FE2)
- economics-v1.md#C23 — ASSUMPTION used as the basis of months to first revenue (K6)
- forge-v1.md#C09, #C16, #C17, #C18, #C19, #C22, #C23 — ASSUMPTIONs used as the basis of the need gap, the team cost, the price premium, the hours and the acquisition path
- forge-v1.md#C08 — partly ASSUMPTION (inference from absence) used as the basis of "why open now"; also load-bearing for FM1 and FE5
- 01-local-market.md#D12 and the salon buyer mix — ASSUMPTION, not relevant to I03

## Summary
- verified: 1, misrepresented: 0, unreachable: 22 (of which tool failure: 22), unsourced: 0
- demand evidence surviving the audit: none. D05 (01-local-market.md#C32, #C34), forge-v1.md#C01 to #C04 and the Ghare listing are all struck as UNREACHABLE (tool failure). The Judge should treat this as an environment failure that leaves demand evidence unverified, not as a finding that the sources are false. The one verified item (economics arithmetic) is internal consistency only and is not demand evidence.
