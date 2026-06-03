# Reading Guide: Module 15 — Specialized Testing Environments

## Course: CIS-4333 Penetration Testing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA PenTest+ (PT0-002)

---

## Overview

This module examines the unique attack surfaces, testing methodologies, tools, and authorization requirements for cloud infrastructure, OT/ICS/SCADA systems, IoT devices, mobile applications, thick clients, and APIs. Specialized environments are increasingly prominent in PT0-002 Domain 3 and represent the most rapidly evolving portion of the penetration testing discipline.

---

## Learning Objectives

After completing this module, students will be able to:

1. Identify cloud-specific attack vectors including IAM misconfigurations and IMDS exploitation.
2. Apply a passive-first testing methodology appropriate for OT/ICS environments.
3. Describe IoT firmware analysis techniques and identify relevant tools.
4. Apply the OWASP Mobile Top 10 to mobile application testing.
5. Identify thick client testing techniques and relevant tools.
6. Apply the OWASP API Security Top 10 to REST and GraphQL API testing.
7. Select appropriate tools for each specialized environment tested.

---

## Section 1: Cloud Penetration Testing

### 1.1 Cloud Service Models and Security Responsibility

The shared responsibility model defines what the customer is responsible for securing versus what the cloud provider secures:

| Layer | IaaS | PaaS | SaaS |
|-------|------|------|------|
| Physical infrastructure | Provider | Provider | Provider |
| Hypervisor | Provider | Provider | Provider |
| OS and runtime | Customer | Provider | Provider |
| Application | Customer | Customer | Provider |
| Data and IAM | Customer | Customer | Customer |

The customer is always responsible for IAM configuration, data classification, and access controls. Cloud security failures typically involve customer-side misconfigurations, not provider-side vulnerabilities.

### 1.2 IAM Misconfiguration Attacks

AWS IAM misconfigurations are the most impactful cloud attack vector. Key patterns:

**Overprivileged roles:** IAM roles or users with `*:*` permissions (all actions on all resources). Any compromise of an identity with this policy gives full account control.

**Public S3 bucket access:** An S3 bucket with `"Principal": "*"` in its policy or an ACL permitting public access exposes all contents without authentication.

**Cross-account trust:** IAM roles with trust policies permitting any AWS account to assume the role can be assumed by an attacker-controlled AWS account.

**Long-lived access keys:** IAM user access keys that have not been rotated persist indefinitely. Exposed in code repositories, environment variables, or configuration files, they provide persistent access.

### 1.3 Instance Metadata Service (IMDS) Attacks

The AWS EC2 Instance Metadata Service (IMDS) is accessible from within an EC2 instance at 169.254.169.254. It provides:

- Instance identity (instance ID, region, AMI)
- IAM role credentials (temporary access key, secret key, session token)
- Network configuration
- User data (often contains credentials passed at launch)

**IMDSv1** (the original version) is accessible by any process on the instance, including web application code executing in response to HTTP requests. A Server-Side Request Forgery (SSRF) vulnerability in a web application can retrieve IAM credentials:

```
GET /?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/[role-name]
```

**IMDSv2** (the mitigated version) requires a session token obtained via a PUT request. SSRF attacks cannot easily forge the PUT request, significantly raising the attack complexity. Organizations should enforce IMDSv2 for all EC2 instances.

### 1.4 Cloud Testing Authorization

**AWS:** Testing is permitted on customer-owned resources. Specific prohibited activities: DDoS simulation, DNS zone walking, port flooding, protocol fuzzing that could affect AWS shared infrastructure.

**Azure:** Customers must agree to the Microsoft Cloud Penetration Testing Rules of Engagement. Pre-notification is no longer required for most testing but the ROE must be followed.

**GCP:** Google permits penetration testing of GCP resources. Customers should follow the GCP guidelines and ensure testing does not affect Google's infrastructure.

