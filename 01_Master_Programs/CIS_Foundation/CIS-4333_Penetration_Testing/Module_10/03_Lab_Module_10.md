# Lab Activity: Module 10 — Web Application Exploit Methods

## Course: CIS-4333 Penetration Testing

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Overview

In this lab you will perform hands-on web application penetration testing against DVWA (Damn Vulnerable Web Application), a deliberately insecure PHP application designed for security training. You will use Burp Suite Community Edition as your intercepting proxy and SQLMap for automated SQL injection exploitation. All activities are performed in an isolated lab environment with no connection to production systems.

Estimated time: 90–120 minutes.

---

## Learning Objectives

By the end of this lab, you will be able to:

- Configure Burp Suite as an intercepting proxy and use Repeater for manual testing
- Identify and exploit a reflected XSS vulnerability by injecting a test payload
- Identify and exploit a SQL injection vulnerability manually using Burp Repeater
- Automate SQL injection with SQLMap to enumerate the database
- Perform a directory traversal attack to read a server-side file
- Document each finding with the required fields for a penetration test report

---

## Prerequisites

- Kali Linux VM (or a Parrot OS VM) with Burp Suite Community and SQLMap installed
- DVWA running locally via XAMPP, Docker, or a TryHackMe/HackTheBox lab instance
- DVWA security level set to Low for initial exercises
- Firefox configured to use Burp proxy at `127.0.0.1:8080`
- Burp CA certificate installed in Firefox to intercept HTTPS

If you are using TryHackMe, the "DVWA" room provides a pre-configured environment accessible from your browser.

---

## Part 1 — Burp Suite Setup and Traffic Interception (15 minutes)

### Step 1.1 — Configure the Proxy

1. Open Burp Suite Community Edition.
2. Navigate to Proxy > Options and confirm the listener is running on `127.0.0.1:8080`.
3. In Firefox, open Settings > Network Settings and configure Manual Proxy to `127.0.0.1`, port `8080` for HTTP and HTTPS.
4. Navigate to `http://burp` in Firefox and download the Burp CA certificate. Install it in Firefox under Settings > Privacy & Security > View Certificates > Authorities > Import.

### Step 1.2 — Verify Interception

1. Enable Intercept in Burp under Proxy > Intercept.
2. Navigate to the DVWA login page in Firefox.
3. Observe the login request appear in Burp. Note the POST parameters.
4. Click Forward to send the request. Log in with username `admin` and password `password`.

**Deliverable 1:** Screenshot showing a captured HTTP request in Burp Intercept with visible POST parameters.

---

## Part 2 — Reflected XSS (20 minutes)

### Step 2.1 — Locate the Vulnerable Field

1. In DVWA, navigate to XSS (Reflected).
2. The page displays a "What is your name?" input field.

### Step 2.2 — Test with a Basic Payload

1. Enter the following into the name field and submit:

```html
<script>alert('XSS-Test')</script>
```

2. If a JavaScript alert box appears, the field is vulnerable to reflected XSS.

### Step 2.3 — Cookie Theft Simulation

1. Enter the following payload to simulate session cookie exfiltration:

```html
<script>alert(document.cookie)</script>
```

2. The alert box should display the current session cookie value.
3. In Burp, switch to Proxy > HTTP History. Find the GET request containing your XSS payload in the URL parameter.
4. Right-click the request and send it to Repeater.

### Step 2.4 — Analyze in Repeater

1. In Repeater, modify the `name` parameter value and observe how the application reflects it into the HTML response.
2. Identify the exact location in the HTML where your input appears unsanitized.

**Deliverable 2:** Screenshot of the alert box showing the session cookie value, and a screenshot of Burp Repeater showing the injection point in the response body.

---

## Part 3 — Manual SQL Injection with Burp Repeater (25 minutes)

### Step 3.1 — Identify the Injection Point

1. In DVWA, navigate to SQL Injection.
2. Enter `1` in the User ID field and submit. Note the response showing a user's information.
3. In Burp Proxy History, locate the GET request with the `id` parameter.
4. Send the request to Repeater.

### Step 3.2 — Confirm Injection

1. In Repeater, change the `id` parameter value to `1'` (with a single quote).
2. Send the request. A database error in the response confirms the application is vulnerable.
3. Try `1' OR '1'='1` — the response should return all users in the table.

### Step 3.3 — Determine Column Count

1. Test `1' ORDER BY 1--` — submit and note whether an error occurs.
2. Increment: `1' ORDER BY 2--`, then `1' ORDER BY 3--`.
3. When an error occurs, the column count is one less than the failing number.

### Step 3.4 — Union-Based Data Extraction

1. Assuming two columns, inject:

```
1' UNION SELECT null, version()--
```

2. The database version should appear in the response alongside or instead of the normal output.
3. Next, extract the current database name:

```
1' UNION SELECT null, database()--
```

**Deliverable 3:** Screenshots from Burp Repeater showing (a) the error confirming injection, (b) the ORDER BY column count test, and (c) the database version extracted via UNION injection.

---

## Part 4 — Automated SQL Injection with SQLMap (20 minutes)

### Step 4.1 — Capture the Request

1. In Burp Proxy History, right-click the DVWA SQL Injection request and select "Save item." Save it as `sqli_request.txt`.

### Step 4.2 — Run SQLMap

1. Open a terminal and run SQLMap using the saved request file:

```bash
sqlmap -r sqli_request.txt --dbs --batch
```

2. The `--dbs` flag enumerates all databases. The `--batch` flag accepts defaults automatically.
3. Identify the DVWA database in the output.

