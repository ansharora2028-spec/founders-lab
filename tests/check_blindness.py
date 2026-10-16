#!/usr/bin/env python3
"""Audit venture blindness from Claude Code stream-json transcripts.

Usage:
  claude -p '/venture:run ...' --output-format stream-json --verbose > run.log
  python3 tests/check_blindness.py run.log [more.log ...]

Checks two things against the visibility matrix in skills/file-schemas/SKILL.md:
  1. the input paths the main session passed to each venture subagent;
  2. every Read/Glob/Grep/Bash call each subagent actually made.
Exits 1 if any forbidden file was passed or opened.
"""
import json
import re
import sys

FORBID = {
    "prosecutor-market": ["forge-v2", "prosecution-execution", "criteria-execution", "audit-v", "verdict-v"],
    "prosecutor-execution": ["forge-v2", "prosecution-market", "criteria-market", "audit-v", "verdict-v"],
    "forge": ["kill-criteria", "criteria-", "strategy-v", "prosecution-", "audit-v", "verdict-v"],
    "economics-modeler": ["kill-criteria", "criteria-", "prosecution-", "audit-v", "verdict-v"],
    "market-strategist": ["kill-criteria", "criteria-", "economics-v", "simulation-v", "prosecution-", "audit-v", "verdict-v"],
    "evidence-auditor": ["verdict-v"],
    "screener": ["01-local-market", "02-signals"],
    "generator": ["04-screen", "kill-criteria", "verdict-v"],
    "local-market-scout": ["02-signals", "03-ideas", "04-screen"],
    "signal-scout": ["01-local-market", "03-ideas", "04-screen"],
}


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
                    agent = inp.get("subagent_type", "").split(":")[-1]
                    owner[c["id"]] = agent
                    passed += 1
                    block = input_block(inp.get("prompt", ""))
                    for needle in FORBID.get(agent, []):
                        if needle in block:
                            bad += 1
                            print(f"PASSED  {agent} was given {needle}  ({path})")
                elif parent in owner and c.get("name") in ("Read", "Glob", "Grep", "Bash"):
                    agent = owner[parent]
                    arg = json.dumps(inp)
                    opened += 1
                    for needle in FORBID.get(agent, []):
                        if needle in arg and "SKILL.md" not in arg:
                            bad += 1
                            print(f"OPENED  {agent} {c['name']} {arg[:160]}  ({path})")
    print(f"{passed} agent calls and {opened} subagent file accesses checked, {bad} violations")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
