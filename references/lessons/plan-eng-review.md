# Lesson: `/plan-eng-review`

> Sprint phase: **Think** | Template: 280 lines | Version: 1.0.0
> Source: `garrytan/gstack/plan-eng-review/SKILL.md.tmpl`

## What Is This?

Eng manager-mode plan review. Lock in the execution plan — architecture,
data flow, diagrams, edge cases, test coverage, performance. Walks through
issues interactively with opinionated recommendations. Use when asked to
"review the architecture", "engineering review", or "lock in the plan".
start coding — to catch architecture issues before implementation.

## When Do You Use It?

- issues interactively with opinionated recommendations. Use when asked to
- Proactively suggest when the user has a plan or design doc and is about to

## What Do You Say to Claude?

Type `/plan-eng-review` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "review the architecture"
- "engineering review"
- "lock in the plan"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"Is this solving a real problem or one we created?"*

## What Do You Get?

- Design Doc Check
- Required outputs

## The Workflow

**Step 1: Plan Review Mode**
> Review this plan thoroughly before making any code changes. For every issue or recommendation, explain the concrete tradeoffs, give me an opinionated recommendation, and ask for my input before assumi...

**Step 2: Priority hierarchy**
> If you are running low on context or the user asks you to compress: Step 0 > Test diagram > Opinionated recommendations > Everything else. Never skip Step 0 or the test diagram.

**Step 3: My engineering preferences (use these to guide your recommendations):**
> * DRY is important—flag repetition aggressively.

**Step 4: Cognitive Patterns — How Great Eng Managers Think**
> These are not additional checklist items. They are the instincts that experienced engineering leaders develop over years — the pattern recognition that separates "reviewed the code" from "caught the l...

**Step 5: Documentation and diagrams:**
> * I value ASCII art diagrams highly — for data flow, state machines, dependency graphs, processing pipelines, and decision trees. Use them liberally in plans and design docs.

**Step 6: BEFORE YOU START:**

**Step 7: Review Sections (after scope is agreed)**

**Step 8: CRITICAL RULE — How to ask questions**
> Follow the AskUserQuestion format from the Preamble above. Additional rules for plan reviews:

**Step 9: Required outputs**

**Step 10: Retrospective learning**
> Check the git log for this branch. If there are prior commits suggesting a previous review cycle (e.g., review-driven refactors, reverted changes), note what was changed and whether the current plan t...

**Step 11: Formatting rules**
> * NUMBER issues (1, 2, 3...) and LETTERS for options (A, B, C...).

**Step 12: Review Log**
> After producing the Completion Summary above, persist the review result.

**Step 13: Next Steps — Review Chaining**
> After displaying the Review Readiness Dashboard, check if additional reviews would be valuable. Read the dashboard output to see which reviews have already been run and whether they are stale.

**Step 14: Unresolved decisions**
> If the user does not respond to an AskUserQuestion or interrupts to move on, note which decisions were left unresolved. At the end of the review, list these as "Unresolved decisions that may bite you ...

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: THINK phase
```

## What Comes Next?

- After thinking, plan: `/plan-ceo-review` → `/plan-eng-review`
- Then build, review, test, ship.
