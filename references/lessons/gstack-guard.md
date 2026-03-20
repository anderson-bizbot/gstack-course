# Lesson: `/guard`

> Sprint phase: **Safety** | Size: 3,015 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-guard/SKILL.md`

## What Is This?

Full safety mode: destructive command warnings + directory-scoped edits.
Combines /careful (warns before rm -rf, DROP TABLE, force-push, etc.) with
/freeze (blocks edits outside a specified directory). Use for maximum safety

## When Do You Use It?

- when touching prod or debugging live systems. Use when asked to "guard mode",

## What Do You Say to Claude?

Type `/guard` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "guard mode"
- "full safety"
- "lock it down"
- "maximum safety"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

The skill produces structured output relevant to the safety phase.

## The Workflow (Step by Step)

1. **/guard — Full Safety Mode**
   Activates both destructive command warnings and directory-scoped edit restrictions.

2. **Setup**
   Ask the user which directory to restrict edits to. Use AskUserQuestion:

3. **What's protected**
   See `/careful` for the full list of destructive command patterns and safe exceptions.

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `(continue your current workflow with safety enabled)`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
