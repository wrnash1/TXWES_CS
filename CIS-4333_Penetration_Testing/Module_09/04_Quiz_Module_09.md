# Quiz: Module 09 - Web Application Penetration Testing – OWASP Top 10
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

**Question 1**
Which web application vulnerability allows an attacker to manipulate database queries by injecting malicious input directly into an unsanitized parameter, potentially exposing or modifying the entire database?
*   A) Cross-Site Scripting (XSS)
*   B) SQL Injection (SQLi)
*   C) Cross-Site Request Forgery (CSRF)
*   D) Directory Traversal
*   **Correct Answer:** B) SQL Injection (SQLi)
*   **Distractor Analysis:**
    *   *Why B is correct:* SQL Injection occurs when user-supplied input is embedded directly into a database query without proper sanitization or parameterization. An attacker can inject SQL syntax to alter query logic — for example, `' OR '1'='1` to bypass authentication — or extract, modify, and delete database contents. It is consistently ranked among the most critical web vulnerabilities in the OWASP Top 10.
    *   *Why A is incorrect:* Cross-Site Scripting (XSS) injects malicious JavaScript into a web page that executes in another user's browser. It targets the client side and does not directly interact with the database layer.
    *   *Why C is incorrect:* CSRF tricks an authenticated user's browser into submitting unintended requests to a web application. It exploits the server's trust in the user's session cookie but does not inject SQL or manipulate database queries directly.
    *   *Why D is incorrect:* Directory Traversal allows attackers to read files outside the web root by manipulating path parameters (e.g., `../../etc/passwd`). It targets the filesystem, not the database query layer.

---

**Question 2**
In the context of web application penetration testing, which of the following best defines **Cross-Site Scripting (XSS)**?
*   A) A vulnerability where an attacker manipulates file path parameters to access files outside the web server's intended directory, such as reading `/etc/passwd`.
*   B) A vulnerability where malicious JavaScript is injected into a web page and executed in the browsers of other users visiting that page, enabling session theft, credential harvesting, or malicious redirects.
*   C) An attack that intercepts and relays NTLM authentication requests between a client and server to gain unauthorized access to network resources.
*   D) A technique that tricks an authenticated user's browser into submitting unauthorized requests to a site where the user is currently logged in, exploiting the server's trust in the session.
*   **Correct Answer:** B) A vulnerability where malicious JavaScript is injected into a web page and executed in the browsers of other users visiting that page, enabling session theft, credential harvesting, or malicious redirects.
*   **Distractor Analysis:**
    *   *Why B is correct:* XSS injects attacker-controlled JavaScript into content served by a trusted web application. When victims load the affected page, their browser executes the script in the context of the legitimate site — giving the attacker access to session cookies, form data, and the ability to redirect the user. Stored XSS persists in the database; reflected XSS is delivered via a crafted URL.
    *   *Why A is incorrect:* This describes Directory Traversal (Path Traversal), which manipulates file path parameters to escape the web root and read arbitrary files from the server's filesystem. It does not involve JavaScript injection.
    *   *Why C is incorrect:* This describes an NTLM Relay attack — a network-level lateral movement technique. It has no relationship to web application JavaScript injection.
    *   *Why D is incorrect:* This describes Cross-Site Request Forgery (CSRF), which forces a logged-in user's browser to send unintended requests. CSRF exploits the user's authenticated session; XSS executes attacker-controlled code in the victim's browser.

---

**Question 3**
A penetration tester suspects a web application's login form is vulnerable to SQL Injection. Which tool automates the detection and exploitation of SQL injection vulnerabilities in a target URL?
*   A) `nmap -sV`
*   B) `sqlmap -u "http://target/login?id=1" --dbs`
*   C) `hydra -l admin -P passwords.txt http-post-form`
*   D) `nikto -h http://target`
*   **Correct Answer:** B) `sqlmap -u "http://target/login?id=1" --dbs`
*   **Distractor Analysis:**
    *   *Why B is correct:* `sqlmap` is an open-source tool that automatically detects and exploits SQL injection vulnerabilities in web application parameters. The `-u` flag specifies the target URL with the injectable parameter, and `--dbs` instructs sqlmap to enumerate all databases accessible through the injection. It supports multiple injection types including error-based, blind boolean-based, and time-based.
    *   *Why A is incorrect:* `nmap -sV` performs service version detection against network ports. It is a network reconnaissance tool and has no capability to test web application input parameters for SQL injection.
    *   *Why C is incorrect:* `hydra` with `http-post-form` is a credential brute-force tool that submits large lists of username/password combinations to a login form. It tests authentication strength, not SQL injection vulnerabilities.
    *   *Why D is incorrect:* `nikto` is a web server scanner that checks for misconfigurations, outdated software, and common web vulnerabilities. While it performs broad web scanning, it is not the purpose-built SQL injection exploitation tool that `sqlmap` is.

