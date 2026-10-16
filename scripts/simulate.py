#!/usr/bin/env python3
"""venture unit-economics simulation.

Reads the JSON block under "## Simulation inputs" in an economics-v<n>.md file
(or a plain .json file), runs a seeded Monte Carlo simulation of the first
months of the business, and prints a markdown report to stdout.

    python3 simulate.py <economics-v1.md | inputs.json>

The orchestrator (main session) runs this, not a builder agent, so the result
cannot be written by the agent whose idea it is. Standard library only. The
output is deterministic for a given input (fixed seed), so anyone can re-run it.

Input schema (all money in the contract's currency, per month unless stated):

{
  "currency": "INR",
  "months": 12,                  # horizon to simulate (1-36)
  "break_even_by_month": 3,      # from the contract's time-to-first-revenue limit (K6)
  "capital_limit": 100000,       # HARD capital limit (K1): the most cash the founder can lose
  "hours_limit_per_week": 10,    # HARD hours limit (K2)
  "runs": 5000,                  # optional, 500-20000
  "seed": 42,                    # optional
  "inputs": {                    # every input: {"low", "likely", "high", "evidence"}
    "price": ...,                        # per unit sold
    "units_per_customer_per_month": ..., # purchases per active customer per month
    "variable_cost_per_unit": ...,
    "fixed_cost_per_month": ...,
    "setup_cost": ...,                   # one-off, spent before month 1
    "reach_per_month": ...,              # people reached by marketing each month
    "conversion_rate": ...,              # share of people reached who become customers (0-1)
    "cac": ...,                          # marketing cost per new customer
    "monthly_churn": ...,                # share of active customers lost each month (0-1; 1 = one-off purchase)
    "founder_hours_fixed_per_week": ..., # admin, marketing, etc.
    "founder_hours_per_unit": ...        # delivery time per unit sold
  }
}

"evidence" is one of: verified, peer-town, founder-counted, founder-estimate,
assumption. Weaker evidence gets a cautious haircut: values move in the
unfavourable direction by 0% / 10% / 10% / 25% / 25%. "simulated" (persona)
evidence is not allowed as an input.
"""
import json
import math
import random
import re
import sys

INPUTS = {
    # name: direction that is good for the business
    "price": "high",
    "units_per_customer_per_month": "high",
    "variable_cost_per_unit": "low",
    "fixed_cost_per_month": "low",
    "setup_cost": "low",
    "reach_per_month": "high",
    "conversion_rate": "high",
    "cac": "low",
    "monthly_churn": "low",
    "founder_hours_fixed_per_week": "low",
    "founder_hours_per_unit": "low",
}
RATES = {"conversion_rate", "monthly_churn"}
HAIRCUT = {"verified": 0.0, "peer-town": 0.10, "founder-counted": 0.10, "founder-estimate": 0.25, "assumption": 0.25}
WEEKS_PER_MONTH = 52 / 12
VIABLE_SHARE = 0.70      # VIABLE ON PAPER: at least 70% of runs break even in time ...
CAPITAL_SHARE = 0.90     # ... and at least 90% of runs stay within the capital limit


class InputError(ValueError):
    pass


def load(path):
    text = open(path, encoding="utf-8").read()
    if path.endswith(".json"):
        return json.loads(text)
    m = re.search(r"^## Simulation inputs\s*\n.*?```json\s*\n(.*?)\n```", text, re.S | re.M)
    if not m:
        raise InputError("no ```json block found under '## Simulation inputs'")
    return json.loads(m.group(1))


