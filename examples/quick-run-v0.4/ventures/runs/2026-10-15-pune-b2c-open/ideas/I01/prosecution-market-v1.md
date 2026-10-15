---
run_id: 2026-10-15-pune-b2c-open
idea_id: I01
agent: prosecutor-market
version: 1
created: 2026-10-15T10:44:03Z
---

## Inputs read
- <project>/ventures/runs/2026-10-15-pune-b2c-open/00-contract.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/01-local-market.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/02-signals.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I01/kill-criteria.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I01/forge-v1.md
- <project>/ventures/runs/2026-10-15-pune-b2c-open/ideas/I01/economics-v1.md
- Own web searches on 2026-10-15 (six, listed under Evidence). Search-result text only; no page was opened.

## Criteria assessment
| criterion | status | evidence (claim refs) | note |
|---|---|---|---|
| KM1 | NOT MET | forge-v1.md#C05, economics-v1.md#C01, C01, C02 | Threshold needs 3 named sellers charging individuals ≥₹500, at least 1 in Maharashtra, and at least 2 with paying-customer evidence (10+ reviews or a case count). Found: Consumer Voice "Consumer Mitra" at ₹500 plus postage (price only, no customer count) and IncorpX at ₹1,499 (price only). Neither is shown to be in Maharashtra. No review counts or case counts for any seller. Akosha's ₹499 complaint service is a 2011 listing, outside the 24-month window. Forge-v1.md#C22 admits no seller revenue was found. Prices alone do not show people pay. No shutdown cause was researched either. |
| KM2 | INSUFFICIENT EVIDENCE | forge-v1.md#C12, forge-v1.md#C14, C05 | Threshold: ≥2,000 education/coaching grievances a year in Maharashtra or ≥50,000 paying Pune coaching enrolments. Only national NCH coaching grievances are available (16,276 in 2023-24). No Maharashtra or Pune count exists in the files or in my search. The threshold may well be reachable (a Maharashtra share of even 12% of the national figure would clear it), but no data supports that share. Also, NCH grievances are mostly not Pune MPSC/UPSC classroom disputes, and the file's wedge is that segment. |
| KM3 | INSUFFICIENT EVIDENCE | forge-v1.md#C07, C06, C01, C02, C03 | Forge did not run the documented free-resource search the criterion asks for; its only check was 6 searches for paid services. Known free routes: NCH 1915 (free; 600+ students recovered ₹1.56 crore, forge-v1.md#C07), PaGaLGuY guide, righttoinformation.wiki guide which lays out a demand-letter structure and a 10-day notice. I found no free ready-made calculation sheet plus letter, so the 2-or-more trigger is not shown. But no paid-uptake evidence exists either, so if 2 free options are later found the idea has no fallback. Status cannot be set above INSUFFICIENT. |
| KM4 | NOT MET | forge-v1.md#C02, forge-v1.md#C03, C04, C05, C06 | Limb 1 (≥3 orders in last 36 months, ≥1 from Maharashtra) is probably satisfiable: Mumbai District Commission v. Rao IIT Academy (Maharashtra; livelaw URL, date not shown in snippet), Central Delhi and New Delhi orders, NCDRC VLCC. Limb 2 fails: the Jan 2024 MoE guidelines are advisory and were sent to states to adopt through their own law (forge-v1.md#C02 admits Maharashtra adoption was not verified); Maharashtra's coaching bill is still only a draft (see C03, C04). So "confirmed to cover private coaching institutes in Maharashtra" is not true as of today. The orders that exist rest on general consumer law, not the guidelines. The only Pune order found (forge-v1.md#C04) is undated, from a 2014 enrolment. |
| KM5 | INSUFFICIENT EVIDENCE | C07, forge-v1.md#C11 | Limb 1 (3 communities, 5,000+ combined) looks satisfiable: third-party trackers list Marathi MPSC Telegram channels at roughly 27,000 to 112,000 subscribers and Pune-tagged Instagram accounts at 26,000+ followers (numbers unverified, snapshot dates unclear). Limb 2 (10 public posts in 12 months complaining about coaching fees, refunds or batch changes) has no evidence. Forge-v1.md#C11 cites protests about paper leaks, which is not a fee complaint. Channel size also does not show permission to promote a paid service inside them. |

