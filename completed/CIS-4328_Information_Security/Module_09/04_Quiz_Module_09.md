# Quiz: Module 09 - Authentication - MFA, SSO, and Biometrics
## Course: CIS-4328_Information_Security (CompTIA Security+ SY0-701)

---

**Question 1**
A company requires employees to log in with a password and then approve a push notification on their registered smartphone before gaining access to corporate systems. An attacker who steals an employee's password attempts to log in and triggers the push notification. The employee declines the request. Which statement best describes this authentication scenario?
A) The system is using single-factor authentication because the password and the phone are both owned by the same person.
B) The push notification is a "something you know" factor because the employee must know which notification to approve.
C) The system is using multi-factor authentication because credentials from two different factor categories are required.
D) This is an example of SSO because the employee only approves one notification to access all corporate systems.
*   **Correct Answer:** C) The system is using multi-factor authentication because credentials from two different factor categories are required.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* MFA is defined by the number of distinct factor categories, not by ownership. The password is "something you know" and the smartphone is "something you have" — two different categories make this MFA regardless of who owns the device.
    *   *Why B is incorrect:* Approving a push notification on a physical device is a "something you have" factor — the authentication relies on possession of the enrolled device, not on knowledge of information.
    *   *Why D is incorrect:* SSO is an architecture that allows one authentication event to grant access to multiple systems. Approving a push notification is a second authentication factor within a single login event, not an SSO session.

---

---

**Question 2**
A security administrator is comparing two biometric fingerprint scanners for deployment at a secure facility. Scanner A has a False Acceptance Rate (FAR) of 0.001% and a False Rejection Rate (FRR) of 5%. Scanner B has an FAR of 1% and an FRR of 0.5%. The facility's primary concern is preventing unauthorized individuals from gaining physical access. Which scanner should be deployed and why?
A) Scanner B, because its lower FRR means fewer legitimate users will be inconvenienced at the door.
B) Scanner A, because its lower FAR means unauthorized individuals are rarely incorrectly granted access.
C) Scanner B, because a lower FAR always indicates a more accurate biometric system overall.
D) Scanner A, because a lower CER always indicates the system with the smaller FAR value.
*   **Correct Answer:** B) Scanner A, because its lower FAR means unauthorized individuals are rarely incorrectly granted access.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* When the primary concern is security (preventing unauthorized access), minimizing the FAR takes priority over minimizing the FRR. A lower FRR improves convenience for legitimate users but does not address the threat of impostors being accepted.
    *   *Why C is incorrect:* Scanner B has a higher FAR (1%), which means it incorrectly accepts impostors more often — this is the opposite of what a security-focused facility needs. Overall accuracy is measured by the CER, not FAR alone.
    *   *Why D is incorrect:* The CER (Crossover Error Rate) is the point where FAR equals FRR and is used to compare overall system accuracy between scanners — it is not calculated simply from the FAR value, and a lower FAR alone does not imply a lower CER.

---

---

**Question 3**
An enterprise is deploying a federated identity solution so that employees can access a cloud-based HR application using their corporate Active Directory credentials without creating a separate account in the HR system. The HR vendor supports industry-standard protocols. Which protocol is most appropriate for this enterprise SSO federation scenario?
A) RADIUS
B) Kerberos
C) SAML 2.0
D) WPA3-Enterprise
*   **Correct Answer:** C) SAML 2.0
*   **Distractor Analysis:**
    *   *Why A is incorrect:* RADIUS (Remote Authentication Dial-In User Service) is an AAA protocol used for network access authentication (Wi-Fi, VPN, 802.1X) — it is not designed for web-based SSO federation between an enterprise identity provider and a cloud application.
    *   *Why B is incorrect:* Kerberos is a ticket-based authentication protocol used within a single administrative domain (such as an Active Directory environment) — it does not natively federate identity across organizational boundaries to external cloud providers.
    *   *Why D is incorrect:* WPA3-Enterprise is a Wi-Fi security standard that uses 802.1X and RADIUS for wireless network authentication — it is unrelated to application-layer SSO federation.

---

