# Changelog

All notable changes to this plugin are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [0.5.0] — 2026-10-15

### Added
- **VIABLE ON PAPER** verdict, between PASS and KILL: ≥70% of simulated runs viable, ≥90% within capital, no fatal flaw, the gap backed by peer-town / brand-absence / founder-counted evidence, only offline-only gaps left, and a strategist CARRY. It lists the 2–3 assumptions to confirm, with cheap checks and stop numbers.
- **market-strategist** (11th agent): an independent full framework check (competitors and steal-ability, price ladder, Five Forces, Blue Ocean, JTBD, need-gap, value proposition, Kano, consumer behaviour, STP, bottom-up TAM/SAM/SOM, Ansoff, PESTLE, 4Ps, funnel, moat, simulated customer panel), with CARRY or DROP before any judge. New `frameworks` skill.
- **Simulation:** `scripts/simulate.py`, a seeded Monte Carlo with evidence haircuts and sensitivity ranking, run by the orchestrator. `simulation-v<n>.md` per idea; `tests/test_simulate.py` in CI.
- **Founder knowledge questionnaire** (`00-founder-knowledge.md`): observation-based, with ranges and how-known tags.
- **Small-town toolkit** for the local scout: peer-town benchmark, big-brand presence map, city profile, government and proxy data.
- **City memory:** `ventures/cities/<city>.md`, append-only.
- **Evidence tiers** in rule 8: verified, peer-town, founder-counted, founder-estimate, assumption, and simulated (never evidence).
- The generator's longlist adds the biggest competitor, our price versus theirs, why customers would switch, and the Ansoff quadrant.

### Changed
- Pipeline: forge → **strategist** → economics → **simulation** → kill.
- Rule 9: thin online data is not evidence against an idea.
- REVISE requires at least one desk-fixable failure.
- Blueprint handles VIABLE ON PAPER, appends city memory, and no longer calls nothing-passed a "successful run".

## [0.4.0] — 2026-10-15

### Changed
- **Rule 1: builders aim to pass, judges stay neutral, and a false pass is the worst outcome.** Scouts, generator, forge and economics now work to find an idea that honestly passes. The judge's bar is unchanged.
- Scouts build a money map: where people already pay (`D..` demand anchors) and what paying customers complain about. They research more deeply (≥25 and ≥20 searches).
- The generator follows the money, longlists ≥3× the ideas it needs, pre-checks each against the pass bar, and keeps the strongest. It now runs on the session model.
- The screen score uses **market proof** instead of novelty.
- Economics states what would have to change for the cautious case to work.

### Added
- The nothing-passed report has a **Why the search missed** section, and its generation lessons go into the ledger.
- `/venture:run --wave2 [run_id]`: a second wave of ideas from the same contract and scouting. It is offered automatically when nothing passes.

## [0.3.0] — 2026-10-15

### Fixed
- `tests/e2e.sh` network check printed `000000` for a blocked host. A first fix then aborted under `set -e`. It now prints `000` and continues.

### Added
- `/venture:check "<idea>" [--variants]`: runs the user's own idea through the full pipeline (scouting focused on the idea, explanation, screen, locked criteria, forge, three-scenario economics, prosecution, audit, one revision round) and gives a clear DO IT / DON'T DO IT verdict. With `--variants`, it also tests up to 3 one-change variants. New depth modes `check` and `check+variants`.
- `tests/e2e.sh check "<idea>"` to test `/venture:check` end to end.
- README rewritten for aspiring founders: purpose, getting started in 3 steps, which command to use, what you'll be asked, what you get, time and cost. Technical detail is under "Under the hood".
- Every idea carries three plain-language explanations: **how it works**, **the need gap**, and **how it makes money**. They appear in `03-ideas.md` and as cards shown to the user at generation and in the final run summary. Forge writes fuller versions, the blueprint explains the winning idea the same way, and the nothing-passed report explains every idea before saying why it died.

## [0.2.0] — 2026-10-15

### Added
- Judge **pivot candidate**. On a KILL whose only fix changes the customer, problem or revenue model, the judge may name a candidate (pivots left, HARD constraints met, grounded in surviving evidence). It re-enters Screen as a new idea. The KILL stands.
- `hooks/judge-bash-guard.sh`: a plugin PreToolUse hook that limits the judge's Bash to hashing `kill-criteria.md`.
- CI workflow: strict validation, schema/reference checks, hook unit tests, blindness checks on recorded transcripts (plus a must-fail fixture).
- `tests/check_schemas.py`, `tests/test_judge_guard.sh`, `tests/trim_transcript.py`, `tests/fixtures/`.

### Changed
- Quick mode carries 2 ideas forward (was 1).
- Timestamps come from `date -u`. Agents receive a `Timestamp:` line instead of guessing.
- `/venture:kill` never re-handles an idea recorded as PIVOTED, and blueprint resolves final status from the pivot record first.
- Forge round 1 keeps an empty `Fixes (round 2 only)` section.
- Author and owner are set in the manifests.

### Fixed
- Invented timestamps in run-logs and file front matter.
- Re-running `/venture:kill` after a pivot could pivot the old idea a second time.

## [0.1.0] — 2026-10-15

### Added
- Plugin and single-plugin marketplace manifests (`venture@venture`).
- 10 subagents: local-market-scout, signal-scout, generator, screener, forge, economics-modeler, prosecutor-market, prosecutor-execution, evidence-auditor, judge.
- 8 commands: `/venture:run`, `intake`, `scout`, `generate`, `forge`, `kill` (pipeline and direct mode), `blueprint`, `ledger`.
- 4 skills: venture-rules (the nine principles), scoring-rubric (screen score + judge decision rule), idea-lenses (six lenses), file-schemas (every run file + visibility matrix).
- Kill-criteria lock: `chmod 444` + SHA-256 recorded in `run-log.md`, verified by the judge before every ruling.
- Append-only ledger at `ventures/LEDGER.md`.
- Templates for every run file and one complete fictional sample run.
