---
run_id: 2026-10-21-check-satara-english
agent: main
version: 1
created: 2026-10-21T10:43:58Z
---

## Summary
- ideas generated: 1, screened out: 0, not carried: 0, killed: 1, pivoted: 0 (I01 is final status KILL, round 2)

## The ideas, explained
### I01 — After-school spoken-English batches for class 6-10 students in Satara, 1 hour on weekday evenings, ₹600 per student per month
- how it works: You rent a small room near a school and teach a 1-hour spoken-English class on weekday evenings, in English with Marathi explanation. Forge narrowed it to class 8-10 and a cap of 20 students per batch, with a free 30-minute demo. Parents hear about it in your 4 WhatsApp groups and from parents of past students, and pay each month by UPI or cash (03-ideas.md § I01; ideas/I01/forge-v1.md § How it works).
- need gap: Parents told you tuition teachers cover homework and grammar, not speaking, and the bus-stand class has batches of about 30. This is founder hearsay (FOUNDER-ESTIMATE). No public Satara review or complaint was found, and the peer-town count shows no under-supply (01-local-market.md; ideas/I01/forge-v2.md C04, C27).
- how it makes money: Parents pay a flat fee per student per month. The room costs ₹4,000-6,000 (founder estimate), but the only Satara commercial rents found were ₹22,000-25,000. Round 2 tested ₹800 as the base price with ₹600 as a test cell (ideas/I01/economics-v2.md; ideas/I01/diff-v2.md D1, D4).
- what happened: KILL, round 2, confidence 8. At ₹600 the conservative case needs ₹76,600 before the first student pays (limit ₹75,000), break-even is 14 students against a path of 10.5 by month 12, and cumulative cash at month 12 is -₹106,656. The ₹800 fix has no school-age price source (ideas/I01/verdict-v2.md).

## Deaths
| idea | pitch | verdict file | decisive evidence |
|---|---|---|---|
| I01 | After-school spoken-English batches, class 6-10, Satara, ₹600/month | ideas/I01/verdict-v2.md | economics-v2.md "Constraint check": K1 BREAKS (₹76,600 to first revenue vs ₹75,000; -₹106,656 at month 12), auditor re-computed the arithmetic as correct (audit-v2.md); simulation-v2.md: 0.0% viable, 17.6% within capital; FE2 FATAL: no verified school-age price of ₹800 or more |

## Estimated savings (ESTIMATE)
- capital saved: about ₹40,000-75,000 (ESTIMATE)
- months saved: about 6-12 months of part-time work (ESTIMATE)
- assumptions:
  - Setup of ₹31,000-62,000 (economics-v2.md and forge-v2.md C31, both built on ASSUMPTION inputs), plus 2-4 months of rent and supplies before enrolment reached break-even.
  - The founder would have run the class for 6-12 months before concluding that about 10 students could not cover rent and a fair wage.
  - Rent at the founder's ₹4,000-6,000 estimate for the low end, and at the ₹8,300 per month implied by the Radhika Road listing for the high end. The deposit is assumed lost only in part.
  - The founder's own hours (about 12 per week) are valued at zero.

## Patterns across deaths
- Only one idea, so the pattern is the idea's own. The price is set against what parents already pay for one subject of tuition (₹800-1,500), not against what a small room and one teacher cost to run.
- Every demand claim that matters is founder-reported (FOUNDER-COUNTED reach, FOUNDER-ESTIMATE gap and price). No Satara price, review or enrolment figure could be verified, so the idea never reached PASS or VIABLE ON PAPER.
- Both the capital limit (K1) and the 12-hour limit (K2) are HARD, with no slack. The same fixed cost (room) is spread over a student count capped by those limits.

## Why the search missed
| idea | cause of death | where it should have been caught | type |
|---|---|---|---|
| I01 | At ₹600 break-even is 14 students against a reachable 10.5, and setup plus two months of rent exceeds ₹75,000 | the user's own price and room-rent estimate; the money model (economics-v1.md) showed K1 breaking by about ₹4,000 in round 1 | constraint |
| I01 | The ₹800 fix has no verified school-age price in Satara, and the Satara demand sources (Justdial, Google Maps, reviews, enrolment tables) could not be opened | scout stage: only one Satara price (Success ₹2,000) was verified | evidence access |

- generation lessons for the next run:
  - Test the price before the room. A pre-sale of the class at ₹800 against ₹600 to 10 named parents is the one input that decides this idea, and it costs close to ₹0.
  - Price against the cost of delivery, not against per-subject tuition. With rent as the only fixed cost, work out the break-even student count at the founder's own rent quote first.
  - Prefer a model with no rent, such as using a free school room, a community hall or the founder's own home, or online batches, so that the fixed cost does not decide the outcome.
  - Collect the missing Satara data by phone or visit (price, batch size and reviews for Success, Goranga, Job 4U, Shivtej and Breath) before modelling.

## Flexible constraints that would most change the outcome
| K# | current | stretch range | ideas it would revive | how |
|---|---|---|---|---|
| K4 | basic Instagram marketing (FLEXIBLE) | not stated | none | the contract gives no stretch range and no unlock condition, and marketing was not the failing input |

K1 (capital), K2 (hours) and K6 (time to first revenue) are HARD and were decisive. Only you can change them.

## Directions for the next run
- Re-test the same idea as a no-rent model: a free or very cheap room (a school hall after hours, a community hall, or your own home), at ₹800 or more, with a 10-parent pre-sale before any spend. Command: `/lab:test "<revised idea>" --variants`.
- Test a smaller-batch premium variant at ₹1,000-1,500 for class 8-10 (the founder-heard bus-stand price is about ₹1,000 and Success lists ₹2,000), against a batch size of 6-10. The audit left the ₹800 and higher price unproven.
- If no variant clears the money gate, run `/lab:ideate` under the same constraints to look for a different idea.
