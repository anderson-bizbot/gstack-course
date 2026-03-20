# Lesson: `/careful`

> Sprint phase: **Safety** | Size: 2,567 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-careful/SKILL.md`

## What Is This?

Safety guardrails for destructive commands. Warns before rm -rf, DROP TABLE,
force-push, git reset --hard, kubectl delete, and similar destructive operations.
User can override each warning. Use when touching prod, debugging live systems,

## When Do You Use It?

- User can override each warning. Use when touching prod, debugging live systems,
- or working in a shared environment. Use when asked to "be careful", "safety mode",

## What Do You Say to Claude?

Type `/careful` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "be careful"
- "safety mode"
- "prod mode"
- "careful mode"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

The skill produces structured output relevant to the safety phase.

## The Workflow (Step by Step)

1. **/careful — Destructive Command Guardrails**
   Safety mode is now **active**. Every bash command will be checked for destructive

2. **What's protected**

3. **Safe exceptions**
   These patterns are allowed without warning:

4. **How it works**
   The hook reads the command from the tool input JSON, checks it against the

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `(continue your current workflow with safety enabled)`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
