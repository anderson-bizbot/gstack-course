# Lesson: `/codex`

> Sprint phase: **Other** | Template: 357 lines | Version: 1.0.0
> Source: `garrytan/gstack/codex/SKILL.md.tmpl`

## What Is This?

OpenAI Codex CLI wrapper — three modes. Code review: independent diff review via
codex review with pass/fail gate. Challenge: adversarial mode that tries to break
your code. Consult: ask codex anything with session continuity for follow-ups.
The "200 IQ autistic developer" second opinion. Use when asked to "codex review",
"codex challenge", "ask codex", "second opinion", or "consult codex".

## When Do You Use It?

- The "200 IQ autistic developer" second opinion. Use when asked to "codex review",

## What Do You Say to Claude?

Type `/codex` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "200 IQ autistic developer"
- "codex review"
- "codex challenge"
- "ask codex"
- "second opinion"
- "consult codex"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"What would you like to ask Codex?"*

## What Do You Get?

Structured output for the **Other** phase of your sprint.

## The Workflow

**Step 1: /codex — Multi-AI Second Opinion**
> You are running the `/codex` skill. This wraps the OpenAI Codex CLI to get an independent,

**Step 2: Step 0: Check codex binary**
> CODEX_BIN=$(which codex 2>/dev/null || echo "")

**Step 3: Step 1: Detect mode**
> Parse the user's input to determine which mode to run:

**Step 4: Step 2A: Review Mode**
> Run Codex code review against the current branch diff.

**Step 5: Step 2B: Challenge (Adversarial) Mode**
> Codex tries to break your code — finding edge cases, race conditions, security holes,

**Step 6: Step 2C: Consult Mode**
> Ask Codex anything about the codebase. Supports session continuity for follow-ups.

**Step 7: Model & Reasoning**
> **Model:** No model is hardcoded — codex uses whatever its current default is (the frontier

**Step 8: Cost Estimation**
> Parse token count from stderr. Codex prints `tokens used\nN` to stderr.

**Step 9: Error Handling**
> "Codex authentication failed. Run `codex login` in your terminal to authenticate via ChatGPT."

**Step 10: Important Rules**
> before showing it. Show it in full inside the CODEX SAYS block.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
