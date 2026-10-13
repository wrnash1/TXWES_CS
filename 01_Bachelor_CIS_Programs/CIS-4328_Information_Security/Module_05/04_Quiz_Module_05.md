# Quiz: Module 05 — Cryptography and PKI

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

A company needs to encrypt a 500 GB database backup stored on tape. Which algorithm is MOST appropriate for this use case?

A. RSA-2048

B. ECC-256

C. AES-256

D. SHA-256

**Correct Answer:** C

**Explanation:** AES is a symmetric cipher designed for bulk data encryption. It is fast and computationally efficient, making it appropriate for large datasets. RSA and ECC are asymmetric algorithms — they are computationally expensive and not designed for bulk encryption. SHA-256 is a hash function, not an encryption algorithm, and cannot be used for encryption.

---

### Question 2

An analyst reviewing TLS configurations discovers that a web server is configured to use RSA key exchange rather than ECDHE for establishing session keys. Which security property is ABSENT from sessions established with RSA key exchange?

A. Confidentiality

B. Integrity

C. Perfect Forward Secrecy

D. Authentication

**Correct Answer:** C

**Explanation:** RSA key exchange uses the server's long-term private key to protect the session key. If that private key is later compromised, all previously recorded sessions can be decrypted. ECDHE generates ephemeral key pairs per session, ensuring that past sessions remain protected even if the long-term key is later compromised — this property is Perfect Forward Secrecy. Confidentiality, integrity, and authentication are all present in both configurations.

---

### Question 3

A user receives a digitally signed email from a colleague. The signature verification succeeds. What two security properties does this confirmation provide?

A. Confidentiality and availability

B. Authentication and non-repudiation

C. Integrity and confidentiality

D. Non-repudiation and availability

**Correct Answer:** B

**Explanation:** A digital signature is created using the sender's private key applied to a hash of the message. Successful verification proves that only the holder of the private key could have created the signature (authentication) and that the sender cannot later deny having sent it (non-repudiation). A digital signature does not encrypt the message, so it provides no confidentiality. Integrity is also provided, but the question asks for the two properties most directly associated with signatures, and non-repudiation is the distinguishing characteristic.

---

### Question 4

Which of the following accurately describes the relationship between a Root CA and an Intermediate CA in a PKI hierarchy?

A. The Root CA issues end-entity certificates; the Intermediate CA handles revocation.

B. The Root CA signs the Intermediate CA's certificate; the Intermediate CA issues end-entity certificates.

C. The Intermediate CA signs the Root CA's certificate to establish mutual trust.

D. Both CAs can issue end-entity certificates independently of each other.

**Correct Answer:** B

**Explanation:** In a standard PKI hierarchy, the Root CA is kept offline and signs the Intermediate CA's certificate, establishing a chain of trust. The Intermediate CA then issues end-entity (server, user, device) certificates. This design keeps the Root CA offline and isolated — if an Intermediate CA is compromised, the Root CA can revoke it and issue a new one without invalidating the entire PKI.

---

### Question 5

A security analyst discovers that a server's TLS certificate uses a SHA-1 signature. What is the PRIMARY security concern?

A. SHA-1 produces a digest that is too short to provide confidentiality.

B. SHA-1 collisions have been demonstrated, meaning an attacker could forge a certificate with the same hash.

C. SHA-1 is a symmetric algorithm and should not be used in certificates.

D. SHA-1 key sizes are too small for modern encryption requirements.

**Correct Answer:** B

