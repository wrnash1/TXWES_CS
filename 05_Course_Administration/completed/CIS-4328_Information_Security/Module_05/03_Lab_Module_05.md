# Lab Activity — Module 05: Cryptography and PKI Analysis

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Cryptography and Certificate Analysis

**Estimated Completion Time:** 90 minutes

**Submission:** Upload your completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Inspect live TLS certificates and identify their cryptographic properties.

- Evaluate cipher suite configurations for compliance with current security standards.

- Trace the chain of trust from a root CA through an intermediate CA to an end-entity certificate.

- Analyze a certificate for revocation status using OCSP.

- Identify deprecated cryptographic algorithms in realistic scenarios.

---

## Background

In this lab you will act as a security analyst conducting a cryptographic hygiene review. You will inspect real TLS certificates, evaluate cipher suites, and analyze revocation mechanisms. All tools used are free, browser-based, or built into your operating system.

No installation is required. No systems are modified.

---

## Required Tools

All tools are free and accessible via browser:

- SSL Labs Server Test (Qualys): [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)

- Certificate Transparency Log (crt.sh): [https://crt.sh](https://crt.sh)

- OpenSSL (pre-installed on macOS and Linux; Windows users may use Git Bash or WSL)

- Any modern web browser

---

## Part 1 — TLS Certificate Inspection via Browser (20 minutes)

### Part 1 Background

Every HTTPS website presents an X.509 certificate during the TLS handshake. Your browser receives and validates this certificate before displaying the padlock icon.

### Part 1 Tasks

Navigate to [https://www.google.com](https://www.google.com) in your browser.

1. Click the padlock icon in the address bar and navigate to the certificate details. Record the following:
  - Subject (CN field)
  - Issuer (CA name)
  - Validity period (Not Before / Not After)
  - Signature Algorithm
  - Public Key Algorithm and key size
  - Subject Alternative Names (SANs)

2. Navigate to [https://expired.badssl.com](https://expired.badssl.com). What does your browser display? What property of the certificate has failed? Record the specific error message.

3. Navigate to [https://self-signed.badssl.com](https://self-signed.badssl.com). What does your browser display? Why does a self-signed certificate trigger this warning even if the cryptographic algorithms are current? What would need to exist for this certificate to be trusted?

4. Navigate to [https://sha256.badssl.com](https://sha256.badssl.com) and [https://sha1-intermediate.badssl.com](https://sha1-intermediate.badssl.com). Compare the signature algorithms used. Which is acceptable by current standards? What would you recommend for the unacceptable one?

### Part 1 Deliverable

A completed table with the information from task 1, plus written answers (2–4 sentences each) for tasks 2, 3, and 4.

---

## Part 2 — SSL Labs Deep Analysis (25 minutes)

### Part 2 Background

Qualys SSL Labs' Server Test performs a comprehensive analysis of a web server's TLS configuration and produces a letter grade. Security teams use this tool during audits and vendor evaluations.

### Part 2 Tasks

Navigate to [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/) and analyze two sites:

- Site A: `www.txwes.edu`

- Site B: `demo.testfire.net` (a deliberately insecure demo site)

For each site, record and answer the following:

1. What overall grade does SSL Labs assign? What are the primary factors driving the grade?

2. What TLS protocol versions does the server support? Which versions, if any, are deprecated and should be disabled?

3. List the supported cipher suites. Identify any cipher suites that do not provide Perfect Forward Secrecy. Explain what characteristic of the cipher suite indicates whether PFS is provided.

4. Does the server support OCSP Stapling? What is the SSL Labs finding for certificate revocation?

5. What recommendations would you make to the server administrator of Site B to bring it to an acceptable security posture? List at least three specific, actionable changes.

### Part 2 Deliverable

A comparison table for Sites A and B covering grade, TLS versions, PFS status, and OCSP stapling, plus a written recommendation paragraph for Site B.

---

## Part 3 — Chain of Trust Analysis (20 minutes)

### Part 3 Background

Every trusted certificate ultimately chains back to a root CA that is pre-installed in your operating system or browser. Understanding this chain is essential for PKI troubleshooting and for Security+ exam questions about CA hierarchy.

### Part 3 Tasks

1. Visit [https://crt.sh](https://crt.sh) and search for certificates issued to `txwes.edu`. Record:
  - How many active certificates are listed?
  - Who is the issuing CA?
  - What is the certificate's expiration date?

2. For the most recently issued certificate, click through to its details. Identify the full chain of trust: end-entity certificate → intermediate CA → root CA. Record the name of each entity in the chain.

3. Answer the following analysis questions:
  - Why does the root CA not directly sign the end-entity certificate?
  - What would happen to all certificates in the chain if the intermediate CA's private key were compromised?
  - What is the purpose of the "Certificate Transparency" logs that crt.sh aggregates? How does CT help detect fraudulently issued certificates?

### Part 3 Deliverable

A chain-of-trust diagram (hand-drawn or text-format) showing all three levels, plus written answers to the three analysis questions.

---

## Part 4 — Cryptographic Algorithm Scenario Analysis (25 minutes)

### Part 4 Background

Organizations frequently inherit legacy systems with deprecated cryptographic configurations. Identifying and prioritizing these findings is a core security analyst function.

### Part 4 Scenario

You have been asked to review the cryptographic configuration of a financial services company's infrastructure. The following findings have been documented by a junior analyst:

**Finding 1:** The internal document management system uses 3DES with 112-bit keys for encrypting stored files.

**Finding 2:** The customer-facing web portal supports TLS 1.0 and TLS 1.1 in addition to TLS 1.2, to accommodate legacy browser clients.

**Finding 3:** Developer workstations use self-signed certificates for local development HTTPS, and developers have been told to click through certificate warnings.

**Finding 4:** The HR system uses MD5 to hash employee passwords before storage. The system was last updated in 2011.

**Finding 5:** Internal code signing uses SHA-1 for the certificate signature. The code signing certificate expires in 14 months.

### Part 4 Tasks

1. For each finding, identify the specific vulnerability or deprecated component.

2. Assign a priority level (Critical, High, Medium, Low) to each finding and justify your ranking. Consider both the severity of the weakness and the difficulty of exploitation.

3. For each finding, provide a specific remediation recommendation — not just "upgrade the algorithm" but a concrete action the organization should take.

4. Finding 3 involves a behavioral/process issue rather than purely a technical one. Explain why training developers to ignore certificate warnings creates a security risk beyond just the development environment.

### Part 4 Deliverable

A five-row findings table with columns for Finding Number, Vulnerability, Priority, Justification, and Remediation. Plus a written paragraph for task 4.

---

## Lab Submission Checklist

Before submitting, verify:

- Part 1: Completed certificate table and written answers for tasks 2, 3, and 4 (screenshots encouraged).

- Part 2: Comparison table for Sites A and B and recommendation paragraph for Site B.

- Part 3: Chain-of-trust diagram and written answers to three analysis questions.

- Part 4: Five-row findings table and written paragraph for task 4.

---

## Part 9 — Challenge Exercise

### Challenge 1: TLS Configuration Audit Using SSL Labs

Using the SSL Labs SSL Test at <https://www.ssllabs.com/ssltest/>, test two different public HTTPS servers of your choice — select one that you expect to be well-configured (e.g., a major bank or cloud provider) and one that may have legacy configuration issues (e.g., a smaller organization's public site).

1. For each site, record: the overall SSL Labs grade, the TLS protocol versions supported, the cipher suites offered (note any that include RC4, 3DES, or non-PFS suites), the certificate's signature algorithm and key size, and whether OCSP Stapling is enabled.
2. For the lower-rated site, identify at least three specific configuration weaknesses found by SSL Labs. For each weakness, state: the weakness name, the attack or risk it enables, and the specific remediation action required.
3. One of the SSL Labs test categories is "Forward Secrecy." Explain in your own words what Perfect Forward Secrecy guarantees and why its absence means that recording encrypted traffic today could allow decryption in the future if a server's long-term private key is later compromised.
4. SSL Labs reports whether a server is vulnerable to specific historical TLS attacks (POODLE, BEAST, ROBOT, etc.). Look up one of these attacks. Describe the attack mechanism in two to three sentences, identify which TLS protocol version or cipher suite is required for the attack to succeed, and state the remediation.

### Challenge 2: PKI Chain of Trust Analysis and Certificate Revocation

Using only a web browser and publicly available tools, complete the following PKI analysis tasks.

1. Visit any three HTTPS websites and manually inspect the full certificate chain for each (browser padlock → Certificate → Certification Path). For each site, record: the end-entity certificate CN and validity dates, the intermediate CA name and issuing organization, and the root CA name. Identify whether any of the three sites share a common root CA.
2. For one of the three sites, locate the OCSP responder URL (found in the certificate's Authority Information Access extension). Explain in plain language what the OCSP responder does, how OCSP Stapling improves on the basic OCSP model, and what the security risk is if a browser cannot reach the OCSP responder during a connection attempt.
3. A security team discovers that one of their public web server certificates was issued with a 1024-bit RSA key and a SHA-1 signature by an intermediate CA whose certificate has since been revoked. The server certificate itself has not yet expired. Walk through each element of this scenario and explain: why the key size is insufficient, why the SHA-1 signature is a problem, why the revoked intermediate CA invalidates the chain regardless of the end-entity certificate's expiration date, and what the correct remediation sequence is.
4. Research the concept of Certificate Transparency (CT) logs at <https://certificate.transparency.dev/>. Explain what CT logs are, why they exist as a PKI control, how they help detect misissued or fraudulent certificates, and what `expect-ct` header enforcement means for a web server operator.

### Reflection Questions

1. After completing both challenges, explain why an organization that enforces TLS 1.3 only — blocking TLS 1.0, 1.1, and 1.2 — is considered to have a stronger security posture even if TLS 1.2 with strong cipher suites is technically still secure. What specific attack classes does TLS 1.3 eliminate by design, and what does this mean for the concept of defense in depth applied to cryptographic protocol selection?
2. In Challenge 2, you analyzed certificate chain validation. A user notices that a bank website shows a padlock and concludes the site is legitimate and safe. Explain two specific scenarios where the padlock could be present on a malicious or fraudulent site — one involving a domain validation certificate and one involving a compromised intermediate CA — and explain what control (beyond the padlock) a user should check to increase confidence in a site's legitimacy.

---

Module 05 Lab — End
