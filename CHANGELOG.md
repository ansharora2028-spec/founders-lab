# Changelog

All notable changes to this plugin are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [0.3.0] — 2026-10-15

### Added
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
