# Reading Guide: Module 09 - Web Application Penetration Testing – OWASP Top 10
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Introduction
Welcome to **Module 09 - Web Application Penetration Testing – OWASP Top 10**! Web applications are among the most commonly targeted attack surfaces in modern engagements — nearly every organization exposes web-based services to the internet, and web application vulnerabilities consistently appear in breach reports. This module covers the attack categories documented in the **OWASP Top 10**, the industry-standard list of the most critical web application security risks, along with the tools and techniques pentesters use to identify and exploit them. This content maps to the **Attacks and Exploits** domain of PT0-002 (**30% of exam weight**).

Understanding web application vulnerabilities allows pentesters to demonstrate real-world impact: a single SQL injection or broken authentication flaw can expose an entire database or allow account takeover without any network-level exploitation.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SQL Injection (SQLi)**: A web application vulnerability in which unsanitized user input is incorporated directly into a database query, allowing an attacker to manipulate the query's logic. Attackers can use SQLi to bypass authentication (e.g., `' OR '1'='1`), extract database contents, modify or delete data, and in some configurations execute OS commands. Tools like `sqlmap` automate detection and exploitation. PT0-002 tests both manual SQLi recognition and tool-based exploitation.

*   **Cross-Site Scripting (XSS)**: A vulnerability in which an attacker injects malicious JavaScript into a web page that is then executed in the browser of other users. **Reflected XSS** executes immediately from a crafted URL. **Stored XSS** persists in the server's database and executes every time a victim loads the page. **DOM-based XSS** occurs entirely in the client-side JavaScript. XSS is used for session cookie theft, credential harvesting, and redirecting users to malicious sites.

*   **Broken Authentication and Session Management**: A class of vulnerabilities where web application authentication mechanisms are implemented insecurely. Examples include: weak password policies, missing account lockout, predictable session tokens, session tokens transmitted over HTTP (not HTTPS), and failure to invalidate sessions after logout. Attackers exploit these flaws to take over accounts without needing the user's actual password.

*   **Directory Traversal (Path Traversal)**: A web vulnerability that allows an attacker to read files outside the web root directory by manipulating file path parameters with sequences like `../../../etc/passwd`. If input is not sanitized, the web server may serve sensitive system files — including configuration files, credentials, or private keys — to an unauthenticated attacker.

*   **Burp Suite**: The industry-standard web application penetration testing proxy tool. Burp Suite intercepts HTTP/HTTPS traffic between the browser and the web server, allowing the tester to inspect, modify, and replay requests. Core features include the Proxy (intercept), Repeater (manually replay requests), Intruder (fuzzing and brute force), and Scanner (automated vulnerability discovery). PT0-002 expects testers to know Burp Suite's role and primary capabilities.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Attacks and Exploits is **30% of PT0-002**. Web application attacks are a significant subset — know SQLi, XSS, broken authentication, CSRF, IDOR, and directory traversal.
*   **OWASP Top 10 Categories Tested:** PT0-002 expects familiarity with the OWASP Top 10 categories by name: Broken Access Control (now #1), Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable Components, Authentication Failures, Software Integrity Failures, Logging Failures, and SSRF.
*   **SQLi Types — Know the Difference:** Blind SQLi (Boolean-based, time-based) does not return database error messages — the attacker infers results from behavioral differences. Error-based SQLi returns visible database errors. In-band SQLi returns results directly in the HTTP response. PT0-002 may present a scenario and ask which type applies.
*   **XSS vs. CSRF:** XSS injects malicious scripts that execute in a victim's browser. CSRF (Cross-Site Request Forgery) tricks an authenticated user's browser into making unintended requests to a site where they are logged in — exploiting the trust the site has in the user's session. These are commonly confused on the exam.
*   **Burp Suite vs. OWASP ZAP:** Both are web proxy tools. Burp Suite is the professional standard with advanced manual testing features. OWASP ZAP (Zed Attack Proxy) is a free, open-source alternative used for automated scanning. PT0-002 expects you to know both exist and their general purpose.
*   **`sqlmap` for Automated SQLi:** The command `sqlmap -u "http://target/page?id=1" --dbs` enumerates databases on a vulnerable target. PT0-002 may test whether a tester knows to use `sqlmap` for SQLi automation versus Burp Suite for manual web traffic manipulation.
*   **Study Resource:** [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting) — The "OWASP Top 10," "Burp Suite," and "Web Application Hacking" rooms provide hands-on, browser-based practice with every major web vulnerability category, including guided SQLi, XSS, and broken authentication labs against realistic vulnerable web applications.
*   **Video Lecture:** [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U) — Navigate to the Web Application Attacks section for content mapped to PT0-002 domain 3 web exploitation objectives.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Complete the OWASP Top 10 and Burp Suite rooms in the [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting). TryHackMe is a browser-based cybersecurity training platform — all labs run entirely in your browser without requiring a local VM or Kali Linux installation. The OWASP rooms walk through each Top 10 category with hands-on exploitation against intentionally vulnerable web applications.
*   **Required Video:** Watch the Web Application Attacks segment of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U). This is a free, full-length PT0-002 prep course on YouTube. Use chapter markers to navigate to the web application content covering SQLi, XSS, broken authentication, and associated tools.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Intercept and manipulate web requests with Burp Suite**: You will configure your browser to route traffic through Burp Suite's proxy, intercept a login request, and modify parameters to understand how web application input reaches the server — building the foundation for manual vulnerability testing.
*   **Test for SQL Injection: `sqlmap -u "http://target/?id=1" --dbs`**: You will run `sqlmap` against a vulnerable lab application to enumerate its databases, demonstrating how a single injectable parameter can expose the entire data tier. You will document the databases discovered and the business impact of this exposure.
*   **Identify and exploit Cross-Site Scripting (XSS)**: You will locate a reflected XSS vulnerability in a lab application, craft a payload that executes JavaScript in the browser, and document what an attacker could accomplish (session hijacking, credential theft, redirect) — demonstrating why output encoding is a critical control.

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Complete the OWASP Top 10 and Burp Suite rooms in [TryHackMe Pentest Learning Path](https://tryhackme.com/path/outline/pentesting).
- [ ] Watch the Web Application Attacks section of the [CompTIA PenTest+ Complete Course by freeCodeCamp](https://www.youtube.com/watch?v=3Kq1MIfC-4U).
- [ ] Review the lab instructions and understand the purpose of each step before starting.
- [ ] Proceed to the weekly hands-on lab activity.
