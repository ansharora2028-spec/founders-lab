#!/usr/bin/env python3
"""Static consistency checks for the venture plugin.

1. Every ${CLAUDE_PLUGIN_ROOT}/... path referenced in agents, commands, skills and hooks exists.
2. Every template's H2 sections match its schema in skills/file-schemas/SKILL.md.
3. Every run file under examples/ has front matter and the H2 sections its schema requires.
4. Every agent file has name, description, tools and model frontmatter.
Exits 1 on any failure.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
errors = []

# 1. plugin-root references
for f in glob.glob("agents/*.md") + glob.glob("commands/*.md") + glob.glob("skills/*/SKILL.md") + glob.glob("hooks/*.json"):
    for m in re.finditer(r"\$\{CLAUDE_PLUGIN_ROOT\}/([\w./-]+)", open(f, encoding="utf-8").read()):
        if not os.path.exists(m.group(1)):
            errors.append(f"{f}: missing reference {m.group(1)}")

# Parse schemas: '## <file> — writer: ...' followed by a ```markdown block
text = open("skills/file-schemas/SKILL.md", encoding="utf-8").read()
heads = list(re.finditer(r"^## (\S+\.md)[^\n]*— writer[^\n]*$", text, re.M))
schema = {}
for i, m in enumerate(heads):
    body = text[m.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
    block = re.search(r"(`{3,})markdown\n(.*?)\n\1(?!`)", body, re.S)
    if not block:
        errors.append(f"schema {m.group(1)} has no markdown block")
        continue
    schema[os.path.basename(m.group(1))] = [l[3:].strip() for l in block.group(2).splitlines() if l.startswith("## ")]


def schema_key(name):
    generic = re.sub(r"pivot\d+", "pivot<k>", re.sub(r"-v\d+\.md$", "-v<n>.md", name))
    aliases = {
        "criteria-execution.md": "criteria-market.md",
        "03-ideas-pivot<k>.md": "03-ideas.md",
        "04-screen-pivot<k>.md": "04-screen.md",
        "prosecution-execution-v<n>.md": "prosecution-market-v<n>.md",
        "diff-v<n>.md": "diff-v2.md",
        "fixable-flaws-v<n>.md": "fixable-flaws-v1.md",
        "city-slug.md": "<city-slug>.md",
    }
    for k in (name, generic, aliases.get(generic, "")):
        if k in schema:
            return k
    return None


def h2(path):
    return [l[3:].strip() for l in open(path, encoding="utf-8").read().splitlines() if l.startswith("## ")]


# 2. templates
for p in glob.glob("templates/**/*.md", recursive=True):
    name = os.path.basename(p)
    if name in ("README.md", "LEDGER.md"):
        continue
    k = schema_key(name)
    want = schema.get(k, [])
    if name.startswith("03-ideas-pivot"):  # one main-written idea: no longlist
        want = [s for s in want if s != "Longlist and pass pre-check"]
    if not k:
        errors.append(f"{p}: no schema")
    elif h2(p) != want:
        errors.append(f"{p}: sections {h2(p)} != schema {want}")

# 3. example run files
for p in glob.glob("examples/**/*.md", recursive=True):
    name = os.path.basename(p)
    if name in ("README.md", "LEDGER.md"):
        continue
    if os.path.basename(os.path.dirname(p)) == "cities":  # ventures/cities/<city-slug>.md: append-only, one H2 per run
        text = open(p, encoding="utf-8").read()
        want = ["Verified facts", "Peer-town benchmark", "Big-brand presence", "City profile",
                "Founder-reported (unverified)", "Useless sources for this town"]
        runs = re.split(r"(?m)^## ", text)[1:]
        if not text.startswith("# ") or not runs:
            errors.append(f"{p}: city memory needs '# <City>, <Country>' and at least one '## <run_id>' section")
        for r in runs:
            got = [l[4:].strip() for l in r.splitlines() if l.startswith("### ")]
            if got != want:
                errors.append(f"{p}: run section {r.splitlines()[0]!r} has {got} != {want}")
        continue
    k = schema_key(name)
    if not k:
        errors.append(f"{p}: no schema")
        continue
    content = open(p, encoding="utf-8").read()
    if not content.startswith("---\n"):
        errors.append(f"{p}: no front matter")
    missing = [s for s in schema[k] if s not in h2(p)]
    # The examples are real v0.1 test output, kept unedited. Two sections were added to the
    # schemas after those runs (DECISIONS.md D24, D25, D30, D33 and D35), so they are allowed to be absent there.
    added_later = {"Pivot candidate (KILL only)", "Fixes (round 2 only)",
                   "How it works", "Need gap", "How it makes money", "The need gap", "The ideas, explained",
                   "Money already moving", "Complaints about paid options", "Paid products people complain about",
                   "Longlist and pass pre-check", "Why the search missed",
                   "Peer-town benchmark", "Big-brand presence", "City profile", "Simulation inputs",
                   "Simulation", "Viable-on-paper check", "Assumptions to confirm (VIABLE ON PAPER only)",
                   "Assumptions to confirm first (VIABLE ON PAPER only)"}
    missing = [s for s in missing if s not in added_later]
    if missing:
        errors.append(f"{p}: missing sections {missing}")

# 4. agent frontmatter
for p in glob.glob("agents/*.md"):
    fm = open(p, encoding="utf-8").read().split("---")[1]
    for field in ("name", "description", "tools", "model"):
        if not re.search(rf"^{field}:\s*\S", fm, re.M):
            errors.append(f"{p}: frontmatter missing {field}")

for e in errors:
    print("FAIL", e)
print(f"{len(schema)} schemas; {len(errors)} problems")
sys.exit(1 if errors else 0)
