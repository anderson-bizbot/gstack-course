# gstack Skills Catalog

> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack) **templates**
> 28 skills | Generated: 2026-03-24 14:37 UTC

## Quick Reference

| Phase | Skill | What You Say | Lines | Version |
|-------|-------|-------------|-------|---------|
| Think | [`/design-consultation`](lessons/design-consultation.md) | `/design-consultation` | 373 | 1.0.0 |
| Think | [`/office-hours`](lessons/office-hours.md) | `/office-hours` | 648 | 2.0.0 |
| Think | [`/plan-ceo-review`](lessons/plan-ceo-review.md) | `/plan-ceo-review` | 810 | 1.0.0 |
| Think | [`/plan-design-review`](lessons/plan-design-review.md) | `/plan-design-review` | 320 | 2.0.0 |
| Think | [`/plan-eng-review`](lessons/plan-eng-review.md) | `/plan-eng-review` | 268 | 1.0.0 |
| Review | [`/design-review`](lessons/design-review.md) | `/design-review` | 268 | 2.0.0 |
| Review | [`/investigate`](lessons/investigate.md) | `/investigate` | 198 | 1.0.0 |
| Review | [`/review`](lessons/review.md) | `/review` | 282 | 1.0.0 |
| Test | [`/browse`](lessons/browse.md) | `/browse` | 143 | 1.1.0 |
| Test | [`/qa`](lessons/qa.md) | `/qa` | 318 | 2.0.0 |
| Test | [`/qa-only`](lessons/qa-only.md) | `/qa-only` | 103 | 1.0.0 |
| Test | [`/setup-browser-cookies`](lessons/setup-browser-cookies.md) | `/setup-browser-cookies` | 77 | 1.0.0 |
| Ship | [`/document-release`](lessons/document-release.md) | `/document-release` | 359 | 1.0.0 |
| Ship | [`/retro`](lessons/retro.md) | `/retro` | 835 | 2.0.0 |
| Ship | [`/ship`](lessons/ship.md) | `/ship` | 557 | 1.0.0 |
| Safety | [`/careful`](lessons/careful.md) | `/careful` | 58 | 0.1.0 |
| Safety | [`/freeze`](lessons/freeze.md) | `/freeze` | 81 | 0.1.0 |
| Safety | [`/guard`](lessons/guard.md) | `/guard` | 81 | 0.1.0 |
| Safety | [`/unfreeze`](lessons/unfreeze.md) | `/unfreeze` | 39 | 0.1.0 |
| Meta | [`/gstack-upgrade`](lessons/gstack-upgrade.md) | `/gstack-upgrade` | 231 | 1.1.0 |
| Other | [`/gstack`](lessons/gstack.md) | `/gstack` | 257 | 1.1.0 |
| Other | [`/autoplan`](lessons/autoplan.md) | `/autoplan` | 632 | 1.0.0 |
| Other | [`/benchmark`](lessons/benchmark.md) | `/benchmark` | 235 | 1.0.0 |
| Other | [`/canary`](lessons/canary.md) | `/canary` | 222 | 1.0.0 |
| Other | [`/codex`](lessons/codex.md) | `/codex` | 358 | 1.0.0 |
| Other | [`/cso`](lessons/cso.md) | `/cso` | 622 | 2.0.0 |
| Other | [`/land-and-deploy`](lessons/land-and-deploy.md) | `/land-and-deploy` | 577 | 1.0.0 |
| Other | [`/setup-deploy`](lessons/setup-deploy.md) | `/setup-deploy` | 222 | 1.0.0 |

## The Sprint Flow

```
THINK:  /office-hours → /plan-ceo-review → /plan-eng-review
        /plan-design-review → /design-consultation
BUILD:  [you describe what you want, Claude writes code]
REVIEW: /review → /investigate → /design-review
TEST:   /qa → /qa-only → /browse
SHIP:   /ship → /document-release → /retro
SAFETY: /careful → /freeze → /guard → /unfreeze
```

## Lessons by Phase

### Think

- [`/design-consultation`](lessons/design-consultation.md) — Design consultation: understands your product, researches the landscape, propose
- [`/office-hours`](lessons/office-hours.md) — YC Office Hours — two modes. Startup mode: six forcing questions that expose
- [`/plan-ceo-review`](lessons/plan-ceo-review.md) — CEO/founder-mode plan review. Rethink the problem, find the 10-star product,
- [`/plan-design-review`](lessons/plan-design-review.md) — Designer's eye plan review — interactive, like CEO and Eng review.
- [`/plan-eng-review`](lessons/plan-eng-review.md) — Eng manager-mode plan review. Lock in the execution plan — architecture,

### Review

- [`/design-review`](lessons/design-review.md) — Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problem
- [`/investigate`](lessons/investigate.md) — Systematic debugging with root cause investigation. Four phases: investigate,
- [`/review`](lessons/review.md) — Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM

### Test

- [`/browse`](lessons/browse.md) — Fast headless browser for QA testing and site dogfooding. Navigate any URL, inte
- [`/qa`](lessons/qa.md) — Systematically QA test a web application and fix bugs found. Runs QA testing,
- [`/qa-only`](lessons/qa-only.md) — Report-only QA testing. Systematically tests a web application and produces a
- [`/setup-browser-cookies`](lessons/setup-browser-cookies.md) — Import cookies from your real Chromium browser into the headless browse session.

### Ship

- [`/document-release`](lessons/document-release.md) — Post-ship documentation update. Reads all project docs, cross-references the
- [`/retro`](lessons/retro.md) — Weekly engineering retrospective. Analyzes commit history, work patterns,
- [`/ship`](lessons/ship.md) — Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION,

### Safety

- [`/careful`](lessons/careful.md) — Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,
- [`/freeze`](lessons/freeze.md) — Restrict file edits to a specific directory for the session. Blocks Edit and
- [`/guard`](lessons/guard.md) — Full safety mode: destructive command warnings + directory-scoped edits.
- [`/unfreeze`](lessons/unfreeze.md) — Clear the freeze boundary set by /freeze, allowing edits to all directories

### Meta

- [`/gstack-upgrade`](lessons/gstack-upgrade.md) — Upgrade gstack to the latest version. Detects global vs vendored install,

### Other

- [`/gstack`](lessons/gstack.md) — Fast headless browser for QA testing and site dogfooding. Navigate pages, intera
- [`/autoplan`](lessons/autoplan.md) — Auto-review pipeline — reads the full CEO, design, and eng review skills from di
- [`/benchmark`](lessons/benchmark.md) — Performance regression detection using the browse daemon. Establishes
- [`/canary`](lessons/canary.md) — Post-deploy canary monitoring. Watches the live app for console errors,
- [`/codex`](lessons/codex.md) — OpenAI Codex CLI wrapper — three modes. Code review: independent diff review via
- [`/cso`](lessons/cso.md) — Chief Security Officer mode. Infrastructure-first security audit: secrets archae
- [`/land-and-deploy`](lessons/land-and-deploy.md) — Land and deploy workflow. Merges the PR, waits for CI and deploy,
- [`/setup-deploy`](lessons/setup-deploy.md) — Configure deployment settings for /land-and-deploy. Detects your deploy