**Question 4**
A threat intelligence report warns that attackers are conducting password spraying attacks against an organization's Office 365 tenant. In a password spraying attack, the attacker tries one common password (such as "Summer2024!") against a large number of accounts before moving to the next password. Which control is MOST effective at preventing account compromise from this attack?
A) Require all users to change their passwords every 30 days.
B) Implement account lockout after three failed attempts within ten minutes.
C) Deploy multi-factor authentication (MFA) for all user accounts.
D) Enforce a minimum password length of eight characters.
*   **Correct Answer:** C) Deploy multi-factor authentication (MFA) for all user accounts.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Frequent password rotation leads users to create predictable patterns (e.g., "Summer2024!", "Fall2024!") and does not prevent the attacker from trying the currently valid password. NIST SP 800-63B no longer recommends forced periodic rotation.
    *   *Why B is incorrect:* Password spraying is specifically designed to evade lockout policies by trying only one or a few passwords per account before moving on — traditional lockout thresholds are not triggered, making lockout ineffective against this attack pattern.
    *   *Why D is incorrect:* A minimum length requirement does not prevent an attacker from successfully guessing a password that meets the requirement, such as "Summer2024!" — it does not address the authentication-layer weakness that MFA closes.

---

**Question 5**
A user reports that they received three unexpected MFA push notifications on their smartphone in rapid succession, which they did not initiate. The user did not approve any of them. What type of attack does this pattern most likely indicate, and what should the user do?
A) This is a credential stuffing attack; the user should immediately reset their password and enroll a new MFA device.
B) This is an MFA fatigue (push bombing) attack; the user should deny all requests and report the incident to the security team so the account can be investigated.
C) This is a phishing attack; the user should click the link in the notifications to verify their identity and stop the requests.
D) This is a brute-force attack against the MFA system; the user should disable MFA temporarily until the attack subsides.
*   **Correct Answer:** B) This is an MFA fatigue (push bombing) attack; the user should deny all requests and report the incident to the security team so the account can be investigated.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* While the attacker clearly possesses the user's password (triggering the MFA prompts), the specific attack pattern of sending repeated push notifications to overwhelm the user into approving is called MFA fatigue or push bombing — not credential stuffing, which refers to replaying leaked credentials at scale across many sites.
    *   *Why C is incorrect:* MFA push notifications do not contain links — they are approve/deny prompts sent by the authenticator app. Clicking a link in a separate message claiming to be an MFA notification would itself be a phishing action and should never be done.
    *   *Why D is incorrect:* Disabling MFA removes the only remaining barrier protecting the account — the attacker already has the password. Disabling MFA would grant the attacker immediate access. MFA must remain enabled and the account must be investigated, not weakened.

---

**Question 6**
A company deploys hardware FIDO2 security keys as the second factor for all remote access. An attacker sets up a convincing phishing site that proxies the real login page in real time, capturing the user's username, password, and MFA code as the user types them, then replaying those credentials immediately to authenticate to the real site. Why does this real-time phishing relay attack fail against FIDO2 keys but succeed against TOTP codes?

A) FIDO2 keys are physically larger and cannot be used on mobile devices where phishing links are typically clicked.
B) FIDO2 cryptographic responses are bound to the specific origin domain of the relying party, so a response generated for the phishing domain is not valid for the legitimate domain.
C) TOTP codes are longer than FIDO2 responses and therefore take longer for the attacker to relay before they expire.
D) FIDO2 requires a PIN in addition to the hardware key, which the attacker cannot capture from the phishing site.

* **Correct Answer:** B) FIDO2 cryptographic responses are bound to the specific origin domain of the relying party, so a response generated for the phishing domain is not valid for the legitimate domain.
* **Distractor Analysis:**
  * *Why A is incorrect:* FIDO2 keys are available in multiple form factors including USB-A, USB-C, and NFC, and work on mobile devices. Physical size is not a security property.
  * *Why C is incorrect:* TOTP codes are typically six digits — not longer than a FIDO2 cryptographic response. The vulnerability of TOTP to real-time phishing relay is due to short validity windows being exploitable in real-time, not code length.
  * *Why D is incorrect:* While many FIDO2 keys support optional PINs, the anti-phishing property is provided by origin binding — the cryptographic challenge-response is computed using the relying party's origin, making it specific to that domain. PIN capture is not the relevant protective mechanism here.

---

**Question 7**
An organization uses Kerberos authentication within its Active Directory domain. A user authenticates to the domain at morning logon and receives a Ticket Granting Ticket (TGT). Two hours later, the user accesses a file share on a server in the same domain. What does the user's workstation present to the file server to prove authentication?

