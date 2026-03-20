# Lesson: `/qa-only`

> Sprint phase: **Test** | Size: 27,114 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-qa-only/SKILL.md`

## What Is This?

Report-only QA testing. Systematically tests a web application and produces a
structured report with health score, screenshots, and repro steps — but never
fixes anything. Use when asked to "just report bugs", "qa report only", or

## When Do You Use It?

- fixes anything. Use when asked to "just report bugs", "qa report only", or
- Proactively suggest when the user wants a bug report without any code changes.

## What Do You Say to Claude?

Type `/qa-only` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "just report bugs"
- "qa report only"
- "test but don't fix"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*

## What Do You Get?

- **Raw output**
- **Output**
- **Output Structure**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Setup**
   **Parse the user's request for these parameters:**

5. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

6. **Test Plan Context**
   Before falling back to git diff heuristics, check for richer test plan sources:

7. **Modes**

8. **Workflow**

9. **Health Score Rubric**
   Compute each category score (0-100), then take the weighted average.

10. **Framework-Specific Guidance**

11. **Important Rules**
   1. **Repro is everything.** Every issue needs at least one screenshot. No exceptions.

12. **Output**
   Write the report to both local and project-scoped locations:

13. **Additional Rules (qa-only specific)**
   11. **Never fix bugs.** Find and document only. Do not read source code, edit files, or suggest fixes in the report. Your job is to report what's brok

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
