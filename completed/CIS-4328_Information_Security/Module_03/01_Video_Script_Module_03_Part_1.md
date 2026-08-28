# Video Script — Module 03, Part 1: Application Attacks and Software Vulnerabilities (Theory)

## CIS-4328 Information Security | Texas Wesleyan University

### Instructor: Professor Nash | CompTIA Security+ SY0-701 Alignment

### Estimated Duration: 13 minutes

---

## Opening

**[INSTRUCTOR ON CAMERA]**

Welcome to Module 03 — Application Attacks and Software Vulnerabilities. I'm Professor Nash.

If Module 01 taught you the vocabulary of threats and Module 02 taught you about attacking humans, this module teaches you how attackers target the software itself. Web applications are among the most targeted assets in modern enterprise environments — they are internet-facing, they process sensitive data, and they were often written before security was a priority.

The SY0-701 exam covers application attacks primarily in Domain 2. You will see injection attacks, memory exploitation, and application-level weaknesses on the exam in scenario form. Let's break them down.

---

## Section 1 — Injection Attacks

**[SHOW DIAGRAM: Web application flow diagram. User browser on left sends HTTP request with input field containing a SQL injection payload. Arrow points to Web Application Server. Arrow continues to Database Server. The database executes the injected SQL and returns unauthorized data back to the browser. Label: SQL Injection Attack Flow.]**

**[Alt-text: Horizontal flow diagram. Left: User Browser sends HTTP POST request with login form containing SQL payload in the password field. Center: Web Application Server receives the request and passes it to the database. Right: Database Server executes the malicious SQL and returns all records. Return arrow shows unauthorized data flowing back to the browser. Top label: SQL Injection Attack Flow.]**

**Injection attacks** occur when an application passes untrusted user input directly to an interpreter — a database engine, an operating system shell, or an LDAP directory — without proper validation or sanitization.

**SQL Injection (SQLi)** is the most common and best-known injection attack. A web application that builds database queries by concatenating user input creates a path for manipulation. If a login form constructs a query using the user's input directly and an attacker enters a crafted string as the password, the resulting query can evaluate to true for every row in the database — bypassing authentication entirely or dumping all records.

The fundamental cause is insufficient input validation. The developer trusted user input and passed it directly to the database engine. The fix is parameterized queries — also called prepared statements — where the query structure is defined first and user input is always treated as data, never as executable code.

**Command Injection** is the same principle applied to operating system commands. An application that passes user input to a system shell without sanitization allows an attacker to append additional OS commands. If the application runs with elevated privileges, the injected commands inherit those privileges.

**LDAP Injection** targets applications that construct LDAP queries from user input, allowing an attacker to manipulate directory service queries.

**XML Injection and XPath Injection** target XML-based data stores and query engines using the same principle.

**Defense for all injection attacks:**

- Input validation — reject input that does not match expected format, type, and length.
- Parameterized queries / prepared statements for all database interactions.
- Stored procedures with appropriate permission boundaries.
- Principle of least privilege for database accounts — the application should not connect to the database as a DBA.
- Web application firewall (WAF) to detect and block known injection patterns.

---

## Section 2 — Cross-Site Scripting (XSS)

