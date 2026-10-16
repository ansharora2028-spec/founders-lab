---
run_id: 2026-10-16-check-spoken-english-satara
idea_id: I01
agent: main
version: 1
created: 2026-10-16T09:12:00Z
---

## Simulation
- method: 5,000 Monte Carlo runs over 12 months, triangular distributions from each input's low / likely / high, seed 42 (deterministic: re-running gives the same result)
- **viable share: 2.6%** of runs break even (monthly profit ≥ 0, after marketing) by month 2 **and** never need more than INR 75,000 of cash
- break even by month 2: 2.6% · stay within the capital limit: 91.5% · never break even within 12 months: 40.0%
- runs where the founder hit the 12 h/week limit (growth capped by time): 0.1%
- viable-on-paper bar (≥ 70% viable and ≥ 90% within capital): **NOT MET**

| metric | P10 (cautious) | P50 (typical) | P90 (good) |
|---|---|---|---|
| monthly profit in month 12 | -INR 2,704 | INR 766 | INR 5,097 |
| cumulative cash after month 12 | -INR 72,996 | -INR 39,075 | INR 2,414 |
| most cash needed at any point | INR 23,725 | INR 42,443 | INR 72,996 |

## Sensitivity (what matters most)
Month-12 monthly profit when one input moves from its low to its high value and every other input stays at its likely value (base case: -INR 464).

| rank | input | at low | at high | swing |
|---|---|---|---|---|
| 1 | reach_per_month | -INR 4,311 | INR 4,024 | INR 8,335 |
| 2 | fixed_cost_per_month | INR 6,036 | -INR 2,089 | INR 8,125 |
| 3 | conversion_rate | -INR 4,311 | INR 3,383 | INR 7,693 |
| 4 | monthly_churn | INR 873 | -INR 2,571 | INR 3,445 |
| 5 | price | -INR 1,599 | INR 1,807 | INR 3,406 |
| 6 | cac | -INR 323 | -INR 1,272 | INR 949 |
| 7 | variable_cost_per_unit | -INR 369 | -INR 653 | INR 284 |
| 8 | units_per_customer_per_month | -INR 464 | -INR 464 | INR 0 |
| 9 | setup_cost | -INR 464 | -INR 464 | INR 0 |
| 10 | founder_hours_per_unit | -INR 464 | -INR 464 | INR 0 |
| 11 | founder_hours_fixed_per_week | -INR 464 | -INR 464 | INR 0 |

## Inputs after evidence haircut
| input | low | likely | high | evidence | haircut |
|---|---|---|---|---|---|
| price | 375.00 | 450.00 | 600.00 | assumption | 25% |
| units_per_customer_per_month | 0.75 | 0.75 | 0.75 | assumption | 25% |
| variable_cost_per_unit | 6.25 | 12.50 | 25.00 | assumption | 25% |
| fixed_cost_per_month | 375.00 | 6,875.00 | 8,500.00 | assumption | 25% |
| setup_cost | 5,000.00 | 23,750.00 | 36,250.00 | assumption | 25% |
| reach_per_month | 30.00 | 75.00 | 127.50 | assumption | 25% |
| conversion_rate | 0.015 | 0.038 | 0.060 | assumption | 25% |
| cac | 25.00 | 75.00 | 362.50 | assumption | 25% |
| monthly_churn | 0.062 | 0.100 | 0.188 | assumption | 25% |
| founder_hours_fixed_per_week | 6.25 | 7.50 | 8.75 | assumption | 25% |
| founder_hours_per_unit | 0.31 | 0.44 | 0.62 | assumption | 25% |
