
# Reading Guide — Module 03: Application Attacks and Software Vulnerabilities

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 | Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

---

## Introduction

Module 03 focuses on attacks that target application software — the code running on web servers, databases, and endpoints. These attacks exploit flaws in how applications handle input, manage memory, and control file access. The SY0-701 exam presents application attack scenarios and asks you to identify the vulnerability type, the exploitation mechanism, and the correct defensive control.

---

## 1. Injection Attack Reference

| Attack Type | Target | Exploitation Mechanism | Primary CIA Impact | Fix |
|---|---|---|---|---|
| SQL Injection | Relational database via web app | Untrusted input inserted into SQL query structure | Confidentiality, Integrity | Parameterized queries / prepared statements |
| Command Injection | OS shell via application | User input appended to shell command without sanitization | Integrity, Availability | Input validation; avoid shell calls; use safe APIs |
| LDAP Injection | Directory service | Untrusted input inserted into LDAP query | Confidentiality | Input validation; parameterized LDAP queries |
| XML Injection | XML parser | Malicious XML elements inserted via input | Confidentiality, Integrity | Input validation; schema validation |
| XPath Injection | XML/XPath query | Untrusted input inserted into XPath query syntax | Confidentiality | Parameterized XPath queries |

### SQL Injection Sub-Types

**In-Band SQLi** — results are returned in the same HTTP response. The most common and straightforward type.

**Blind SQLi** — the application does not return results directly. The attacker infers information from application behavior: Boolean-based (true/false responses) or Time-based (delays from injected wait commands).

**Out-of-Band SQLi** — results are delivered through a separate channel such as a DNS lookup or HTTP request to an attacker-controlled server. Used when in-band and blind techniques are impractical.

---

## 2. Cross-Site Scripting (XSS) Reference

| XSS Type | How Script Is Delivered | Persistence | Who Is Affected |
|---|---|---|---|
| Stored (Persistent) | Script stored in application database or filesystem | Permanent until removed | All users who load the affected page |
| Reflected (Non-Persistent) | Script embedded in URL or form parameter, reflected in response | None — requires click | User who clicks the crafted link |
| DOM-Based | Script manipulates Document Object Model in browser | None on server | User whose browser processes crafted input |

### XSS Impact Chain

1. Attacker injects malicious JavaScript into a vulnerable input field.
2. Script executes in victim's browser with victim's session permissions.
3. Attacker harvests session cookies, performs actions as the victim, or redirects the victim to a phishing page.

### XSS Defenses

* Output encoding appropriate to the output context (HTML, JavaScript, URL encoding).
* Content Security Policy (CSP) header specifying trusted script sources.
* Input validation rejecting script-related characters.
* HttpOnly cookie flag preventing script access to session cookies.
* X-XSS-Protection header enabling browser built-in XSS filtering.

---

## 3. CSRF vs. XSS Comparison

| Property | XSS | CSRF |
|---|---|---|
| Attack vector | Injected script on the target site | Hidden request from a different origin |
| Who is targeted | Other users who visit the injected page | The authenticated user's existing session |
| What the browser does | Runs attacker's script as legitimate site code | Sends attacker's request using victim's stored cookies |
| Primary defense | Output encoding, CSP, HttpOnly | CSRF tokens, SameSite cookies |
| CIA property violated | Confidentiality (cookie theft), Integrity (action as victim) | Integrity (unauthorized action performed) |

---

## 4. Memory Exploitation Reference

| Vulnerability | Description | Exploitation Technique | OS Defense |
|---|---|---|---|
| Buffer Overflow | Writing past end of fixed-size buffer | Overwrite return address to redirect execution | ASLR, DEP/NX, stack canaries |
| Heap Overflow | Writing past end of heap-allocated buffer | Corrupt heap metadata or adjacent heap objects | ASLR, heap integrity checks |
| Integer Overflow | Arithmetic exceeds data type maximum and wraps around | Bypass size or bounds checks | Input validation, compiler checks |
| Use-After-Free | Using a freed memory pointer that may be reallocated | Control value at freed pointer to hijack execution | Memory-safe languages, compiler sanitizers |
| Format String | User-controlled format string passed to printf-style functions | Read or write arbitrary memory addresses | Compiler warnings, avoid %n specifier |

