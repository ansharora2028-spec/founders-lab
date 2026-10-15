---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: evidence-auditor
version: 1
created: 2026-10-15T10:45:41Z
---

## Scope
- files audited: 00-contract.md, 01-local-market.md, 02-signals.md, ideas/I01/kill-criteria.md, ideas/I01/forge-v1.md, ideas/I01/economics-v1.md, ideas/I01/prosecution-market-v1.md, ideas/I01/prosecution-execution-v1.md (all under <project>/ventures/runs/2026-10-15-pune-b2c-open/). Verdict files not read.
- claims in scope: about 190 (01: 51 claims and 13 demand anchors; 02: 32 claims and 18 signals; forge-v1: 22; economics-v1: 18; prosecution-market-v1: 8; prosecution-execution-v1: 5 evidence items), checked: 23 rows in the table below (22 source checks, 1 arithmetic check). Sample method: all economics inputs that carry a source, all FATAL-flaw evidence (FE1, FE2, FE4), all demand evidence (forge-v1 C01, C05, C07, C08; 01 C22-C24; 02 S10), the cited legal and regulatory claims, then 01 and 02 claims picked at random. Economics claims C02, C04-C07, C09-C12 and C16 are labeled ASSUMPTION or reasoning and have no URL to fetch. They are listed under assumptions.
- tool state: this session had no working fetch. Every WebFetch call returned "proxy refused the connection". I made 22 calls to 21 different hosts (consumer-voice.org, incorpx.io, morungexpress.com, upgrowth.in, itatonline.org, livelaw.in (tried twice), scconline.com, outlookbusiness.com, collegedunia.com (two pages), newsonair.gov.in, rsdebate.nic.in, righttoinformation.wiki, lawtrend.in, kanakkupillai.com, seqrite.com, pagalguy.com, yourstory.com, desikaanoon.in, bcajonline.org). All failed the same way. No page text was seen, so no claim could be compared with its source. I did not run the status check from the proxy README because I have no shell tool. The failure is in the tool, not in the sources. Rule 8 has no exception, so every claim whose only support is a URL I could not open is struck, and each is marked "(tool failure)".
- sources the prosecutors and scouts say were not opened: 01 and 02 say all fetches failed, and both prosecutors say they saw search-result text only. Forge and economics also cite from search results. No agent in this round has seen the text of the pages behind these claims.

