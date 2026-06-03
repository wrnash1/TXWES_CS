# Video Script: Module 10 — Application Security (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Pre-Roll Slate

**[SHOW SLIDE: Course title card — "CIS-4328 Information Security | Module 10 | Texas Wesleyan University"]**

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome back to CIS-4328. I'm Professor Nash, and this is Module 10 — Application Security.

Every major breach you read about in the news has a software weakness somewhere in the kill chain. SQL injection, broken authentication, cross-site scripting — these are not exotic research discoveries. They are well-documented, well-understood, and entirely preventable. The OWASP Top 10 list exists precisely because these same categories appear again and again across thousands of real-world incidents.

In Part 1 of this module we are going to work through the OWASP Top 10 with enough depth that you can recognize each category on the Security+ exam and in the field. In Part 2 we will pivot to how development teams bake security into the software lifecycle before code ever ships.

Let's get started.

---

## Section 1 — Why Application Security Matters

**[SHOW SLIDE: Attack surface diagram — network, OS, application layers]**

Think of a target organization as three concentric rings. The outermost ring is the network perimeter — firewalls, routers, DMZ zones. The middle ring is the operating system and host — patch management, endpoint protection. The innermost ring is the application layer — the code that processes user input and business logic.

Perimeter defenses have matured dramatically over the last twenty years. Firewalls, IDS/IPS, and network segmentation make direct network attacks harder. Attackers adapted. They started going through the front door — through applications that are intentionally exposed to the internet because that is how business gets done.

The 2021 IBM Cost of a Data Breach report found that web application attacks accounted for the top initial attack vector for the third consecutive year. The Security+ exam domain "Application Security" in Domain 4 carries roughly 13 percent of the exam weight, and OWASP knowledge underlies almost every question in that domain.

---

## Section 2 — OWASP and the Top 10

**[SHOW SLIDE: OWASP logo and Top 10 list, 2021 edition]**

OWASP stands for the Open Web Application Security Project. It is a nonprofit foundation that maintains free, vendor-neutral guidance on application security. Their flagship publication is the OWASP Top 10 — a ranked list of the most critical web application security risks, updated roughly every three to four years.

The current edition is 2021. The Security+ SY0-701 exam references OWASP throughout its objectives. Let me walk you through each category.

---

## Section 3 — A01: Broken Access Control

**[SHOW SLIDE: A01 heading with padlock icon]**

Number one on the 2021 list is Broken Access Control. Access control enforces the rule that users can only act within their intended permissions. When access control breaks down, users can escalate privilege, view other users' data, or perform privileged actions.

A classic form is Insecure Direct Object Reference, or IDOR. Here is a simple scenario. A user logs into a banking application. Their account statement URL reads: `https://bank.example.com/statement?accountId=1042`. The developer assumed only authenticated users would see this page, but forgot to verify that the authenticated user actually owns account 1042. An attacker who changes the URL to `accountId=1043` may retrieve another customer's statement.

IDOR is not about guessing passwords. It is about the application trusting user-supplied input to identify protected objects without authorization checks.

Countermeasures include enforcing access control server-side, using indirect reference maps, and logging access control failures.

---

## Section 4 — A02: Cryptographic Failures

**[SHOW SLIDE: A02 heading — formerly "Sensitive Data Exposure"]**

A02 was renamed from "Sensitive Data Exposure" in 2021 to better capture the root cause. The problem is not just that data was exposed — it is that encryption was absent, broken, or misconfigured, and that failure led to exposure.

Common failures include transmitting sensitive data in cleartext over HTTP instead of HTTPS, using weak hashing algorithms like MD5 or SHA-1 for password storage, storing encryption keys alongside encrypted data, and using deprecated TLS versions like TLS 1.0.

A memorable example is the 2013 Adobe breach. Adobe stored 153 million user passwords using 3DES encryption — an encryption algorithm, not a one-way hash — and with the same initialization vector for every record. Researchers were able to deduce plain-text passwords by comparing ciphertext across similar password hints. Proper bcrypt or Argon2 hashing would have made cracking computationally infeasible.

---

## Section 5 — A03: Injection

