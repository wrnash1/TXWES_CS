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

---

### Question 11

A user authenticates to a web application using SAML 2.0. The application never directly handles the user's credentials. Instead, the user is redirected to their organization's identity provider, authenticates there, and a signed XML assertion is returned to the application. Which component is the service provider in this scenario?

A. The organization's Active Directory domain controller

B. The SAML certificate authority that signs the assertion

C. The web application that consumes the SAML assertion to grant access

D. The user's browser, which relays the assertion between parties

**Correct Answer:** C

**Explanation:** In SAML 2.0 federation, the Service Provider (SP) is the application or resource that relies on the Identity Provider (IdP) to authenticate users. The SP trusts and consumes the signed XML assertion. The IdP is the organization's authentication service (e.g., Azure AD, Okta). Active Directory is typically the backend identity store used by the IdP. The browser acts as the user agent relaying assertions but is not a SAML principal.

---

### Question 12

A security architect must choose an MFA method for remote access that is phishing-resistant. Which option meets this requirement?

A. SMS-based one-time password (OTP) sent to the user's registered mobile number

B. TOTP authenticator app generating a six-digit time-based code

C. FIDO2 hardware security key requiring physical presence and cryptographic challenge-response

D. Email-based OTP sent to the user's corporate email address

**Correct Answer:** C

**Explanation:** FIDO2 hardware security keys are phishing-resistant because the cryptographic challenge-response is bound to the specific origin (domain) of the legitimate site. Even if a user is redirected to a phishing site, the key will not produce a valid response for a different origin. SMS OTP is vulnerable to SIM swapping and real-time phishing relay. TOTP codes can be captured and replayed by a phishing proxy in real time. Email OTP requires access to email, which is also phishable.

---

### Question 13

A developer is building a mobile app that needs to access a user's calendar data stored in a third-party cloud service. The user should be able to grant the app access without sharing their cloud service password with the app. Which protocol is designed specifically for this delegated authorization scenario?

A. SAML 2.0

B. Kerberos

C. OAuth 2.0

D. LDAP

**Correct Answer:** C

**Explanation:** OAuth 2.0 is an authorization framework designed for delegated resource access — it allows a user to grant a third-party application limited access to their resources without sharing credentials. The user authenticates directly with the resource server's authorization endpoint and an access token is issued to the app. SAML 2.0 is an authentication federation protocol. Kerberos is a ticket-based authentication protocol for internal networks. LDAP is a directory access protocol, not an authorization delegation framework.

---

### Question 14

An organization implements a Mandatory Access Control (MAC) model for its classified document system. Users are assigned clearance levels and documents are assigned sensitivity labels. Which statement BEST describes how access decisions are made in a MAC system?

A. The resource owner decides who can access their documents by setting permissions on each file.

B. Access is determined by group membership defined in the directory service.

C. The system enforces access based on comparing the user's clearance label to the document's sensitivity label according to a policy defined by the system administrator.

D. Users can delegate their access rights to other users as needed.

**Correct Answer:** C

**Explanation:** In MAC, access decisions are made by the system based on security labels assigned to both subjects (users) and objects (resources), enforced by a central policy. Users cannot override these rules — they cannot grant access they do not hold and cannot modify resource labels. DAC (Discretionary Access Control) allows resource owners to set permissions. RBAC uses group/role membership. MAC is the model used in classified government systems where label-based access is enforced independently of user preference.

---

### Question 15

An attacker uses a technique where, after compromising one workstation, they authenticate to additional systems using credential hashes extracted from memory — without ever knowing the plaintext password. Which attack and which primary defensive control are correctly matched?

A. Pass-the-Hash attack; mitigated by enabling NTLM authentication across the domain

B. Pass-the-Hash attack; mitigated by implementing credential guard and restricting NTLM, combined with Just-in-Time privileged access

C. Kerberoasting; mitigated by requiring strong service account passwords and enabling AES encryption for Kerberos

D. Golden Ticket attack; mitigated by resetting the KRBTGT account password

**Correct Answer:** B

**Explanation:** Pass-the-Hash exploits NTLM authentication by using the captured NTLM hash directly as the credential rather than the password. Windows Credential Guard protects credential material in an isolated memory region, preventing tools like Mimikatz from extracting hashes. Restricting NTLM and enforcing Kerberos reduces the attack surface. JIT access limits the time window during which privileged hashes are valuable. Option A incorrectly recommends enabling NTLM (the vulnerable protocol). Kerberoasting targets Kerberos service tickets, not NTLM hashes. Golden Ticket attacks forge Kerberos TGTs using the KRBTGT hash — different from Pass-the-Hash.

---

### Question 16

An organization implements Role-Based Access Control (RBAC). A new employee joins the Finance team. The IAM administrator creates a new user account and grants the account individually assigned permissions to each Finance system rather than placing the user in the Finance role. Six months later, the employee changes departments and retains all individually assigned permissions. Which RBAC principle was violated from the beginning, and what is the correct approach?

A. The administrator violated the principle of need-to-know; the user should have been given no permissions and asked to request access as needed.

B. The administrator violated the role-assignment model of RBAC; permissions should be assigned to roles, not to individual users, and users should be placed in the appropriate role — making permission changes as simple as role membership updates.

C. The administrator violated separation of duties; a second administrator should have approved every individual permission grant.

D. The administrator violated the MAC model; permissions should be based on security labels, not job function.

**Correct Answer:** B

