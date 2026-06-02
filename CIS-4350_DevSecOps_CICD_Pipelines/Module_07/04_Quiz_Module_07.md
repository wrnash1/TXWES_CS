# Quiz: Module 07 - DAST: Dynamic Application Security Testing

## Course: CIS-4350 DevSecOps and CI/CD Pipelines

## Certification Alignment: DevSecOps Professional (DSOE)

---

### Question 1

At which CI/CD pipeline stage should DAST be executed?

- A) At the code commit stage, before any tests run, to provide the earliest possible feedback
- B) After deployment to a staging environment, because DAST requires a running application to test
- C) At the build stage, after dependencies are installed but before the application is packaged
- D) After deployment to production, because the full production environment is required for accurate results

#### Q1 Correct Answer

B — DAST sends HTTP requests to a live application and analyzes responses. A running application is required. Staging is the correct environment: it mirrors production closely enough for meaningful testing while preventing active attack payloads from targeting real users and data.

#### Q1 Distractor Analysis

- *Why A is incorrect:* There is no running application at the commit stage. DAST cannot run without an HTTP server to target.
- *Why C is incorrect:* The build stage produces an artifact but does not start a running application service. DAST cannot scan an artifact.
- *Why D is incorrect:* Active DAST scanning in production risks disrupting real users, corrupting production data (from injection payloads), and triggering security incident alerts. DAST active scanning must never target production.

---

### Question 2

A DevSecOps engineer wants to run OWASP ZAP against the production environment to continuously monitor for new security misconfigurations. Which ZAP scan mode is safe for production use?

- A) Full active scan (`zap-full-scan.py`) — because it provides the most comprehensive coverage
- B) Passive scanning — because it observes HTTP traffic and responses without sending attack payloads
- C) Authenticated active scanning — because credentials allow deeper testing of production endpoints
- D) API scanning with attack mode enabled — because modern applications are primarily APIs

#### Q2 Correct Answer

B — Passive scanning only observes HTTP traffic that already exists or responses to normal application requests. It does not inject attack payloads, modify data, or stress the application. It is safe for production monitoring and can detect missing security headers, insecure cookie flags, and information disclosure.

#### Q2 Distractor Analysis

- *Why A is incorrect:* Active scanning sends SQL injection strings, XSS payloads, and path traversal attempts to every discovered parameter. In production, this could corrupt data, trigger account lockouts, and disrupt real users.
- *Why C is incorrect:* Authenticated active scanning in production compounds the risk — a compromised session token used for active scanning against production is dangerous.
- *Why D is incorrect:* API scanning with attack mode enabled is still active scanning — it sends malicious payloads. Calling it API scanning does not change its risk profile in production.

---

### Question 3

Which of the following vulnerabilities would DAST detect that SAST typically cannot?

- A) A hardcoded database password stored in a Python configuration file
- B) An application that fails to lock user accounts after five failed login attempts, enabling brute-force attacks
- C) An SQL injection vulnerability caused by string concatenation in a Java DAO class
- D) A private key accidentally committed to a YAML configuration file

#### Q3 Correct Answer

B — Account lockout behavior is a runtime characteristic. DAST can verify whether repeated failed login requests result in account lockout by actually sending those requests and observing the response. SAST can see login code but cannot determine whether the runtime lockout threshold is correctly configured and enforced.

#### Q3 Distractor Analysis

- *Why A is incorrect:* A hardcoded database password is a code-level issue detectable by SAST (pattern matching for credential strings) or by secrets scanning tools.
- *Why C is incorrect:* SQL injection via string concatenation is a code pattern. SAST detects this pattern in source code without needing to execute the application.
- *Why D is incorrect:* A private key in a YAML file is a secrets exposure issue. Secrets scanners (Gitleaks, truffleHog) detect this at the commit stage. It is not a runtime behavior that requires DAST.

---

### Question 4

A ZAP baseline scan is run in a GitHub Actions pipeline with `fail_action: true`. The scan finds two WARN-severity findings and zero FAIL-severity findings. What happens to the pipeline job?

- A) The pipeline job succeeds because no FAIL-severity findings were detected
- B) The pipeline job fails because any finding — including WARN — causes the action to exit non-zero when `fail_action: true` is set
- C) The pipeline job pauses and waits for a security engineer to review the WARN findings before continuing
- D) The pipeline job uploads the findings to GitHub Security tab and continues regardless of severity

#### Q4 Correct Answer

