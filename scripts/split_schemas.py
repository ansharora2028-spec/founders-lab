#!/usr/bin/env python3
"""Split skills/file-schemas/SKILL.md into one small file per schema.

Agents read only the conventions and their own output's schema (a few hundred
words) instead of the whole 30 KB file. SKILL.md stays the single source of
truth: edit it, then run

    python3 scripts/split_schemas.py          # rewrite skills/file-schemas/parts/
    python3 scripts/split_schemas.py --check  # CI: fail if parts/ is out of date
"""
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "skills", "file-schemas", "SKILL.md")
OUT = os.path.join(ROOT, "skills", "file-schemas", "parts")
HEADER = "<!-- Generated from skills/file-schemas/SKILL.md by scripts/split_schemas.py. Do not edit; edit SKILL.md and re-run. -->\n\n"


def part_name(heading):
    path = heading.split(" — ")[0].split(" and ")[0].strip()
    name = os.path.basename(path)
    name = name.replace("<city-slug>", "city").replace("<n>", "n").replace("<k>", "k")
    return name


def split(text):
    """Return {filename: content} for conventions, visibility matrix and each file schema."""
    lines = text.splitlines(keepends=True)
    in_code = False
    starts = []  # (line index, filename)
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_code = not in_code
        if in_code or not line.startswith("## "):
            continue
        title = line[3:].strip()
        if title == "Conventions":
            starts.append((i, "_conventions.md"))
        elif title.startswith("Visibility matrix"):
            starts.append((i, "_visibility.md"))
        elif " — writer" in title:
            starts.append((i, part_name(title)))
    parts = {}
    for n, (i, name) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        body = "".join(lines[i:end]).rstrip()
        body = re.sub(r"\n+---\s*$", "", body)  # drop a trailing section rule
        if name in parts:
            raise SystemExit(f"duplicate part name {name}")
        parts[name] = HEADER + body + "\n"
    return parts


def main(argv):
    parts = split(open(SRC, encoding="utf-8").read())
    check = "--check" in argv
    existing = set(os.listdir(OUT)) if os.path.isdir(OUT) else set()
    stale = sorted(n for n in existing if n.endswith(".md") and n not in parts)
    changed = [n for n, c in parts.items()
               if not os.path.exists(os.path.join(OUT, n)) or open(os.path.join(OUT, n), encoding="utf-8").read() != c]
    if check:
        if changed or stale:
            print("schema parts out of date; run python3 scripts/split_schemas.py", file=sys.stderr)
            for n in changed + stale:
                print(f"  {n}", file=sys.stderr)
            return 1
        print(f"{len(parts)} schema parts up to date")
        return 0
    os.makedirs(OUT, exist_ok=True)
    for n in stale:
        os.remove(os.path.join(OUT, n))
    for n in changed:
        with open(os.path.join(OUT, n), "w", encoding="utf-8") as f:
            f.write(parts[n])
    print(f"wrote {len(changed)} of {len(parts)} parts, removed {len(stale)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
