# Lab: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

**Title:** Identifying and Exploiting Web Application Vulnerabilities (Controlled Environment)

**Duration:** Approximately 90 minutes

**Environment:** OWASP WebGoat (local Docker container — no external network access required)

**Skill Level:** Intermediate — assumes familiarity with web browsers and basic HTTP concepts

---

## Objectives

Upon completing this lab, you will be able to:

1. Set up OWASP WebGoat as a local vulnerable web application for safe security testing
2. Demonstrate a SQL injection attack against a deliberately vulnerable login form
3. Demonstrate a reflected XSS attack and observe script execution in the browser
4. Identify an IDOR (Insecure Direct Object Reference) vulnerability
5. Apply input validation and output encoding fixes conceptually to each vulnerability
6. Analyze a SAST scan result and interpret findings

---

## Prerequisites

- Docker Desktop installed ([https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/))
- Web browser (Chrome or Firefox recommended)
- Completed Module 10 video lectures and Reading Guide
- Text editor for lab notes

---

## Important Safety Notice

All attacks in this lab are performed exclusively against WebGoat, a deliberately vulnerable application running locally on your own machine. Do NOT perform any of these techniques against real websites, production systems, or any system you do not own and have explicit written permission to test. Unauthorized security testing is illegal under the Computer Fraud and Abuse Act (CFAA) and equivalent state and international laws.

---

## Part 1 — Environment Setup (10 minutes)

### Step 1.1 — Pull and Run WebGoat

Open a terminal (Command Prompt, PowerShell, or Terminal on macOS/Linux) and run:

```bash
docker pull webgoat/webgoat
docker run -p 8080:8080 -d webgoat/webgoat
```

### Step 1.2 — Verify WebGoat is Running

Open your browser and navigate to `http://localhost:8080/WebGoat`

