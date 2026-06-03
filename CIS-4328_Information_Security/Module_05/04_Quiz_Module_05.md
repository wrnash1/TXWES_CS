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

Module 05 Quiz — End
