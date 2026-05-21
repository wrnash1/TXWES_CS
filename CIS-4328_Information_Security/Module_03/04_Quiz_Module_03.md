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
