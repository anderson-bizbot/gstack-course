# gstack Workflow Patterns

## The Full Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] →
/review → /qa → /ship → /document-release → /retro
```

Each skill reads what the previous one wrote. ~30 min per sprint. Run 10-15 in parallel.

---

## Common Patterns

### Quick Fix (bug → ship)
`/investigate → [fix] → /review → /qa → /ship`

### New Feature (idea → ship)
`/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /document-release`

### Design-Heavy Feature
`/office-hours → /plan-ceo-review → /plan-design-review → /design-consultation → [build] → /design-review → /qa → /ship`

### Production Hotfix (safety mode)
`/guard → /investigate → [fix] → /review → /qa → /ship → /unfreeze`

### Audit Only (no changes)
`/qa-only → [read report] → file issues`

### Parallel Sprints
Multiple CC sessions on different branches. This is how Garry hits 10-20k lines/day.

---

## Anti-Patterns

- **Skipping /office-hours** — catches 80% of scope mistakes via reframing
- **Skipping /review before /ship** — /review catches logic bugs CI misses
- **Using /qa without a running app** — deploy to localhost/staging first
- **Never running /retro** — lose the feedback loop on your process

## Chaining Rules

- `/office-hours` writes design doc → `/plan-ceo-review` reads it
- `/plan-eng-review` writes test plan → `/qa` picks it up
- `/review` marks AUTO-FIX vs ASK → you only decide ASK items
- `/ship` runs tests + review → opens PR verified
- `/document-release` reads ship diff → updates matching docs
