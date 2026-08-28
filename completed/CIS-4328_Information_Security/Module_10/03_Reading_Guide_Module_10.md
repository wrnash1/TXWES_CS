# Reading Guide: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Overview

This reading guide supports the Module 10 video lectures on application security. Application security content appears throughout the Security+ exam, particularly in scenarios involving web application vulnerabilities and secure development practices. Complete all readings before the quiz and lab.

---

## Learning Objectives

By the end of this module, you will be able to:

1. Describe the security activities that occur in each phase of the Secure SDLC
2. Apply the STRIDE threat model to identify threats in a system design
3. Explain the OWASP Top 10 vulnerabilities from an attacker and defender perspective
4. Distinguish between input validation and output encoding and apply each correctly
5. Describe secure coding practices including error handling, cryptography, and secrets management
6. Conduct a structured security-focused code review using a checklist approach
7. Compare SAST and DAST tools: what each finds, when each runs, and their limitations
8. Describe how SCA tools address third-party dependency risks

---

## Assigned Readings (Zero-Cost / Open Access)

### Primary Reading

**OWASP Top 10 — 2021**

- Access: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
- Read: All 10 categories with their description, example attack scenarios, and prevention guidance
- Focus areas: A01 Broken Access Control, A03 Injection, A07 Identification and Authentication Failures, A08 Software and Data Integrity Failures
- Estimated reading time: 45–60 minutes

**OWASP Input Validation Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- Read: Full document
- Focus areas: allowlist vs. blocklist, server-side enforcement, canonicalization

**OWASP XSS Prevention Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- Read: Full document
- Focus areas: output encoding rules by context, Content Security Policy

### Supplemental Reading

**OWASP SQL Injection Prevention Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Read: Full document
- Focus areas: parameterized queries, stored procedures, escaping as last resort

**OWASP Authentication Cheat Sheet**

