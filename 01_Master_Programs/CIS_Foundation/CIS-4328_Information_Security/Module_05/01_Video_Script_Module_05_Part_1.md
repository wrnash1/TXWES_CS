# Video Script: Module 05 — Cryptography and PKI (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Module 05, Part 1. I'm Professor Nash.

Cryptography is the mathematical foundation of virtually every security control we rely on. TLS certificates, VPNs, digital signatures, password hashing, secure email — all of it comes back to the concepts in this module. Domain 1 of the Security+ exam — "General Security Concepts" — includes cryptography, and it appears throughout other domains as well.

In Part 1 we cover the conceptual and theoretical foundations: symmetric versus asymmetric encryption, the major algorithms you must know, hashing, and digital signatures. In Part 2 we apply these to TLS, PKI, the certificate lifecycle, and the exam traps.

Let's start with the core problem cryptography solves.

---

### [SECTION 1 — The Core Problem — 1:00]

When Alice wants to send Bob a confidential message over an untrusted network — the internet — three problems must be solved:

- **Confidentiality** — Only Bob can read the message.

- **Integrity** — The message was not altered in transit.

- **Authentication** — The message actually came from Alice.

Cryptography provides the mathematical tools to solve all three. Different mechanisms address different problems, which is why modern security protocols combine multiple cryptographic primitives.

---

### [SECTION 2 — Symmetric Encryption — 2:00]

Symmetric encryption uses the **same key for both encryption and decryption**. It is fast and computationally efficient, making it suitable for encrypting large amounts of data.

#### AES — Advanced Encryption Standard

AES is the current standard for symmetric encryption. You must know these specifics for the exam:

- Block cipher operating on 128-bit blocks.

- Key sizes: **128, 192, or 256 bits**.

- AES-256 is considered quantum-resistant for the foreseeable future.

- Modes of operation include CBC (Cipher Block Chaining) and GCM (Galois/Counter Mode). GCM provides both encryption and integrity verification (authenticated encryption).

AES replaced DES (Data Encryption Standard) and 3DES. Both DES and 3DES are now deprecated. The exam expects you to know that DES uses a 56-bit key (too short), and 3DES applies DES three times (slow and increasingly deprecated).

#### The Key Distribution Problem

Symmetric encryption's critical weakness: **how do Alice and Bob securely share the key in the first place?** If they can already communicate securely, why do they need the cipher?

This is called the **key distribution problem**, and it is the reason asymmetric encryption exists.

---

### [SECTION 3 — Asymmetric Encryption — 4:30]

Asymmetric encryption uses a **mathematically linked key pair**: a public key and a private key.

The fundamental rules:

- What the public key encrypts, only the private key can decrypt.

- What the private key signs, the public key can verify.

The public key can be shared with anyone. The private key is never shared.

This solves the key distribution problem: Alice can encrypt a message using Bob's public key. Only Bob — who holds the private key — can decrypt it.

#### RSA — Rivest–Shamir–Adleman

RSA is the most widely deployed asymmetric algorithm. Key facts for the exam:

- Security is based on the mathematical difficulty of **factoring large prime numbers**.

- Common key sizes: **2048 bits** (minimum current standard), **4096 bits** (higher security).

- RSA 1024-bit keys are considered broken and are no longer acceptable.

- RSA is computationally expensive — it is used to encrypt small data (like a symmetric session key), not large files directly.

- RSA supports both encryption and digital signatures.

#### ECC — Elliptic Curve Cryptography

ECC provides equivalent security to RSA with **much smaller key sizes**, making it preferred for resource-constrained environments: mobile devices, IoT, embedded systems, and TLS in modern browsers.

Key facts:

- Security is based on the difficulty of the **elliptic curve discrete logarithm problem**.

- A 256-bit ECC key provides approximately the same security as a 3072-bit RSA key.

- Common ECC algorithms include **ECDSA** (Elliptic Curve Digital Signature Algorithm) and **ECDH** (Elliptic Curve Diffie-Hellman).

