# Reading Guide: Module 06 - PKI and Certificate Management
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 06 – PKI and Certificate Management**! Public Key Infrastructure (PKI) is the trust framework that makes HTTPS, code signing, email encryption, and VPN authentication possible. SY0-701 tests PKI concepts in scenario questions about certificate errors, trust chains, and revocation — situations that security professionals encounter in real production environments.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Certificate Authority (CA)**: A trusted third party that issues, signs, and revokes digital certificates. A Root CA sits at the top of the trust hierarchy and signs Intermediate CA certificates. Browsers and operating systems ship with a pre-installed list of trusted Root CAs. When an organization deploys an internal CA, all devices must be configured to trust it explicitly.
*   **Certificate Signing Request (CSR)**: A block of encoded data that a server or device generates and submits to a CA when requesting a digital certificate. The CSR contains the subject's public key and identity information (Common Name, Organization, etc.) but never includes the private key. The CA verifies the identity claim and returns a signed certificate.
*   **X.509 Certificate**: The standard format for public key certificates used in PKI. An X.509 certificate binds an entity's identity (domain name, organization) to its public key and is signed by a CA. Key fields include Subject, Issuer, Validity Period (Not Before / Not After), Subject Public Key Info, and extensions like Subject Alternative Names (SANs).
*   **CRL (Certificate Revocation List)**: A periodically published list of certificate serial numbers that a CA has revoked before their natural expiration date. Clients download and cache the CRL to check whether a presented certificate has been revoked. CRLs can become large and stale between publications — a weakness addressed by OCSP.
*   **OCSP (Online Certificate Status Protocol)**: A real-time protocol that allows a client to query a CA's OCSP responder to check the revocation status of a specific certificate. Unlike a CRL, OCSP returns a status for one certificate on demand rather than requiring a full list download. OCSP Stapling has the server pre-fetch and attach the OCSP response to the TLS handshake, reducing latency and preserving client privacy.
*   **Certificate Pinning**: A security technique where an application is hard-coded to accept only a specific certificate or CA for a given host, rather than trusting any CA in the system store. Pinning prevents MITM attacks using fraudulently issued certificates from rogue CAs but requires careful management to avoid breaking connections when legitimate certificates are renewed.

---

### 2. Certification Exam Tips
*   **Domain Weight:** PKI falls under **Domain 1 – General Security Concepts (12%)** of SY0-701. Certificate-related scenario questions are extremely common and test practical knowledge of trust chains and error resolution.
*   **Certificate Error Scenarios:** The exam presents a described error and asks you to identify the cause. "Certificate not trusted" = the issuing CA is not in the trust store. "Certificate expired" = the validity period has passed, requiring a new CSR and re-issuance. "Certificate revoked" = the CA invalidated it early, often due to key compromise.
*   **CRL vs. OCSP Trap:** CRL = periodic batch list (slower, can be stale). OCSP = real-time single-certificate query (faster, current). OCSP Stapling = server attaches the response to the handshake (eliminates separate client-to-OCSP-server round trip). Know when each is the better choice.
*   **Wildcard vs. SAN Certificates:** A wildcard certificate (*.example.com) covers all immediate subdomains but not sub-subdomains. A SAN certificate explicitly lists every hostname it covers and is the modern standard. SY0-701 may ask which certificate type is appropriate for a given multi-host scenario.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include PKI chain-of-trust diagrams and certificate field breakdowns that map directly to exam scenario questions.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "PKI and Certificate Management" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on the certificate lifecycle: generation, issuance, deployment, renewal, and revocation.
*   **Required Video:** Watch the PKI video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos walk through the full PKI trust hierarchy using real browser certificate inspector screenshots.

---

### Lab & Command Integration
In this week's hands-on lab, you will use OpenSSL to generate a CSR, self-sign a certificate, and inspect an X.509 certificate's fields using `openssl x509 -text -noout -in cert.pem`. Understanding every field in a certificate output is a direct SY0-701 performance-based question skill.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to trace the full certificate lifecycle from CSR to revocation.
- [ ] Read the "PKI and Certificate Management" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the PKI video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Be able to identify the correct action for each common certificate error: expired, untrusted CA, revoked, name mismatch.
- [ ] Proceed to the weekly hands-on lab activity.