B — When `fail_action: true` is set in the ZAP GitHub Action, any finding above the threshold (default: WARN and above) causes the action to exit with a non-zero code, failing the pipeline job. To pass only on FAIL-severity findings, you would configure the alert level threshold in the rules file.

#### Q4 Distractor Analysis

- *Why A is incorrect:* With `fail_action: true`, WARN findings also trigger a failure. The distinction between WARN and FAIL matters for rules file configuration but both cause job failure by default.
- *Why C is incorrect:* GitHub Actions has no built-in "pause for review" mechanism within a job step. Pause-for-approval requires environment protection rules at the deployment level.
- *Why D is incorrect:* SARIF uploading to GitHub Security is a separate step. `fail_action: true` controls the job exit code, not what happens to the report.

---

### Question 5

What is the primary reason DAST has a lower false positive rate than SAST for injection vulnerabilities?

- A) DAST has access to the application's source code, enabling more accurate analysis
- B) DAST verifies vulnerabilities by observing actual application behavior in response to injected payloads, confirming exploitability
- C) DAST tools use more sophisticated machine learning algorithms than SAST tools
- D) DAST runs against production data, which provides more realistic testing conditions

#### Q5 Correct Answer

B — DAST confirms a SQL injection by sending an injection payload and observing a database error message or behavioral change in the response. This behavioral confirmation means DAST reports findings that are actually exploitable, reducing false positives compared to SAST's code-pattern matching which may flag code that has compensating runtime controls.

#### Q5 Distractor Analysis

- *Why A is incorrect:* DAST does not have source code access. It operates entirely through the HTTP interface, which is why it runs against a deployed application, not source code.
- *Why C is incorrect:* Algorithm sophistication is not the explanation. The lower false positive rate comes from runtime behavioral confirmation, not algorithmic superiority.
- *Why D is incorrect:* DAST runs against staging, not production. Running against production data is a security risk, not a testing advantage.

---

### Question 6

An OWASP ZAP scan produces the following finding for a web application. What is the remediation?

```text
WARN-NEW: Cookie Without Secure Flag [10011]
Evidence: Set-Cookie: session=xyz789; HttpOnly; Path=/
CWE: 614
```

- A) Remove the `HttpOnly` attribute from the Set-Cookie header to make the flag easier to read
- B) Add the `Secure` attribute to the Set-Cookie header so the cookie is only transmitted over HTTPS connections
- C) Change the cookie name from `session` to a more obscure value to prevent prediction attacks
- D) Reduce the cookie expiration time to 15 minutes to limit the exposure window

#### Q6 Correct Answer

B — The `Secure` attribute instructs the browser to only transmit the cookie over encrypted HTTPS connections. Without it, the session cookie can be transmitted over unencrypted HTTP if the user accesses the site via HTTP (e.g., a man-in-the-middle on a coffee shop network can capture the cookie).

#### Q6 Distractor Analysis

- *Why A is incorrect:* Removing `HttpOnly` would make the cookie accessible to JavaScript, increasing vulnerability. The `HttpOnly` attribute is a security feature that should be kept.
- *Why C is incorrect:* Cookie name obscurity is security through obscurity and does not address the transmission risk. The `Secure` flag controls whether the cookie is sent over unencrypted connections.
- *Why D is incorrect:* A shorter expiration time limits the session duration but does not prevent the cookie from being captured over an unencrypted connection during its valid lifetime.

---

### Question 7

A development team's DAST pipeline scans a React Single Page Application using ZAP's default spider. The scan reports very few findings because the spider only discovered 3 of the application's 47 routes. What is the most likely cause and solution?

- A) The application uses HTTPS, and ZAP only scans HTTP applications — the solution is to configure HTTP-to-HTTPS redirection
- B) ZAP's default spider cannot follow JavaScript-rendered navigation in SPAs — the solution is to use ZAP's AJAX spider or OpenAPI/GraphQL API scan mode
- C) The application uses cookies for navigation, and ZAP must be configured with a valid session cookie to discover all routes
- D) The 3 routes discovered are on a different subdomain from the other 44 — the solution is to configure ZAP to scan multiple target domains

#### Q7 Correct Answer

B — React SPAs render navigation and content via JavaScript. ZAP's traditional spider follows HTML links (anchor tags, forms) and cannot execute JavaScript. Most routes in a React app are only discoverable by a JavaScript-capable browser. The AJAX spider uses a headless browser to discover dynamically rendered content.

#### Q7 Distractor Analysis