## Checked claims
| ref | claim (short) | url | label | note |
|---|---|---|---|---|
| economics-v1.md#C01 | Notice drafting Rs 500 plus postage (Consumer Voice) and Rs 1,499 plus Rs 60-80 (IncorpX); price anchors for the conservative Rs 500 price | https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting | UNREACHABLE (tool failure) | Both URLs were tried and failed. Load-bearing. The conservative price is Rs 500 from this claim. Both pages are also price-only (no customer counts) per prosecution-market-v1.md#C01. |
| economics-v1.md#C03 | UPI at or under Rs 2,000 carries zero MDR from 2026-10-15; 0.4% above that; small merchants up to Rs 1 lakh a month keep zero MDR | https://morungexpress.com/npci-reveals-mdr-on-upi-payments-above-rs-2000-from-oct-15-small-merchants-continue-to-benefit | UNREACHABLE (tool failure) | The second URL (bajajbroking.in) was not tried separately. The conservative case does not use this claim. It uses a 2% gateway fee instead. |
| economics-v1.md#C08 | Instagram ad CPC in India 2026 about Rs 6-55, Education Rs 15-30 | https://upgrowth.in/instagram-ads-pricing-india-2026/ | UNREACHABLE (tool failure) | Load-bearing. Rs 55 CPC gives the conservative paid CAC of Rs 5,500. The second URL (bosswallah.com) was not tried separately. The file itself says sources conflict (one gives Rs 2-6). |
| economics-v1.md#C13 | Supreme Court, BCI v. A.K. Balaji: practice of law includes non-litigation drafting; Advocates Act s.29 | https://itatonline.org/archives/lawyers-collective-vs-bar-council-bombay-high-court/ ; https://bcajonline.org/?p=16796 | UNREACHABLE (tool failure) | Both URLs were tried and failed. Load-bearing for FE1 (FATAL) and KE2. The URL title (Lawyers Collective vs Bar Council, Bombay HC) does not obviously match a Balaji holding, so this deserves a manual check once a fetch works. |
| economics-v1.md#C14 | NCH coaching complaints 16,276 in 2023-24 (national) | https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes | UNREACHABLE (tool failure) | Same source as forge-v1.md#C08 and #C12. |
| economics-v1.md#C15 | NCH 1915 recovered Rs 1.56 crore for 600+ coaching students | https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres | UNREACHABLE (tool failure) | Same source as forge-v1.md#C07. Used by FM4. |
| economics-v1.md#C17 | GST registration threshold Rs 20 lakh for services (national rule) | https://www.kanakkupillai.com/gst-registration-online-in-pune | UNREACHABLE (tool failure) | Not decisive. Turnover is far below any threshold. |
| economics-v1.md Calculations (conservative column) | Gateway fee 12; COGS 62; contribution 438; margin 87.6%; 24 customers; CAC 500 and 208; payback 0.48; hours 83 of 130; paid CAC 5,500; capital 6,500; 3-month net -1,000; peak outlay 11,500; break-even 5.9 to 6; steady month 920; 29 files for Rs 10,000 | none (arithmetic) | VERIFIED | Recomputed every step from the file's own inputs. 2% x 500 = 10; 18% x 10 = 1.80; 11.80 rounds to 12; 12 + 50 = 62; 500 - 62 = 438; 438/500 = 87.6%; 10 + 11 + 3 = 24; 5,000/10 = 500; 5,000/24 = 208.3; 208/438 = 0.48; 39 + 26 + 18 = 83 hours and 83/13 = 6.4; 55/0.01 = 5,500; 5,000 + 1,000 + 500 = 6,500; 12,000 - 1,488 - 5,000 - 1,500 - 5,000 = -1,000; 5,000 + 5,000 + 1,500 = 11,500; (500 + 1,667 + 417)/438 = 5.9; 8 x 438 - 2,584 = 920; (10,000 + 2,584)/438 = 28.7. All correct. This confirms the arithmetic only. It does not confirm the inputs. |
| forge-v1.md#C01 and 01-local-market.md#C22 | Bhagirath IAS Pune fees about Rs 65,000-95,000, registration Rs 5,000/10,000 non-refundable, batches of 50-75 | https://collegedunia.com/institute/314-bhagirath-ias-academy-pune | UNREACHABLE (tool failure) | Demand evidence (D01). Struck even though the tool, not the source, failed. |
| 01-local-market.md#C23 (forge-v1.md#C01) | Dnyandeep Academy Rs 60,000-1,25,000; UPSC prelims Rs 70,000, mains Rs 50,000 | https://collegedunia.com/institute/4208-dnyandeep-academy-pune-pune | UNREACHABLE (tool failure) | Demand evidence (D01). The Prithvi page (01#C24) was not tried separately. |
| forge-v1.md#C02 | MoE coaching guidelines circulated to states 2024-01-16; easy-exit and pro-rata refund; advisory | https://rsdebate.nic.in/bitstream/123456789/750740/1/PQ_265_31072024_U983_p142_p143.pdf | UNREACHABLE (tool failure) | The same ministry date and advisory status are in prosecution-market-v1.md#C03, from a different rsdebate URL that I did not open. Load-bearing for KM4. |
| forge-v1.md#C04 | Pune District Consumer Forum coaching refund order Rs 25,000 plus 9% plus Rs 10,000; enrolment 2014 | https://lawtrend.in/consumer-court-directs-coaching-institute-to-refund-rs-25000-along-with-rs-10000-as-compensation-to-the-student | UNREACHABLE (tool failure) | Forge itself says the order is undated. |
| forge-v1.md#C05 | Notice prices Rs 500 and Rs 1,499 (same pages as economics#C01) | https://join.consumer-voice.org/legal/ ; https://www.incorpx.io/legal-notice-drafting | UNREACHABLE (tool failure) | Duplicate of economics-v1.md#C01. Demand evidence (existing spending on a worse solution). |
| forge-v1.md#C07 | NCH recovered Rs 1.56 crore for 600+ coaching students as of 2025-02 | https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres | UNREACHABLE (tool failure) | Evidence of a free substitute, not of demand. |
| forge-v1.md#C08 | NCH coaching complaints 4,815, 5,351 and 16,276 over 2021-24 | https://www.newsonair.gov.in/department-of-consumer-affairs-facilitates-refund-of-more-than-%e2%82%b9-1-cr-to-aspirants-students-of-various-coaching-institutes | UNREACHABLE (tool failure) | Offered as the "why open now" reason. The etvbharat URL was not tried. |
| 01-local-market.md#C38 | Jan 2024 Education Ministry guidelines call for pro-rata refunds; NCH 1915 handles refund requests | https://righttoinformation.wiki/practical-guides/coaching-institute-refund-batch-cancellation-poor-service | UNREACHABLE (tool failure) | Load-bearing for the idea's premise. The source is a non-official wiki (prosecution-market-v1.md#C06 says it could not match the pro-rata claim to the official text). |
| 01-local-market.md#C47 | Pune consumer forum held fees cannot be withheld; pro-rata refund ordered; date not stated | https://www.pagalguy.com/articles/how-practical-is-it-to-seek-a-refund-from-your-coaching-institute-the-one-you-left-halfway | UNREACHABLE (tool failure) | The claim itself says the date is not stated. |
| 01-local-market.md#C37 | DPDP Rules notified 2025-11-14, phased compliance about 18 months | https://www.seqrite.com/blog/what-is-the-dpdp-act-2025-key-rules-compliance-requirements-and-business-impact/ | UNREACHABLE (tool failure) | Random sample. |
| 02-signals.md#S10 | PM announced free online coaching for competitive exams, 2026-08; student protests 2026-07-30 | https://yourstory.com/2026/08/pm-modi-announces-free-online-coaching-for-youth | UNREACHABLE (tool failure) | Used in FM4 and in the forge need gap. |
| prosecution-execution-v1.md#E1 | Delhi HC Dec 2024 (Anuj Kumar Chauhan v. LG NCT Delhi, W.P.(C) 17737/2024): non-advocates barred from consumer courts on authority letters | https://www.livelaw.in/amp/high-court/delhi-high-court/delhi-high-court-bars-non-advocates-from-appearing-before-consumer-courts-279456 | UNREACHABLE (tool failure) | Tried twice. Load-bearing for FE1 (FATAL). Even if verified, it concerns appearing before consumer courts, not paid drafting of letters, which is what the product does. |
| prosecution-execution-v1.md#E2 | Summary says Advocates Act s.29 limits law practice to advocates | https://desikaanoon.in/delhi-high-court-non-advocates-representation-2024 | UNREACHABLE (tool failure) | Load-bearing for FE1 (FATAL). E2 also says no source was found on the question, which is an absence statement, not a fact. |
| prosecution-execution-v1.md#E5 (FE4 evidence) | Maharashtra draft Private Coaching Centers Act 2026: pro-rata refund, about 10 days, registration, fee disclosure, objections to 2026-09-04 | https://www.scconline.com/blog/post/2026/08/25/draft-maharashtra-private-coaching-centers-act-2026/ | UNREACHABLE (tool failure) | Load-bearing for FE4 (FATAL). The second URL (freepressjournal) and the careers360 URL were not tried separately. |
| prosecution-execution-v1.md FE2 evidence | Conservative case: about 8 files a month, Rs 920 net a month, paid CAC Rs 5,500 vs contribution Rs 438 | economics-v1.md Calculations | VERIFIED | The figures match the arithmetic verified above. FE2 relies on the economics file, not on a URL. The "does not return a meaningful amount" judgement is an opinion, not a claim. |

