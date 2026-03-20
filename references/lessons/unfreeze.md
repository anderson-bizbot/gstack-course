# Lesson: `/unfreeze`

> Sprint phase: **Safety** | Template: 39 lines | Version: 0.1.0
> Source: `garrytan/gstack/unfreeze/SKILL.md.tmpl`

## What Is This?

Clear the freeze boundary set by /freeze, allowing edits to all directories
again. Use when you want to widen edit scope without ending the session.
"allow all edits".

## When Do You Use It?

- again. Use when you want to widen edit scope without ending the session.
- Use when asked to "unfreeze", "unlock edits", "remove freeze", or

## What Do You Say to Claude?

Type `/unfreeze` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "unfreeze"
- "unlock edits"
- "remove freeze"
- "allow all edits"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Safety** phase of your sprint.

## The Workflow

**Step 1: /unfreeze — Clear Freeze Boundary**
> Remove the edit restriction set by `/freeze`, allowing edits to all directories.

**Step 2: Clear the boundary**
> STATE_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.gstack}"

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SAFETY phase
```

## What Comes Next?

- Continue your current workflow with safety enabled.
- Use `/unfreeze` when done.