**Explanation:** SHA-1 was deprecated because practical collision attacks were demonstrated (notably Google's SHAttered attack in 2017). A collision means two different inputs produce the same hash. For certificate signing, a collision attack could allow an attacker to create a fraudulent certificate that has the same SHA-1 signature as a legitimate one, undermining the integrity guarantee. SHA-1 is a hash function, not an encryption or symmetric algorithm, so options C and D are factually incorrect.

---

### Question 6

An administrator wants to check in real time whether a specific TLS certificate has been revoked before accepting it. Which mechanism provides this capability?

A. CRL

B. OCSP

C. OCSP Stapling

D. Certificate Transparency

**Correct Answer:** B

**Explanation:** OCSP (Online Certificate Status Protocol) allows a client to query an OCSP responder in real time for the revocation status of a specific certificate. A CRL is a periodically published list — it is not real-time and requires downloading the full list. OCSP Stapling is an optimization where the server pre-fetches and caches a signed OCSP response; the client receives it from the server, not by querying directly. Certificate Transparency logs certificate issuance but does not provide revocation status.

---

### Question 7

Which statement BEST describes the mathematical basis that makes ECC more efficient than RSA for the same security level?

A. ECC uses symmetric key operations internally, which are faster than asymmetric operations.

B. ECC is based on the elliptic curve discrete logarithm problem, which is harder to solve per bit than the integer factorization problem underlying RSA.

C. ECC uses longer keys than RSA, which allows it to operate on smaller data blocks.

D. ECC eliminates the need for key exchange entirely.

**Correct Answer:** B

**Explanation:** ECC's security relies on the elliptic curve discrete logarithm problem, which is computationally harder per bit than the integer factorization problem that RSA uses. This means a 256-bit ECC key provides approximately the same security as a 3072-bit RSA key. ECC does not use symmetric operations internally, does not use longer keys (it uses shorter keys), and does not eliminate key exchange.

---

### Question 8

A developer is implementing a password storage system. They plan to hash each password with SHA-256 before storing it. A security reviewer flags this as insufficient. What additional mechanism MUST be applied to prevent rainbow table attacks?

A. Encrypt the SHA-256 hash with AES before storing.

B. Add a unique random value (salt) to each password before hashing.

C. Use SHA-512 instead of SHA-256 for a larger hash output.

D. Hash each password twice to produce a double hash.

**Correct Answer:** B

**Explanation:** A rainbow table is a precomputed lookup table mapping common passwords to their hash values. If two users have the same password, they will have the same SHA-256 hash — making the table effective for mass cracking. A salt is a unique random value prepended or appended to each password before hashing. Because every salt is different, identical passwords produce different hashes, invalidating rainbow tables entirely. Using a larger hash (SHA-512) or double-hashing does not prevent rainbow tables. Encrypting the hash adds a layer but does not address the precomputation problem.

---

### Question 9

During the TLS handshake, the server sends its digital certificate to the client. What is the PRIMARY purpose of this certificate in the handshake?

A. To encrypt the session data using the server's public key.

B. To allow the client to verify the server's identity and obtain the server's public key.

C. To provide the symmetric session key to the client.

D. To sign the client's certificate request.

**Correct Answer:** B

**Explanation:** The server's certificate serves two purposes in the TLS handshake: it allows the client to verify that it is communicating with the legitimate server (by validating the certificate chain back to a trusted root CA), and it provides the server's public key for use in the key exchange phase. The certificate does not encrypt session data directly — that is done with a symmetric session key derived during key exchange. The certificate does not contain or transmit a symmetric key, and standard TLS does not involve client certificate requests unless mutual TLS is configured.

---

### Question 10

An organization's internal PKI has three levels: a root CA, two intermediate CAs, and thousands of end-entity certificates. The root CA's private key is compromised. What is the MOST accurate statement about the impact?

A. Only the certificates issued by the compromised root CA are affected; intermediate CA certificates remain valid.

B. The entire PKI is compromised, because all trust in the hierarchy ultimately derives from the root CA.

C. Only the intermediate CAs need to reissue their certificates; end-entity certificates are unaffected.

D. The impact is limited to TLS certificates; code signing and email certificates are unaffected.

**Correct Answer:** B

**Explanation:** In a PKI hierarchy, all trust ultimately flows from the root CA. Every intermediate CA certificate and every end-entity certificate was issued under the authority of the root CA. If the root CA's private key is compromised, an attacker can sign fraudulent certificates that will appear valid to any system that trusts the root. The entire PKI must be rebuilt: the root CA key pair must be replaced, intermediate CAs must be reissued, and all end-entity certificates must be reissued under the new hierarchy.

---

---

### Question 11

A developer implements a file integrity monitoring system and wants to detect any unauthorized modification to a critical configuration file. Which property of a cryptographic hash function makes it suitable for this purpose?

A. Hash functions are reversible, allowing the original file to be recovered if the hash is known.

B. A hash function produces the same fixed-size output regardless of input size, and any change to the input produces a completely different hash.

C. Hash functions encrypt the file content, preventing unauthorized users from reading it.

D. Hash functions use a shared secret key to produce the digest, making it impossible to forge without the key.

**Correct Answer:** B

**Explanation:** The deterministic and collision-resistant properties of a hash function make it suitable for integrity monitoring. The same input always produces the same hash (determinism), and any modification to the file — even a single bit — produces a completely different hash (avalanche effect). Hash functions are one-way, not reversible. They do not encrypt content. Hash functions (without HMAC) do not use a shared secret key — that is the distinction between a hash and a MAC.

---

### Question 12

An organization wants to ensure that data exchanged between two parties cannot be altered in transit without detection, and that the sender cannot later deny sending the data. Which combination of controls satisfies BOTH requirements?

A. AES-256 encryption with a shared symmetric key

B. TLS 1.3 with a server-only certificate

C. A digital signature using the sender's private key, combined with TLS for transport encryption

D. SHA-256 hashing of the transmitted data

**Correct Answer:** C

**Explanation:** A digital signature satisfies both requirements: the hash of the message signed with the sender's private key provides integrity (any alteration invalidates the signature) and non-repudiation (only the holder of the private key could have produced the signature). AES-256 with a shared key provides confidentiality and integrity but not non-repudiation — either party with the key could have produced the ciphertext. TLS alone provides integrity and server authentication but not sender non-repudiation. SHA-256 provides integrity detection but not non-repudiation since anyone can compute the hash.

---

### Question 13

A security architect is selecting an asymmetric algorithm for a new system that must generate large numbers of ephemeral key pairs quickly on resource-constrained IoT devices. Which algorithm is MOST appropriate and why?

A. RSA-4096, because larger keys provide more security.

B. ECC with a 256-bit key, because it provides security equivalent to RSA-3072 with much smaller keys and lower computational cost.

C. MD5 with a 128-bit digest, because it is faster than RSA.

D. AES-256, because symmetric algorithms are faster than asymmetric algorithms.

**Correct Answer:** B

**Explanation:** ECC (Elliptic Curve Cryptography) provides security equivalent to much larger RSA keys with significantly shorter key lengths, making it faster to generate, use, and transmit. A 256-bit ECC key provides approximately the same security as a 3072-bit RSA key. This efficiency makes ECC the preferred choice for IoT and resource-constrained environments. RSA-4096 is computationally expensive. MD5 is a hash function, not an asymmetric encryption algorithm. AES-256 is symmetric and does not support the key exchange functions of asymmetric cryptography.

---

### Question 14

A web application's database stores user passwords as SHA-256 hashes with no additional processing. An attacker who obtains the password hash database can determine that two different users have the same password because their hashes are identical. Which cryptographic technique would prevent this?

A. Using SHA-512 instead of SHA-256 to produce longer hashes

B. Adding a unique random salt to each password before hashing

C. Encrypting the hash database with AES-256

D. Hashing each password twice using two different algorithms

**Correct Answer:** B

**Explanation:** A salt is a unique random value added to each password before hashing. Because every user has a different salt, identical passwords produce different hashes, preventing both cross-user comparison and precomputed (rainbow table) attacks. Switching to SHA-512 produces longer hashes but still allows identical passwords to match. Encrypting the hash database protects it in transit and at rest but does not prevent an attacker with database access from comparing identical hashes. Double-hashing with different algorithms does not prevent the identical-hash comparison problem.

---

### Question 15

An organization discovers that a certificate authority used by their internal PKI has been compromised. The CA had issued certificates to 400 internal servers. What is the CORRECT sequence of remediation steps?

A. Revoke the compromised CA certificate, reissue all 400 server certificates under a new CA, and distribute the updated CRL or OCSP information to all clients.

B. Delete the CA certificate from all client trust stores and wait for all 400 server certificates to expire naturally.

C. Add the compromised certificates to the OCSP responder and continue using them until new certificates can be issued.

D. Rotate the CA's private key without revoking existing certificates, then reissue server certificates over the next six months.

**Correct Answer:** A

**Explanation:** When a CA is compromised, all certificates issued by that CA are untrusted regardless of whether individual certificates appear valid. The correct sequence is to revoke the compromised CA certificate (which invalidates all its issued certificates through the chain of trust), stand up a new CA with a new key pair, reissue all server certificates under the new CA, and update CRL/OCSP infrastructure so clients can verify revocation status. Waiting for natural expiration leaves systems exposed. Adding to OCSP without revoking perpetuates trust in compromised certificates. Rotating the CA key without revoking existing certificates does not invalidate the certificates signed by the old (compromised) key.

---

### Question 16

A security engineer must transmit a 2 GB encrypted archive to a business partner over the internet. The engineer encrypts the archive with AES-256 and then needs to securely deliver the decryption key to the partner without prior shared-secret agreement. Which approach correctly solves the key distribution problem?

A. Encrypt the AES key with the partner's public RSA key and transmit it alongside the encrypted archive.

B. Hash the AES key with SHA-256 and email the hash to the partner so they can verify the key on receipt.

C. Transmit the AES key in the same encrypted archive — the partner can extract it after decryption.

D. Use a second AES key to encrypt the first AES key, and email the second key to the partner.

**Correct Answer:** A

**Explanation:** This is a hybrid encryption scheme — the data itself is encrypted with fast symmetric AES, while the AES key is protected with asymmetric RSA using the partner's public key. Only the partner's private key can decrypt the AES key. SHA-256 is a hash function that cannot encrypt or protect the key — it only produces a fixed-size digest. Bundling the AES key inside the archive it encrypts is logically circular — the partner cannot decrypt the archive to get the key they need for decryption. Using a second AES key shifts the problem one level without solving it, as the second key now has no secure delivery mechanism.

---

### Question 17

An organization is transitioning its web services from TLS 1.2 to TLS 1.3. A network analyst notes that TLS 1.3 removes support for RSA key exchange cipher suites entirely. What is the PRIMARY security reason for this removal?

A. RSA keys are too short for modern encryption requirements and must be replaced with longer keys.

B. RSA key exchange does not provide Perfect Forward Secrecy — if the server's private key is later compromised, all previously recorded TLS sessions can be decrypted.

C. RSA is a symmetric algorithm that conflicts with TLS 1.3's requirement for asymmetric key exchange.

D. RSA certificates cannot be validated against a CRL, making certificate revocation impossible in TLS 1.3.

**Correct Answer:** B

**Explanation:** In RSA key exchange, the client encrypts the pre-master secret using the server's RSA public key. If the server's private key is ever compromised — even years later — an attacker who recorded past sessions can decrypt the pre-master secret and then decrypt all recorded session data. TLS 1.3 mandates ephemeral Diffie-Hellman key exchange (ECDHE), which derives a unique session key not recoverable from the long-term private key, providing Perfect Forward Secrecy. RSA key sizes are not the issue — RSA-2048 and RSA-4096 remain computationally secure. RSA is an asymmetric algorithm, not symmetric. CRL validation is independent of the key exchange algorithm.

---

### Question 18

A company stores HMAC-SHA256 values alongside log files to detect unauthorized modification. An auditor asks how HMAC differs from a plain SHA-256 hash for integrity verification. Which answer BEST describes the difference?

A. HMAC produces a longer output than SHA-256, making collisions less likely.

B. HMAC incorporates a shared secret key into the hash computation, so only a party with the correct key can produce or verify a valid HMAC — preventing an attacker who modifies a file from also recomputing a valid integrity value.

C. HMAC uses asymmetric key pairs, allowing the public key to verify HMACs produced with the private key.

D. HMAC is faster than SHA-256 because it skips the padding step in the hash computation.

**Correct Answer:** B

**Explanation:** A plain SHA-256 hash provides integrity detection only if the hash is stored separately from the file — but any attacker who can modify the file can also recompute a new SHA-256 hash over the modified content and replace the stored hash, undetected. HMAC (Hash-based Message Authentication Code) mixes a shared secret key into the hash using a defined construction (RFC 2104), so without knowledge of the key, an attacker cannot compute a valid HMAC for modified data. HMAC output length matches the underlying hash function — it is not longer. HMAC uses a symmetric shared secret, not asymmetric key pairs. HMAC is not faster than SHA-256; it involves additional key mixing steps.

---

### Question 19

A PKI administrator receives a request to issue a wildcard certificate for `*.example.com`. A security architect objects, citing risk. Which concern about wildcard certificates BEST justifies the architect's objection?

A. Wildcard certificates use weaker encryption algorithms than single-name certificates.

B. Wildcard certificates cannot be validated by OCSP responders and must rely solely on CRL.

C. If a single server using the wildcard certificate is compromised, the private key can be used to impersonate any subdomain covered by the wildcard, expanding the blast radius of the compromise.

D. Wildcard certificates expire after 30 days and require more frequent renewal than standard certificates.

**Correct Answer:** C

**Explanation:** A wildcard certificate covers all first-level subdomains of the specified domain (e.g., mail.example.com, vpn.example.com, store.example.com). All servers using the wildcard share the same private key. If any one of those servers is compromised and the private key is extracted, an attacker can impersonate every subdomain — greatly expanding the scope of a single server compromise. Wildcard certificates use the same encryption algorithms as standard certificates. OCSP works for wildcard certificates. Certificate validity periods are determined by CA policy and are not inherently shorter for wildcards.

---

### Question 20

A developer must store API keys on behalf of users in a web application. Each API key is unique per user and must be retrievable in plaintext when the user needs to use it. A security reviewer flags storing API keys as SHA-256 hashes as inadequate for this requirement. Which cryptographic approach is CORRECT for this use case and why?

A. Store SHA-512 hashes — the longer output makes retrieval possible for authorized users.

B. Store the API keys encrypted with AES-256 using a key derived from a server-side master secret, because the application needs to recover the original plaintext and hashing is a one-way operation that cannot be reversed.

C. Store the API keys as bcrypt hashes — the higher cost factor makes them retrievable with a password.

D. Store the API keys as plain text — since they will be displayed to users anyway, encryption provides no benefit.

**Correct Answer:** B

**Explanation:** Hashing (SHA-256, SHA-512, bcrypt) is a one-way operation — the original value cannot be recovered from the hash. Since the application must return the original API key to the user, reversible encryption is required. AES-256 with a securely managed server-side key allows the application to decrypt and return the API key when authorized. The master encryption key must be protected in a key management system or hardware security module. SHA-512 is still a one-way hash — output length does not enable retrieval. Bcrypt is specifically designed for password hashing and is equally irreversible. Storing API keys in plaintext provides no protection if the database is breached; at minimum, encryption at rest is required.

---

Module 05 Quiz — End
