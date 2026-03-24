# Lesson: `/ship`

> Sprint phase: **Ship** | Template: 557 lines | Version: 1.0.0
> Source: `garrytan/gstack/ship/SKILL.md.tmpl`

## What Is This?

Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "create a PR", or "merge and push".

## When Do You Use It?

- Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "create a PR", or "merge and push".
- Proactively suggest when the user says code is ready or asks about deploying.

## What Do You Say to Claude?

Type `/ship` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "ship"
- "deploy"
- "push to main"
- "create a PR"
- "merge and push"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"GStack recommends maintaining a TODOS.md organized by skill/component, then priority (P0 at top through P4, then Completed at bottom). See TODOS-format.md for the full format. Would you like to create one?"*
- *"TODOS.md doesn't follow the recommended structure (skill/component groupings, P0-P4 priority, Completed section). Would you like to reorganize it?"*

## What Do You Get?

- Ship: Fully Automated Ship Workflow
- Eval Results

## The Workflow

**Step 1: Ship: Fully Automated Ship Workflow**
> You are running the `/ship` workflow. This is a **non-interactive, fully automated** workflow. Do NOT ask for confirmation at any step. The user said `/ship` which means DO IT. Run straight through an...

**Step 2: Step 1: Pre-flight**
> 1. Check the current branch. If on the base branch or the repo's default branch, **abort**: "You're on the base branch. Ship from a feature branch."

**Step 3: Step 1.5: Distribution Pipeline Check**
> If the diff introduces a new standalone artifact (CLI binary, library package, tool) — not a web

**Step 4: Step 2: Merge the base branch (BEFORE tests)**
> Fetch and merge the base branch into the feature branch so tests run against the merged state:

**Step 5: Step 2.5: Test Framework Bootstrap**
> {{TEST_BOOTSTRAP}}

**Step 6: Step 3: Run tests (on merged code)**
> **Do NOT run `RAILS_ENV=test bin/rails db:migrate`** — `bin/test-lane` already calls

**Step 7: Step 3.25: Eval Suites (conditional)**
> Evals are mandatory when prompt-related files change. Skip this step entirely if no prompt files are in the diff.

**Step 8: Step 3.4: Test Coverage Audit**
> {{TEST_COVERAGE_AUDIT_SHIP}}

**Step 9: Step 3.5: Pre-Landing Review**
> Review the diff for structural issues that tests don't catch.

**Step 10: Step 3.75: Address Greptile review comments (if PR exists)**
> Read `.claude/skills/review/greptile-triage.md` and follow the fetch, filter, classify, and **escalation detection** steps.

**Step 11: Step 4: Version bump (auto-decide)**
> 1. Read the current `VERSION` file (4-digit format: `MAJOR.MINOR.PATCH.MICRO`)

**Step 12: Step 5: CHANGELOG (auto-generate)**
> 1. Read `CHANGELOG.md` header to know the format.

**Step 13: Step 5.5: TODOS.md (auto-update)**
> Cross-reference the project's TODOS.md against the changes being shipped. Mark completed items automatically; prompt only if the file is missing or disorganized.

**Step 14: Step 6: Commit (bisectable chunks)**
> **Goal:** Create small, logical commits that work well with `git bisect` and help LLMs understand what changed.

**Step 15: Step 6.5: Verification Gate**
> **IRON LAW: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

**Step 16: Step 7: Push**
> Push to the remote with upstream tracking:

**Step 17: Step 8: Create PR**
> Create a pull request using `gh`:

**Step 18: Summary**
> <bullet points from CHANGELOG>

**Step 19: Test Coverage**
> <coverage diagram from Step 3.4, or "All new code paths have test coverage.">

**Step 20: Pre-Landing Review**
> <findings from Step 3.5 code review, or "No issues found.">

**Step 21: Design Review**
> <If design review ran: "Design Review (lite): N findings — M auto-fixed, K skipped. AI Slop: clean/N issues.">

**Step 22: Eval Results**
> <If evals ran: suite names, pass/fail counts, cost dashboard summary. If skipped: "No prompt-related files changed — evals skipped.">

**Step 23: Greptile Review**
> <If Greptile comments were found: bullet list with [FIXED] / [FALSE POSITIVE] / [ALREADY FIXED] tag + one-line summary per comment>

**Step 24: TODOS**
> <If items marked complete: bullet list of completed items with version>

**Step 25: Test plan**
> 🤖 Generated with [Claude Code](https://claude.com/claude-code)

**Step 26: Step 8.5: Auto-invoke /document-release**
> After the PR is created, automatically sync project documentation. Read the

**Step 27: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SHIP phase
```

## What Comes Next?

- After shipping, document: `/document-release`
- End of week: `/retro`
