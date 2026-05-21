# Quiz: Module 13 - Web Application Security Analysis
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
Which vulnerability class allows an attacker to inject client-side scripts into web pages viewed by other users, enabling session hijacking, credential theft, or malicious redirects?

*   A) SQL Injection — the attacker inserts malicious SQL into an input field to manipulate backend database queries
*   B) Cross-Site Scripting (XSS) — the attacker injects malicious scripts into web pages that execute in the browsers of other users visiting the affected page
*   C) Server-Side Request Forgery (SSRF) — the attacker causes the web server to make unauthorized HTTP requests to internal or external targets
*   D) Command Injection — the attacker executes arbitrary OS commands on the web server by injecting shell syntax into an application input field
*   **Correct Answer:** B) Cross-Site Scripting (XSS) — the attacker injects malicious scripts into web pages that execute in the browsers of other users visiting the affected page.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SQL Injection targets backend database queries, not the browsers of other users. Its impact is unauthorized database access, not client-side script execution.
    *   *Why B is correct:* XSS occurs when untrusted user input is included in HTML output without encoding, allowing the attacker's script to run in victims' browsers. Stored XSS is particularly high-impact because the payload persists in the application database and executes for every user who loads the affected page — enabling mass session cookie theft or credential harvesting.
    *   *Why C is incorrect:* SSRF causes the server itself to make requests to unintended targets; it does not inject scripts into pages viewed by other users.
    *   *Why D is incorrect:* Command injection executes OS commands on the server; it does not target other users' browsers.

---

**Question 2**
In web application security analysis, which of the following most accurately defines **SQL injection (SQLi)**?

*   A) A vulnerability in which an attacker causes the web server to send HTTP requests to internal systems by supplying a crafted URL in a user-controlled parameter
*   B) A vulnerability in which malicious SQL code is inserted into an application input field that is passed unsanitized to a backend database query, allowing unauthorized data access, authentication bypass, or database manipulation
*   C) A vulnerability in which an attacker intercepts HTTP traffic between a client and server and modifies request parameters before they reach the application
*   D) A vulnerability in which the application stores sensitive data in client-side cookies without encryption, allowing an attacker who reads the cookie to extract credentials
*   **Correct Answer:** B) A vulnerability in which malicious SQL code is inserted into an application input field that is passed unsanitized to a backend database query, allowing unauthorized data access, authentication bypass, or database manipulation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Causing the server to make requests to internal systems by supplying a crafted URL describes Server-Side Request Forgery (SSRF), not SQL injection.
    *   *Why B is correct:* SQLi exploits the failure to separate SQL code from user-supplied data. When input like `' OR '1'='1` is passed directly into a query string, the database executes attacker-controlled logic. The correct fix is parameterized queries (prepared statements) that treat user input as data, not executable SQL code.
    *   *Why C is incorrect:* Intercepting and modifying HTTP traffic in transit describes a man-in-the-middle (MitM) attack; it is a network-level attack, not a web application injection vulnerability.
    *   *Why D is incorrect:* Storing unencrypted sensitive data in client-side cookies is an insecure storage vulnerability; it does not describe the injection of SQL code into database queries.

---

**Question 3**
A security analyst reviews Apache web server access logs and finds the following request: `GET /search?q=%27+OR+1%3D1--+HTTP/1.1`. The `%27` decodes to `'` and `%3D` decodes to `=`. Which attack does this request most strongly indicate?

*   A) A cross-site scripting (XSS) attack — the attacker is injecting a script tag into the search parameter to execute in the browser of an administrator who views the search results
*   B) A SQL injection attack — the attacker is submitting `' OR 1=1--` to attempt to bypass authentication or extract all records from the database query handling the search parameter
*   C) A directory traversal attack — the attacker is attempting to navigate outside the web root to access sensitive files on the underlying server filesystem
*   D) A CSRF attack — the attacker is forging a cross-site request to perform an unauthorized action on behalf of an authenticated user
*   **Correct Answer:** B) A SQL injection attack — the attacker is submitting `' OR 1=1--` to attempt to bypass authentication or extract all records from the database query handling the search parameter.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* XSS payloads contain script tags or JavaScript event handlers (e.g., `<script>alert(1)</script>` or `onerror=`). The decoded payload `' OR 1=1--` contains SQL syntax — a single quote to break out of the query string and a comment (`--`) to truncate remaining SQL — which is the signature of SQLi, not XSS.
    *   *Why B is correct:* `' OR 1=1--` is a classic SQL injection test string. The single quote terminates the intended string literal in the SQL query, `OR 1=1` makes the WHERE condition always true (returning all rows), and `--` comments out the remainder of the original query. Seeing this in URL-encoded form in web logs is a definitive SQLi indicator.
    *   *Why C is incorrect:* Directory traversal payloads use path traversal sequences such as `../../../etc/passwd`. The decoded payload here contains SQL syntax, not path traversal characters.
    *   *Why D is incorrect:* CSRF attacks forge requests that appear to originate from an authenticated user's browser; they do not inject SQL syntax into query parameters.

