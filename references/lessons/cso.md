# Lesson: `/cso`

> Sprint phase: **Other** | Template: 621 lines | Version: 2.0.0
> Source: `garrytan/gstack/cso/SKILL.md.tmpl`

## What Is This?

Chief Security Officer mode. Infrastructure-first security audit: secrets archaeology,
dependency supply chain, CI/CD pipeline security, LLM/AI security, skill supply chain
scanning, plus OWASP Top 10, STRIDE threat modeling, and active verification.
Two modes: daily (zero-noise, 8/10 confidence gate) and comprehensive (monthly deep
scan, 2/10 bar). Trend tracking across audit runs.

## When Do You Use It?

- Use when: "security audit", "threat model", "pentest review", "OWASP", "CSO review".

## What Do You Say to Claude?

Type `/cso` in Claude Code. The skill activates and guides you.

**Natural language triggers:**
- "security audit"
- "threat model"
- "pentest review"
- "OWASP"
- "CSO review"

## What Will Claude Ask You?

Claude walks you through a structured conversation:

- *"Phase 8 can scan your globally installed AI coding agent skills and hooks for malicious patterns. This reads files outside the repo. Want to include this?"*

## What Do You Get?

- Phase 13: Findings Report + Trend Tracking + Remediation
- Phase 14: Save Report

## The Workflow

**Step 1: /cso — Chief Security Officer Audit (v2)**
> You are a **Chief Security Officer** who has led incident response on real breaches and testified before boards about security posture. You think like an attacker but report like a defender. You don't...

**Step 2: User-invocable**
> When the user types `/cso`, run this skill.

**Step 3: Arguments**

**Step 4: Mode Resolution**
> 1. If no flags → run ALL phases 0-14, daily mode (8/10 confidence gate).

**Step 5: Important: Use the Grep tool for all code searches**
> The bash blocks throughout this skill show WHAT patterns to search for, not HOW to run them. Use Claude Code's Grep tool (which handles permissions and access correctly) rather than raw bash grep. The...

**Step 6: Instructions**

**Step 7: Sev    Conf   Status      Category         Finding                          Phase   File:Line**
> ──  ────   ────   ──────      ────────         ───────                          ─────   ─────────

**Step 8: Finding N: [Title] — [File:Line]**
> * **Severity:** CRITICAL | HIGH | MEDIUM

**Step 9: Important Rules**

**Step 10: Disclaimer**
> **This tool is not a substitute for a professional security audit.** /cso is an AI-assisted

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
