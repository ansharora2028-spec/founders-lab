---
description: venture kill — blind prosecution, evidence audit and judgement of forged ideas against their locked kill criteria, with at most one evidence-only revision round and pivot detection. Also usable directly on any idea - /venture:kill "<idea description>" - with a minimal intake and no forge.
argument-hint: "[run_id] [idea_id ...]  |  \"<idea description>\" for a direct verdict"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *)
---

# /venture:kill

## 0. Load the rules and pick the mode
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md` and Part 2 of `${CLAUDE_PLUGIN_ROOT}/skills/scoring-rubric/SKILL.md`. Read the Visibility matrix and the schemas for `diff-v2.md`, `fixable-flaws-v1.md`, `idea.md` and `run-log.md` in `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/SKILL.md`. Read `ventures/LEDGER.md` if it exists.
2. Arguments: `$ARGUMENTS`
   - If the arguments are empty, or start with a folder name in `ventures/runs/`, this is **pipeline mode** (§A). `RUN` = that folder, or the most recent run. Remaining arguments are idea ids.
   - Otherwise the arguments are an idea description: **direct mode** (§B).

All agent prompts use this form and contain nothing else:

```
Run folder: <absolute RUN path>
Mode: <criteria | kill>
Idea id: <id>
Round: <1 | 2>
Input files (read only these):
- <path>
Output file (write exactly this one file):
- <path>
Today's date: <YYYY-MM-DD>
```

**Before every agent call, check its path list against the Visibility matrix.** Never pass `forge-v2.md` to a prosecutor. Never pass one prosecutor's file to the other. Never pass `kill-criteria.md` or `criteria-*.md` to forge or the economics modeler. Never pass a verdict to the auditor. Log every call in `run-log.md` § Agent calls with the exact paths.

---

## A. Pipeline mode

Ideas to judge: the given ids, or every idea in `RUN/ideas/` that has `economics-v1.md` and no `verdict-v1.md`, plus any idea with `economics-v2.md` and no `verdict-v2.md`.

**Resuming:** an idea whose `verdict-v1.md` is REVISE and that has no `verdict-v2.md` resumes at §A2. Skip any §A2 step whose output file already exists (`fixable-flaws-v1.md`, `forge-v2.md`, `diff-v2.md`, `economics-v2.md`), but always run the pivot detection in step 3 before using an existing `forge-v2.md`.

### A1. Kill round (run for all ideas at once, stage by stage)

Progress note: `Kill round <n>: prosecuting <k> idea(s) — 2 prosecutors each in parallel, then audit, then judge (paid stage).`

**Step 1 — prosecutors, in parallel across all ideas (one message).** For each idea launch both `venture:prosecutor-market` and `venture:prosecutor-execution`, `Mode: kill`:
- round 1 inputs: `00-contract.md`, `01-local-market.md`, `02-signals.md`, `ideas/<id>/kill-criteria.md`, `ideas/<id>/forge-v1.md`, `ideas/<id>/economics-v1.md`;
- round 2 inputs: `00-contract.md`, `01-local-market.md`, `02-signals.md`, `ideas/<id>/kill-criteria.md`, `ideas/<id>/diff-v2.md`, `ideas/<id>/economics-v2.md`, and **its own** `ideas/<id>/prosecution-<side>-v1.md`;
- outputs: `ideas/<id>/prosecution-market-v<n>.md`, `ideas/<id>/prosecution-execution-v<n>.md`.

**Step 2 — evidence auditor, in parallel across ideas (one message), after both prosecutions exist.** `venture:evidence-auditor` with every file for that idea in this round except the verdict:
- round 1: `00`, `01`, `02`, `kill-criteria.md`, `forge-v1.md`, `economics-v1.md`, `prosecution-market-v1.md`, `prosecution-execution-v1.md`;
- round 2: `00`, `01`, `02`, `kill-criteria.md`, `diff-v2.md`, `forge-v2.md`, `economics-v2.md`, `prosecution-market-v2.md`, `prosecution-execution-v2.md`;
- output: `ideas/<id>/audit-v<n>.md`.

(The auditor runs after the prosecutors, not alongside them, because it must check the evidence behind every FATAL flaw a prosecutor raises.)

**Audit health check.** If an audit's notes say more than half of its UNREACHABLE labels are `UNREACHABLE (tool failure)` (the fetch tool could not reach any host, e.g. a blocked network), tell the user before judging: "The auditor could not open sources for <id> (network/tool failure). Struck claims will push the verdict toward KILL. Fix network access and re-run `/venture:kill <run_id> <id>` for a fair audit." Then continue. The rule still applies, and you never un-strike claims yourself. Record the warning in run-log § Stages.

**Step 3 — judge, in parallel across ideas (one message).** `venture:judge` with `run-log.md` and every file for the idea (all rounds so far, including `03-ideas.md`/pivot file and `04-screen.md`); output `ideas/<id>/verdict-v<n>.md`.

**Step 4 — read each verdict.**
- `HALTED` → stop the whole run. Tell the user: "Kill criteria for <id> were modified after locking (hash mismatch). The run is halted." Record `HALTED (tamper)` in run-log. Do not continue to blueprint; still append the ledger entry with outcome `NOTHING PASSED` and the HALTED idea.
- `PASS` → final for this idea.
- `KILL` → final for this idea.
- `REVISE` in round 2 → **treat as KILL**; note `REVISE in round 2 → KILL (rule 6)` in run-log.
- `REVISE` in round 1 → §A2 for this idea.

### A2. Revision round (round 1 REVISE only, max once per idea)

Progress note: `<id> got REVISE: one evidence-only revision round.`

1. Write `ideas/<id>/fixable-flaws-v1.md`: the verdict's "Fixable flaws" table copied verbatim, nothing else from the verdict.
2. `venture:forge`, `Round: 2`, inputs `00`, `01`, `02`, the ideas file, `ideas/<id>/forge-v1.md`, `ideas/<id>/fixable-flaws-v1.md`; output `ideas/<id>/forge-v2.md`.
3. **Pivot detection** — before creating any diff. Compare `forge-v1.md` and `forge-v2.md` § Core identity:
   - did the **customer** change (a different payer or segment type, not a narrowing within the same one)?
   - did the **problem** change?
   - did the **revenue model** change (who pays, for what, how often, pricing basis)?
   - did forge set `pivot declared: YES`?
   If any is yes → run the **Pivot procedure** below for this idea and stop handling it here.
4. Write `ideas/<id>/diff-v2.md` in the schema. One row per change: flaw addressed, field, old value (verbatim from forge-v1), new value (verbatim from forge-v2), evidence URL (verbatim from forge-v2's Fixes table, or `NONE`). Also list unaddressed flaws. **Copy, do not paraphrase.** No prose from forge-v2 beyond the new values.
5. `venture:economics-modeler`, inputs `00`, `01`, `ideas/<id>/forge-v2.md`, `ideas/<id>/economics-v1.md`; output `ideas/<id>/economics-v2.md`.
6. Run §A1 again for this idea with round 2.

Run revision rounds for several ideas in parallel where possible (same step, one message).

### Pivot procedure

1. Read `pivots used` from `run-log.md`.
2. If it is already **2**: the idea is **KILLED** — `pivot required but pivot limit (2) reached`. Record it in run-log § Pivots and Stages. Stop.
3. Otherwise `k` = pivots used + 1. New id = `<old-id>-P<k>`.
   - Record the old idea as `PIVOTED → <new id>` in run-log § Pivots, with the field(s) changed. Set `pivots used: k/2`.
   - Write `RUN/03-ideas-pivot<k>.md` in the `03-ideas` schema with one idea: id `<new id>`, pitch, customer, problem and revenue model taken verbatim from the forge file's Core identity, lens unchanged, signal ids unchanged, `pivoted from: <old-id>`, `pivot reason: <field changed>`.
   - **Screen it from zero:** `venture:screener`, inputs `00`, `03-ideas-pivot<k>.md`, LEDGER; output `04-screen-pivot<k>.md`. If REJECTED, the new idea is dead (`REJECTED (screen)`).
   - Otherwise: criteria mode for both prosecutors on the new idea (inputs `00`, `01`, `02`, `03-ideas-pivot<k>.md`, idea id), merge, lock (chmod 444 + sha256 into run-log § Locks) — exactly as in `${CLAUDE_PLUGIN_ROOT}/commands/generate.md` §4–5.
   - Then forge round 1 and economics round 1 for the new idea (as in `${CLAUDE_PLUGIN_ROOT}/commands/forge.md`), then §A1 round 1. The new idea gets its own single revision round.

### A3. Report
Add a Stages row `kill — done`. Show a table: idea, final verdict, round, confidence, top decisive reason. Next step: `/venture:blueprint` (writes the blueprint or the nothing-passed report).

---

## B. Direct mode — `/venture:kill "<idea description>"`

For users who just want an existing idea judged. No scouting, no generation, no forge, no revision.

1. **Minimal intake.** The idea is the quoted text in the arguments. Any text after the quoted idea is pre-filled intake answers; use them and ask only for what is missing. Ask (AskUserQuestion where available, one topic at a time) only for: location (city, country), target market, and the constraints K1–K9 with HARD/FLEXIBLE (and stretch range + unlock condition for FLEXIBLE). Constraints or a budget stated inside the idea description count as answers — e.g. "₹50k budget" is K1 = ₹50,000; ask whether it is HARD or FLEXIBLE if you can; in a non-interactive session treat stated budgets as HARD. Read the contract back and get explicit confirmation (non-interactive: follow the arguments rule in `${CLAUDE_PLUGIN_ROOT}/commands/intake.md` §1; anything not stated is recorded as `not stated` and is not a constraint).
2. **Create the run.** `run_id` = `<YYYY-MM-DD>-kill-<slug>`. `mkdir -p ventures/runs/<run_id>/ideas/I01`. Write `00-contract.md` (starting point: path a, in their words: the idea; depth mode: `direct-kill`) and `run-log.md`. Create `ventures/LEDGER.md` with `# venture ledger` if missing.
3. Write `ideas/I01/idea.md` in the schema: the idea **as stated**, parsed but not improved.
4. **Criteria (parallel, one message):** `venture:prosecutor-market` and `venture:prosecutor-execution`, `Mode: criteria`, inputs `00-contract.md`, `ideas/I01/idea.md`; outputs `ideas/I01/criteria-market.md`, `ideas/I01/criteria-execution.md`.
5. **Merge and lock** into `ideas/I01/kill-criteria.md` (raw idea = `idea.md` § Idea as stated), `chmod 444`, sha256 into run-log § Locks.
6. **Economics:** `venture:economics-modeler`, inputs `00-contract.md`, `ideas/I01/idea.md`; output `ideas/I01/economics-v1.md`. (Without it, a PASS is impossible.)
7. **Kill round 1:** prosecutors in parallel (`Mode: kill`, inputs `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`), then `venture:evidence-auditor` (inputs `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`, both prosecutions), then `venture:judge` (everything for I01 plus `run-log.md`).
8. **Verdict.** PASS and KILL are final. A REVISE is reported as `KILL as stated — it would need: <fixable flaws>` (direct mode has no revision round), and recorded as KILL in the ledger. HALTED: report tampering.
9. **Ledger.** Append an entry as in `${CLAUDE_PLUGIN_ROOT}/commands/ledger.md` § Append.
10. **Report** to the user: verdict, confidence, decisive reasons with file references, and the path of the verdict file. If PASS, suggest `/venture:blueprint <run_id>`. If KILL, suggest `/venture:run` to explore alternatives under the same constraints.
