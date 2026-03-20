# Lesson: `/qa`

> Sprint phase: **Test** | Size: 41,814 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-qa/SKILL.md`

## What Is This?

Systematically QA test a web application and fix bugs found. Runs QA testing,
then iteratively fixes bugs in source code, committing each fix atomically and
re-verifying. Use when asked to "qa", "QA", "test this site", "find bugs",

## When Do You Use It?

- re-verifying. Use when asked to "qa", "QA", "test this site", "find bugs",
- Proactively suggest when the user says a feature is ready for testing

## What Do You Say to Claude?

Type `/qa` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "qa"
- "QA"
- "test this site"
- "find bugs"
- "test and fix"
- "fix what's broken"
- "does this work?"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"gstack browse needs a one-time build (~10 seconds). OK to proceed?"*
- *"I couldn't detect your project's language. What runtime are you using?"*

## What Do You Get?

- **Raw output**
- **Output Structure**
- **Phase 10: Report**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Step 0: Detect base branch**
   Determine which branch this PR targets. Use the result as "the base branch" in all subsequent steps.

5. **/qa: Test → Fix → Verify**
   You are a QA engineer AND a bug-fix engineer. Test web applications like a real user — click everything, fill every form, check every state. When you 

6. **Setup**
   **Parse the user's request for these parameters:**

7. **SETUP (run this check BEFORE any browse command)**
   _ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

8. **Test Framework Bootstrap**
   **Detect existing test framework and project runtime:**

9. **Detect project runtime**
   [ -f Gemfile ] && echo "RUNTIME:ruby"

10. **Detect sub-frameworks**
   [ -f Gemfile ] && grep -q "rails" Gemfile 2>/dev/null && echo "FRAMEWORK:rails"

11. **Check for existing test infrastructure**
   ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject.toml phpunit.xml 2>/dev/null

12. **Check opt-out marker**
   [ -f .gstack/no-test-bootstrap ] && echo "BOOTSTRAP_DECLINED"

13. **Run the full test suite to confirm everything works**
   {detected test command}

14. **Check CI provider**
   ls -d .github/ 2>/dev/null && echo "CI:github"

15. **Test Plan Context**
   Before falling back to git diff heuristics, check for richer test plan sources:

16. **Phases 1-6: QA Baseline**

17. **Modes**

18. **Workflow**

19. **Health Score Rubric**
   Compute each category score (0-100), then take the weighted average.

20. **Framework-Specific Guidance**

21. **Important Rules**
   1. **Repro is everything.** Every issue needs at least one screenshot. No exceptions.

22. **Output Structure**
   .gstack/qa-reports/

23. **Phase 7: Triage**
   Sort all discovered issues by severity, then decide which to fix based on the selected tier:

24. **Phase 8: Fix Loop**
   For each fixable issue, in severity order:

25. **Grep for error messages, component names, route definitions**

26. **Glob for file patterns matching the affected page**

27. **Phase 9: Final QA**
   After all fixes are applied:

28. **Phase 10: Report**
   Write the report to both local and project-scoped locations:

29. **Phase 11: TODOS.md Update**
   If the repo has a `TODOS.md`:

30. **Additional Rules (qa-specific)**
   11. **Clean working tree required.** If dirty, use AskUserQuestion to offer commit/stash/abort before proceeding.

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → >>>/qa<<< → /ship → /retro
```

## What Comes Next?

- `/ship`
- `/review`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
