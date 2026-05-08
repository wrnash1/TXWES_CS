### 5. Quiz 3: Security Architecture (Question Bank)
**Question 1**
An organization wants to deploy a new public-facing customer portal. The portal must communicate with a highly secure backend database that stores PII. Which network architectural design provides the most secure placement for these servers?
A) Place both the web server and the database server in the DMZ to ensure fast communication.
B) Place the web server in the DMZ and the database server on the internal secure network.
C) Place both servers on the internal secure network and forward port 80/443 directly from the internet router.
D) Place the database server in the DMZ and the web server on the internal network.
*   **Correct Answer:** B) Place the web server in the DMZ and the database server on the internal secure network.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Placing the database in the DMZ exposes sensitive PII to a less secure zone, violating defense-in-depth principles.
    *   *Why C is incorrect:* Port forwarding directly to the internal network bypasses the DMZ entirely, exposing the secure network to direct internet attacks.
    *   *Why D is incorrect:* The web server must face the public internet (DMZ), and the database must be hidden (Internal). Reversing them breaks functionality and security.

**Question 2**
Alice wants to send a highly confidential contract to Bob over an untrusted network. She wants to ensure that *only* Bob can read the contract. Using asymmetric cryptography, whose key should Alice use to encrypt the document?
A) Alice's Private Key
B) Alice's Public Key
C) Bob's Private Key
D) Bob's Public Key
*   **Correct Answer:** D) Bob's Public Key
*   **Distractor Analysis:**
    *   *Why A is incorrect:* If Alice encrypts it with her private key, anyone with her public key (which is everyone) can decrypt it. This provides non-repudiation, not confidentiality.
    *   *Why B is incorrect:* You do not encrypt messages with your own public key.
    *   *Why C is incorrect:* Alice does not have access to Bob's private key; it must remain exclusively with Bob. Only Bob's private key can decrypt a message encrypted with Bob's public key.
