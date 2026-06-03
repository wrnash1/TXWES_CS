# Lab: Module 15 — Specialized Testing Environments

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Lab Authorization Statement

This lab is conducted against intentionally vulnerable web applications and APIs deployed in an isolated, professor-controlled lab environment. All testing is performed against systems specifically designed for security education. Testing any system other than the designated lab targets is unauthorized and may violate federal law.

---

## Lab Overview

- **Duration:** 3 hours
- **Environment:** Kali Linux VM, isolated lab network
- **Lab Targets:**
  - WebGoat (API and web application testing): http://10.99.60.10:8080/WebGoat
  - DVWA (Damn Vulnerable Web Application): http://10.99.60.11/dvwa
  - Juice Shop (OWASP API/application): http://10.99.60.12:3000
  - Lab JWT Service: http://10.99.60.13:5000 (custom lab application)
- **Required Tools:** Burp Suite Community, Postman, jwt_tool, Python 3

---

## Lab Objectives

By completing this lab, students will:

1. Identify and exploit BOLA (Broken Object Level Authorization) in a REST API.
2. Identify and exploit a JWT vulnerability (algorithm manipulation).
3. Perform GraphQL introspection and identify authorization weaknesses.
4. Analyze cloud IAM misconfiguration scenarios.
5. Conduct a passive OT/ICS network analysis on a simulated OT PCAP file.
6. Document API security findings in professional format.

---

## Part 1: REST API — Broken Object Level Authorization (45 minutes)

### Step 1.1: Configure Burp Suite Proxy

Open Burp Suite. Confirm the proxy listener is on 127.0.0.1:8080.

Configure Firefox in Kali to use Burp as proxy (Network Settings → Manual Proxy → 127.0.0.1:8080).

Navigate to Juice Shop: http://10.99.60.12:3000

### Step 1.2: Register and Authenticate

Register a test account (use labtest1@lab.local as email).

Log in and observe the authentication flow in Burp Proxy HTTP History. Identify:

- The endpoint handling login
- The response format (JWT bearer token or session cookie)
- How the token is included in subsequent requests

**Lab Report Item 1:** Screenshot the login request and response in Burp. Identify the authentication token format and where it appears in API requests.

### Step 1.3: Explore the API

Navigate to your account profile. Identify the API endpoint serving your user data. In Burp, send the profile request to Repeater.

Observe the structure of the request. Identify any object identifier (user ID, email) that appears in the URL or request body.

**Lab Report Item 2:** What API endpoint provides your profile data? What object identifier is used? Is this identifier sequential or random?

### Step 1.4: Test for BOLA

If the identifier is sequential (integer): Modify the identifier to attempt to access another user's profile.

In Burp Repeater, change the user identifier in the request to increment or decrement the value.

**Lab Report Item 3:** Were you able to access another user's profile by changing the identifier? Screenshot the successful BOLA response (or document that the application properly rejected the request with an authorization error). Classify this finding using OWASP API Top 10 category.

---

## Part 2: JWT Vulnerability Testing (45 minutes)

### Step 2.1: Connect to Lab JWT Service

The lab JWT service at http://10.99.60.13:5000 provides an authenticated API.

Register a test account:

```bash
curl -X POST http://10.99.60.13:5000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "labuser1", "password": "LabPassword1"}'
```

Login to obtain a JWT:

```bash
curl -X POST http://10.99.60.13:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "labuser1", "password": "LabPassword1"}'
```

Copy the returned JWT.

### Step 2.2: Decode and Analyze the JWT

Decode the JWT at jwt.io or using jwt_tool:

```bash
python3 jwt_tool.py [YOUR_JWT]
```

**Lab Report Item 4:** Document the JWT header and payload contents. What algorithm is specified in the header? What claims are in the payload? Note the expiration time and any role or privilege claims.

### Step 2.3: Test Algorithm Confusion

The lab service is intentionally configured to be vulnerable. Test the "alg:none" attack:

```bash
python3 jwt_tool.py [YOUR_JWT] -X a   # Test alg:none attack
```

Attempt to access the admin endpoint with the modified token:

