# Lesson: `/setup-browser-cookies`

> Sprint phase: **Test** | Size: 14,217 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-setup-browser-cookies/SKILL.md`

## What Is This?

Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the
headless browse session. Opens an interactive picker UI where you select which
cookie domains to import. Use before QA testing authenticated pages. Use when asked

## When Do You Use It?

- cookie domains to import. Use before QA testing authenticated pages. Use when asked

## What Do You Say to Claude?

Type `/setup-browser-cookies` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "import cookies"
- "login to the site"
- "authenticate the browser"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*

## What Do You Get?

- **Raw output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **How it works**
   1. Find the browse binary

5. **Steps**

6. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

7. **Notes**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `/ship`
- `/review`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