A) The user's NTLM hash, retrieved from the Windows credential cache
B) A service ticket obtained from the KDC using the TGT, specific to the file server service
C) The original TGT, which the file server validates directly
D) The user's Kerberos password hash, encrypted with the file server's key

* **Correct Answer:** B) A service ticket obtained from the KDC using the TGT, specific to the file server service
* **Distractor Analysis:**
  * *Why A is incorrect:* Kerberos, not NTLM, is the default authentication protocol in modern Active Directory. NTLM hashes are used in NTLM challenge-response, not in Kerberos ticket flows.
  * *Why C is incorrect:* The TGT is never presented to a service — it is presented only to the Key Distribution Center (KDC) to request service tickets. The TGT is encrypted with the KDC's key and cannot be validated by the file server.
  * *Why D is incorrect:* In Kerberos, passwords are not transmitted during service access. The user's long-term key is used only during the initial TGT request — subsequent resource access uses time-limited service tickets, not password hashes.

---

**Question 8**
A company's SSO deployment uses SAML 2.0. An internal security audit finds that the Service Provider (SP) trusts SAML assertions from the Identity Provider (IdP) without validating the XML signature on the assertion. A penetration tester intercepts a valid SAML assertion and modifies the NameID element to change the authenticated username to an administrator account. What type of attack is this, and what control prevents it?

A) A replay attack; prevented by requiring HTTPS for all SAML traffic
B) A SAML assertion injection attack; prevented by the SP validating the IdP's digital signature on every assertion
C) A session hijacking attack; prevented by enabling SAML artifact binding
D) A credential stuffing attack; prevented by enforcing account lockout at the IdP

* **Correct Answer:** B) A SAML assertion injection attack; prevented by the SP validating the IdP's digital signature on every assertion
* **Distractor Analysis:**
  * *Why A is incorrect:* A replay attack reuses a captured valid assertion — this attack modifies the assertion content. HTTPS encrypts the assertion in transit but does not protect against modification of the assertion content if the SP does not validate the XML signature.
  * *Why C is incorrect:* Artifact binding sends only a reference (artifact) to the assertion rather than the full XML, which reduces interception risk, but the core protection against content modification is signature validation. Artifact binding alone does not prevent a compromised SP-side assertion from being accepted without signature checking.
  * *Why D is incorrect:* Credential stuffing targets password authentication. This attack manipulates the SAML assertion XML and does not involve password guessing or authentication credentials.

---

**Question 9**
An organization deploys TOTP (Time-Based One-Time Password) as the second authentication factor. Each TOTP code is valid for 30 seconds. An attacker conducts a real-time phishing attack: they host a fake login portal, the victim enters their credentials including the current TOTP code, and the attacker immediately relays those credentials to the real site. Why can TOTP codes be compromised this way, and what authenticator type is resistant to this attack?

A) TOTP codes are too short; a longer code would prevent relay. Resistance comes from biometric second factors.
B) TOTP codes are time-limited but not origin-bound; within their validity window they can be relayed. FIDO2 hardware keys are resistant because their responses are bound to the relying party origin.
C) TOTP codes use symmetric keys that the attacker can extract from the authenticator app. Hardware tokens with asymmetric keys are resistant.
D) TOTP codes are transmitted in plaintext; encrypting them prevents relay attacks. FIDO2 provides this encryption.

* **Correct Answer:** B) TOTP codes are time-limited but not origin-bound; within their validity window they can be relayed. FIDO2 hardware keys are resistant because their responses are bound to the relying party origin.
* **Distractor Analysis:**
  * *Why A is incorrect:* Code length is not the vulnerability. A longer TOTP code would still be replayable within its validity window. Biometrics can also be phished through a relay proxy if the authentication result (not the biometric data itself) is what is relayed.
  * *Why C is incorrect:* TOTP keys are secret seed values stored in the authenticator app — the attacker in this scenario is not extracting app secrets. The relay attack works by capturing the valid code and replaying it within its 30-second window. FIDO2 resistance is due to origin binding, not key type.
  * *Why D is incorrect:* TOTP codes are transmitted over HTTPS in modern implementations and are not typically in plaintext. The vulnerability is the origin-blindness of the OTP, not the transmission security.

