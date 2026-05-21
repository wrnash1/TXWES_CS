# Quiz: Module 06 - PKI and Certificate Management
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A web browser displays a "Your connection is not private" warning when a user navigates to an internal company web application. The IT team confirms the server certificate was issued by the company's own internal Certificate Authority. What is the most likely cause of this warning?
A) The certificate has expired and must be renewed by submitting a new CSR.
B) The internal CA's root certificate is not installed in the user's browser trust store.
C) The certificate was revoked by the CA due to a detected private key compromise.
D) The web server is using a self-signed certificate with a 1024-bit RSA key.
*   **Correct Answer:** B) The internal CA's root certificate is not installed in the user's browser trust store.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An expired certificate triggers a different browser warning that explicitly states the certificate has expired and shows the expiration date — it is a distinct error from an untrusted issuer warning.
    *   *Why C is incorrect:* A revoked certificate would show a revocation error if OCSP/CRL checking is functioning. However, the scenario states the CA is internal and the most direct explanation for the "not private" warning on an internal certificate is a missing trust anchor.
    *   *Why D is incorrect:* While a 1024-bit RSA key is weak and should not be used, browsers display an untrusted issuer warning specifically when the signing CA is not in the trust store — key length alone does not trigger the described warning message.

---

---

**Question 2**
A security engineer needs to check whether a specific TLS certificate presented by a web server has been revoked, without downloading the entire Certificate Revocation List. Which protocol should the engineer use?
A) LDAP
B) DNSSEC
C) OCSP
D) RADIUS
*   **Correct Answer:** C) OCSP
*   **Distractor Analysis:**
    *   *Why A is incorrect:* LDAP (Lightweight Directory Access Protocol) is used to query directory services such as Active Directory for user and group information — it is not used for certificate revocation status checks.
    *   *Why B is incorrect:* DNSSEC (DNS Security Extensions) adds cryptographic signatures to DNS records to prevent DNS spoofing — it does not provide certificate revocation status for TLS certificates.
    *   *Why D is incorrect:* RADIUS (Remote Authentication Dial-In User Service) is an AAA protocol used for network access authentication — it has no role in checking certificate revocation status.

---

---

**Question 3**
A systems administrator needs to display the detailed metadata and validation parameters of an SSL/TLS digital certificate stored in a PEM file. Which command is most appropriate?
A) openssl x509 -text -noout -in cert.pem
B) nmap -sV -p 443 target_ip
C) wireshark
D) hydra -l admin -P passwords.txt ssh://target
*   **Correct Answer:** A) openssl x509 -text -noout -in cert.pem
*   **Distractor Analysis:**
    *   *Why B is incorrect:* nmap -sV performs port scanning and service version detection — it can retrieve certificate information remotely but is not the correct tool for inspecting a locally stored certificate PEM file.
    *   *Why C is incorrect:* Wireshark captures and analyzes live network packets — it can show TLS handshake data in a capture but cannot inspect a certificate file stored on disk.
    *   *Why D is incorrect:* Hydra is a network login brute-force tool — it tests credentials against authentication services and has no function related to certificate inspection.

---

**Question 4**
An organization's PKI administrator receives a report that the private key for a recently issued web server certificate may have been exfiltrated from a misconfigured backup. What is the MOST appropriate immediate action?
A) Generate a new Certificate Signing Request and wait for the current certificate to expire naturally.
B) Revoke the compromised certificate via the CA and issue a new certificate with a freshly generated key pair.
C) Extend the certificate's validity period using the CA management console to buy time for investigation.
D) Re-deploy the same certificate on a new server to isolate the compromised system.
*   **Correct Answer:** B) Revoke the compromised certificate via the CA and issue a new certificate with a freshly generated key pair.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Waiting for natural expiration is never acceptable when a private key compromise is suspected — an attacker holding the key can impersonate the server or decrypt intercepted traffic until the certificate expires.
    *   *Why C is incorrect:* Certificate validity periods are set by the CA at issuance and cannot be extended after the fact. Even if it were possible, extending a compromised certificate prolongs the exposure window.
    *   *Why D is incorrect:* Redeploying the same certificate with the same compromised private key on a different server does not address the compromise — the attacker still holds the private key and can decrypt or impersonate regardless of which server hosts the certificate.

---

**Question 5**
An organization uses a three-tier PKI hierarchy: Root CA, Intermediate CA, and Issuing CA. The Root CA is kept offline in a physically secured vault. What is the PRIMARY security reason for keeping the Root CA offline?
A) Offline Root CAs issue certificates faster because they are not subject to network latency.
B) If the Root CA's private key is compromised, every certificate in the entire PKI hierarchy becomes untrusted and must be replaced.
C) Regulations require Root CAs to be air-gapped to comply with PCI-DSS Section 3.4.
D) Keeping the Root CA offline prevents it from being included in CRL distribution points.
*   **Correct Answer:** B) If the Root CA's private key is compromised, every certificate in the entire PKI hierarchy becomes untrusted and must be replaced.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Root CA does not issue end-entity certificates in a three-tier hierarchy — the Issuing CA does. The Root CA only signs the Intermediate CA certificate, which happens rarely. Offline status has nothing to do with issuance speed.
    *   *Why C is incorrect:* While compliance frameworks encourage strong CA protection, the fundamental reason is trust preservation, not regulatory mandate. PCI-DSS does not specifically require Root CA air-gapping in the manner described.
    *   *Why D is incorrect:* The Root CA's certificate does not typically appear in CRL distribution points — end-entity certificates reference the Issuing CA's CRL. Offline status is purely a key protection strategy.
