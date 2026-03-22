# Lesson: `/cso`

> Sprint phase: **Other** | Template: 377 lines | Version: 1.0.0
> Source: `garrytan/gstack/cso/SKILL.md.tmpl`

## What Is This?

Chief Security Officer mode. Performs OWASP Top 10 audit, STRIDE threat modeling,
attack surface analysis, auth flow verification, secret detection, dependency CVE
scanning, supply chain risk assessment, and data classification review.

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

This skill runs mostly automatically — you provide initial context and Claude handles the rest.

## What Do You Get?

- Phase 6: Findings Report
- Phase 8: Save Report

## The Workflow

**Step 1: /cso — Chief Security Officer Audit**
> You are a **Chief Security Officer** who has led incident response on real breaches and testified before boards about security posture. You think like an attacker but report like a defender. You don't...

**Step 2: User-invocable**
> When the user types `/cso`, run this skill.

**Step 3: Arguments**

**Step 4: Instructions**

**Step 5: Endpoints and routes (REST, GraphQL, gRPC, WebSocket)**
> grep -rn "get \|post \|put \|patch \|delete \|route\|router\." --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" --include="*.go" --include="*.java" --include="*.php" --include="*.cs...

**Step 6: Authentication boundaries**
> grep -rn "authenticate\|authorize\|before_action\|middleware\|jwt\|session\|cookie" --include="*.rb" --include="*.js" --include="*.ts" --include="*.go" --include="*.java" --include="*.py" -l | head -2...

**Step 7: External integrations (attack surface expansion)**
> grep -rn "http\|https\|fetch\|axios\|Faraday\|RestClient\|Net::HTTP\|urllib\|http\.Get\|http\.Post\|HttpClient" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" --include="*.go" --i...

**Step 8: File upload/download paths**
> grep -rn "upload\|multipart\|file.*param\|send_file\|send_data\|attachment" --include="*.rb" --include="*.js" --include="*.ts" --include="*.go" --include="*.java" -l | head -10

**Step 9: Admin/privileged routes**
> grep -rn "admin\|superuser\|root\|privilege" --include="*.rb" --include="*.js" --include="*.ts" --include="*.go" --include="*.java" -l | head -10

**Step 10: Check for missing auth on controllers/routes**
> grep -rn "skip_before_action\|skip_authorization\|public\|no_auth" --include="*.rb" --include="*.js" --include="*.ts" -l

**Step 11: Check for direct object reference patterns**
> grep -rn "params\[:id\]\|params\[.id.\]\|req.params.id\|request.args.get" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -20

**Step 12: Weak crypto / hardcoded secrets**
> grep -rn "MD5\|SHA1\|DES\|ECB\|hardcoded\|password.*=.*[\"']" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -20

**Step 13: Encryption at rest**
> grep -rn "encrypt\|decrypt\|cipher\|aes\|rsa" --include="*.rb" --include="*.js" --include="*.ts" -l

**Step 14: SQL injection vectors**
> grep -rn "where(\"\|execute(\"\|raw(\"\|find_by_sql\|\.query(" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -20

**Step 15: Command injection vectors**
> grep -rn "system(\|exec(\|spawn(\|popen\|backtick\|\`" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -20

**Step 16: Template injection**
> grep -rn "render.*params\|eval(\|safe_join\|html_safe\|raw(" --include="*.rb" --include="*.js" --include="*.ts" | head -20

**Step 17: LLM prompt injection**
> grep -rn "prompt\|system.*message\|user.*input.*llm\|completion" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -20

**Step 18: CORS configuration**
> grep -rn "cors\|Access-Control\|origin" --include="*.rb" --include="*.js" --include="*.ts" --include="*.yaml" | head -10

**Step 19: CSP headers**
> grep -rn "Content-Security-Policy\|CSP\|content_security_policy" --include="*.rb" --include="*.js" --include="*.ts" | head -10

**Step 20: Debug mode / verbose errors in production**
> grep -rn "debug.*true\|DEBUG.*=.*1\|verbose.*error\|stack.*trace" --include="*.rb" --include="*.js" --include="*.ts" --include="*.yaml" | head -10

**Step 21: Check for known vulnerable versions**
> cat Gemfile.lock 2>/dev/null | head -50

**Step 22: Audit logging**
> grep -rn "audit\|security.*log\|auth.*log\|access.*log" --include="*.rb" --include="*.js" --include="*.ts" -l

**Step 23: URL construction from user input**
> grep -rn "URI\|URL\|fetch.*param\|request.*url\|redirect.*param" --include="*.rb" --include="*.js" --include="*.ts" --include="*.py" | head -15

**Step 24: Sev    Conf   Category         Finding                          OWASP   File:Line**
> ──  ────   ────   ────────         ───────                          ─────   ─────────

**Step 25: Finding 1: [Title] — [File:Line]**
> * **Severity:** CRITICAL | HIGH | MEDIUM

**Step 26: Important Rules**

**Step 27: Disclaimer**
> **This tool is not a substitute for a professional security audit.** /cso is an AI-assisted

## Where It Fits

```
Think → Plan → Build → Review → Test → Ship
                    ↑
        You are here: OTHER phase
```

## What Comes Next?

- Continue with the next sprint phase.
