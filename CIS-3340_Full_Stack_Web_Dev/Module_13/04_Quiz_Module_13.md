# Quiz: Module 13 - Web Security (JWT & CORS)
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
What are the three parts of a JSON Web Token (JWT)?
*   A) Header, Payload, Signature
*   B) ID, Key, Secret
*   C) Username, Timestamp, Salt
*   D) Origin, Destination, Protocol
*   **Correct Answer:** A) A JWT is a dot-separated string with three Base64URL-encoded sections: a **Header** (algorithm + token type), a **Payload** (claims including user data and expiration), and a **Signature** (cryptographic hash verifying the token has not been tampered with).
*   **Distractor Analysis:**
    *   *Why A is correct:* Header.Payload.Signature is the standard JWT structure defined in RFC 7519.
    *   *Why B is incorrect:* ID, Key, and Secret are generic authentication concepts — not the structural components of a JWT.
    *   *Why C is incorrect:* Username, Timestamp, and Salt are password-related concepts — not the three sections of a JWT.
    *   *Why D is incorrect:* Origin, Destination, and Protocol describe network routing concepts — unrelated to JWT structure.

---

**Question 2**
Which of the following is the most accurate definition of **Cross-Origin Resource Sharing (CORS)**?
*   A) A browser security mechanism that allows or restricts browser-side JavaScript from reading HTTP responses from a different origin than the page that initiated the request — enforced via response headers like `Access-Control-Allow-Origin`.
*   B) A cryptographic protocol that encrypts all data transferred between a browser and a web server using TLS certificates issued by a trusted Certificate Authority.
*   C) An AWS IAM policy mechanism that restricts which AWS accounts can invoke an API Gateway endpoint from external accounts.
*   D) A JavaScript content security policy that prevents inline scripts and eval() from executing in the browser to mitigate XSS attacks.
*   **Correct Answer:** A) A browser security mechanism that allows or restricts browser-side JavaScript from reading HTTP responses from a different origin — enforced via response headers like `Access-Control-Allow-Origin`.
*   **Distractor Analysis:**
    *   *Why A is correct:* CORS is enforced by the browser at the HTTP response level — the server sends permission headers and the browser decides whether to expose the response to JavaScript.
    *   *Why B is incorrect:* This describes HTTPS/TLS — the transport encryption layer. CORS is about origin-based access control, not encryption.
    *   *Why C is incorrect:* This describes AWS resource-based policies for cross-account API access — a separate AWS security mechanism.
    *   *Why D is incorrect:* This describes Content Security Policy (CSP) — a separate browser security header that restricts script sources and execution contexts.

---

**Question 3**
A developer stores a JWT in the browser. Where is it most appropriately stored for security?
*   A) In a JavaScript variable in the global `window` object — accessible everywhere across the application.
*   B) In `localStorage` — persists across tabs and sessions, simple to access.
*   C) In an HTTP-only, Secure, SameSite=Strict cookie — inaccessible to JavaScript, preventing XSS theft, and protected against CSRF with the SameSite attribute.
*   D) In the URL query string — so it can be easily passed between pages without additional JavaScript.
*   **Correct Answer:** C) In an HTTP-only, Secure, SameSite=Strict cookie — inaccessible to JavaScript, preventing XSS theft, and protected against CSRF with the SameSite attribute.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Storing a JWT in `window` exposes it to any JavaScript on the page — a XSS attack can immediately steal it.
    *   *Why B is incorrect:* `localStorage` is accessible by JavaScript — any XSS payload on the page can read and exfiltrate the token. The OWASP recommendation is to avoid storing JWTs in `localStorage`.
    *   *Why C is correct:* HTTP-only cookies cannot be read by JavaScript — eliminating XSS theft. `Secure` ensures transmission only over HTTPS. `SameSite=Strict` prevents the cookie from being sent on cross-site requests, mitigating CSRF.
    *   *Why D is incorrect:* Tokens in URL query strings are logged in server access logs, browser history, and referrer headers — a significant credential exposure risk.

---

**Question 4**
An Express API receives a `POST /login` request with a username and password. The user is found in the database. What is the correct sequence for verifying the password and issuing a JWT?
*   A) Compare the plain-text submitted password directly to the stored password hash using `===`.
*   B) Use `bcrypt.compare(submittedPassword, storedHash)` to verify the password, then call `jwt.sign({ userId }, JWT_SECRET, { expiresIn: '1h' })` to generate and return the token if the comparison returns `true`.
*   C) Decrypt the stored password hash using `bcrypt.decrypt()` and compare the result to the submitted password.
*   D) Hash the submitted password with `bcrypt.hash()` and store the new hash — then issue the JWT unconditionally since the user was found.
*   **Correct Answer:** B) Use `bcrypt.compare(submittedPassword, storedHash)` to verify the password, then issue the JWT only if the comparison returns `true`.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The stored value is a bcrypt hash, not the plaintext password — direct string comparison will always fail and should never be used for password verification.
    *   *Why B is correct:* `bcrypt.compare()` rehashes the submitted password with the salt embedded in the stored hash and compares the result — this is the correct, secure verification pattern.
    *   *Why C is incorrect:* bcrypt is a one-way hash function — there is no `bcrypt.decrypt()`. One-way hashes cannot be reversed by design.
    *   *Why D is incorrect:* Re-hashing on every login does not verify the password — it would replace the stored hash and issue a JWT regardless of whether the password was correct.

---

**Question 5**
A JWT issued by an API has an `exp` claim set to a Unix timestamp 1 hour in the future. The server's `jwt.verify()` call starts rejecting the token 70 minutes after issuance. What is the most accurate explanation?
*   A) The `exp` claim was overridden by the `iat` (issued-at) claim, shortening the effective token lifetime.
*   B) The JWT has expired — the `exp` claim specifies the absolute Unix timestamp after which the token is invalid, and 70 minutes after issuance exceeds the 1-hour `expiresIn` window.
*   C) JWT tokens automatically expire after 60 minutes regardless of the `exp` value — the `expiresIn` option is advisory only.
*   D) The server's system clock drifted 10 minutes ahead — causing it to consider the token expired 10 minutes before the client expects.
*   **Correct Answer:** B) The JWT has expired — the `exp` claim specifies the absolute Unix timestamp after which the token is invalid, and 70 minutes after issuance exceeds the 1-hour `expiresIn` window.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `iat` claim records when the token was issued but does not override `exp` — both can exist in the same token.
    *   *Why B is correct:* `exp` is an absolute Unix timestamp. After that timestamp passes, `jwt.verify()` throws a `TokenExpiredError`. 70 minutes after issuance exceeds the 1-hour (3600-second) window.
    *   *Why C is incorrect:* The `exp` claim is enforced by the verifier — it is not advisory. `expiresIn` controls what timestamp is written into `exp` during signing.
    *   *Why D is incorrect:* Clock skew between client and server is a real operational concern, but 10 minutes of skew is unusually large. While the answer is plausible, option B is the primary explanation that directly accounts for the 70-minute timeline.