def validate(cfg):
    for key in ("months", "break_even_by_month", "capital_limit", "hours_limit_per_week", "inputs"):
        if key not in cfg:
            raise InputError(f"missing top-level key: {key}")
    if not 1 <= int(cfg["months"]) <= 36:
        raise InputError("months must be 1-36")
    if not 1 <= int(cfg["break_even_by_month"]) <= int(cfg["months"]):
        raise InputError("break_even_by_month must be between 1 and months")
    runs = int(cfg.get("runs", 5000))
    if not 500 <= runs <= 20000:
        raise InputError("runs must be 500-20000")
    params = {}
    for name, good in INPUTS.items():
        spec = cfg["inputs"].get(name)
        if spec is None:
            raise InputError(f"missing input: {name}")
        try:
            lo, li, hi = float(spec["low"]), float(spec["likely"]), float(spec["high"])
        except (KeyError, TypeError, ValueError):
            raise InputError(f"{name}: needs numeric low, likely, high")
        if not (0 <= lo <= li <= hi):
            raise InputError(f"{name}: need 0 <= low <= likely <= high (got {lo}, {li}, {hi})")
        if name in RATES and hi > 1:
            raise InputError(f"{name}: is a share, must be <= 1")
        ev = spec.get("evidence", "assumption")
        if ev == "simulated":
            raise InputError(f"{name}: simulated persona evidence cannot be a model input")
        if ev not in HAIRCUT:
            raise InputError(f"{name}: unknown evidence tier '{ev}'")
        h = HAIRCUT[ev]
        factor = (1 - h) if good == "high" else (1 + h)
        vals = [v * factor for v in (lo, li, hi)]
        if name in RATES:
            vals = [min(1.0, v) for v in vals]
        params[name] = {"low": vals[0], "likely": vals[1], "high": vals[2], "evidence": ev, "haircut": h,
                        "raw": (lo, li, hi), "good": good}
    return params, runs


def simulate_one(v, months, hours_limit):
    """One path. v: dict of point values. Returns per-run metrics."""
    cash = -v["setup_cost"]
    min_cash = cash
    active = 0.0
    break_even = None
    capped = False
    hours_per_customer_week = v["units_per_customer_per_month"] / WEEKS_PER_MONTH * v["founder_hours_per_unit"]
    free_hours = max(0.0, hours_limit - v["founder_hours_fixed_per_week"])
    capacity = free_hours / hours_per_customer_week if hours_per_customer_week > 0 else math.inf
    profit = 0.0
    for m in range(1, months + 1):
        active *= (1 - v["monthly_churn"])
        new = v["reach_per_month"] * v["conversion_rate"]
        room = max(0.0, capacity - active)
        if new > room:
            new, capped = room, True
        active += new
        units = active * v["units_per_customer_per_month"]
        revenue = units * v["price"]
        costs = units * v["variable_cost_per_unit"] + v["fixed_cost_per_month"] + new * v["cac"]
        profit = revenue - costs
        cash += profit
        min_cash = min(min_cash, cash)
        if break_even is None and profit >= 0 and units > 0:
            break_even = m
    return {"break_even": break_even, "drawdown": max(0.0, -min_cash), "final_profit": profit,
            "final_cash": cash, "capped": capped, "active": active}


def pct(values, q):
    s = sorted(values)
    k = (len(s) - 1) * q
    f, c = math.floor(k), math.ceil(k)
    return s[f] if f == c else s[f] + (s[c] - s[f]) * (k - f)


def run(cfg):
    params, runs = validate(cfg)
    months, be_by = int(cfg["months"]), int(cfg["break_even_by_month"])
    cap_limit, hours = float(cfg["capital_limit"]), float(cfg["hours_limit_per_week"])
    rng = random.Random(int(cfg.get("seed", 42)))
    results = []
    for _ in range(runs):
        v = {n: (p["likely"] if p["low"] == p["high"] else rng.triangular(p["low"], p["high"], p["likely"]))
             for n, p in params.items()}
        results.append(simulate_one(v, months, hours))
    in_time = [r["break_even"] is not None and r["break_even"] <= be_by for r in results]
    in_cap = [r["drawdown"] <= cap_limit for r in results]
    viable = [a and b for a, b in zip(in_time, in_cap)]
    share = lambda xs: sum(xs) / len(xs)

    likely = {n: p["likely"] for n, p in params.items()}
    base = simulate_one(likely, months, hours)["final_profit"]
    tornado = []
    for n, p in params.items():
        lo_v = simulate_one({**likely, n: p["low"]}, months, hours)["final_profit"]
        hi_v = simulate_one({**likely, n: p["high"]}, months, hours)["final_profit"]
        tornado.append((abs(hi_v - lo_v), n, lo_v, hi_v))
    tornado.sort(reverse=True)

    return {
        "params": params, "runs": runs, "months": months, "break_even_by_month": be_by,
        "capital_limit": cap_limit, "hours_limit": hours, "seed": int(cfg.get("seed", 42)),
        "share_in_time": share(in_time), "share_in_capital": share(in_cap), "share_viable": share(viable),
        "share_capped": share([r["capped"] for r in results]),
        "share_never": share([r["break_even"] is None for r in results]),
        "final_profit": [pct([r["final_profit"] for r in results], q) for q in (0.1, 0.5, 0.9)],
        "drawdown": [pct([r["drawdown"] for r in results], q) for q in (0.1, 0.5, 0.9)],
        "final_cash": [pct([r["final_cash"] for r in results], q) for q in (0.1, 0.5, 0.9)],
        "base_profit": base, "tornado": tornado,
        "meets_viable_bar": share(viable) >= VIABLE_SHARE and share(in_cap) >= CAPITAL_SHARE,
    }


