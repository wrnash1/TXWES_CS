# Video Script: Module 06 - SAST: Static Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 06 — SAST: Static Application Security Testing"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. This module covers SAST — Static Application Security Testing — which is the most widely integrated automated security control in DevSecOps pipelines.

SAST is the workhorse of the shift-left movement. It runs at the commit or pull request stage — before any code is deployed, before any tests run — and it analyzes your source code for vulnerability patterns. By the end of this video you'll be able to explain how SAST works mechanically, compare the major SAST tools, integrate Semgrep into a GitHub Actions pipeline, and — critically — analyze a real SAST finding and describe the vulnerability and its remediation. That analysis skill is directly tested in this module's lab and on the DevSecOps Professional exam."

---

### [01:30 - 06:00] How SAST Works: Data Flow and Pattern Analysis

**Visual:** Code snippet with annotated taint flow from user input to SQL query

**Audio:**

"Let's start with how SAST actually works under the hood, because understanding the mechanism helps you understand its strengths and limitations.

SAST tools analyze source code — or compiled bytecode or binaries — without executing the program. They use two primary analysis techniques.

The first is pattern matching. Simple SAST tools use regular expressions or abstract syntax tree (AST) analysis to find known dangerous patterns: string concatenation in SQL queries, `eval()` calls with user input, `innerHTML` assignments, hardcoded password strings, and similar anti-patterns. Semgrep is primarily a pattern-matching tool with a rich, community-contributed rule library.

The second and more powerful technique is taint analysis, also called data flow analysis. Taint analysis tracks the flow of untrusted data — 'tainted' data from user input, API parameters, database reads, file reads — through the code, looking for paths where that tainted data reaches a dangerous 'sink' — a SQL query, a shell command, a file write, an HTML output function — without being properly sanitized or validated along the way.

**[SHOW CODE]**

Here is a concrete example. Consider this Python Flask route:

```python
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # SQL Injection: untrusted user_id directly concatenated into query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return str(cursor.fetchall())
```

A taint analysis SAST tool traces: `user_id` ← `request.args.get('id')` (source: HTTP request parameter — untrusted). Then: `query` ← f-string with `user_id` (taint propagates). Then: `cursor.execute(query)` (sink: SQL execution). No sanitization in between. Result: SQL injection finding, severity CRITICAL.

A pattern-matching tool finds this by recognizing the `f"SELECT ... {variable}"` pattern as SQL string concatenation.

The remediation: use parameterized queries.

```python
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

The `?` placeholder with a separate parameter tuple is handled by the database driver, which treats the parameter as data, not as SQL syntax. Injection is impossible."

---

### [06:00 - 11:00] SAST Tools: Semgrep, SonarQube, Checkmarx

**Visual:** Tool comparison table on screen

**Audio:**

"The three SAST tools you need to know for the DevSecOps Professional exam are Semgrep, SonarQube, and Checkmarx.

**Semgrep** is an open-source, pattern-matching SAST tool that uses a simple, readable rule syntax. Rules are written in YAML and closely resemble the code patterns they detect, making them easy to understand and write. Semgrep has a large community registry of rules covering OWASP Top 10 vulnerabilities across dozens of languages. It integrates natively with GitHub Actions, GitLab CI, and Jenkins.

**[SHOW CODE]**

Running Semgrep in a GitHub Actions pipeline:

```yaml
- name: Run Semgrep SAST
  uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/owasp-top-ten
      p/python
      p/secrets
  env:
    SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