**Explanation:** RBAC's fundamental principle is that permissions are assigned to roles, and users are assigned to roles — not given direct permissions. This design means that when an employee changes departments, the administrator simply removes the old role and adds the new one; there are no individual permissions to audit and revoke one by one. Assigning permissions directly to users bypasses the role model entirely, creates management complexity, and is a common cause of privilege accumulation. Need-to-know and separation of duties are valid principles but are not the RBAC violation described. MAC uses security labels, not role membership.

---

### Question 17

A healthcare organization uses Active Directory for authentication. A nurse accesses the electronic health records (EHR) system, which requires the nurse's AD credentials. The EHR system is configured to query the organization's AD via LDAP to verify group membership before granting access. The LDAP query is transmitted over port 389 on the internal network. What security risk does this configuration present?

A. Port 389 uses LDAP over TLS, so the query is encrypted and no risk is present.

B. LDAP on port 389 transmits directory queries and bind credentials in cleartext, allowing an attacker with network access to capture AD credentials and group membership data.

C. LDAP on port 389 uses Kerberos for mutual authentication, which encrypts the session automatically.

D. Port 389 is blocked by default on Windows Server, so the EHR integration would not function.

**Correct Answer:** B

**Explanation:** Standard LDAP (port 389) does not encrypt communications by default — bind operations (which transmit the username and password used to authenticate the LDAP query) and query results are transmitted in cleartext. An attacker with access to the internal network segment can capture these credentials with a passive packet capture tool. The secure alternative is LDAPS on port 636, which wraps LDAP in TLS. LDAP on port 389 is not encrypted by default and does not use Kerberos — Kerberos is a separate authentication protocol. Port 389 is not blocked by default on Windows Server; it is the standard LDAP port.

---

### Question 18

A company's IAM policy requires that access to production systems be granted only through a PAM solution that records all privileged sessions. A new contractor is given direct SSH access to a production database server using a shared root credential because "the PAM solution is too slow." Which IAM control failures does this situation represent?

A. Failure of authentication only — the contractor should use certificate-based SSH instead of password authentication.

B. Failure of privileged access management and non-repudiation — shared credentials eliminate individual accountability, and bypassing session recording removes the audit trail required to attribute actions to a specific person.

C. Failure of authorization only — the contractor has too many permissions but the access method is acceptable.

D. Failure of provisioning only — the access should have been provisioned through the ticketing system before the contractor arrived.

**Correct Answer:** B

**Explanation:** Two distinct IAM control failures are present. First, using a shared root credential eliminates individual accountability — if a change or incident occurs, there is no way to determine which person using the shared credential was responsible, violating non-repudiation. Second, bypassing the PAM session recording removes the audit trail that the policy mandates for privileged access. PAM solutions exist precisely to enforce least privilege, credential vaulting, and session recording for privileged accounts. The fact that the PAM solution is slow is an operational concern that should be addressed, not bypassed. Authentication method and provisioning process are secondary concerns to the accountability and audit trail failures.

---

### Question 19

An organization wants to implement federated identity so that employees can use their corporate credentials to access partner organization systems, and partner employees can access some internal systems, without either organization managing accounts in the other's directory. Which identity federation trust model describes a direct bilateral trust relationship between two organizations' identity providers?

A. Hub-and-spoke federation — one central IdP brokers all identity assertions between all parties.

B. Cross-certification PKI — both CAs sign each other's root certificates to establish mutual trust.

C. Direct (bilateral) federation — each organization's IdP is configured to trust the other's IdP directly, enabling mutual SSO without a third-party broker.

D. Transitive trust — trust flows automatically from Organization A to Organization C because A trusts B and B trusts C.

**Correct Answer:** C

**Explanation:** Direct or bilateral federation establishes a one-to-one trust relationship between two organizations' identity providers. Each IdP is configured with metadata about the other (typically exchanged via SAML metadata documents or OIDC discovery endpoints), and each trusts assertions issued by the other. This model works well for a small number of partners but scales poorly — each new partner requires a new bilateral configuration. Hub-and-spoke federation uses a central broker (such as a federation hub) to manage identity translation between many parties. Cross-certification is a PKI concept for CA trust, not identity federation. Transitive trust in Active Directory refers to domain trust propagation, not federated IdP relationships.

---

### Question 20

A company conducts a quarterly user access review and discovers that a senior developer has accumulated the following access over three years: production database administrator rights (from a past incident response), a read/write role in the financial reporting system (from a temporary project), and their current software development role. The developer's current job function requires only the development role. Which IAM process is designed to detect and remediate this condition, and which principle is being violated?

A. Onboarding review; violating the principle of separation of duties.

B. Periodic access recertification (access review); violating the principle of least privilege by allowing permissions that exceed the user's current job function requirements.

C. Provisioning audit; violating the principle of need-to-know only at the time of initial grant.

D. Offboarding review; violating the principle of mandatory access control.

**Correct Answer:** B

**Explanation:** Periodic access recertification — also called an access review or entitlement review — is the formal IAM process of systematically reviewing all user permissions on a scheduled basis and revoking any access that is no longer justified by the user's current role. The condition described (accumulation of permissions from past temporary roles) is called privilege creep, and it directly violates the principle of least privilege, which requires that users hold only the minimum permissions necessary to perform their current job function. Onboarding and offboarding reviews occur at specific employment lifecycle events, not on a recurring schedule. Mandatory access control is a classification-based model unrelated to this scenario.

---

Module 06 Quiz — End
