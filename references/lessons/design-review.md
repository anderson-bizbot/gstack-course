# Lesson: `/design-review`

> Sprint phase: **Review** | Template: 274 lines | Version: 2.0.0
> Source: `garrytan/gstack/design-review/SKILL.md.tmpl`

## What Is This?

Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems,
AI slop patterns, and slow interactions — then fixes them. Iteratively fixes issues
in source code, committing each fix atomically and re-verifying with before/after
screenshots. For plan-mode design review (before implementation), use /plan-design-review.
wants to polish the look of a live site.

## When Do You Use It?

- Use when asked to "audit the design", "visual QA", "check if it looks good", or "design polish".
- Proactively suggest when the user mentions visual inconsistencies or

## What Do You Say to Claude?

Type `/design-review` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "audit the design"
- "visual QA"
- "check if it looks good"
- "design polish"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Output Structure
- Phase 10: Report
- File: `~/.gstack/projects/{slug}/{user}-{branch}-design-audit-{datetime}.md`

## The Workflow

**Step 1: /design-review: Design Audit → Fix → Verify**
> You are a senior product designer AND a frontend engineer. Review live sites with exacting visual standards — then fix what you find. You have strong opinions about typography, spacing, and visual hie...

**Step 2: Setup**
> **Parse the user's request for these parameters:**

**Step 3: Phases 1-6: Design Audit Baseline**
> {{DESIGN_METHODOLOGY}}

**Step 4: Output Structure**
> .gstack/design-reports/

**Step 5: Phase 7: Triage**
> Sort all discovered findings by impact, then decide which to fix:

**Step 6: Phase 8: Fix Loop**
> For each fixable finding, in impact order:

**Step 7: Search for CSS classes, component names, style files**

**Step 8: Glob for file patterns matching the affected page**

**Step 9: Phase 9: Final Design Audit**
> After all fixes are applied:

**Step 10: Phase 10: Report**
> Write the report to both local and project-scoped locations:

**Step 11: Phase 11: TODOS.md Update**
> If the repo has a `TODOS.md`:

**Step 12: Additional Rules (design-review specific)**
> 11. **Clean working tree required.** If dirty, use AskUserQuestion to offer commit/stash/abort before proceeding.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: REVIEW phase
```

## What Comes Next?

- After review, test: `/qa` or `/qa-only`
- Then ship: `/ship`
