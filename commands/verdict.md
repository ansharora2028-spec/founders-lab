---
description: Want a fast yes or no? Judges your idea exactly as you wrote it, with no research or sharpening: blind prosecution, unit economics with a simulation, an evidence audit and a verdict. Cheaper than /lab:test, and it can't give VIABLE ON PAPER (no framework check).
argument-hint: "\"<your idea in your own words>\" [optional: location, budget, hours]"
allowed-tools: Read, Write, Edit, Glob, Grep, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *), Bash(python3 *)
---

# /lab:verdict

Arguments: `$ARGUMENTS`

If there is no idea in the arguments, ask: "Describe your idea in a sentence or two, in your own words."

Otherwise follow `${CLAUDE_PLUGIN_ROOT}/stages/kill.md` §0 and then **§B (direct mode)** exactly, with these arguments as the idea description. Do not use pipeline mode.
