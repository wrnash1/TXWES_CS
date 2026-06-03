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

Module 05 Lab — End
