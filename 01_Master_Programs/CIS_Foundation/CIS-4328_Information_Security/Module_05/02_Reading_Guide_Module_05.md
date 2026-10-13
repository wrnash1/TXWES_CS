# Reading Guide: Module 05 — Cryptography and PKI

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This reading guide supports Module 05 of CIS-4328. It covers the cryptographic foundations tested on the Security+ exam, including symmetric and asymmetric encryption, hashing algorithms, digital signatures, the TLS handshake, PKI components, and the certificate lifecycle.

All readings use zero-cost, openly licensed resources.

---

## Learning Objectives

By the end of this module, you will be able to:

- Explain the key distribution problem and describe how asymmetric encryption solves it.

- Compare symmetric and asymmetric encryption by speed, key structure, and appropriate use cases.

- Identify AES, RSA, and ECC by their mathematical basis, key size requirements, and exam-relevant properties.

- Describe the properties of a cryptographic hash function and explain why MD5 and SHA-1 are deprecated.

- Trace the steps of a digital signature creation and verification process.

- Describe the TLS handshake and explain why it uses both asymmetric and symmetric cryptography.

- Identify the components of a PKI and explain the role of each.

- Describe the X.509 certificate structure and the three certificate validation levels.

- Explain CRL, OCSP, and OCSP Stapling and their relative advantages.

---

## Primary Readings

### Reading 1 — NIST SP 800-175B Rev. 1: Guideline for Using Cryptographic Standards

Source: [https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final](https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final)

Read: Chapter 2 (Cryptographic Mechanisms Overview) and Chapter 3 (Symmetric Encryption).

Focus areas:

- NIST's current recommendations for symmetric algorithms (AES) and deprecation of DES/3DES.

- The concept of modes of operation and why mode selection matters for security.

- Key length requirements and the relationship between key length and security margin.

### Reading 2 — NIST SP 800-57 Part 1 Rev. 5: Recommendation for Key Management

Source: [https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final)

Read: Section 5.6 (Asymmetric Key Pair Management) and Section 7 (Cryptographic Key Transitions).

Focus areas:

- RSA key size recommendations and the transition away from 1024-bit keys.

- ECC key sizes and their equivalence to RSA key sizes.

- Guidance on algorithm transitions — why organizations must plan migrations away from deprecated algorithms.

### Reading 3 — NIST FIPS 180-4: Secure Hash Standard

