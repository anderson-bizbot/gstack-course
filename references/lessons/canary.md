# Lesson: `/canary`

> Sprint phase: **Other** | Template: 221 lines | Version: 1.0.0
> Source: `garrytan/gstack/canary/SKILL.md.tmpl`

## What Is This?

Post-deploy canary monitoring. Watches the live app for console errors,
performance regressions, and page failures using the browse daemon. Takes
periodic screenshots, compares against pre-deploy baselines, and alerts
on anomalies. Use when: "monitor deploy", "canary", "post-deploy check",
"watch production", "verify deploy".

## When Do You Use It?

- on anomalies. Use when: "monitor deploy", "canary", "post-deploy check",

## What Do You Say to Claude?

Type `/canary` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "monitor deploy"
- "canary"
- "post-deploy check"
- "watch production"
- "verify deploy"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Phase 6: Health Report

## The Workflow

**Step 1: /canary — Post-Deploy Visual Monitor**
> You are a **Release Reliability Engineer** watching production after a deploy. You've seen deploys that pass CI but break in production — a missing environment variable, a CDN cache serving stale asse...

**Step 2: User-invocable**
> When the user types `/canary`, run this skill.

**Step 3: Arguments**

**Step 4: Instructions**

**Step 5: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