---

**Question 4**
A web application tester is using Burp Suite during an engagement. Which of the following best describes the primary function of Burp Suite's **Repeater** module?
*   A) Automatically scan the web application for OWASP Top 10 vulnerabilities and generate a findings report.
*   B) Intercept all HTTP/HTTPS traffic between the browser and the server to view requests and responses in real time.
*   C) Manually resend and modify individual HTTP requests to the server and inspect the responses, allowing iterative manual testing of parameters.
*   D) Perform automated brute-force or fuzzing attacks by submitting large lists of payloads against a specified request parameter.
*   **Correct Answer:** C) Manually resend and modify individual HTTP requests to the server and inspect the responses, allowing iterative manual testing of parameters.
*   **Distractor Analysis:**
    *   *Why C is correct:* Burp Suite's Repeater module allows a tester to capture a request (typically via the Proxy), send it to Repeater, then manually modify any part of the request — headers, parameters, body — and resend it to the server as many times as needed. This is the primary tool for manually testing for SQLi, XSS, authentication bypass, IDOR, and other parameter-level vulnerabilities.
    *   *Why A is incorrect:* Automated vulnerability scanning is performed by Burp Suite's **Scanner** module (available in the Pro edition). The Repeater is specifically for manual, iterative request testing.
    *   *Why B is incorrect:* Intercepting traffic in real time is the function of Burp Suite's **Proxy** module, which sits between the browser and server and pauses requests for inspection. The Repeater works on saved/forwarded requests, not live intercept.
    *   *Why D is incorrect:* Automated payload fuzzing and brute-force attacks are performed by Burp Suite's **Intruder** module, which accepts a request, marks injection points, and iterates through a payload list. The Repeater is for one-at-a-time manual testing, not automated iteration.

---

**Question 5**
A penetration tester discovers that a web application constructs file paths from user input without sanitization. When the tester submits the value `../../../../etc/passwd` as a filename parameter, the server returns the contents of the Linux password file. What vulnerability has been exploited?
*   A) SQL Injection — the attacker has injected a path sequence into a database query.
*   B) Cross-Site Scripting (XSS) — the attacker has injected a script that traverses the DOM tree.
*   C) Directory Traversal (Path Traversal) — the attacker has escaped the web root to read arbitrary files from the server's filesystem.
*   D) Broken Authentication — the attacker has bypassed the login form using a crafted session token.
*   **Correct Answer:** C) Directory Traversal (Path Traversal) — the attacker has escaped the web root to read arbitrary files from the server's filesystem.
*   **Distractor Analysis:**
    *   *Why C is correct:* Directory Traversal exploits insufficient input validation on file path parameters. By injecting `../` sequences, an attacker can navigate up the directory tree and read files outside the intended web root — such as `/etc/passwd`, SSH private keys, or web application configuration files containing database credentials. This is a classic OWASP vulnerability that demonstrates the critical importance of sanitizing all user-controlled path input.
    *   *Why A is incorrect:* SQL Injection manipulates database query syntax using SQL metacharacters. Directory traversal uses filesystem path sequences (`../`) and does not interact with a database query layer.
    *   *Why B is incorrect:* XSS involves injecting JavaScript that executes in another user's browser. `../` sequences are filesystem navigation — they have nothing to do with DOM manipulation or browser-side script execution.
    *   *Why D is incorrect:* Broken Authentication involves flaws in login mechanisms, session management, or credential handling. In this scenario the attacker is not bypassing a login — they are reading files through an unsanitized path parameter in an already-accessible endpoint.
