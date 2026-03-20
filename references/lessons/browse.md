# Lesson: `/browse`

> Sprint phase: **Test** | Template: 142 lines | Version: 1.1.0
> Source: `garrytan/gstack/browse/SKILL.md.tmpl`

## What Is This?

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.
~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
user flow, or file a bug with evidence. Use when asked to "open in browser", "test the
site", "take a screenshot", or "dogfood this".

## When Do You Use It?

- ~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
- user flow, or file a bug with evidence. Use when asked to "open in browser", "test the

## What Do You Say to Claude?

Type `/browse` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "open in browser"
- "test the
site"
- "take a screenshot"
- "dogfood this"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- 4. Visual evidence for bug reports
- User Handoff

## The Workflow

**Step 1: browse: QA Testing & Dogfooding**
> Persistent headless Chromium. First call auto-starts (~3s), then ~100ms per command.

**Step 2: Core QA Patterns**

**Step 3: User Handoff**
> When you hit something you can't handle in headless mode (CAPTCHA, complex auth, multi-factor

**Step 4: 1. Open a visible Chrome at the current page**
> $B handoff "Stuck on CAPTCHA at login page"

**Step 5: 2. Tell the user what happened (via AskUserQuestion)**

**Step 6: "I've opened Chrome at the login page. Please solve the CAPTCHA**

**Step 7: and let me know when you're done."**

**Step 8: 3. When user says "done", re-snapshot and continue**
> **When to use handoff:**

**Step 9: Snapshot Flags**
> {{SNAPSHOT_FLAGS}}

**Step 10: Full Command List**
> {{COMMAND_REFERENCE}}

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: TEST phase
```

## What Comes Next?

- After testing, ship: `/ship`
- If bugs found, fix and re-test.
