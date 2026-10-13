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

---

## Part 9 — Challenge Exercise

### Challenge 1: Secure Code Review and Vulnerability Chain Analysis

A fintech startup has asked you to review the security of their loan application API. The following pseudocode represents key sections of their codebase. Analyze each snippet and answer the questions that follow.

**Snippet A — Loan Status Endpoint:**

```python
@app.route('/api/loan/status')
def loan_status():
    loan_id = request.args.get('loan_id')
    query = "SELECT * FROM loans WHERE loan_id = '" + loan_id + "'"
    result = db.execute(query)
    return jsonify(result)
```

**Snippet B — Document Retrieval Endpoint:**

```python
@app.route('/api/document')
def get_document():
    filename = request.args.get('file')
    path = '/var/app/documents/' + filename
    with open(path, 'rb') as f:
        return send_file(f)
```

**Snippet C — External Data Fetch:**

```python
@app.route('/api/fetch-rate')
def fetch_rate():
    url = request.args.get('source_url')
    response = requests.get(url)
    return response.text
```

**Snippet D — Password Reset:**

```python
def reset_password(email):
    token = str(random.randint(1000, 9999))
    db.store_reset_token(email, token)
    send_email(email, f'Your reset code is: {token}')
```

1. For each snippet (A through D), identify: the OWASP Top 10 category violated, the specific attack an adversary would use to exploit it, a concrete attack payload or scenario demonstrating the exploit, and the corrected code using secure implementation practices. Present your analysis for each snippet in a structured format.

2. An attacker chains Snippets A and B together in a single attack session. First, they use Snippet A's vulnerability to enumerate the `loan_id` values belonging to another customer, and then use Snippet B's vulnerability to retrieve the PDF loan agreement for that customer. Trace the full attack chain step by step. For each step, identify: what the attacker sends, what the server returns, and what OWASP category is being exploited. Then explain why addressing only one of the two vulnerabilities does not fully protect the customer's document.

3. The startup's CISO asks you to estimate the CVSS v3.1 Base Score for the vulnerability in Snippet C. Using the CVSS v3.1 scoring rubric (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability Impact), assign a score and justify each metric selection. Then compare this score to the vulnerability in Snippet D and explain why Snippet D may be more dangerous in practice despite having a lower theoretical CVSS score.

4. The startup wants to add security gates to their CI/CD pipeline to detect all four vulnerabilities before they reach production. For each of the four snippets, identify whether a SAST tool, a DAST tool, or both would detect the vulnerability in an automated pipeline scan, and explain the detection mechanism each tool type uses for that specific vulnerability class.

### Challenge 2: Threat Modeling and SDLC Integration

A healthcare SaaS company is building a patient portal that allows patients to view lab results, message their physician, and request prescription refills. The portal is a React single-page application (SPA) with a REST API backend. Patient data is subject to HIPAA. You have been engaged as the security architect for the design phase.

1. Conduct a STRIDE threat model for the patient portal. For each STRIDE category, identify at least two specific threats relevant to this application's architecture (SPA + REST API + HIPAA data), the system component at risk, the attack mechanism, and the specific security control that mitigates it. Present your threat model in a table with columns for STRIDE Category, Threat Description, Affected Component, and Mitigation.

2. The development team uses a React SPA. A junior developer proposes using `dangerouslySetInnerHTML` in React to render physician notes that contain formatting. Explain why this creates a stored XSS risk in a healthcare context, describe the specific patient harm that could result from session cookie theft via XSS in a HIPAA-regulated portal, and provide the correct React implementation pattern that preserves the formatting requirement without introducing XSS risk.

3. The product team requests a "share lab results" feature that lets patients generate a shareable link to a specific lab result. The link will be accessible without login for 72 hours. Design the security requirements for this feature. Your design must address: how the share token is generated (algorithm and entropy requirements), how the 72-hour expiration is enforced, what data is included in the shared view versus withheld, rate limiting on share link generation, and how the organization demonstrates HIPAA compliance for this feature (what audit log entries are required).

4. Three months after launch, a DAST scan discovers that the prescription refill endpoint is vulnerable to CSRF — an attacker who tricks a logged-in patient into visiting a malicious page can submit a refill request on their behalf. The engineering lead argues that adding CSRF protection will require a two-week refactor. As the security architect, write a prioritized remediation plan that includes: an immediate compensating control deployable in hours, the root cause of the CSRF vulnerability in SPA architectures, the correct long-term fix (specify whether SameSite cookie attribute, CSRF token, or double-submit cookie pattern is most appropriate for this SPA architecture and why), and a post-fix verification step using DAST.

### Reflection Questions

1. After completing both challenges, explain why application security cannot be achieved through testing alone, even if a development team runs both SAST and DAST on every commit. Address the specific vulnerability categories that SAST and DAST cannot reliably detect (business logic flaws, insecure design, improper authorization), explain why these require threat modeling and security requirements during the design phase, and describe the concept of "residual risk" — the risk that remains even after testing — and how a mature DevSecOps program manages it through defense-in-depth controls like WAF, runtime application self-protection (RASP), and anomaly detection.

2. In Challenge 1, the SSRF vulnerability in Snippet C received a high CVSS score, but Snippet D's weak password reset token may be more dangerous in practice. This illustrates a limitation of CVSS as a sole risk metric. Identify two additional factors beyond CVSS Base Score that a security team should use when prioritizing remediation, explain how the KEV catalog addresses one of those factors, and describe a scenario where a CVSS 5.0 Medium vulnerability should be patched before a CVSS 9.8 Critical vulnerability in the same organization's environment.

---

*End of Lab — Module 10*