For SaaS applications: Testing a SaaS application requires authorization from both the customer (who has authorized the SaaS use) and the SaaS vendor. Customer authorization alone is insufficient.

---

## Section 2: OT/ICS/SCADA Security Assessment

### 2.1 OT Protocol Vulnerabilities

Legacy OT protocols were designed for closed networks before internet connectivity was anticipated:

**Modbus:** TCP/IP variant (Modbus TCP, port 502). No authentication, no encryption. Any device on the network can send commands to any Modbus device. Widely used in manufacturing and utilities.

**DNP3 (Distributed Network Protocol):** Used in utilities (electric, water, oil and gas). No authentication in the base protocol (Secure Authentication version 5 exists but is not universally deployed).

**BACnet:** Building automation. No authentication by default. BACnet Discovery enables enumeration of all devices on a network.

**Profibus/Profinet:** Industrial Ethernet. No built-in security.

**EtherNet/IP:** Ethernet-based industrial protocol. Partial security features in newer versions.

### 2.2 ICS Security Assessment Methodology

The ICS security assessment follows a fundamentally different approach than IT penetration testing:

**Phase 1 — Documentation Review:** Network diagrams, system inventory, vendor documentation, incident history. Understanding the environment before any active assessment.

**Phase 2 — Passive Network Analysis:** Deploy a network tap or SPAN port. Capture traffic without generating any probes. Use tools like Wireshark, Nozomi Networks, Dragos, or Claroty to analyze captured traffic, identify devices, and build an asset inventory.

**Phase 3 — Architecture Assessment:** Evaluate IT/OT network segmentation, boundary controls, remote access configurations, and authentication controls. This is primarily a documentation and interview exercise.

