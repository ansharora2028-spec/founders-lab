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

## v0.3 changes

**D30. Every idea is explained in plain language: how it works, the need gap, how it makes money.** A one-line pitch plus customer/problem/revenue fields wasn't enough for a user to understand what was being suggested. The generator now writes three explanation lines per idea. Forge writes fuller `How it works`, `Need gap` and `How it makes money` sections. The user sees them as cards at generation, in the final run summary, and in `90-blueprint.md` / `91-nothing-passed.md` (`The ideas, explained`). They explain the idea without selling it: numbers are sourced or marked `ASSUMPTION`, and the real model stays with the economics modeler. Because the cards are part of the idea block, they are also copied into the locked kill criteria's raw idea, so the prosecutors judge the same idea the user read.

**D31. `/venture:check "<idea>"` gives a founder's own idea the full pipeline.** Before this, a user's own idea either got the fast direct verdict (`/venture:kill "<idea>"`: judged as written, with no scouting, forge or revision) or had to compete with generated ideas in `/venture:run` path (a). Neither matched what founders asked for: "check my idea the way you check the others, run the economics, then tell me whether to do it." `/venture:check` reuses every stage through two new depth modes:
- `check`: only the user's idea, which is always carried forward unless Screen rejects it on a HARD constraint;
- `check+variants` (`--variants`): the user's idea plus up to 3 one-change variants, with the best variant also carried.

Intake asks one extra question: "who would pay for this, and how would you charge?" The generator writes the idea up faithfully. Anything the user did not state is marked `not stated by the user — ASSUMPTION`, and improving the idea is left to forge, under evidence. The final message leads with **DO IT / DON'T DO IT** and the plain-language explanation. The judge applies the same rule as for any idea.

**D32. The README is written for aspiring founders first.** The top half covers what the tool is for (test an idea on paper before spending savings on it), who it's for, a real idea card, three steps to get started, a "where are you?" table of commands, the intake questions, a plain-language walk through the pipeline, time and cost, and honest limits. Technical detail (rules, all commands, depth modes, pipeline diagram, run folder, ledger, testing) moved under "Under the hood".

## v0.4 changes: better ideas

