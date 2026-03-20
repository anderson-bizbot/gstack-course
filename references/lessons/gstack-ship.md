# Lesson: `/ship`

> Sprint phase: **Ship** | Size: 54,822 bytes
> Source: `garrytan/gstack/.agents/skills/gstack-ship/SKILL.md`

## What Is This?

Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "create a PR", or "merge and push".
Proactively suggest when the user says code is ready or asks about deploying.

## When Do You Use It?

- Ship workflow: detect + merge base branch, run tests, review diff, bump VERSION, update CHANGELOG, commit, push, create PR. Use when asked to "ship", "deploy", "push to main", "create a PR", or "merge and push".
- Proactively suggest when the user says code is ready or asks about deploying.

## What Do You Say to Claude?

Type `/ship` in Claude Code. That's it. The skill takes over from there.

**Trigger phrases that also work:**
- "ship"
- "deploy"
- "push to main"
- "create a PR"
- "merge and push"

## What Will Claude Ask You?

Claude will walk you through a structured conversation. Key questions include:

- *"I couldn't detect your project's language. What runtime are you using?"*
- *"GStack recommends maintaining a TODOS.md organized by skill/component, then priority (P0 at top through P4, then Completed at bottom). See TODOS-format.md for the full format. Would you like to create one?"*
- *"TODOS.md doesn't follow the recommended structure (skill/component groupings, P0-P4 priority, Completed section). Would you like to reorganize it?"*

## What Do You Get?

- **Raw output**
- **Eval Results**

## The Workflow (Step by Step)

1. **Steps to reproduce**
   1. {step}

2. **Raw output**
   {paste the actual error or unexpected output here}

3. **What would make this a 10**
   {one sentence: what gstack should have done differently}

4. **Step 0: Detect base branch**
   Determine which branch this PR targets. Use the result as "the base branch" in all subsequent steps.

5. **Ship: Fully Automated Ship Workflow**
   You are running the `/ship` workflow. This is a **non-interactive, fully automated** workflow. Do NOT ask for confirmation at any step. The user said 

6. **Step 1: Pre-flight**
   1. Check the current branch. If on the base branch or the repo's default branch, **abort**: "You're on the base branch. Ship from a feature branch."

7. **Review Readiness Dashboard**
   After completing the review, read the review log and config to display the dashboard.

8. **Step 2: Merge the base branch (BEFORE tests)**
   Fetch and merge the base branch into the feature branch so tests run against the merged state:

9. **Step 2.5: Test Framework Bootstrap**

10. **Test Framework Bootstrap**
   **Detect existing test framework and project runtime:**

11. **Detect project runtime**
   [ -f Gemfile ] && echo "RUNTIME:ruby"

12. **Detect sub-frameworks**
   [ -f Gemfile ] && grep -q "rails" Gemfile 2>/dev/null && echo "FRAMEWORK:rails"

13. **Check for existing test infrastructure**
   ls jest.config.* vitest.config.* playwright.config.* .rspec pytest.ini pyproject.toml phpunit.xml 2>/dev/null

14. **Check opt-out marker**
   [ -f .gstack/no-test-bootstrap ] && echo "BOOTSTRAP_DECLINED"

15. **Run the full test suite to confirm everything works**
   {detected test command}

16. **Check CI provider**
   ls -d .github/ 2>/dev/null && echo "CI:github"

17. **Step 3: Run tests (on merged code)**
   **Do NOT run `RAILS_ENV=test bin/rails db:migrate`** — `bin/test-lane` already calls

18. **Step 3.25: Eval Suites (conditional)**
   Evals are mandatory when prompt-related files change. Skip this step entirely if no prompt files are in the diff.

19. **Step 3.4: Test Coverage Audit**
   100% coverage is the goal — every untested path is a path where bugs hide and vibe coding becomes yolo coding. Evaluate what was ACTUALLY coded (from 

20. **Count test files before any generation**
   find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec.*' | grep -v node_modules | wc -l

21. **Count test files after generation**
   find . -name '*.test.*' -o -name '*.spec.*' -o -name '*_test.*' -o -name '*_spec.*' | grep -v node_modules | wc -l

22. **Step 3.5: Pre-Landing Review**
   Review the diff for structural issues that tests don't catch.

23. **Design Review (conditional, diff-scoped)**
   Check if the diff touches frontend files using `gstack-diff-scope`:

24. **Step 3.75: Address Greptile review comments (if PR exists)**
   Read `.agents/skills/gstack/review/greptile-triage.md` and follow the fetch, filter, classify, and **escalation detection** steps.

25. **Step 4: Version bump (auto-decide)**
   1. Read the current `VERSION` file (4-digit format: `MAJOR.MINOR.PATCH.MICRO`)

26. **Step 5: CHANGELOG (auto-generate)**
   1. Read `CHANGELOG.md` header to know the format.

27. **Step 5.5: TODOS.md (auto-update)**
   Cross-reference the project's TODOS.md against the changes being shipped. Mark completed items automatically; prompt only if the file is missing or di

28. **Step 6: Commit (bisectable chunks)**
   **Goal:** Create small, logical commits that work well with `git bisect` and help LLMs understand what changed.

29. **Step 6.5: Verification Gate**
   **IRON LAW: NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

30. **Step 7: Push**
   Push to the remote with upstream tracking:

31. **Step 8: Create PR**
   Create a pull request using `gh`:

32. **Summary**
   <bullet points from CHANGELOG>

33. **Test Coverage**
   <coverage diagram from Step 3.4, or "All new code paths have test coverage.">

34. **Pre-Landing Review**
   <findings from Step 3.5 code review, or "No issues found.">

35. **Design Review**
   <If design review ran: "Design Review (lite): N findings — M auto-fixed, K skipped. AI Slop: clean/N issues.">

36. **Eval Results**
   <If evals ran: suite names, pass/fail counts, cost dashboard summary. If skipped: "No prompt-related files changed — evals skipped.">

37. **Greptile Review**
   <If Greptile comments were found: bullet list with [FIXED] / [FALSE POSITIVE] / [ALREADY FIXED] tag + one-line summary per comment>

38. **TODOS**
   <If items marked complete: bullet list of completed items with version>

39. **Test plan**
   🤖 Generated with [Claude Code](https://claude.com/claude-code)

40. **Step 8.5: Auto-invoke /document-release**
   After the PR is created, automatically sync project documentation. Read the

41. **Important Rules**

## Where It Fits in the Sprint

```
/office-hours → /plan-ceo-review → /plan-eng-review → [build] → /review → /qa → >>>/ship<<< → /retro
```

## What Comes Next?

- `/document-release`
- `/retro`

## Pro Tips

- Run this skill before moving to the next sprint phase
- The output feeds automatically into downstream skills