## Struck claims
Each of these is struck as UNREACHABLE (tool failure). The sources may be accurate. Struck claims are removed from the Judge's evidence all the same.
- economics-v1.md#C01 — UNREACHABLE (tool failure) — both price-anchor URLs unopened; the conservative price rests on it
- economics-v1.md#C03 — UNREACHABLE (tool failure) — UPI MDR; not used by the conservative case
- economics-v1.md#C08 — UNREACHABLE (tool failure) — CPC Rs 6-55; sets the Rs 5,500 paid CAC
- economics-v1.md#C13 — UNREACHABLE (tool failure) — Balaji holding; basis for FE1
- economics-v1.md#C14 — UNREACHABLE (tool failure) — NCH complaint count
- economics-v1.md#C15 — UNREACHABLE (tool failure) — Rs 1.56 crore recovered via NCH
- economics-v1.md#C17 — UNREACHABLE (tool failure) — GST threshold
- forge-v1.md#C01 — UNREACHABLE (tool failure) — coaching fees; demand anchor D01
- forge-v1.md#C02 — UNREACHABLE (tool failure) — MoE guidelines date and scope
- forge-v1.md#C04 — UNREACHABLE (tool failure) — Pune forum order
- forge-v1.md#C05 — UNREACHABLE (tool failure) — competitor notice prices; the only "existing spending on a worse solution" evidence offered
- forge-v1.md#C07 — UNREACHABLE (tool failure) — NCH recoveries
- forge-v1.md#C08 — UNREACHABLE (tool failure) — NCH complaint trend
- 01-local-market.md#C22 — UNREACHABLE (tool failure) — Bhagirath fees (D01)
- 01-local-market.md#C23 — UNREACHABLE (tool failure) — Dnyandeep fees (D01)
- 01-local-market.md#C37 — UNREACHABLE (tool failure) — DPDP notification date
- 01-local-market.md#C38 — UNREACHABLE (tool failure) — Jan 2024 guidelines, helpline
- 01-local-market.md#C47 — UNREACHABLE (tool failure) — Pune forum holding
- 02-signals.md#S10 — UNREACHABLE (tool failure) — free coaching announcement
- prosecution-execution-v1.md#E1 — UNREACHABLE (tool failure) — Delhi HC order; FE1
- prosecution-execution-v1.md#E2 — UNREACHABLE (tool failure) — Advocates Act s.29 summary; FE1
- prosecution-execution-v1.md#E5 — UNREACHABLE (tool failure) — Maharashtra draft Act; FE4

