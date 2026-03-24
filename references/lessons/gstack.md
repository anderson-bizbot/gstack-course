# Lesson: `/gstack`

> Sprint phase: **Other** | Template: 257 lines | Version: 1.1.0
> Source: `garrytan/gstack/gstack/SKILL.md.tmpl`

## What Is This?

Fast headless browser for QA testing and site dogfooding. Navigate pages, interact with
elements, verify state, diff before/after, take annotated screenshots, test responsive
layouts, forms, uploads, dialogs, and capture bug evidence. Use when asked to open or
test a site, verify a deployment, dogfood a user flow, or file a bug with screenshots.
Also suggest adjacent gstack skills by stage: brainstorm /office-hours; strategy
/plan-ceo-review; architecture /plan-eng-review; design /plan-design-review or
/design-consultation; auto-review /autoplan; debugging /investigate; QA /qa; code review
/review; visual audit /design-review; shipping /ship; docs /document-release; retro
/retro; second opinion /codex; prod safety /careful or /guard; scoped edits /freeze or
/unfreeze; gstack upgrades /gstack-upgrade. If the user opts out of suggestions, stop
and run gstack-config set proactive false; if they opt back in, run gstack-config set
proactive true.

## When Do You Use It?

- layouts, forms, uploads, dialogs, and capture bug evidence. Use when asked to open or

## What Do You Say to Claude?

Type `/gstack` in Claude Code. The skill activates and guides you.

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
