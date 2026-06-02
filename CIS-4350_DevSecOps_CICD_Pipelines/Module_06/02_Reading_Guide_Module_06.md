# Reading Guide: Module 06 - SAST: Static Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 06 covers SAST — Static Application Security Testing — the most widely deployed automated security control at the code commit stage of the DevSecOps pipeline. SAST analyzes source code without executing the application, detecting vulnerability patterns and data flow issues before code reaches any environment. Understanding SAST mechanics, tools, finding analysis, and pipeline integration is essential for the DevSecOps Professional exam.

---

## Section 1: High-Yield Glossary

**SAST (Static Application Security Testing)** — Analysis of source code, bytecode, or binaries without executing the application. Identifies vulnerability patterns, insecure API usage, and data flow issues. Runs at the commit or pull request pipeline stage.

**Pattern matching** — A SAST analysis technique that uses regular expressions or abstract syntax tree (AST) matching to detect known dangerous code patterns: SQL string concatenation, `eval()` calls, `innerHTML` assignments, hardcoded credentials. Semgrep is primarily pattern-matching.

**Taint analysis** — A SAST analysis technique that tracks the flow of untrusted data (taint sources: user input, API parameters) through code paths to dangerous operations (taint sinks: SQL execution, shell commands, HTML rendering) without sanitization. More accurate than pattern matching but computationally expensive.

**Taint source** — A location in code where untrusted data enters the application: HTTP request parameters, form inputs, file reads, database query results, environment variables.

**Taint sink** — A location in code where untrusted data could cause a vulnerability if it arrives unvalidated: SQL execution functions, OS command execution, HTML rendering, file write operations.

**Abstract Syntax Tree (AST)** — A tree representation of the syntactic structure of source code. AST-based analysis enables more precise pattern matching than regex, understanding code structure rather than just text patterns.

**CWE (Common Weakness Enumeration)** — A community-developed list of software and hardware weakness types. SAST findings are mapped to CWE identifiers. Key CWEs for SAST: CWE-89 (SQL Injection), CWE-79 (XSS), CWE-798 (Hardcoded Credentials), CWE-22 (Path Traversal), CWE-502 (Deserialization of Untrusted Data).

**OWASP Top 10** — A regularly updated list of the ten most critical web application security risks, published by OWASP. SAST rule packs are commonly organized around OWASP Top 10 categories. Key categories: A01 (Broken Access Control), A03 (Injection), A07 (Authentication Failures).

**Semgrep** — An open-source, pattern-matching SAST tool with a readable YAML rule syntax. Supports 30+ languages. Community rule registry at semgrep.dev. Integrates natively with GitHub Actions.

**SonarQube** — An enterprise-grade code quality and security platform. Supports quality gates (configurable pass/fail thresholds). Community edition is free; Enterprise adds advanced taint analysis.

**Checkmarx** — A commercial enterprise SAST platform known for deep interprocedural taint analysis used in regulated industries. Higher accuracy and higher false-positive rate than pattern-based tools.

**Quality gate** — A SonarQube feature that defines configurable thresholds a code change must pass: no new critical vulnerabilities, test coverage above a percentage. Quality gate failure blocks PR merging.

**False positive** — A SAST finding that reports a vulnerability that does not actually exist in the running application. High false-positive rates cause alert fatigue and reduce developer trust in SAST tooling.

**Alert fatigue** — A condition where developers begin ignoring security alerts because the volume or false-positive rate is too high. Alert fatigue reduces the effectiveness of automated security tooling.

**Suppression comment** — A code comment that instructs a SAST tool to ignore a specific finding at a specific line. Used for confirmed false positives. Must include a documented justification.

**Breaking vs. non-breaking mode** — A pipeline configuration distinction. Breaking mode: SAST findings above a severity threshold fail the pipeline job and block merging. Non-breaking mode: findings are reported but do not block the pipeline.

**Parameterized query** — The secure alternative to SQL string concatenation. Uses placeholders (`?`, `%s`, or named parameters) with a separate parameter list. The database driver treats parameters as data, not as SQL syntax, preventing injection.

