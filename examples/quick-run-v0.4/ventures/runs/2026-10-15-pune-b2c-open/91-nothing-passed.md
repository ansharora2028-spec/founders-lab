---
run_id: 2026-10-15-pune-b2c-open
agent: main
version: 1
created: 2026-10-15T10:57:02Z
---

## Summary
- ideas generated: 3, screened out: 0, not carried: 1, killed: 2, pivoted: 0
- Every source fetch in this run failed with "proxy refused the connection" (both scouts, all auditors, and the forge, prosecutor and judge agents that tried). No page was opened by any agent. Every claim in the run rests on search-result text. The audits struck 22 of 22 (I01 round 1), 22 of 22 (I03 round 1) and 23 of 23 (I01 round 2) URL rows as UNREACHABLE; every one was a tool failure, not a source failure. Local data coverage is 4/10 (01-local-market.md § Coverage).

## The ideas, explained
### I01 — Refund-claim file for Pune coaching students who leave a course (MPSC/UPSC and similar), ₹799 per file
- how it works: A student sends the fee receipt and the institute's terms over WhatsApp. The founder fills a spreadsheet that works out the pro-rata refund, and the student gets a calculation sheet, a letter and the steps to file on the National Consumer Helpline (1915). Round 2 narrowed the letter to a generic fill-in template, to reduce the risk of acting as a lawyer (forge-v2.md, How it works).
- need gap: The student today accepts the loss, pays for a notice (priced at ₹500 to ₹1,499 in the forge file, sources struck), or reads free guides. The gap claimed is that no local, Marathi-language, done-for-you option was found; the forge file calls absence in search results weak evidence (forge-v2.md#C06).
- how it makes money: The student pays ₹799 once (economics modelled the conservative price at ₹500). Conservative case: contribution about ₹413 per file, about 8 files a month, about ₹720 net a month, ceiling about ₹4,437 a month at the 10-hour cap (economics-v2.md; verdict-v2.md, decisive reason 4).
- what happened: KILL, round 2, confidence 7 (ideas/I01/verdict-v2.md). Decisive reason as written: "This is round 2. PASS requires every locked criterion MET and verified demand evidence. Six criteria are NOT MET (KM1, KM4, KE1, KE2, KE3, KE5) and four are INSUFFICIENT EVIDENCE, which counts as NOT MET for PASS. A REVISE in round 2 is a KILL (rule 6; rubric rule 5)."

### I02 — Daily spoken-English practice on WhatsApp for Marathi and Hindi speakers in Pune, ₹499 per month
- how it works: The customer replies to a daily prompt with a voice note and gets corrected text and tips in Marathi or Hindi from an AI model the founder configures with no-code tools (03-ideas.md, I02).
- need gap: Offline Pune institutes cost ₹5,000 to ₹14,000 a month in batches; free apps and AI tools exist; the idea says the gap is a guess (03-ideas.md, I02).
- how it makes money: ₹499 a month, delivery about ₹130 per customer (ASSUMPTION), about 40 customers would give about ₹20,000 a month (ASSUMPTION) (03-ideas.md, I02).
- what happened: NOT CARRIED (rank). Screened 13/25, ranked third behind I01 (14) and I03 (13, higher market proof), with 2 carried in quick mode (04-screen.md § Ranking). It was never forged, criteria-written or prosecuted, so nothing here says it would have failed.

### I03 — Pre-booked home deep-clean for 1-2 BHK flats with a photo checklist and a free re-clean if areas are missed, in one or two Pune neighbourhoods
- how it works: The customer books on WhatsApp or Instagram and gets a fixed quote and a room-by-room checklist. Independent cleaning teams do the work and upload before and after photos; the founder checks the photos and a missed item triggers a free re-clean. The founder does no cleaning (03-ideas.md, I03).
- need gap: Households pay Urban Company or use unvetted local teams; the idea cites reviewer complaints about skipped areas and extra fees, from one Pune reviewer page. Round 1 prosecution found Urban Company's Pune pages already advertise a 3-day guarantee and ₹10,000 damage cover (prosecution-execution-v1.md, KE5 assessment, as summarised by the prosecutor; the cited pages were struck by the auditor as unreachable).
- how it makes money: Fixed price per booking, team paid per job, founder keeps the difference. Conservative case: price ₹2,999, cost ₹3,250, margin −₹251 per job before acquisition cost and −₹813 after it, no break-even at any volume (economics-v1.md; the team rate behind it is an unsourced assumption).
- what happened: KILL, round 1, confidence 5 (ideas/I03/verdict-v1.md). Decisive reason as written: "PASS is unavailable. It needs every criterion MET. Only the economics arithmetic survived the audit (1 of 23 claims checked verified). Five criteria are NOT MET and four are INSUFFICIENT EVIDENCE."

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I01 | Refund-claim file, ₹799, Pune coaching students | ideas/I01/verdict-v2.md | KILL round 2. Rule 4: five of eleven fix rows carry evidence NONE and score as no fix. "No demand evidence survives." Conservative size about ₹720 net a month at 8 files (economics-v2.md, arithmetic VERIFIED). diff-v2.md concedes "Not fixed to the stated bar" on seller demand, and that Maharashtra's rules are advisory/draft, so these findings do not depend on the tool-failure strikes. |
| I02 | WhatsApp spoken-English practice, ₹499/month | (none) 04-screen.md | NOT CARRIED (rank): 13/25, third of three; quick mode carries 2. |
| I03 | Pre-booked home deep-clean with photo checklist | ideas/I03/verdict-v1.md | KILL round 1. Conservative economics −₹251 per job before acquisition cost, −₹813 after; about 10.7 founder hours a week at 25 jobs against the 10-hour HARD cap (K2); no demand evidence survived the audit (tool-failure strikes). Judge: "The kill is for lack of positive evidence, not because a decisive contradiction was proved." |

## Estimated savings (ESTIMATE)
- capital saved: ₹10,000 to ₹60,000, counting only the modelled outlay of the two carried ideas (I01 peak outlay about ₹11,500 in round 1 and about ₹19,500 in round 2 economics; I03 capital to first revenue ₹29,500 and about ₹58,300 by month 3 per verdict-v1.md). The upper end applies to I03 only.
- months saved: 2 to 4 months of part-time work at 10 hours a week before the founder would see that the monthly result is small (I01) or negative (I03). I01 first revenue was modelled at about 1.5 to 2 months; I03 at about 2 months.
- assumptions: (1) the founder would have launched the idea and run it for the modelled period; (2) the conservative-case economics are right, although their key inputs (team rate, conversion rates, CAC) are ASSUMPTIONs and most sourced inputs were struck for tool failure, so the true figures could be better or worse; (3) I03's certain loss of about ₹6,300 a month comes from economics-v1.md and rests on the unsourced team rate; (4) no income target is in the contract, so "viable size" is not a contract test. These are ranges, not findings. They are a weaker basis than usual because no source could be opened.

## Patterns across deaths
- No verified demand evidence for either carried idea. Both audits struck every demand source as UNREACHABLE; this is an environment failure. Rule 3 still requires verified demand evidence, so neither could PASS even with strong economics.
- Both ideas have thin per-month economics under the conservative case: I01 about ₹720 net a month at 8 files, I03 negative per job.
- The 10-hour HARD cap (K2) binds both: I01 breaks "every week" at about 10.5 hours in a heavy week (diff-v2.md#D11), I03 needs about 10.7 hours at 25 jobs.
- Legal and regulatory uncertainty was unresolved for both (I01: Advocates Act scope; I03: gig-worker and aggregator rules), and neither could be settled by desk research alone.
- Both rely on free or funded substitutes: the free National Consumer Helpline for I01, Urban Company at ₹2,999 for I03.

## Why the search missed
| idea | cause of death | where it should have been caught | type |
|---|---|---|---|
| I01 | No verified demand that anyone pays for refund-claim help; legal-scope question unresolved; conservative volume about 8 files a month | generator: demand anchor D01 showed coaching fees and complaints, not spending on refund help (screen scored market proof 2/5) | generation |
| I01 | 22 and 23 source strikes from the fetch tool, which lowered the judge's confidence and made the demand check impossible | environment: web fetch blocked for every agent | evidence access |
| I02 | Not tested | screen ranking (quick mode carries 2 of 3) | bad luck (rank) |
| I03 | Conservative economics negative: price capped by Urban Company's Pune price, team cost above it; 10.7 h/week at the volume needed | generator: its own longlist called it the thinnest margin (₹700 per job before CAC), and the screen scored constraint fit 2/5 | generation |
| I03 | All demand and price sources struck for tool failure | environment: web fetch blocked | evidence access |

- type is one of: generation (weak idea: no demand anchor, crowded, wrong segment, money math never worked) · constraint (good idea, but it breaks the contract) · evidence access (sources couldn't be opened: tool failure, thin local data) · bad luck (it was a reasonable bet that failed on new evidence)
- Read this honestly: both carried ideas have a generation cause (no demand anchor of spending, thin or negative money math) that does not depend on the fetch failures. The evidence-access problem is real and affects confidence and the demand check, but it is not the only reason the run missed. A second wave will not fix the evidence-access part until web access works.
- generation lessons for the next run:
  1. Start only from demand anchors where named sellers charge for the same job and a price or review count is findable (such as D05 deep-clean pricing, D08 spoken-English institutes, D10), and reject ideas whose only anchor is a complaint count (I01's D01).
  2. Do a volume-ceiling check at the K2 cap before carrying an idea: compute files or jobs per week at 10 hours and the monthly contribution at the conservative price, and drop ideas whose ceiling is a few thousand rupees a month. (I01's ceiling was about ₹4,437 a month.)
  3. Avoid legal-adjacent paid documents that need an advocate's opinion, and subcontracted physical services priced against a funded app's floor price (Urban Company ₹2,999 in this run's economics), unless the generator can show a team rate or price that works.
  4. Fix web access before running again: both scouts and every auditor were blocked, so a second wave would repeat the same evidence gap.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K4 | no-code tools; can hire freelancers within the capital limit (FLEXIBLE) | hiring freelancers, only if freelancer cost stays inside the K1 ₹1,00,000 cap | none | I03's team cost is already inside K1 and its loss is per job, so more freelancers do not fix it. I01 needed a written advocate opinion (about ₹5,000 per forge-v2.md, an ASSUMPTION), which would fit inside K1, but the verdict rests on missing demand evidence and scale, not on that opinion. |
- No FLEXIBLE constraint would have changed either verdict. The decisive HARD constraints were K2 (10 hours a week) for I03 and, for I01, the interaction of K2 with a small per-file contribution. Only the user can change HARD constraints; this report does not suggest it.

## Directions for the next run
- Fix web access first, then re-run the audits on the same ideas if the user wants a fair check of the struck demand claims (I01 audit-v1.md and audit-v2.md both say the strikes may reverse).
- Consider spaces where signals held up in the scouts' files and the founder's skills (spreadsheets, social media marketing, Marathi/Hindi/English) fit a digital, single-person deliverable: for example the spoken-English practice idea (I02, never tested), or a service built on D08 (Pune spoken-English institutes) or D09. These are starting points to test, not recommendations that they will pass.
- Use the lessons above: demand anchors with named sellers, a volume-ceiling check at the 10-hour cap, no legal-adjacent documents, and no subcontracted service priced against Urban Company's floor.
- Run `/venture:run --wave2 2026-10-15-pune-b2c-open` once web access works. It reuses the contract and the scouting files, so it needs no new scouting.
