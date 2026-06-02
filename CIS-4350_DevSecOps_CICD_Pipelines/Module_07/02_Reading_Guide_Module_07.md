# Reading Guide: Module 07 - DAST: Dynamic Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

## Introduction

Module 07 covers DAST — Dynamic Application Security Testing — the runtime complement to SAST. DAST tests a deployed application by sending real HTTP requests and analyzing responses, finding vulnerabilities that only manifest during execution. Understanding DAST mechanics, OWASP ZAP, pipeline placement, and the comparison with SAST is essential for the DevSecOps Professional exam.

---

## Section 1: High-Yield Glossary

**DAST (Dynamic Application Security Testing)** — Security testing that sends crafted HTTP requests to a running application and analyzes responses to detect runtime vulnerabilities. Requires a deployed application. Runs at the staging pipeline stage.

**Spider (crawler)** — The DAST discovery phase where the tool systematically follows links, forms, and API endpoints to map the application's attack surface before testing begins.

**Passive scanning** — A DAST mode that observes HTTP traffic without sending additional requests. Detects: missing security headers, insecure cookie attributes, information disclosure. Safe for any environment including production monitoring.

**Active scanning** — A DAST mode that sends crafted attack payloads (SQL injection strings, XSS payloads, command injection, path traversal) to discovered parameters. Detects exploitable vulnerabilities. Must only be run against non-production environments.

**OWASP ZAP (Zed Attack Proxy)** — The primary open-source DAST tool for DevSecOps pipelines, maintained by OWASP. Available at [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/). Supports both passive and active scanning, authenticated scanning, CI/CD integration via Docker, and report generation.

**zap-baseline.py** — A ZAP script that runs passive scanning plus a small subset of active checks. Fast (2-5 minutes), safe for staging environments. Recommended for CI/CD pipeline integration.

**zap-full-scan.py** — A ZAP script that runs the complete active scanner against all discovered endpoints. Comprehensive but slow (30-90 minutes for complex applications). Run on a nightly or weekly schedule rather than every PR.

**Authenticated scanning** — DAST that tests endpoints behind authentication by maintaining a valid session. Required to discover IDOR, broken object-level authorization, and other authenticated vulnerabilities.

**IDOR (Insecure Direct Object Reference)** — A broken access control vulnerability where a user can access another user's resource by modifying an identifier (e.g., changing `/orders/12345` to `/orders/12346`). Detected by DAST, not SAST.

**Security header** — An HTTP response header that instructs the browser to apply a security policy: Content-Security-Policy, Strict-Transport-Security, X-Frame-Options, X-Content-Type-Options, Referrer-Policy. Absence of required headers is detected by DAST passive scanning.

**False positive (DAST context)** — A DAST finding that reports a vulnerability the application is not actually exploitable for. Common sources: scanner misinterpreting error messages, benign responses that match injection indicators. Managed via ZAP rules configuration files.

**AJAX spider** — A ZAP component that uses a headless browser to discover endpoints in Single Page Applications (SPAs) where JavaScript dynamically renders content and navigation. Required for effective DAST of React/Angular/Vue applications.

**Burp Suite Enterprise** — A commercial DAST platform from PortSwigger with advanced scanning capabilities, team collaboration features, and CI/CD integrations. The commercial alternative to ZAP for enterprise DevSecOps environments.

**Security misconfiguration** — A vulnerability class (OWASP A05) where the application or its hosting environment is configured insecurely: missing security headers, default credentials, verbose error messages, unnecessarily exposed services. DAST is the primary detection tool for this class.

---

## Section 2: SAST vs. DAST vs. SCA Comparison

| Dimension | SAST | DAST | SCA |
|---|---|---|---|
| Full name | Static Application Security Testing | Dynamic Application Security Testing | Software Composition Analysis |
| Requires running application | No | Yes | No |
| Primary target | First-party source code | Running application endpoints | Third-party dependencies |
| Pipeline stage | Commit / Pull request | Staging | Build |
| Finds | Insecure code patterns, injection flaws | Runtime flaws, auth issues, config errors | Known CVEs in libraries |
| False positive rate | Higher | Lower | Low |
| Unique to this tool | Code-level data flow vulnerabilities | Runtime behavior, IDOR, missing headers | Transitive dependency CVEs |
| Representative tools | Semgrep, SonarQube, Checkmarx | OWASP ZAP, Burp Suite Enterprise | Snyk, OWASP Dependency-Check |

---

## Section 3: Vulnerability Classes by Detection Method

| Vulnerability Class | SAST Detects | DAST Detects | Explanation |
|---|---|---|---|
| SQL Injection (code pattern) | Yes | Yes | SAST detects concatenation pattern; DAST detects via response analysis |
| SQL Injection (stored, multi-step) | Partial | Yes | DAST tests the full request/response cycle |
| XSS (reflected, obvious) | Yes | Yes | Both detect common patterns |
| XSS (DOM-based, SPA) | Partial | Yes | DOM manipulation only visible at runtime |
| Broken Authentication (rate limiting) | No | Yes | Rate limiting is runtime behavior |
| IDOR / Broken Access Control | No | Yes | Authorization enforcement tested at runtime |
| Missing Security Headers | No | Yes | Headers are in HTTP responses, not source code |
| Insecure Cookie Attributes | Partial | Yes | Cookie flags tested via response inspection |
| Hardcoded Credentials | Yes | No | Credentials in source code — SAST's strength |
| Vulnerable Dependencies (CVEs) | No | No | SCA domain |

---

