# Lesson: `/retro`

> Sprint phase: **Ship** | Template: 849 lines | Version: 2.0.0
> Source: `garrytan/gstack/retro/SKILL.md.tmpl`

## What Is This?

Weekly engineering retrospective. Analyzes commit history, work patterns,
and code quality metrics with persistent history and trend tracking.
Team-aware: breaks down per-person contributions with praise and growth areas.

## When Do You Use It?

- Use when asked to "weekly retro", "what did we ship", or "engineering retrospective".
- Proactively suggest at the end of a work week or sprint.

## What Do You Say to Claude?

Type `/retro` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "weekly retro"
- "what did we ship"
- "engineering retrospective"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Step 8: Focus Score + Ship of the Week
- Shipping Velocity
- Global Step 4: Compute global shipping streak
- Ship of the Week (Global)

## The Workflow

**Step 1: /retro — Weekly Engineering Retrospective**
> Generates a comprehensive engineering retrospective analyzing commit history, work patterns, and code quality metrics. Team-aware: identifies the user running the command, then analyzes every contribu...

**Step 2: User-invocable**
> When the user types `/retro`, run this skill.

**Step 3: Arguments**

**Step 4: Instructions**
> Parse the argument to determine the time window. Default to 7 days if no argument given. All times should be reported in the user's **local timezone** (use the system default — do NOT set `TZ`).

**Step 5: Identify who is running the retro**
> git config user.name

**Step 6: 1. All commits in window with timestamps, subject, hash, AUTHOR, files changed, insertions, deletions**
> git log origin/<default> --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat

**Step 7: 2. Per-commit test vs total LOC breakdown with author**

**Step 8: Each commit block starts with COMMIT:<hash>|<author>, followed by numstat lines.**

**Step 9: Separate test files (matching test/|spec/|__tests__/) from production files.**
> git log origin/<default> --since="<window>" --format="COMMIT:%H|%aN" --numstat

**Step 10: 3. Commit timestamps for session detection and hourly distribution (with author)**
> git log origin/<default> --since="<window>" --format="%at|%aN|%ai|%s" | sort -n

**Step 11: 4. Files most frequently changed (hotspot analysis)**
> git log origin/<default> --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn

**Step 12: 5. PR/MR numbers from commit messages (GitHub #NNN, GitLab !NNN)**
> git log origin/<default> --since="<window>" --format="%s" | grep -oE '[#!][0-9]+' | sort -t'#' -k1 | uniq

**Step 13: 6. Per-author file hotspots (who touches what)**
> git log origin/<default> --since="<window>" --format="AUTHOR:%aN" --name-only

**Step 14: 7. Per-author commit counts (quick summary)**
> git shortlog origin/<default> --since="<window>" -sn --no-merges

**Step 15: 8. Greptile triage history (if available)**
> cat ~/.gstack/greptile-history.md 2>/dev/null || true

**Step 16: 9. TODOS.md backlog (if available)**
> cat TODOS.md 2>/dev/null || true

**Step 17: 10. Test file count**
> find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec.*' 2>/dev/null | grep -v node_modules | wc -l

**Step 18: 11. Regression test commits in window**
> git log origin/<default> --since="<window>" --oneline --grep="test(qa):" --grep="test(design):" --grep="test: coverage"

**Step 19: 12. gstack skill usage telemetry (if available)**
> cat ~/.gstack/analytics/skill-usage.jsonl 2>/dev/null || true

**Step 20: 12. Test files changed in window**
> git log origin/<default> --since="<window>" --format="" --name-only | grep -E '\.(test|spec)\.' | sort -u | wc -l

**Step 21: Team streak: all unique commit dates (local time) — no hard cutoff**
> git log origin/<default> --format="%ad" --date=format:"%Y-%m-%d" | sort -u

**Step 22: Personal streak: only the current user's commits**
> git log origin/<default> --author="<user_name>" --format="%ad" --date=format:"%Y-%m-%d" | sort -u

**Step 23: Count existing retros for today to get next sequence number**
> today=$(date +%Y-%m-%d)

**Step 24: Save as .context/retros/${today}-${next}.json**
> Use the Write tool to save the JSON file with this schema:

**Step 25: Engineering Retro: [date range]**

**Step 26: Global Retrospective Mode**
> When the user runs `/retro global` (or `/retro global 14d`), follow this flow instead of the repo-scoped Steps 1-14. This mode works from any directory — it does NOT require being inside a git repo.

**Step 27: Commits with stats**
> git -C <path> log origin/$DEFAULT --since="<start_date>T00:00:00" --format="%H|%aN|%ai|%s" --shortstat

**Step 28: Commit timestamps for session detection, streak, and context switching**
> git -C <path> log origin/$DEFAULT --since="<start_date>T00:00:00" --format="%at|%aN|%ai|%s" | sort -n

**Step 29: Per-author commit counts**
> git -C <path> shortlog origin/$DEFAULT --since="<start_date>T00:00:00" -sn --no-merges

**Step 30: PR/MR numbers from commit messages (GitHub #NNN, GitLab !NNN)**
> git -C <path> log origin/$DEFAULT --since="<start_date>T00:00:00" --format="%s" | grep -oE '[#!][0-9]+' | sort -t'#' -k1 | uniq

**Step 31: 🚀 Your Week: [user name] — [date range]**
> This section is the **shareable personal card**. It contains ONLY the current user's

**Step 32: Global Engineering Retro: [date range]**
> Everything below is the full analysis — team data, project breakdowns, patterns.

**Step 33: Compare Mode**
> When the user runs `/retro compare` (or `/retro compare 14d`):

**Step 34: Tone**

**Step 35: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SHIP phase
```

## What Comes Next?

- After shipping, document: `/document-release`
- End of week: `/retro`
