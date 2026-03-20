# Lesson: `/guard`

> Sprint phase: **Safety** | Template: 81 lines | Version: 0.1.0
> Source: `garrytan/gstack/guard/SKILL.md.tmpl`

## What Is This?

Full safety mode: destructive command warnings + directory-scoped edits.
Combines /careful (warns before rm -rf, DROP TABLE, force-push, etc.) with
/freeze (blocks edits outside a specified directory). Use for maximum safety
when touching prod or debugging live systems. Use when asked to "guard mode",
"full safety", "lock it down", or "maximum safety".

## When Do You Use It?

- when touching prod or debugging live systems. Use when asked to "guard mode",

## What Do You Say to Claude?

Type `/guard` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "guard mode"
- "full safety"
- "lock it down"
- "maximum safety"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Safety** phase of your sprint.

## The Workflow

**Step 1: /guard — Full Safety Mode**
> Activates both destructive command warnings and directory-scoped edit restrictions.

**Step 2: Setup**
> Ask the user which directory to restrict edits to. Use AskUserQuestion:

**Step 3: What's protected**
> See `/careful` for the full list of destructive command patterns and safe exceptions.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SAFETY phase
```

## What Comes Next?

- Continue your current workflow with safety enabled.
- Use `/unfreeze` when done.