**[SHOW SLIDE: A03 heading — SQL injection diagram]**

Injection ranks third in 2021, though it held the top spot for over a decade in prior editions. Injection occurs when untrusted data is sent to an interpreter as part of a command or query.

SQL injection is the most well-known variant. Consider a login form. The developer constructs a query like this: `SELECT * FROM users WHERE username='` plus the user input plus `'`. If an attacker enters `admin'--` as the username, the closing single-quote terminates the string and the double-dash comments out the rest of the WHERE clause, including the password check. The query becomes `SELECT * FROM users WHERE username='admin'--` and authentication is bypassed.

Other injection types include LDAP injection, XML injection, OS command injection, and template injection. The root cause is always the same — interpreter commands and data are mixed together without sanitization.

Defenses include parameterized queries, prepared statements, stored procedures with parameterized inputs, input validation, and least-privilege database accounts.

---

## Section 6 — A04: Insecure Design

**[SHOW SLIDE: A04 heading — design vs. implementation distinction]**

A04 is a newer category that distinguishes design flaws from implementation bugs. An insecure design cannot be fixed by proper implementation alone — the design itself is flawed.

An example is a password recovery feature that asks users to answer secret questions. Even if the implementation is technically correct, the design is weak because secret questions provide guessable answers. The correct design uses a time-limited token sent to a verified email or phone number.

Threat modeling is the countermeasure for insecure design. Threat modeling is a structured analysis of potential threats to a system conducted during the design phase, before any code is written. Common frameworks include STRIDE and PASTA.

---

## Section 7 — A05: Security Misconfiguration

**[SHOW SLIDE: A05 heading — default credentials image]**

Security Misconfiguration moved up in 2021 because cloud infrastructure expanded the attack surface dramatically. Misconfiguration includes default credentials left unchanged, unnecessary features or services enabled, overly permissive cloud storage bucket permissions, verbose error messages that reveal stack traces to attackers, and missing security hardening.

A high-profile example is the 2019 Capital One breach. An attacker exploited a misconfigured Web Application Firewall running on AWS to perform a Server-Side Request Forgery attack, ultimately accessing S3 buckets containing more than 100 million customer records.

The countermeasure is a repeatable hardening process — configuration baselines, CIS Benchmarks, automated configuration scanning, and change management.

---

## Section 8 — A06: Vulnerable and Outdated Components

**[SHOW SLIDE: A06 — dependency tree diagram]**

Modern applications do not exist in isolation. They import dozens or hundreds of open-source libraries, frameworks, and components. A06 addresses the risk introduced by components with known vulnerabilities that developers fail to track and update.

The 2017 Equifax breach is the textbook example. Apache Struts — an open-source Java framework — had a critical remote code execution vulnerability, CVE-2017-5638. A patch was available two months before the Equifax breach began, but the organization had not updated its components. Attackers exploited the known vulnerability to exfiltrate 147 million records.

Defenses include maintaining a software bill of materials, or SBOM, subscribing to vulnerability notifications for all dependencies, and automating dependency updates in the CI/CD pipeline.

---

## Section 9 — A07: Identification and Authentication Failures

**[SHOW SLIDE: A07 heading — authentication attack vectors]**

A07 covers failures in identity verification and session management. Examples include permitting credential stuffing attacks by not implementing rate limiting, allowing weak passwords, storing passwords in plain text, and exposing session tokens in URLs where they may be logged.

Session fixation is a subtle attack in this category. An attacker tricks a user into using a session token the attacker already knows, then after the user authenticates, the attacker uses that same token to hijack the authenticated session.

Countermeasures include multi-factor authentication, strong password policies, secure session token generation with sufficient entropy, token rotation after login, and account lockout policies.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

We have covered the first seven categories of the OWASP Top 10 — broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, and authentication failures. Every one of these has appeared on Security+ exams and in real breach post-mortems.

In Part 2 we will finish the Top 10 and then shift to the secure software development lifecycle — how development teams build security in rather than bolt it on after the fact. We will also look at SAST, DAST, and code signing.

See you in Part 2.

---

*End of Part 1*
