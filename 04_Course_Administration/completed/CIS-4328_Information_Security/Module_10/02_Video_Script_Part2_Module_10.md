# Video Script: Module 10 — Application Security (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — OWASP Top 10 Continued: Access Control and Authentication (4 minutes)

Welcome back. In Part 1 we covered the Secure SDLC, threat modeling, injection attacks, and input/output handling. Now we continue through the OWASP Top 10 and close with security tooling and code review.

### A01: Broken Access Control

This has been the number one OWASP category since 2021, and it deserves that position. Access control failures allow users to act outside their intended permissions — accessing other users' data, performing privileged functions, or viewing resources they should not see.

**Horizontal privilege escalation** means accessing another user's resources at the same privilege level. Example: a banking application uses the URL `https://bank.com/account?id=1234`. The attacker changes `id=1234` to `id=1235` and views another customer's account. This is called **Insecure Direct Object Reference (IDOR)**.

**Vertical privilege escalation** means gaining higher-level access. Example: a regular user manipulates a hidden form field to send `role=admin` in a request, and the server accepts it.

**Preventing Access Control Failures**

- Enforce access control on the server side — never trust client-supplied role or permission data
- Use indirect object references (internal IDs that map to objects, not guessable sequential integers)
- Apply deny-by-default: deny access unless explicitly granted
- Log all access control failures and alert on patterns suggesting enumeration

### A07: Identification and Authentication Failures

Authentication vulnerabilities allow attackers to compromise passwords, keys, or session tokens to assume other users' identities.

**Common authentication weaknesses:**

- Allowing weak passwords (no minimum complexity, no breach password checking)
- No account lockout after failed attempts (enables brute force and credential stuffing)
- Weak session tokens that are predictable or short enough to brute force
- Sessions that do not expire after a reasonable idle period
- Insecure session token transmission (sent over HTTP, stored in localStorage where XSS can steal it)
- Improper logout — session remains valid on the server after the user clicks "Log out"

**Credential stuffing** deserves special mention. Attackers purchase or download breach databases containing email/password pairs and try those credentials against other services. Because users reuse passwords, this attack is highly effective. Detection: monitor for high volumes of failed logins across many accounts from distributed IP addresses.

**Secure authentication best practices:**

- Require MFA for all privileged accounts; offer it for all accounts
- Use secure password hashing: bcrypt, Argon2, or PBKDF2 — never MD5 or SHA-1 without salting and stretching
- Implement secure session management: cryptographically random session tokens (128+ bits), HttpOnly and Secure cookie flags, SameSite cookie attribute, session invalidation on logout

### A08: Software and Data Integrity Failures

This category covers failures in software update mechanisms and CI/CD pipeline integrity. An attacker who can inject code into your build pipeline or software update process can compromise every system that receives the update.

**Supply chain attacks** exploit this vector. The SolarWinds attack (2020) modified the build system to inject malicious code into legitimate software updates. Every organization that installed the update was compromised.

Mitigations: code signing for artifacts, verified checksums, dependency pinning, software composition analysis (SCA), and secured CI/CD pipelines with access controls.

---

## Segment 2 — Secure Coding Practices (4 minutes)

Beyond input validation and output encoding, secure coding encompasses a broader set of practices that reduce the attack surface of application code.

### Principle of Least Privilege in Code

Every component of your application should operate with the minimum permissions required. A database connection should use a database account that only has SELECT, INSERT, UPDATE privileges on the tables it needs — not DBA-level access. A file processing service should only read from and write to its designated directory — not have unrestricted file system access.

### Error Handling and Logging

**Error handling — fail securely and quietly for users, verbosely for administrators.** Error messages shown to users should never reveal:

- Stack traces (reveal code paths and technology stack)
- Database error messages (reveal schema details)
- Internal server paths or hostnames
- Version information for servers or frameworks

Log detailed error information server-side where only administrators can access it. Return a generic user-facing message: "An error occurred. Please try again or contact support."

**Security-relevant logging** should capture:

