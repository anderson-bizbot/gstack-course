# Lesson: `/gstack-upgrade`

> Sprint phase: **Meta** | Template: 225 lines | Version: 1.1.0
> Source: `garrytan/gstack/gstack-upgrade/SKILL.md.tmpl`

## What Is This?

Upgrade gstack to the latest version. Detects global vs vendored install,
runs the upgrade, and shows what's new. Use when asked to "upgrade gstack",
"update gstack", or "get latest version".

## When Do You Use It?

- runs the upgrade, and shows what's new. Use when asked to "upgrade gstack",

## What Do You Say to Claude?

Type `/gstack-upgrade` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "upgrade gstack"
- "update gstack"
- "get latest version"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Meta** phase of your sprint.

## The Workflow

**Step 1: /gstack-upgrade**
> Upgrade gstack to the latest version and show what's new.

**Step 2: Inline upgrade flow**
> This section is referenced by all skill preambles when they detect `UPGRADE_AVAILABLE`.

**Step 3: Standalone usage**
> When invoked directly as `/gstack-upgrade` (not from a preamble):

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: META phase
```

## What Comes Next?

- Continue with your current sprint.