---

**Question 4**
An analyst discovers that a web application is vulnerable to Server-Side Request Forgery (SSRF). An attacker has used the vulnerability to reach the AWS EC2 instance metadata endpoint at `http://169.254.169.254/latest/meta-data/iam/security-credentials/` and retrieve temporary IAM credentials. Which security control would most directly have prevented this specific SSRF exploitation?

*   A) Enable HTTPS (TLS 1.3) for all connections to the web application to encrypt traffic between clients and the server
*   B) Implement URL allowlisting on the server-side HTTP request functionality to permit only approved external domains, blocking requests to internal IP ranges including the metadata endpoint
*   C) Deploy a Web Application Firewall (WAF) in blocking mode to detect and reject incoming requests containing suspicious payload patterns from external clients
*   D) Require input validation on all form fields to reject inputs containing special characters such as angle brackets and single quotes
*   **Correct Answer:** B) Implement URL allowlisting on the server-side HTTP request functionality to permit only approved external domains, blocking requests to internal IP ranges including the metadata endpoint.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* TLS encrypts traffic in transit between external clients and the server; it does not prevent the server from making outbound requests to internal metadata endpoints. The SSRF exploit originates from the server itself, not from an external attacker's direct connection.
    *   *Why B is correct:* SSRF is exploited when an application makes server-side HTTP requests to attacker-supplied URLs without validation. URL allowlisting restricts the destinations the server can request to a defined set of approved external domains, preventing requests to internal IP ranges like `169.254.169.254` (cloud metadata), `10.x.x.x`, or `172.16.x.x`. This is the primary preventive control for SSRF.
    *   *Why C is incorrect:* A WAF inspects inbound client requests; it is not positioned to block the server's outbound HTTP requests to internal services that the SSRF attack generates. A WAF cannot intercept requests the server initiates internally.
    *   *Why D is incorrect:* Rejecting angle brackets and single quotes addresses XSS and SQLi injection vectors; these characters are not relevant to SSRF, which exploits the server's ability to make HTTP requests to arbitrary URLs.

---

**Question 5**
An organization wants to detect active web application attacks against its customer-facing e-commerce site and reduce the time from attack initiation to analyst alert. Which two controls together best achieve this goal?

*   A) Deploy full-disk encryption on the web application servers and configure automated certificate renewal to prevent TLS expiration downtime
*   B) Integrate web application access logs into the SIEM with correlation rules that alert on patterns indicating SQLi (repeated 500 errors from the same IP), XSS (script tag strings in request parameters), and directory enumeration (sequential 404 errors) — combined with deploying a WAF in detection mode to generate alerts on matched attack signatures
*   C) Enforce a Content Security Policy (CSP) header on all application responses to restrict which scripts can execute in users' browsers
*   D) Require all developers to complete secure coding training and conduct quarterly penetration tests of the web application to identify new vulnerabilities before attackers do
*   **Correct Answer:** B) Integrate web application access logs into the SIEM with correlation rules that alert on SQLi, XSS, and enumeration patterns — combined with deploying a WAF in detection mode to generate alerts on matched attack signatures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full-disk encryption and certificate renewal address data-at-rest confidentiality and availability; they have no effect on detecting active web attacks in real time.
    *   *Why B is correct:* SIEM log integration with web-attack correlation rules provides pattern-based detection (e.g., five 500 errors in 60 seconds from one IP → SQLi alert), and a WAF in detection mode adds signature-based alerting on known attack payloads. Together these cover both anomaly-based and signature-based detection for the most common web attack categories, directly addressing the "reduce time to alert" objective.
    *   *Why C is incorrect:* CSP is a preventive browser-side control that limits XSS impact for end users; it does not detect or alert on active attacks reaching the server.
    *   *Why D is incorrect:* Secure coding training and penetration testing are proactive vulnerability management activities; they do not provide real-time detection of active attacks in production.
