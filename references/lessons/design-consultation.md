# Lesson: `/design-consultation`

> Sprint phase: **Think** | Template: 370 lines | Version: 1.0.0
> Source: `garrytan/gstack/design-consultation/SKILL.md.tmpl`

## What Is This?

Design consultation: understands your product, researches the landscape, proposes a
complete design system (aesthetic, typography, color, layout, spacing, motion), and
generates font+color preview pages. Creates DESIGN.md as your project's design source
of truth. For existing sites, use /plan-design-review to infer the system instead.
design system or DESIGN.md.

## When Do You Use It?

- Use when asked to "design system", "brand guidelines", or "create DESIGN.md".
- Proactively suggest when starting a new project's UI with no existing

## What Do You Say to Claude?

Type `/design-consultation` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "design system"
- "brand guidelines"
- "create DESIGN.md"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"You already have a design system. Want to **update** it, **start fresh**, or **cancel**?"*
- *"Want me to research what top products in your space are doing for design, or should I work from my design knowledge?"*
- *"From what I can see, this is [X] for [Y] in the [Z] space. Sound right? And would you like me to research what's out there in this space, or should I work from what I know?"*
- *"Heads up: brutalist aesthetics usually pair with minimal motion. Your combo is unusual — which is fine if intentional. Want me to suggest motion that fits, or keep it?"*
- *"Bold palette with minimal decoration can work, but the colors will carry a lot of weight. Want me to suggest decoration that supports the palette?"*
- *"Editorial layouts are gorgeous but can fight data density. Want me to show how a hybrid approach keeps both?"*

## What Do You Get?

Structured output for the **Think** phase of your sprint.

## The Workflow

**Step 1: /design-consultation: Your Design System, Built Together**
> You are a senior product designer with strong opinions about typography, color, and visual systems. You don't present menus — you listen, think, research, and propose. You're opinionated but not dogma...

**Step 2: Phase 0: Pre-checks**
> **Check for existing DESIGN.md:**

**Step 3: Phase 1: Product Context**
> Ask the user a single question that covers everything you need to know. Pre-fill what you can infer from the codebase.

**Step 4: Phase 2: Research (only if user said yes)**
> If the user wants competitive research:

**Step 5: Phase 3: The Complete Proposal**
> This is the soul of the skill. Propose EVERYTHING as one coherent package.

**Step 6: Phase 4: Drill-downs (only if user requests adjustments)**
> When the user wants to change a specific section, go deep on that section:

**Step 7: Phase 5: Font & Color Preview Page (default ON)**
> Generate a polished HTML preview page and open it in the user's browser. This page is the first visual artifact the skill produces — it should look beautiful.

**Step 8: Phase 6: Write DESIGN.md & Confirm**
> Write `DESIGN.md` to the repo root with this structure:

**Step 9: Design System — [Project Name]**

**Step 10: Product Context**

**Step 11: Aesthetic Direction**

**Step 12: Typography**

**Step 13: Color**

**Step 14: Spacing**

**Step 15: Layout**

**Step 16: Motion**

**Step 17: Decisions Log**
> **Update CLAUDE.md** (or create it if it doesn't exist) — append this section:

**Step 18: Design System**
> Always read DESIGN.md before making any visual or UI decisions.

**Step 19: Important Rules**
> 1. **Propose, don't present menus.** You are a consultant, not a form. Make opinionated recommendations based on the product context, then let the user adjust.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: THINK phase
```

## What Comes Next?

- After thinking, plan: `/plan-ceo-review` → `/plan-eng-review`
- Then build, review, test, ship.
