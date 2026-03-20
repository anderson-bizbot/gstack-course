# Lesson: `/retro`

> Sprint phase: **Ship** | Size: 33,922 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-retro/SKILL.md`

## What Is This?

Weekly engineering retrospective. Analyzes commit history, work patterns,
and code quality metrics with persistent history and trend tracking.
Team-aware: breaks down per-person contributions with praise and growth areas.

## When Do You Use It?

- Use when asked to "weekly retro", "what did we ship", or "engineering retrospective".
- Proactively suggest at the end of a work week or sprint.

## What Do You Say to Claude?

Type `/retro` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "weekly retro"
- "what did we ship"
- "engineering retrospective"

## What Will Claude Ask You?

Claude handles this automatically — you provide the context, it runs the workflow.

## What Do You Get?

- **Raw output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Detect default branch**
   Before gathering data, detect the repo's default branch name:

5. **/retro — Weekly Engineering Retrospective**
   Generates a comprehensive engineering retrospective analyzing commit history, work patterns, and code quality metrics. Team-aware: identifies the user

6. **User-invocable**
   When the user types `/retro`, run this skill.

7. **Arguments**

8. **Instructions**
   Parse the argument to determine the time window. Default to 7 days if no argument given. All times should be reported in the user's **local timezone**

9. **Identify who is running the retro**
   git config user.name

10. **1. All commits in window with timestamps, subject, hash, AUTHOR, files changed, insertions, deletions**
   git log origin/<default> --since="<window>" --format="%H|%aN|%ae|%ai|%s" --shortstat

11. **2. Per-commit test vs total LOC breakdown with author**

12. **Each commit block starts with COMMIT:<hash>|<author>, followed by numstat lines.**

13. **Separate test files (matching test/|spec/|__tests__/) from production files.**
   git log origin/<default> --since="<window>" --format="COMMIT:%H|%aN" --numstat

14. **3. Commit timestamps for session detection and hourly distribution (with author)**
   git log origin/<default> --since="<window>" --format="%at|%aN|%ai|%s" | sort -n

15. **4. Files most frequently changed (hotspot analysis)**
   git log origin/<default> --since="<window>" --format="" --name-only | grep -v '^$' | sort | uniq -c | sort -rn

16. **5. PR numbers from commit messages (extract #NNN patterns)**
   git log origin/<default> --since="<window>" --format="%s" | grep -oE '#[0-9]+' | sed 's/^#//' | sort -n | uniq | sed 's/^/#/'

17. **6. Per-author file hotspots (who touches what)**
   git log origin/<default> --since="<window>" --format="AUTHOR:%aN" --name-only

18. **7. Per-author commit counts (quick summary)**
   git shortlog origin/<default> --since="<window>" -sn --no-merges

19. **8. Greptile triage history (if available)**
   cat ~/.gstack/greptile-history.md 2>/dev/null || true

20. **9. TODOS.md backlog (if available)**
   cat TODOS.md 2>/dev/null || true

21. **10. Test file count**
   find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec.*' 2>/dev/null | grep -v node_modules | wc -l

22. **11. Regression test commits in window**
   git log origin/<default> --since="<window>" --oneline --grep="test(qa):" --grep="test(design):" --grep="test: coverage"

23. **12. gstack skill usage telemetry (if available)**
   cat ~/.gstack/analytics/skill-usage.jsonl 2>/dev/null || true

24. **12. Test files changed in window**
   git log origin/<default> --since="<window>" --format="" --name-only | grep -E '\.(test|spec)\.' | sort -u | wc -l

25. **Team streak: all unique commit dates (local time) — no hard cutoff**
   git log origin/<default> --format="%ad" --date=format:"%Y-%m-%d" | sort -u

26. **Personal streak: only the current user's commits**
   git log origin/<default> --author="<user_name>" --format="%ad" --date=format:"%Y-%m-%d" | sort -u

27. **Count existing retros for today to get next sequence number**
   today=$(date +%Y-%m-%d)

28. **Save as .context/retros/${today}-${next}.json**
   Use the Write tool to save the JSON file with this schema:

29. **Engineering Retro: [date range]**

30. **Compare Mode**
   When the user runs `/retro compare` (or `/retro compare 14d`):

31. **Tone**

32. **Important Rules**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → >>>/retro<<<
```

## What Comes Next?

- `/document-release`
- `/retro`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
