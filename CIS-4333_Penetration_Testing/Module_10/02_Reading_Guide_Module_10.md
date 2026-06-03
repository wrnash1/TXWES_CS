# Reading Guide: Module 10 — Web Application Exploit Methods

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This reading guide supports Module 10 and directs your study toward the concepts tested on the CompTIA PenTest+ exam under Domain 3: Attacks and Exploits. Web application vulnerabilities consistently rank among the most common findings in real-world penetration tests. This guide organizes the key reading areas, vocabulary, and study questions to prepare you for the quiz and lab.

---

## Primary Reading Topics

### 1. OWASP Top 10

The OWASP Top 10 is the foundational reference for web application security. For this module, focus on the following categories:

- A01: Broken Access Control
- A02: Cryptographic Failures
- A03: Injection
- A05: Security Misconfiguration
- A07: Identification and Authentication Failures
- A08: Software and Data Integrity Failures

Read each entry for the description, example attack scenarios, and prevention guidance. The OWASP Top 10 is freely available at owasp.org.

### 2. SQL Injection

Read the OWASP SQL Injection Prevention Cheat Sheet. Focus on:

- How parameterized queries (prepared statements) eliminate the vulnerability at the root cause level
- The difference between union-based, error-based, and blind (boolean and time-based) techniques
- How SQLMap automates detection and exploitation across all injection types
- The risk of second-order SQL injection, where input is stored safely then executed unsafely later

### 3. Cross-Site Scripting

Read the OWASP XSS Prevention Cheat Sheet and the DOM-Based XSS Prevention Cheat Sheet. Key concepts:

- The difference between server-side rendering vulnerabilities (reflected and stored) versus client-side vulnerabilities (DOM-based)
- Why `HttpOnly` cookies prevent XSS-based session theft
- Content Security Policy as a defense-in-depth control that limits script execution sources
- How `innerHTML` and `document.write()` are dangerous JavaScript sinks in DOM-based XSS

### 4. Injection Vulnerabilities Beyond SQL

Review command injection, LDAP injection, and XML injection. The PenTest+ exam tests your ability to recognize vulnerable code patterns and recommend fixes. Focus on:

- Shell metacharacters that enable command injection: semicolon, pipe, ampersand, backtick, `$()`
- How directory traversal sequences bypass path restrictions and how URL encoding evades simple filters
- The difference between LFI and RFI, and the conditions that make each exploitable
- PHP configuration settings such as `allow_url_include` that affect file inclusion risk

### 5. Authentication and Session Management

Read the OWASP Authentication Cheat Sheet and Session Management Cheat Sheet. Key areas:

- Multi-factor authentication as a credential stuffing countermeasure
- Session token entropy requirements and what makes a token unpredictable
- Secure and HttpOnly cookie flags and when each applies
- The difference between session fixation and session hijacking as distinct attacks
- How account lockout policies interact with brute force timing and engagement risk

### 6. Burp Suite Professional Workflows

Review the PortSwigger Web Security Academy documentation for Burp Suite. Focus on:

- Configuring browser proxy settings for Burp intercept
- Using Repeater for manual injection testing and iterative payload refinement
- Configuring Intruder attack types: Sniper for single-position fuzzing versus Cluster bomb for credential testing
- Reading scanner output and triaging findings by severity
- Using the Decoder tab for encoding and decoding payloads in various schemes

### 7. API Security

Read the OWASP API Security Top 10. Focus on:

- API1: Broken Object Level Authorization (BOLA)
- API3: Excessive Data Exposure
- API6: Mass Assignment
- API7: Security Misconfiguration
- How to use ffuf or Gobuster for API endpoint discovery using wordlists
- Reading OpenAPI and Swagger documentation to enumerate available endpoints and parameters

---

## Key Vocabulary

Review and be able to define each of the following terms:

- SQL injection
- Union-based injection
- Boolean-based blind injection
- Time-based blind injection
- Second-order injection
- Reflected XSS
- Stored XSS
- DOM-based XSS
- Cross-site request forgery (CSRF)
- Command injection
- Directory traversal
- Local file inclusion (LFI)
- Remote file inclusion (RFI)
- Log poisoning
- Brute force attack
- Credential stuffing
- Session hijacking
- Session fixation
- Broken Object Level Authorization (BOLA/IDOR)
- Mass assignment
- Excessive data exposure
- Content Security Policy (CSP)
- Prepared statement
- Parameterized query
- Burp Suite Intruder
- Burp Suite Repeater
- OWASP Top 10
- CVSS score

---

## Study Questions

Answer these questions in your own words after completing the reading. These questions are not submitted — they are self-check questions to prepare for the quiz.

1. What is the fundamental cause of SQL injection, and why do parameterized queries eliminate it?

2. Explain the difference between reflected XSS and stored XSS. Which is more dangerous and why?

3. A web application includes a file based on the `page` URL parameter. The developer strips `../` sequences from input. What alternative traversal sequences might an attacker try?

4. What is the difference between brute force and credential stuffing? Which is more likely to succeed against a large target with many user accounts, and why?

5. Describe two Burp Suite modules and explain a specific scenario where you would use each one.

6. What is BOLA? Give a concrete example showing how an attacker exploits it against a REST API.

7. Why does mass assignment represent a privilege escalation risk? What field should an attacker try to modify in a user update request?

8. What is the purpose of the `HttpOnly` cookie flag? Which type of XSS attack does it prevent?

9. Explain time-based blind SQL injection. How does the attacker extract a single character of data using only timing responses?

10. What OWASP Top 10 category covers SQL injection, command injection, and LDAP injection under a single umbrella heading?

---

## Recommended Resources

The following freely available resources supplement the module lecture.

- OWASP Top 10: owasp.org/www-project-top-ten
- OWASP Testing Guide v4.2: owasp.org/www-project-web-security-testing-guide
- PortSwigger Web Security Academy: portswigger.net/web-security — free browser-based labs for SQLi, XSS, CSRF, SSRF, and more
- HackTricks Web Application Testing: book.hacktricks.xyz
- SecLists wordlists: github.com/danielmiessler/SecLists
- SQLMap documentation: sqlmap.org

PortSwigger Web Security Academy is particularly valuable. It provides free browser-based labs for every topic in this module. Complete at least the apprentice-level SQL injection and XSS labs before your quiz.

---

## CompTIA PenTest+ Exam Objectives Covered

The following PT0-002 exam objectives are addressed in this module:

- 3.3: Given a scenario, research attack vectors and perform application-based attacks

This objective explicitly lists SQL injection, XSS, command injection, directory traversal, file inclusion, authentication attacks, and API vulnerabilities. Web application testing is the largest single component of the Attacks and Exploits domain and appears in multiple scenario-format questions on the exam.

---

*End of Module 10 Reading Guide*