### Memory Defense Mechanisms

**ASLR — Address Space Layout Randomization:** The OS randomizes the base addresses of the stack, heap, and loaded libraries at each program launch. An attacker who cannot predict addresses cannot reliably redirect execution.

**DEP / NX — Data Execution Prevention / No-Execute bit:** Marks memory regions such as the stack and heap as non-executable. Even if an attacker injects shellcode into a data region, the processor refuses to execute code from that region.

**Stack Canaries:** The compiler inserts a random value between local variables and the return address on the stack. Before a function returns, the runtime checks whether the canary value is unchanged. If overwritten, the program aborts rather than following the corrupted return address.

---

## 5. Additional Application Vulnerabilities

**Directory Traversal (Path Traversal):** An application uses user-supplied input to construct file paths without validation. By inserting path traversal sequences, an attacker navigates outside the web root to read system files. Defense: validate paths against an allowlist; canonicalize paths and confirm they begin with the expected base directory.

**SSRF — Server-Side Request Forgery:** The attacker causes a server-side application to make HTTP requests to internal addresses it cannot reach directly. In cloud environments, SSRF can reach instance metadata endpoints that expose credentials. Defense: restrict outbound URLs; block requests to private IP ranges.

**Insecure Direct Object Reference (IDOR):** An application exposes internal object identifiers in URLs or parameters without authorization checks. An attacker who increments an ID parameter can access another user's records. Defense: enforce authorization checks on every object access, not just at login.

**Security Misconfiguration:** Default credentials not changed, debug mode enabled in production, unnecessary services running, excessive file permissions. Defense: hardening checklists applied at deployment; automated configuration scanning.

**Sensitive Data Exposure:** Applications store or transmit sensitive data without adequate protection. Defense: encrypt sensitive data at rest with AES-256 and in transit with TLS 1.2 or higher; hash passwords with bcrypt, Argon2, or PBKDF2.

---

## 6. Static vs. Dynamic Testing Comparison

| Property | SAST | DAST | Fuzzing | Penetration Test |
|---|---|---|---|---|
| When performed | During development | Against running application | During QA or security testing | Pre-deployment or periodically |
| What is examined | Source code, bytecode, binaries | Application inputs and outputs | Application input handling | Full attack surface |
| Requires running app | No | Yes | Yes | Yes |
| Good at finding | Hardcoded credentials, injection patterns | Auth flaws, runtime injection, session issues | Edge-case input crashes | Business logic flaws, chained exploits |
| Limitation | Cannot detect runtime-only issues | Cannot see all code paths | Limited scope | Requires skilled tester; point-in-time |

---

## 7. CVSS Scoring Overview

| Score Range | Severity | Typical Example |
|---|---|---|
| 0.0 | None | No security impact |
| 0.1 – 3.9 | Low | Minimal impact; significant preconditions required |
| 4.0 – 6.9 | Medium | Limited disclosure or requires authentication |
| 7.0 – 8.9 | High | Significant impact; authenticated code execution |
| 9.0 – 10.0 | Critical | Remote code execution without authentication |

CVSS Base Score factors: Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, and Confidentiality/Integrity/Availability impact.

---

## 8. Secure Development Principles Summary

| Principle | Description | Attack It Prevents |
|---|---|---|
| Input validation | Validate type, format, length, range for all external input | Injection, buffer overflow, path traversal |
| Output encoding | Encode output for the specific rendering context | XSS |
| Parameterized queries | Use prepared statements for all database interactions | SQL injection |
| Least privilege | Application runs with minimum required permissions | Limits damage if compromised |
| Error handling | Never expose internal details in user-facing errors | Information disclosure |
| Secure defaults | Disable unnecessary features; change default credentials | Misconfiguration attacks |
| CSRF tokens | Unique tokens in all state-changing forms | CSRF |
| HttpOnly / SameSite cookies | Limit cookie accessibility from script and cross-origin requests | XSS cookie theft, CSRF |

