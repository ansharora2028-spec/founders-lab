---
name: scoring-rubric
description: The venture screen score (0-25) used only to rank ideas, and the Judge's PASS / REVISE / KILL decision rule that no score can override. Use when screening ideas or ruling on a verdict.
user-invocable: false
---

# venture scoring rubric

## Part 1 — Screen score (0–25). Ranking only.

Five dimensions, each 0–5. Score each one with a one-line justification that cites claim ids or signal ids.

### Signal strength (0–5)
| score | meaning |
|---|---|
| 0 | no cited signal, or the cited signal does not support the idea |
| 1 | one weak signal |
| 2 | one medium signal, or several weak ones |
| 3 | one strong signal, or two medium signals |
| 4 | a strong signal plus corroboration from a second independent source |
| 5 | multiple strong, recent, independent signals, at least one local to the target market |

### Constraint fit (0–5)
Any HARD-constraint violation means the idea is **REJECTED**, not scored.
| score | meaning |
|---|---|
| 1 | fits only by using several FLEXIBLE stretches whose unlock conditions are uncertain |
| 2 | needs one FLEXIBLE stretch whose unlock condition is uncertain |
| 3 | fits, but close to the edge of at least one constraint |
| 4 | fits with some slack |
| 5 | fits comfortably on every constraint |

### Novelty
| state | score |
|---|---|
| open (no direct competitor found in the target market) | 5 |
| contested (1–4 direct competitors, none dominant) | 3 |
| crowded (5+ direct competitors, or one dominant incumbent) | 1 |

"Open" is not automatically good: an open market with no demand evidence will still die at Kill.

### Fit with unfair advantages (0–5)
| score | meaning |
|---|---|
| 0 | none of the user's advantages apply, or the user stated none |
| 1–2 | a minor advantage applies (e.g. language, general familiarity) |
| 3 | one stated advantage materially lowers cost or CAC |
| 4–5 | the idea depends on a stated advantage that competitors lack |

### Speed to first revenue (0–5)
Relative to the contract's time-to-first-revenue constraint.
| score | meaning |
|---|---|
| 0 | first revenue clearly beyond the HARD limit (that is a rejection) |
| 1 | at the limit |
| 3 | within about half the limit |
| 5 | first paid transaction plausible within 2–4 weeks |

### Use
- The screener ranks by total score. Ties are broken by signal strength, then by constraint fit.
- The main session carries the top N forward (quick 2, standard 3, deep 5; `check` carries the user's idea, and `check+variants` the user's idea plus the best variant, unless rejected on a HARD constraint).
- **The screen score is used only for ranking. It never decides a PASS.**

## Part 2 — The Judge's decision rule. Overrides every score.

Apply to claims that **survived the audit** only. Struck claims do not exist.

Definitions:
- A criterion's status is the **lower** of the two prosecutors' assessments where they overlap, and the Judge's own reading of the surviving evidence otherwise. Order: NOT MET < INSUFFICIENT EVIDENCE < MET.
- **INSUFFICIENT EVIDENCE** counts as NOT MET for PASS purposes. It counts as FIXABLE for REVISE only if the missing evidence is obtainable through desk research (web search, public data, published reports), not through running an experiment, building a product or surveying customers.
- **Demand evidence** is one of: competitors with verifiable revenue or paying customers; measurable search demand (a sourced volume or trend figure); existing spending on a worse solution. It must be VERIFIED by the auditor.

Rule, applied in this order:

1. **HALT** if the kill-criteria hash does not match the hash in `run-log.md`.
2. **KILL** if any of:
   - a FATAL flaw survived the audit;
   - a locked criterion is NOT MET and has no plausible fix;
   - the conservative economics break a HARD constraint;
   - a fix would change the customer, problem or revenue model and the run has used 2 pivots.
3. **PASS** only if all of:
   - every locked criterion is MET;
   - demand evidence is positive and verified;
   - the conservative economics are positive and fit the contract (FLEXIBLE stretches only where the unlock condition is met and stated).
4. **REVISE** only if all of:
   - it is round 1;
   - every failure is FIXABLE;
   - no fix would change the customer, problem or revenue model.
5. Otherwise **KILL**. A REVISE in round 2 is a KILL.

**Pivot candidate (KILL only).** The Judge writes one only if all of these hold. Otherwise it writes `- none` and the reason:
- the verdict is KILL;
- a decisive reason is that the only plausible fix changes the customer, the problem or the revenue model (so REVISE was unavailable);
- `run-log.md` shows fewer than 2 pivots used;
- the candidate changes at least one of those three fields, keeps the rest of the idea, and fits every HARD constraint in `00-contract.md`;
- the change is grounded in surviving (unstruck) evidence that the Judge cites, not invented.
A candidate never changes the verdict. The killed idea stays killed; the candidate is a new idea that must survive Screen, freshly locked criteria, forge and kill on its own.

Confidence (1–10) reflects the quality of the surviving evidence, not how much the Judge likes the idea. Lower it when local coverage is below 5, when load-bearing inputs are ASSUMPTIONs, or when the auditor struck many claims.

**No numeric score can override this rule.** A 25/25 screen score that fails rule 3 is a KILL.