---

**Question 10**
An organization's SSO solution uses OIDC (OpenID Connect) for authentication. The application developer stores the ID token in the browser's localStorage and uses the email claim from the token to identify the logged-in user without further server-side validation. A security review flags this implementation. What is the PRIMARY security risk?

A) localStorage is encrypted by the browser and attackers cannot read the token
B) The email claim can be modified by any user with JavaScript access because localStorage is accessible via the browser console, and the application trusts the token claims without server-side verification of the token signature
C) OIDC ID tokens do not contain email claims and the developer is using an incorrect claim
D) Storing tokens in localStorage is required by the OIDC specification and the security review is incorrect

* **Correct Answer:** B) The email claim can be modified by any user with JavaScript access because localStorage is accessible via the browser console, and the application trusts the token claims without server-side verification of the token signature
* **Distractor Analysis:**
  * *Why A is incorrect:* localStorage is NOT encrypted — it is accessible to any JavaScript running on the same origin, including injected scripts in a cross-site scripting (XSS) attack. This makes token theft possible.
  * *Why C is incorrect:* OIDC ID tokens typically do include email claims (standard claim name: `email`) when the email scope is requested. The developer's use of the email claim is not incorrect per se.
  * *Why D is incorrect:* The OIDC specification does not require localStorage — many implementations use HttpOnly cookies or server-side session stores to protect tokens from JavaScript access. Storing tokens in localStorage is a developer choice with security implications, not a specification requirement.

---

**Question 11**
A company wants to allow employees to use their work identity to log into a third-party SaaS project management tool without creating separate accounts. The SaaS vendor supports both SAML 2.0 and OIDC. The company's IAM team notes that their current identity provider (IdP) issues JWT-format tokens. Which integration protocol aligns best with this infrastructure and why?

A) SAML 2.0, because it provides XML assertions that are more secure than JWT tokens
B) OIDC, because it is built on OAuth 2.0 and uses JWT-format ID tokens natively, aligning with the IdP's existing token format
C) OAuth 2.0, because delegated authorization is the correct model for SSO federation
D) Kerberos, because the company's IdP already issues ticket-format tokens

* **Correct Answer:** B) OIDC, because it is built on OAuth 2.0 and uses JWT-format ID tokens natively, aligning with the IdP's existing token format
* **Distractor Analysis:**
  * *Why A is incorrect:* SAML 2.0 uses XML assertions, not JWT. If the IdP issues JWTs, a SAML integration would require additional transformation layers. XML assertions are not inherently more or less secure than JWT — security depends on correct implementation of signature validation.
  * *Why C is incorrect:* OAuth 2.0 provides authorization (delegated access to resources) but not authentication — it does not issue identity claims about the authenticated user. OIDC adds the identity layer on top of OAuth 2.0. For SSO federation where the application needs to know who the user is, OIDC is the correct choice.
  * *Why D is incorrect:* Kerberos is a ticket-based protocol for internal Active Directory authentication, not for cross-organizational web SSO. JWT tokens from an IdP are not Kerberos tickets — they are different formats and protocols entirely.

---

**Question 12**
A bank requires tellers to use a smart card containing a digital certificate for workstation logon. The smart card is inserted into a reader, and the teller enters a PIN. This is an example of which authentication concept?

A) Two-step verification using two "something you know" factors — the certificate and the PIN
B) Multi-factor authentication combining "something you have" (smart card) and "something you know" (PIN)
C) Single-factor authentication because both elements are presented at the same workstation
D) Certificate-only authentication because the PIN simply unlocks the card but is not verified by the domain

* **Correct Answer:** B) Multi-factor authentication combining "something you have" (smart card) and "something you know" (PIN)
* **Distractor Analysis:**
  * *Why A is incorrect:* A digital certificate on a smart card is not "something you know" — it is "something you have." The certificate material is stored on the physical card, and possession of the card is the have factor.
  * *Why C is incorrect:* MFA is defined by the factor categories involved, not by the physical location where they are presented. Using two different factor categories at the same workstation is still MFA.
  * *Why D is incorrect:* Smart card PINs serve a dual purpose: they unlock the private key material on the card AND the PIN may be verified as part of the authentication chain (depending on implementation). Regardless, the combination of physical card possession and PIN knowledge constitutes MFA.