**D33. Builders aim to pass; judges stay neutral (replaces spec principle 1, "Kill can win", at the owner's request).** In testing, every idea died. Part of the cause was the environment: the blocked network meant no demand evidence survived the audit. Part was the design:
1. **Wrong incentive.** Every agent was told a kill was a success, so the agents that *make* ideas had no reason to strive.
2. **Wrong screen reward.** The screen gave "open market, no competitors" 5/5, while the pass rule requires proof that people already pay.
3. **Wrong starting point.** The generator worked from trends rather than from spending.

Changes:
- **Roles.** Rule 1 now splits the agents. The **builders** (scouts, generator, forge, economics) work to find an idea that honestly passes; a pass is their success and nothing passing is a miss they must diagnose. The **judges** (prosecutors, auditor, judge) are neutral. A *false* pass is named as the worst outcome, so the evidence bar and the judge's decision rule are unchanged.
- **Money map.** Scouts build one: `Money already moving` (`D..` demand anchors: who pays, how much, to whom, with evidence) plus complaints about paid options. Minimum research depth is ≥25 local and ≥20 signal searches.
- **Generator.** It follows the money, longlists ≥3× the needed ideas, and pre-checks each candidate against the pass bar (demand anchor, gap, cautious money math, most likely killer) before keeping the strongest. It reads the rubric's pass rule. Its model moved from `sonnet` to `inherit`, because idea quality is the bottleneck and it is a single call.
- **Screen.** *Novelty* is replaced by **market proof** (people already pay in the target market and there's an evidenced gap). Novelty is still recorded, but no longer scores.
- **Forge and economics.** Forge looks for the strongest honest version of the idea: demand evidence, the narrowest segment, the cheapest real channel. Economics states exactly which number would have to change for the cautious case to work.
- **Learning loop.** A nothing-passed report diagnoses **why the search missed**: per death, the type (generation, constraint, evidence access, or bad luck) and where it should have been caught, plus generation lessons. Those lessons go into the ledger. `/venture:run --wave2` generates a second wave of ideas from the same contract and scouting using those lessons, with no new scouting cost. When nothing passes, `/venture:run` offers it.

**D34. The generator checks each idea's earning ceiling at the founder's hour limit, and counts only spending on the same job as a demand anchor.** Both rules came from the v0.4 run's own "Why the search missed" lessons. The refund-claim idea was profitable per sale, but at 10 h/week it could only ever earn about ₹4,400 a month. Its "demand anchor" was coaching fees, which is spending in a nearby category, not on refund help.

## v0.5 changes: fair to small towns, full framework check, simulation

**D35. Thin online data is no longer treated as evidence against an idea.** Before v0.5, "no local data online" became INSUFFICIENT EVIDENCE, which counted as NOT MET, which meant KILL. That systematically punished small towns, which are often under-served precisely because big brands and the internet haven't reached them. Five changes fix it:
1. **Evidence tiers (rule 8).** `source` (verified) > `PEER-TOWN` > `FOUNDER-COUNTED` > `FOUNDER-ESTIMATE` > `ASSUMPTION`, and `SIMULATED` is never evidence. Only verified sources support a PASS. Peer-town and founder-counted claims support VIABLE ON PAPER. The auditor checks peer-town arithmetic and sources, and checks that founder claims match the founder's file and carry the right tier.
2. **Founder knowledge questionnaire** (`00-founder-knowledge.md`): 8 town questions plus 4 idea questions. It asks for observations, not opinions ("what did you last pay?", not "would people pay?"), with ranges and a how-known tag (counted / heard / guess), all skippable, never filled in for the founder.
3. **The local scout's small-town toolkit:**
   - a peer-town benchmark (5–10 comparable towns, suppliers per 10,000 people, under-served or over-served);
   - a big-brand presence map;
   - a city profile (how people buy, payment, trust, language, seasonality, income cycles, delivery reach, migration);
   - government and proxy data.
4. **City memory** (`ventures/cities/<city>.md`): append-only, verified facts only, plus peer-town results, brand presence, the city profile and founder answers (marked unverified). Every later run in that town reads it.
5. **A new verdict, VIABLE ON PAPER** (D37).

**D36. An 11th agent, `market-strategist`, runs the full framework check independently of forge (lifts the spec's 10-agent cap, at the owner's request).** It covers:
- **competition:** competitor map (including big national players and "do nothing"), steal-ability, price ladder, Porter's Five Forces, Blue Ocean ERRC;
- **the customer:** Jobs-to-be-Done, need-gap, value proposition canvas, Kano, consumer behaviour (adoption, trust, habit, price sensitivity, decision-maker versus user);
- **market and strategy:** STP, bottom-up TAM/SAM/SOM, Ansoff, PESTLE, 4Ps, AIDA funnel, moat;
- **a simulated customer panel**, for objections only.

Every framework answers one decision question and ends with SUPPORTS / NEUTRAL / AGAINST (`skills/frameworks/SKILL.md`). Two critical AGAINSTs (on buyer power or substitutes, steal-ability, price ladder or channel access), or one on verified evidence that can't be fixed without a pivot, mean **DROP**: the idea stops before any judge, cheaply. A drop is a builder's own call and can't create a false pass. The strategist runs after forge, because it needs the sharpened idea, and before economics, which uses its price, funnel and churn numbers. It never sees kill criteria. The generator also gets a light version in its longlist (biggest competitor, their price versus ours, why customers would switch, Ansoff quadrant), so weak ideas die before forge. SWOT is deliberately left out: the strategist's strengths/risks summary covers it.

**D37. VIABLE ON PAPER: definition and threshold.** All five must hold:
1. ≥**70%** of simulated runs break even by the contract's time-to-first-revenue limit within the capital limit, **and** ≥**90%** of runs never exceed the HARD capital limit;
2. no FATAL flaw survived the audit;
3. the gap is backed by surviving PEER-TOWN, brand-absence or FOUNDER-COUNTED evidence;
4. every unmet criterion is an *offline-only gap* (the proof sits offline in this town, and nothing contradicts it);
5. it fits the contract, and the strategist said CARRY with no unmitigated critical AGAINST.

The threshold was the owner's call to delegate. **70%** was chosen over 60% because a false pass is the worst outcome: the bar tolerates at most 30% odds of not breaking even in time, and losing more than the founder can afford must be rare (≤10% of runs). The verdict lists the 2–3 assumptions to confirm, taken from the simulation's sensitivity ranking, each with a cheap check and a "stop if" number. It is reported as "viable on paper, not proven", never as a PASS. REVISE was adjusted: round 1 REVISE now needs at least one desk-fixable failure, and tolerates offline-only gaps alongside it, so a revision round is used only when desk research can help. VIABLE ON PAPER is allowed in round 1 or 2. Direct `/venture:kill` skips the strategist, so it can't give VIABLE ON PAPER; it points to `/venture:check`.

**D38. The simulation is a real script run by the orchestrator, not a builder.** `scripts/simulate.py` (standard-library Python) runs a seeded Monte Carlo: 5,000 runs by default, with triangular distributions from each input's low / likely / high. It models monthly acquisition (reach × conversion, capped by the founder's hour limit), churn, revenue, variable and fixed costs, marketing spend and cash. It reports:
- the viable share and the share within capital;
- P10 / P50 / P90 profit, cash and peak cash need;
- a sensitivity ranking ("what matters most").

Weaker evidence gets a cautious haircut in the unfavourable direction: 0% for verified, 10% for peer-town and founder-counted, 25% for founder estimates and assumptions. The economics agent only writes the `## Simulation inputs` JSON block. The main session runs the script and pastes its stdout unedited into `simulation-v<n>.md`, so the builder whose idea it is can't author the result. Because the seed is fixed, anyone can re-run it. Without `python3`, the simulation is marked "not run" and VIABLE ON PAPER isn't available; PASS and KILL still work. `tests/test_simulate.py` (10 tests) runs in CI.

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

### v0.2.0 end-to-end run (quick mode, same fictional Pune user)
A full `/venture:run` with the v0.2 plugin, in the same restricted-network container. It is saved as `examples/quick-run-v0.2/`, with its trimmed transcript in `tests/fixtures/v2-quick.jsonl`.
- **Outcome: NOTHING PASSED** ($6.81, 15 minutes, 09:23–09:38 UTC). Quick mode carried **2** ideas (D26), using 20 agent calls as estimated.
  - I01 (₹199 WhatsApp refund-complaint service): **KILL**, confidence 7. Forge's own file names free AI chat tools as the substitute for the drafting, which a locked criterion forbids. The locked volume doesn't fit in 10 h/week, and the conservative case loses ₹403/month.
  - I03 (₹399 tenant protection kit): **KILL**, confidence 5. Conservative CAC is ₹1,426 against ₹170 gross profit on a one-time sale.
  - I02 was not carried (7/25).
- **Pivot candidate (D25):** both judges evaluated it and wrote `none`. Pivots were available and the fatal flaws did point to a change of payer or revenue model, but no surviving evidence showed that the alternative payer would pay. Proposing one would have meant inventing it. That is the intended conservative behavior. A candidate that is actually spawned has not yet been observed, and needs open network access for evidence to survive.
- **Hook (D27):** both judges' `sha256sum` calls passed the guard (hash MATCH on both).
- **Timestamps (D22):** every `created`, Locks and Stages time came from `date -u`. Agent files carry their launch timestamp, and no file claims a time after its modification time.
- **Permissions:** 0 permission denials in the transcript (D17).
- **Blindness:** `tests/check_blindness.py` found 20 agent calls and 143 subagent file accesses, 0 violations.
- **Network:** a fresh cloud session on the same environment was also refused by the proxy (Wikipedia, Reddit, TechCrunch, inc42 all 403), so the environment's network policy is still restricted. The open-network run is still to do: `sh tests/e2e.sh standard` once access is widened.

### v0.3 runs: idea explanations and `/venture:check`
- **Quick run** ($7.24): every idea in `03-ideas.md` carried the three explanation lines. Forge wrote the new How it works / Need gap / How it makes money sections. Need gaps were honest: one named a funded competitor at the same price (SpeakX, ₹299) and called the gap narrow. The final message showed one plain-language card per carried idea, and `91-nothing-passed.md` had "The ideas, explained".
- **`/venture:check`** ($4.04, 12 agent calls, 0 blindness violations; saved as `examples/check-run/`). Intake recorded the charging question, and the depth mode was `check`. The generator wrote up only I01, faithfully, marking every unstated detail as an ASSUMPTION. Verdict: DON'T DO IT (KILL, confidence 6). The decisive reason was verified arithmetic, independent of the blocked network: break-even needs two groups and 12 h/week against HARD K2 = 10 h. The final message led with the verdict, then how it works, the need gap, the money math, quoted reasons, savings, and what would have to be true.
- **Bug found:** `tests/e2e.sh` printed `000000` for blocked hosts, and the first fix aborted under `set -e`. Both are fixed.

### v0.4 run: builders aim to pass ($11.62, 26 agent calls, 0 blindness violations; saved as `examples/quick-run-v0.4/`)
- **Scouting:** the money map found 13 demand anchors (for example MPSC/UPSC coaching at ₹50k–1.25L, Urban Company deep cleaning with 220k+ reviews, dog care, children's camps) and complaints about paid options (rushed cleaning, coaching refund refusals). Local coverage was 4/10, up from 3.
- **Generation:** the generator longlisted 9 candidates, dropped 6 with concrete reasons (no anchor, breaks K2, outside K6, market already served), and kept 3, each tied to a demand anchor and a complaint.
- **Screen:** market proof scored as designed, rating paid demand above empty markets, and the tie-break on market proof worked.
- **Verdicts:** I01 earned the **first REVISE** of any test run: positive conservative economics (₹438 contribution per file, ₹11.5k peak outlay, 6.4 h/week, about 1.5 months to first revenue) and no surviving FATAL flaw. Forge's round 2 brought 11 diff rows: consumer-commission refund orders, a Bar Council ruling with the deliverable redesigned to fit it, sourced CPCs, an hours table and a day-30 plan. Both prosecutors rejected all 11 rows, mainly because every source was a search snippet that couldn't be opened, so the idea was KILLED in round 2. I03 was KILLED on negative conservative economics (−₹251 per job before CAC).
- **Learning loop:** `91-nothing-passed.md` § Why the search missed separated generation causes (I01's anchor was spending in a nearby category; I03's margin never worked) from evidence-access causes, wrote 4 concrete lessons, and the run offered a second wave. Lessons 1 and 2 are now built into the generator (D34).
- **Takeaway:** the builders now produce ideas that get close to the bar on economics. What stops a PASS in this environment is verification: no page can be opened, so demand evidence can't survive the audit.

### v0.5 run: small-town `/venture:check`, open network ($7.50, 14 agent calls, 0 blindness violations; saved as `examples/small-town-check-v0.5/`)
- Idea: ₹600/month after-school spoken-English batches for class 6-10 in Satara, with K1 ₹75,000 HARD, K2 12 h/week and K6 2 months. Founder answers Q1-Q12 were given up front.
- The whole v0.5 path ran: founder knowledge, peer-town and brand map, strategist (CARRY, no critical AGAINST), economics with simulation inputs, and `simulate.py` run by main. The simulation found 2.6% of runs viable by month 2, against the 70% bar, and 40% never break even in 12 months.
- Verdict: **KILL**, confidence 6. The conservative case breaks the HARD capital limit (about -₹99,400 at month 12). No FATAL flaw, and the market criteria were INSUFFICIENT EVIDENCE rather than NOT MET. VIABLE ON PAPER was correctly withheld because the simulation bar failed. The report names what would flip it: a free venue, about 2.3 new students a month, and the draft Maharashtra coaching Act.
- With the open network the auditor checked 58 claims and struck 14 for real reasons, not for blocked fetches.
- Quirks:
  - The judge's first `sha256sum` was blocked by the sandbox because the path was outside the shell's cwd, and the first judge call wrote no verdict. A re-run computed the matching hash with `shasum -a 256`, and the guard allows both.
  - In this headless harness the orchestrator wrote files under a path whose directory name differed from the shell cwd. That is a test-harness artifact.
- The standard-mode open-network run was stopped early at the user's request to save tokens. A PASS or VIABLE ON PAPER has still not been observed live.

### Observations from testing
- **Kill won every time**, which is consistent with principle 1. It's also partly an artifact of the blocked network: when the auditor can't verify demand evidence, a PASS is impossible. A PASS path was not observed in testing. Running in an environment with open web access is the next thing to check.
- In tests 6 and 7 the orchestrator noticed the fixture's inconsistency (verdict-v1 says REVISE; the ledger and nothing-passed report say KILL) and reported it rather than hiding it. It also declined to edit agent files or the append-only ledger.
- Early runs hit permission prompts when the main session used shell redirection to write files. The fix is D17.