---

## Section 2: SAST Tool Comparison

| Dimension | Semgrep | SonarQube | Checkmarx |
|---|---|---|---|
| License | Open-source (Community) | Open-source Community / Commercial Enterprise | Commercial |
| Primary analysis technique | Pattern matching + lightweight taint | Semantic analysis + taint | Deep interprocedural taint |
| Rule format | YAML (readable, writable by engineers) | Built-in + custom rules | Built-in + custom queries |
| Pipeline integration | GitHub Actions, GitLab CI, Jenkins | SonarScanner CLI, CI plugins | CxFlow CI integration |
| Quality gates | Via Semgrep App | Built-in quality gate feature | Project-level policies |
| Language support | 30+ languages | 30+ languages | 30+ languages |
| False positive rate | Lower (pattern-based) | Medium | Higher (deep analysis) |
| Best suited for | Most DevSecOps pipelines | Code quality + security combined | Regulated enterprise (banking, health) |

---

## Section 3: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Full name | Static Application Security Testing | Dynamic Application Security Testing | Software Composition Analysis |
| Requires running application | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Finds | Insecure code patterns, injection flaws, hardcoded creds | Runtime flaws, auth issues, config errors | Known CVEs in libraries |
| False positive rate | Higher (no runtime context) | Lower (real execution) | Low (CVE database match) |
| Representative tools | Semgrep, SonarQube, Checkmarx | OWASP ZAP, Burp Suite Enterprise | Snyk, OWASP Dependency-Check |

---

## Section 4: Common SAST-Detected Vulnerabilities Reference

| CWE | OWASP Category | Vulnerability | Insecure Pattern | Secure Pattern |
|---|---|---|---|---|
| CWE-89 | A03 Injection | SQL Injection | `f"SELECT ... {user_input}"` | Parameterized query with `?` placeholder |
| CWE-79 | A03 Injection | Cross-Site Scripting (XSS) | `response.write(request.param)` | `html.escape(param)` before output |
| CWE-78 | A03 Injection | OS Command Injection | `os.system(user_input)` | `subprocess.run([cmd], shell=False)` |
| CWE-798 | A07 Auth Failures | Hardcoded Credentials | `password = "secret123"` | `os.environ.get('PASSWORD')` |
| CWE-22 | A01 Access Control | Path Traversal | `open(user_path)` | Validate against allowlist, use `os.path.realpath` |
| CWE-502 | A08 Data Integrity | Insecure Deserialization | `pickle.loads(user_data)` | Use JSON; never deserialize untrusted data with pickle |

---

## Section 5: SAST Finding Analysis Framework

When analyzing a SAST finding (required in the lab and tested on the exam), use this structure:

1. **Finding description:** What did the tool flag? Quote the rule name and the flagged line.
2. **Vulnerability type:** Name the vulnerability class (SQL injection, XSS, hardcoded credential, etc.).
3. **CWE and OWASP classification:** Map to the correct CWE number and OWASP Top 10 category.
4. **Attack scenario:** Describe how an attacker would exploit this finding in practice.
5. **Why SAST caught it:** What analysis technique (pattern matching, taint analysis) detected it?
6. **Remediation:** Write the corrected code. Explain why the fix eliminates the vulnerability.

---

## Section 6: Semgrep Rule Structure Reference

Semgrep rules are written in YAML. Understanding the structure is tested on the exam.

```yaml
rules:
  - id: sql-injection-string-concat
    patterns:
      - pattern: |
          $CURSOR.execute("..." + $INPUT)
      - pattern: |
          $CURSOR.execute(f"...{$INPUT}...")
    message: >
      Potential SQL injection: untrusted input concatenated into SQL query.
      Use parameterized queries instead.
    languages: [python]
    severity: ERROR
    metadata:
      cwe: CWE-89
      owasp: A03:2021
```

Key fields: `id` (unique rule identifier), `patterns` (code patterns to match), `message` (developer-facing description and remediation hint), `languages` (scoped to specific languages), `severity` (INFO/WARNING/ERROR).

