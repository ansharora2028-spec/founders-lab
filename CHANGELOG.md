# Changelog

All notable changes to this plugin are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [0.1.0] — 2026-10-15

### Added
- Plugin and single-plugin marketplace manifests (`venture@venture`).
- 10 subagents: local-market-scout, signal-scout, generator, screener, forge, economics-modeler, prosecutor-market, prosecutor-execution, evidence-auditor, judge.
- 8 commands: `/venture:run`, `intake`, `scout`, `generate`, `forge`, `kill` (pipeline and direct mode), `blueprint`, `ledger`.
- 4 skills: venture-rules (the nine principles), scoring-rubric (screen score + judge decision rule), idea-lenses (six lenses), file-schemas (every run file + visibility matrix).
- Kill-criteria lock: `chmod 444` + SHA-256 recorded in `run-log.md`, verified by the judge before every ruling.
- Append-only ledger at `ventures/LEDGER.md`.
- Templates for every run file and one complete fictional sample run.