- Access: [https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- Read: Sections 1–4 (password storage, authentication guidelines, session management basics)

**Microsoft Threat Modeling Tool Documentation — STRIDE**

- Access: [https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats)
- Read: Full page
- Focus: STRIDE category definitions and example mitigations

---

## Key Terms and Definitions

**Secure SDLC (S-SDLC)** — A software development lifecycle that integrates security activities into every phase: requirements, design, implementation, testing, deployment, and maintenance.

**Threat Modeling** — A structured process for identifying, enumerating, and prioritizing security threats against a system before implementation.

**STRIDE** — A threat modeling framework representing six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.

**Trust Boundary** — A line in a data flow diagram marking where data moves between security domains with different privilege levels; a primary focus of threat modeling.

**OWASP Top 10** — The Open Web Application Security Project's list of the ten most critical web application security risks, updated periodically.

**Broken Access Control (A01)** — A class of vulnerabilities where users can act outside their intended permissions, including IDOR and horizontal/vertical privilege escalation.

**IDOR (Insecure Direct Object Reference)** — A specific type of broken access control where an application exposes a direct reference to an internal object (such as a database key) without verifying the requesting user's authorization.

**Injection (A03)** — A class of attacks where untrusted data is sent to an interpreter as part of a command or query, causing the interpreter to execute attacker-controlled data as code.

**SQL Injection** — An injection attack that inserts malicious SQL code into a query, allowing attackers to bypass authentication, retrieve data, or modify the database.

**Parameterized Query** — A SQL query template where user-supplied values are passed separately from the query structure, preventing injection; also called a prepared statement.

**XSS (Cross-Site Scripting)** — An injection attack where malicious scripts are injected into web pages viewed by other users; exploits insufficient output encoding.

**Reflected XSS** — XSS where the malicious script is reflected off the web server in the immediate response to a crafted request.

**Stored XSS** — XSS where the malicious script is permanently stored on the server (in a database, comment field, etc.) and served to all users who view the content.

**CSP (Content Security Policy)** — A browser security header that restricts the sources from which scripts, styles, and other resources may be loaded.

**Input Validation** — The process of verifying that data entering an application conforms to expected type, length, range, and format before processing.

**Output Encoding** — The process of converting special characters in data to safe representations appropriate for the output context, preventing injection into HTML, JavaScript, SQL, or other languages.

**SAST (Static Application Security Testing)** — Automated analysis of source code, bytecode, or binary code to identify security vulnerabilities without executing the application.

**DAST (Dynamic Application Security Testing)** — Automated security testing of a running application from the outside, simulating external attacker behavior.

**IAST (Interactive Application Security Testing)** — Security testing that uses an agent embedded in the running application to monitor execution during functional tests.

**SCA (Software Composition Analysis)** — Automated analysis of third-party libraries and open-source dependencies to identify known vulnerabilities.

**Credential Stuffing** — An attack that uses breach databases of stolen username/password pairs to authenticate against other services, exploiting password reuse.

**Defense in Depth** — A security strategy that uses multiple overlapping controls so that the failure of one control does not lead to full compromise.

**Shift Left** — The practice of moving security testing and validation earlier in the development lifecycle to reduce the cost and impact of discovered vulnerabilities.

---

## Concept Deep Dives

### STRIDE Applied — Worked Example

Imagine you are threat modeling a web application login endpoint. The endpoint accepts a username and password over HTTPS and validates credentials against a database.

Apply STRIDE at the trust boundary where the user's browser submits credentials to the web server:

| Threat | STRIDE Category | Example | Mitigation |
|---|---|---|---|
| Attacker submits stolen credentials | Spoofing | Credential stuffing attack | MFA, rate limiting, breach password checking |
| Attacker intercepts credentials in transit | Tampering | MITM on HTTP (not HTTPS) | Enforce HTTPS, HSTS header |
| User denies logging in | Repudiation | Insider disputes audit log | Log authentication events with timestamp and IP |
| Error message reveals username validity | Information Disclosure | "That username does not exist" | Return generic error: "Invalid username or password" |
| Attacker floods login with requests | Denial of Service | Brute force / rate exhaustion | Rate limiting, CAPTCHA, account lockout |
| Attacker escalates after login | Elevation of Privilege | Exploits session fixation | New session token on authentication |

Every row becomes a security requirement or design decision.

### SAST vs. DAST — Decision Guide

| Question | SAST | DAST |
|---|---|---|
| When does it run? | At code commit / build time | Against running application in staging |
| Does it need source code? | Yes | No |
| Does it need the app to run? | No | Yes |
| False positive rate | Higher | Lower |
| Finds code-level flaws? | Yes | Partially |
| Finds runtime/config flaws? | No | Yes |
| Can pinpoint vulnerable line? | Yes | No |
| Suitable for production use? | Yes (code review) | No (can disrupt services) |

---

## Security+ Exam Alignment

### Relevant Exam Objectives (SY0-701)

- **1.3** — Explain various types of vulnerabilities (web application vulnerabilities: injection, XSS, IDOR, CSRF, directory traversal, insecure deserialization)
- **2.4** — Explain the importance of resilience and recovery in security architecture (secure coding, code review)
- **2.6** — Explain the security implications of proper hardware, software, and data asset management (SAST, DAST, SCA)

### High-Probability Exam Topics from This Module

- Distinguishing SQL injection from XSS: injection targets the database/server; XSS targets the client browser
- Identifying the correct defense for injection attacks (parameterized queries, not input validation alone)
- Distinguishing reflected XSS from stored XSS
- Identifying IDOR as a broken access control vulnerability
- Knowing that SAST runs without executing the application; DAST requires a running application
- Understanding credential stuffing vs. brute force (stuffing uses real breach credentials; brute force tries all combinations)

---

## Review Questions (Self-Check — Not Graded)

1. A developer writes a search function that builds a SQL query by concatenating user input with no validation or parameterization. An attacker enters `'; DROP TABLE users; --`. What type of attack is this and what is the correct remediation?

2. A web application displays a user's profile name on the page without encoding. A user saves their profile name as `<script>alert('XSS')</script>`. When another user views the first user's profile, a JavaScript alert fires. What type of XSS is this and what control would prevent it?

3. A developer implements server-side access control for an API endpoint but the front-end JavaScript also hides the "Admin" button from non-admin users. An attacker bypasses the JavaScript and calls the API endpoint directly. Is the application vulnerable? Why?

4. A SAST tool flags a line of code as a potential SQL injection vulnerability. The developer argues the flagged code is actually safe because the input is already validated upstream. Is the developer necessarily correct? What is the name of this SAST limitation?

5. An organization wants to find vulnerabilities in the third-party npm packages their Node.js application uses. Which tool category addresses this need?

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 10*
