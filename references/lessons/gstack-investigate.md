# Lesson: `/investigate`

> Sprint phase: **Review** | Size: 18,747 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-investigate/SKILL.md`

## What Is This?

Systematic debugging with root cause investigation. Four phases: investigate,
analyze, hypothesize, implement. Iron Law: no fixes without root cause.
Use when asked to "debug this", "fix this bug", "why is this broken",

## When Do You Use It?

- Use when asked to "debug this", "fix this bug", "why is this broken",
- Proactively suggest when the user reports errors, unexpected behavior, or

## What Do You Say to Claude?

Type `/investigate` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "debug this"
- "fix this bug"
- "why is this broken"
- "investigate this error"
- "root cause analysis"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

- **Raw output**
- **Phase 5: Verification & Report**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Iron Law**
   **NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST.**

5. **Phase 1: Root Cause Investigation**
   Gather context before forming any hypothesis.

6. **Scope Lock**
   After forming your root cause hypothesis, lock edits to the affected module to prevent scope creep.

7. **Phase 2: Pattern Analysis**
   Check if this bug matches a known pattern:

8. **Phase 3: Hypothesis Testing**
   Before writing ANY fix, verify your hypothesis.

9. **Phase 4: Implementation**
   Once root cause is confirmed:

10. **Phase 5: Verification & Report**
   **Fresh verification:** Reproduce the original bug scenario and confirm it's fixed. This is not optional.

11. **Important Rules**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `/qa`
- `/ship`

## Pro Tips

- Watch for red flags Claude identifies — they're based on YC pattern matching
