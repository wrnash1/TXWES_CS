# Quiz: Module 07 - DAST – Dynamic Application Security Testing

## Course: CIS-4350_DevSecOps_CICD_Pipelines (Certified DevSecOps Professional (CDP))

---

**Question 1**
How does DAST (Dynamic Application Security Testing) scan for security vulnerabilities?

* A) By reading and parsing application source code files for insecure coding patterns
* B) By testing the running application, simulating real attacks from an external perspective and analyzing HTTP responses
* C) By analyzing database backup files on disk for exposed credentials or schema vulnerabilities
* D) By scanning the developer's local IDE workspace for misconfigured project settings
* **Correct Answer:** B) DAST scanners send crafted requests (such as SQL injection strings and XSS payloads) to active endpoints and evaluate the application's responses to identify runtime vulnerabilities.
* **Distractor Analysis:**
  * *Why B is correct:* DAST is a black-box testing technique — it interacts with the application exactly as an external attacker would, using only HTTP requests and response analysis, with no access to source code.
  * *Why A is incorrect:* Reading and parsing source code for patterns describes SAST, not DAST. DAST requires no source code access.
  * *Why C is incorrect:* Analyzing database backup files is a data-at-rest audit activity, not a dynamic application test. DAST targets live HTTP endpoints.
  * *Why D is incorrect:* Scanning local IDE workspaces for configuration issues is an IDE plugin or developer tool function, not DAST. DAST operates against deployed, network-accessible applications.

---

**Question 2**
Which of the following most accurately describes the role of OWASP ZAP in a DevSecOps pipeline?

* A) An open-source SAST tool that scans Python and JavaScript source files for OWASP Top 10 vulnerabilities without executing the code
* B) An open-source DAST proxy and scanner that intercepts HTTP traffic, crawls application endpoints, and sends attack payloads to identify runtime vulnerabilities in a deployed web application
* C) A secrets management platform that stores and rotates API keys and database passwords used by CI/CD pipeline jobs
* D) A Kubernetes admission controller that validates pod security contexts against defined policy standards before allowing pod creation
* **Correct Answer:** B) OWASP ZAP is a free, open-source DAST tool that can run in headless mode within a CI/CD pipeline to actively scan a deployed web application for vulnerabilities such as injection, authentication flaws, and missing security headers.
* **Distractor Analysis:**
  * *Why B is correct:* ZAP acts as a proxy to spider the application, then switches to active scan mode to send attack payloads. Its GitHub Actions integration allows it to run as a pipeline job after a staging deployment.
  * *Why A is incorrect:* ZAP is a DAST tool, not a SAST tool. It requires a running application and does not analyze source code files. Semgrep and CodeQL are SAST tools.
  * *Why C is incorrect:* Secrets management describes tools like HashiCorp Vault or AWS Secrets Manager, not ZAP. ZAP is focused on web application vulnerability detection.
  * *Why D is incorrect:* Kubernetes admission controllers (like OPA Gatekeeper) enforce pod policies at scheduling time. ZAP operates at the HTTP application layer against running web services.

---

**Question 3**
A DevSecOps team wants to add DAST to their CI/CD pipeline. At which pipeline stage should the DAST scan run, and why?

* A) At the code commit stage, immediately after the developer pushes a commit, before the code is built
* B) During the SAST stage, in parallel with source code analysis, to save pipeline execution time
* C) After the application is successfully deployed to a staging environment, because DAST requires a live, network-accessible application to send and receive HTTP requests
* D) Only in production, because staging environments do not accurately replicate production vulnerabilities
* **Correct Answer:** C) DAST requires a running, accessible web application to test — it cannot operate against source code or build artifacts. Running it against a staging environment before production deployment is the standard DevSecOps pipeline pattern.
* **Distractor Analysis:**
  * *Why C is correct:* The pipeline order is: SAST at commit → build → deploy to staging → DAST against staging → promote to production. DAST at staging catches runtime vulnerabilities before they reach production.
  * *Why A is incorrect:* DAST cannot run at commit time because there is no deployed application to test. At that stage, only SAST and linting can run.
  * *Why B is incorrect:* DAST cannot run in parallel with SAST because it requires a built and deployed application that does not exist until after the SAST and build stages complete.
  * *Why D is incorrect:* Running DAST only in production means vulnerabilities are discovered after deployment to production users. Staging environments are specifically designed to replicate production closely enough for effective DAST scanning.