---

**Question 13**
An organization's help desk receives calls from users who are locked out of their accounts after entering incorrect passwords. Analysis shows the lockouts occur within a three-minute window at approximately 8:00 AM, affecting fifteen to twenty accounts per day with no geographic pattern. Which attack pattern does this BEST describe?

A) Brute force — the attacker is systematically trying all password combinations against individual accounts
B) Password spraying — the attacker is trying one or a few common passwords across many accounts, triggering lockout thresholds
C) Credential stuffing — the attacker is replaying known username/password pairs from a data breach
D) Dictionary attack — the attacker is running a wordlist attack against offline credential hashes

* **Correct Answer:** B) Password spraying — the attacker is trying one or a few common passwords across many accounts, triggering lockout thresholds
* **Distractor Analysis:**
  * *Why A is incorrect:* A brute force attack against a single account would quickly trigger lockout on that one account. The pattern described — many accounts locked in a short window — is not consistent with per-account brute force.
  * *Why C is incorrect:* Credential stuffing replays previously breached specific username/password pairs, typically resulting in some successful logins rather than mass lockouts. The mass lockout pattern suggests the wrong password is being tried at scale, not known credential pairs.
  * *Why D is incorrect:* A dictionary attack operates against offline credential hashes (e.g., a stolen password database) — it does not trigger online account lockouts because it occurs locally without making authentication requests to the live system.

---

**Question 14**
A security architect is evaluating whether to require users to re-authenticate when accessing highly sensitive financial data, even if they are already logged into the corporate SSO session. This requirement is called what, and what authentication standard defines levels of assurance for these decisions?

A) Step-up authentication; defined by NIST SP 800-63B Authenticator Assurance Levels (AAL1, AAL2, AAL3)
B) Re-authentication; defined by the OAuth 2.0 RFC 6749 token refresh requirements
C) Session token renewal; defined by SAML 2.0 assertion validity periods
D) Continuous authentication; defined by the Zero Trust Architecture principle of never trust, always verify

* **Correct Answer:** A) Step-up authentication; defined by NIST SP 800-63B Authenticator Assurance Levels (AAL1, AAL2, AAL3)
* **Distractor Analysis:**
  * *Why B is incorrect:* OAuth 2.0 defines token refresh for maintaining authorization sessions — it is an authorization framework, not an assurance level standard for authentication strength decisions. Re-authentication for sensitive resources is an authentication decision, not an OAuth token lifecycle event.
  * *Why C is incorrect:* SAML assertion validity periods define how long an issued assertion remains valid for session maintenance — they do not define when applications should require elevated re-authentication. Assertion expiry is a session timeout mechanism.
  * *Why D is incorrect:* Continuous authentication is a broader zero-trust concept involving ongoing risk-based verification throughout a session. Step-up authentication is the specific term for requiring additional authentication factors when a user attempts to access a higher-risk resource during an existing session.

---

**Question 15**
An organization's biometric door lock system is configured to prioritize security at all costs. As a result, the system's sensitivity is set very high. What is the likely consequence of this configuration, and which biometric error rate metric describes the resulting problem?

A) Impostors will be incorrectly accepted more often; this is measured by a high False Acceptance Rate (FAR)
B) Legitimate users will be incorrectly rejected more often; this is measured by a high False Rejection Rate (FRR)
C) The Crossover Error Rate will decrease, indicating the system is performing optimally
D) The system will require biometric re-enrollment from all users due to data corruption

* **Correct Answer:** B) Legitimate users will be incorrectly rejected more often; this is measured by a high False Rejection Rate (FRR)
* **Distractor Analysis:**
  * *Why A is incorrect:* Increasing sensitivity (making the system more discriminating) reduces the FAR — fewer impostors are accepted. The tradeoff is that legitimate users whose biometrics do not exactly match the stored template are also rejected more often, increasing the FRR.
  * *Why C is incorrect:* The CER is the point where FAR equals FRR and represents the crossover of the two error curves — it is a characteristic of the biometric system hardware and template quality. Adjusting sensitivity changes the operating point on the FAR/FRR curve but does not change the CER of the underlying system.
  * *Why D is incorrect:* Adjusting sensitivity thresholds is a software configuration change that affects how strictly biometric samples are matched. It does not corrupt stored templates or require re-enrollment.

