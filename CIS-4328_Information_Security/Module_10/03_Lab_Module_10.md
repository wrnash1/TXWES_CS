# Lab: Module 10 — Application Security

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

In this lab you will analyze a vulnerable web application to identify OWASP Top 10 vulnerabilities, test parameterized query defenses, evaluate a CI/CD pipeline for missing security gates, and examine code signing output. All activities use free, legal tools and intentionally vulnerable applications designed for educational use.

**Estimated completion time:** 90 to 120 minutes

**Tools required:** OWASP WebGoat (Docker or standalone JAR), Burp Suite Community Edition, browser developer tools

---

## Learning Outcomes

By completing this lab you will be able to:

- Demonstrate an SQL injection attack on a vulnerable application and explain why it works.
- Demonstrate parameterized query defense and explain why it blocks injection.
- Identify OWASP Top 10 vulnerabilities in a web application walkthrough.
- Evaluate a CI/CD pipeline configuration for missing security gates.
- Interpret code signing output from a command-line tool.

---

## Part 1 — Setup: OWASP WebGoat

WebGoat is an intentionally insecure Java web application maintained by OWASP. It is designed for learning web application security in a safe, legal environment.

### Step 1 — Download and Run WebGoat

Option A (Docker, recommended):

```
docker pull webgoat/webgoat
docker run -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

Option B (standalone JAR):

Download `webgoat-2023.4.jar` from github.com/WebGoat/WebGoat/releases and run:

```
java -jar webgoat-2023.4.jar --server.port=8080
```

### Step 2 — Access WebGoat

Open your browser and navigate to `http://127.0.0.1:8080/WebGoat/login`. Register a new account (username and password of your choice — this is local only).

---

## Part 2 — SQL Injection Exercise

### Step 1 — Navigate to SQL Injection

In WebGoat, select **A1 Injection** from the left menu, then select **SQL Injection (intro)**.

### Step 2 — Basic Injection Attack

In Exercise 3 (Try It! String SQL Injection), the application asks for an employee last name. In the Name field enter:

```
Smith' OR '1'='1
```

Observe the results. The query returns all employees because the injected condition `'1'='1'` is always true.

**Lab Question 1:** Write the SQL query the application constructed after your input was inserted. Explain why the WHERE clause behavior changed.

### Step 3 — Authentication Bypass

Navigate to **SQL Injection (advanced)**, Exercise 5. Attempt to log in as the user `tom` without knowing the password by entering:

```
tom'--
```

as the username and any value as the password.

**Lab Question 2:** Why does the double-dash (`--`) comment character break the authentication check? What query structure did the developer write that made this possible?

### Step 4 — Parameterized Query Defense

In Exercise 9, WebGoat demonstrates a parameterized version of the same query. Attempt the same injection payload. Observe that the application rejects it.

**Lab Question 3:** Write one to three sentences explaining why parameterized queries prevent injection. In your explanation, describe what happens to the single-quote in your payload when it is treated as a literal data value.

---

## Part 3 — Cross-Site Scripting Exercise

### Step 1 — Navigate to XSS

In WebGoat, select **A7 Cross-Site Scripting** from the left menu.

### Step 2 — Reflected XSS

In the Reflected XSS exercise, enter the following payload in the search field:

```
<script>alert('XSS')</script>
```

Observe whether the application reflects and executes the script.

**Lab Question 4:** Describe the difference between reflected XSS and stored XSS. Which is more dangerous from an attacker's perspective, and why?

### Step 3 — DOM XSS

Navigate to the DOM-based XSS exercise. Follow the instructions to inject a script through a URL parameter that is processed by client-side JavaScript without server-side reflection.

**Lab Question 5:** In a DOM-based XSS attack, does the malicious payload ever reach the server? What does this mean for server-side input validation as a defense?

---

## Part 4 — Access Control and IDOR Exercise

### Step 1 — Navigate to Access Control

