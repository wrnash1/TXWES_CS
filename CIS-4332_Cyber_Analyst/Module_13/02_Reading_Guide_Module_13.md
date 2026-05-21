# Reading Guide: Module 13 - Web Application Security Analysis
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 13 - Web Application Security Analysis**! This module covers how analysts identify, analyze, and respond to web application vulnerabilities and attacks. You will learn the OWASP Top 10 vulnerability categories, how common web attacks like SQL injection, cross-site scripting (XSS), and server-side request forgery (SSRF) work, and how to use proxy tools and web application logs to detect active exploitation. These topics are tested under **Domain 1: Security Operations (33%)** and **Domain 2: Vulnerability Management (30%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn to recognize web attack patterns in logs, understand how WAFs and input validation controls mitigate web vulnerabilities, and interpret HTTP status codes as investigative indicators. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **SQL Injection (SQLi)**: A web application attack in which an attacker inserts malicious SQL code into an input field that is passed unsanitized to a backend database query, allowing the attacker to retrieve, modify, or delete data, bypass authentication, or execute OS commands on the database server. SQLi is prevented through parameterized queries (prepared statements) and input validation — never by escaping alone. CySA+ tests SQLi identification and the correct preventive control.
*   **Cross-Site Scripting (XSS)**: A vulnerability in which a web application includes untrusted user input in its HTML output without proper encoding, allowing attackers to inject client-side scripts into pages viewed by other users. Stored XSS persists in the database and executes for every user who views the affected page. Reflected XSS is delivered via a crafted URL and executes only when the victim clicks the link. XSS is prevented through output encoding and Content Security Policy (CSP) headers.
*   **Server-Side Request Forgery (SSRF)**: A vulnerability that allows an attacker to cause the web application server to make HTTP requests to unintended internal or external targets — such as internal cloud metadata endpoints (e.g., `169.254.169.254` in AWS) or internal network services that are not otherwise accessible. SSRF bypasses perimeter controls because the malicious request originates from a trusted server inside the network. It is prevented through URL allowlisting and disabling unnecessary server-side HTTP request functionality.

---

### 2. Certification Exam Tips
*   **Focus Area – OWASP Top 10 (Domain 2):** CySA+ CS0-003 tests whether you can identify which OWASP vulnerability category is being exploited from a described attack scenario. Know the key categories: Injection (SQLi, command injection), Broken Access Control, Security Misconfiguration, XSS (now under Injection in OWASP 2021), Insecure Deserialization, and SSRF. The exam presents scenarios and asks you to classify the vulnerability type.
*   **Scenario Trap – WAF vs. Input Validation:** A Web Application Firewall (WAF) is a detective/preventive network control that can block known attack signatures at the perimeter — but it is not a substitute for fixing the underlying code vulnerability. CySA+ questions that ask for the "correct long-term fix" for SQLi always expect parameterized queries, not WAF deployment. WAF is a compensating control, not a remediation.
*   **HTTP Status Codes as Attack Indicators:** Analysts use web proxy logs to detect attacks. Know that: 200 OK = successful request; 403 Forbidden = access control blocking (may indicate scanning); 404 Not Found = probing for non-existent paths (common in directory enumeration); 500 Internal Server Error = potential SQLi or command injection success triggering an unhandled exception.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers web application vulnerability identification, OWASP categories, and attack detection in proxy logs mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes walkthroughs of web attack pattern recognition.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Web Application Security** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details OWASP vulnerability categories, web attack techniques, and mitigation controls tested on the exam.
*   **Required Video:** Watch the video lecture on **Web Application Security Analysis** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of web attack identification in proxy logs and OWASP vulnerability classification exercises.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify a SQL injection vulnerability in a provided code snippet**: Review the provided PHP code snippet that constructs a database query by concatenating unsanitized user input; identify the vulnerable line, explain why it is exploitable, and rewrite it using a parameterized query (prepared statement) to remediate the vulnerability.
*   **Analyze web proxy logs for attack patterns**: Review a provided Apache access log excerpt containing a mix of normal and malicious requests; identify requests showing SQLi attempts (e.g., `' OR 1=1--` in query parameters), XSS payloads (e.g., `<script>` in form fields), and directory traversal attempts (e.g., `../../../etc/passwd`); document the source IP, timestamp, and attack type for each.
*   **Inspect OWASP security checklists and map findings to categories**: Using the OWASP Top 10 as a reference, take three of the vulnerabilities identified in the proxy log analysis and map each to its OWASP category, document the recommended preventive control, and identify the corresponding MITRE ATT&CK technique ID.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Web Application Security** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Web Application Security Analysis** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the proxy log analysis and OWASP classification steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