- Authentication events (success and failure with username, timestamp, source IP)
- Authorization failures (user attempted to access resource they cannot access)
- Input validation failures (user submitted data outside expected parameters)
- High-value transactions (payments, account changes, privilege escalations)

Logs must be tamper-evident. Write them to a write-protected location or ship them to a centralized SIEM immediately.

### Cryptographic Best Practices in Code

**Use established libraries, never implement your own cryptography.** Cryptographic algorithms are extremely difficult to implement correctly. Even expert cryptographers make implementation mistakes. Use standard libraries: OpenSSL, libsodium, Java's JCA, Python's cryptography library.

**Algorithm choices:**

- Symmetric encryption: AES-256-GCM (provides both confidentiality and integrity)
- Asymmetric encryption: RSA-2048 minimum, RSA-3072 or ECC preferred
- Hashing (non-password): SHA-256 minimum; SHA-3 for new designs
- Password hashing: bcrypt (cost factor 12+), Argon2id (preferred for new systems)
- TLS: 1.2 minimum, 1.3 preferred; disable SSLv3, TLS 1.0, TLS 1.1

**Secrets in code — the cardinal rule:** Never commit credentials, API keys, private keys, or database passwords to source code or version control. Once in a git repository, a secret persists in history even if deleted in a later commit. Use secrets management tools: AWS Secrets Manager, Azure Key Vault, HashiCorp Vault, or environment variables injected at runtime.

### Defense in Depth in Application Architecture

Apply multiple overlapping security controls rather than relying on any single protection. Example:

- WAF blocks common attack patterns at the network edge
- Input validation rejects malformed data at the application boundary
- Parameterized queries prevent SQL injection at the data layer
- Database least privilege limits damage if injection succeeds
- Database audit logging detects anomalous query patterns

Each layer independently reduces risk. An attacker who bypasses the WAF still faces input validation. An attacker who exploits a validation gap still faces parameterized queries.

---

## Segment 3 — Code Review for Security (3 minutes)

Code review is the practice of having one or more developers examine code for defects before it merges into the main branch. Security-focused code review looks specifically for vulnerabilities.

### Manual Code Review

A security-focused manual code review follows these steps:

**Identify sensitive operations.** Focus review effort on authentication, authorization, cryptography, session management, file operations, database queries, and any code that processes untrusted input.

**Trace data flows.** Follow user-supplied data from where it enters the application to where it is used. Does it get validated? Does it get sanitized before reaching a database query or HTML output? Does it get encoded before being logged?

**Check for common patterns.** Reviewers build intuition for dangerous patterns:

- String concatenation with user input in SQL queries (injection risk)
- Direct use of user input in file paths (path traversal risk)
- Use of deprecated cryptographic functions (MD5, DES, SHA-1 for passwords)
- Hardcoded credentials or secrets
- `eval()` or similar dynamic code execution with user-controlled input

**Review error handling.** Ensure errors do not leak sensitive information. Ensure failures are handled gracefully.

### Security Code Review Checklist

Structure your review around these checkpoints:

- Input validation present on all externally supplied data?
- Output encoding applied before rendering data in HTML/JS/CSS/URL contexts?
- Parameterized queries used for all database interactions?
- Authentication and authorization enforced server-side?
- Session management follows secure practices?
- Cryptography uses approved algorithms and libraries?
- No hardcoded secrets?
- Error messages do not expose implementation details?
- Security-relevant events are logged?
- Third-party dependencies are up to date and from trusted sources?

### The Cost of Code Review

Code review catches approximately 60–65% of security defects according to research by Capers Jones. It is the most cost-effective security testing technique — far cheaper than finding the same defect in production. Make it a required gate, not an optional step.

---

## Segment 4 — SAST and DAST Integration (4 minutes)

Automated security testing tools complement manual code review. Security+ tests your understanding of what these tools do and when to use them.

### SAST — Static Application Security Testing

SAST tools analyze source code, bytecode, or binary code without executing the application. They find vulnerabilities by examining code patterns.

**What SAST finds well:**

