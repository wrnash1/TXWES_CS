# Reading Guide: Module 09 - Authentication - MFA, SSO, and Biometrics
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

### Introduction
Welcome to **Module 09 – Authentication: MFA, SSO, and Biometrics**! Authentication is the process of verifying that a user or system is who they claim to be. SY0-701 tests authentication concepts across multiple domains — expect scenario questions on selecting the right authentication factor, understanding federation protocols, and evaluating biometric error rates.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Authentication Factors**: The three classical categories used to verify identity — something you know (password, PIN), something you have (smart card, hardware token, OTP), and something you are (fingerprint, retina scan). A fourth category — somewhere you are (geolocation) — appears on SY0-701. Multi-factor authentication (MFA) requires at least two different factor categories; using two passwords is not MFA.
*   **Multi-Factor Authentication (MFA)**: An authentication method requiring a user to present credentials from two or more distinct factor categories before access is granted. MFA dramatically reduces account compromise risk because an attacker who steals a password still cannot authenticate without the second factor. SY0-701 tests MFA in scenarios involving phishing-resistant authenticators, push notification fatigue (MFA bombing), and hardware token deployment.
*   **Single Sign-On (SSO)**: An authentication architecture that allows a user to authenticate once and gain access to multiple applications or services without re-entering credentials for each one. SSO relies on a trusted identity provider (IdP) that issues tokens or assertions to service providers. Common protocols include SAML 2.0, OAuth 2.0, and OpenID Connect (OIDC). SY0-701 tests SSO in federation and cloud identity scenarios.
*   **SAML (Security Assertion Markup Language)**: An XML-based open standard for exchanging authentication and authorization data between an identity provider (IdP) and a service provider (SP). SAML 2.0 is widely used for enterprise SSO — when a user authenticates to the IdP, the IdP issues a signed SAML assertion that the SP trusts to grant access without requiring a separate login.
*   **Biometric Authentication**: An authentication method that verifies identity based on unique biological or behavioral characteristics — fingerprint, iris scan, facial recognition, voice pattern, or typing cadence. Key biometric metrics on SY0-701: False Acceptance Rate (FAR) — the rate at which impostors are incorrectly accepted; False Rejection Rate (FRR) — the rate at which legitimate users are incorrectly denied; Crossover Error Rate (CER/EER) — the point where FAR equals FRR, used to compare biometric system accuracy.
*   **Password Attacks and Defenses**: Common password attacks tested on SY0-701 include dictionary attacks (wordlist against hashed credentials), brute force (all possible combinations), credential stuffing (using breach-leaked credentials against other sites), and password spraying (one common password against many accounts to avoid lockout). Defenses include salted hashing, account lockout policies, MFA, and privileged password managers.

---

### 2. Certification Exam Tips
*   **Domain Weight:** Authentication falls under **Domain 2 – Threats, Vulnerabilities, and Mitigations (22%)** and **Domain 4 – Security Operations (28%)** of SY0-701. Expect scenario questions selecting the strongest authentication method for a given risk scenario.
*   **MFA Factor Trap:** Two passwords (even from different systems) are NOT MFA — they are both "something you know." MFA requires credentials from two different factor categories. If a question describes a user entering a password and a PIN, that is single-factor (both are knowledge factors). A password plus a hardware token or a fingerprint is true MFA.
*   **Biometric Error Rate Trap:** Lower CER = better biometric system. FAR and FRR trade off against each other: decreasing sensitivity lowers FAR (fewer false accepts) but raises FRR (more false rejects). The exam may describe a scenario where security is prioritized (minimize FAR) or convenience is prioritized (minimize FRR) and ask which setting is appropriate.
*   **SSO Protocol Selection:** SAML 2.0 is used for enterprise web SSO (XML-based, identity federation). OAuth 2.0 is an authorization framework (grants access without sharing credentials — used for "Sign in with Google"). OpenID Connect (OIDC) adds an authentication layer on top of OAuth 2.0. SY0-701 tests which protocol fits a given integration scenario.
*   **Study Resource:** Professor Messer's free [CompTIA Security+ SY0-701 study notes and video course](https://www.professormesser.com/) include authentication factor diagrams, SSO flow charts, and biometric error rate comparisons that mirror SY0-701 scenario question formats.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the "Authentication" section in the OER Textbook: [Professor Messer's CompTIA Security+ SY0-701 Study Notes](https://www.professormesser.com/). Focus on authentication factor categories, MFA implementations, and SSO federation protocols.
*   **Required Video:** Watch the authentication video lectures in [Professor Messer's SY0-701 Course Playlist on YouTube](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy). The videos walk through MFA push notification attacks, SAML assertion flows, and biometric system comparisons.

---

### Lab & Command Integration
In this week's hands-on lab, you will configure MFA policies, analyze authentication logs for failed login patterns (credential stuffing vs. brute force vs. password spraying), and review SSO token flows. Recognizing attack patterns in authentication logs is a direct SY0-701 performance-based question skill.

---

### 9. Supplemental Resources

**1. NIST SP 800-63B — Digital Identity Guidelines: Authentication and Lifecycle Management**
<https://pages.nist.gov/800-63-3/sp800-63b.html>
NIST's authoritative guidance on authenticator assurance levels (AAL1, AAL2, AAL3), phishing-resistant MFA requirements, and password policy recommendations. Directly supports Module 09 coverage of MFA factor types, FIDO2 requirements, and the deprecation of SMS OTP for high-assurance use cases.

**2. FIDO Alliance — How FIDO Works**
<https://fidoalliance.org/how-fido-works/>
The FIDO Alliance's explanation of FIDO2/WebAuthn authentication including passkeys, hardware security keys, and the origin-binding mechanism that makes FIDO2 phishing-resistant. Directly addresses Module 09 content on phishing-resistant authenticators and the distinction between TOTP and FIDO2 security properties.

**3. OWASP Authentication Cheat Sheet**
<https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>
A practical reference covering secure authentication implementation including password storage (salting and hashing), account lockout policies, MFA implementation, and session management. Bridges Module 09 authentication concepts with the secure coding practices covered in Module 03.

---

### 3. Study Checklist
- [ ] Read the glossary terms above and be able to classify authentication factors and select the correct method for any given scenario.
- [ ] Read the "Authentication" section in [Professor Messer's SY0-701 Study Notes](https://www.professormesser.com/).
- [ ] Watch the authentication video lectures in [Professor Messer's SY0-701 Course Playlist](https://www.youtube.com/playlist?list=PLG49S3nxzAnl4Q7y9umx51bbtILyD4Syy).
- [ ] Memorize: MFA = two different factor categories; CER = FAR equals FRR crossover; SAML = enterprise SSO; OAuth = delegated authorization.
- [ ] Proceed to the weekly hands-on lab activity.
