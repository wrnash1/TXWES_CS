# Quiz: Module 12 - Identity Threat Detection – IAM and Privileged Access
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

**Question 1**
What is the primary security risk associated with orphaned accounts in an enterprise Active Directory environment?

*   A) They consume excessive storage space in the directory database and slow down authentication queries
*   B) They remain active after the associated employee has left the organization, providing unmonitored access points that attackers or former insiders can exploit
*   C) They prevent new user accounts from being created because they occupy unique username slots in the directory namespace
*   D) They cause IP address conflicts on the network when the former employee's workstation is reassigned to a new user
*   **Correct Answer:** B) They remain active after the associated employee has left the organization, providing unmonitored access points that attackers or former insiders can exploit.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Storage consumption and query performance are not security risks associated with orphaned accounts. The risk is unauthorized access, not resource overhead.
    *   *Why B is correct:* Orphaned accounts retain all the permissions assigned to the departed employee and remain valid credentials in the directory. A disgruntled former employee who remembers their credentials, or an attacker who obtains them through credential stuffing or phishing, can authenticate without triggering any active user suspicion. Regular access reviews to identify and disable orphaned accounts are a required IAM hygiene control.
    *   *Why C is incorrect:* Directory systems support account disablement without releasing the username; username namespace conflicts are not a security concern associated with orphaned accounts.
    *   *Why D is incorrect:* IP address conflicts are a network configuration issue unrelated to directory account lifecycle management.

---

**Question 2**
In identity threat detection, which of the following most accurately defines **multifactor authentication (MFA) gaps**?

*   A) The latency introduced when an authentication server must contact a secondary MFA provider before granting access, causing delays in the user login experience
*   B) Conditions in which MFA is not enforced for high-risk access scenarios — such as privileged account logins, remote access, or cloud management plane access — leaving credential-only authentication as the only barrier against attackers who have obtained valid passwords
*   C) A configuration error in the RADIUS server that causes MFA challenges to be sent to the wrong device, resulting in authentication failures for legitimate users
*   D) The window of time between when a TOTP (time-based one-time password) token is generated and when it expires, during which an intercepted token could theoretically be reused
*   **Correct Answer:** B) Conditions in which MFA is not enforced for high-risk access scenarios — such as privileged account logins, remote access, or cloud management plane access — leaving credential-only authentication as the only barrier against attackers who have obtained valid passwords.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Authentication latency is a performance issue, not a security gap. MFA gaps refer to missing enforcement of MFA, not to timing delays in the MFA flow.
    *   *Why B is correct:* MFA gaps occur when MFA is either not deployed at all for certain access paths or is deployed inconsistently — enforced for standard users but not for administrators, or enforced for the web portal but not for VPN. When an attacker obtains valid credentials through phishing or credential stuffing, MFA gaps mean there is no second barrier. CySA+ consistently presents MFA enforcement as the primary recommended control when a credential-based attack scenario is described.
    *   *Why C is incorrect:* A RADIUS misconfiguration causing MFA challenges to route incorrectly is an operational fault that prevents legitimate authentication; it is a reliability issue, not an MFA gap security concern.
    *   *Why D is incorrect:* The TOTP validity window is a known design trade-off in time-based OTP systems; it is not what CySA+ means by "MFA gaps." MFA gaps are about the absence of MFA enforcement, not about token replay windows.

---

**Question 3**
A SOC analyst reviews Windows Security Event Logs and finds that a standard help desk user account added itself to the Domain Admins group (Event ID 4728) at 11:43 PM on a Saturday, with no corresponding change management ticket. The account then logged into the domain controller at 11:47 PM (Event ID 4624). Which threat does this activity most strongly indicate?

*   A) A brute-force attack — the attacker is trying multiple passwords against the help desk account to gain access to the domain controller
*   B) Privilege escalation — a compromised help desk account is elevating its own permissions to gain domain administrator access outside authorized change windows
*   C) Lateral movement — the attacker is moving from a compromised workstation to the domain controller using stolen Kerberos tickets
*   D) Phishing — the help desk user received a malicious email that automatically added their account to Domain Admins when opened
*   **Correct Answer:** B) Privilege escalation — a compromised help desk account is elevating its own permissions to gain domain administrator access outside authorized change windows.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A brute-force attack would appear as many Event ID 4625 (failed logon) entries before a successful logon. The described activity shows a group membership change followed by a successful login — indicating already-valid credentials being used, not a brute-force attempt.
    *   *Why B is correct:* Event ID 4728 (member added to security-enabled global group) combined with a Domain Admins group change, occurring after hours without a change ticket, is the signature of privilege escalation. The attacker likely compromised the help desk account's credentials and is now self-escalating to domain admin to enable full domain compromise. This maps to MITRE ATT&CK T1078 (Valid Accounts) and T1098 (Account Manipulation).
    *   *Why C is incorrect:* Lateral movement involves using credentials or tokens to authenticate to other systems — moving between hosts. The described activity is about modifying group membership on the same domain, which is privilege escalation, not lateral movement to a new host.
    *   *Why D is incorrect:* While phishing is a common initial access vector, a phishing email cannot directly modify Active Directory group membership. Group membership changes require authenticated API calls with sufficient privileges — this is a post-compromise privileged action, not an email-triggered automatic change.