You should see the WebGoat login/registration page. If Docker is not available, navigate to the WebGoat GitHub releases page ([https://github.com/WebGoat/WebGoat/releases](https://github.com/WebGoat/WebGoat/releases)) and download the standalone JAR, then run:

```bash
java -jar webgoat-[version].jar
```

### Step 1.3 — Register an Account

Click "Register new user" and create a local account with any username and password. You do not need a real email address. Log in.

### Step 1.4 — Explore the Interface

WebGoat organizes lessons by category. You will see categories in the left sidebar: Introduction, General, (A1) Broken Access Control, (A2) Cryptographic Failures, (A3) Injection, etc. Take two minutes to explore the sidebar before proceeding.

---

## Part 2 — SQL Injection (25 minutes)

Navigate to the **Injection** section in the left sidebar.

### Step 2.1 — SQL Injection Concept Overview

In WebGoat, open **SQL Injection (intro)** and complete the introductory lessons (lessons 2 and 3). These are instructional pages, not interactive exercises. Read each page carefully.

**Record in your lab notes:** What is the fundamental reason SQL injection is possible? (Answer in one sentence using the concept of untrusted data and query interpretation.)

### Step 2.2 — String SQL Injection

Open **SQL Injection (intro)** lesson 9 — "String SQL Injection."

1. Read the scenario: you are asked to retrieve employee data for all employees
2. The form has an employee name field and submits a SQL query
3. Try entering: `Smith' OR '1'='1`
4. Observe the result — you should retrieve all employee records

**Explain what happened:** The condition `'1'='1'` is always true. By injecting `OR '1'='1`, you made the WHERE clause always true, returning all rows.

**Record in your lab notes:** Write the full SQL query that was likely executed after your injection. Use `[input]` to represent where your injected string was placed, then substitute it.

### Step 2.3 — Numeric SQL Injection

Open lesson 10 — "Numeric SQL Injection."

1. Read the scenario: a form retrieves weather data based on a station number
2. The station field accepts a number
3. Inject: `101 OR 1=1`
4. Observe results

**Record in your lab notes:** Why did you not need quote marks in this injection but needed them in Step 2.2?

### Step 2.4 — Query String Parameter Injection

Open lesson 11 — "Compromising Confidentiality with String SQL Injection."

Follow the lesson instructions to retrieve employee data you should not have access to. The lesson provides guidance.

**Lab Reflection Question 1:** You have now demonstrated SQL injection multiple ways. Write a paragraph (four to six sentences) describing:

- What parameterized queries do differently than string concatenation
- Why input validation alone (checking for special characters) is not a sufficient defense
- In the shared responsibility model for a SaaS application, who is responsible for fixing SQL injection vulnerabilities in the application code?

---

## Part 3 — Cross-Site Scripting (XSS) (20 minutes)

Navigate to the **(A7) Cross-Site Scripting** section in the WebGoat sidebar.

### Step 3.1 — Reflected XSS

Open the **Reflected XSS** lesson.

1. Read the scenario
2. Find the input field that reflects user input back in the page
3. Enter a basic XSS payload: `<script>alert('XSS by [your initials]')</script>`
4. Submit and observe whether a JavaScript alert fires

Note: modern browsers have XSS auditors that may suppress some reflected XSS. If the alert does not fire, try: `<img src=x onerror=alert('XSS')>`

**Record in your lab notes:** Did the browser execute the injected script? What does this indicate about the application's output encoding?

### Step 3.2 — DOM-Based XSS

Open the **DOM-based XSS** lesson in WebGoat.

1. Read the explanation of DOM-based XSS versus reflected/stored XSS
2. Complete the challenge as instructed

**Lab Reflection Question 2:** Write a paragraph (four to six sentences) describing:

- The difference between reflected XSS, stored XSS, and DOM-based XSS
- Which type is most dangerous and why
- What specific output encoding rule would have prevented the reflected XSS you demonstrated (be specific about HTML context encoding)

---

## Part 4 — Broken Access Control / IDOR (15 minutes)

Navigate to the **(A1) Broken Access Control** section.

### Step 4.1 — Insecure Direct Object Reference

Open the **Insecure Direct Object Reference** lesson.

1. Read the scenario: a user profile endpoint exposes a direct database reference
2. Follow the lesson to access another user's profile by manipulating the URL parameter
3. Note the original URL parameter value and the value you changed it to

**Record in your lab notes:** The original URL parameter value was ______. The modified value that revealed another user's data was ______.

### Step 4.2 — Analyze the Vulnerability

**Lab Reflection Question 3:** Write a paragraph (four to six sentences) addressing:

- What specific check was missing from the server-side code that allowed this access
- How indirect object references would have prevented this attack
- How this vulnerability relates to the OWASP A01 category (Broken Access Control)

---

## Part 5 — SAST Findings Analysis (20 minutes)

In this section, you analyze pre-generated SAST output rather than running a SAST tool (which requires a code repository to scan). This simulates what a developer sees in a CI/CD pipeline.

### Step 5.1 — Review Simulated SAST Report

The following is a simulated SAST finding summary. Analyze it as if it were from your organization's CI/CD pipeline:

---

**SAST Scan Report — Simulated Output**

Tool: Semgrep (simulated)
Repository: internal-webapp
Branch: feature/user-profile
Scan time: 2 minutes 14 seconds

**Finding 1 — HIGH severity**
File: `src/database/userQueries.js`
Line: 47
Rule: `javascript.lang.security.audit.sqli.node-mssql-sqli`
Message: Detected string concatenation with user-controlled input in a SQL query. This could allow SQL injection. Use parameterized queries.
Code: `const query = "SELECT * FROM profiles WHERE userId = " + req.params.userId;`

**Finding 2 — MEDIUM severity**
File: `src/views/profile.html`
Line: 203
Rule: `html.security.audit.xss.script-tag-injection`
Message: User-controlled data is rendered into the page without HTML encoding. This could allow XSS.
Code: `<p>Welcome back, <%= userData.displayName %>!</p>` (using EJS template without HTML escaping)

**Finding 3 — CRITICAL severity**
File: `src/config/database.js`
Line: 12
Rule: `generic.secrets.security.detected-password`
Message: Hardcoded password detected in source code.
Code: `const dbPassword = "Tr0ub4dor&3";`

**Finding 4 — LOW severity**
File: `src/utils/crypto.js`
Line: 88
Rule: `javascript.lang.security.audit.md5-used`
Message: MD5 is a weak cryptographic hash function. Consider using SHA-256 or stronger.
Code: `const hash = crypto.createHash('md5').update(data).digest('hex');`

---

### Step 5.2 — Complete the SAST Analysis Table

For each finding, complete the table:

| Finding | Vulnerability Class | OWASP Category | Remediation (one sentence) | False Positive? Why or why not? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

**Lab Reflection Question 4:** Findings 1 and 4 are marked HIGH and LOW respectively. A developer argues Finding 4 (MD5) should be fixed first because it is "in the crypto utils" and "affects everything." Evaluate this argument. Is the developer correct about prioritization? Use the concept of exploitability and impact in your answer (four to six sentences).

---

## Part 6 — Cleanup (5 minutes)

Stop the WebGoat container:

```bash
docker stop $(docker ps -q --filter ancestor=webgoat/webgoat)
```

Or stop it from Docker Desktop.

---

## Lab Report Submission Requirements

Submit a single document containing:

1. Completed lab notes from Parts 2, 3, and 4 (SQL queries, XSS payloads observed, IDOR parameter values)
2. Answers to all four Lab Reflection Questions (numbered, full paragraphs)
3. Completed SAST analysis table (Part 5)
4. One concluding paragraph (five to seven sentences) describing how SAST and DAST complement each other — what each tool would find in this application that the other would miss

**Format:** PDF or Word document

**Length:** Minimum 600 words excluding tables and code snippets

---

## Grading Rubric

| Component | Points |
|---|---|
| Lab notes — SQL injection exercises (queries recorded) | 10 |
| Lab Reflection Question 1 — parameterized queries explanation | 20 |
| Lab Reflection Question 2 — XSS types and prevention | 20 |
| Lab Reflection Question 3 — IDOR analysis | 15 |
| SAST analysis table — all four findings complete | 20 |
| Lab Reflection Question 4 — prioritization reasoning | 15 |
| **Total** | **100** |

---

*Texas Wesleyan University | CIS-4328 Information Security | Module 10*
