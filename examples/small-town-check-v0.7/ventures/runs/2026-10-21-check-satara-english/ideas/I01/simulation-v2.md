---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: main
version: 2
created: 2026-10-21T10:36:19Z
---

## Simulation
- method: 5,000 Monte Carlo runs over 12 months, triangular distributions from each input's low / likely / high, seed 42 (deterministic: re-running gives the same result)
- **viable share: 0.0%** of runs break even (monthly profit ≥ 0, after marketing) by month 2 **and** never need more than INR 75,000 of cash
- break even by month 2: 0.0% · stay within the capital limit: 17.6% · never break even within 12 months: 63.9%
- runs where the founder hit the 12 h/week limit (growth capped by time): 7.6%
- viable-on-paper bar (≥ 70% viable and ≥ 90% within capital): **NOT MET**

| metric | P10 (cautious) | P50 (typical) | P90 (good) |
|---|---|---|---|
| monthly profit in month 12 | -INR 5,178 | -INR 1,219 | INR 3,609 |
| cumulative cash after month 12 | -INR 133,998 | -INR 96,627 | -INR 57,917 |
| most cash needed at any point | INR 68,123 | INR 97,107 | INR 133,998 |

## Sensitivity (what matters most)
Month-12 monthly profit when one input moves from its low to its high value and every other input stays at its likely value (base case: -INR 1,298).

| rank | input | at low | at high | swing |
|---|---|---|---|---|
| 1 | reach_per_month | -INR 3,490 | INR 5,279 | INR 8,769 |
| 2 | conversion_rate | -INR 4,587 | INR 3,635 | INR 8,221 |
| 3 | founder_hours_fixed_per_week | -INR 1,298 | -INR 7,875 | INR 6,577 |
| 4 | fixed_cost_per_month | -INR 48 | -INR 5,423 | INR 5,375 |
| 5 | price | -INR 3,144 | INR 548 | INR 3,691 |
| 6 | monthly_churn | -INR 366 | -INR 2,761 | INR 2,396 |
| 7 | variable_cost_per_unit | -INR 1,144 | -INR 1,452 | INR 308 |
| 8 | cac | -INR 1,250 | -INR 1,435 | INR 185 |
| 9 | units_per_customer_per_month | -INR 1,298 | -INR 1,298 | INR 0 |
| 10 | setup_cost | -INR 1,298 | -INR 1,298 | INR 0 |
| 11 | founder_hours_per_unit | -INR 1,298 | -INR 1,298 | INR 0 |

## Money gate
- best-case viable share (no evidence haircut, the builders' numbers at face value): 34.2%; gate threshold 20%
- **money gate: PASS**

### What would have to change
Each row moves ONE input in its good direction, everything else unchanged, until 70% of runs are viable (with evidence haircuts). Likely values shown.

| input | now (likely) | would need (likely) | change |
|---|---|---|---|
| reach_per_month | 67.50 | 499.36 | x7.40 |
| conversion_rate | 0.030 | 0.222 | x7.40 |
| founder_hours_fixed_per_week | 10.62 | not reachable by this input alone | beyond x20 |

## Inputs after evidence haircut
| input | low | likely | high | evidence | haircut |
|---|---|---|---|---|---|
| price | 450.00 | 600.00 | 750.00 | assumption | 25% |
| units_per_customer_per_month | 0.75 | 0.75 | 0.75 | assumption | 25% |
| variable_cost_per_unit | 25.00 | 37.50 | 50.00 | assumption | 25% |
| fixed_cost_per_month | 6,625.00 | 7,875.00 | 12,000.00 | assumption | 25% |
| setup_cost | 25,625.00 | 38,750.00 | 77,500.00 | assumption | 25% |
| reach_per_month | 45.00 | 67.50 | 135.00 | assumption | 25% |
| conversion_rate | 0.015 | 0.030 | 0.053 | assumption | 25% |
| cac | 146.25 | 170.00 | 237.50 | assumption | 25% |
| monthly_churn | 0.050 | 0.075 | 0.125 | assumption | 25% |
| founder_hours_fixed_per_week | 8.75 | 10.62 | 12.50 | assumption | 25% |
| founder_hours_per_unit | 0.04 | 0.06 | 0.09 | assumption | 25% |
