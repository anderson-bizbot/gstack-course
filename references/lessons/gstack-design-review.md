# Lesson: `/design-review`

> Sprint phase: **Review** | Size: 44,283 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-design-review/SKILL.md`

## What Is This?

Designer's eye QA: finds visual inconsistency, spacing issues, hierarchy problems,
AI slop patterns, and slow interactions — then fixes them. Iteratively fixes issues
in source code, committing each fix atomically and re-verifying with before/after

## When Do You Use It?

- Use when asked to "audit the design", "visual QA", "check if it looks good", or "design polish".
- Proactively suggest when the user mentions visual inconsistencies or

## What Do You Say to Claude?

Type `/design-review` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "audit the design"
- "visual QA"
- "check if it looks good"
- "design polish"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*
- *"I couldn't detect your project's language. What runtime are you using?"*
- *"What if we moved search to a more prominent position?"*

## What Do You Get?

- **Raw output**
- **Phase 6: Compile Report**
- **Output Locations**
- **Regression Output**
- **Output Structure**
- **Phase 10: Report**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Setup**
   **Parse the user's request for these parameters:**

5. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

6. **Test Framework Bootstrap**
   **Detect existing test framework and project runtime:**

7. **Detect project runtime**
   [ -f Gemfile ] && echo "RUNTIME:ruby"

8. **Detect sub-frameworks**
   [ -f Gemfile ] && grep -q "rails" Gemfile 2>/dev/null && echo "FRAMEWORK:rails"

9. **Check for existing test infrastructure**
   ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject.toml phpunit.xml 2>/dev/null

10. **Check opt-out marker**
   [ -f .gstack/no-test-bootstrap ] && echo "BOOTSTRAP_DECLINED"

11. **Run the full test suite to confirm everything works**
   {detected test command}

12. **Check CI provider**
   ls -d .github/ 2>/dev/null && echo "CI:github"

13. **Phases 1-6: Design Audit Baseline**

14. **Modes**

15. **Phase 1: First Impression**
   The most uniquely designer-like output. Form a gut reaction before analyzing anything.

16. **Phase 2: Design System Extraction**
   Extract the actual design system the site uses (not what a DESIGN.md says, but what's rendered):

17. **Fonts in use (capped at 500 elements to avoid timeout)**
   $B js "JSON.stringify([...new Set([...document.querySelectorAll('*')].slice(0,500).map(e => getComputedStyle(e).fontFamily))])"

18. **Color palette in use**
   $B js "JSON.stringify([...new Set([...document.querySelectorAll('*')].slice(0,500).flatMap(e => [getComputedStyle(e).color, getComputedStyle(e).backgr

19. **Heading hierarchy**
   $B js "JSON.stringify([...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => ({tag:h.tagName, text:h.textContent.trim().slice(0,50), size:getCom

20. **Touch target audit (find undersized interactive elements)**
   $B js "JSON.stringify([...document.querySelectorAll('a,button,input,[role=button]')].filter(e => {const r=e.getBoundingClientRect(); return r.width>0 

21. **Performance baseline**
   $B perf

22. **Phase 3: Page-by-Page Visual Audit**
   For each page in scope:

23. **Phase 4: Interaction Flow Review**
   Walk 2-3 key user flows and evaluate the *feel*, not just the function:

24. **Phase 5: Cross-Page Consistency**
   Compare screenshots and observations across pages for:

25. **Phase 6: Compile Report**

26. **Design Critique Format**
   Use structured feedback, not opinions:

27. **Important Rules**
   1. **Think like a designer, not a QA engineer.** You care whether things feel right, look intentional, and respect the user. You do NOT just care whet

28. **Output Structure**
   .gstack/design-reports/

29. **Phase 7: Triage**
   Sort all discovered findings by impact, then decide which to fix:

30. **Phase 8: Fix Loop**
   For each fixable finding, in impact order:

31. **Search for CSS classes, component names, style files**

32. **Glob for file patterns matching the affected page**

33. **Phase 9: Final Design Audit**
   After all fixes are applied:

34. **Phase 10: Report**
   Write the report to both local and project-scoped locations:

35. **Phase 11: TODOS.md Update**
   If the repo has a `TODOS.md`:

36. **Additional Rules (design-review specific)**
   11. **Clean working tree required.** If dirty, use AskUserQuestion to offer commit/stash/abort before proceeding.

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → /ship → /retro
```

## What Comes Next?

- `/qa`
- `/ship`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