---

**Question 4**
An organization's access review identifies a service account used by an automated backup application that has been granted Domain Admin privileges. The backup application only needs read access to specific file shares. Which action best addresses this IAM risk?

*   A) Disable the service account immediately and restore the Domain Admin group to its original membership to eliminate the excessive privilege
*   B) Apply the principle of least privilege — replace the Domain Admin role assignment with a custom role granting only the specific read permissions the backup application requires, and document the change
*   C) Rotate the service account password to a 32-character random value and store it in a PAM vault to prevent the credentials from being used interactively
*   D) Enable MFA on the service account to require a second factor whenever the backup application authenticates to prevent unauthorized use of the over-privileged credential
*   **Correct Answer:** B) Apply the principle of least privilege — replace the Domain Admin role assignment with a custom role granting only the specific read permissions the backup application requires, and document the change.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Disabling the service account would break the backup application, causing a business continuity impact. The correct remediation is to right-size the permissions, not disable the account entirely.
    *   *Why B is correct:* The principle of least privilege requires accounts to have only the minimum permissions necessary for their function. A backup application needs read access to specific shares — not domain admin. Replacing the over-privileged role with a precisely scoped read-only permission eliminates the risk without disrupting the application. Documenting the change maintains audit trail compliance.
    *   *Why C is incorrect:* Password rotation and PAM vaulting are good credential hygiene practices that reduce the risk of credential theft, but they do not address the underlying over-privilege problem. If the account is compromised, the attacker still has Domain Admin access regardless of password strength.
    *   *Why D is incorrect:* MFA is designed for interactive human authentication; service accounts authenticate non-interactively through stored credentials or certificates. MFA cannot be meaningfully applied to automated service account logins and does not reduce the excessive permissions granted to the account.

---

**Question 5**
An organization wants to reduce the risk of privileged account compromise enabling attackers to achieve persistent domain-level access. Which two controls together best achieve this goal?

*   A) Deploy full-disk encryption on all domain controllers and require BitLocker PIN entry at server boot to prevent unauthorized physical access
*   B) Implement a Privileged Access Management (PAM) solution that vaults privileged credentials, enforces just-in-time access with manager approval, and automatically rotates privileged account passwords after each use — combined with SIEM alerting on Event ID 4672 (special privileges assigned) outside approved change windows
*   C) Enforce a 90-day password rotation policy for all standard user accounts and require passwords to meet complexity requirements of at least 12 characters
*   D) Segment the domain controller network subnet using VLANs and restrict inbound firewall rules to permit only required management protocols from authorized administrator workstations
*   **Correct Answer:** B) Implement a PAM solution that vaults privileged credentials, enforces just-in-time access with manager approval, and automatically rotates privileged account passwords after each use — combined with SIEM alerting on Event ID 4672 outside approved change windows.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* BitLocker on domain controllers protects against physical theft of powered-off servers; it does not prevent credential-based remote attacks against running domain controllers or detect privilege escalation by authenticated users.
    *   *Why B is correct:* PAM addresses the core risk — standing privileged access with static credentials that can be stolen and reused — by eliminating persistent privilege (just-in-time access) and rotating credentials after each session. SIEM alerting on Event ID 4672 outside change windows provides the detective layer, alerting analysts when privileged assignments occur outside approved processes. Together these are the most direct preventive and detective controls for privileged account compromise.
    *   *Why C is incorrect:* Standard user password rotation policies address general credential hygiene; they do not specifically target the privileged account compromise risk or provide detection capability for privilege escalation events.
    *   *Why D is incorrect:* VLAN segmentation and firewall restrictions limit which hosts can reach domain controllers, reducing the attack surface for lateral movement — but they do not prevent a legitimately connected administrator workstation with stolen credentials from being used to escalate privileges on the domain.