### Step 4.3 — Enumerate Tables and Dump Data

1. Enumerate tables in the DVWA database:

```bash
sqlmap -r sqli_request.txt -D dvwa --tables --batch
```

2. Dump the users table:

```bash
sqlmap -r sqli_request.txt -D dvwa -T users --dump --batch
```

3. Note the usernames and password hashes in the output. SQLMap may attempt to crack the hashes automatically.

**Deliverable 4:** Screenshot of SQLMap output showing enumerated databases, tables, and at least one row from the users table.

---

## Part 5 — Directory Traversal (15 minutes)

### Step 5.1 — Locate the Vulnerable Parameter

1. In DVWA, navigate to File Inclusion.
2. The page URL contains a `page` parameter: `?page=include.php`.

### Step 5.2 — Test Traversal Payloads

1. Modify the URL parameter directly in the browser or in Burp Repeater:

```
?page=../../../../etc/passwd
```

2. If the page displays the contents of `/etc/passwd`, directory traversal is confirmed.
3. Try URL-encoded variants to test filter bypass:

```
?page=..%2F..%2F..%2F..%2Fetc%2Fpasswd
```

**Deliverable 5:** Screenshot showing the contents of `/etc/passwd` rendered in the DVWA page via directory traversal.

---

## Part 6 — Findings Documentation (15 minutes)

For each vulnerability discovered, complete a finding record using the template below. Submit all finding records together with your screenshots.

### Finding Template

- **Finding Title:** (e.g., Reflected Cross-Site Scripting in Name Parameter)
- **Severity:** Critical / High / Medium / Low / Informational
- **CVSS Score:** (estimate using CVSS 3.1 base score calculator)
- **Affected URL and Parameter:** (exact URL and parameter name)
- **Description:** One paragraph explaining what the vulnerability is and how it was confirmed.
- **Proof of Concept:** Copy the exact HTTP request from Burp Repeater that demonstrates the vulnerability.
- **Business Impact:** One to two sentences explaining what an attacker could do if this vulnerability existed in a production system.
- **Remediation Recommendation:** One to three sentences explaining how to fix the vulnerability.

Complete this template for: Reflected XSS, SQL Injection, and Directory Traversal.

---

## Troubleshooting

- If Burp does not intercept traffic: verify Firefox is using the correct proxy address and port, and confirm Intercept is toggled ON in Burp.
- If SQLMap returns "connection refused": ensure DVWA is running and accessible at the URL in your saved request file.
- If directory traversal returns the PHP source instead of file contents: DVWA may be running on a Windows host; try `../../../../Windows/System32/drivers/etc/hosts` instead.
- If DVWA returns "Access Denied": confirm the security level is set to Low in DVWA Security settings.

---

## Submission Checklist

Before submitting, confirm you have included:

- [ ] Deliverable 1: Burp Intercept screenshot
- [ ] Deliverable 2: XSS alert box and Repeater screenshots
- [ ] Deliverable 3: SQL injection Repeater screenshots (error, column count, UNION result)
- [ ] Deliverable 4: SQLMap output screenshot
- [ ] Deliverable 5: Directory traversal result screenshot
- [ ] Three completed finding records (XSS, SQLi, Directory Traversal)

Submit all screenshots and finding records as a single PDF or ZIP file to the Canvas assignment portal.

---

---

## Part 9 — Challenge Exercise

### Challenge 1: Blind SQL Injection Time-Based Extraction

On your authorized DVWA target (security level: Low), navigate to the SQL Injection (Blind) module. Using Burp Repeater, manually test for time-based blind SQL injection by submitting: `1' AND SLEEP(5)--`. Observe the response time compared to a baseline request. Then extract the first character of the database name using: `1' AND IF(SUBSTRING(database(),1,1)='d',SLEEP(5),0)--`. Systematically adjust the character being tested until you confirm the first character. Document your complete methodology: the baseline response time, the sleep-confirmed response time, the injection payload for each character position tested, and the extracted character. Explain in writing why time-based blind injection is significantly harder to automate safely than union-based injection and what risk the `SLEEP()` function creates on a production database server.

### Challenge 2: File Upload Filter Bypass Analysis

On your authorized DVWA target, navigate to the File Upload module at security level Medium. Attempt to upload a PHP webshell (`shell.php`) — document the server's rejection message. Then attempt the following bypass techniques in order, documenting the result of each: (1) rename to `shell.php.jpg`, (2) rename to `shell.jpg.php`, (3) keep `.php` extension but change the `Content-Type` header in Burp Intercept from `application/x-php` to `image/jpeg`. For each attempt, record the request in Burp, the server's response, and whether the bypass succeeded. Write a structured analysis explaining what validation layer each technique attempts to bypass (extension blacklist, extension whitelist, MIME type check, content inspection) and what the most robust server-side file upload validation approach would include.

### Reflection Questions

1. During the lab you exploited SQL injection to extract data from the DVWA database. However, in a real engagement the client's production database may contain tens of thousands of records of customer PII. Using the legal and ethical framework from Modules 01 and 02, explain what level of data extraction is appropriate to confirm and document an SQL injection finding, and what language you would want in the RoE document before conducting any database enumeration against a production system.

2. You discovered both a reflected XSS vulnerability and a stored XSS vulnerability in the same DVWA application. Write a comparative risk analysis: which vulnerability receives the higher CVSS 3.1 base score and why, how the attack scope and victim population differ between the two types, and what remediation approach addresses both vulnerabilities at the root cause rather than through filtering.

*End of Module 10 Lab Activity*
