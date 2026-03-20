# Lesson: `/freeze`

> Sprint phase: **Safety** | Template: 81 lines | Version: 0.1.0
> Source: `garrytan/gstack/freeze/SKILL.md.tmpl`

## What Is This?

Restrict file edits to a specific directory for the session. Blocks Edit and
Write outside the allowed path. Use when debugging to prevent accidentally
"fixing" unrelated code, or when you want to scope changes to one module.
or "lock down edits".

## When Do You Use It?

- Write outside the allowed path. Use when debugging to prevent accidentally
- Use when asked to "freeze", "restrict edits", "only edit this folder",

## What Do You Say to Claude?

Type `/freeze` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "fixing"
- "freeze"
- "restrict edits"
- "only edit this folder"
- "lock down edits"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Safety** phase of your sprint.

## The Workflow

**Step 1: /freeze — Restrict Edits to a Directory**
> Lock file edits to a specific directory. Any Edit or Write operation targeting

**Step 2: Setup**
> Ask the user which directory to restrict edits to. Use AskUserQuestion:

**Step 3: How it works**
> The hook reads `file_path` from the Edit/Write tool input JSON, then checks

**Step 4: Notes**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SAFETY phase
```

## What Comes Next?

- Continue your current workflow with safety enabled.
- Use `/unfreeze` when done.