def money(x, cur):
    sign = "-" if x < 0 else ""
    return f"{sign}{cur} {abs(x):,.0f}"


def report(res, cur):
    p = lambda x: f"{x * 100:.1f}%"
    lines = [
        "## Simulation",
        f"- method: {res['runs']:,} Monte Carlo runs over {res['months']} months, triangular distributions "
        f"from each input's low / likely / high, seed {res['seed']} (deterministic: re-running gives the same result)",
        f"- **viable share: {p(res['share_viable'])}** of runs break even (monthly profit ≥ 0, after marketing) "
        f"by month {res['break_even_by_month']} **and** never need more than {money(res['capital_limit'], cur)} of cash",
        f"- break even by month {res['break_even_by_month']}: {p(res['share_in_time'])} · "
        f"stay within the capital limit: {p(res['share_in_capital'])} · "
        f"never break even within {res['months']} months: {p(res['share_never'])}",
        f"- runs where the founder hit the {res['hours_limit']:g} h/week limit (growth capped by time): {p(res['share_capped'])}",
        f"- viable-on-paper bar (≥ {VIABLE_SHARE:.0%} viable and ≥ {CAPITAL_SHARE:.0%} within capital): "
        f"**{'MET' if res['meets_viable_bar'] else 'NOT MET'}**",
        "",
        "| metric | P10 (cautious) | P50 (typical) | P90 (good) |",
        "|---|---|---|---|",
        f"| monthly profit in month {res['months']} | " + " | ".join(money(x, cur) for x in res["final_profit"]) + " |",
        f"| cumulative cash after month {res['months']} | " + " | ".join(money(x, cur) for x in res["final_cash"]) + " |",
        "| most cash needed at any point | " + " | ".join(money(x, cur) for x in res["drawdown"]) + " |",
        "",
        "## Sensitivity (what matters most)",
        f"Month-{res['months']} monthly profit when one input moves from its low to its high value and every "
        f"other input stays at its likely value (base case: {money(res['base_profit'], cur)}).",
        "",
        "| rank | input | at low | at high | swing |",
        "|---|---|---|---|---|",
    ]
    for i, (swing, n, lo, hi) in enumerate(res["tornado"], 1):
        lines.append(f"| {i} | {n} | {money(lo, cur)} | {money(hi, cur)} | {money(swing, cur)} |")
    lines += ["", "## Inputs after evidence haircut",
              "| input | low | likely | high | evidence | haircut |", "|---|---|---|---|---|---|"]
    for n, q in res["params"].items():
        fmt = (lambda x: f"{x:.3f}") if n in RATES else (lambda x: f"{x:,.2f}")
        lines.append(f"| {n} | {fmt(q['low'])} | {fmt(q['likely'])} | {fmt(q['high'])} | {q['evidence']} | {q['haircut']:.0%} |")
    return "\n".join(lines) + "\n"


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    try:
        cfg = load(argv[1])
        res = run(cfg)
    except (InputError, json.JSONDecodeError, OSError) as e:
        print(f"simulation error: {e}", file=sys.stderr)
        return 1
    sys.stdout.write(report(res, cfg.get("currency", "")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