Source: [https://csrc.nist.gov/publications/detail/fips/180/4/final](https://csrc.nist.gov/publications/detail/fips/180/4/final)

Read: Section 1 (Purpose and Scope) and the summary of SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.

Focus areas:

- Output sizes for each SHA-2 variant.

- Why SHA-256 is the baseline for current security applications.

- The deprecation status of SHA-1.

---

## Supplemental Readings

### Reading 4 — Mozilla Developer Network: TLS Handshake

Source: [https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security](https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security)

Read: The full article.

Focus areas:

- How cipher suite negotiation works.

- The role of the server certificate in the handshake.

- TLS 1.3 improvements over TLS 1.2.

### Reading 5 — Let's Encrypt: How It Works

Source: [https://letsencrypt.org/how-it-works/](https://letsencrypt.org/how-it-works/)

Read: The full article.

Focus areas:

- The ACME protocol and automated certificate issuance.

- Domain validation in practice.

- The certificate lifecycle as implemented in a real CA.

---

## Concept Reference Tables

### Table 1 — Encryption Algorithm Comparison

| Algorithm | Type | Key Sizes | Mathematical Basis | Primary Use |
|---|---|---|---|---|
| AES-128/192/256 | Symmetric | 128, 192, 256 bits | Substitution-permutation network | Bulk data encryption |
| DES | Symmetric | 56 bits | Feistel network | Deprecated — do not use |
| 3DES | Symmetric | 112/168 bits | Triple DES | Deprecated — do not use |
| RSA | Asymmetric | 2048+ bits | Integer factorization | Key exchange, digital signatures |
| ECC | Asymmetric | 256+ bits | Elliptic curve discrete log | Key exchange, digital signatures (resource-constrained) |
| ECDHE | Asymmetric | 256+ bits | ECC + Diffie-Hellman | Key exchange with Perfect Forward Secrecy |

### Table 2 — Hashing Algorithm Status

| Algorithm | Output Size | Status | Notes |
|---|---|---|---|
| MD5 | 128 bits | Broken | Collision attacks are practical |
| SHA-1 | 160 bits | Deprecated | SHAttered collision attack (2017) |
| SHA-256 | 256 bits | Current standard | SHA-2 family; use as baseline |
| SHA-384 | 384 bits | Current | SHA-2 family; higher security |
| SHA-512 | 512 bits | Current | SHA-2 family; higher security |
| SHA-3 | Variable | Current | Alternative design; Keccak |

### Table 3 — PKI Component Roles

| Component | Role |
|---|---|
| Root CA | Top of trust hierarchy; signs Intermediate CA certificates; kept offline |
| Intermediate CA | Issues end-entity certificates; signed by Root CA |
| Registration Authority (RA) | Verifies applicant identity; approves or rejects CSR |
| Certificate Revocation List (CRL) | Periodic list of revoked certificate serial numbers |
| OCSP Responder | Real-time certificate status query service |
| End-Entity Certificate | The certificate installed on a server, device, or user |

### Table 4 — Certificate Validation Levels

| Level | Validation Performed | Identity Assurance | Common Use |
|---|---|---|---|
| Domain Validation (DV) | Domain control only | Low | General HTTPS |
| Organization Validation (OV) | Domain + legal identity | Medium | Business websites |
| Extended Validation (EV) | Most rigorous vetting | High | Financial, high-trust sites |

---

## Key Terms and Definitions

**Symmetric Encryption** — Encryption that uses the same key for both encryption and decryption.

**Asymmetric Encryption** — Encryption that uses a mathematically linked key pair: one public, one private.

**AES** — Advanced Encryption Standard; current symmetric encryption standard using 128, 192, or 256-bit keys.

**RSA** — Rivest–Shamir–Adleman; asymmetric algorithm based on integer factorization difficulty.

**ECC** — Elliptic Curve Cryptography; asymmetric algorithm providing equivalent security with shorter keys.

**ECDHE** — Elliptic Curve Diffie-Hellman Ephemeral; provides Perfect Forward Secrecy.

**Perfect Forward Secrecy (PFS)** — Property ensuring that compromise of a long-term key does not expose past session keys.

**Hash Function** — A one-way function producing a fixed-size digest from variable-size input.

**SHA-256** — Secure Hash Algorithm with 256-bit output; current hashing standard.

**MD5** — Message Digest 5; cryptographically broken due to practical collision attacks.

**Digital Signature** — A hash of a message encrypted with the sender's private key; provides authentication, integrity, and non-repudiation.

**Non-repudiation** — Inability for a sender to deny having sent a message; provided by digital signatures.

**TLS** — Transport Layer Security; protocol securing HTTPS and other network communication.

**PKI** — Public Key Infrastructure; the system for creating, managing, distributing, and revoking digital certificates.

**Certificate Authority (CA)** — An entity trusted to issue digital certificates.

**Root CA** — The top-level CA in a trust hierarchy; typically kept offline.

**Intermediate CA** — A CA subordinate to the Root CA that issues end-entity certificates.

**Registration Authority (RA)** — Verifies identity of certificate requestors on behalf of the CA.

**X.509** — The standard format for digital certificates.

**CSR** — Certificate Signing Request; a formatted request containing a public key and identity information.

**CRL** — Certificate Revocation List; a periodically published list of revoked certificates.

**OCSP** — Online Certificate Status Protocol; real-time certificate revocation status query.

**OCSP Stapling** — Server-side caching and presentation of a signed OCSP response during the TLS handshake.

**Chain of Trust** — The hierarchical relationship from Root CA through Intermediate CA to end-entity certificate.

---

## Security+ Exam Alignment

The following SY0-701 exam objectives are covered in this module:

- 1.4 — Explain the importance of using appropriate cryptographic solutions.

---

## Critical Thinking Questions

1. A web server is using a certificate with a SHA-1 signature and a 1024-bit RSA key. What specific risks does each of these properties introduce? What should an administrator do, and in what order of priority?

2. An organization's root CA private key is compromised. What is the impact? What steps must the organization take? Why is keeping the root CA offline a primary architectural control against this scenario?

3. A browser displays a padlock icon for a website. A user interprets this as meaning "this website is safe." Is this interpretation correct? What does the padlock actually guarantee, and what does it not guarantee?

4. Your organization's security policy requires Perfect Forward Secrecy for all TLS connections. What specific cipher suite components must be present to satisfy this requirement? What TLS cipher suites do NOT provide PFS?

5. An incident responder discovers that an internal application is using MD5 to hash user passwords stored in a database. Explain why this is a security risk, what specific attacks become practical, and what migration steps are required.

---

## 9. Supplemental Resources

**1. NIST SP 800-175B Rev. 1 — Guideline for Using Cryptographic Standards in the Federal Government**
<https://csrc.nist.gov/publications/detail/sp/800-175b/rev-1/final>
NIST's authoritative guidance on selecting and using approved cryptographic algorithms including AES, SHA-2, RSA, ECC, and ECDHE. Directly supports Module 05 coverage of algorithm selection, key length recommendations, and the deprecation of MD5 and SHA-1.

**2. SSL Labs SSL Test**
<https://www.ssllabs.com/ssltest/>
A free tool for analyzing the TLS configuration of any public HTTPS server. Use it to observe real-world certificate chains, cipher suite negotiations, protocol version support, and Perfect Forward Secrecy configuration — directly reinforcing the Module 05 lab TLS inspection tasks.

**3. RFC 5280 — Internet X.509 Public Key Infrastructure Certificate and CRL Profile**
<https://datatracker.ietf.org/doc/html/rfc5280>
The authoritative specification for X.509 certificate structure, certificate extensions, the chain of trust validation algorithm, and CRL format. Reference Sections 3–4 for PKI architecture concepts and Section 6 for the path validation algorithm that browsers and TLS clients use to verify certificate chains.

---

## Review Checklist

Before taking the Module 05 quiz, verify you can do each of the following without notes:

- State the key size options for AES and the minimum acceptable RSA key size.

- Explain why ECC keys can be shorter than RSA keys for equivalent security.

- Describe the digital signature process in the correct order, identifying which key is used at each step.

- Explain why TLS uses both asymmetric and symmetric cryptography rather than one or the other alone.

- Name the four PKI components and state the role of each in one sentence.

- Distinguish CRL from OCSP and explain OCSP Stapling's purpose.

- State which hashing algorithms are deprecated and why each was deprecated.

---

Module 05 Reading Guide — End
