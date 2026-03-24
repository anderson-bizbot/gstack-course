# Lesson: `/document-release`

> Sprint phase: **Ship** | Template: 359 lines | Version: 1.0.0
> Source: `garrytan/gstack/document-release/SKILL.md.tmpl`

## What Is This?

Post-ship documentation update. Reads all project docs, cross-references the
diff, updates README/ARCHITECTURE/CONTRIBUTING/CLAUDE.md to match what shipped,
polishes CHANGELOG voice, cleans up TODOS, and optionally bumps VERSION. Use when
asked to "update the docs", "sync documentation", or "post-ship docs".

## When Do You Use It?

- polishes CHANGELOG voice, cleans up TODOS, and optionally bumps VERSION. Use when
- Proactively suggest after a PR is merged or code is shipped.

## What Do You Say to Claude?

Type `/document-release` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "update the docs"
- "sync documentation"
- "post-ship docs"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Document Release: Post-Ship Documentation Update
- Step 9: Commit & Output

## The Workflow

**Step 1: Document Release: Post-Ship Documentation Update**
> You are running the `/document-release` workflow. This runs **after `/ship`** (code committed, PR

**Step 2: Step 1: Pre-flight & Diff Analysis**
> 1. Check the current branch. If on the base branch, **abort**: "You're on the base branch. Run from a feature branch."

**Step 3: Step 2: Per-File Documentation Audit**
> Read each documentation file and cross-reference it against the diff. Use these generic heuristics

**Step 4: Step 3: Apply Auto-Updates**
> Make all clear, factual updates directly using the Edit tool.

**Step 5: Step 4: Ask About Risky/Questionable Changes**
> For each risky or questionable update identified in Step 2, use AskUserQuestion with:

**Step 6: Step 5: CHANGELOG Voice Polish**
> **CRITICAL — NEVER CLOBBER CHANGELOG ENTRIES.**

**Step 7: Step 6: Cross-Doc Consistency & Discoverability Check**
> After auditing each file individually, do a cross-doc consistency pass:

**Step 8: Step 7: TODOS.md Cleanup**
> This is a second pass that complements `/ship`'s Step 5.5. Read `review/TODOS-format.md` (if

**Step 9: Step 8: VERSION Bump Question**
> **CRITICAL — NEVER BUMP VERSION WITHOUT ASKING.**

**Step 10: Step 9: Commit & Output**
> **Empty check first:** Run `git status` (never use `-uall`). If no documentation files were

**Step 11: Important Rules**
> who hasn't seen the code.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SHIP phase
```

## What Comes Next?

- After shipping, document: `/document-release`
- End of week: `/retro`
