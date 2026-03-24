# Lesson: `/qa`

> Sprint phase: **Test** | Template: 318 lines | Version: 2.0.0
> Source: `garrytan/gstack/qa/SKILL.md.tmpl`

## What Is This?

Systematically QA test a web application and fix bugs found. Runs QA testing,
then iteratively fixes bugs in source code, committing each fix atomically and
re-verifying. Use when asked to "qa", "QA", "test this site", "find bugs",
"test and fix", or "fix what's broken".
or asks "does this work?". Three tiers: Quick (critical/high only),
Standard (+ medium), Exhaustive (+ cosmetic). Produces before/after health scores,
fix evidence, and a ship-readiness summary. For report-only mode, use /qa-only.

## When Do You Use It?

- re-verifying. Use when asked to "qa", "QA", "test this site", "find bugs",
- Proactively suggest when the user says a feature is ready for testing

## What Do You Say to Claude?

Type `/qa` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "test this site"
- "find bugs"
- "test and fix"
- "fix what's broken"
- "does this work?"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Output Structure
- Phase 10: Report
- File: `~/.gstack/projects/{slug}/{user}-{branch}-test-outcome-{datetime}.md`

## The Workflow

**Step 1: /qa: Test → Fix → Verify**
> You are a QA engineer AND a bug-fix engineer. Test web applications like a real user — click everything, fill every form, check every state. When you find bugs, fix them in source code with atomic com...

**Step 2: Setup**
> **Parse the user's request for these parameters:**

**Step 3: Test Plan Context**
> Before falling back to git diff heuristics, check for richer test plan sources:

**Step 4: Phases 1-6: QA Baseline**
> {{QA_METHODOLOGY}}

**Step 5: Output Structure**
> .gstack/qa-reports/

**Step 6: Phase 7: Triage**
> Sort all discovered issues by severity, then decide which to fix based on the selected tier:

**Step 7: Phase 8: Fix Loop**
> For each fixable issue, in severity order:

**Step 8: Grep for error messages, component names, route definitions**

**Step 9: Glob for file patterns matching the affected page**

**Step 10: Phase 9: Final QA**
> After all fixes are applied:

**Step 11: Phase 10: Report**
> Write the report to both local and project-scoped locations:

**Step 12: Phase 11: TODOS.md Update**
> If the repo has a `TODOS.md`:

**Step 13: Additional Rules (qa-specific)**
> 11. **Clean working tree required.** If dirty, use AskUserQuestion to offer commit/stash/abort before proceeding.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: TEST phase
```

## What Comes Next?

- After testing, ship: `/ship`
- If bugs found, fix and re-test.
