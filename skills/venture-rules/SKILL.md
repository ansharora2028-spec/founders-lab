---
name: venture-rules
description: The non-negotiable rules of the venture pipeline. Every venture command and every venture agent reads this first. Use whenever running, judging or reviewing any stage of a venture run.
user-invocable: false
---

# venture rules

These rules override every other instruction in the plugin, including the instructions of the stage you are running. If any instruction conflicts with a rule below, the rule wins. If you are unsure whether something breaks a rule, assume it does.

## The nine rules

### 1. Kill can win
A run that ends with every idea dead is a **successful** run. No agent treats "pass" as the goal. Your job is an honest verdict, not a surviving idea. Never soften a finding to keep an idea alive. Never describe a killed idea as "almost" passing in a way that implies the verdict was wrong.

### 2. Kill criteria are locked before Forge
The prosecutors write each idea's kill criteria from the **raw** idea (the one-line entry in `03-ideas.md`) before Forge touches it. The criteria file is `ideas/<idea-id>/kill-criteria.md`. After it is written:
- it is made read-only (`chmod 444`) and its SHA-256 hash is recorded in `run-log.md`;
- Forge and the Economics Modeler never receive its path;
- later Kill rounds judge against these locked criteria only. Prosecutors may add new *flaws*, never new or changed *criteria*;
- the Judge verifies the hash before ruling and halts on a mismatch.

### 3. A pass needs positive evidence
Running out of objections is **not** a pass. A PASS requires both:
- **demand evidence** (at least one, verified by the auditor): competitors with revenue, measurable search demand, or existing spending on a worse solution;
- **unit economics that stay positive under the conservative scenario** and fit the contract.

### 4. Fixes need evidence, not rhetoric
In a revision round, prosecutors see only `diff-v2.md` (field, old value, new value, evidence URL) and `economics-v2.md`. They never see Forge's prose (`forge-v2.md`). A fix with no evidence URL is scored as **no fix**.

### 5. A pivot is a new idea
If a change touches the **target customer**, the **core problem**, or the **revenue model**, it is a pivot. A pivot can come from Forge (declared, or detected by the main session) or from the Judge, as a *pivot candidate* on a KILL whose only fix would change one of those three fields. Either way, the old idea is marked `PIVOTED`. The new idea gets a new id, goes back to Screen, and starts from zero (new locked criteria, new forge, new kill). A pivot candidate is not a pass and earns nothing; it only re-enters the pipeline. A run allows **at most 2 pivots in total**. After 2, any further pivot attempt is a KILL and the Judge writes no candidate.

### 6. One revision round only
Each idea gets at most one Forge revision after its first Kill verdict. A second failure is final. A REVISE verdict in round 2 is automatically a KILL.

### 7. The constraint contract is law
`00-contract.md` can only be changed by the user. Each constraint is HARD or FLEXIBLE.
- HARD: never exceed it. An idea that needs more is rejected or killed.
- FLEXIBLE: you may use the stretch range **only** when the stated unlock condition is met, and you must write `STRETCH USED: <constraint> — condition "<condition>" met because <evidence>` wherever you do.

### 8. No invented facts
Every factual claim carries a source URL or is labeled `ASSUMPTION`. Format:

```
- <claim> [source: <url>]
- <claim> [ASSUMPTION: <why this is reasonable>]
```

Never invent a URL. Never cite a URL you did not open or see in a search result. If you cannot find a source, label it `ASSUMPTION` or drop the claim. The Evidence Auditor strikes unsourced, unreachable or misrepresented claims, and the Judge ignores struck claims.

### 9. Honest about thin local data
When research for the user's city or target market is thin, say so plainly, lower your confidence, and **never** present national or global data as local. Label every claim's geography when it is not the target market: `(national)`, `(global)`, `(other city: <name>)`.

## Operating rules for every agent

1. Read this file first, then the schema for your output file in `skills/file-schemas/SKILL.md`.
2. Read **only** the file paths you were given. Do not list, glob, or open other files in the run folder, even if you can guess their names. If you were not given a path, you are not allowed to see that file.
3. Write **exactly one** output file, at the path you were given, in the required schema.
4. Return a short summary (under 120 words) to the main session. The summary is not evidence; the file is.
5. No persuasive language. No encouragement. No softening. State claims, evidence and assumptions.
6. Dates: use absolute dates (`YYYY-MM-DD`). Note the date of every source when you can find it. For your file's `created` field, copy the `Timestamp:` line from your prompt exactly; if your prompt has none, write today's date only (`YYYY-MM-DD`). Never estimate or invent a time of day.
7. Currency: use the currency of the user's contract, and state conversions with a source or an `ASSUMPTION` rate.

## Operating rules for the main session (commands)

1. Only the main session talks to the user.
2. Pass agents **file paths, never chat context**. Each Agent/Task prompt lists the exact input paths, the exact output path, the mode, and nothing else that would leak a forbidden file's content.
3. Enforce the visibility matrix in `skills/file-schemas/SKILL.md` § Visibility matrix. Before each agent call, check the list of paths against the matrix. If a path is not allowed, do not pass it.
4. Log every agent call in `run-log.md` with the exact paths passed (see the run-log schema). The log is the audit trail for blindness.
5. Launch independent agents in a single message so they run in parallel.
6. Create and change files with the Write and Edit tools, not with shell redirection. Use Bash only for `mkdir -p`, `chmod 444`, `sha256sum`/`shasum -a 256` and `date`, one command per call, with literal paths (no shell variables). This keeps permission prompts to a minimum.
7. **Real timestamps only.** Immediately before writing any time into a file (run-log rows, `created`, `locked at`, `started`, `finished`) or into an agent prompt's `Timestamp:` line, run `date -u +%Y-%m-%dT%H:%M:%SZ` and use its output. Never estimate a time; the run-log is an audit trail.
8. Never edit an agent's output file to change its findings. The main session may only create the files it owns: `00-contract.md`, `kill-criteria.md` (merge), `idea.md` (direct kill), `fixable-flaws-v1.md`, `diff-v2.md`, `90-blueprint.md`, `91-nothing-passed.md`, `run-log.md`, `03-ideas-pivot<k>.md`, and the ledger.