KE criteria: not assessed (owned by the execution prosecutor). One market observation relevant to KE4 is in FM5.

## Flaws
### FM1 — FIXABLE
- flaw: There is no demand evidence for paid refund-claim help. All demand evidence is coaching course prices and national complaint counts (forge-v1.md#C22). Rule 3 requires demand evidence (competitors with revenue, measurable search demand, or existing spending on a worse solution). The only comparable paid services have prices but no customers shown. The closest "worse solution" spending is a ₹500 lawyer-issued notice from a nonprofit.
- evidence: [C01] Consumer Voice lists legal notice drafting and issuing at ₹500 at standard rates, postage extra [source: https://join.consumer-voice.org/legal/]. No customer count or reviews found. [C02] Akosha charged ₹499 for a consumer complaint service, from a 2011 interview (dated) [source: https://ts.yourstory.com/2011/02/ankur-singla-founder-akosha-enabling-legal-solutions-online-for-consumers].
- what would fix it: opened pages showing ≥2 sellers with ≥10 dated customer reviews or a stated case count for consumer-complaint or refund drafting at ≥₹500, or a search-volume figure for "coaching fee refund" in Pune/Maharashtra. Desk research can obtain it (marketplace listings, Google Business reviews, Keyword Planner), but it may simply not exist.
- fix would change customer/problem/revenue model: no

### FM2 — FIXABLE
- flaw: The legal basis for the product is weaker in the target market than the pitch implies. The pitch rests on MoE guidelines that are advisory (forge-v1.md#C02), and Maharashtra has only a draft coaching bill. Orders found are for IIT-JEE, medical or other coaching in Mumbai, Delhi and Kerala, not Pune MPSC/UPSC academies in Sadashiv Peth. Whether a small local academy's registration fee ("non-refundable") would be reversed is untested. The 2024 Mumbai Rao IIT order shows deficiency-in-service reasoning but not the exact clause test.
- evidence: [C03] The MoE circulated its guidelines to states on 2024-01-16 asking them to consider them within a legal framework; Maharashtra told the Bombay High Court in March 2025 it had drafted a bill, and an August 2026 report describes a draft Maharashtra Private Coaching Centers (Registration and Regulation) Bill, 2026; passage not confirmed [source: https://rsdebate.nic.in/bitstream/123456789/750594/1/PQ_265_31072024_U984_p144_p145.pdf ; https://news.careers360.com/maharashtra-pvt-coaching-centres-regulation-bill-kota-institutes-99pc-state-classes-small-association-neet-2026-infra-standards/amp]. [C04] Mumbai District Commission held Rao IIT Academy liable for not refunding an advance course fee after withdrawal [source: https://www.livelaw.in/amp/consumer-cases/mumbai-district-commission-rao-iit-academy-refund-coaching-fee-withdrawal-admission-261464].
- what would fix it: ≥3 dated orders within 36 months against a non-refundable registration clause, including at least 1 from Maharashtra and ideally 1 against a UPSC/MPSC academy; a Maharashtra source stating that the MoE guidelines or the new bill apply. Desk research can obtain the orders; the bill status can be checked on the state legislature site.
- fix would change customer/problem/revenue model: no

### FM3 — FIXABLE
- flaw: Trigger frequency and pool size in Pune are unknown, and the economics file shows the business is small even if everything works. The conservative case is 24 files in 3 months (₹12,000 revenue, about ₹920 net a month); a ₹10,000 net month needs about 29 files a month, 3.6 times the conservative flow (economics-v1.md#Calculations). Forge's own path to 100 customers reaches about 70 in 3 months using only assumed conversions (forge-v1.md, Path to first 100). Purchase happens once per customer, at the moment of a dispute, so there is no repeat revenue and the pool refills only from new disputes.
- evidence: forge-v1.md#C14 (Pune complaint volume not found), forge-v1.md#C18 (volume assumed), economics-v1.md#C16 (one-time purchase), economics-v1.md#C14 (national volume only).
- what would fix it: a Pune or Maharashtra count of coaching disputes or enrolments (consumer commission statistics, NCH state dashboard, press with enrolment numbers). Partly desk-researchable; NCH state-wise data may need an RTI request, which takes longer than the run.
- fix would change customer/problem/revenue model: no

### FM4 — FIXABLE
- flaw: Free substitutes are strong and government-backed, and the customer's maximum paid alternative is cheap. NCH 1915 intervenes at no cost and reports ₹1.56 crore recovered for 600+ coaching students; a free demand-letter structure is published in guides; e-Daakhil has no fee for claims up to ₹5 lakh per forge's source. The PM announced free online coaching for exams (02 S10), which shrinks the future pool of paying coaching students. The only priced paid comparator (₹500 for a lawyer-issued notice) is below the ₹799 working price, so the product is not cheaper than a lawyer-issued notice at the low end.
- evidence: [C05] NCH 1915 handles coaching refund grievances and has facilitated refunds of ₹1.56 crore for 600+ students [source: https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]. [C06] A free guide sets out a written demand with a 10-day deadline and e-Daakhil escalation [source: https://righttoinformation.wiki/practical-guides/coaching-institute-refund-batch-cancellation-poor-service]. Also 02-signals.md#S10, forge-v1.md#C05.
- what would fix it: evidence that buyers pay for comparable help while NCH exists (paid sellers' review counts, case counts), plus an itemised comparison showing what the ₹799 file does that NCH/free guides do not. Desk research can partly supply it.
- fix would change customer/problem/revenue model: no

### FM5 — FIXABLE
- flaw: Legal-adjacent sale by a non-lawyer is unresolved, and it also affects whether customers will pay. Forge-v1.md#C17 left the question unresearched; economics-v1.md#C13 reports that the Supreme Court in Bar Council of India v. A.K. Balaji treated non-litigation drafting as practice of law. This is flagged for the execution prosecutor's KE2; as a market matter, a disclaimer that the product is "not legal advice" reduces the value the customer is paying for.
- evidence: economics-v1.md#C13; forge-v1.md#C17.
- what would fix it: a source showing paid non-lawyer document preparation of this kind is lawful and currently operates in India. Desk-researchable in part.
- fix would change customer/problem/revenue model: no

### FM6 — FIXABLE
- flaw: Graveyard not researched. Neither the forge nor the scouts identify any India consumer-grievance or complaint-drafting startup, its revenue or its cause of death. 01-local-market.md#C07 and #L07 acknowledge no Pune consumer failure data. The only precedent surfaced (Akosha, ₹499 complaint service, 2011) has no outcome in the files. I did not verify what happened to it and make no claim.
- evidence: [C02] (Akosha 2011 listing, above); 01-local-market.md (Launched and failed section: no relevant entry).
- what would fix it: named Indian consumer-complaint or legal-document startups, with revenue or shutdown evidence and cause of death (press reports, Tracxn/Entrackr, company blog posts). Desk-researchable.
- fix would change customer/problem/revenue model: no

No FATAL flaw is declared. FM1 is the one that decides the outcome: if desk research cannot produce paying-customer evidence for paid refund-drafting help, the idea has no demand anchor under rule 3.

## Evidence
- [C01] Consumer Mitra (Consumer Voice) lists legal notice drafting and issuance at ₹500 at standard rates with postage separate, and a subsidised ₹199 per hour for other document drafting. No customer numbers shown. (national) [source: https://join.consumer-voice.org/legal/]
- [C02] A 2011 interview says Akosha charged ₹499 for a consumer complaint service covering the notice, follow-up and complaint. Dated; outcome of the company not checked. (national) [source: https://ts.yourstory.com/2011/02/ankur-singla-founder-akosha-enabling-legal-solutions-online-for-consumers, 2011]
- [C03] Ministry of Education circulated its coaching-centre guidelines to states and UTs on 2024-01-16 asking them to consider them within an appropriate legal framework; they are not self-executing. Maharashtra told the Bombay High Court in March 2025 it had drafted a bill and was studying the guidelines; a draft Maharashtra Private Coaching Centers (Registration and Regulation) Bill, 2026 was reported in August 2026; passage unverified. (national / Maharashtra) [source: https://rsdebate.nic.in/bitstream/123456789/750594/1/PQ_265_31072024_U984_p144_p145.pdf ; https://www.livelaw.in/amp/high-court/bombay-high-court/state-tells-court-draft-bill-regulating-coaching-centres-to-be-introduced-in-monsoon-session-287446 ; https://news.careers360.com/maharashtra-pvt-coaching-centres-regulation-bill-kota-institutes-99pc-state-classes-small-association-neet-2026-infra-standards/amp]
- [C04] Mumbai District Commission held Rao IIT Academy liable for failing to refund an advance course fee after withdrawal (Maharashtra, IIT-JEE coaching, not MPSC/UPSC; order date not visible in the snippet). Other orders: Central Delhi 2023 against a medical coaching academy for a lumpsum fee; NCDRC VLCC order of ₹2,79,329 plus ₹50,000 (Kerala case). (other city: Mumbai / Delhi / Kerala) [source: https://www.livelaw.in/amp/consumer-cases/mumbai-district-commission-rao-iit-academy-refund-coaching-fee-withdrawal-admission-261464 ; https://www.livelaw.in/amp/consumer-cases/lumpsum-fee-in-advance-exploits-students-central-delhi-consumer-commission-orders-delhi-academy-of-medical-science-to-refund-1-lakh-236429 ; https://admin.mondaq.com/india/dodd-frank-consumer-protection-act/1631936/unscrupulous-coaching-institutes-have-no-right-to-retain-fees-of-students-who-leave-the-course-midway-due-to-dissatisfaction-with-the-services]
- [C05] NCH logged 16,276 student grievances in 2023-24, up from 5,351 and 4,815 in the two prior years; no state-wise coaching figure found. Maharashtra was third by call volume in a May 2013 national report (1,437 calls, all sectors; dated). The Department of Consumer Affairs reported ₹1.56 crore refunded to 600+ coaching students via NCH in February 2025. (national) [source: https://udayavani.com/?p=1707507 ; https://www.outlookbusiness.com/news/deptt-of-consumer-affairs-ensures-refund-of-rs-156cr-to-students-from-coaching-centres]
- [C06] A guide on righttoinformation.wiki describes the free route: written demand to the centre head, a 10-day deadline, NCH 1915, then e-Daakhil with an evidence PDF. It is a non-official site and says the pro-rata claim could not be matched to the official text. (national) [source: https://righttoinformation.wiki/practical-guides/coaching-institute-refund-batch-cancellation-poor-service]
- [C07] Third-party trackers list Marathi MPSC Telegram channels from about 27,000 (@mpscandolan, page dated August 2026) to about 112,000 subscribers, and Instagram accounts @mpscmantra (about 26,100 followers, Pune tag) and @mpsc_studentt (about 592,000, Pune tag, content mainly police and talathi recruitment). Engagement and location data unverified. No complaint-post counts found. [source: https://socialveins.com/influencer/instagram/mpscmantra ; https://playboard.co/en/search?q=MPSC ; https://tlmtr.io/en/channels/1203901022-mpscandolan/posts]
- [C08] Search for legal-service platform pricing (LegalKart, Vakilsearch, RegisterKaro) returned no consumer-complaint price and no review counts for these sellers. [source: https://www.registerkaro.in/consumer-complaint/consumer-complaint-in-gandhinagar]

## Round-2 notes (v2 only)
| diff row | accepted as fix | reason |
|---|---|---|
| n/a | n/a | Round 1. |