**Exam trap**: ECC is not "weaker" than RSA because the key is shorter. Shorter key = same strength due to a different mathematical problem. This distinction is tested.

#### Diffie-Hellman Key Exchange

Diffie-Hellman (DH) solves the key distribution problem differently: two parties each generate a key pair and exchange public values. Through a mathematical operation, both parties independently arrive at the **same shared secret** without ever transmitting it.

**Perfect Forward Secrecy (PFS)**: Ephemeral Diffie-Hellman (DHE or ECDHE) generates a new key pair for each session. Even if a server's private key is later compromised, past session keys cannot be recovered. The exam tests PFS as a property of ECDHE, not of static RSA.

---

### [SECTION 4 — Hashing — 8:30]

A **hash function** takes an input of any size and produces a fixed-size output called a **digest** or **hash value**.

Properties of a cryptographic hash function:

- **Deterministic** — the same input always produces the same hash.

- **One-way** — given the hash, you cannot derive the original input.

- **Collision-resistant** — it should be computationally infeasible to find two different inputs that produce the same hash.

- **Avalanche effect** — a small change in input produces a dramatically different hash.

Hashing provides **integrity verification**, not encryption. If you hash a file before sending it and the recipient hashes it after receiving it, matching hashes confirm the file was not altered.

#### SHA-256

SHA-256 (Secure Hash Algorithm, 256-bit output) is the current standard for general-purpose cryptographic hashing.

- Part of the SHA-2 family.

- 256-bit output.

- Used in TLS certificates, code signing, blockchain, file integrity verification.

- SHA-384 and SHA-512 are available for higher-security applications.

#### MD5 — Broken

MD5 (Message Digest 5) produces a 128-bit hash. It was widely used but is now **cryptographically broken** — collision attacks are practical, meaning an attacker can create two different files with the same MD5 hash.

**Exam rule**: If a scenario involves MD5 in a security context, the correct answer almost always involves replacing it with SHA-256 or better. MD5 is still used for non-security purposes (checksums for detecting accidental corruption), but it must never be used where collision resistance matters.

#### SHA-1 — Also Deprecated

SHA-1 (160-bit output) was deprecated following successful collision attacks (Google's SHAttered attack, 2017). The exam expects you to know SHA-1 is no longer acceptable for security purposes. Most certificate authorities stopped issuing SHA-1 certificates years ago.

---

### [SECTION 5 — Digital Signatures — 12:00]

A digital signature combines asymmetric cryptography and hashing to provide **authentication and integrity** simultaneously.

The process:

1. Alice hashes the message to produce a digest.

2. Alice encrypts the digest with her **private key** — this is the signature.

3. Alice sends the message and signature to Bob.

4. Bob decrypts the signature using Alice's **public key** to recover the digest.

5. Bob hashes the received message independently.

6. If the two digests match, the message is authentic and unaltered.

This proves two things:

- **Authenticity** — only Alice could have created the signature (only she has her private key).

- **Integrity** — the message was not altered after signing.

**What a digital signature does NOT provide**: Confidentiality. Anyone can read the message. For confidentiality, encryption is needed separately.

**Exam trap**: "Non-repudiation" is a property provided by digital signatures. Non-repudiation means the sender cannot later deny having sent the message — the signature is proof. Questions testing non-repudiation almost always point to digital signatures as the answer.

---

### [OUTRO — 15:00]

Part 1 has given you the cryptographic primitives:

- Symmetric encryption (AES) — fast, same key both directions.

- Asymmetric encryption (RSA, ECC) — key pair, solves key distribution.

- Hashing (SHA-256, broken MD5) — one-way, integrity only.

- Digital signatures — hash plus asymmetric, authentication plus integrity plus non-repudiation.

In Part 2 we apply these to the TLS handshake, PKI, certificate lifecycle, and the specific Security+ exam traps in this domain.

See you in Part 2.

---

End of Part 1 — Module 05
