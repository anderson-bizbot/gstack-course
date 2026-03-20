# Lesson: `/design-consultation`

> Sprint phase: **Think** | Size: 30,606 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-design-consultation/SKILL.md`

## What Is This?

Design consultation: understands your product, researches the landscape, proposes a
complete design system (aesthetic, typography, color, layout, spacing, motion), and
generates font+color preview pages. Creates DESIGN.md as your project's design source

## When Do You Use It?

- Use when asked to "design system", "brand guidelines", or "create DESIGN.md".
- Proactively suggest when starting a new project's UI with no existing

## What Do You Say to Claude?

Type `/design-consultation` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "design system"
- "brand guidelines"
- "create DESIGN.md"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"You already have a design system. Want to **update** it, **start fresh**, or **cancel**?"*
- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*
- *"Want me to research what top products in your space are doing for design, or should I work from my design knowledge?"*
- *"From what I can see, this is [X] for [Y] in the [Z] space. Sound right? And would you like me to research what's out there in this space, or should I work from what I know?"*
- *"Heads up: brutalist aesthetics usually pair with minimal motion. Your combo is unusual — which is fine if intentional. Want me to suggest motion that fits, or keep it?"*
- *"Bold palette with minimal decoration can work, but the colors will carry a lot of weight. Want me to suggest decoration that supports the palette?"*

## What Do You Get?

- **Raw output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Phase 0: Pre-checks**
   **Check for existing DESIGN.md:**

5. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

6. **Phase 1: Product Context**
   Ask the user a single question that covers everything you need to know. Pre-fill what you can infer from the codebase.

7. **Phase 2: Research (only if user said yes)**
   If the user wants competitive research:

8. **Phase 3: The Complete Proposal**
   This is the soul of the skill. Propose EVERYTHING as one coherent package.

9. **Phase 4: Drill-downs (only if user requests adjustments)**
   When the user wants to change a specific section, go deep on that section:

10. **Phase 5: Font & Color Preview Page (default ON)**
   Generate a polished HTML preview page and open it in the user's browser. This page is the first visual artifact the skill produces — it should look be

11. **Phase 6: Write DESIGN.md & Confirm**
   Write `DESIGN.md` to the repo root with this structure:

12. **Design System — [Project Name]**

13. **Product Context**

14. **Aesthetic Direction**

15. **Typography**

16. **Color**

17. **Spacing**

18. **Layout**

19. **Motion**

20. **Decisions Log**
   **Update CLAUDE.md** (or create it if it doesn't exist) — append this section:

21. **Design System**
   Always read DESIGN.md before making any visual or UI decisions.

22. **Important Rules**
   1. **Propose, don't present menus.** You are a consultant, not a form. Make opinionated recommendations based on the product context, then let the use

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