---

### Question 16

An organization deploys a password manager for all employees. During a security review, the team debates how the password manager should store the master password used to encrypt the vault. Which storage approach is MOST secure?

A) Store the master password in plaintext in the password manager's database so it can be compared directly during login.
B) Store the master password as an unsalted SHA-256 hash to allow fast comparison without storing the plaintext.
C) Never store the master password at all — derive the vault encryption key from the master password using a memory-hard KDF (such as Argon2 or bcrypt) so the vault can only be unlocked by providing the correct password at runtime.
D) Encrypt the master password with AES-256 and store the ciphertext alongside the AES key in the database.

* **Correct Answer:** C) Never store the master password at all — derive the vault encryption key from the master password using a memory-hard KDF (such as Argon2 or bcrypt) so the vault can only be unlocked by providing the correct password at runtime.
* **Distractor Analysis:**
  * *Why A is incorrect:* Storing the master password in plaintext means any database breach instantly exposes every user's vault master credential. There is no scenario in which the master password of a password manager should be stored in recoverable form.
  * *Why B is incorrect:* An unsalted SHA-256 hash is fast to compute, making it vulnerable to GPU-accelerated dictionary and rainbow table attacks. Without a unique salt and a memory-hard function, identical master passwords produce identical hashes across users, enabling precomputed attacks.
  * *Why D is incorrect:* Encrypting the master password and storing the encryption key in the same database provides no protection — an attacker with database access has both the ciphertext and the key. This is equivalent to obscurity, not security.

---

### Question 17

A user at a company that uses SSO via SAML 2.0 closes their laptop lid at lunch. When they return and open the lid, they are immediately prompted to re-authenticate with their password and MFA before the session resumes — even though the laptop was only idle for 25 minutes. The administrator explains this behavior is by design. Which security control produces this behavior?

A) The SAML IdP has configured an assertion validity period shorter than the idle session duration, forcing re-authentication when the assertion expires.
B) The laptop hard disk is encrypted with BitLocker, which locks the drive on lid close and requires re-authentication to decrypt.
C) The VPN client disconnected during lid close and requires re-authentication to reconnect.
D) The SSO session cookie expired because it was configured with a Secure flag that clears it on network change.

* **Correct Answer:** A) The SAML IdP has configured an assertion validity period shorter than the idle session duration, forcing re-authentication when the assertion expires.
* **Distractor Analysis:**
  * *Why B is incorrect:* BitLocker full-disk encryption locks access to the encrypted drive but does not by itself produce an MFA prompt for SSO session resumption at the application layer — BitLocker unlocks the OS, not the federated identity session.
  * *Why C is incorrect:* A VPN reconnect prompt would request VPN credentials or certificate authentication — it would not produce an SSO re-authentication flow with password and MFA specific to the identity provider.
  * *Why D is incorrect:* The Secure flag on a cookie restricts the cookie to HTTPS connections and prevents transmission over HTTP — it does not cause the cookie to expire or clear on network change or lid close. Session expiration based on timeout is controlled by cookie Max-Age or Expires attributes, not the Secure flag.

---

### Question 18

A company is evaluating whether to adopt passkeys (FIDO2/WebAuthn) as a replacement for passwords. A manager asks what happens if a user loses the device that holds their passkey. Which statement BEST describes the recovery scenario and its security implications?

A) Passkeys are permanently lost when a device is lost — the user must create a new account because there is no recovery mechanism.
B) The user can recover access through account recovery mechanisms (such as a backup code, secondary email, or synced passkey in a platform authenticator) — the security implication is that the recovery path becomes the weakest link and must be protected with strong authentication.
C) Passkeys are stored on the authentication server, so the user simply registers a new device and the old passkey is automatically transferred.
D) The lost device's passkey remains active and allows anyone who finds the device to authenticate without a PIN or biometric because passkeys do not support device unlock requirements.

