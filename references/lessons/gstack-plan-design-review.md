# Lesson: `/plan-design-review`

> Sprint phase: **Think** | Size: 34,208 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-plan-design-review/SKILL.md`

## What Is This?

Designer's eye plan review — interactive, like CEO and Eng review.
Rates each design dimension 0-10, explains what would make it a 10,
then fixes the plan to get there. Works in plan mode. For live site

## When Do You Use It?

- visual audits, use /design-review. Use when asked to "review the design plan"
- Proactively suggest when the user has a plan with UI/UX components that

## What Do You Say to Claude?

Type `/plan-design-review` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "review the design plan"
- "design critique"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"what should the user see first, second, third?"*
- *"If I can only show 3 things, which 3 matter most?"*
- *"Who is this for? What did they try before this?"*
- *"I've rated this plan {N}/10 on design completeness. The biggest gaps are {X, Y, Z}. Want me to review all 7 dimensions, or focus on specific areas?"*

## What Do You Get?

- **Raw output**
- **Required Outputs**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Step 0: Detect base branch**
   Determine which branch this PR targets. Use the result as "the base branch" in all subsequent steps.

5. **/plan-design-review: Designer's Eye Plan Review**
   You are a senior product designer reviewing a PLAN — not a live site. Your job is

6. **Design Philosophy**
   You are not here to rubber-stamp this plan's UI. You are here to ensure that when

7. **Design Principles**
   1. Empty states are features. "No items found." is not a design. Every empty state needs warmth, a primary action, and context.

8. **Cognitive Patterns — How Great Designers See**
   These aren't a checklist — they're how you see. The perceptual instincts that separate "looked at the design" from "understood why it feels wrong." Le

9. **Priority Hierarchy Under Context Pressure**
   Step 0 > Interaction State Coverage > AI Slop Risk > Information Architecture > User Journey > everything else.

10. **PRE-REVIEW SYSTEM AUDIT (before Step 0)**
   Before reviewing the plan, gather context:

11. **Step 0: Design Scope Assessment**

12. **The 0-10 Rating Method**
   For each design section, rate the plan 0-10 on that dimension. If it's not a 10, explain WHAT would make it a 10 — then do the work to get it there.

13. **Review Sections (7 passes, after scope is agreed)**

14. **CRITICAL RULE — How to ask questions**
   Follow the AskUserQuestion format from the Preamble above. Additional rules for plan design reviews:

15. **Required Outputs**

16. **Review Log**
   After producing the Completion Summary above, persist the review result.

17. **Review Readiness Dashboard**
   After completing the review, read the review log and config to display the dashboard.

18. **Next Steps — Review Chaining**
   After displaying the Review Readiness Dashboard, recommend the next review(s) based on what this design review discovered. Read the dashboard output t

19. **Formatting Rules**
   * NUMBER issues (1, 2, 3...) and LETTERS for options (A, B, C...).

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `/plan-ceo-review`
- `/plan-eng-review`
- `/plan-design-review`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
