# Lesson: `/connect-chrome`

> Sprint phase: **Other** | Template: 137 lines | Version: 0.1.0
> Source: `garrytan/gstack/connect-chrome/SKILL.md.tmpl`

## What Is This?

Launch real Chrome controlled by gstack with the Side Panel extension auto-loaded.
One command: connects Claude to a visible Chrome window where you can watch every
action in real time. The extension shows a live activity feed in the Side Panel.
"side panel", or "control my browser".

## When Do You Use It?

- Use when asked to "connect chrome", "open chrome", "real browser", "launch chrome",

## What Do You Say to Claude?

Type `/connect-chrome` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "connect chrome"
- "open chrome"
- "real browser"
- "launch chrome"
- "side panel"
- "control my browser"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Other** phase of your sprint.

## The Workflow

**Step 1: /connect-chrome — Launch Real Chrome with Side Panel**
> Connect Claude to a visible Chrome window with the gstack extension auto-loaded.

**Step 2: Step 1: Connect**
> This launches your system Chrome via Playwright with:

**Step 3: Step 2: Verify**
> Confirm the output shows `Mode: cdp`. Print the port number — the user may need

**Step 4: Step 3: Guide the user to the Side Panel**
> Use AskUserQuestion:

**Step 5: Step 4: Demo**
> After the user confirms the Side Panel is working, run a quick demo so they

**Step 6: Step 5: Sidebar chat**
> After the activity feed demo, tell the user about the sidebar chat:

**Step 7: Step 6: What's next**
> > You're all set! Chrome is under Claude's control with the Side Panel showing

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
