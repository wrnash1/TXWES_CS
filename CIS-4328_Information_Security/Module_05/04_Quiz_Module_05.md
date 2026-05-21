# Quiz: Module 05 - Cryptography Fundamentals
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
In the context of standard IT systems, which of the following is the most accurate definition of **Role-Based Access Control (RBAC)**?
A) A method of granting permissions based on a user's job role, so that all users with the same role inherit the same set of access rights.
B) A cryptographic method that uses a public key to encrypt data and a mathematically related private key to decrypt it.
C) A security model where every access request is verified regardless of network location, assuming no implicit trust inside or outside the perimeter.
D) A one-way mathematical function that produces a fixed-length digest used to verify data integrity without revealing the original data.
*   **Correct Answer:** A) A method of granting permissions based on a user's job role, so that all users with the same role inherit the same set of access rights.
*   **Distractor Analysis:**
    *   *Why A is correct:* RBAC assigns permissions to roles (e.g., "HR Manager," "Network Admin") rather than to individual users, simplifying administration and enforcing least privilege by job function.
    *   *Why B is incorrect:* This describes asymmetric (public-key) cryptography — a completely separate concept from access control models.
    *   *Why C is incorrect:* This describes the Zero Trust security model — an architectural principle about trust levels, not an access control assignment method.
    *   *Why D is incorrect:* This describes a cryptographic hash function — a data integrity tool, not an access control mechanism.

---

---

**Question 2**
An organization needs to store user passwords securely in its database so that even if the database is breached, plaintext passwords cannot be recovered. Which cryptographic technique should be applied to each password before storage?
A) Encrypt each password with AES-256 using a master encryption key stored in a Hardware Security Module.
B) Apply a salted hash using SHA-256 to each password before storing the digest in the database.
C) Encode each password using Base64 encoding before writing it to the database.
D) Apply RSA encryption to each password using the server's public key.
*   **Correct Answer:** B) Apply a salted hash using SHA-256 to each password before storing the digest in the database.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Symmetric encryption is reversible — if an attacker obtains the master key they can decrypt all passwords. Hashing is one-way and the preferred approach for password storage because recovery is computationally infeasible.
    *   *Why C is incorrect:* Base64 is an encoding scheme, not encryption or hashing — it provides no security whatsoever. Any tool can decode Base64 in milliseconds.
    *   *Why D is incorrect:* RSA is designed for key exchange and digital signatures on small data, not bulk password storage. RSA encryption is also reversible with the private key, defeating the purpose of one-way protection.

---

---

**Question 3**
A security engineer needs to run a dictionary brute-force test against an SSH service to evaluate password strength. Which command accomplishes this task?
A) hydra -l admin -P passwords.txt ssh://target
B) nmap -sV -p 1-1024 target_ip
C) wireshark
D) openssl x509 -text -noout -in cert.pem
*   **Correct Answer:** A) hydra -l admin -P passwords.txt ssh://target
*   **Distractor Analysis:**
    *   *Why B is incorrect:* nmap performs port scanning and service version detection — it identifies open ports but does not attempt authentication against services.
    *   *Why C is incorrect:* Wireshark is a packet capture and protocol analysis tool — it passively captures traffic but does not send authentication attempts.
    *   *Why D is incorrect:* The openssl x509 command displays the contents of an X.509 certificate file — it is a certificate inspection tool, not a credential-testing tool.

---

**Question 4**
An organization wants to protect data in transit between a web server and clients using the strongest available symmetric encryption. Which algorithm and key length should the security team configure?
A) DES with a 56-bit key
B) RC4 with a 128-bit key
C) 3DES with a 112-bit effective key
D) AES with a 256-bit key
*   **Correct Answer:** D) AES with a 256-bit key
*   **Distractor Analysis:**
    *   *Why A is incorrect:* DES uses a 56-bit key that can be brute-forced in under 24 hours with modern hardware — it has been considered cryptographically broken since the late 1990s and is not approved for current use.
    *   *Why B is incorrect:* RC4 is a stream cipher with multiple known biases and vulnerabilities that allow statistical attacks to recover plaintext. It was officially prohibited in TLS by RFC 7465 and should never be used for security purposes.
    *   *Why C is incorrect:* 3DES applies DES three times to increase effective key length to 112 bits, but it is slow, vulnerable to the Sweet32 birthday attack on long-lived sessions, and deprecated by NIST as of 2023.

---

**Question 5**
A developer wants to ensure that a software package downloaded from the internet has not been tampered with during transit. Which cryptographic technique provides the BEST assurance of file integrity?
A) Encrypt the file with AES-256 before uploading it to the distribution server.
B) Publish the SHA-256 hash of the original file alongside the download link and verify it after download.
C) Sign the download page with an SSL/TLS certificate so the channel is encrypted.
D) Require users to download the file over a VPN tunnel to prevent interception.
*   **Correct Answer:** B) Publish the SHA-256 hash of the original file alongside the download link and verify it after download.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Encrypting the file protects confidentiality in transit, but if the file is tampered with at rest on the server before encryption, the hash of the tampered file will match the hash of the tampered ciphertext — encryption alone does not verify integrity of the original content.
    *   *Why C is incorrect:* TLS encrypts the transport channel and authenticates the server, but it does not guarantee the file on the server itself was not modified before being served. A compromised server serves the tampered file over a perfectly valid TLS connection.
    *   *Why D is incorrect:* A VPN encrypts the network tunnel between the user and the VPN endpoint but does not validate that the file content matches what the developer originally published — the tampered file arrives intact through the VPN.