## Section 4: OWASP ZAP Pipeline Integration Reference

### Baseline Scan (Recommended for All PRs/Deployments)

```bash
docker run --rm ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py \
  -t https://staging.myapp.com \
  -r zap-baseline-report.html \
  -l WARN
```

- `-t` — target URL
- `-r` — HTML report output file
- `-l WARN` — fail the scan if WARN or higher severity findings are discovered

### Full Active Scan (Nightly/Weekly Schedule)

```bash
docker run --rm \
  -v $(pwd)/reports:/zap/wrk \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-full-scan.py \
  -t https://staging.myapp.com \
  -r zap-full-report.html \
  -x zap-full-report.xml \
  -l WARN
```

### GitHub Actions Integration

```yaml
- name: Run OWASP ZAP baseline scan
  uses: zaproxy/action-baseline@v0.10.0
  with:
    target: 'https://staging.myapp.com'
    fail_action: true
    rules_file_name: '.zap/rules.tsv'
```

The `.zap/rules.tsv` file maps ZAP rule IDs to alert levels (IGNORE, INFO, WARN, FAIL), allowing per-rule configuration without disabling the scan.

---

## Section 5: CI/CD Pipeline Stage Comparison

| Stage | Security Activity | Tool | Notes |
|---|---|---|---|
| Pre-commit | Secrets scanning | Gitleaks | Earliest gate |
| Commit / PR | SAST | Semgrep, SonarQube | Code-level patterns |
| Build | SCA | Snyk, OWASP Dependency-Check | Dependency CVEs |
| Container build | Image scan | Trivy, Grype | OS + runtime CVEs |
| Deploy to staging | DAST | OWASP ZAP | Runtime vulnerabilities |
| IaC provisioning | IaC scan | Checkov, tfsec | Misconfiguration |
| Production | Runtime monitoring | Falco, GuardDuty | Anomaly detection |

---

## Section 6: DAST Limitations Reference

These limitations are tested on the DevSecOps Professional exam.

| Limitation | Explanation | Mitigation |
|---|---|---|
| Requires running application | Cannot run before staging deployment | Accept — this is by design for DAST |
| Slow for complex apps | Full active scan: 30-90+ minutes | Use baseline in pipeline; full scan nightly |
| SPA/AJAX coverage | Basic spider misses JS-rendered content | Use AJAX spider or API scan mode |
| Authenticated endpoints | Unauthenticated scans miss auth vulnerabilities | Configure authenticated scanning |
| Business logic flaws | ZAP cannot understand application logic | Supplement with manual penetration testing |
| No source code access | Cannot detect code-level issues SAST finds | Pair with SAST — complementary tools |

---

## Section 7: Docker Security Best Practices Reference

These cross-cutting exam topics apply to DAST containerized environments as well.

- DAST tools like ZAP are commonly run in Docker containers within CI/CD pipelines.
- Apply the same container security principles: minimal base images, non-root user, no secrets in image layers.
- ZAP's Docker image runs as a non-root user by default.

---

## Section 8: DevSecOps Professional Exam Tips

1. **DAST pipeline stage** — DAST runs after deployment to staging. The exam tests this as the correct placement because DAST requires a running application.

2. **Passive vs. active scan** — Know the difference: passive scanning observes without sending payloads (safe for any environment); active scanning sends attack payloads (staging only). A question asking "what DAST mode is safe for production monitoring?" has the answer: passive scanning.

3. **What DAST finds that SAST misses** — Know the four categories: broken authentication (runtime behavior), IDOR (authorization enforcement), security misconfigurations (HTTP headers), and runtime XSS in SPAs. This comparison appears frequently on the exam.

4. **zap-baseline.py vs. zap-full-scan.py** — Baseline is fast, safe, and appropriate for every CI pipeline run. Full scan is comprehensive but slow and appropriate for scheduled nightly/weekly runs.

5. **fail_action: true / -l WARN** — These are the flags that make DAST a pipeline gate rather than an advisory report. Know that without these, ZAP exits with 0 (success) regardless of findings.

6. **Authenticated DAST requirement** — Many critical vulnerabilities (IDOR, broken object-level authorization) only exist behind authentication. An unauthenticated DAST scan misses these. The exam tests when authenticated scanning is required.

7. **OWASP ZAP project URL** — The exam may reference [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/) as the authoritative DAST tool reference.

8. **DAST does not replace penetration testing** — DAST cannot detect business logic vulnerabilities. Manual penetration testing is required for comprehensive coverage. The exam tests the complementary roles of DAST, SAST, and manual testing.

---

## Section 9: Required Reading

- Review the OWASP ZAP project overview at [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/).
- Read the OWASP DevSecOps Guideline DAST section at [https://owasp.org/www-project-devsecops-guideline/](https://owasp.org/www-project-devsecops-guideline/).

---

## Section 10: Study Checklist

- [ ] Explain why DAST is necessary even when SAST is already integrated.
- [ ] List four vulnerability classes that DAST finds but SAST typically misses.
- [ ] Explain the difference between passive and active scanning in OWASP ZAP.
- [ ] Describe where DAST belongs in the CI/CD pipeline and why.
- [ ] Explain the difference between `zap-baseline.py` and `zap-full-scan.py`.
- [ ] Explain three DAST limitations and their mitigations.
- [ ] Describe what an authenticated DAST scan is and when it is required.
- [ ] Review the OWASP ZAP project at [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/).
- [ ] Complete the Module 07 lab activity.
- [ ] Attempt all 10 quiz questions and review distractor analysis for any incorrect answers.