**[SHOW DIAGRAM: Three-party XSS attack flow. Left: Attacker injects malicious script into a web application's comment or input field. Center: Vulnerable web server stores or reflects the script. Right: Victim user's browser loads the page and the script executes in the victim's browser context. Arrow from attacker's script execution in victim browser leads to stolen session cookie being sent to attacker's server.]**

**[Alt-text: Three-party diagram. Left box: Attacker — injects malicious JavaScript into web application input field. Center box: Vulnerable Web Server — stores injected script in database (stored XSS) or reflects it in response (reflected XSS). Right box: Victim Browser — loads page containing attacker script, which executes with victim's browser permissions. Arrow from victim browser to Attacker Server: stolen session cookie transmitted.]**

**Cross-Site Scripting (XSS)** occurs when an attacker injects malicious client-side script — typically JavaScript — into a web page that is then rendered by other users' browsers. Unlike SQL injection which targets the server, XSS targets the user's browser.

**Stored (Persistent) XSS** — the malicious script is permanently stored on the server — in a database, message board, or comment field — and is served to every user who visits the affected page. This is the highest-impact form because it affects all visitors without any further action from the attacker.

**Reflected (Non-Persistent) XSS** — the malicious script is embedded in a URL or form parameter and is reflected back in the server's response without being stored. The attack requires the victim to click a crafted link. Phishing emails frequently deliver reflected XSS payloads.

**DOM-Based XSS** — the attack manipulates the Document Object Model in the victim's browser directly, without the script ever being sent to the server.

Common XSS payloads steal session cookies, redirect users to phishing pages, capture keystrokes, or display fake login forms to harvest credentials.

**Defense:**

- Output encoding — encode all user-supplied content before rendering it in HTML.
- Content Security Policy (CSP) headers — tell browsers which scripts are authorized to execute.
- Input validation — reject or sanitize input that contains script tags or event handlers.
- HttpOnly cookie flag — prevents JavaScript from reading session cookies, limiting XSS impact.

---

## Section 3 — Cross-Site Request Forgery (CSRF)

**[SHOW DIAGRAM: CSRF attack flow. Step 1: Victim logs into bank website and holds active session cookie. Step 2: Victim visits attacker-controlled page while still logged in. Step 3: Attacker's page sends a hidden HTTP request to the bank using the victim's active session cookie. Step 4: Bank processes the request as if the victim initiated it.]**

**[Alt-text: Four-step sequence diagram. Step 1: Victim authenticates to bank website, browser stores session cookie. Step 2: Victim navigates to attacker's malicious web page in the same browser. Step 3: Hidden form or image tag on attacker's page sends POST request to bank URL, browser automatically attaches victim's session cookie. Step 4: Bank receives authenticated request, processes the transaction. Victim did not intend this action.]**

**Cross-Site Request Forgery (CSRF)** — pronounced "sea surf" — tricks an authenticated user's browser into sending an unintended request to a web application where the user is currently logged in. The browser automatically includes session cookies with requests to the target domain, so the forged request appears authentic.

A classic CSRF attack against an online banking site would embed a hidden form on an attacker's page that submits a funds transfer to the bank when the victim loads the page. If the victim has an active authenticated session, the bank processes the transfer.

CSRF differs from XSS in a key way: XSS injects malicious script that runs in the victim's browser context on the legitimate site; CSRF forces the victim's browser to make a legitimate-looking request to the target site from a different origin.

**Defense:**

- CSRF tokens — a unique, secret, unpredictable token embedded in each form that the server validates. An attacker cannot forge a request with a valid CSRF token because they cannot read the token from a different origin.
- SameSite cookie attribute — instructs browsers not to send cookies with cross-origin requests.
- Requiring re-authentication for sensitive actions (password change, wire transfer).

---

## Section 4 — Memory Exploitation

**[SHOW DIAGRAM: Memory layout diagram for a running process. Stack grows downward from high addresses. Heap grows upward from low addresses. Segments labeled: Text (code), Data, Heap, Stack. Arrow from buffer region in Stack points past the buffer boundary into the Return Address area. Label: Buffer Overflow — overwriting the return address to redirect execution.]**

**[Alt-text: Vertical memory layout diagram. Top (high addresses): Stack — contains function call frames including local variables, saved registers, and return address. Bottom (low addresses): Text segment — compiled code. Data segment — global variables. Heap — dynamically allocated memory growing upward. A red arrow shows data written past the end of a local buffer in the stack, overwriting the return address stored above it. Caption: Buffer Overflow — overwriting return address to redirect code execution.]**

**Buffer Overflow** occurs when a program writes more data into a fixed-size memory buffer than the buffer can hold. The excess data overwrites adjacent memory — including the return address that tells the CPU where to jump after a function completes. An attacker who can control what overwrites the return address can redirect execution to attacker-supplied code (shellcode) or to existing executable code in the program or OS libraries.

**Stack Overflow** — the classic buffer overflow — overwrites data on the call stack, typically the return address or function pointers.

**Heap Overflow** — writes past the end of a heap-allocated buffer, corrupting heap management structures or other heap objects.

**Integer Overflow** — arithmetic produces a value too large for the data type, which wraps around to an unexpected small value and causes logic errors in size or bounds checks.

**Use-After-Free** — a program continues to use a memory pointer after the memory it points to has been freed. If the attacker can cause the freed memory to be reallocated with attacker-controlled content, they control what the dangling pointer accesses.

**Defenses:**

- Address Space Layout Randomization (ASLR) — randomizes memory addresses, making it difficult to predict where shellcode or return-oriented gadgets are located.
- Data Execution Prevention (DEP) / No-Execute (NX) bit — marks memory regions as non-executable, preventing shellcode stored in data regions from running.
- Stack Canaries — a random value placed between local variables and the return address; if the canary is overwritten, the program aborts before the corrupted return address is used.
- Safe coding practices — use of bounds-checked functions and memory-safe languages.

---

## Section 5 — Directory Traversal and Other Application Attacks

**[SHOW DIAGRAM: Directory traversal attack. Web application accepts a file parameter in the URL. Attacker modifies the parameter to include path traversal sequences. Dashed arrow shows navigation from the web root directory upward through the file system to reach system configuration files outside the web root.]**

**[Alt-text: Diagram showing web server file system. Web root directory is shown at mid-level. A URL parameter points to a file within the web root. Below the parameter, the attacker's modified version adds dot-dot-slash sequences to navigate upward out of the web root and into the operating system directory, reaching sensitive files like password or configuration files. Caption: Directory Traversal Attack Path.]**

**Directory Traversal** — also called path traversal — occurs when an application uses user-supplied input to construct file paths without validation, allowing an attacker to navigate outside the intended directory. An attacker can potentially read configuration files, password hashes, or any readable file on the server.

**Defense:** Validate and sanitize all file path inputs. Use an allowlist of permitted files. Never construct file paths from user input without strict bounds enforcement.

**Server-Side Request Forgery (SSRF)** — an attacker tricks a server-side application into making HTTP requests to internal resources that the attacker cannot access directly. The server is used as a proxy to reach internal APIs, metadata services (such as cloud instance metadata endpoints), or internal network resources.

**Defense:** Validate and restrict outbound URLs the application is permitted to request. Block requests to internal IP ranges from server-side request functions.

**Race Condition / TOCTOU (Time-of-Check/Time-of-Use)** — a flaw where an attacker can change a resource between the time it is checked and the time it is used, causing the application to act on stale or attacker-modified data.

---

## Closing — Part 1

**[INSTRUCTOR ON CAMERA]**

In Part 1 we covered injection attacks including SQL injection, XSS, CSRF, memory exploitation including buffer overflow, and directory traversal and SSRF. In Part 2 we will cover secure coding principles, the OWASP Top 10 context, and exam scenario walkthroughs.

Study resources: **professormesser.com** for SY0-701 video lectures, and **comptia.org** for the official exam objectives.

---

Texas Wesleyan University — CIS-4328 Information Security — Module 03 Part 1

Proprietary and Confidential. Not for disclosure outside of authorized course use.
