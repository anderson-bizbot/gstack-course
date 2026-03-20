# gstack Skills Catalog

> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack)
> 21 skills | Generated: 2026-03-20 22:58 UTC

## How to Use This Course

Each skill has a **lesson file** in `references/lessons/` that teaches you:
- What the skill does (plain English)
- When to use it
- What you say to Claude to trigger it
- What Claude will ask you
- What you get out of it
- Where it fits in the sprint workflow

Read the lesson for any skill you want to learn. Start with `/office-hours`.

## Quick Reference

| Phase | Skill | What You Say | One-Liner |
|-------|-------|-------------|-----------|
| Think | [`/design-consultation`](lessons/gstack-design-consultation.md) | Type `/design-consultation` | Design consultation: understands your product, researches th |
| Think | [`/office-hours`](lessons/gstack-office-hours.md) | Type `/office-hours` | YC Office Hours — two modes. Startup mode: six forcing quest |
| Think | [`/plan-ceo-review`](lessons/gstack-plan-ceo-review.md) | Type `/plan-ceo-review` | CEO/founder-mode plan review. Rethink the problem, find the  |
| Think | [`/plan-design-review`](lessons/gstack-plan-design-review.md) | Type `/plan-design-review` | Designer's eye plan review — interactive, like CEO and Eng r |
| Think | [`/plan-eng-review`](lessons/gstack-plan-eng-review.md) | Type `/plan-eng-review` | Eng manager-mode plan review. Lock in the execution plan — a |
| Review | [`/design-review`](lessons/gstack-design-review.md) | Type `/design-review` | Designer's eye QA: finds visual inconsistency, spacing issue |
| Review | [`/investigate`](lessons/gstack-investigate.md) | Type `/investigate` | Systematic debugging with root cause investigation. Four pha |
| Review | [`/review`](lessons/gstack-review.md) | Type `/review` | Pre-landing PR review. Analyzes diff against the base branch |
| Test | [`/browse`](lessons/gstack-browse.md) | Type `/browse` | Fast headless browser for QA testing and site dogfooding. Na |
| Test | [`/qa`](lessons/gstack-qa.md) | Type `/qa` | Systematically QA test a web application and fix bugs found. |
| Test | [`/qa-only`](lessons/gstack-qa-only.md) | Type `/qa-only` | Report-only QA testing. Systematically tests a web applicati |
| Test | [`/setup-browser-cookies`](lessons/gstack-setup-browser-cookies.md) | Type `/setup-browser-cookies` | Import cookies from your real browser (Comet, Chrome, Arc, B |
| Ship | [`/document-release`](lessons/gstack-document-release.md) | Type `/document-release` | Post-ship documentation update. Reads all project docs, cros |
| Ship | [`/retro`](lessons/gstack-retro.md) | Type `/retro` | Weekly engineering retrospective. Analyzes commit history, w |
| Ship | [`/ship`](lessons/gstack-ship.md) | Type `/ship` | Ship workflow: detect + merge base branch, run tests, review |
| Safety | [`/careful`](lessons/gstack-careful.md) | Type `/careful` | Safety guardrails for destructive commands. Warns before rm  |
| Safety | [`/freeze`](lessons/gstack-freeze.md) | Type `/freeze` | Restrict file edits to a specific directory for the session. |
| Safety | [`/guard`](lessons/gstack-guard.md) | Type `/guard` | Full safety mode: destructive command warnings + directory-s |
| Safety | [`/unfreeze`](lessons/gstack-unfreeze.md) | Type `/unfreeze` | Clear the freeze boundary set by /freeze, allowing edits to  |
| Meta | [`/upgrade`](lessons/gstack-upgrade.md) | Type `/upgrade` | Upgrade gstack to the latest version. Detects global vs vend |
| Other | [`/gstack`](lessons/gstack.md) | Type `/gstack` | Fast headless browser for QA testing and site dogfooding. Na |

## The Sprint (Read in This Order)

gstack is a process. Skills chain together:

```
Think:  /office-hours → /plan-ceo-review → /plan-eng-review
                        /plan-design-review → /design-consultation
Build:  [you + Claude write code]
Review: /review → /investigate → /design-review
Test:   /qa → /qa-only → /browse
Ship:   /ship → /document-release → /retro
Safety: /careful → /freeze → /guard → /unfreeze
```

## Lessons by Phase

### Think

- [`/design-consultation`](lessons/gstack-design-consultation.md) — Design consultation: understands your product, researches the landscape, propose
- [`/office-hours`](lessons/gstack-office-hours.md) — YC Office Hours — two modes. Startup mode: six forcing questions that expose
- [`/plan-ceo-review`](lessons/gstack-plan-ceo-review.md) — CEO/founder-mode plan review. Rethink the problem, find the 10-star product,
- [`/plan-design-review`](lessons/gstack-plan-design-review.md) — Designer's eye plan review — interactive, like CEO and Eng review.
- [`/plan-eng-review`](lessons/gstack-plan-eng-review.md) — Eng manager-mode plan review. Lock in the execution plan — architecture,

### Review

- [`/design-review`](lessons/gstack-design-review.md) — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problem
- [`/investigate`](lessons/gstack-investigate.md) — Systematic debugging with root cause investigation. Four phases: investigate,
- [`/review`](lessons/gstack-review.md) — Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM

### Test

- [`/browse`](lessons/gstack-browse.md) — Fast headless browser for QA testing and site dogfooding. Navigate any URL, inte
- [`/qa`](lessons/gstack-qa.md) — Systematically QA test a web application and fix bugs found. Runs QA testing,
- [`/qa-only`](lessons/gstack-qa-only.md) — Report-only QA testing. Systematically tests a web application and produces a
- [`/setup-browser-cookies`](lessons/gstack-setup-browser-cookies.md) — Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the

### Ship

- [`/document-release`](lessons/gstack-document-release.md) — Post-ship documentation update. Reads all project docs, cross-references the
- [`/retro`](lessons/gstack-retro.md) — Weekly engineering retrospective. Analyzes commit history, work patterns,
- [`/ship`](lessons/gstack-ship.md) — Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION,

### Safety

- [`/careful`](lessons/gstack-careful.md) — Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,
- [`/freeze`](lessons/gstack-freeze.md) — Restrict file edits to a specific directory for the session. Blocks Edit and
- [`/guard`](lessons/gstack-guard.md) — Full safety mode: destructive command warnings + directory-scoped edits.
- [`/unfreeze`](lessons/gstack-unfreeze.md) — Clear the freeze boundary set by /freeze, allowing edits to all directories

### Meta

- [`/upgrade`](lessons/gstack-upgrade.md) — Upgrade gstack to the latest version. Detects global vs vendored install,

### Other

- [`/gstack`](lessons/gstack.md) — Fast headless browser for QA testing and site dogfooding. Navigate any URL, inte