**Phase 4 — Vulnerability Identification:** Match identified assets to the ICS-CERT vulnerability database (https://www.cisa.gov/ics-advisories) and vendor security advisories. Do not run vulnerability scanners against live OT equipment.

**Phase 5 — Limited Active Testing (test environment only):** Any active exploitation testing must be performed in an isolated test environment, never against live operational systems. This typically requires the vendor to provide test hardware.

### 2.3 IT/OT Convergence Risks

Most modern OT environments are not truly air-gapped. Common connection points:

- Remote monitoring via corporate VPN
- Vendor remote maintenance connections
- Historian servers with both IT and OT connections
- Jump servers bridging IT and OT networks

These connections are the primary attack paths from IT to OT. Assessing these boundaries is a key component of ICS security assessment.

---

## Section 3: IoT Security Assessment

### 3.1 OWASP IoT Top 10

OWASP maintains an IoT-specific threat list. Key items:

1. Weak, guessable, or hardcoded passwords
2. Insecure network services
3. Insecure ecosystem interfaces (web, API, cloud, mobile)
4. Lack of a secure update mechanism
5. Use of insecure or outdated components
6. Insufficient privacy protection
7. Insecure data transfer and storage
8. Lack of device management
9. Insecure default settings
10. Lack of physical hardening

### 3.2 Firmware Analysis

Firmware is the software running on embedded IoT devices. Extracting and analyzing firmware reveals hardcoded credentials, encryption keys, and exploitable vulnerabilities.

**Extraction methods:**

- Downloading from vendor website (easiest — many vendors publish firmware for updates)
- Firmware update interception (capture the update traffic during an authorized update)
- Physical extraction via UART/JTAG/SPI interfaces on the PCB

**Static analysis with Binwalk:**

```bash
binwalk -e firmware.bin    # Extract filesystem from firmware image
```

Binwalk identifies and extracts compressed filesystems, kernel images, and other components.

**Sensitive data identification:**

```bash
firmwalker.sh ./firmware_extracted_path    # Searches for passwords, keys, scripts
```

Look for: `/etc/shadow` or `/etc/passwd` equivalents, private keys (`*.pem`, `*.key`), hardcoded credentials in configuration files, and debug/development interfaces.

### 3.3 Dynamic Analysis with Frida

Frida is a dynamic instrumentation framework for running processes on mobile and IoT platforms. It allows:

- Hooking function calls to observe arguments and return values
- Bypassing authentication checks (override return value of authentication function)
- Extracting keys from memory during cryptographic operations
- Modifying application behavior at runtime

Basic Frida usage (mobile/IoT):

```bash
frida-ps -U              # List processes on USB-connected device
frida -U -n TargetApp    # Attach to running application
```

---

## Section 4: Mobile Application Testing

### 4.1 Android Application Analysis

**APK structure:** Android applications are ZIP archives. Extracting the APK reveals:

- `classes.dex` — compiled Java/Kotlin bytecode
- `AndroidManifest.xml` — application metadata, permissions, exported activities
- `res/` — resources including strings (may contain hardcoded values)
- `assets/` — arbitrary files bundled with the app
- `lib/` — native libraries

**Decompilation with Jadx:**

```bash
jadx -d output_dir target.apk    # Decompile APK to Java source
```

Review decompiled code for: hardcoded API keys, hardcoded credentials, insecure algorithms, debug code left in release builds.

**AndroidManifest.xml review:** Exported activities with no permissions (`android:exported="true"` with no `android:permission`) can be launched by any application — a potential attack vector.

### 4.2 iOS Application Analysis

iOS applications use the IPA format. Analysis requires either:

- Extracting the IPA from a non-encrypted backup
- Decrypting the app binary from memory on a jailbroken device using tools like `bfdecrypt` or `frida-ios-dump`

**Binary analysis:** iOS binaries are typically ARM64 Mach-O format. Use Ghidra, IDA Pro, or Hopper to decompile.

**Keychain analysis (jailbroken device):** The iOS Keychain should store credentials securely, but misconfigured keychain items may be accessible to other applications. Use `objection` to dump keychain contents:

```bash
objection -g "App Name" explore
ios keychain dump
```

### 4.3 Certificate Pinning Bypass

Many security-conscious mobile applications implement certificate pinning — the app only accepts TLS connections from a specific certificate or CA, blocking proxy interception.

Bypass techniques:

- **Frida scripts:** Hook the certificate validation function and override the return value to accept any certificate.
- **Objection:** `android sslpinning disable` or `ios sslpinning disable` automates common pinning bypass patterns.
- **Patching the APK:** Modify the `network_security_config.xml` or specific pinning code in the decompiled APK, recompile, resign, and reinstall.

---

## Section 5: API Security Testing

### 5.1 REST API Testing Methodology

A systematic REST API testing approach follows these steps:

**Discovery:** Identify all API endpoints. Sources: JavaScript files (reverse engineer front-end), developer documentation, API documentation URLs (/api/docs, /swagger, /openapi.json), and fuzzing known endpoint name patterns.

**Authentication review:** Test authentication mechanisms — Bearer tokens, API keys, OAuth flows. Test for missing authentication on sensitive endpoints.

**Authorization testing:** Test BOLA (Broken Object Level Authorization) by substituting other users' object IDs in API parameters. Test BFLA (Broken Function Level Authorization) by accessing admin or elevated functions as a low-privilege user.

**Input validation:** Test for SQL injection, command injection, and template injection in API parameters.

**Business logic:** Identify flows that can be abused — rate limit bypasses, price manipulation, quantity manipulation.

### 5.2 JWT Security Testing

JSON Web Tokens (JWTs) are widely used for API authentication. Common JWT vulnerabilities:

**Algorithm confusion (alg:none):** Some implementations accept a JWT with `alg: "none"` and no signature, bypassing verification entirely.

**Algorithm substitution (RS256 → HS256):** If the server uses RS256 (asymmetric), an attacker can forge a token by switching to HS256 and signing with the server's public key (which is known).

**Weak secret:** HS256-signed JWTs with a weak secret key can be brute-forced.

**Claim manipulation:** Modify claims (exp, role, user_id) in the JWT payload. If the signature is not verified, modified tokens are accepted.

Testing tools: jwt.io for manual decoding and modification, jwt_tool for automated vulnerability testing, Burp Suite JWT Editor extension.

### 5.3 GraphQL Testing

GraphQL APIs present a distinct testing surface from REST:

**Introspection:** By default, GraphQL APIs expose schema introspection, revealing all types, queries, mutations, and fields. Use `graphql-voyager` to visualize the schema.

**Introspection query:**

```graphql
{ __schema { types { name } } }
```

**Batching attacks:** GraphQL supports batching multiple queries in a single request, enabling rate limit bypass.

**IDOR in GraphQL:** Substitute IDs in queries to access other users' data — the same BOLA vulnerability as in REST APIs.

**Injection:** GraphQL resolvers may pass arguments to backend databases. Test for SQL injection and NoSQL injection in query arguments.

---

## Section 6: PT0-002 Exam Alignment

### 6.1 Cloud Attack Scenarios

Exam patterns for cloud testing:

"A tester discovers an SSRF vulnerability in a web application hosted on an EC2 instance. What additional attack is directly enabled by this vulnerability?" — Reaching the IMDS at 169.254.169.254 to retrieve IAM role credentials.

"Which tool is specifically designed for AWS exploitation framework functionality?" — Pacu.

### 6.2 OT/ICS Safety Approach

"During an ICS assessment, the tester wants to identify all devices on the manufacturing floor network. Which approach is MOST appropriate?" — Passive traffic capture (NOT active scanning).

### 6.3 API Security

"Which OWASP API vulnerability category describes accessing another user's order by changing the order ID in the API request?" — API1:2023 — Broken Object Level Authorization (BOLA).

---

## Key Terms

**IaaS:** Infrastructure as a Service — customer manages OS and above.

**IMDS:** Instance Metadata Service — AWS service at 169.254.169.254 providing instance metadata including IAM credentials.

**BOLA:** Broken Object Level Authorization — API vulnerability where object identifiers can be manipulated to access other users' data.

**BFLA:** Broken Function Level Authorization — API vulnerability where privileged functions are accessible to lower-privilege users.

**Purdue Model:** Reference architecture for industrial control system network segmentation.

**ScoutSuite:** Open-source multi-cloud security auditing tool.

**Pacu:** AWS exploitation framework.

**Frida:** Dynamic instrumentation toolkit for mobile and embedded device testing.

**MobSF:** Mobile Security Framework — automated static and dynamic mobile application analysis.

**Binwalk:** Firmware extraction and analysis tool.

**JWT:** JSON Web Token — compact token format used for API authentication.

---

## Review Questions

1. Explain the IMDS attack path: starting from an SSRF vulnerability in a web application on EC2, describe each step to obtain AWS IAM credentials.

2. Why does OT security assessment require a passive-first methodology, and what types of active testing are performed only in test environments?

3. What is certificate pinning in mobile applications, and what are two techniques used to bypass it in authorized testing?

4. Describe the algorithm confusion attack against JWT tokens (RS256 to HS256). What condition must exist for this attack to succeed?

5. Compare BOLA and BFLA in the context of API security. Give a specific HTTP request example illustrating each.

---

## References

- CompTIA PenTest+ PT0-002 Exam Objectives, Domain 3.7, 3.8
- OWASP API Security Top 10: https://owasp.org/API-Security/
- OWASP Mobile Top 10: https://owasp.org/www-project-mobile-top-10/
- OWASP IoT Top 10: https://owasp.org/www-project-internet-of-things/
- AWS Penetration Testing Policy: https://aws.amazon.com/security/penetration-testing/
- CISA ICS Security Advisories: https://www.cisa.gov/ics-advisories
- Pacu Framework: https://github.com/RhinoSecurityLabs/pacu
- ScoutSuite: https://github.com/nccgroup/ScoutSuite
