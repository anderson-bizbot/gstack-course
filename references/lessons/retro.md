# Lesson: `/retro`

> Sprint phase: **Ship** | Template: 526 lines | Version: 2.0.0
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

## The Workflow

**Step 1: Detect default branch**
> Before gathering data, detect the repo's default branch name:

**Step 2: /retro — Weekly Engineering Retrospective**
> Generates a comprehensive engineering retrospective analyzing commit history, work patterns, and code quality metrics. Team-aware: identifies the user running the command, then analyzes every contribu...

**Step 3: User-invocable**
> When the user types `/retro`, run this skill.

**Step 4: Arguments**

**Step 5: Instructions**
> Parse the argument to determine the time window. Default to 7 days if no argument given. All times should be reported in the user's **local timezone** (use the system default — do NOT set `TZ`).

**Step 6: Identify who is running the retro**
> git config user.name

**Step 7: 1. All commits in window with timestamps, subject, hash, AUTHOR, files changed, insertions, deletions**
> git log origin/<default> --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat

**Step 8: 2. Per-commit test vs total LOC breakdown with author**

**Step 9: Each commit block starts with COMMIT:<hash>|<author>, followed by numstat lines.**

**Step 10: Separate test files (matching test/|spec/|__tests__/) from production files.**
> git log origin/<default> --since="<window>" --format="COMMIT:%H|%aN" --numstat

**Step 11: 3. Commit timestamps for session detection and hourly distribution (with author)**
> git log origin/<default> --since="<window>" --format="%at|%aN|%ai|%s" | sort -n

**Step 12: 4. Files most frequently changed (hotspot analysis)**
> git log origin/<default> --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn

**Step 13: 5. PR numbers from commit messages (extract #NNN patterns)**
> git log origin/<default> --since="<window>" --format="%s" | grep -oE '#[0-9]+' | sed 's/^#//' | sort -n | uniq | sed 's/^/#/'

**Step 14: 6. Per-author file hotspots (who touches what)**
> git log origin/<default> --since="<window>" --format="AUTHOR:%aN" --name-only

**Step 15: 7. Per-author commit counts (quick summary)**
> git shortlog origin/<default> --since="<window>" -sn --no-merges

**Step 16: 8. Greptile triage history (if available)**
> cat ~/.gstack/greptile-history.md 2>/dev/null || true

**Step 17: 9. TODOS.md backlog (if available)**
> cat TODOS.md 2>/dev/null || true

**Step 18: 10. Test file count**
> find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec.*' 2>/dev/null | grep -v node_modules | wc -l

**Step 19: 11. Regression test commits in window**
> git log origin/<default> --since="<window>" --oneline --grep="test(qa):" --grep="test(design):" --grep="test: coverage"

**Step 20: 12. gstack skill usage telemetry (if available)**
> cat ~/.gstack/analytics/skill-usage.jsonl 2>/dev/null || true

**Step 21: 12. Test files changed in window**
> git log origin/<default> --since="<window>" --format="" --name-only | grep -E '\.(test|spec)\.' | sort -u | wc -l

**Step 22: Team streak: all unique commit dates (local time) — no hard cutoff**
> git log origin/<default> --format="%ad" --date=format:"%Y-%m-%d" | sort -u

**Step 23: Personal streak: only the current user's commits**
> git log origin/<default> --author="<user_name>" --format="%ad" --date=format:"%Y-%m-%d" | sort -u

**Step 24: Count existing retros for today to get next sequence number**
> today=$(date +%Y-%m-%d)

**Step 25: Save as .context/retros/${today}-${next}.json**
> Use the Write tool to save the JSON file with this schema:

**Step 26: Engineering Retro: [date range]**

**Step 27: Compare Mode**
> When the user runs `/retro compare` (or `/retro compare 14d`):

**Step 28: Tone**

**Step 29: Important Rules**

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: SHIP phase
```

## What Comes Next?

- After shipping, document: `/document-release`
- End of week: `/retro`
