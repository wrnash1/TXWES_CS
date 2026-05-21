# Quiz: Module 09 - Entra Authentication and MFA

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Entra ID feature allows you to enforce security policies based on signals like user location or device compliance state?

* A) Multi-Factor Authentication
* B) Conditional Access
* C) Role-Based Access Control
* D) Privileged Identity Management
* **Correct Answer:** B) Conditional Access implements "if-then" policies (e.g., if logging in from outside the corporate network, require MFA).
* **Distractor Analysis:**
  * *Why correct:* Conditional Access evaluates signals (location, device state, user risk) and applies access controls based on those conditions.
  * *Why A is incorrect:* MFA is the authentication mechanism — Conditional Access is the policy that decides when MFA is triggered.

---

**Question 2**
Which of the following most accurately describes **Single Sign-On (SSO)** in the context of Microsoft Entra ID?

* A) An authentication capability that allows users to sign in once with a single set of credentials and gain access to multiple integrated applications without re-entering their password for each one.
* B) A method of requiring users to provide two or more verification factors before accessing cloud resources.
* C) A policy that evaluates user location, device compliance, and risk level to decide whether to allow, block, or require additional verification for a sign-in attempt.
* D) A synchronization tool that copies on-premises Active Directory identities to Microsoft Entra ID for hybrid identity scenarios.
* **Correct Answer:** A) SSO allows users to authenticate once and access multiple applications — Entra ID issues tokens honored by all integrated services.
* **Distractor Analysis:**
  * *Why A is correct:* SSO's defining feature is single authentication for multiple application access, reducing password fatigue and improving security through centralized identity control.
  * *Why B is incorrect:* That describes Multi-Factor Authentication (MFA), not SSO.
  * *Why C is incorrect:* That describes Conditional Access policies, not SSO.
  * *Why D is incorrect:* That describes Microsoft Entra Connect (directory synchronization), not SSO.

---

**Question 3**
A security team needs to ensure that users accessing the Azure portal from unmanaged, personal devices are always required to complete MFA, while users on corporate-managed devices on the internal network are not prompted. Which feature implements this requirement?

* A) Per-user MFA with always-on enforcement in Entra ID settings
* B) Conditional Access policy with device compliance and network location as conditions
* C) Azure RBAC with MFA-only role assignments
* D) Entra ID Password Protection with banned password lists
* **Correct Answer:** B) A Conditional Access policy can use device compliance status and named locations (corporate network) as conditions, requiring MFA only when those conditions are not met.
* **Distractor Analysis:**
  * *Why B is correct:* Conditional Access's "if-then" logic handles exactly this scenario: if unmanaged device or outside corporate network, then require MFA.
  * *Why A is incorrect:* Per-user always-on MFA applies to all sign-ins regardless of device or location — it cannot differentiate based on device compliance.
  * *Why C is incorrect:* RBAC controls what users can do after authentication — it does not control authentication requirements.
  * *Why D is incorrect:* Password Protection enforces password complexity rules and blocks banned passwords — it does not trigger MFA based on device state.

---

**Question 4**
After a user's credentials are compromised, security administrators need to immediately prevent that user from accessing all Microsoft 365 and Azure applications, including all active sessions. What is the most effective immediate action?

* A) Reset the user's password in the on-premises Active Directory
* B) Disable the user's account in Microsoft Entra ID and revoke all active refresh tokens
* C) Remove the user from all security groups in Entra ID
* D) Delete all Conditional Access policies that apply to the user
* **Correct Answer:** B) Disabling the Entra ID account and revoking refresh tokens immediately blocks all new sign-ins and invalidates existing sessions across all Entra ID-integrated applications.
* **Distractor Analysis:**
  * *Why B is correct:* Disabling the Entra ID account stops new authentications; revoking refresh tokens (via "Revoke sessions" in the portal) invalidates existing access across all connected apps simultaneously.
  * *Why A is incorrect:* Resetting the on-premises AD password only helps if Entra Connect is syncing credentials — active cloud sessions using existing tokens would remain valid.
  * *Why C is incorrect:* Removing from groups removes permissions but does not invalidate active authentication sessions or prevent sign-in.
  * *Why D is incorrect:* Deleting Conditional Access policies removes access controls — this would make the environment less secure, not more.

---

**Question 5**
Which statement correctly describes the relationship between MFA and Conditional Access in Microsoft Entra ID?

* A) MFA replaces Conditional Access — once MFA is enabled, no Conditional Access policies are needed.
* B) MFA is an authentication method; Conditional Access is the policy engine that determines when and under what conditions MFA is required.
* C) Conditional Access is only available when MFA is disabled — the two features cannot be used simultaneously.
* D) MFA requires Entra ID P2 licensing; Conditional Access is available in the Free tier only.
* **Correct Answer:** B) MFA is the authentication method (second factor); Conditional Access is the policy engine controlling when MFA is triggered based on evaluated signals.
* **Distractor Analysis:**
  * *Why B is correct:* MFA and Conditional Access are complementary. Conditional Access evaluates conditions and can require MFA as a grant control when conditions are met.
  * *Why A is incorrect:* MFA and Conditional Access serve different functions and are both needed — MFA provides the second factor; Conditional Access applies context-based rules.
  * *Why C is incorrect:* MFA and Conditional Access are designed to work together — Conditional Access commonly uses MFA as its enforcement action.
  * *Why D is incorrect:* The licensing is reversed — Conditional Access (policy-driven MFA) requires Entra ID P1 or higher; per-user MFA is available in the Free tier.