```

`p/owasp-top-ten` uses the community rule pack for OWASP Top 10 vulnerabilities. `p/python` adds Python-specific rules. `p/secrets` detects hardcoded credentials.

**SonarQube** is an enterprise-grade code quality and security platform with deeper semantic analysis than Semgrep. SonarQube integrates into CI pipelines via the SonarScanner and posts results to a SonarQube server. It supports quality gates — configurable thresholds (e.g., no new critical vulnerabilities, code coverage above 80%) that must pass before a PR can merge. SonarQube Community edition is free; Enterprise edition adds taint analysis and additional language support.

**Checkmarx** is a commercial enterprise SAST platform used in highly regulated industries (banking, healthcare, government). Checkmarx performs deep interprocedural taint analysis — it follows data flow across function calls, class boundaries, and module imports. It is more accurate than pattern-based tools but requires more configuration and has higher false-positive rates. For the exam, know Checkmarx as the enterprise taint analysis SAST tool."

---

### [11:00 - 16:00] Analyzing SAST Findings: The Lab Skill

**Visual:** Semgrep output showing a finding with metadata

**Audio:**

"Now let's cover the skill this module's lab specifically tests: analyzing a SAST finding, identifying the vulnerability, and describing the remediation. This is directly tested on the DevSecOps Professional exam.

**[SHOW CODE]**

Here is representative Semgrep output for a finding:

```text
/app/routes/auth.py
  python.flask.security.audit.hardcoded-token.hardcoded-token
  Hardcoded token `SECRET_KEY` detected. Avoid hardcoding sensitive values.
  Use environment variables or a secrets management system instead.

  79  |  app.secret_key = "my-super-secret-key-12345"
       |  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Severity: ERROR
  Rule: python.flask.security.audit.hardcoded-token.hardcoded-token
  CWE: CWE-798 (Use of Hard-coded Credentials)
  OWASP: A07:2021 - Identification and Authentication Failures
```

Let me walk through how to analyze this finding.

**Vulnerability identified:** Hardcoded Flask secret key. The string `"my-super-secret-key-12345"` is embedded directly in the source code.

**Why it's a vulnerability:** Flask uses the secret key to sign session cookies and CSRF tokens. If the secret key is known, an attacker can forge valid session cookies, impersonating any user including administrators. Because it's hardcoded in source code, anyone with read access to the repository — including after the repository is made public or after a breach of the version control system — has the secret key permanently, even if the code is later changed.

**CWE and OWASP mapping:** CWE-798 (Use of Hard-coded Credentials). OWASP A07:2021 — Identification and Authentication Failures.

**Remediation:**

```python
import os
# Read from environment variable — never hardcode
app.secret_key = os.environ.get('FLASK_SECRET_KEY')
if not app.secret_key:
    raise RuntimeError('FLASK_SECRET_KEY environment variable is required')
```

Store `FLASK_SECRET_KEY` in your secrets management system (GitHub Secrets, HashiCorp Vault, AWS Secrets Manager) and inject it as an environment variable at runtime.

This is the pattern for analyzing any SAST finding: identify the vulnerability type, explain why it is dangerous, cite the CWE/OWASP classification, and write the remediated code."

---

### [16:00 - 20:00] SAST Integration Patterns and False Positives

**Visual:** Pipeline diagram showing SAST placement and breaking vs. non-breaking modes

**Audio:**

"Let's talk about how SAST integrates into a real DevSecOps pipeline — including the challenge of false positives.

SAST tools run in two modes in a pipeline: breaking and non-breaking. In breaking mode, a finding at or above a configured severity threshold fails the pipeline job, blocking the merge. In non-breaking mode, findings are reported but do not block the pipeline — they appear as advisory results.

The recommended DevSecOps pattern is: use non-breaking mode initially when introducing SAST to a codebase that has existing technical debt. Scan and triage existing findings without blocking the team. Then progressively tighten: first make CRITICAL findings breaking, then add HIGH, and so on, as the team works down the backlog.

False positives — SAST findings that are not actual vulnerabilities — are a real operational challenge. Every SAST tool has them. Too many false positives cause 'alert fatigue' and developers start ignoring all SAST output. Managing false positives requires: tuning rule configurations to disable rules that generate noise for your tech stack, adding suppression comments for confirmed false positives with documented justification, and establishing a triage process.

**[SHOW CODE]**

Semgrep suppression comment syntax — marking a specific line as a known false positive:

```python
# nosemgrep: python.flask.security.audit.debug-enabled.debug-enabled
app.run(debug=True)  # Debug mode enabled only in development, gated by environment check
```

The `# nosemgrep:` comment with the specific rule ID suppresses that rule for that line only, without disabling the rule globally."

---

### [20:00 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know that SAST analyzes source code without execution, using pattern matching and taint analysis. Know the three major tools: Semgrep (open-source, pattern-based), SonarQube (enterprise, quality gates), Checkmarx (enterprise, deep taint analysis). Know that SAST runs at the commit/PR stage. Know CWE-89 (SQL Injection), CWE-79 (XSS), and CWE-798 (Hardcoded Credentials) as the top SAST-detected vulnerability classes. Know the difference between breaking and non-breaking SAST integration modes.

Complete the lab, which requires analyzing a SAST finding and writing a remediation. The OWASP reference for SAST concepts is at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/). See you in Module 07."
