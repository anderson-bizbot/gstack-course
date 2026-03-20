# Lesson: `/freeze`

> Sprint phase: **Safety** | Size: 2,955 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-freeze/SKILL.md`

## What Is This?

Restrict file edits to a specific directory for the session. Blocks Edit and
Write outside the allowed path. Use when debugging to prevent accidentally
"fixing" unrelated code, or when you want to scope changes to one module.

## When Do You Use It?

- Write outside the allowed path. Use when debugging to prevent accidentally
- Use when asked to "freeze", "restrict edits", "only edit this folder",

## What Do You Say to Claude?

Type `/freeze` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "fixing"
- "freeze"
- "restrict edits"
- "only edit this folder"
- "lock down edits"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

The skill produces structured output relevant to the safety phase.

## The Workflow (Step by Step)

1. **/freeze — Restrict Edits to a Directory**
   Lock file edits to a specific directory. Any Edit or Write operation targeting

2. **Setup**
   Ask the user which directory to restrict edits to. Use AskUserQuestion:

3. **How it works**
   The hook reads `file_path` from the Edit/Write tool input JSON, then checks

4. **Notes**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `(continue your current workflow with safety enabled)`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
