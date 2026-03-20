# Lesson: `/upgrade`

> Sprint phase: **Meta** | Size: 7,959 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-upgrade/SKILL.md`

## What Is This?

Upgrade gstack to the latest version. Detects global vs vendored install,
runs the upgrade, and shows what's new. Use when asked to "upgrade gstack",
"update gstack", or "get latest version".

## When Do You Use It?

- runs the upgrade, and shows what's new. Use when asked to "upgrade gstack",

## What Do You Say to Claude?

Type `/upgrade` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "upgrade gstack"
- "update gstack"
- "get latest version"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack **v{new}** is available (you're on v{old}). Upgrade now?"*

## What Do You Get?

The skill produces structured output relevant to the meta phase.

## The Workflow (Step by Step)

1. **/gstack-upgrade**
   Upgrade gstack to the latest version and show what's new.

2. **Inline upgrade flow**
   This section is referenced by all skill preambles when they detect `UPGRADE_AVAILABLE`.

3. **Standalone usage**
   When invoked directly as `/gstack-upgrade` (not from a preamble):

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `(continue with your current sprint)`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
