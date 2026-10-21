---
description: Internal pipeline stage (not a slash command), followed by /lab:ideate, /lab:test, /lab:verdict and /lab:resume. kill — for ideas that passed the money gate: the framework check (strategist) and blind prosecution in parallel, then evidence audit and judgement against the locked kill criteria, with at most one evidence-only revision round and pivot detection. Also usable directly on any idea - /lab:verdict "<idea description>" - with a minimal intake and no forge.
argument-hint: "[run_id] [idea_id ...]  |  \"<idea description>\" for a direct verdict"
allowed-tools: Read, Write, Edit, Glob, Agent, Task, AskUserQuestion, Bash(mkdir *), Bash(chmod *), Bash(sha256sum *), Bash(shasum *), Bash(date *), Bash(python3 *)
---

# Stage: kill

## 0. Load the rules and pick the mode
1. Read `${CLAUDE_PLUGIN_ROOT}/skills/rules/SKILL.md` and Part 2 of `${CLAUDE_PLUGIN_ROOT}/skills/scoring-rubric/SKILL.md`. In `${CLAUDE_PLUGIN_ROOT}/skills/file-schemas/parts/`, read `_visibility.md`, `diff-v2.md`, `fixable-flaws-v1.md`, `idea.md`, `gate-vn.md` and `run-log.md`. Read `ventures/LEDGER.md` if it exists.
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
Timestamp: <output of date -u +%Y-%m-%dT%H:%M:%SZ, run just before this call>
```

**Before every agent call, check its path list against the Visibility matrix.** Never pass `forge-v2.md` or `strategy-v1.md` to the prosecutor. Never pass `kill-criteria.md` or `criteria.md` to forge, the strategist or the economics modeler. Never pass a verdict to the auditor. Log every call in `run-log.md` § Agent calls with the exact paths.

---

## A. Pipeline mode

Ideas to judge: the given ids, or every idea in `RUN/ideas/` that has `economics-v1.md` and `simulation-v1.md` and no `verdict-v1.md`, plus any idea with `economics-v2.md` and no `verdict-v2.md`. Skip ideas recorded as `KILL (money gate)` (they have a `gate-v<n>.md`) or `DROPPED (strategist)`.

**Never re-handle a finished idea.** Read `run-log.md` § Pivots and § Stages first. An idea recorded there as `PIVOTED → <id>`, as killed by the pivot limit, as `KILL (money gate)` or as `DROPPED (strategist)` is final: skip it, even though its `verdict-v1.md` may still say REVISE (a pivot's successor is handled under its own id).

**Resuming:** an idea whose `verdict-v1.md` is REVISE, that has no `verdict-v2.md`, and that is not recorded as final above resumes at §A2. Skip any §A2 step whose output file already exists (`fixable-flaws-v1.md`, `forge-v2.md`, `diff-v2.md`, `economics-v2.md`, `simulation-v2.md`), but always run the pivot detection in step 3 before using an existing `forge-v2.md`. In §A1, skip any step whose output file already exists.

### A1. Kill round (run for all ideas at once, stage by stage)

Progress note: `Kill round <n> for <k> idea(s): framework check and prosecution in parallel, then audit, then judge (paid stage).`

**Step 1: strategist and prosecutor, in parallel across all ideas (one message).** For each idea, launch both at once:
- **Round 1 only:** `lab:market-strategist`, with inputs `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, the ideas file (+ `Idea id`), `ideas/<id>/forge-v1.md`, and the city memory file if it exists; output `ideas/<id>/strategy-v1.md`. Never criteria, economics or the simulation.
- `lab:prosecutor`, `Mode: kill`:
  - **round 1 inputs:** `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, `ideas/<id>/kill-criteria.md`, `ideas/<id>/forge-v1.md`, `ideas/<id>/economics-v1.md`, `ideas/<id>/simulation-v1.md`;
  - **round 2 inputs:** `00-contract.md`, `00-founder-knowledge.md`, `01-local-market.md`, `02-signals.md`, `ideas/<id>/kill-criteria.md`, `ideas/<id>/diff-v2.md`, `ideas/<id>/economics-v2.md`, `ideas/<id>/simulation-v2.md`, and its own `ideas/<id>/prosecution-v1.md`;
  - **output:** `ideas/<id>/prosecution-v<n>.md`.

  The prosecutor never receives `strategy-v1.md`. The two run side by side so neither waits for the other.

**Step 1b: strategist DROP (round 1).** If `strategy-v1.md` recommends DROP, the idea stops:
- record `DROPPED (strategist): <reason>` in `run-log.md` § Stages;
- run no audit or judge for it;
- tell the user the idea and the reason in one line.

A DROP is a builder's own call. It can never create a false pass.

**Step 2: evidence auditor, in parallel across ideas (one message), after step 1 is done.** `lab:evidence-auditor` with every file for that idea in this round except the verdict:
- **round 1:** `00`, `00-founder-knowledge.md`, `01`, `02`, `kill-criteria.md`, `forge-v1.md`, `strategy-v1.md`, `economics-v1.md`, `simulation-v1.md`, `prosecution-v1.md`;
- **round 2:** `00`, `00-founder-knowledge.md`, `01`, `02`, `kill-criteria.md`, `diff-v2.md`, `forge-v2.md`, `strategy-v1.md`, `economics-v2.md`, `simulation-v2.md`, `prosecution-v2.md`;
- **output:** `ideas/<id>/audit-v<n>.md`.

(The auditor runs after the prosecutor, not alongside it, because it must check the evidence behind every FATAL flaw the prosecutor raises.)

**Audit health check.** If an audit's notes say more than half of its UNREACHABLE labels are `UNREACHABLE (tool failure)` (the fetch tool could not reach any host, e.g. a blocked network), warn the user before judging. Say: "The auditor could not open sources for <id> (network/tool failure). Struck claims will push the verdict toward KILL. Fix network access and re-run `/lab:resume <run_id>` for a fair audit."
- Then continue. The rule still applies, and you never un-strike claims yourself.
- Record the warning in run-log § Stages.

**Step 3: pre-judge hash check, then the judge (one message for all ideas).**
1. For each idea, just before the judge call, run `sha256sum "<RUN>/ideas/<id>/kill-criteria.md"` (or `shasum -a 256`).
2. Compare it with the hash in § Locks, and add a row to § Locks: `pre-judge check | <id> | <hash> | match` (or `MISMATCH`). This lets the judge still rule if its own sandbox blocks the hash command.
3. Launch `lab:judge` with `run-log.md` and every file for the idea: all rounds so far, including `03-ideas.md` (or the pivot file) and `04-screen.md`. Output: `ideas/<id>/verdict-v<n>.md`.
4. **Call the judge once per idea per round.** If the verdict file is missing afterwards, re-run it once with the line `Your previous run wrote no verdict file. Write it now.`, and record the retry in run-log.

**Step 4: read each verdict.**
- `HALTED` → stop the whole run.
  - Tell the user: "Kill criteria for <id> were modified after locking (hash mismatch). The run is halted."
  - Record `HALTED (tamper)` in run-log.
  - Do not continue to blueprint. Still append the ledger entry, with outcome `NOTHING PASSED` and the HALTED idea.
- `PASS` → final for this idea.
- `VIABLE ON PAPER` → final for this idea. It is not a PASS: report it as "viable on paper, confirm <the assumptions> first".
- `KILL` → final for this idea. Check the verdict's **Pivot candidate** section:
  - if it names a candidate (not `none`) and `run-log.md` shows fewer than 2 pivots used, run the **Pivot procedure** with the candidate as the source;
  - the killed idea is then recorded as `PIVOTED → <new id>`, and its KILL verdict stays as written.
- `REVISE` in round 2 → **treat as KILL**; note `REVISE in round 2 → KILL (rule 6)` in run-log.
- `REVISE` in round 1 → §A2 for this idea.

### A2. Revision round (round 1 REVISE only, max once per idea)

Progress note: `<id> got REVISE: one evidence-only revision round.`

1. Write `ideas/<id>/fixable-flaws-v1.md`: the verdict's "Fixable flaws" table copied verbatim, nothing else from the verdict.
2. `lab:forge`, `Round: 2`, inputs `00`, `01`, `02`, the ideas file, `ideas/<id>/forge-v1.md`, `ideas/<id>/fixable-flaws-v1.md`; output `ideas/<id>/forge-v2.md`.
3. **Pivot detection** — before creating any diff. Compare `forge-v1.md` and `forge-v2.md` § Core identity:
   - did the **customer** change (a different payer or segment type, not a narrowing within the same one)?
   - did the **problem** change?
   - did the **revenue model** change (who pays, for what, how often, pricing basis)?
   - did forge set `pivot declared: YES`?
   If any is yes → run the **Pivot procedure** below for this idea and stop handling it here.
4. Write `ideas/<id>/diff-v2.md` in the schema. One row per change: flaw addressed, field, old value (verbatim from forge-v1), new value (verbatim from forge-v2), evidence URL (verbatim from forge-v2's Fixes table, or `NONE`). Also list unaddressed flaws. **Copy, do not paraphrase.** No prose from forge-v2 beyond the new values.
5. `lab:economics-modeler`, inputs `00`, `00-founder-knowledge.md`, `01`, `ideas/<id>/forge-v2.md`, `ideas/<id>/economics-v1.md`; output `ideas/<id>/economics-v2.md`.
6. Run the simulation and the money gate on it, exactly as in `${CLAUDE_PLUGIN_ROOT}/stages/forge.md` §4, writing `ideas/<id>/simulation-v2.md`. If the gate fails, write `gate-v2.md`, record `KILL (money gate)`, and stop handling this idea.
7. Run §A1 again for this idea with round 2 (prosecutor only, since the strategist runs in round 1 only).

Run revision rounds for several ideas in parallel where possible (same step, one message).

### Pivot procedure

1. Read `pivots used` from `run-log.md`.
2. If it is already **2**: the idea is **KILLED** (for a judge candidate, it simply stays KILLED) — `pivot required but pivot limit (2) reached`. Record it in run-log § Pivots (`to: KILLED (pivot limit)`) and § Stages. Stop.
3. Otherwise `k` = pivots used + 1. New id = `<old-id>-P<k>`.
   - Record the old idea as `PIVOTED → <new id>` in run-log § Pivots, with the field(s) changed. Set `pivots used: k/2`.
   - Write `RUN/03-ideas-pivot<k>.md` in the `03-ideas` schema with one idea: id `<new id>`, customer, problem and revenue model taken verbatim from the source (the forge file's Core identity for a forge pivot, or the verdict's Pivot candidate section for a judge candidate), a one-line pitch built only from those fields, lens unchanged, signal ids unchanged, `pivoted from: <old-id>`, `pivot reason: <field changed>; source: forge | judge candidate`.
   - **Screen it from zero:** `lab:screener`, inputs `00`, `03-ideas-pivot<k>.md`, LEDGER; output `04-screen-pivot<k>.md`. If REJECTED, the new idea is dead (`REJECTED (screen)`).
   - Otherwise: the prosecutor in criteria mode on the new idea (inputs `00`, `01`, `02`, `03-ideas-pivot<k>.md`, idea id), then copy into `kill-criteria.md` and lock it (chmod 444, sha256 into run-log § Locks), exactly as in `${CLAUDE_PLUGIN_ROOT}/stages/generate.md` §4–5.
   - Then forge round 1, economics round 1, the simulation and the money gate for the new idea (as in `${CLAUDE_PLUGIN_ROOT}/stages/forge.md`), then §A1 round 1. The new idea gets its own single revision round.

### A3. Report
Add a Stages row `kill — done`. Show a table: idea, pitch, final verdict, round, confidence, top decisive reason. Under it, one line per idea on how it was meant to make money (from `03-ideas.md`), so the verdict reads in context. Next step: `/lab:resume` (writes the blueprint or the nothing-passed report).

---

## B. Direct mode — `/lab:verdict "<idea description>"`

For users who just want an existing idea judged. No scouting, no generation, no forge, no revision.

1. **Minimal intake.** The idea is the quoted text in the arguments. Any text after the quoted idea is pre-filled intake answers; use them and ask only for what is missing. Ask (AskUserQuestion where available, one topic at a time) only for: location (city, country), target market, and the constraints K1–K9 with HARD/FLEXIBLE (and stretch range + unlock condition for FLEXIBLE). Constraints or a budget stated inside the idea description count as answers — e.g. "₹50k budget" is K1 = ₹50,000; ask whether it is HARD or FLEXIBLE if you can; in a non-interactive session treat stated budgets as HARD. Read the contract back and get explicit confirmation (non-interactive: follow the arguments rule in `${CLAUDE_PLUGIN_ROOT}/stages/intake.md` §1; anything not stated is recorded as `not stated` and is not a constraint).
2. **Create the run.** `run_id` = `<YYYY-MM-DD>-kill-<slug>`. `mkdir -p ventures/runs/<run_id>/ideas/I01`. Write `00-contract.md` (starting point: path a, in their words: the idea; depth mode: `direct-kill`) and `run-log.md`. Create `ventures/LEDGER.md` with `# venture ledger` if missing.
3. Write `ideas/I01/idea.md` in the schema: the idea **as stated**, parsed but not improved.
4. **Criteria:** `lab:prosecutor`, `Mode: criteria`, inputs `00-contract.md`, `ideas/I01/idea.md`; output `ideas/I01/criteria.md`.
5. **Copy and lock** into `ideas/I01/kill-criteria.md` (raw idea = `idea.md` § Idea as stated), `chmod 444`, sha256 into run-log § Locks.
6. **Economics and simulation:** `lab:economics-modeler`, inputs `00-contract.md`, `ideas/I01/idea.md`; output `ideas/I01/economics-v1.md`. (Without it, a PASS is impossible.) Then run the simulation and the money gate as in `${CLAUDE_PLUGIN_ROOT}/stages/forge.md` §4, writing `ideas/I01/simulation-v1.md`. If the gate fails, write `gate-v1.md`, skip steps 7–8, and report `KILL — the money doesn't work` with the What would have to change table. Direct mode is the fast version, so it skips the strategist; VIABLE ON PAPER is therefore not available here. Suggest `/lab:test` for the full framework check.
7. **Kill round 1:**
   - `lab:prosecutor` (`Mode: kill`, inputs `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`, `simulation-v1.md`);
   - then `lab:evidence-auditor` (inputs `00`, `kill-criteria.md`, `idea.md`, `economics-v1.md`, `simulation-v1.md`, `prosecution-v1.md`);
   - then the pre-judge hash check and `lab:judge` (everything for I01 plus `run-log.md`), as in §A1 step 3.
8. **Verdict.** PASS and KILL are final. A REVISE is reported as `KILL as stated — it would need: <fixable flaws>` (direct mode has no revision round), and recorded as KILL in the ledger. A Pivot candidate on a KILL is reported to the user as a suggestion to judge separately (`/lab:verdict "<candidate>"`); direct mode does not run pivots. HALTED: report tampering.
9. **Ledger.** Append an entry as in `${CLAUDE_PLUGIN_ROOT}/commands/history.md` § Append.
10. **Report** to the user: verdict, confidence, decisive reasons with file references, and the path of the verdict file. If PASS, suggest `/lab:resume <run_id>`. If KILL, suggest `/lab:ideate` to explore alternatives under the same constraints.