- *Why A is incorrect:* ZAP supports HTTPS scanning natively. HTTPS is not the limitation here.
- *Why C is incorrect:* While authenticated scanning requires a valid session, the inability to discover routes is specifically a JavaScript rendering problem, not a session/authentication issue.
- *Why D is incorrect:* Subdomain differences would result in ZAP discovering the routes it can see and attempting to follow links to other subdomains. The issue described (only 3 of 47 routes discovered) is characteristic of JavaScript rendering limitations.

---

### Question 8

Which class of vulnerability cannot be detected by DAST automated scanning and requires manual penetration testing?

- A) SQL injection via GET parameter manipulation
- B) Missing HTTP security response headers
- C) Business logic vulnerabilities where an attacker exploits application workflow assumptions
- D) Insecure direct object references via incremental ID enumeration

#### Q8 Correct Answer

C — Business logic vulnerabilities involve understanding the application's intended workflow and finding ways to subvert it: skipping payment steps in a checkout flow, exploiting discounts that only apply to certain accounts, or bypassing multi-step approval processes. These require a tester who understands the application's business rules — something automated tools cannot replicate.

#### Q8 Distractor Analysis

- *Why A is incorrect:* SQL injection via GET parameters is detectable by DAST active scanning. ZAP sends injection payloads to all discovered parameters.
- *Why B is incorrect:* Missing security headers are detected by ZAP passive scanning by inspecting HTTP response headers.
- *Why D is incorrect:* IDOR via incremental ID enumeration is a pattern DAST tools can automate — they test ID modification in API responses to detect when unauthorized access is returned.

---

### Question 9

A GitHub Actions pipeline has the following DAST job structure. What is the security purpose of the health check step before the ZAP scan?

```yaml
dast-scan:
  needs: deploy-staging
  steps:
    - name: Wait for staging health check
      run: |
        for i in {1..30}; do
          curl -sf https://staging.myapp.com/health && break
          sleep 10
        done
    - name: Run ZAP baseline scan
      uses: zaproxy/action-baseline@v0.10.0
```

- A) To verify that the staging database has been populated with test data before scanning begins
- B) To ensure the staging application is fully started and responding before ZAP begins crawling, preventing incomplete scan coverage from a partially initialized application
- C) To authenticate ZAP to the staging application before passive scanning begins
- D) To warm up the application's JVM or runtime cache so performance does not affect scan timing

#### Q9 Correct Answer

B — If ZAP begins scanning before the staging application has fully started, the spider will encounter connection errors or incomplete responses. This produces an incomplete discovery phase, meaning the ZAP scan misses endpoints that were not yet serving requests when the spider ran. The health check loop waits until the application is confirming readiness before the scan begins.

#### Q9 Distractor Analysis

- *Why A is incorrect:* The health check verifies application availability, not database population. Test data loading is a separate concern for DAST test environment setup.
- *Why C is incorrect:* The health check is a curl GET request to a health endpoint. It does not authenticate ZAP or configure session handling.
- *Why D is incorrect:* JVM warmup is a performance concern, not a security concern. The health check is specifically about ensuring scan completeness.

---

### Question 10

A DevSecOps team wants comprehensive DAST coverage but recognizes that a full active ZAP scan takes 45 minutes and cannot run on every PR. What is the recommended approach to balance coverage and velocity?

- A) Run the full 45-minute active scan on every PR to maintain maximum security coverage regardless of pipeline duration
- B) Eliminate DAST from the pipeline entirely and rely on SAST for all automated security testing
- C) Run a fast ZAP baseline scan on every PR merge to staging, and run a full active scan on a nightly scheduled pipeline
- D) Run DAST only on the main release branch once per month to limit scan frequency

#### Q10 Correct Answer

C — The baseline scan takes 2-5 minutes and catches the most common, high-impact findings in every deployment. The full active scan runs on a schedule (nightly) to provide comprehensive coverage without blocking development velocity. This is the standard DevSecOps pattern for balancing thoroughness with feedback loop speed.

#### Q10 Distractor Analysis

- *Why A is incorrect:* A 45-minute pipeline step on every PR dramatically slows development velocity. Developers will work around or disable the scan to restore velocity.
- *Why B is incorrect:* SAST and DAST are complementary. Removing DAST eliminates detection of runtime vulnerabilities, authentication flaws, and security misconfigurations.
- *Why D is incorrect:* Monthly DAST scanning means vulnerabilities introduced at any point in the month are in production for up to 30 days before detection. This violates the DevSecOps short feedback loop principle.
