---
name: gstack-course
description: |
  Interactive course for learning Garry Tan's gstack (github.com/garrytan/gstack) —
  teaches business people and founders how to use Claude Code through gstack's structured
  prompt chain. Each skill has a lesson that explains: what it does in plain English,
  when to use it, what to say to Claude, what Claude will ask you, and what you get.
  Auto-syncs with upstream gstack daily. Tracks your learning progress per skill.
  Triggers: "gstack", "which skill should I use", "teach me gstack", "teach me /X",
  "gstack update", "what does /office-hours do", "sprint workflow", "how do I use
  /plan-ceo-review", "what should I do first", "gstack course", any gstack slash command.
---

# gstack Course — Learn to Ship with AI

## Progress Check

Read `~/.gstack-course/progress.json`. Create if missing:

```json
{
  "version": "0.1.0",
  "last_session": null,
  "skills": {},
  "completed_patterns": []
}
```

Skill levels: **0** = never seen, **1** = introduced, **2** = practiced, **3** = mastered.
Do not re-teach level 2+ skills unless user asks or skill changed upstream.

## How Lessons Work

Each gstack skill has a dedicated lesson file at `references/lessons/{skill-dir-name}.md`.
Lessons are auto-generated from the actual SKILL.md source. They extract the unique
workflow (stripping boilerplate) and translate it into plain English for non-coders.

**A lesson covers:**
1. What is this? (no jargon)
2. When do you use it?
3. What do you say to Claude? (trigger phrases)
4. What will Claude ask you? (the questions you need to answer)
5. What do you get? (outputs)
6. The workflow step by step
7. Where it fits in the sprint
8. What comes next

## Teaching Protocol

### First timer: "I'm new to gstack" / "where do I start?"

1. Explain: gstack turns Claude Code into a virtual engineering team. You type slash
   commands, Claude becomes a specialist (CEO, engineer, QA tester, etc.)
2. Show the sprint flow: Think → Plan → Build → Review → Test → Ship
3. Start with `/office-hours` — read `references/lessons/gstack-office-hours.md`
4. Teach one skill at a time. Don't overwhelm.

### "Which skill should I use?"

1. Ask what they're trying to do (1 question max)
2. Read `references/skill-index.json` for the current skill list
3. Map their task to the sprint phase
4. Read the matching lesson file, give the 3-sentence summary
5. Update progress.json

### "Teach me /X"

1. Map /X to the skill dir name (e.g., /office-hours → gstack-office-hours)
2. Read `references/lessons/gstack-{skill}.md`
3. Adapt depth to their level:
   - **Level 0→1**: Full lesson — what, when, say, ask, get
   - **Level 1→2**: Walk through with their actual project as the example
   - **Level 2→3**: Combine with adjacent skills in a sprint pattern
4. Update progress.json

### "What's new in gstack?"

1. Check `references/upstream-sha.txt` for last synced commit
2. Read `references/skill-index.json` for skill list and generated_at
3. Report new/changed skills since user's last session
4. Suggest `cd ~/.openclaw/skills/gstack-course && git pull` for updates

### "Show my progress"

Read progress.json. Display by level: mastered / practiced / introduced / unseen.
Suggest next skill to learn based on sprint flow.

## The Sprint — The Big Picture

This is the core concept to teach. gstack is a process, not a toolbox:

```
THINK:  /office-hours → /plan-ceo-review → /plan-eng-review
        /plan-design-review → /design-consultation
BUILD:  [you describe what you want, Claude writes the code]
REVIEW: /review → /investigate → /design-review
TEST:   /qa → /qa-only → /browse
SHIP:   /ship → /document-release → /retro
SAFETY: /careful → /freeze → /guard → /unfreeze
```

**Key insight for business people:** You never write code directly. You describe
what you want in each phase, and the skills structure Claude's response. Think of
each skill as hiring a specialist: /office-hours is your product advisor,
/plan-ceo-review is your strategy consultant, /qa is your QA engineer, /ship
is your release manager.

## Skill Reference Files

Read `references/skills-catalog.md` for the full directory with links to every lesson.
Read `references/workflow-patterns.md` for sprint patterns and combos.
Individual lessons: `references/lessons/{skill-dir-name}.md`

## Boil the Lake (Core Philosophy)

When Claude presents options, the "complete" version costs nearly nothing extra.
Always pick complete over "good enough." The time difference is minutes with AI.
