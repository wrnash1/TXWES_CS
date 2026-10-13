# Video Script: Module 05 — Cryptography and PKI (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Part 2 of Module 05. In Part 1 we built the cryptographic primitives — symmetric, asymmetric, hashing, and digital signatures. Now we see how those primitives combine in the real-world systems the Security+ exam tests: TLS, PKI, the certificate lifecycle, and X.509.

We will also work through the exam traps specific to cryptography — this domain has more vocabulary-based traps than almost any other.

---

### [SECTION 1 — The TLS Handshake — 0:30]

TLS (Transport Layer Security) is the protocol that secures HTTPS connections. Every time you see a padlock in a browser, TLS is running. Understanding the handshake tells you exactly how symmetric and asymmetric cryptography work together.

The TLS 1.3 handshake (simplified):

1. **Client Hello** — Client sends supported cipher suites and a random value.

2. **Server Hello** — Server selects a cipher suite, sends its certificate, and a random value.

3. **Key Exchange** — Both parties use Diffie-Hellman (ECDHE in TLS 1.3) to derive a shared session key. The server's certificate is authenticated during this step.

4. **Session Keys Derived** — Both parties independently compute identical symmetric session keys.

5. **Encrypted Communication Begins** — All further communication uses AES (or another agreed symmetric cipher) with the session key.

**Why this design?**

Asymmetric cryptography (the certificate / ECDHE) solves the key distribution problem and provides authentication. Symmetric cryptography (AES session key) handles the bulk data because it is fast. Each session gets a fresh key pair (ephemeral), providing Perfect Forward Secrecy.

**Exam points:**

- TLS 1.0 and 1.1 are deprecated. The exam expects you to recommend TLS 1.2 as minimum, TLS 1.3 as preferred.

- SSL is entirely deprecated. Any exam scenario using SSL should be flagged as insecure.

- The certificate in the TLS handshake authenticates the **server** to the client. Mutual TLS (mTLS) authenticates both parties.

---

### [SECTION 2 — PKI Architecture — 3:30]

**Public Key Infrastructure (PKI)** is the framework of policies, procedures, hardware, software, and people that create, manage, distribute, store, and revoke digital certificates.

#### Certificate Authority (CA)

A CA is an entity trusted to issue digital certificates. When you see a padlock on a bank's website, you trust it because the certificate was issued by a CA your operating system and browser already trust.

**Root CA** — The top of the trust hierarchy. Root CAs are extremely sensitive; they are kept offline in air-gapped facilities (offline root CA). Root certificates are pre-installed in operating systems and browsers.

**Intermediate CA (Subordinate CA)** — Issues certificates on behalf of the Root CA. The Root CA signs the Intermediate CA's certificate, creating a **chain of trust**. Using intermediates means the Root CA stays offline.

**Exam point**: If the root CA is compromised, the entire PKI is compromised. This is why root CAs are kept offline.

#### Registration Authority (RA)

The RA handles the verification of identity for certificate requests. It collects and validates applicant information, then passes the approved request to the CA for signing. The RA does not issue certificates — that is the CA's role.

**Exam trap**: RA verifies identity; CA issues the certificate. These are distinct roles.

#### Certificate Revocation

Certificates can be revoked before expiration if the private key is compromised, if the organization changes, or if the certificate was issued fraudulently.

Two revocation mechanisms:

- **CRL (Certificate Revocation List)** — A periodically published list of revoked certificate serial numbers. Clients download the CRL and check it. Weakness: CRLs can be large and are only updated periodically, leaving a window where a revoked certificate appears valid.

- **OCSP (Online Certificate Status Protocol)** — Real-time per-certificate query to an OCSP responder. Returns "good," "revoked," or "unknown." Faster and more current than CRL.

- **OCSP Stapling** — The server pre-fetches and caches a signed OCSP response and presents it during the TLS handshake, reducing latency and load on OCSP responders.

**Exam order**: CRL came first (older, batch, larger); OCSP came after (newer, real-time, per-certificate); OCSP Stapling is the optimization.

---

### [SECTION 3 — X.509 Certificate Structure — 7:30]

An X.509 certificate is the standard format for digital certificates. Every TLS certificate, code signing certificate, and email S/MIME certificate uses X.509.

Key fields in an X.509 certificate:

- **Subject** — Who the certificate was issued to (e.g., `CN=www.example.com, O=Example Corp`).

- **Issuer** — Which CA issued the certificate.

- **Serial Number** — Unique identifier for this certificate within the issuing CA.

- **Validity Period** — `Not Before` and `Not After` dates.

- **Public Key** — The subject's public key.

- **Subject Alternative Names (SANs)** — Additional domain names or IP addresses the certificate covers. Modern certificates use SANs; the CN field alone is no longer sufficient.

- **Signature Algorithm** — The algorithm used to sign the certificate (e.g., SHA-256 with RSA).

