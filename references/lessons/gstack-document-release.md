# Lesson: `/document-release`

> Sprint phase: **Ship** | Size: 25,976 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-document-release/SKILL.md`

## What Is This?

Post-ship documentation update. Reads all project docs, cross-references the
diff, updates README/ARCHITECTURE/CONTRIBUTING/CLAUDE.md to match what shipped,
polishes CHANGELOG voice, cleans up TODOS, and optionally bumps VERSION. Use when

## When Do You Use It?

- polishes CHANGELOG voice, cleans up TODOS, and optionally bumps VERSION. Use when
- Proactively suggest after a PR is merged or code is shipped.

## What Do You Say to Claude?

Type `/document-release` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "update the docs"
- "sync documentation"
- "post-ship docs"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

- **Raw output**
- **Step 9: Commit & Output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Step 0: Detect base branch**
   Determine which branch this PR targets. Use the result as "the base branch" in all subsequent steps.

5. **Document Release: Post-Ship Documentation Update**
   You are running the `/document-release` workflow. This runs **after `/ship`** (code committed, PR

6. **Step 1: Pre-flight & Diff Analysis**
   1. Check the current branch. If on the base branch, **abort**: "You're on the base branch. Run from a feature branch."

7. **Step 2: Per-File Documentation Audit**
   Read each documentation file and cross-reference it against the diff. Use these generic heuristics

8. **Step 3: Apply Auto-Updates**
   Make all clear, factual updates directly using the Edit tool.

9. **Step 4: Ask About Risky/Questionable Changes**
   For each risky or questionable update identified in Step 2, use AskUserQuestion with:

10. **Step 5: CHANGELOG Voice Polish**
   **CRITICAL — NEVER CLOBBER CHANGELOG ENTRIES.**

11. **Step 6: Cross-Doc Consistency & Discoverability Check**
   After auditing each file individually, do a cross-doc consistency pass:

12. **Step 7: TODOS.md Cleanup**
   This is a second pass that complements `/ship`'s Step 5.5. Read `review/TODOS-format.md` (if

13. **Step 8: VERSION Bump Question**
   **CRITICAL — NEVER BUMP VERSION WITHOUT ASKING.**

14. **Step 9: Commit & Output**
   **Empty check first:** Run `git status` (never use `-uall`). If no documentation files were

15. **Important Rules**
   who hasn't seen the code.

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `/document-release`
- `/retro`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
