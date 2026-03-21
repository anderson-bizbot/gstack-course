# Lesson: `/land-and-deploy`

> Sprint phase: **Other** | Template: 576 lines | Version: 1.0.0
> Source: `garrytan/gstack/land-and-deploy/SKILL.md.tmpl`

## What Is This?

Land and deploy workflow. Merges the PR, waits for CI and deploy,
verifies production health via canary checks. Takes over after /ship
creates the PR. Use when: "merge", "land", "deploy", "merge and verify",
"land it", "ship it to production".

## When Do You Use It?

- creates the PR. Use when: "merge", "land", "deploy", "merge and verify",

## What Do You Say to Claude?

Type `/land-and-deploy` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "merge"
- "land"
- "deploy"
- "merge and verify"
- "land it"
- "ship it to production"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Non-interactive philosophy (like /ship) — with one critical gate
- 3.5b: Test results
- 3.5e: Readiness report and confirmation
- Step 9: Deploy report

## The Workflow

**Step 1: /land-and-deploy — Merge, Deploy, Verify**
> You are a **Release Engineer** who has deployed to production thousands of times. You know the two worst feelings in software: the merge that breaks prod, and the merge that sits in queue for 45 minut...

**Step 2: User-invocable**
> When the user types `/land-and-deploy`, run this skill.

**Step 3: Arguments**

**Step 4: Non-interactive philosophy (like /ship) — with one critical gate**
> This is a **mostly automated** workflow. Do NOT ask for confirmation at any step except

**Step 5: Step 1: Pre-flight**
> 1. Check GitHub CLI authentication:

**Step 6: Step 2: Pre-merge checks**
> Check CI status and merge readiness:

**Step 7: Step 3: Wait for CI (if pending)**
> If required checks are still pending, wait for them to complete. Use a timeout of 15 minutes:

**Step 8: Step 3.5: Pre-merge readiness gate**
> **This is the critical safety check before an irreversible merge.** The merge cannot

**Step 9: Step 4: Merge the PR**
> Record the start timestamp for timing data.

**Step 10: Step 5: Deploy strategy detection**
> Determine what kind of project this is and how to verify the deploy.

**Step 11: Step 6: Wait for deploy (if applicable)**
> The deploy verification strategy depends on the platform detected in Step 5.

**Step 12: Step 7: Canary verification (conditional depth)**
> Use the diff-scope classification from Step 5 to determine canary depth:

**Step 13: Step 8: Revert (if needed)**
> If the user chose to revert at any point:

**Step 14: Step 9: Deploy report**
> Create the deploy report directory:

**Step 15: Step 10: Suggest follow-ups**
> After the deploy report, suggest relevant follow-ups:

**Step 16: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
