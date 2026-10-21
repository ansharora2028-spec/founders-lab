#!/usr/bin/env python3
"""Audit Founders Lab blindness from Claude Code stream-json transcripts.

Usage:
  claude -p '/lab:ideate ...' --output-format stream-json --verbose > run.log
  python3 tests/check_blindness.py run.log [more.log ...]

Checks two things against the visibility matrix (skills/file-schemas/parts/_visibility.md):
  1. the input paths the main session passed to each venture subagent;
  2. every Read/Glob/Grep/Bash call each subagent actually made.
Exits 1 if any forbidden file was passed or opened.
"""
import json
import re
import sys

FORBID = {
    "prosecutor": ["forge-v2", "strategy-v", "audit-v", "verdict-v"],
    # pre-0.7 transcripts (two prosecutors)
    "prosecutor-market": ["forge-v2", "prosecution-execution", "criteria-execution", "audit-v", "verdict-v"],
    "prosecutor-execution": ["forge-v2", "prosecution-market", "criteria-market", "audit-v", "verdict-v"],
    "forge": ["kill-criteria", "/criteria", "strategy-v", "prosecution-", "audit-v", "verdict-v"],
    "economics-modeler": ["kill-criteria", "/criteria", "strategy-v", "prosecution-", "audit-v", "verdict-v"],
    "market-strategist": ["kill-criteria", "/criteria", "economics-v", "simulation-v", "prosecution-", "audit-v", "verdict-v"],
    "evidence-auditor": ["verdict-v"],
    "screener": ["01-local-market", "02-signals"],
    "generator": ["04-screen", "kill-criteria", "verdict-v"],
    "local-market-scout": ["02-signals", "03-ideas", "04-screen"],
    "signal-scout": ["01-local-market", "03-ideas", "04-screen"],
}
# Before v0.7 (agents named venture:*), economics ran after the strategist and was meant to read strategy-v1.
LEGACY_ALLOW = {"economics-modeler": ["strategy-v"]}


def forbidden(full_agent):
    agent = full_agent.split(":")[-1]
    needles = FORBID.get(agent, [])
    if full_agent.startswith("venture:"):
        needles = [n for n in needles if n not in LEGACY_ALLOW.get(agent, [])]
    return needles


def input_block(prompt):
    m = re.search(r"Input files.*?:\n(.*?)\n\s*Output file", prompt, re.S)
    return m.group(1) if m else prompt


def main(paths):
    passed = opened = bad = 0
    for path in paths:
        owner = {}
        for line in open(path, encoding="utf-8"):
            try:
                ev = json.loads(line)
            except ValueError:
                continue
            if ev.get("type") != "assistant":
                continue
            parent = ev.get("parent_tool_use_id")
            for c in ev.get("message", {}).get("content", []):
                if c.get("type") != "tool_use":
                    continue
                inp = c.get("input", {})
                if c.get("name") in ("Agent", "Task") and not parent:
                    full = inp.get("subagent_type", "")
                    agent = full.split(":")[-1]
                    owner[c["id"]] = full
                    passed += 1
                    block = input_block(inp.get("prompt", ""))
                    for needle in forbidden(full):
                        if needle in block:
                            bad += 1
                            print(f"PASSED  {agent} was given {needle}  ({path})")
                elif parent in owner and c.get("name") in ("Read", "Glob", "Grep", "Bash"):
                    full = owner[parent]
                    agent = full.split(":")[-1]
                    arg = json.dumps(inp)
                    opened += 1
                    for needle in forbidden(full):
                        if needle in arg and "/skills/" not in arg:  # plugin rulebooks and schema parts are fine
                            bad += 1
                            print(f"OPENED  {agent} {c['name']} {arg[:160]}  ({path})")
    print(f"{passed} agent calls and {opened} subagent file accesses checked, {bad} violations")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
