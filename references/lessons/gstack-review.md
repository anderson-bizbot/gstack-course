# Lesson: `/review`

> Sprint phase: **Review** | Size: 24,426 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-review/SKILL.md`

## What Is This?

Pre-landing PR review. Analyzes diff against the base branch for SQL safety, LLM trust
boundary violations, conditional side effects, and other structural issues. Use when
asked to "review this PR", "code review", "pre-landing review", or "check my diff".

## When Do You Use It?

- boundary violations, conditional side effects, and other structural issues. Use when
- Proactively suggest when the user is about to merge or land code changes.

## What Do You Say to Claude?

Type `/review` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "review this PR"
- "code review"
- "pre-landing review"
- "check my diff"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

- **Raw output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Step 0: Detect base branch**
   Determine which branch this PR targets. Use the result as "the base branch" in all subsequent steps.

5. **Pre-Landing PR Review**
   You are running the `/review` workflow. Analyze the current branch's diff against the base branch for structural issues that tests don't catch.

6. **Step 1: Check branch**
   1. Run `git branch --show-current` to get the current branch.

7. **Step 1.5: Scope Drift Detection**
   Before reviewing code quality, check: **did they build what was requested — nothing more, nothing less?**

8. **Step 2: Read the checklist**
   Read `.agents/skills/gstack/review/checklist.md`.

9. **Step 2.5: Check for Greptile review comments**
   Read `.agents/skills/gstack/review/greptile-triage.md` and follow the fetch, filter, classify, and **escalation detection** steps.

10. **Step 3: Get the diff**
   Fetch the latest base branch to avoid false positives from stale local state:

11. **Step 4: Two-pass review**
   Apply the checklist against the diff in two passes:

12. **Step 4.5: Design Review (conditional)**

13. **Design Review (conditional, diff-scoped)**
   Check if the diff touches frontend files using `gstack-diff-scope`:

14. **Step 5: Fix-First Review**
   **Every finding gets action — not just critical ones.**

15. **Step 5.5: TODOS cross-reference**
   Read `TODOS.md` in the repository root (if it exists). Cross-reference the PR against open TODOs:

16. **Step 5.6: Documentation staleness check**
   Cross-reference the diff against documentation files. For each `.md` file in the repo root (README.md, ARCHITECTURE.md, CONTRIBUTING.md, CLAUDE.md, et

17. **Important Rules**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → >>>/review<<< → /qa → /ship → /retro
```

## What Comes Next?

- `/qa`
- `/ship`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
