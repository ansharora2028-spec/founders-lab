#!/usr/bin/env python3
"""Unit tests for scripts/simulate.py. Run: python3 tests/test_simulate.py"""
import copy
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import simulate  # noqa: E402


def spec(lo, li, hi, ev="verified"):
    return {"low": lo, "likely": li, "high": hi, "evidence": ev}


GOOD = {
    "currency": "INR", "months": 12, "break_even_by_month": 3,
    "capital_limit": 100000, "hours_limit_per_week": 10, "runs": 2000, "seed": 7,
    "inputs": {
        "price": spec(550, 600, 650),
        "units_per_customer_per_month": spec(1, 1, 1),
        "variable_cost_per_unit": spec(40, 50, 60),
        "fixed_cost_per_month": spec(1500, 2000, 2500),
        "setup_cost": spec(5000, 8000, 10000),
        "reach_per_month": spec(400, 500, 600),
        "conversion_rate": spec(0.03, 0.04, 0.05),
        "cac": spec(80, 100, 120),
        "monthly_churn": spec(0.05, 0.08, 0.10),
        "founder_hours_fixed_per_week": spec(2, 3, 4),
        "founder_hours_per_unit": spec(0.05, 0.1, 0.15),
    },
}


def with_inputs(**changes):
    cfg = copy.deepcopy(GOOD)
    cfg["inputs"].update(changes)
    return cfg


class SimulateTest(unittest.TestCase):
    def test_good_business_meets_bar(self):
        res = simulate.run(GOOD)
        self.assertGreater(res["share_viable"], 0.9)
        self.assertTrue(res["meets_viable_bar"])

    def test_bad_business_fails_bar(self):
        res = simulate.run(with_inputs(cac=spec(1500, 2000, 2500), monthly_churn=spec(0.8, 0.9, 1.0)))
        self.assertLess(res["share_viable"], 0.05)
        self.assertFalse(res["meets_viable_bar"])

    def test_capital_limit_binds(self):
        cfg = copy.deepcopy(GOOD)
        cfg["capital_limit"] = 1000  # setup alone costs more
        res = simulate.run(cfg)
        self.assertEqual(res["share_in_capital"], 0.0)
        self.assertFalse(res["meets_viable_bar"])

    def test_hours_cap_limits_growth(self):
        res = simulate.run(with_inputs(founder_hours_per_unit=spec(3, 4, 5), reach_per_month=spec(5000, 6000, 7000)))
        self.assertGreater(res["share_capped"], 0.99)

    def test_deterministic(self):
        a, b = simulate.run(GOOD), simulate.run(GOOD)
        self.assertEqual(a["share_viable"], b["share_viable"])
        self.assertEqual(simulate.report(a, "INR"), simulate.report(b, "INR"))

    def test_haircut_makes_it_worse(self):
        weak = copy.deepcopy(GOOD)
        for s in weak["inputs"].values():
            s["evidence"] = "founder-estimate"
        self.assertLess(simulate.run(weak)["base_profit"], simulate.run(GOOD)["base_profit"])

    def test_one_off_purchase(self):
        res = simulate.run(with_inputs(monthly_churn=spec(1, 1, 1)))
        self.assertIsNotNone(res)  # churn of 1 is a valid one-off model

    def test_sensitivity_ranks_inputs(self):
        res = simulate.run(GOOD)
        swings = [t[0] for t in res["tornado"]]
        self.assertEqual(swings, sorted(swings, reverse=True))
        self.assertEqual(len(res["tornado"]), len(simulate.INPUTS))

    def test_rejects_bad_input(self):
        for bad in (
            with_inputs(price=spec(700, 600, 650)),               # low > likely
            with_inputs(conversion_rate=spec(0.1, 0.5, 1.5)),     # rate > 1
            with_inputs(price={"low": 1, "likely": 2, "high": 3, "evidence": "simulated"}),
            with_inputs(price={"low": 1, "likely": 2, "high": 3, "evidence": "vibes"}),
        ):
            with self.assertRaises(simulate.InputError):
                simulate.run(bad)
        missing = copy.deepcopy(GOOD)
        del missing["inputs"]["cac"]
        with self.assertRaises(simulate.InputError):
            simulate.run(missing)

    def test_reads_markdown_block(self):
        import json
        md = "## Inputs\n- x\n\n## Simulation inputs\n```json\n" + json.dumps(GOOD) + "\n```\n\n## Scenarios\n"
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write(md)
        try:
            self.assertEqual(simulate.load(f.name)["months"], 12)
            self.assertEqual(simulate.main(["simulate.py", f.name]), 0)
        finally:
            os.unlink(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=1)
