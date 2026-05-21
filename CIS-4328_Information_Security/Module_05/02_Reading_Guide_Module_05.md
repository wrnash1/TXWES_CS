# Reading Guide: Module 05 - Cryptography Fundamentals
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 05 – Cryptography Fundamentals**! Cryptography underpins nearly every security control in modern IT — TLS, VPNs, digital signatures, password storage, and more. SY0-701 tests cryptography concepts in both direct definition questions and applied scenario questions where you must select the right algorithm or key type for a given security requirement.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Symmetric Encryption**: A cryptographic method that uses a single shared secret key for both encryption and decryption. It is fast and efficient for bulk data encryption but requires secure key distribution. Common algorithms include AES (current standard), 3DES (legacy), and RC4 (deprecated/broken). SY0-701 expects you to know AES key sizes: 128, 192, and 256 bits.
*   **Asymmetric Encryption**: A cryptographic method that uses a mathematically linked key pair — a public key (freely shared) and a private key (kept secret). Encrypting with the public key ensures only the private key holder can decrypt (confidentiality). Signing with the private key allows anyone with the public key to verify authenticity (non-repudiation). RSA, ECC, and Diffie-Hellman are the primary asymmetric algorithms on SY0-701.
*   **Hashing**: A one-way mathematical function that produces a fixed-length digest (hash value) from any input. Because it is irreversible, hashing is used to verify data integrity rather than to encrypt it. Common algorithms: SHA-256 (current standard), SHA-1 (deprecated), MD5 (broken — do not use for security). If two different inputs produce the same hash, it is called a collision — a property that breaks integrity guarantees.
*   **Digital Signatures**: Created by hashing a document and encrypting that hash with the sender's private key. The recipient verifies by decrypting the hash with the sender's public key and re-hashing the document — if they match, the signature is valid. Digital signatures prove both integrity (the document was not altered) and non-repudiation (the sender cannot deny signing it).
*   **Diffie-Hellman Key Exchange**: A protocol that allows two parties to independently derive the same shared secret over an insecure channel without ever transmitting the secret itself. It is the foundation of Perfect Forward Secrecy (PFS) in TLS. DHE (ephemeral) and ECDHE are the current preferred variants because they generate a new key pair per session.
*   **Elliptic Curve Cryptography (ECC)**: An asymmetric algorithm that achieves equivalent security to RSA with much shorter key lengths. A 256-bit ECC key provides roughly the same security as a 3072-bit RSA key. ECC is preferred for mobile and IoT environments where computational resources are limited.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Cryptography falls under **Domain 1 – General Security Concepts (12%)** and appears throughout **Domain 2** and **Domain 3** of SY0-701. Expect 8–12 questions referencing cryptographic controls.
*   **Symmetric vs. Asymmetric Speed Trap:** Symmetric is fast (used for bulk data); asymmetric is slow (used for key exchange and signatures). TLS uses asymmetric cryptography to exchange a symmetric session key — then switches to symmetric for data transfer. Know this hybrid model.
*   **Hashing ≠ Encryption:** A critical exam distinction. You cannot "decrypt" a hash. If a question describes reversing a hash, that is a red flag — hashing is one-way. Only encryption is reversible with a key.
*   **Key Length vs. Algorithm:** For SY0-701, memorize these minimums: RSA ≥ 2048 bits, AES ≥ 128 bits (256 preferred), ECC ≥ 256 bits. The exam tests whether you can identify a configuration as adequately or inadequately keyed.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include side-by-side comparison tables for symmetric vs. asymmetric algorithms and hash function properties that are ideal for exam review.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Cryptography" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Pay particular attention to the algorithm comparison tables and key exchange diagrams.
*   **Required Video:** Watch the cryptography video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos walk through how TLS combines symmetric and asymmetric cryptography in a real handshake.

---

### Lab & Command Integration
In this week's hands-on lab, you will use OpenSSL command-line tools to generate key pairs, create hashes, and inspect certificates. These tasks directly mirror SY0-701 performance-based questions that ask you to identify certificate properties or select the correct cryptographic operation.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to explain when to use each algorithm type and why.
- [ ] Read the "Cryptography" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the cryptography video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: symmetric = speed + shared key; asymmetric = key pairs + non-repudiation; hashing = one-way + integrity only.
- [ ] Proceed to the weekly hands-on lab activity.