* **Correct Answer:** B) The user can recover access through account recovery mechanisms (such as a backup code, secondary email, or synced passkey in a platform authenticator) — the security implication is that the recovery path becomes the weakest link and must be protected with strong authentication.
* **Distractor Analysis:**
  * *Why A is incorrect:* Passkeys do not require a new account on device loss. Modern implementations support recovery via backup authentication factors, synced credentials in platform clouds (e.g., iCloud Keychain, Google Password Manager), or pre-registered recovery codes. Account destruction on device loss would be impractical for enterprise deployment.
  * *Why C is incorrect:* Passkeys are based on asymmetric cryptography — the private key is stored on the user's device (or in a synced platform authenticator) and the server stores only the public key. The server cannot transfer the private key material to a new device because it never possesses it.
  * *Why D is incorrect:* FIDO2 device-bound passkeys require local authentication (PIN, biometric, or device unlock) before the private key is used to sign the authentication challenge. A found device cannot be used to authenticate without the local unlock credential.

---

### Question 19

An organization's SSO implementation uses OAuth 2.0 with the Authorization Code flow. A security engineer discovers that the application does not validate the `state` parameter returned in the authorization callback. Which attack does the missing `state` validation enable?

A) Token replay attack — an attacker replays a captured authorization code to obtain a new access token.
B) CSRF on the OAuth callback — an attacker tricks the user's browser into completing an authorization flow initiated by the attacker, linking the victim's account to the attacker's credentials.
C) JWT forgery — an attacker modifies the access token claims because the state parameter signs the token.
D) Open redirect — the missing state causes the authorization server to redirect to an attacker-controlled URL.

* **Correct Answer:** B) CSRF on the OAuth callback — an attacker tricks the user's browser into completing an authorization flow initiated by the attacker, linking the victim's account to the attacker's credentials.
* **Distractor Analysis:**
  * *Why A is incorrect:* Token replay attacks target access tokens or authorization codes after they are issued — they are mitigated by short token lifetimes and one-time-use codes. The `state` parameter is not involved in preventing code replay; PKCE (Proof Key for Code Exchange) addresses code interception.
  * *Why C is incorrect:* The `state` parameter is an opaque value used to correlate the authorization request with the callback — it is not used to sign JWT tokens. JWT integrity is protected by the token signature (using the authorization server's private key), not the state parameter.
  * *Why D is incorrect:* Open redirects in OAuth are mitigated by strict redirect URI validation at the authorization server — requiring exact match of the registered redirect URI. The `state` parameter is used for CSRF protection, not redirect URI enforcement.

---

### Question 20

A company deploys a TOTP-based MFA solution. The help desk reports that users in a remote office are experiencing frequent "invalid code" errors even when entering the code immediately after it generates. Investigation reveals the remote office workstations have a system clock that is approximately 90 seconds ahead of the NTP server. Why does clock drift cause TOTP failures, and what is the recommended fix?

A) TOTP codes are encrypted with a time-based key — clock drift causes decryption to fail because the wrong key is derived. The fix is to re-enroll all affected users.
B) TOTP is computed using the current Unix timestamp divided into 30-second windows — a 90-second drift places the client in a different time window than the server, generating a code the server does not expect. The fix is to synchronize all workstation clocks to the organization's NTP server and optionally enable a server-side time-window tolerance of ±1 step.
C) TOTP codes are one-time-use hashes of the user's password — clock drift means the password hash was computed at the wrong time. The fix is to reset all affected user passwords.
D) TOTP codes expire after exactly 10 seconds — any system latency over 10 seconds causes failure regardless of clock synchronization.

* **Correct Answer:** B) TOTP is computed using the current Unix timestamp divided into 30-second windows — a 90-second drift places the client in a different time window than the server, generating a code the server does not expect. The fix is to synchronize all workstation clocks to the organization's NTP server and optionally enable a server-side time-window tolerance of ±1 step.
* **Distractor Analysis:**
  * *Why A is incorrect:* TOTP codes are not encrypted — they are computed using HMAC-SHA1 (per RFC 6238) applied to the shared secret seed and the current time step counter. There is no encryption key to derive from a timestamp, and re-enrollment would not resolve a clock synchronization problem.
  * *Why C is incorrect:* TOTP is entirely independent of the user's password — it uses a shared secret seed established during enrollment, not a password hash. Password resets would have no effect on TOTP code generation or validation.
  * *Why D is incorrect:* The standard TOTP time step is 30 seconds (RFC 6238), not 10 seconds. Most TOTP implementations also accept codes from the immediately adjacent time windows (±1 step = ±30 seconds) to accommodate minor clock skew. A 90-second drift exceeds this tolerance, which explains the failures described.
