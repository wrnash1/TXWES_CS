# Lab Activity: Module 09 — Web Application Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Authorization and Legal Notice

> **REQUIRED BEFORE STARTING:** All web application testing in this lab occurs EXCLUSIVELY against DVWA (Damn Vulnerable Web Application) running in your local isolated VM, or against the TryHackMe room specified below. You have NO authorization to use Burp Suite, sqlmap, or any web testing tool against any website, web application, or API that you do not own and have not received explicit written authorization to test. SQL injection and XSS attacks against unauthorized applications are violations of the Computer Fraud and Abuse Act and may violate the Electronic Communications Privacy Act. There are no exceptions. If you are unsure whether a target is authorized, STOP and contact Professor Nash.

---

## Lab Overview

In this lab you will configure Burp Suite as an HTTP proxy, manually exploit SQL injection and XSS vulnerabilities in DVWA at multiple security levels, test for IDOR vulnerabilities, and use sqlmap for automated SQLi. You will document each finding with evidence as you would in a professional web application penetration test.

**Estimated Time:** 2.5–3 hours

**Authorized Lab Targets:**

- DVWA (Damn Vulnerable Web Application) — running in your local Metasploitable 2 VM or a dedicated DVWA Docker container
- TryHackMe room: "OWASP Top 10" — [https://tryhackme.com/room/owasptop10](https://tryhackme.com/room/owasptop10)

**DVWA Access:**

- URL: `http://METASPLOITABLE_IP/dvwa/` (or your Docker container's IP)
- Default credentials: `admin` / `password`
- Set security level to **Low** before beginning (DVWA Security tab in the top menu)

**Required Setup:**

- Kali Linux with Burp Suite Community Edition and Firefox installed
- Burp CA certificate installed in Firefox
- Firefox configured to proxy through `127.0.0.1:8080`
- DVWA accessible and security level set to Low

---

## Part 1 — Burp Suite Configuration (20 minutes)

### Step 1.1 — Configure Proxy

Launch Burp Suite Community Edition. Navigate to the Proxy tab and confirm the listener is active on `127.0.0.1:8080`.

In Firefox, open Settings and search for "proxy." Set the manual proxy to HTTP: `127.0.0.1`, Port: `8080`. Apply the same for HTTPS.

### Step 1.2 — Install the Burp CA Certificate

With the proxy configured and Firefox pointing through Burp, navigate to `http://burp` in Firefox. Download the CA Certificate (`cacert.der`). In Firefox, go to Preferences > Privacy & Security > Certificates > View Certificates > Import. Import `cacert.der` and check "Trust this CA to identify websites."

Verify: Navigate to `https://www.google.com`. If you see the page without a certificate error, Burp's HTTPS interception is working.

### Step 1.3 — Explore DVWA in Proxy

Navigate to your DVWA instance. With Intercept set to On in Burp, log in to DVWA. Observe each request in the Proxy Intercept tab before forwarding it. After the login request passes, turn Intercept Off and explore the DVWA menu.

Review the Proxy HTTP History tab. Take a screenshot showing at least five captured requests from your DVWA browsing session.

In your lab notes, record: What cookies does DVWA set? What does `PHPSESSID` represent?

---

## Part 2 — SQL Injection with Burp Suite (50 minutes)

### Step 2.1 — Identify the Vulnerable Parameter

Navigate to DVWA > SQL Injection. The page shows a "User ID" field. Enter `1` and click Submit. Observe the response.

Turn Intercept On in Burp. Submit the form again. In Burp, observe the GET request and note the `id` parameter. Forward the request and turn Intercept Off.

Send this request to Repeater (right-click > Send to Repeater).

### Step 2.2 — Confirm SQLi with a Quote

In Repeater, change `id=1` to `id=1'` and click Send. Observe the response.

If you see a SQL error message such as `You have an error in your SQL syntax`, the input is being interpreted as SQL. Take a screenshot of the error.

### Step 2.3 — Basic Authentication Bypass Pattern

Test the classic always-true pattern in Repeater:

```text
id=1' OR '1'='1
```

What does the response contain? Record the number of records returned and the data shown.

### Step 2.4 — Union-Based SQLi — Column Enumeration

Determine the number of columns in the query:

```text
id=1' ORDER BY 1--+
id=1' ORDER BY 2--+
id=1' ORDER BY 3--+
```

When the response returns an error, you have exceeded the column count. Record how many columns the query uses.

### Step 2.5 — Union-Based Data Extraction

Using the correct number of columns, extract database information:

```text
id=1' UNION SELECT null, database()--+
id=1' UNION SELECT null, user()--+
id=1' UNION SELECT null, table_name FROM information_schema.tables WHERE table_schema=database()--+
```

From the last query, identify the table names in the DVWA database. Record them.

Extract data from the users table:

```text
id=1' UNION SELECT null, concat(user,':',password) FROM users--+
```

Take a screenshot showing the extracted usernames and password hashes.

### Step 2.6 — Automated SQLi with sqlmap

Switch to a terminal. Use sqlmap against the same DVWA endpoint. You need your PHPSESSID cookie from the Burp Proxy history.

```bash
sqlmap -u "http://DVWA_IP/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=YOUR_SESSION_ID;security=low" \
  --dbs
```

After identifying the databases, dump the DVWA users table:

```bash
sqlmap -u "http://DVWA_IP/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" \
  --cookie="PHPSESSID=YOUR_SESSION_ID;security=low" \
  -D dvwa -T users --dump
```

Take a screenshot of the sqlmap output showing dumped credentials.

---

## Part 3 — Cross-Site Scripting (40 minutes)

### Step 3.1 — Reflected XSS

Navigate to DVWA > XSS (Reflected). The page has a "What's your name?" field.

Enter the following payload in the field:

```html
<script>alert('XSS')</script>
```

If an alert dialog appears, reflected XSS is confirmed. Take a screenshot of the alert.

Examine the URL in your browser's address bar. Note the payload appears in the URL. This is how reflected XSS is typically shared — via a crafted link.

### Step 3.2 — Stored XSS

Navigate to DVWA > XSS (Stored). Enter a message in the guestbook form.

In the Name field, enter:

```html
<script>alert('Stored XSS')</script>
```

In the Message field, enter a normal message and submit. Reload the page. Does the alert trigger on page load?

Take a screenshot showing the stored XSS executing on page reload. Record: Why is this more dangerous than reflected XSS? Who is affected?

### Step 3.3 — Cookie Stealing Simulation

In the Reflected XSS field, enter a payload that would exfiltrate the cookie value (for lab documentation only — this goes to your browser console, not an external server):

```html
<script>document.write(document.cookie)</script>
```

Take a screenshot showing the cookie content written to the page. This demonstrates what a real attacker could steal using XSS.

### Step 3.4 — XSS in Burp Repeater

Navigate to DVWA > XSS (Reflected). Capture the form submission in Burp and send it to Repeater. In Repeater, test the following bypass payloads and record which ones execute (shown by alert or other visible effect):

```html
<img src=x onerror=alert('XSS')>
<svg onload=alert(1)>
<body onload=alert('XSS')>
```

---

## Part 4 — IDOR Testing (30 minutes)

### Step 4.1 — DVWA File Inclusion as IDOR Proxy

DVWA does not have a dedicated IDOR module, but DVWA's file inclusion vulnerability demonstrates unauthorized object access. Navigate to DVWA > File Inclusion (security level: Low).

The URL will show something like:

```text
http://DVWA_IP/dvwa/vulnerabilities/fi/?page=include.php
```

Modify the `page` parameter in Burp Repeater:

```text
page=../../../../../../etc/passwd
```

If the file contents appear in the response, this demonstrates path traversal — a close relative of IDOR. Take a screenshot.

### Step 4.2 — IDOR Concept Documentation

In your lab notes, create a hypothetical IDOR scenario based on the DVWA user data you extracted in Part 2. Write:

- The vulnerable URL pattern that would exist if DVWA had a user profile page
- The test you would perform to confirm IDOR
- The impact of a confirmed IDOR in the context of the DVWA user data
- A remediation recommendation

---

## Part 5 — TryHackMe OWASP Top 10 Room (20 minutes)

Complete at least three tasks from the TryHackMe "OWASP Top 10" room. Focus on the Injection, Broken Access Control, and XSS tasks if available in the current room version.

For each completed task, record:

- The task name and OWASP category
- The vulnerability demonstrated
- The answer to the task question

Take a screenshot of your room progress showing the completed tasks.

---

## Deliverables

Submit to Canvas:

1. **Burp Proxy history screenshot** — showing at least five captured DVWA requests
2. **SQLi confirmation screenshot** — SQL error message from single quote test
3. **Union-based extraction screenshot** — showing extracted usernames and hashes from DVWA
4. **sqlmap dump screenshot** — showing automated credential extraction
5. **Reflected XSS screenshot** — alert dialog
6. **Stored XSS screenshot** — alert on page reload with explanation of greater impact
7. **Cookie display screenshot** — document.cookie rendered via XSS
8. **Path traversal screenshot** — /etc/passwd contents via file inclusion
9. **IDOR documentation** — hypothetical scenario from Step 4.2
10. **TryHackMe progress screenshot** — three completed tasks
11. **Web App Test Summary** — 200–300 words: which vulnerability class you found most impactful, what a real attacker could accomplish with each finding, and what single remediation would have the highest impact

---

## Grading Rubric

| Component | Points | Criteria |
|-----------|--------|---------|
| Burp proxy history | 5 | Screenshot shows multiple requests |
| SQLi confirmation | 10 | Error message or always-true output |
| Union extraction | 15 | Usernames and hashes extracted |
| sqlmap dump | 15 | Automated extraction screenshot |
| Reflected XSS | 10 | Alert dialog screenshot |
| Stored XSS + explanation | 10 | Alert on reload, impact explained |
| Cookie XSS + path traversal | 10 | Both screenshots present |
| IDOR documentation | 10 | Scenario, test, impact, remediation |
| TryHackMe tasks | 10 | Three tasks documented |
| Summary | 5 | 200–300 words, professional |
| **Total** | **100** | |

---

## Troubleshooting

**Burp Proxy not intercepting HTTPS:**
Confirm the CA certificate is installed in Firefox. Go to `http://burp` in Firefox (with proxy on) and re-download/re-import the certificate.

**DVWA shows blank page or database error:**
Navigate to `http://DVWA_IP/dvwa/setup.php` and click "Create / Reset Database."

**sqlmap session cookie expiring:**
Log back into DVWA in Firefox, copy the new PHPSESSID from Burp Proxy history, and update your sqlmap command.

**XSS alert not appearing:**
Confirm DVWA security is set to Low. Medium and High levels add filters that block basic script tags.

**TryHackMe room tasks changed:**
TryHackMe periodically updates room content. If specific tasks differ from the lab, document the tasks you completed and explain the OWASP category each covered.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Multi-Vulnerability DVWA Exploitation Chain

On your authorized DVWA instance, set the security level to Low and execute a three-stage exploitation chain. First, exploit the SQL Injection module using a union-based injection to extract the names of all database tables: `1 UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema=database()--`. Second, use the File Upload module to upload a PHP webshell (a single-line PHP file: `<?php system($_GET['cmd']); ?>`) and confirm remote code execution by accessing the file with `?cmd=id`. Third, exploit the Command Injection module to confirm OS command execution using a payload that identifies the server's network interfaces. Document each step with a screenshot showing the request in Burp Repeater, the server response, and your interpretation of the result. Write a one-paragraph business impact statement for each finding as it would appear in a professional penetration test report.

### Challenge 2: Burp Suite Intercept and Manipulation Analysis

Configure Burp Suite as your browser proxy and browse through DVWA's IDOR-equivalent functionality (the Insecure CAPTCHA or user management module, or use Burp Repeater to test object ID manipulation on any parameter you identify). For each parameter you test, document: the original parameter value and what resource it references, the modified value you tested and what resource you attempted to access, the server's response code and response body indicating success or failure, and the OWASP Top 10 category and specific risk description. Then write a comparison of which vulnerability class — SQLi, XSS, or IDOR — would have the highest business impact in a real e-commerce application, with justification based on the data accessible through each attack type.

### Reflection Questions

1. During SQL injection testing you discovered that the application returns verbose error messages including stack traces and SQL query fragments when invalid syntax is submitted. Explain how you would document this as a finding in the penetration test report — what is the vulnerability name, the OWASP category, the evidence you would include, and why verbose error messages are a security risk even if direct SQL injection is not confirmed?

2. A colleague argues that web application scanners like OWASP ZAP or Nikto can fully replace manual web application testing because they cover all OWASP Top 10 categories automatically. Using your experience from the Module 09 lab, explain two specific vulnerability classes or test scenarios where automated scanner output would be incomplete or inaccurate without manual verification, and what specific manual technique you would use to complete the testing.

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