```bash
curl -H "Authorization: Bearer [MODIFIED_JWT]" http://10.99.60.13:5000/admin
```

**Lab Report Item 5:** Was the alg:none attack successful? Screenshot the response. If successful, what data was returned from the admin endpoint? Write a two-sentence explanation of why this vulnerability exists and how the server should validate tokens.

### Step 2.4: Test Weak Secret Brute Force

```bash
python3 jwt_tool.py [YOUR_JWT] -C -d /usr/share/wordlists/rockyou.txt
```

**Lab Report Item 6:** Was the JWT secret found in rockyou.txt? If yes, what is the secret, and what does this enable an attacker to do? What minimum entropy is recommended for JWT secrets?

---

## Part 3: GraphQL Testing (30 minutes)

WebGoat includes a GraphQL exercise. Navigate to http://10.99.60.10:8080/WebGoat/start.mvc#lesson/GraphQL.lesson

### Step 3.1: Introspection Query

Use Burp Suite to intercept the GraphQL endpoint traffic. Identify the GraphQL endpoint URL.

In Burp Repeater, send an introspection query:

```graphql
{"query": "{ __schema { types { name fields { name } } } }"}
```

**Lab Report Item 7:** Document the types and fields returned by introspection. What sensitive operations or data fields are exposed in the schema?

### Step 3.2: IDOR via GraphQL

Based on the introspection results, attempt to access another user's data by substituting user IDs in a query.

**Lab Report Item 8:** Construct and document the GraphQL query used. Was access to another user's data successful? Screenshot the response.

---

## Part 4: Cloud IAM Misconfiguration Analysis (20 minutes)

This is a scenario analysis exercise — no live cloud environment access.

### Scenario

A cloud security assessment of a fictional company finds the following AWS IAM policy attached to an EC2 instance role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

The EC2 instance runs a web application that accepts user-supplied URLs and fetches their content (a feature for importing data from external sources).

**Lab Report Item 9:** Answer the following:

a. What is wrong with this IAM policy, and what CVSS score would you assign?

b. How does the web application's URL-fetching feature enable an IMDS attack?

c. Write the specific URL path that the SSRF attack would target to retrieve IAM credentials.

d. What two AWS security controls would mitigate this attack chain (one addressing the IAM policy, one addressing the IMDS)?

---

## Part 5: OT/ICS Passive Analysis (20 minutes)

A PCAP file has been placed at `/home/kali/lab_files/ot_capture.pcap`. This is a captured sample of simulated Modbus TCP traffic from a fictional water treatment facility. Analyze it passively.

### Step 5.1: Open in Wireshark

```bash
wireshark /home/kali/lab_files/ot_capture.pcap
```

Filter for Modbus traffic: `modbus`

### Step 5.2: Analyze Traffic

Identify:

- Source and destination IP addresses of Modbus communications
- Which device is the Modbus master (initiating requests)
- Which devices are Modbus slaves (responding)
- What function codes are in use (1 = Read Coils, 3 = Read Holding Registers, 6 = Write Single Register, 16 = Write Multiple Registers)

**Lab Report Item 10:** Complete this OT asset inventory table from passive analysis only:

| IP Address | Role (Master/Slave) | Protocol | Function Codes Observed | Notes |
|------------|---------------------|---------|------------------------|-------|

Also answer: Were any write commands (function codes 6 or 16) observed? What is the security implication of Modbus TCP having no authentication?

---

## Lab Report Submission

Your lab report must include:

- Lab Report Items 1–10 with all screenshots
- All analysis tables completed
- Cloud IAM scenario analysis (Item 9)
- OT asset inventory (Item 10)

**Submission:** Canvas, PDF format, due one week from lab date.

---

## Grading Rubric

| Component | Points |
|-----------|--------|
| REST API BOLA testing (Items 1–3) | 20 |
| JWT vulnerability testing (Items 4–6) | 30 |
| GraphQL testing (Items 7–8) | 20 |
| Cloud IAM analysis (Item 9) | 15 |
| OT passive analysis (Item 10) | 15 |
| **Total** | **100** |
