# Quiz: Module 06 — Identity and Access Management

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Questions mirror the style and difficulty of CompTIA Security+ SY0-701 exam items.

---

### Question 1

A user authenticates to a corporate portal by providing a password and then approving a push notification on their smartphone. Which authentication factor categories are being used?

A. Something you know and something you are

B. Something you know and something you have

C. Something you have and something you do

D. Something you are and something you have

**Correct Answer:** B

**Explanation:** A password is "something you know." Approving a push notification on a registered smartphone is "something you have" — possession of the registered device. This combination satisfies MFA with two different factor categories. Biometrics ("something you are") are not involved. Behavioral factors ("something you do") are not involved.

---

### Question 2

A company wants employees to use their Active Directory credentials to log in to a cloud-hosted SaaS application without requiring a separate username and password. The SaaS vendor supports SAML 2.0. Which architectural component issues the SAML assertion to the SaaS application?

A. Service Provider

B. Registration Authority

C. Identity Provider

D. Certificate Authority

**Correct Answer:** C

**Explanation:** In a SAML federation, the Identity Provider (IdP) authenticates the user against Active Directory and issues the signed SAML assertion. The Service Provider (SP) is the SaaS application — it receives and validates the assertion but does not issue it. The Registration Authority and Certificate Authority are PKI components, not SAML components.

---

### Question 3

A mobile app developer needs to allow users to grant the app access to their Google Drive files without sharing their Google password with the app. Which protocol is MOST appropriate for implementing this delegated access?

A. SAML 2.0

B. Kerberos

C. LDAP

D. OAuth 2.0

**Correct Answer:** D

**Explanation:** OAuth 2.0 is an authorization framework specifically designed for delegated access scenarios — allowing a third-party application to access resources on behalf of a user without sharing the user's credentials. SAML is designed for enterprise web SSO using XML assertions, not mobile app delegation. Kerberos is an enterprise ticket-based authentication protocol. LDAP is a directory query protocol.

---

### Question 4

A penetration tester runs a tool that extracts NTLM credential hashes from memory on a compromised Windows workstation. The tester then uses these hashes to authenticate to other servers on the network without cracking them. Which attack technique is being demonstrated?

A. Credential stuffing

B. Pass-the-Hash

C. Kerberoasting

D. Golden Ticket

**Correct Answer:** B

**Explanation:** Pass-the-Hash exploits the fact that NTLM authentication accepts the hash directly as the authentication credential — the plaintext password is never needed. Credential stuffing uses known username/password combinations from breaches. Kerberoasting extracts and cracks Kerberos service ticket hashes. A Golden Ticket attack forges Kerberos TGTs using the KRBTGT account hash.

---

### Question 5

An access control system grants permissions based on the user's department, their security clearance level, the classification of the data being requested, and the time of day. Which access control model BEST describes this system?

A. DAC

B. MAC

C. RBAC

D. ABAC

**Correct Answer:** D

**Explanation:** ABAC (Attribute-Based Access Control) makes access decisions based on attributes of the user, the resource, and the environment — exactly the combination described. RBAC uses organizational roles, not multiple contextual attributes. MAC uses centrally assigned classification labels on both subjects and objects. DAC leaves access decisions to the resource owner.

---

### Question 6

A company discovers that a former IT administrator who resigned three months ago still has an active account with domain admin privileges. The account has been used twice in the past month. Which IAM process failure PRIMARILY allowed this situation to occur?

A. Lack of multi-factor authentication

B. Inadequate offboarding procedures

C. Missing access reviews

D. Failure to implement role-based access control

**Correct Answer:** B

**Explanation:** Offboarding procedures — the immediate revocation of all access upon an employee's departure — are the primary control that prevents departed employees from retaining access. While access reviews (option C) might eventually detect the issue, they are a detective control and are secondary to the preventive control of offboarding. MFA and RBAC do not address accounts that remain active after departure.

---

### Question 7

Which LDAP port number provides encrypted communication by default?

A. 389

B. 443

C. 636

D. 3268

**Correct Answer:** C

**Explanation:** LDAP uses port 389 for cleartext communication. LDAPS (LDAP over TLS) uses port 636 and provides encrypted communication. Port 443 is HTTPS. Port 3268 is the Global Catalog port in Active Directory.

---

### Question 8

A developer implements a login system where users can authenticate with their corporate credentials via OAuth 2.0. After testing, the security team notes that the application does not know who the user is — only that they have been granted access. What is MISSING from the implementation?

A. A SAML assertion

B. An LDAP bind

C. OpenID Connect (OIDC) for identity claims

D. A Kerberos service ticket

**Correct Answer:** C

**Explanation:** OAuth 2.0 provides authorization (the application can access resources on behalf of the user) but does not inherently provide the user's identity. OpenID Connect is an identity layer built on top of OAuth 2.0 that provides an ID token containing verified claims about who the user is. Without OIDC, the application has an access token but no reliable way to identify the authenticated user.

---

### Question 9

An organization implements a PAM solution where IT administrators must request elevated access for a specific task, and that access is automatically revoked after the task window expires. Which PAM control does this describe?

A. Privileged Access Workstation

B. Password Vaulting

C. Just-in-Time Access

D. Session Recording

**Correct Answer:** C

**Explanation:** Just-in-Time (JIT) Access provides temporary privilege elevation for a specific task or time window and automatically revokes it when the window expires. This eliminates persistent privileged credentials that represent a standing target. PAWs are hardened devices for admin work. Password vaulting stores and rotates credentials. Session recording captures privileged session activity.

---

### Question 10

An employee moves from the Finance department to the HR department. Six months later, an access review reveals the employee still has Finance system access in addition to newly granted HR access. Which term BEST describes this IAM condition?

A. Privilege escalation

B. Excessive entitlement accumulation

C. Separation of duties violation

D. Insider threat

**Correct Answer:** B

**Explanation:** Excessive entitlement accumulation (also called privilege creep or access accumulation) occurs when users retain access from previous roles as they move within an organization, resulting in permissions that exceed what their current role requires. While this violates least privilege, the specific term for the pattern of accumulation over time is privilege creep or entitlement accumulation. Privilege escalation refers to actively gaining additional permissions beyond what was granted. Separation of duties is violated when one person can complete a sensitive transaction alone — that is a different condition.

---

Module 06 Quiz — End
