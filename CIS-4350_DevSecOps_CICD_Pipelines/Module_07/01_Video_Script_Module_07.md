# Video Script: Module 07 - DAST: Dynamic Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

## Estimated Duration: 20-24 minutes

## Instructor: Professor Nash

---

### [00:00 - 01:30] Opening and Module Overview

**Visual:** Instructor on camera, title card: "Module 07 — DAST: Dynamic Application Security Testing"

**Audio:**

"Welcome back to CIS-4350. I'm Professor Nash. We just covered SAST in Module 06 — analyzing source code without running it. In this module we're covering the complementary technique: DAST, Dynamic Application Security Testing. DAST tests a running application by sending it real HTTP requests and analyzing the responses.

By the end of this video you'll understand why DAST is necessary alongside SAST, how OWASP ZAP works as a DAST tool, how to integrate DAST into the CI/CD pipeline at the staging stage, and what classes of vulnerability DAST finds that SAST cannot detect."

---

### [01:30 - 06:00] Why DAST: What SAST Cannot Find

**Visual:** Comparison diagram — SAST detects code patterns, DAST detects runtime behavior

**Audio:**

"The key question is: if SAST scans the source code, why do we also need DAST? The answer is that a significant class of vulnerabilities only manifests at runtime — when the application is actually executing, handling real HTTP sessions, interacting with a real database, and processing real request flows.

Let me give you four concrete examples of vulnerabilities DAST finds that SAST typically misses.

**Broken authentication.** SAST can see that a login function exists. DAST can actually send requests to that login endpoint and discover that after five failed login attempts, the account is not locked — a brute-force attack is possible. SAST cannot test rate limiting or lockout behavior because those are runtime behaviors.

**Insecure direct object references (IDOR).** If the application exposes `/api/orders/12345` and user A can access user B's order by changing the ID number, that's an IDOR — a broken access control vulnerability. SAST might see the route definition, but it cannot determine at code analysis time whether authorization is actually enforced correctly for all request paths. DAST sends the actual request as User A and verifies whether User B's data is returned.

**Security misconfigurations.** Missing security headers — Content-Security-Policy, Strict-Transport-Security, X-Frame-Options — are runtime configuration issues. The source code might not set these headers. DAST makes an HTTP request and inspects the response headers directly, detecting missing security headers in seconds.

**XSS via reflected parameters.** While SAST can find some XSS patterns, DAST actually injects payloads through every input parameter and checks whether the payload appears in the response body unescaped. This tests the full runtime behavior including template rendering, which may not be obvious from source code alone.

The takeaway: SAST catches code-level vulnerabilities early. DAST catches runtime and configuration vulnerabilities at the staging stage. Both are required. Neither replaces the other."

---

### [06:00 - 12:00] OWASP ZAP: Architecture and Operation

**Visual:** OWASP ZAP scanning diagram — spider, active scan, passive scan

**Audio:**

"The primary DAST tool for DevSecOps pipelines is OWASP ZAP — the Zed Attack Proxy. ZAP is an open-source, OWASP-maintained tool used by security professionals worldwide. The OWASP reference is at [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/).

ZAP works in two phases: discovery and testing.

In the discovery phase, ZAP's spider crawls the application — starting from a seed URL, it follows every link, form, and JavaScript-referenced endpoint to build a map of the application's attack surface. This automated crawl produces the list of URLs and parameters that ZAP will then test.

In the testing phase, ZAP runs scans against every discovered endpoint. ZAP has two scan modes: passive scanning and active scanning.

**Passive scanning** records and analyzes every HTTP response ZAP observes, without sending additional requests. It detects: missing security headers, insecure cookie attributes (missing Secure, HttpOnly flags), information disclosure in response bodies, and server version banners. Passive scanning is safe for any environment — it only observes.

**Active scanning** sends crafted attack payloads to every discovered parameter — SQL injection strings, XSS payloads, path traversal strings, command injection payloads. ZAP then analyzes responses for signs of vulnerability: SQL error messages, reflected script execution, unexpected file content. Active scanning is disruptive and must only be run against non-production environments.

**[SHOW CODE]**

Running OWASP ZAP in Docker for a CI/CD pipeline integration:

```bash
# Pull the ZAP stable image
docker pull ghcr.io/zaproxy/zaproxy:stable

# Run a baseline scan (passive only, safe for any environment)
docker run --rm ghcr.io/zaproxy/zaproxy:stable \
  zap-baseline.py \
  -t https://staging.myapp.com \
  -r zap-baseline-report.html

# Run a full active scan against staging
docker run --rm \
  -v $(pwd)/reports:/zap/wrk \
  ghcr.io/zaproxy/zaproxy:stable \
  zap-full-scan.py \
  -t https://staging.myapp.com \
  -r zap-full-report.html \
  -x zap-full-report.xml \
  -l WARN
```

