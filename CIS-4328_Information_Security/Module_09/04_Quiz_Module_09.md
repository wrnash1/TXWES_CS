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
