# Decisions

Where the build spec was silent, ambiguous, or out of date with the current Claude Code plugin docs, this file records what was chosen and why. Test results from spec §12 are at the end.

Docs checked on 2026-10-15 (Claude Code 2.1.300): [plugin manifest reference](https://code.claude.com/docs/en/plugins-reference), [marketplace reference](https://code.claude.com/docs/en/plugins/marketplace-reference), [create a marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [subagents](https://code.claude.com/docs/en/sub-agents), [slash commands / skills](https://code.claude.com/docs/en/slash-commands).

## Packaging

**D1. The plugin lives at the repository root, and the repo is also the marketplace.** The spec's layout puts everything under a `venture/` folder that is itself the repo (`/plugin marketplace add <github-user>/venture`). This repository is `founders-lab`, so the plugin files sit at its root and `marketplace.json` lists one plugin with `"source": "./"` (the docs allow a relative source that is the marketplace root). Install is `/plugin marketplace add ansharora2028-spec/founders-lab` then `/plugin install venture@venture`. If the repo is renamed to `venture`, only the README's install lines change.

**D2. marketplace.json schema differs slightly from the spec's assumption.** The current schema requires `name`, `owner` (with `owner.name`) and `plugins`; each entry needs `name` and `source`. A top-level `description` is recommended (the validator warns without it). The file follows the docs. The name `venture` appears only in `plugin.json`, `marketplace.json` and user-facing text/subagent ids (`venture:<agent>`), which Claude Code derives from the plugin name.

**D3. `commands/` is kept even though the docs now prefer `skills/` for new plugins.** The spec asks for `commands/`, the directory is still supported, and the commands load as `/venture:<name>`. The four reference skills set `user-invocable: false` so they don't clutter the `/` menu; agents and commands read them by path.

**D4. Skills are read by path via `${CLAUDE_PLUGIN_ROOT}`.** The docs confirm `${CLAUDE_PLUGIN_ROOT}` is substituted inline in command, skill and agent Markdown bodies. Every agent and command begins by reading `${CLAUDE_PLUGIN_ROOT}/skills/venture-rules/SKILL.md`, which satisfies the spec's "begin by reading" requirement without depending on skill preloading.

**D5. Subagents *can* now spawn subagents (spec §3 says they cannot).** Current docs allow nesting up to three levels. No venture agent is given the `Agent` tool, so specialists still cannot spawn others or talk to the user; only the main session orchestrates.

**D6. Agent model choices follow the spec exactly:** screener `haiku`; prosecutors, auditor, judge `inherit`; everything else `sonnet`. Each is one `model:` line.

## Pipeline mechanics

**D7. Prosecutors write criteria drafts to their own files, and the main session merges them.** Criteria mode outputs `ideas/<id>/criteria-market.md` and `criteria-execution.md` (not in spec §5). Each agent must write exactly one file, so the merge into `kill-criteria.md` is a verbatim copy by the main session, followed by `chmod 444` and a SHA-256 entry in `run-log.md` § Locks.

**D8. The evidence auditor runs after the prosecutors, not in parallel with them.** Spec §6.6 says to launch both prosecutors and the auditor in parallel, but §8.9 requires the auditor to check "every claim a prosecutor uses to justify a FATAL flaw", which it can't do before the prosecutions exist. Principle 8 (the auditor strikes claims before the Judge rules) wins: prosecutors run in parallel, then the auditor, then the judge. Parallelism across ideas is kept at every step.

**D9. Forge's round-2 input is an extracted file, not the verdict.** The verdict contains the criteria table, which Forge must never see. The main session copies only the Judge's "Fixable flaws" table into `ideas/<id>/fixable-flaws-v1.md` and passes that.

**D10. In round 2 each prosecutor also receives its *own* round-1 prosecution.** It needs its flaw ids and earlier findings to judge the diff row by row. It still never receives the other prosecutor's file, the audit, or `forge-v2.md`.

**D11. Claims carry ids (`[C07]`), referenced as `file#C07`.** The spec requires the Judge to cite "file and claim references" and the auditor to strike specific claims. Per-file claim ids make both possible without a global registry.

**D12. Pivot ids are `<old-id>-P<k>`, and the pivoted idea gets its own `03-ideas-pivot<k>.md` and `04-screen-pivot<k>.md`.** This keeps "each agent writes one file" and leaves the original generator and screener files untouched. The pivot counter is global per run (max 2), stored in `run-log.md`.

**D13. Direct kill mode runs the economics modeler on the idea as stated.** Spec §6.6 says direct kill uses "no forge". Without economics, principle 3 makes a PASS impossible by construction, so the modeler runs on `ideas/I01/idea.md` (it's not Forge, and it doesn't improve the idea). There's no scouting and no revision round in direct mode: a REVISE is reported as "would need: …" and recorded as KILL.

**D14. Non-interactive intake.** Subagents can't ask questions, and in `claude -p` sessions the main session can't either. If every intake topic is answered in the command arguments, the arguments count as the confirmed contract (`how: arguments (non-interactive)`). If anything is missing, the command stops and lists it. It never invents a constraint. This is also how the §12 tests run.

**D15. The kill-criteria lock is chmod + hash, with the hash in `run-log.md`.** The hash is not stored inside the locked file (that would change the hash). Someone who edits both the criteria and the run-log can defeat it; the lock is meant to catch accidental or agent-driven edits, not a determined user. The Judge's only Bash use is `sha256sum` (or `shasum -a 256` on macOS).

**D16. Resumable revision rounds.** `/venture:kill` resumes an idea whose round-1 verdict is REVISE at the first missing revision-round file, and always runs pivot detection before using an existing `forge-v2.md`. This makes interrupted runs recoverable and lets the pivot test inject a forged revenue-model change.

**D17. The main session uses Write/Edit for files and Bash only for `mkdir`, `chmod`, hashing and `date`.** Early test runs hit permission prompts on shell redirection, so the rule is in `venture-rules`.

**D18. Screener gets WebSearch but not WebFetch.** This follows the spec's tool list. Competitor URLs come from search results.

**D19. INSUFFICIENT EVIDENCE vs desk research.** The rubric defines "obtainable through desk research" as web search, public data and published reports, not experiments, product builds or customer surveys. The spec didn't define it, and the Judge needs a bright line.

**D20. Audit tool failures are labeled, still struck, and surfaced.** In the test container the network policy refused WebFetch to most hosts (WebSearch still worked). The auditor correctly struck every claim it couldn't open. To keep principle 8 intact while being honest about why, the auditor now writes `UNREACHABLE (tool failure)`, the audit summary counts those, and `/venture:kill` warns the user before judging when most strikes are tool failures, telling them to fix network access and re-run. Nobody un-strikes claims.

**D21. `tests/check_blindness.py` checks blindness from transcripts, not from the self-reported run-log.** It parses `claude -p --output-format stream-json --verbose` logs and checks (1) the input paths passed in every venture Agent call and (2) every Read/Glob/Grep/Bash call each subagent actually made against the visibility matrix.

**D22. Timestamps come from the clock, never from the model.** The first test runs showed invented times, such as a verdict "created" at 20:00 for a run that actually finished at 08:17. The main session now runs `date -u` before writing any time, and passes a `Timestamp:` line in every agent prompt for the agents' `created` field. Agents have no shell, so if a prompt carries no timestamp they write the date only.

**D23. A pivoted idea is final.** Its round-1 `verdict-v1.md` still says REVISE, so `/venture:kill` skips any idea that `run-log.md` § Pivots records as PIVOTED or pivot-limit-killed. Without that, re-running the command resumed the old idea's revision round and pivoted it again. `/venture:blueprint` resolves final status in a fixed order: the pivot record, then the latest verdict, then the screen.

**D24. Forge keeps the empty round-2 Fixes section in round 1** (`- none`), so every forge file matches the schema.

## v0.2 changes (after review)

**D25. The judge can name a pivot candidate on a KILL.** Under the spec's rules, REVISE is unavailable whenever the only fix changes the customer, problem or revenue model, so the judge kills, and a pivot could only happen if Forge changed the idea on its own. Principle 5 ("a pivot is a new idea") had almost no path. The judge now writes a *pivot candidate* on a KILL only when that is the sole fix, fewer than 2 pivots have been used, the candidate fits every HARD constraint, and it rests on surviving evidence. The KILL stands. The main session turns the candidate into a new idea that goes back to Screen and gets fresh locked criteria, forge and kill. Direct-kill mode only reports the candidate. The 2-pivot cap still bounds cost.

**D26. Quick mode carries 2 ideas, not 1 (departs from spec §6.1).** In testing, quick mode killed its single carried idea and left the other two ideas unjudged, so a quick run said little. Carrying 2 costs about 8 more agent calls. Standard (3) and deep (5) are unchanged.

**D27. The judge's Bash is enforced by a hook, not just instructions.** Plugin agents ignore `permissionMode` and `hooks` frontmatter, but plugin-level `hooks/hooks.json` runs inside subagents and identifies the caller (`agent_type`). `hooks/judge-bash-guard.sh` (POSIX `sh`, no jq/python/node) blocks every Bash call from `venture:judge` except one `sha256sum` or `shasum -a 256` on a single `kill-criteria.md`. It rejects chaining, substitution, redirection, globs, escapes and newlines. Calls from the main session and other agents pass through untouched. Verified live: the hook fired inside the judge with `agent_type: "venture:judge"` and allowed the real hash call. Replaying that exact payload with `ls /` or a chained command was blocked (exit 2). `tests/test_judge_guard.sh` covers 13 cases.

**D28. CI** (`.github/workflows/ci.yml`, on every push and PR):
- `claude plugin validate . --strict`.
- `tests/check_schemas.py`: plugin-root references exist, templates match schemas, example run files match schemas, agent frontmatter is complete.
- The hook unit tests.
- `tests/check_blindness.py` over trimmed transcripts of the four §12 test runs (`tests/fixtures/*.jsonl`, made with `tests/trim_transcript.py`: tool calls only, no model text or web content).
- A must-fail fixture with planted leaks, so the checker itself is tested.

**D29. Author and owner** are set to the repository owner (`ansharora2028-spec`) in both manifests and the LICENSE. The version is bumped to 0.2.0, because a set `version` pins installed users until it changes.

## Test results (spec §12)

All tests ran on 2026-10-15 with Claude Code 2.1.300, headless (`claude -p`), in a cloud container whose network policy blocked WebFetch to most hosts (see D20). Every intake was given in the arguments (D14). Costs are the `total_cost_usd` the CLI reported for each session.

| # | Test | Result |
|---|---|---|
| 1 | Validate frontmatter and manifests against current docs | **Pass.** `claude plugin validate . --strict` passes, as do `.claude-plugin/plugin.json`, `agents/`, `commands/` and `skills/` individually, with no errors or warnings. Schema differences from the spec are in D2, D3 and D5. |
| 2 | Install locally and confirm every `/venture:*` command appears | **Pass.** `claude plugin marketplace add ./` then `claude plugin install venture@venture` succeeded. `claude plugin details venture` lists all 8 commands (run, intake, scout, generate, forge, kill, blueprint, ledger), the 4 skills and the 10 agents. `/venture:ledger` ran headless in an empty project and correctly reported no past runs. |
| 3 | `/venture:run` quick mode: Pune, ₹1L, 10 hrs/week, B2C, no idea | **Pass. Outcome: NOTHING PASSED** (≈ $3.70). The run completed every stage: contract → scouting (local coverage honestly scored **3/10**, with national data labeled) → 3 ideas (rent-agreement check, Marathi/Hindi English tutor, furniture resale board) → screen (none rejected; I03 ranked first at 12/25) → criteria locked for I03 (`chmod 444`, hash in run-log) → forge → economics → 2 prosecutors → audit → judge. **KILL**, confidence 7: no locked criterion MET and no demand evidence survived. Then `91-nothing-passed.md` (savings ESTIMATE ₹10k–₹25k and 3–6 months, with assumptions) and a ledger entry. Saved as `examples/sample-run/`. |
| 4 | `/venture:kill "a new general social network for everyone, ₹50k budget"` | **Pass. KILLED** (≈ $2.44), confidence 6. Decisive reasons cite files and claims: the conservative case breaks HARD K6 (first revenue at 7 months vs 6, arithmetic verified by the auditor); ~50 retained users for the full budget vs ~4,167 needed to break even; the customer "everyone" means any fix is a pivot, so REVISE was unavailable; no demand evidence survived. Ledger appended. The network block meant 23 of 25 sourced claims were struck as UNREACHABLE. The judge ruled only on surviving claims (verified arithmetic, the idea text, ASSUMPTION-labeled inputs) and lowered its confidence. |
| 5 | Tamper test | **Pass.** On a copy of the test-4 run, `kill-criteria.md` was made writable, one threshold changed ("at least 2" → "at least 0"), re-locked, and the judge re-invoked with the standard prompt. The judge computed `7957a18a…` against the recorded `8d31d57d…`, wrote `verdict: HALTED` / `MISMATCH — HALTED`, and refused to rule. (The edit was made between lock and judgement on a copy, which is equivalent to an edit mid-run.) |
| 6 | Blindness test | **Pass.** `run-log.md` § Agent calls in every run shows prosecutors never received `forge-v2.md` or the other prosecutor's files, and forge/economics never received kill criteria. Independently, `tests/check_blindness.py` over all four transcripts checked **35 agent calls and 261 subagent file accesses: 0 violations**. The revision round was exercised on a copy of the test-3 run whose I03 verdict-v1 was changed to REVISE with three desk-researchable fixable flaws (labeled `TEST FIXTURE`). The real forge wrote `forge-v2.md`, the main session wrote `diff-v2.md` (NOT A PIVOT; 3 rows, one with evidence `NONE`), and round-2 prosecutors received only `diff-v2.md`, `economics-v2.md` and their own v1 file. The market prosecutor's file states "forge-v2.md was not read", and it rejected all three diff rows as insufficient. Final: **KILL in round 2** (≈ $2.20). Saved as `examples/revision-round/`. |
| 7 | Pivot test | **Pass** (≈ $3.12). On another copy with the same REVISE fixture, a `forge-v2.md` was injected that switched the revenue model from a ₹199 listing fee to a 10% commission while still saying `pivot declared: no`. The main session's pivot check caught the undeclared change before writing any diff. It marked `I03 → PIVOTED → I03-P1` (pivots 1/2), wrote `03-ideas-pivot1.md`, and re-screened (`04-screen-pivot1.md`, 7/25). It then locked fresh criteria for I03-P1 (new hash `bb57d9c8…`) and ran forge, economics, both prosecutors, the audit and the judge from zero. I03-P1 was **KILLED** in round 1: conservative contribution ₹117 per sale vs ₹1,064 blended CAC, and a 40% commission collection rate vs the 60% its locked criteria require. Saved as `examples/pivot/`. |
| 8 | Save one complete run | **Done.** `examples/sample-run/` is the unmodified test-3 run (absolute paths replaced with `<project>`, and the kill-criteria hash still matches). `examples/revision-round/` and `examples/pivot/` hold the round-2 and pivot artifacts. |

### Debugging pass (after the §12 tests)
- **Static checks:** every `${CLAUDE_PLUGIN_ROOT}` path referenced in agents, commands and skills exists. Every template's H2 sections match its schema. Every agent output from the test runs matched its schema, except forge round 1 omitting the empty Fixes section (fixed, D24).
- **Prompt leak check:** every Agent prompt in all four transcripts contained only the standard fields (run folder, mode, idea id, round, input paths, output path, date, focus). No chat context or summaries of other files leaked.
- **Bugs found and fixed:** invented timestamps (D22), and the re-pivot of an already-pivoted idea on re-run (D23).
- **D23 verified live:** re-running `/venture:kill` on the finished pivot run launched no agents and changed no files. `/venture:blueprint` then resolved I03 → PIVOTED, I03-P1 → KILL and I01/I02 → NOT CARRIED. It appended an `(amended)` ledger entry and kept the original. Its timestamp (09:11:13Z) fell inside the command's real run window (09:10:40–09:12:03).

### Observations from testing
- **Kill won every time**, which is consistent with principle 1. It's also partly an artifact of the blocked network: when the auditor can't verify demand evidence, a PASS is impossible. A PASS path was not observed in testing. Running in an environment with open web access is the next thing to check.
- In tests 6 and 7 the orchestrator noticed the fixture's inconsistency (verdict-v1 says REVISE; the ledger and nothing-passed report say KILL) and reported it rather than hiding it. It also declined to edit agent files or the append-only ledger.
- Early runs hit permission prompts when the main session used shell redirection to write files. The fix is D17.