---

**Question 4**
During a DAST active scan, OWASP ZAP sends the payload `' OR '1'='1` to a login form's username field and receives a 200 OK response with user account data. What vulnerability has been confirmed, and what is the root cause?

* A) Cross-Site Scripting (XSS) — the application reflects user input in the HTML response without encoding
* B) SQL Injection — the application constructs SQL queries by concatenating user input rather than using parameterized queries, allowing the attacker's payload to modify the query logic
* C) Broken Authentication — the application accepts blank passwords, allowing login without credentials
* D) Server-Side Request Forgery (SSRF) — the application fetches internal resources based on user-supplied URLs
* **Correct Answer:** B) The `' OR '1'='1` payload is a classic SQL injection string that alters the WHERE clause of a login query from `WHERE username = 'input'` to `WHERE username = '' OR '1'='1'`, making the condition always true and bypassing authentication.
* **Distractor Analysis:**
  * *Why B is correct:* SQL injection occurs when user input is concatenated into SQL without sanitization. The `OR '1'='1'` payload makes the WHERE clause always evaluate to true, returning all rows (or the first user). DAST confirms this by observing that the 200 response contains actual account data rather than a login failure.
  * *Why A is incorrect:* XSS involves injecting JavaScript into HTML responses that executes in the victim's browser. The `' OR '1'='1` payload contains SQL syntax, not JavaScript, and the described response is user data retrieval, not script execution.
  * *Why C is incorrect:* Broken authentication from blank passwords would involve sending an empty password field, not a SQL injection string. The payload used is specifically designed to alter SQL logic.
  * *Why D is incorrect:* SSRF exploits occur when an application fetches internal or external URLs based on user-controlled input. A SQL injection test against a login form is unrelated to SSRF.

---

**Question 5**
A DevSecOps pipeline runs OWASP ZAP in active scan mode against the staging environment and produces 200 findings. The team wants to configure the scan so only HIGH and CRITICAL risk findings fail the pipeline. Which ZAP configuration approach achieves this?

* A) Limit the scan to only the login and registration endpoints so fewer total findings are generated
* B) Configure the ZAP GitHub Actions step with a `fail_action: true` flag and set `cmd_options` to use a scan policy that maps HIGH and CRITICAL risk levels to a fail exit code, leaving MEDIUM and LOW as warnings
* C) Run the ZAP scan on a weekly schedule rather than on every pipeline run, so fewer findings accumulate per run
* D) Suppress all MEDIUM and LOW findings globally in the ZAP configuration so the total finding count is reduced before the threshold check
* **Correct Answer:** B) ZAP's `fail_action` and scan policy options allow teams to define which risk levels trigger a non-zero exit code (pipeline failure) versus which levels are reported as informational, matching the team's risk threshold.
* **Distractor Analysis:**
  * *Why B is correct:* The OWASP ZAP GitHub Actions integration supports `fail_action: true` combined with minimum risk level options. Configuring a scan policy that only raises exit code 1 on HIGH/CRITICAL findings allows the pipeline to pass for lower-severity issues while enforcing blocking on critical risks.
  * *Why A is incorrect:* Limiting scan scope to fewer endpoints reduces DAST coverage, potentially missing vulnerabilities elsewhere in the application. The goal is to tune the reporting threshold, not reduce testing coverage.
  * *Why C is incorrect:* Weekly scheduled scans cannot serve as pipeline gates on individual deployments. A security issue introduced on Monday would not be caught until the weekly scan, potentially reaching production.
  * *Why D is incorrect:* Globally suppressing MEDIUM and LOW findings removes them from the report, reducing visibility of lower-severity issues that may collectively represent significant risk. Threshold-based failure configuration is preferable to global suppression.
