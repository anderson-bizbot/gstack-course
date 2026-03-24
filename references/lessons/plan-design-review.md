# Lesson: `/plan-design-review`

> Sprint phase: **Think** | Template: 320 lines | Version: 2.0.0
> Source: `garrytan/gstack/plan-design-review/SKILL.md.tmpl`

## What Is This?

Designer's eye plan review — interactive, like CEO and Eng review.
Rates each design dimension 0-10, explains what would make it a 10,
then fixes the plan to get there. Works in plan mode. For live site
visual audits, use /design-review. Use when asked to "review the design plan"
or "design critique".
should be reviewed before implementation.

## When Do You Use It?

- visual audits, use /design-review. Use when asked to "review the design plan"
- Proactively suggest when the user has a plan with UI/UX components that

## What Do You Say to Claude?

Type `/plan-design-review` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "review the design plan"
- "design critique"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"If I can only show 3 things, which 3 matter most?"*
- *"Who is this for? What did they try before this?"*
- *"I've rated this plan {N}/10 on design completeness. The biggest gaps are {X, Y, Z}. Want me to review all 7 dimensions, or focus on specific areas?"*

## What Do You Get?

- Required Outputs

## The Workflow

**Step 1: /plan-design-review: Designer's Eye Plan Review**
> You are a senior product designer reviewing a PLAN — not a live site. Your job is

**Step 2: Design Philosophy**
> You are not here to rubber-stamp this plan's UI. You are here to ensure that when

**Step 3: Design Principles**
> 1. Empty states are features. "No items found." is not a design. Every empty state needs warmth, a primary action, and context.

**Step 4: Cognitive Patterns — How Great Designers See**
> These aren't a checklist — they're how you see. The perceptual instincts that separate "looked at the design" from "understood why it feels wrong." Let them run automatically as you review.

**Step 5: Priority Hierarchy Under Context Pressure**
> Step 0 > Interaction State Coverage > AI Slop Risk > Information Architecture > User Journey > everything else.

**Step 6: PRE-REVIEW SYSTEM AUDIT (before Step 0)**
> Before reviewing the plan, gather context:

**Step 7: Step 0: Design Scope Assessment**

**Step 8: The 0-10 Rating Method**
> For each design section, rate the plan 0-10 on that dimension. If it's not a 10, explain WHAT would make it a 10 — then do the work to get it there.

**Step 9: Review Sections (7 passes, after scope is agreed)**

**Step 10: CRITICAL RULE — How to ask questions**
> Follow the AskUserQuestion format from the Preamble above. Additional rules for plan design reviews:

**Step 11: Required Outputs**

**Step 12: Review Log**
> After producing the Completion Summary above, persist the review result.

**Step 13: Next Steps — Review Chaining**
> After displaying the Review Readiness Dashboard, recommend the next review(s) based on what this design review discovered. Read the dashboard output to see which reviews have already been run and whet...

**Step 14: Formatting Rules**
> * NUMBER issues (1, 2, 3...) and LETTERS for options (A, B, C...).

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: THINK phase
```

## What Comes Next?

- After thinking, plan: `/plan-ceo-review` → `/plan-eng-review`
- Then build, review, test, ship.
