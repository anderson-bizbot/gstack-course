# Lesson: `/land-and-deploy`

> Sprint phase: **Other** | Template: 916 lines | Version: 1.0.0
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

Claude walks you through a structured conversation:

- *"That's everything I detected. Take a look at the table above — does this match how your project actually deploys?"*

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

**Step 5: Voice & Tone**
> Every message to the user should make them feel like they have a senior release engineer

**Step 6: Step 1: Pre-flight**
> Tell the user: "Starting deploy sequence. First, let me make sure everything is connected and find your PR."

**Step 7: Step 1.5: First-run dry-run validation**
> Check whether this project has been through a successful `/land-and-deploy` before,

**Step 8: Test gh auth (already passed in Step 1, but confirm)**
> gh auth status 2>&1 | head -3

**Step 9: Test platform CLI if detected**

**Step 10: Fly.io: fly status --app {app} 2>/dev/null**

**Step 11: Heroku: heroku releases --app {app} -n 1 2>/dev/null**

**Step 12: Vercel: vercel ls 2>/dev/null | head -3**

**Step 13: Test production URL reachability**

**Step 14: curl -sf {production-url} -o /dev/null -w "%{http_code}" 2>/dev/null**
> Run whichever commands are relevant based on the detected platform. Build the results into this table:

**Step 15: Step 2: Pre-merge checks**
> Tell the user: "Checking CI status and merge readiness..."

**Step 16: Step 3: Wait for CI (if pending)**
> If required checks are still pending, wait for them to complete. Use a timeout of 15 minutes:

**Step 17: Step 3.5: Pre-merge readiness gate**
> **This is the critical safety check before an irreversible merge.** The merge cannot

**Step 18: Step 4: Merge the PR**
> Record the start timestamp for timing data. Also record which merge path is taken

**Step 19: Step 5: Deploy strategy detection**
> Determine what kind of project this is and how to verify the deploy.

**Step 20: Step 6: Wait for deploy (if applicable)**
> The deploy verification strategy depends on the platform detected in Step 5.

**Step 21: Step 7: Canary verification (conditional depth)**
> Tell the user: "Deploy is done. Now I'm going to check the live site to make sure everything looks good — loading the page, checking for errors, and measuring performance."

**Step 22: Step 8: Revert (if needed)**
> If the user chose to revert at any point:

**Step 23: Step 9: Deploy report**
> Create the deploy report directory:

**Step 24: Step 10: Suggest follow-ups**
> After the deploy report:

**Step 25: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
