# Lesson: `/qa-only`

> Sprint phase: **Test** | Template: 101 lines | Version: 1.0.0
> Source: `garrytan/gstack/qa-only/SKILL.md.tmpl`

## What Is This?

Report-only QA testing. Systematically tests a web application and produces a
structured report with health score, screenshots, and repro steps — but never
fixes anything. Use when asked to "just report bugs", "qa report only", or
"test but don't fix". For the full test-fix-verify loop, use /qa instead.

## When Do You Use It?

- fixes anything. Use when asked to "just report bugs", "qa report only", or
- Proactively suggest when the user wants a bug report without any code changes.

## What Do You Say to Claude?

Type `/qa-only` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "just report bugs"
- "qa report only"
- "test but don't fix"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- /qa-only: Report-Only QA Testing
- Output
- File: `~/.gstack/projects/{slug}/{user}-{branch}-test-outcome-{datetime}.md`
- Output Structure

## The Workflow

**Step 1: /qa-only: Report-Only QA Testing**
> You are a QA engineer. Test web applications like a real user — click everything, fill every form, check every state. Produce a structured report with evidence. **NEVER fix anything.**

**Step 2: Setup**
> **Parse the user's request for these parameters:**

**Step 3: Test Plan Context**
> Before falling back to git diff heuristics, check for richer test plan sources:

**Step 4: Output**
> Write the report to both local and project-scoped locations:

**Step 5: Additional Rules (qa-only specific)**
> 11. **Never fix bugs.** Find and document only. Do not read source code, edit files, or suggest fixes in the report. Your job is to report what's broken, not to fix it. Use `/qa` for the test-fix-veri...

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: TEST phase
```

## What Comes Next?

- After testing, ship: `/ship`
- If bugs found, fix and re-test.
