---
run_id: 2026-10-21-check-satara-english
idea_id: I01
agent: main
version: 1
created: 2026-10-21T10:22:31Z
---

## Simulation
- method: 5,000 Monte Carlo runs over 12 months, triangular distributions from each input's low / likely / high, seed 42 (deterministic: re-running gives the same result)
- **viable share: 0.0%** of runs break even (monthly profit ≥ 0, after marketing) by month 2 **and** never need more than INR 75,000 of cash
- break even by month 2: 0.0% · stay within the capital limit: 69.1% · never break even within 12 months: 15.3%
- runs where the founder hit the 12 h/week limit (growth capped by time): 11.1%
- viable-on-paper bar (≥ 70% viable and ≥ 90% within capital): **NOT MET**

| metric | P10 (cautious) | P50 (typical) | P90 (good) |
|---|---|---|---|
| monthly profit in month 12 | -INR 1,260 | INR 4,567 | INR 12,426 |
| cumulative cash after month 12 | -INR 93,238 | -INR 47,610 | INR 10,436 |
| most cash needed at any point | INR 49,698 | INR 66,401 | INR 93,812 |

## Sensitivity (what matters most)
Month-12 monthly profit when one input moves from its low to its high value and every other input stays at its likely value (base case: INR 3,087).

| rank | input | at low | at high | swing |
|---|---|---|---|---|
| 1 | reach_per_month | -INR 567 | INR 14,048 | INR 14,616 |
| 2 | conversion_rate | -INR 2,394 | INR 11,308 | INR 13,702 |
| 3 | founder_hours_fixed_per_week | INR 3,087 | -INR 7,875 | INR 10,962 |
| 4 | price | INR 11 | INR 6,163 | INR 6,152 |
| 5 | monthly_churn | INR 4,640 | INR 648 | INR 3,993 |
| 6 | fixed_cost_per_month | INR 4,337 | INR 1,837 | INR 2,500 |
| 7 | variable_cost_per_unit | INR 3,343 | INR 2,830 | INR 513 |
| 8 | cac | INR 3,167 | INR 2,876 | INR 291 |
| 9 | units_per_customer_per_month | INR 3,087 | INR 3,087 | INR 0 |
| 10 | setup_cost | INR 3,087 | INR 3,087 | INR 0 |
| 11 | founder_hours_per_unit | INR 3,087 | INR 3,087 | INR 0 |

## Money gate
- best-case viable share (no evidence haircut, the builders' numbers at face value): 90.0%; gate threshold 20%
- **money gate: PASS**

### What would have to change
Each row moves ONE input in its good direction, everything else unchanged, until 70% of runs are viable (with evidence haircuts). Likely values shown.

| input | now (likely) | would need (likely) | change |
|---|---|---|---|
| reach_per_month | 112.50 | 433.31 | x3.85 |
| conversion_rate | 0.030 | 0.116 | x3.85 |
| founder_hours_fixed_per_week | 10.62 | not reachable by this input alone | beyond x20 |

## Inputs after evidence haircut
| input | low | likely | high | evidence | haircut |
|---|---|---|---|---|---|
| price | 450.00 | 600.00 | 750.00 | founder-estimate | 25% |
| units_per_customer_per_month | 0.75 | 0.75 | 0.75 | assumption | 25% |
| variable_cost_per_unit | 25.00 | 37.50 | 50.00 | assumption | 25% |
| fixed_cost_per_month | 6,625.00 | 7,875.00 | 9,125.00 | founder-estimate | 25% |
| setup_cost | 23,750.00 | 39,375.00 | 70,625.00 | assumption | 25% |
| reach_per_month | 75.00 | 112.50 | 225.00 | assumption | 25% |
| conversion_rate | 0.015 | 0.030 | 0.053 | assumption | 25% |
| cac | 146.25 | 170.00 | 232.50 | assumption | 25% |
| monthly_churn | 0.050 | 0.075 | 0.125 | assumption | 25% |
| founder_hours_fixed_per_week | 8.75 | 10.62 | 12.50 | assumption | 25% |
| founder_hours_per_unit | 0.04 | 0.06 | 0.09 | assumption | 25% |
