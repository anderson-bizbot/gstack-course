# Lesson: `/careful`

> Sprint phase: **Safety** | Template: 58 lines | Version: 0.1.0
> Source: `garrytan/gstack/careful/SKILL.md.tmpl`

## What Is This?

Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,
force-push, git reset --hard, kubectl delete, and similar destructive operations.
User can override each warning. Use when touching prod, debugging live systems,
or working in a shared environment. Use when asked to "be careful", "safety mode",
"prod mode", or "careful mode".

## When Do You Use It?

- User can override each warning. Use when touching prod, debugging live systems,
- or working in a shared environment. Use when asked to "be careful", "safety mode",

## What Do You Say to Claude?

Type `/careful` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "be careful"
- "safety mode"
- "prod mode"
- "careful mode"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Safety** phase of your sprint.

## The Workflow

**Step 1: /careful — Destructive Command Guardrails**
> Safety mode is now **active**. Every bash command will be checked for destructive

**Step 2: What's protected**

**Step 3: Safe exceptions**
> These patterns are allowed without warning:

**Step 4: How it works**
> The hook reads the command from the tool input JSON, checks it against the

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SAFETY phase
```

## What Comes Next?

- Continue your current workflow with safety enabled.
- Use `/unfreeze` when done.