- **CA Signature** — The CA's digital signature over the certificate contents.

**Exam point**: A wildcard certificate (`*.example.com`) covers any single-level subdomain of example.com. It does not cover `sub.sub.example.com` — that requires two wildcard levels or a SAN.

#### Certificate Types by Validation Level

- **Domain Validation (DV)** — CA verifies the applicant controls the domain. Fast and automated. Provides encryption but no identity assurance beyond domain control.

- **Organization Validation (OV)** — CA verifies the domain and the organization's legal identity. More thorough.

- **Extended Validation (EV)** — Most rigorous vetting. Previously showed a green bar in browsers; now displays organization name in certificate details.

**Exam point**: DV, OV, and EV all provide the same encryption strength. They differ only in identity assurance.

---

### [SECTION 4 — Certificate Lifecycle — 10:00]

A certificate goes through these phases:

1. **Key Generation** — The entity generates a key pair.

2. **Certificate Signing Request (CSR)** — A formatted request containing the entity's public key and identity information, signed with the entity's private key to prove key ownership.

3. **Validation** — The RA verifies the CSR and identity.

4. **Issuance** — The CA signs the certificate.

5. **Deployment** — Certificate installed on the server or device.

6. **Renewal** — Certificates have expiration dates; renewal happens before expiration.

7. **Revocation** — Certificate invalidated early if the private key is compromised or circumstances change.

**Exam point**: Expired certificates are a common compliance finding. Certificate management automation (tools like Let's Encrypt with ACME protocol) reduces the risk of unintentional expiration.

---

### [SECTION 5 — EXAM TRAPS AND QUESTION ANALYSIS — 11:45]

Let's work through the cryptography traps that consistently appear on Security+.

#### Trap 1: Confidentiality vs. Authentication Direction

"Alice signs a document." Which key does she use?

Wrong answer: public key.

Correct answer: **private key**. Signing uses the private key. Verification uses the public key.

"Alice encrypts a message for Bob." Which key does she use?

Wrong answer: her own public key.

Correct answer: **Bob's public key**. She encrypts with the recipient's public key; only Bob's private key decrypts it.

#### Trap 2: What Hashing Provides

"A network administrator sends a configuration file to a remote site and wants to ensure it was not modified in transit."

Wrong answers: encryption, digital certificate, VPN.

Correct answer: **hashing** (or a hash with the file). Hashing provides integrity. If the question adds "and prove who sent it," then a digital signature is needed.

#### Trap 3: MD5 in a Security Context

Any exam question that asks "which algorithm should NOT be used for certificate signing?" or "which hash is no longer considered secure?" — MD5 and SHA-1 are the correct answers.

If a scenario describes a system using MD5 for password hashing, the correct recommendation is migration to a modern algorithm with salting (bcrypt, Argon2, or at minimum SHA-256 with per-user salt).

#### Trap 4: Symmetric vs. Asymmetric Speed

"A company needs to encrypt 2 TB of data at rest."

Wrong answer: RSA encryption.

Correct answer: **AES** (symmetric). RSA is computationally expensive and not designed for bulk data. Symmetric encryption handles large data. Asymmetric handles key exchange.

#### Trap 5: Perfect Forward Secrecy

"Which feature ensures that a compromise of the server's long-term private key does not expose past session traffic?"

Wrong answer: TLS 1.2, RSA key exchange.

Correct answer: **Perfect Forward Secrecy using ECDHE**. Static RSA key exchange uses the same private key for every session — if that key is compromised later, all past sessions can be decrypted. ECDHE generates ephemeral keys per session.

#### Trap 6: Root CA vs. Intermediate CA

"An organization wants to issue certificates from their internal CA but keep the root CA offline."

The structure: **Root CA (offline) signs Intermediate CA certificate → Intermediate CA issues end-entity certificates**.

"Which component verifies the identity of certificate requestors before the CA issues the certificate?"

Answer: **Registration Authority (RA)**, not the CA itself.

---

### [OUTRO — 15:00]

Cryptography rewards precise vocabulary. The exam does not ask you to perform the math — it asks you to know which algorithm does what, what properties each provides, and what breaks or is deprecated.

Key review summary:

- AES: symmetric, fast, bulk data.

- RSA: asymmetric, key pair, factoring problem.

- ECC: asymmetric, smaller keys, discrete log problem.

- SHA-256: hashing, integrity, one-way.

- MD5 and SHA-1: broken, do not use for security.

- Digital signatures: private key signs, public key verifies, provides authentication and non-repudiation.

- TLS: asymmetric for key exchange, symmetric for session data.

- PKI: Root CA → Intermediate CA → end-entity certificate → chain of trust.

- Revocation: CRL (periodic list) vs. OCSP (real-time query) vs. OCSP Stapling (cached response).

Complete the Module 05 quiz and lab before moving to Module 06 — Identity and Access Management.

---

End of Part 2 — Module 05