---

## 9. Supplemental Resources

**1. OWASP Top 10 — 2021 Edition**
<https://owasp.org/www-project-top-ten/>
The authoritative ranked list of the ten most critical web application security risks, maintained by the Open Web Application Security Project. Directly maps to the injection, XSS, IDOR, SSRF, and security misconfiguration vulnerabilities covered in Module 03, and provides detailed descriptions, attack scenarios, and prevention guidance for each category.

**2. OWASP Web Security Testing Guide (WSTG)**
<https://owasp.org/www-project-web-security-testing-guide/>
A comprehensive open-source guide for testing web application security. Use it to understand how testers identify SQL injection, XSS, CSRF, directory traversal, and SSRF in practice — directly reinforcing the Module 03 vulnerability recognition and defense content tested on SY0-701.

**3. NIST National Vulnerability Database (NVD) — CVE Search**
<https://nvd.nist.gov/vuln/search>
The US government repository of vulnerability data using the CVE standard and CVSS scoring. Search for real CVE entries for SQL injection, buffer overflow, or XSS to see how CVSS scores are assigned to each factor (Attack Vector, Complexity, Privileges Required) covered in Module 03 Section 7, and to observe the relationship between vulnerability class and severity score.

---

## 9. Security+ Exam Tips for Module 03

**Exam Tip 1:** SQL injection fix = parameterized queries (prepared statements). Input filtering alone is easily bypassed. Stored procedures alone are insufficient unless they also use parameters.

**Exam Tip 2:** XSS injects script that runs on the legitimate site in the victim's browser. CSRF forces the victim's browser to send requests to the legitimate site from an external origin. The direction of attack is the key differentiator.

**Exam Tip 3:** Stored XSS affects every visitor to the compromised page. Reflected XSS requires the victim to click a crafted link. Look for whether the malicious content is stored in a database.

**Exam Tip 4:** Buffer overflow defenses — ASLR randomizes addresses; DEP/NX marks data memory non-executable; stack canaries detect stack smashing before the return address is used. All three are used together.

**Exam Tip 5:** SAST requires source code access and runs without executing the application. DAST requires a running application and tests from the outside. Neither alone is sufficient.

**Exam Tip 6:** IDOR is about missing authorization checks. Symptom: changing an ID parameter in a URL returns another user's data. Fix: server-side authorization enforcement on every object access.

**Exam Tip 7:** SSRF causes the server to make requests on the attacker's behalf. In cloud environments this commonly targets the instance metadata service. Defense: restrict which hosts the server may request.

**Exam Tip 8:** CVSS Critical (9.0–10.0) = remote code execution without authentication. Know the five severity ranges and their score thresholds.

---

## 10. Required Study Resources

* Professor Messer's SY0-701 video lectures and study notes for Domain 2 application attack objectives, available free at professormesser.com.
* CompTIA's official SY0-701 exam objectives document, available at comptia.org.

---

## 11. Study Checklist

* [ ] Define SQL injection, command injection, LDAP injection, and XML injection. State the fix for each.
* [ ] Distinguish stored XSS, reflected XSS, and DOM-based XSS by delivery mechanism and persistence.
* [ ] Explain the difference between XSS and CSRF including the direction of attack and respective defenses.
* [ ] Describe buffer overflow, heap overflow, integer overflow, and use-after-free vulnerabilities.
* [ ] Explain ASLR, DEP/NX, and stack canaries and what each protects against.
* [ ] Describe directory traversal and SSRF and state the fix for each.
* [ ] Compare SAST and DAST by when each runs, what each finds, and what each cannot find.
* [ ] Interpret a CVSS score and explain what Critical means in terms of exploitation conditions.
* [ ] List the eight secure development principles and match each to the attack it prevents.
* [ ] Complete the Module 03 Lab activity.
* [ ] Post your initial discussion response by Wednesday at 11:59 PM.
* [ ] Post two peer replies by Sunday at 11:59 PM.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 03 Reading Guide

Proprietary and Confidential. Not for disclosure outside of authorized course use.
