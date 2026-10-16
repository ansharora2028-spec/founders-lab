---
run_id: 2026-10-16-check-spoken-english-satara
agent: main
version: 1
created: 2026-10-16T09:22:16Z
---

## Summary
- ideas generated: 1, screened out: 0, not carried: 0, killed: 1, pivoted: 0

## The ideas, explained
### I01 — After-school spoken-English batches for class 6-10 students in Satara, 1 hour on weekday evenings, ₹600 per student per month
- how it works: Class 6-10 students attend a 1-hour weekday-evening speaking batch (conversation, role-play, short talks) in a small room near a school. The founder teaches it, fills the first batch through her 4 parent WhatsApp groups and word of mouth, and collects fees by UPI or cash each month. Assumed: 3 evenings a week, 25 or fewer students per batch (03-ideas.md; ideas/I01/forge-v1.md narrows the first batch to class 8-10).
- need gap: Parents pay ₹800-1,500 per subject for school tuition (founder-counted) and say tuition covers grammar, not speaking. A spoken-English class near the bus stand charges about ₹1,000 with batches of 30 (founder-heard). The gap is a smaller in-person batch at ₹600 from a teacher parents know. No review or order data for any Satara seller could be found, so the gap rests on the founder's report (03-ideas.md; strategy-v1.md A1).
- how it makes money: Parents pay ₹600 per student per month. The main costs are the room (₹4,000-6,000 a month, founder-heard) and the founder's time. Break-even is about 8-10 students at the stated price. In the conservative case it is 15 students against about 2.5 modelled (economics-v1.md).
- what happened: KILL, round 1, confidence 6. The conservative economics break K1 and K5 over 12 months (cumulative cash about -₹99,400; passes -₹75,000 in month 8 without a stop rule), and only 2.6% of simulated cases break even by month 2 (ideas/I01/verdict-v1.md; simulation-v1.md).

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I01 | After-school spoken-English batches, class 6-10, Satara, ₹600/month | ideas/I01/verdict-v1.md | economics-v1.md Constraint check (K1, K5 break over 12 months); simulation-v1.md (2.6% viable vs 70% bar); no verified positive demand evidence (audit-v1.md) |

## Estimated savings (ESTIMATE)
- capital saved: ₹30,000-75,000
- months saved: 3-8 months of weekday evenings (about 7-8 hours a week)
- assumptions:
  - setup of about ₹29,000 (chairs, board, deposit, paperwork, printing) is spent before the founder learns enrolment is low (economics-v1.md, all ASSUMPTION inputs);
  - rent and other costs of about ₹6,800 a month run for 3-8 months before a stop decision;
  - without a written stop rule, losses continue towards the ₹99,400 twelve-month figure; the founder would more likely stop between months 3 and 8;
  - a refundable deposit (₹12,000) may be recovered, which lowers the loss;
  - all of this rests on assumed reach, conversion and churn, which nobody has tested in Satara.

## Patterns across deaths
- One idea only. The decisive pattern: a ₹600 price with a ₹4,000-6,000 room needs 8-15 paying students, and the founder's reach (300 parents) at an untested conversion rate does not reliably produce them within the 2-month window.
- Demand for kids' spoken English in Satara is evidenced only by founder hearsay and one ₹2,000 seller listing. Online data for Satara is thin (local coverage 3/10), so this is a gap in evidence, not proof that parents will not pay.
- The draft Maharashtra private-coaching Act is unresolved (draft; under-13 bar; registration above 25 students; fines of ₹1 lakh and up). One fine would exceed the ₹75,000 loss limit.

## Why the search missed
| idea | cause of death | where it should have been caught | type |
|---|---|---|---|
| I01 | conservative economics fail with a rented room; no verified local demand evidence | generator: no demand anchor with orders or reviews (D01-D03 all weak); a paid room makes break-even depend on 8-15 students | generation |
- Not a miss in the usual sense: the user brought the idea, so there were no alternatives to search. The cause is the idea's cost structure (rent) set against an untested enrolment rate.
- generation lessons for the next run:
  - test with a zero-rent venue (home, a borrowed school or community hall) so break-even drops to about 2 students;
  - collect paid pre-enrolments from parents before any room is rented;
  - read the official text of the draft Maharashtra Act before spending anything, and confirm whether spoken English is covered and whether the 25-student limit is per batch or per centre;
  - count class 6-10 enrolment at the 6 nearby schools (UDISE+) to size the market.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K9 | rent a room near a school, only within K1 | no stretch beyond K1 | I01 | the room is the cost that breaks the model; the contract only lets the room be an option, so a zero-rent venue is a design choice inside the contract, not a stretch |
| K4 | basic Instagram marketing | learnable skills | I01 | more reach per month is the second-biggest lever (simulation-v1.md sensitivity), but only if conversion is also proven |

HARD constraints K1 (₹75,000), K5 (cannot lose more than ₹75,000) and K6 (2 months to first revenue) were decisive. Only the user can change the contract.

## Directions for the next run
- Re-run with a zero-rent, pre-enrolment version of the same idea: `/venture:check "Spoken-English batch for class 8-10 in Satara at a free or borrowed venue, ₹600 per month, paid pre-enrolment of 10 students before starting" --variants`.
- Start from what held up: parents already pay ₹800-1,500 per subject (founder-counted), the founder reaches about 300 parents, and PW Pathshala is the only national brand with a Satara centre (class 8-10 Maths and Science, not English).
