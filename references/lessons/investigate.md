# Lesson: `/investigate`

> Sprint phase: **Review** | Template: 197 lines | Version: 1.0.0
> Source: `garrytan/gstack/investigate/SKILL.md.tmpl`

## What Is This?

Systematic debugging with root cause investigation. Four phases: investigate,
analyze, hypothesize, implement. Iron Law: no fixes without root cause.
"investigate this error", or "root cause analysis".
is troubleshooting why something stopped working.

## When Do You Use It?

- Use when asked to "debug this", "fix this bug", "why is this broken",
- Proactively suggest when the user reports errors, unexpected behavior, or

## What Do You Say to Claude?

Type `/investigate` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "debug this"
- "fix this bug"
- "why is this broken"
- "investigate this error"
- "root cause analysis"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Phase 5: Verification & Report

## The Workflow

**Step 1: Systematic Debugging**

**Step 2: Iron Law**
> **NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.**

**Step 3: Phase 1: Root Cause Investigation**
> Gather context before forming any hypothesis.

**Step 4: Scope Lock**
> After forming your root cause hypothesis, lock edits to the affected module to prevent scope creep.

**Step 5: Phase 2: Pattern Analysis**
> Check if this bug matches a known pattern:

**Step 6: Phase 3: Hypothesis Testing**
> Before writing ANY fix, verify your hypothesis.

**Step 7: Phase 4: Implementation**
> Once root cause is confirmed:

**Step 8: Phase 5: Verification & Report**
> **Fresh verification:** Reproduce the original bug scenario and confirm it's fixed. This is not optional.

**Step 9: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: REVIEW phase
```

## What Comes Next?

- After review, test: `/qa` or `/qa-only`
- Then ship: `/ship`
