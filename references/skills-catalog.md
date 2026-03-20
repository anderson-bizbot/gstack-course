# gstack Skills Catalog

> Auto-generated from [garrytan/gstack](https://github.com/garrytan/gstack)
> 21 skills | Generated: 2026-03-20 22:52 UTC

## Quick Reference

| Phase | Skill | Description | Size |
|-------|-------|-------------|------|
| Think | `/gstack` | Fast headless browser for QA testing and site dogfooding. Navigate any URL, inte | 26KB |
| Think | `/design-consultation` | Design consultation: understands your product, researches the landscape, propose | 30KB |
| Think | `/office-hours` | YC Office Hours — two modes. Startup mode: six forcing questions that expose | 42KB |
| Think | `/plan-ceo-review` | CEO/founder-mode plan review. Rethink the problem, find the 10-star product, | 71KB |
| Think | `/plan-design-review` | Designer's eye plan review — interactive, like CEO and Eng review. | 33KB |
| Think | `/plan-eng-review` | Eng manager-mode plan review. Lock in the execution plan — architecture, | 35KB |
| Review | `/design-review` | Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problem | 43KB |
| Review | `/investigate` | Systematic debugging with root cause investigation. Four phases: investigate, | 18KB |
| Review | `/review` | Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM | 24KB |
| Test | `/browse` | Fast headless browser for QA testing and site dogfooding. Navigate any URL, inte | 21KB |
| Test | `/qa` | Systematically QA test a web application and fix bugs found. Runs QA testing, | 41KB |
| Test | `/qa-only` | Report-only QA testing. Systematically tests a web application and produces a | 26KB |
| Test | `/setup-browser-cookies` | Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the | 14KB |
| Ship | `/document-release` | Post-ship documentation update. Reads all project docs, cross-references the | 25KB |
| Ship | `/retro` | Weekly engineering retrospective. Analyzes commit history, work patterns, | 33KB |
| Ship | `/ship` | Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, | 54KB |
| Safety | `/careful` | Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE, | 3KB |
| Safety | `/freeze` | Restrict file edits to a specific directory for the session. Blocks Edit and | 3KB |
| Safety | `/guard` | Full safety mode: destructive command warnings + directory-scoped edits. | 3KB |
| Safety | `/unfreeze` | Clear the freeze boundary set by /freeze, allowing edits to all directories | 1KB |
| Meta | `/upgrade` | Upgrade gstack to the latest version. Detects global vs vendored install, | 8KB |

---

## Phase: Think

### `/gstack` (gstack)

**Size:** 26,233 bytes

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.
~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
user flow, or file a bug with evidence.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/design-consultation` (gstack-design-consultation)

**Size:** 30,606 bytes

Design consultation: understands your product, researches the landscape, proposes a
complete design system (aesthetic, typography, color, layout, spacing, motion), and
generates font+color preview pages. Creates DESIGN.md as your project's design source
of truth. For existing sites, use /plan-design-review to infer the system instead.
Use when asked to "design system", "brand guidelines", or "create DESIGN.md".

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/office-hours` (gstack-office-hours)

**Size:** 42,796 bytes

YC Office Hours — two modes. Startup mode: six forcing questions that expose
demand reality, status quo, desperate specificity, narrowest wedge, observation,
and future-fit. Builder mode: design thinking brainstorming for side projects,
hackathons, learning, and open source. Saves a design doc.
Use when asked to "brainstorm this", "I have an idea", "help me think through

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/plan-ceo-review` (gstack-plan-ceo-review)

**Size:** 72,270 bytes

CEO/founder-mode plan review. Rethink the problem, find the 10-star product,
challenge premises, expand scope when it creates a better product. Four modes:
SCOPE EXPANSION (dream big), SELECTIVE EXPANSION (hold scope + cherry-pick
expansions), HOLD SCOPE (maximum rigor), SCOPE REDUCTION (strip to essentials).
Use when asked to "think bigger", "expand scope", "strategy review", "rethink this",

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/plan-design-review` (gstack-plan-design-review)

**Size:** 34,208 bytes

Designer's eye plan review — interactive, like CEO and Eng review.
Rates each design dimension 0-10, explains what would make it a 10,
then fixes the plan to get there. Works in plan mode. For live site
visual audits, use /design-review. Use when asked to "review the design plan"
or "design critique".

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/plan-eng-review` (gstack-plan-eng-review)

**Size:** 36,320 bytes

Eng manager-mode plan review. Lock in the execution plan — architecture,
data flow, diagrams, edge cases, test coverage, performance. Walks through
issues interactively with opinionated recommendations. Use when asked to
"review the architecture", "engineering review", or "lock in the plan".
Proactively suggest when the user has a plan or design doc and is about to

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

## Phase: Review

### `/design-review` (gstack-design-review)

**Size:** 44,283 bytes

Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems,
AI slop patterns, and slow interactions — then fixes them. Iteratively fixes issues
in source code, committing each fix atomically and re-verifying with before/after
screenshots. For plan-mode design review (before implementation), use /plan-design-review.
Use when asked to "audit the design", "visual QA", "check if it looks good", or "design polish".

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/investigate` (gstack-investigate)

**Size:** 18,747 bytes

Systematic debugging with root cause investigation. Four phases: investigate,
analyze, hypothesize, implement. Iron Law: no fixes without root cause.
Use when asked to "debug this", "fix this bug", "why is this broken",
"investigate this error", or "root cause analysis".
Proactively suggest when the user reports errors, unexpected behavior, or

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/review` (gstack-review)

**Size:** 24,426 bytes

Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM trust
boundary violations, conditional side effects, and other structural issues. Use when
asked to "review this PR", "code review", "pre-landing review", or "check my diff".
Proactively suggest when the user is about to merge or land code changes.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

## Phase: Test

### `/browse` (gstack-browse)

**Size:** 21,794 bytes

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.
~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
user flow, or file a bug with evidence. Use when asked to "open in browser", "test the

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/qa` (gstack-qa)

**Size:** 41,814 bytes

Systematically QA test a web application and fix bugs found. Runs QA testing,
then iteratively fixes bugs in source code, committing each fix atomically and
re-verifying. Use when asked to "qa", "QA", "test this site", "find bugs",
"test and fix", or "fix what's broken".
Proactively suggest when the user says a feature is ready for testing

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/qa-only` (gstack-qa-only)

**Size:** 27,114 bytes

Report-only QA testing. Systematically tests a web application and produces a
structured report with health score, screenshots, and repro steps — but never
fixes anything. Use when asked to "just report bugs", "qa report only", or
"test but don't fix". For the full test-fix-verify loop, use /qa instead.
Proactively suggest when the user wants a bug report without any code changes.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/setup-browser-cookies` (gstack-setup-browser-cookies)

**Size:** 14,217 bytes

Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the
headless browse session. Opens an interactive picker UI where you select which
cookie domains to import. Use before QA testing authenticated pages. Use when asked
to "import cookies", "login to the site", or "authenticate the browser".

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

## Phase: Ship

### `/document-release` (gstack-document-release)

**Size:** 25,976 bytes

Post-ship documentation update. Reads all project docs, cross-references the
diff, updates README/ARCHITECTURE/CONTRIBUTING/CLAUDE.md to match what shipped,
polishes CHANGELOG voice, cleans up TODOS, and optionally bumps VERSION. Use when
asked to "update the docs", "sync documentation", or "post-ship docs".
Proactively suggest after a PR is merged or code is shipped.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/retro` (gstack-retro)

**Size:** 33,922 bytes

Weekly engineering retrospective. Analyzes commit history, work patterns,
and code quality metrics with persistent history and trend tracking.
Team-aware: breaks down per-person contributions with praise and growth areas.
Use when asked to "weekly retro", "what did we ship", or "engineering retrospective".
Proactively suggest at the end of a work week or sprint.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

### `/ship` (gstack-ship)

**Size:** 54,822 bytes

Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "create a PR", or "merge and push".
Proactively suggest when the user says code is ready or asks about deploying.

**Key sections:** Preamble (run first), AskUserQuestion Format, Completeness Principle — Boil the Lake, Contributor Mode, {Title}, Steps to reproduce

---

## Phase: Safety

### `/careful` (gstack-careful)

**Size:** 2,567 bytes

Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,
force-push, git reset --hard, kubectl delete, and similar destructive operations.
User can override each warning. Use when touching prod, debugging live systems,
or working in a shared environment. Use when asked to "be careful", "safety mode",
"prod mode", or "careful mode".

**Key sections:** /careful — Destructive Command Guardrails, What's protected, Safe exceptions, How it works

---

### `/freeze` (gstack-freeze)

**Size:** 2,955 bytes

Restrict file edits to a specific directory for the session. Blocks Edit and
Write outside the allowed path. Use when debugging to prevent accidentally
"fixing" unrelated code, or when you want to scope changes to one module.
Use when asked to "freeze", "restrict edits", "only edit this folder",
or "lock down edits".

**Key sections:** /freeze — Restrict Edits to a Directory, Setup, How it works, Notes

---

### `/guard` (gstack-guard)

**Size:** 3,015 bytes

Full safety mode: destructive command warnings + directory-scoped edits.
Combines /careful (warns before rm -rf, DROP TABLE, force-push, etc.) with
/freeze (blocks edits outside a specified directory). Use for maximum safety
when touching prod or debugging live systems. Use when asked to "guard mode",
"full safety", "lock it down", or "maximum safety".

**Key sections:** /guard — Full Safety Mode, Setup, What's protected

---

### `/unfreeze` (gstack-unfreeze)

**Size:** 1,307 bytes

Clear the freeze boundary set by /freeze, allowing edits to all directories
again. Use when you want to widen edit scope without ending the session.
Use when asked to "unfreeze", "unlock edits", "remove freeze", or
"allow all edits".

**Key sections:** /unfreeze — Clear Freeze Boundary, Clear the boundary

---

## Phase: Meta

### `/upgrade` (gstack-upgrade)

**Size:** 7,959 bytes

Upgrade gstack to the latest version. Detects global vs vendored install,
runs the upgrade, and shows what's new. Use when asked to "upgrade gstack",
"update gstack", or "get latest version".

**Key sections:** /gstack-upgrade, Inline upgrade flow, Standalone usage

---
