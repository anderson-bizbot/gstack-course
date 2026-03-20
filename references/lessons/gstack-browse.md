# Lesson: `/browse`

> Sprint phase: **Test** | Size: 21,794 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-browse/SKILL.md`

## What Is This?

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.

## When Do You Use It?

- ~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
- user flow, or file a bug with evidence. Use when asked to "open in browser", "test the

## What Do You Say to Claude?

Type `/browse` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "open in browser"
- "test the
site"
- "take a screenshot"
- "dogfood this"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*

## What Do You Get?

- **Raw output**
- **4. Visual evidence for bug reports**
- **User Handoff**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

5. **Core QA Patterns**

6. **User Handoff**
   When you hit something you can't handle in headless mode (CAPTCHA, complex auth, multi-factor

7. **1. Open a visible Chrome at the current page**
   $B handoff "Stuck on CAPTCHA at login page"

8. **2. Tell the user what happened (via AskUserQuestion)**

9. **"I've opened Chrome at the login page. Please solve the CAPTCHA**

10. **and let me know when you're done."**

11. **3. When user says "done", re-snapshot and continue**
   $B resume

12. **Snapshot Flags**
   The snapshot is your primary tool for understanding and interacting with pages.

13. **Full Command List**

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