- Injection vulnerabilities (string concatenation in queries)
- Hardcoded secrets and credentials
- Use of insecure cryptographic functions
- Buffer overflows and memory safety issues (in C/C++)
- Input validation gaps (data flowing from taint sources to dangerous sinks without sanitization)
- Security misconfigurations in code (disabled SSL verification, weak cipher selection)

**SAST limitations:**

- High false positive rate — tools flag code patterns that look dangerous but are safe in context; developers suffer alert fatigue
- Cannot find logic flaws or business logic vulnerabilities
- Cannot find runtime configuration issues or infrastructure problems
- Requires access to source code

**SAST tools:** Checkmarx, Semgrep, SonarQube, Veracode Static Analysis, Fortify, Bandit (Python), SpotBugs (Java)

**Integration in the SDLC:** SAST runs in the CI/CD pipeline on every commit or pull request. Findings block merges if severity exceeds a threshold. This is "shift-left security" in action — catching vulnerabilities before they reach production.

### DAST — Dynamic Application Security Testing

DAST tools test the running application from the outside, simulating an attacker. They send malicious input and observe responses.

**What DAST finds well:**

- Injection vulnerabilities that manifest at runtime (SQL injection, XSS, command injection)
- Authentication and session management weaknesses
- Security header misconfigurations (missing CSP, X-Frame-Options, HSTS)
- Server-side request forgery (SSRF)
- Exposed sensitive information in responses (stack traces, version banners)
- Unprotected API endpoints

**DAST limitations:**

- Does not require source code — but also cannot pinpoint the vulnerable line of code
- Lower false positive rate than SAST but may miss code paths not exercised during testing
- Can generate noisy HTTP traffic that triggers IDS alerts in production environments
- Slower than SAST — requires a running application

**DAST tools:** OWASP ZAP (open source, free), Burp Suite Pro, Nikto, Nessus Web App Scanning, Rapid7 InsightAppSec

**Integration in the SDLC:** DAST runs against a staging or test environment as part of the release pipeline, not against production. Running DAST against production risks disrupting services or triggering false incident alerts.

### SAST + DAST = Complementary Coverage

Neither tool replaces the other. The professional approach is to use both:

- SAST: early, frequent, catches code-level issues at commit time
- DAST: later, against a running application, catches runtime and configuration issues

Add **IAST (Interactive Application Security Testing)** for maximum coverage: an agent embedded in the running application monitors execution paths during functional testing, combining the depth of SAST with the runtime accuracy of DAST.

Add **SCA (Software Composition Analysis)** to identify vulnerabilities in third-party libraries and open-source dependencies. Tools: OWASP Dependency Check, Snyk, Black Duck.

### Security Testing in the Pipeline — Summary Flow

A mature AppSec pipeline looks like this:

**Code commit → SAST scan → Dependency check (SCA) → Code review → Merge → Build → DAST against staging → Security review gate → Production deployment**

At each gate, findings above a severity threshold block the pipeline. The pipeline does not penalize developers for finding issues — it rewards them for catching issues early before they become production incidents.

---

## Module 10 Full Summary

Application security is a discipline that spans the entire development lifecycle:

- Secure SDLC embeds security activities into every phase from requirements through maintenance
- Threat modeling with STRIDE identifies threats at design time, before code is written
- OWASP Top 10 represents the most critical web application vulnerabilities: injection, broken access control, authentication failures, insecure design, and more
- Input validation (server-side, allowlist, type/length/range/format) prevents malformed input from reaching application logic
- Output encoding prevents data from being interpreted as code in HTML, JavaScript, URL, and other contexts
- Secure coding practices: least privilege, safe error handling, approved cryptography, no hardcoded secrets
- Code review catches 60–65% of security defects before they reach production
- SAST analyzes code statically and integrates into CI/CD; DAST tests the running application; SCA checks third-party dependencies

These concepts map directly to Security+ Domain 2 objectives and you will see them in scenario questions. Complete the reading guide, lab, and quiz. See you in Module 11.

---

*End of Part 2 Script*
