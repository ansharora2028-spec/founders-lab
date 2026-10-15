#!/usr/bin/env python3
"""Trim a `claude -p --output-format stream-json --verbose` log to what check_blindness.py needs.

Keeps only tool_use blocks: Agent/Task calls from the main session, and Read/Glob/Grep/Bash
calls made inside subagents. Drops all model text, tool results and fetched web content.

Usage: python3 tests/trim_transcript.py run.log > tests/fixtures/<name>.jsonl [--strip-prefix /abs/path]
"""
import json
import sys

args = sys.argv[1:]
prefix = None
if "--strip-prefix" in args:
    i = args.index("--strip-prefix")
    prefix = args[i + 1]
    del args[i:i + 2]

for line in open(args[0], encoding="utf-8"):
    try:
        ev = json.loads(line)
    except ValueError:
        continue
    if ev.get("type") != "assistant":
        continue
    parent = ev.get("parent_tool_use_id")
    keep = []
    for c in ev.get("message", {}).get("content", []):
        if c.get("type") != "tool_use":
            continue
        if (not parent and c.get("name") in ("Agent", "Task")) or (parent and c.get("name") in ("Read", "Glob", "Grep", "Bash")):
            keep.append({"type": "tool_use", "id": c["id"], "name": c["name"], "input": c.get("input", {})})
    if keep:
        out = json.dumps({"type": "assistant", "parent_tool_use_id": parent, "message": {"content": keep}}, ensure_ascii=False)
        if prefix:
            out = out.replace(prefix, "<project>")
        print(out)
