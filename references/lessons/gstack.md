# Lesson: `/gstack`

> Sprint phase: **Other** | Template: 281 lines | Version: 1.1.0
> Source: `garrytan/gstack/gstack/SKILL.md.tmpl`

## What Is This?

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.
~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a
user flow, or file a bug with evidence.
gstack also includes development workflow skills. When you notice the user is at
these stages, suggest the appropriate skill:
- Brainstorming a new idea → suggest /office-hours
- Reviewing a plan (strategy) → suggest /plan-ceo-review
- Reviewing a plan (architecture) → suggest /plan-eng-review
- Reviewing a plan (design) → suggest /plan-design-review
- Creating a design system → suggest /design-consultation
- Debugging errors → suggest /investigate
- Testing the app → suggest /qa
- Code review before merge → suggest /review
- Visual design audit → suggest /design-review
- Ready to deploy / create PR → suggest /ship
- Post-ship doc updates → suggest /document-release
- Weekly retrospective → suggest /retro
- Wanting a second opinion or adversarial code review → suggest /codex
- Working with production or live systems → suggest /careful
- Want to scope edits to one module/directory → suggest /freeze
- Maximum safety mode (destructive warnings + edit restrictions) → suggest /guard
- Removing edit restrictions → suggest /unfreeze
- Upgrading gstack to latest version → suggest /gstack-upgrade
If the user pushes back on skill suggestions ("stop suggesting things",
"I don't need suggestions", "too aggressive"):
1. Stop suggesting for the rest of this session
2. Run: gstack-config set proactive false
3. Say: "Got it — I'll stop suggesting skills. Just tell me to be proactive
again if you change your mind."
If the user says "be proactive again" or "turn on suggestions":
1. Run: gstack-config set proactive true
2. Say: "Proactive suggestions are back on."

## When Do You Use It?

- ~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a

## What Do You Say to Claude?

Type `/gstack` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "stop suggesting things"
- "I don't need suggestions"
- "too aggressive"
- "Got it — I'll stop suggesting skills. Just tell me to be proactive
   again if you change your mind."
- "be proactive again"
- "turn on suggestions"

## What Will Claude Ask You?

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

Structured output for the **Other** phase of your sprint.

## The Workflow

**Step 1: gstack browse: QA Testing & Dogfooding**
> Persistent headless Chromium. First call auto-starts (~3s), then ~100-200ms per command.

**Step 2: IMPORTANT**

**Step 3: QA Workflows**

**Step 4: 1. Go to the page**
> $B goto https://app.example.com/login

**Step 5: 2. See what's interactive**

**Step 6: 3. Fill the form using refs**
> $B fill @e3 "test@example.com"

**Step 7: 4. Verify it worked**
> $B snapshot -D              # diff shows what changed after clicking

**Step 8: Navigate to the feature**
> $B goto https://app.example.com/new-feature

**Step 9: Take annotated screenshot — shows every interactive element with labels**
> $B snapshot -i -a -o /tmp/feature-annotated.png

**Step 10: Find ALL clickable things (including divs with cursor:pointer)**

**Step 11: Walk through the flow**
> $B snapshot -i          # baseline

**Step 12: Check element states**
> $B is visible ".success-toast"

**Step 13: Check console for errors after interactions**

**Step 14: Quick: 3 screenshots at mobile/tablet/desktop**
> $B goto https://yourapp.com

**Step 15: Manual: specific viewport**
> $B viewport 375x812     # iPhone

**Step 16: Element screenshot (crop to specific element)**
> $B screenshot "#hero-banner" /tmp/hero.png

**Step 17: Region crop**
> $B screenshot --clip 0,0,800,600 /tmp/above-fold.png

**Step 18: Viewport only (no scroll)**
> $B screenshot --viewport /tmp/viewport.png

**Step 19: Submit empty — check validation errors appear**
> $B click @e10                        # submit button

**Step 20: Fill and resubmit**
> $B fill @e3 "valid input"

**Step 21: Set up dialog handling BEFORE triggering**
> $B dialog-accept              # will auto-accept next alert/confirm

**Step 22: For prompts that need input**
> $B dialog-accept "my answer"  # accept with text

**Step 23: Import cookies from your real browser (opens interactive picker)**
> $B cookie-import-browser

**Step 24: Or import a specific domain directly**
> $B cookie-import-browser comet --domain .github.com

**Step 25: Now test authenticated pages**
> $B goto https://github.com/settings/profile

**Step 26: Quick Assertion Patterns**

**Step 27: Element exists and is visible**
> $B is visible ".modal"

**Step 28: Button is enabled/disabled**
> $B is enabled "#submit-btn"

**Step 29: Checkbox state**
> $B is checked "#agree"

**Step 30: Input is editable**
> $B is editable "#name-field"

**Step 31: Element has focus**
> $B is focused "#search-input"

**Step 32: Page contains text**
> $B js "document.body.textContent.includes('Success')"

**Step 33: Element count**
> $B js "document.querySelectorAll('.list-item').length"

**Step 34: Specific attribute value**
> $B attrs "#logo"    # returns all attributes as JSON

**Step 35: CSS property**
> $B css ".button" "background-color"

**Step 36: Snapshot System**
> {{SNAPSHOT_FLAGS}}

**Step 37: Command Reference**
> {{COMMAND_REFERENCE}}

**Step 38: Tips**
> 1. **Navigate once, query many times.** `goto` loads the page; then `text`, `js`, `screenshot` all hit the loaded page instantly.

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
