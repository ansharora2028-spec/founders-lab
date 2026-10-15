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

## Test results (spec §12)

_Filled in below after running the tests._