In WebGoat, select **A1 Broken Access Control**, then **Insecure Direct Object References**.

### Step 2 — IDOR Exploitation

The exercise presents a profile page at a predictable URL. Use the browser address bar or Burp Suite to modify the numeric identifier in the URL to attempt to access another user's profile.

**Lab Question 6:** Describe what server-side check was missing that allowed IDOR to succeed. Write a pseudocode check that would have prevented unauthorized access.

---

## Part 5 — SAST and DAST Pipeline Analysis

For this part, analyze the following fictional CI/CD pipeline configuration and identify the missing security gates.

```yaml
# ci-pipeline.yml (fictional example)
stages:
  - build
  - unit-test
  - deploy-staging
  - deploy-production

build:
  script:
    - npm install
    - npm run build

unit-test:
  script:
    - npm test

deploy-staging:
  script:
    - kubectl apply -f k8s/staging/

deploy-production:
  script:
    - kubectl apply -f k8s/production/
  only:
    - main
```

**Lab Question 7:** Identify four specific security gates that are missing from this pipeline. For each missing gate, state what it would catch and at which stage it should be inserted.

**Example format for your answer:**

- Missing gate: [name] | Stage to insert: [stage] | What it catches: [description]

---

## Part 6 — Code Signing Demonstration

### Step 1 — Generate a Self-Signed Certificate (Windows)

Open PowerShell and run:

```powershell
$cert = New-SelfSignedCertificate `
  -Subject "CN=Lab Code Signing" `
  -Type CodeSigningCert `
  -CertStoreLocation Cert:\CurrentUser\My

$cert.Thumbprint
```

Record the thumbprint output.

### Step 2 — Create and Sign a Test Script

Create a file named `hello.ps1` with content:

```powershell
Write-Output "Hello from signed script"
```

Sign the script:

```powershell
$cert = Get-ChildItem Cert:\CurrentUser\My -CodeSigningCert | Select-Object -First 1
Set-AuthenticodeSignature -FilePath .\hello.ps1 -Certificate $cert
```

### Step 3 — Inspect the Signature

Run:

```powershell
Get-AuthenticodeSignature .\hello.ps1
```

Then open `hello.ps1` in a text editor and scroll to the bottom to view the embedded signature block.

**Lab Question 8:** What does the `SignerCertificate` field in the Get-AuthenticodeSignature output tell you? What does the `Status: Valid` result confirm?

### Step 4 — Tamper Test

Using Notepad, add a comment line to `hello.ps1` after the signature block, then re-run Get-AuthenticodeSignature.

**Lab Question 9:** What status does the signature show after tampering? What does this demonstrate about the integrity guarantee of code signing?

---

## Part 7 — Reflection

**Lab Question 10:** The SolarWinds SUNBURST attack bypassed code signing even though the malicious binary was legitimately signed. Based on what you observed in Parts 5 and 6, describe two pipeline controls that would have made the SolarWinds attack more difficult to execute.

---

## Deliverables

Submit a lab report containing:

- Answers to Lab Questions 1 through 10.
- Screenshots for Part 2 Steps 2 and 3, Part 3 Step 2, Part 4 Step 2, and Part 6 Steps 3 and 4.
- A one-paragraph summary describing the most significant vulnerability you found and the single highest-value control you would implement first in a real development environment.

---

## Grading Rubric

| Component | Points |
|---|---|
| Part 2 — SQL Injection (Questions 1–3 + screenshots) | 25 |
| Part 3 — XSS (Questions 4–5 + screenshot) | 15 |
| Part 4 — IDOR (Question 6 + screenshot) | 15 |
| Part 5 — Pipeline Analysis (Question 7) | 20 |
| Part 6 — Code Signing (Questions 8–9 + screenshots) | 15 |
| Part 7 — Reflection (Question 10) | 10 |
| **Total** | **100** |

---

*End of Lab — Module 10*
