# Lesson: `/gstack`

> Sprint phase: **Other** | Size: 26,233 bytes
> Source: `garrytan/gstack/.agents/skills/gstack/SKILL.md`

## What Is This?

Fast headless browser for QA testing and site dogfooding. Navigate any URL, interact with
elements, verify page state, diff before/after actions, take annotated screenshots, check
responsive layouts, test forms and uploads, handle dialogs, and assert element states.

## When Do You Use It?

- ~100ms per command. Use when you need to test a feature, verify a deployment, dogfood a

## What Do You Say to Claude?

Type `/gstack` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "stop suggesting things"
- "I don't need suggestions"
- "too aggressive"
- "Got it — I'll stop suggesting skills. Just tell me to be proactive
   again if you change your mind."
- "be proactive again"
- "turn on suggestions"
- "Proactive suggestions are back on."

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*

## What Do You Get?

- **Raw output**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

5. **IMPORTANT**

6. **QA Workflows**

7. **1. Go to the page**
   $B goto https://app.example.com/login

8. **2. See what's interactive**
   $B snapshot -i

9. **3. Fill the form using refs**
   $B fill @e3 "test@example.com"

10. **4. Verify it worked**
   $B snapshot -D              # diff shows what changed after clicking

11. **Navigate to the feature**
   $B goto https://app.example.com/new-feature

12. **Take annotated screenshot — shows every interactive element with labels**
   $B snapshot -i -a -o /tmp/feature-annotated.png

13. **Find ALL clickable things (including divs with cursor:pointer)**
   $B snapshot -C

14. **Walk through the flow**
   $B snapshot -i          # baseline

15. **Check element states**
   $B is visible ".success-toast"

16. **Check console for errors after interactions**
   $B console

17. **Quick: 3 screenshots at mobile/tablet/desktop**
   $B goto https://yourapp.com

18. **Manual: specific viewport**
   $B viewport 375x812     # iPhone

19. **Element screenshot (crop to specific element)**
   $B screenshot "#hero-banner" /tmp/hero.png

20. **Region crop**
   $B screenshot --clip 0,0,800,600 /tmp/above-fold.png

21. **Viewport only (no scroll)**
   $B screenshot --viewport /tmp/viewport.png

22. **Submit empty — check validation errors appear**
   $B click @e10                        # submit button

23. **Fill and resubmit**
   $B fill @e3 "valid input"

24. **Set up dialog handling BEFORE triggering**
   $B dialog-accept              # will auto-accept next alert/confirm

25. **For prompts that need input**
   $B dialog-accept "my answer"  # accept with text

26. **Import cookies from your real browser (opens interactive picker)**
   $B cookie-import-browser

27. **Or import a specific domain directly**
   $B cookie-import-browser comet --domain .github.com

28. **Now test authenticated pages**
   $B goto https://github.com/settings/profile

29. **Quick Assertion Patterns**

30. **Element exists and is visible**
   $B is visible ".modal"

31. **Button is enabled/disabled**
   $B is enabled "#submit-btn"

32. **Checkbox state**
   $B is checked "#agree"

33. **Input is editable**
   $B is editable "#name-field"

34. **Element has focus**
   $B is focused "#search-input"

35. **Page contains text**
   $B js "document.body.textContent.includes('Success')"

36. **Element count**
   $B js "document.querySelectorAll('.list-item').length"

37. **Specific attribute value**
   $B attrs "#logo"    # returns all attributes as JSON

38. **CSS property**
   $B css ".button" "background-color"

39. **Snapshot System**
   The snapshot is your primary tool for understanding and interacting with pages.

40. **Command Reference**

41. **Tips**
   1. **Navigate once, query many times.** `goto` loads the page; then `text`, `js`, `screenshot` all hit the loaded page instantly.

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `See workflow patterns`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
