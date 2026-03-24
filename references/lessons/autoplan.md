# Lesson: `/autoplan`

> Sprint phase: **Other** | Template: 632 lines | Version: 1.0.0
> Source: `garrytan/gstack/autoplan/SKILL.md.tmpl`

## What Is This?

Auto-review pipeline — reads the full CEO, design, and eng review skills from disk
and runs them sequentially with auto-decisions using 6 decision principles. Surfaces
taste decisions (close approaches, borderline scope, codex disagreements) at a final
approval gate. One command, fully reviewed plan out.
automatically", or "make the decisions for me".
gauntlet without answering 15-30 intermediate questions.

## When Do You Use It?

- Use when asked to "auto review", "autoplan", "run all reviews", "review this plan
- Proactively suggest when the user has a plan file and wants to run the full review

## What Do You Say to Claude?

Type `/autoplan` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "auto review"
- "autoplan"
- "run all reviews"
- "review this plan
automatically"
- "make the decisions for me"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Other** phase of your sprint.

## The Workflow

**Step 1: /autoplan — Auto-Review Pipeline**
> One command. Rough plan in, fully reviewed plan out.

**Step 2: The 6 Decision Principles**
> These rules auto-answer every intermediate question:

**Step 3: Decision Classification**
> Every auto-decision is classified:

**Step 4: Sequential Execution — MANDATORY**
> Phases MUST execute in strict order: CEO → Design → Eng.

**Step 5: What "Auto-Decide" Means**
> Auto-decide replaces the USER'S judgment with the 6 principles. It does NOT replace

**Step 6: Phase 0: Intake + Restore Point**

**Step 7: /autoplan Restore Point**
> Captured: [timestamp] | Branch: [branch] | Commit: [short hash]

**Step 8: Re-run Instructions**
> 1. Copy "Original Plan State" below back to your plan file

**Step 9: Original Plan State**
> [verbatim plan file contents]

**Step 10: Phase 1: CEO Review (Strategy & Scope)**
> Follow plan-ceo-review/SKILL.md — all sections, full depth.

**Step 11: Phase 2: Design Review (conditional — skip if no UI scope)**
> Follow plan-design-review/SKILL.md — all 7 dimensions, full depth.

**Step 12: Phase 3: Eng Review + Dual Voices**
> Follow plan-eng-review/SKILL.md — all sections, full depth.

**Step 13: Decision Audit Trail**
> After each auto-decision, append a row to the plan file using Edit:

**Step 14: Decision Audit Trail**
> Write one row per decision incrementally (via Edit). This keeps the audit on disk,

**Step 15: Pre-Gate Verification**
> Before presenting the Final Approval Gate, verify that required outputs were actually

**Step 16: Phase 4: Final Approval Gate**
> **STOP here and present the final state to the user.**

**Step 17: /autoplan Review Complete**

**Step 18: Completion: Write Review Logs**
> On approval, write 3 separate review log entries so /ship's dashboard recognizes them:

**Step 19: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
