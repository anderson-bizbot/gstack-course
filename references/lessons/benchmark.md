# Lesson: `/benchmark`

> Sprint phase: **Other** | Template: 234 lines | Version: 1.0.0
> Source: `garrytan/gstack/benchmark/SKILL.md.tmpl`

## What Is This?

Performance regression detection using the browse daemon. Establishes
baselines for page load times, Core Web Vitals, and resource sizes.
Compares before/after on every PR. Tracks performance trends over time.
"bundle size", "load time".

## When Do You Use It?

- Use when: "performance", "benchmark", "page speed", "lighthouse", "web vitals",

## What Do You Say to Claude?

Type `/benchmark` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "performance"
- "benchmark"
- "page speed"
- "lighthouse"
- "web vitals"
- "bundle size"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- File: `.gstack/benchmark-reports/baselines/baseline.json`
- Phase 9: Save Report
- File: `.gstack/benchmark-reports/{date}-benchmark.md`

## The Workflow

**Step 1: /benchmark — Performance Regression Detection**
> You are a **Performance Engineer** who has optimized apps serving millions of requests. You know that performance doesn't degrade in one big regression — it dies by a thousand paper cuts. Each PR adds...

**Step 2: User-invocable**
> When the user types `/benchmark`, run this skill.

**Step 3: Arguments**

**Step 4: Instructions**

**Step 5: Resource                  Type      Size      Duration**
> 1   vendor.chunk.js          script    320KB     480ms

**Step 6: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
