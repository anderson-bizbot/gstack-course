# Lesson: `/review`

> Sprint phase: **Review** | Template: 285 lines | Version: 1.0.0
> Source: `garrytan/gstack/review/SKILL.md.tmpl`

## What Is This?

Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM trust
boundary violations, conditional side effects, and other structural issues. Use when
asked to "review this PR", "code review", "pre-landing review", or "check my diff".

## When Do You Use It?

- boundary violations, conditional side effects, and other structural issues. Use when
- Proactively suggest when the user is about to merge or land code changes.

## What Do You Say to Claude?

Type `/review` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "review this PR"
- "code review"
- "pre-landing review"
- "check my diff"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Step 5.8: Persist Eng Review result

## The Workflow

**Step 1: Pre-Landing PR Review**
> You are running the `/review` workflow. Analyze the current branch's diff against the base branch for structural issues that tests don't catch.

**Step 2: Step 1: Check branch**
> 1. Run `git branch --show-current` to get the current branch.

**Step 3: Step 1.5: Scope Drift Detection**
> Before reviewing code quality, check: **did they build what was requested — nothing more, nothing less?**

**Step 4: Step 2: Read the checklist**
> Read `.claude/skills/review/checklist.md`.

**Step 5: Step 2.5: Check for Greptile review comments**
> Read `.claude/skills/review/greptile-triage.md` and follow the fetch, filter, classify, and **escalation detection** steps.

**Step 6: Step 3: Get the diff**
> Fetch the latest base branch to avoid false positives from stale local state:

**Step 7: Step 4: Two-pass review**
> Apply the checklist against the diff in two passes:

**Step 8: Step 4.5: Design Review (conditional)**
> {{DESIGN_REVIEW_LITE}}

**Step 9: Step 4.75: Test Coverage Diagram**
> {{TEST_COVERAGE_AUDIT_REVIEW}}

**Step 10: Step 5: Fix-First Review**
> **Every finding gets action — not just critical ones.**

**Step 11: Step 5.5: TODOS cross-reference**
> Read `TODOS.md` in the repository root (if it exists). Cross-reference the PR against open TODOs:

**Step 12: Step 5.6: Documentation staleness check**
> Cross-reference the diff against documentation files. For each `.md` file in the repo root (README.md, ARCHITECTURE.md, CONTRIBUTING.md, CLAUDE.md, etc.):

**Step 13: Step 5.8: Persist Eng Review result**
> After all review passes complete, persist the final `/review` outcome so `/ship` can

**Step 14: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: REVIEW phase
```

## What Comes Next?

- After review, test: `/qa` or `/qa-only`
- Then ship: `/ship`