The `zap-baseline.py` script runs a passive scan plus a small subset of active rules — safe for use against staging environments. The `zap-full-scan.py` script runs the full active scanner — only against staging, never production.

The `-l WARN` flag sets the minimum finding severity that causes the scan to exit with a non-zero code, making it a pipeline gate."

---

### [12:00 - 17:00] DAST in the CI/CD Pipeline

**Visual:** CI/CD pipeline diagram with DAST stage after staging deployment highlighted

**Audio:**

"Now let's put DAST in its correct pipeline position. DAST requires a running application, so it can only run after the application has been deployed to a staging environment. In our four-stage pipeline from Module 03, DAST belongs after the deploy-to-staging step.

**[SHOW CODE]**

Here is a GitHub Actions DAST job that runs after staging deployment:

```yaml
dast-scan:
  name: DAST Scan
  runs-on: ubuntu-latest
  needs: deploy-staging
  steps:
    - name: Wait for staging to be ready
      run: |
        for i in {1..30}; do
          curl -sf https://staging.myapp.com/health && break
          echo "Waiting for staging... attempt $i"
          sleep 10
        done

    - name: Run OWASP ZAP baseline scan
      uses: zaproxy/action-baseline@v0.10.0
      with:
        target: 'https://staging.myapp.com'
        rules_file_name: '.zap/rules.tsv'
        cmd_options: '-a -j'
        fail_action: true

    - name: Upload ZAP report
      uses: actions/upload-artifact@v4
      if: always()
      with:
        name: zap-scan-report
        path: report_html.html
```

A few important design decisions here. The health check loop waits for the staging deployment to be ready before starting the scan. Without this, ZAP might spider a partially started application and produce incomplete results.

`fail_action: true` makes the ZAP action exit non-zero if findings above a configured severity are found, making it a pipeline gate.

The `.zap/rules.tsv` file allows you to customize which ZAP rules are applied and which are excluded or marked as false positive suppressions for your application. This is how you manage alert noise in DAST similarly to how suppression comments manage false positives in SAST.

`if: always()` on the report upload ensures the artifact is saved even if the scan step fails, so you always have a report to review."

---

### [17:00 - 20:30] Authenticated DAST and Limitations

**Visual:** Browser-based authentication flow diagram

**Audio:**

"One significant challenge with DAST in CI/CD pipelines is authenticated scanning. Many vulnerabilities — IDOR, broken object-level authorization, excessive data exposure — only exist behind authentication. If ZAP crawls and scans only the unauthenticated parts of your application, it misses the most sensitive endpoints.

ZAP supports authenticated scanning through several mechanisms: form-based authentication (ZAP submits a login form and maintains the session cookie), script-based authentication for OAuth and JWT flows, and browser-based authentication using a headless browser.

For CI/CD pipeline integration, the simplest approach is to provide ZAP with a pre-authenticated session cookie or an API key that grants access to authenticated endpoints, then include it in the scan configuration.

Understanding DAST limitations is also exam-critical. DAST cannot scan Single Page Applications (SPAs) effectively with basic spider mode — heavy JavaScript frameworks like React and Angular require a browser-based AJAX spider or dedicated API scanning. DAST active scanning is time-consuming — a full scan of a complex application can take 30-90 minutes, which may be too slow for a CI/CD pipeline. For this reason, many teams run a fast baseline scan in the pipeline and run full active scans on a nightly or weekly schedule.

Finally, DAST cannot test business logic vulnerabilities — things like bypassing a multi-step checkout flow or exploiting application-specific workflow assumptions. Those require manual penetration testing."

---

### [20:30 - End] Closing and Exam Alignment

**Visual:** Instructor on camera

**Audio:**

"For the exam: know that DAST requires a running application and runs at the staging stage. Know the four vulnerability classes DAST catches that SAST misses: broken authentication, IDOR, security misconfigurations, and runtime XSS via reflected parameters. Know OWASP ZAP's two scan modes: passive (safe, observes) and active (disruptive, sends attack payloads — staging only). Know that `zap-baseline.py` is the safe, fast pipeline option and `zap-full-scan.py` is the comprehensive but slower option. Know the OWASP ZAP project reference at [https://owasp.org/www-project-zap/](https://owasp.org/www-project-zap/). See you in Module 08."
