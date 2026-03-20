# Lesson: `/unfreeze`

> Sprint phase: **Safety** | Size: 1,307 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-unfreeze/SKILL.md`

## What Is This?

Clear the freeze boundary set by /freeze, allowing edits to all directories
again. Use when you want to widen edit scope without ending the session.
Use when asked to "unfreeze", "unlock edits", "remove freeze", or

## When Do You Use It?

- again. Use when you want to widen edit scope without ending the session.
- Use when asked to "unfreeze", "unlock edits", "remove freeze", or

## What Do You Say to Claude?

Type `/unfreeze` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "unfreeze"
- "unlock edits"
- "remove freeze"
- "allow all edits"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

The skill produces structured output relevant to the safety phase.

## The Workflow (Step by Step)

1. **/unfreeze — Clear Freeze Boundary**
   Remove the edit restriction set by `/freeze`, allowing edits to all directories.

2. **Clear the boundary**
   STATE_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.gstack}"

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `(continue your current workflow with safety enabled)`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
