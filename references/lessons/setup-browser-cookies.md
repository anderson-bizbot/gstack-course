# Lesson: `/setup-browser-cookies`

> Sprint phase: **Test** | Template: 75 lines | Version: 1.0.0
> Source: `garrytan/gstack/setup-browser-cookies/SKILL.md.tmpl`

## What Is This?

Import cookies from your real browser (Comet, Chrome, Arc, Brave, Edge) into the
headless browse session. Opens an interactive picker UI where you select which
cookie domains to import. Use before QA testing authenticated pages. Use when asked
to "import cookies", "login to the site", or "authenticate the browser".

## When Do You Use It?

- cookie domains to import. Use before QA testing authenticated pages. Use when asked

## What Do You Say to Claude?

Type `/setup-browser-cookies` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "import cookies"
- "login to the site"
- "authenticate the browser"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Test** phase of your sprint.

## The Workflow

**Step 1: Setup Browser Cookies**
> Import logged-in sessions from your real Chromium browser into the headless browse session.

**Step 2: How it works**
> 1. Find the browse binary

**Step 3: Steps**

**Step 4: Notes**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: TEST phase
```

## What Comes Next?

- After testing, ship: `/ship`
- If bugs found, fix and re-test.