Dependent claims not individually opened and not listed above:
- 01-local-market.md#C24 (Prithvi fees), forge-v1.md#C12 and #C13 (same sources as C08 and C07), forge-v1.md#C03, #C09 to #C11, and all of prosecution-market-v1.md#C01-C08. I could not check them with a working fetch. They were not part of the table, and the Judge should treat them as unchecked, not as verified.
- Forge-v1.md#C13 (about Rs 26,000 per student) is arithmetic from C07: 1.56 crore / 600 = Rs 26,000, which is correct. It is struck with its input.

## Assumptions in load-bearing positions
- economics-v1.md#C02 — ASSUMPTION used as the basis of the conservative price (Rs 500). No buyer of this exact service was found.
- economics-v1.md#C05 — ASSUMPTION: 10% refund or concession allowance in conservative COGS.
- economics-v1.md#C07 and forge-v1.md#C16 — ASSUMPTION: 45 minutes per file, behind the K2 fit (83 of 130 hours).
- economics-v1.md#C09 — ASSUMPTION: 1% click-to-paid, behind the Rs 5,500 paid CAC and behind FE2.
- economics-v1.md#C10 and #C11 — ASSUMPTION: the conservative customer count (24) and the Rs 5,000 boost spend. These come from forge-v1's unsourced Path to first 100 table.
- economics-v1.md#C12 — ASSUMPTION: Rs 5,000 advocate review. This is part of capital to first revenue and no quote was found.
- forge-v1.md#C15, #C17, #C18, #C19, #C20, #C21 — ASSUMPTION: Rs 799 price acceptance, lawfulness of non-lawyer drafting (basis of FE1 and KE2), Pune dispute volume (basis of KM2, FM3 and FE2), refund success rate, group permission (KE3), and that free routes do not make the product redundant.
- forge-v1.md#C06 — ASSUMPTION: the gap exists (6 searches found no coaching-specific service). Absence in search results.
- Contract-level ASSUMPTION in economics-v1.md Constraint check K9: employer permits side work.
- Base-column COGS of Rs 27 (economics-v1.md Scenarios) shows no arithmetic. The file's inputs give 3% x 799 = Rs 24 (or about Rs 43 with the gateway fee), so Rs 27 does not follow from either. The file labels base figures as rough estimates and does not argue from them, so I have not struck it. Neither base nor optimistic is used by the conservative test.

## Summary
- verified: 2 (both arithmetic checks against the file's own inputs, not source checks), misrepresented: 0, unreachable: 22 (of which tool failure: 22), unsourced: 0
- tool-failure strikes: 22. Every URL check failed because of the fetch tool, not because of a source. The main session should re-run this audit once fetch works. The result may change substantially.
- load-bearing struck claims: economics-v1.md#C01 (conservative price anchor), #C08 (paid CAC), #C13 (legal exposure for FE1), forge-v1.md#C01 and #C05 (demand evidence), 01#C22 and #C23 (D01 anchor), prosecution-execution-v1.md#E1, #E2 (FE1) and #E5 (FE4).
- demand evidence surviving the audit: none. Every demand item (D01 listing prices, the Rs 500 and Rs 1,499 notice prices, NCH recoveries) rests on a struck URL. Both prosecutors also say no seller of this service was shown with paying customers or reviews.
