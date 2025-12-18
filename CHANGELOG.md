# CHANGELOG

All notable changes to TURNBACK will be documented in this file.

## [0.1.0] - 2025-12-18

### Added
- `README.md` project homepage defining scope and non-goals
- `docs/taxonomy.md` canonical Issue Taxonomy (Speaker Focus / Interruption Timing)
- `docs/signals.md` reference signal heuristics (rule-level, interpretable)
- `.github/ISSUE_TEMPLATE/turnback_issue.md` GitHub Issue template for standardized reporting
- `CONTRIBUTING.md` contribution rules and responsibility boundaries
- `tools/turnback_cli.py` minimal CLI to convert a transcript into:
  - TURNBACK report JSON
  - optional GitHub Issue markdown draft

### Scope
- MVP focuses strictly on:
  - Speaker Focus Failure
  - Interruption Timing Failure
- Refusal, moderation, privacy compliance, and model training are explicitly out of scope.

### Notes
- TURNBACK is infrastructure: it standardizes feedback, not behavior policies.
- Redaction in v0.1 is optional and basic (email/phone patterns only).


Sample release note snippet
TURNBACK v0.1.0 ships the minimum feedback loop: taxonomy + issue template + CLI report generator.
It targets speaker focus failures and interruption timing failures in real-world conversations.