---

## Section 7: Pipeline Integration Patterns

### Breaking Mode (Recommended for New Projects)

Configure the SAST action to exit with a non-zero code on findings:

```yaml
- name: Run Semgrep SAST
  uses: returntocorp/semgrep-action@v1
  with:
    config: p/owasp-top-ten
    # Semgrep action exits non-zero on findings by default in CI mode
```

### Non-Breaking Mode (Recommended When Introducing SAST to Legacy Code)

```yaml
- name: Run Semgrep SAST (advisory)
  uses: returntocorp/semgrep-action@v1
  with:
    config: p/owasp-top-ten
  continue-on-error: true
  # continue-on-error: true makes the job succeed regardless of Semgrep exit code
```

### Progressive Tightening Strategy

Week 1: Non-breaking, CRITICAL only — measure baseline finding count.
Week 2-4: Triage and remediate CRITICAL findings.
Week 5: Make CRITICAL breaking. Continue non-breaking for HIGH.
Week 6-8: Remediate HIGH findings.
Week 9: Make HIGH breaking. Continue pattern for MEDIUM.

---

## Section 8: Docker Security Best Practices Reference

These practices are cross-cutting exam topics.

- Use minimal base images (Alpine, distroless) — reduces attack surface.
- Never run containers as root — use USER directive.
- Multi-stage builds — excludes build tools from production image.
- Pin dependency versions — reproducible and CVE-trackable.
- Scan images with Trivy or Grype before push.
- Store secrets in environment variables — never in image layers.

---

## Section 9: DevSecOps Professional Exam Tips

1. **SAST pipeline stage** — SAST runs at the commit/PR stage. The exam tests this as the correct placement for catching first-party code vulnerabilities before they merge.

2. **Taint source to sink** — Know the taint flow pattern: source (user input) → code path → sink (SQL execution) without sanitization = vulnerability. The exam presents code snippets and asks you to identify the source, sink, and remediation.

3. **Parameterized queries** — Know that parameterized queries (with `?` placeholders and separate parameter lists) are the correct SQL injection remediation. String concatenation and f-strings are the insecure pattern.

4. **False positive management** — Know that high false-positive rates cause alert fatigue. Know that suppression comments with documented justification are the correct way to handle confirmed false positives.

5. **Breaking vs. non-breaking** — Know when each mode is appropriate. For legacy codebases with existing findings, start non-breaking to avoid blocking all development work while the team triages the backlog.

6. **SonarQube quality gates** — Know that SonarQube quality gates define pass/fail thresholds. A quality gate failure blocks PR merging in the same way a CI job failure does.

7. **CWE vs. OWASP** — CWE identifies the vulnerability class (e.g., CWE-89 SQL Injection). OWASP Top 10 categorizes the risk (e.g., A03 Injection). A single OWASP category covers multiple CWEs.

8. **Semgrep rule packs** — Know that `p/owasp-top-ten` covers OWASP Top 10 vulnerabilities, `p/secrets` covers hardcoded credentials, and rules are available per language (`p/python`, `p/javascript`).

---

## Section 10: Required Reading

- Read the OWASP DevSecOps Guideline SAST section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).

---

## Section 11: Study Checklist

- [ ] Explain the difference between pattern matching and taint analysis in SAST.
- [ ] Identify the taint source, code path, and sink in a given code snippet.
- [ ] Write the parameterized query remediation for a SQL injection finding.
- [ ] Compare Semgrep, SonarQube, and Checkmarx — when is each appropriate?
- [ ] Explain what a quality gate is and how it blocks PR merging.
- [ ] Explain the difference between breaking and non-breaking SAST pipeline integration.
- [ ] Use the SAST finding analysis framework to analyze a sample finding.
- [ ] Map common vulnerability types to their CWE numbers.
- [ ] Read the OWASP DevSecOps Guideline SAST section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).
- [ ] Complete the Module 06 lab (SAST finding analysis and remediation).
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
