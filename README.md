# gstack-course

Adaptive learning skill for [Garry Tan's gstack](https://github.com/garrytan/gstack) — a 21-skill Claude Code workflow system.

## What this does

- **Teaches** you gstack skills interactively, tracking what you've learned
- **Auto-syncs** with garrytan/gstack daily via GitHub Actions
- **Tracks progress** per skill (unseen → introduced → practiced → mastered)
- **Never re-teaches** mastered skills unless they changed upstream

## Install

### OpenClaw
```bash
git clone https://github.com/YOUR_ORG/gstack-course.git ~/.openclaw/skills/gstack-course
```

### Claude Code
```bash
git clone https://github.com/YOUR_ORG/gstack-course.git ~/.claude/skills/gstack-course
```

### Codex
```bash
git clone https://github.com/YOUR_ORG/gstack-course.git ~/.codex/skills/gstack-course
```

## Usage

Just ask your agent:
- "Which gstack skill should I use?"
- "Teach me /office-hours"
- "What's new in gstack?"
- "Show my gstack progress"

## How updates work

A GitHub Actions workflow runs daily:
1. Checks garrytan/gstack for new commits
2. Regenerates `references/skills-catalog.md` and `references/skill-index.json`
3. Bumps the version
4. Commits and pushes

Your local install just needs `git pull` to get the latest.

## Structure

```
gstack-course/
├── SKILL.md                          # Main skill (loaded by agent)
├── version.json                      # Current version
├── references/
│   ├── skills-catalog.md             # Auto-generated skill descriptions
│   ├── skill-index.json              # Machine-readable skill index
│   ├── workflow-patterns.md          # Sprint patterns and combos
│   └── upstream-sha.txt              # Last synced gstack commit
├── scripts/
│   ├── generate-catalog.py           # Builds catalog from gstack SKILL.md files
│   └── bump-version.py               # Version management
└── .github/workflows/
    └── sync-gstack.yml               # Daily sync workflow
```

Progress is stored locally at `~/.gstack-course/progress.json` (never committed).

## License

MIT
