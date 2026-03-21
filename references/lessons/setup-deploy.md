# Lesson: `/setup-deploy`

> Sprint phase: **Other** | Template: 221 lines | Version: 1.0.0
> Source: `garrytan/gstack/setup-deploy/SKILL.md.tmpl`

## What Is This?

Configure deployment settings for /land-and-deploy. Detects your deploy
platform (Fly.io, Render, Vercel, Netlify, Heroku, GitHub Actions, custom),
production URL, health check endpoints, and deploy status commands. Writes
the configuration to CLAUDE.md so all future deploys are automatic.
"how do I deploy with gstack", "add deploy config".

## When Do You Use It?

- Use when: "setup deploy", "configure deployment", "set up land-and-deploy",

## What Do You Say to Claude?

Type `/setup-deploy` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "setup deploy"
- "configure deployment"
- "set up land-and-deploy"
- "how do I deploy with gstack"
- "add deploy config"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Other** phase of your sprint.

## The Workflow

**Step 1: /setup-deploy — Configure Deployment for gstack**
> You are helping the user configure their deployment so `/land-and-deploy` works

**Step 2: User-invocable**
> When the user types `/setup-deploy`, run this skill.

**Step 3: Instructions**

**Step 4: Platform config files**
> [ -f fly.toml ] && echo "PLATFORM:fly" && cat fly.toml

**Step 5: GitHub Actions deploy workflows**
> for f in .github/workflows/*.yml .github/workflows/*.yaml; do

**Step 6: Project type**
> [ -f package.json ] && grep -q '"bin"' package.json 2>/dev/null && echo "PROJECT_TYPE:cli"

**Step 7: Deploy Configuration (configured by /setup-deploy)**

**Step 8: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
