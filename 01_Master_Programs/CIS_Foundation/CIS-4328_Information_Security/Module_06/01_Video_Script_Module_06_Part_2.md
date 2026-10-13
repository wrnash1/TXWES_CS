# Video Script: Module 06 — Identity and Access Management (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Part 2 of Module 06. In Part 1 we covered authentication factors, MFA, SSO, SAML, OAuth 2.0, and OIDC. Now we cover the infrastructure layer — directory services — and the operational practices: IAM best practices, privileged access management, and exam traps.

---

### [SECTION 1 — Directory Services — 0:30]

A **directory service** is a database optimized for storing and querying identity information: users, groups, computers, and their attributes.

#### LDAP

**LDAP (Lightweight Directory Access Protocol)** is the protocol used to query and modify directory services. It uses a hierarchical structure called a **Directory Information Tree (DIT)**.

LDAP distinguished names identify objects in the hierarchy:

```text
CN=John Smith, OU=Finance, DC=example, DC=com
```

Key LDAP facts for the exam:

- LDAP uses **port 389** (cleartext) or **port 636** (LDAPS — LDAP over TLS).

- LDAP itself is a protocol; the directory database is the service (like Active Directory or OpenLDAP).

- Authentication via LDAP uses a **bind operation** — the client provides a DN and password.

**Exam point**: The exam distinguishes LDAP (the protocol) from Active Directory (a directory service that uses LDAP as its query protocol). LDAP is not Active Directory; Active Directory uses LDAP.

#### Active Directory (AD)

Active Directory is Microsoft's directory service for Windows environments. It provides:

- Centralized user account management.

- Group Policy for configuration enforcement.

- Kerberos-based authentication.

- LDAP as the query protocol.

**Kerberos** is the authentication protocol used within AD environments. It uses **tickets** rather than passwords for authentication after initial login.

Key Kerberos components:

- **KDC (Key Distribution Center)** — the central authentication service in AD.

- **TGT (Ticket Granting Ticket)** — issued after initial authentication; used to request service tickets.

- **Service Ticket** — authorizes access to a specific resource.

**Exam trap**: Kerberos uses tickets, not challenges. NTLM uses challenge-response. AD uses Kerberos by default; NTLM is the fallback for legacy compatibility.

---

### [SECTION 2 — IAM Best Practices — 4:30]

#### Principle of Least Privilege

Users, systems, and applications should have only the permissions necessary to perform their defined function — nothing more.

This applies at multiple layers:

- User accounts: no administrative access unless required.

- Service accounts: minimal permissions for their function.

- Application access: no write permission if only read is needed.

**Why it matters**: If a least-privilege account is compromised, the attacker's lateral movement options are limited. A compromised domain admin account is catastrophic; a compromised read-only service account is contained.

#### Separation of Duties

No single individual should have the ability to complete a sensitive transaction alone. A classic example: the person who approves purchase orders should not be the same person who processes payments.

In IAM terms: sensitive operations require **dual control** — two different authenticated identities to complete.

**Exam distinction**: Separation of duties is an **administrative control**; it is a policy that shapes how roles are designed. Enforcing it technically (requiring two accounts to sign off on a transaction) is a **technical control** implementing that policy.

#### Access Reviews and Recertification

User access should be reviewed periodically. The most common failure mode is **access accumulation** — users who change roles or departments retain access from their previous roles. This violates least privilege over time.

**User Account Reviews** — scheduled verification that each user's access is still appropriate.

**Privileged Account Reviews** — more frequent, given the risk level.

**Offboarding** — immediate access revocation upon employee departure is a critical control. Accounts left active after an employee's departure are a persistent risk.

#### Account Types

- **Standard user account** — day-to-day operations; limited permissions.

- **Privileged account / administrative account** — elevated permissions; higher risk.

- **Service account** — used by applications and services; should have minimal, scoped permissions; should not be used for interactive logins.

- **Shared account** — multiple users share one account; breaks audit trail; generally prohibited in security-conscious environments.

**Exam point**: Shared accounts violate non-repudiation. If a shared account takes a malicious action, you cannot determine which individual was responsible.

---

### [SECTION 3 — Privileged Access Management — 8:00]

**Privileged Access Management (PAM)** is the set of controls specifically addressing high-privilege accounts — accounts that can significantly affect system configuration, security controls, or sensitive data.

#### Why PAM Matters

Administrative accounts are the highest-value targets for attackers. Credential theft attacks (Pass-the-Hash, Kerberoasting) specifically target privileged credentials. An attacker with domain admin credentials has essentially won — they can read all data, create backdoors, and disable security controls.

#### PAM Controls

**Just-in-Time (JIT) Access** — privileged access is granted only for the duration needed to complete a specific task, then automatically revoked. Rather than having persistent admin rights, a user requests elevation, works, and access expires.

**Privileged Access Workstations (PAWs)** — dedicated, hardened workstations used exclusively for administrative tasks. Administrative work is never performed from a general-purpose workstation that also browses the web and reads email.

**Password Vaulting** — privileged account passwords are stored in an encrypted vault, automatically rotated, and checked out for specific sessions. Administrators never know the actual password; they check out a session.

**Session Recording** — all privileged sessions are recorded for audit and forensic purposes. Administrators know their actions are logged.

**Break Glass Accounts** — emergency accounts with highest privilege, stored in a sealed envelope (or vault), used only when normal administrative access is unavailable. Usage triggers an immediate alert.

---

### [SECTION 4 — Access Control Models — 10:30]

The Security+ exam tests four access control models. Know the defining characteristic of each.

**DAC (Discretionary Access Control)** — the resource owner decides who has access. Standard file system permissions in Windows and Linux are DAC. Flexible but difficult to manage at scale and does not protect against compromised owner accounts.

**MAC (Mandatory Access Control)** — access decisions are based on labels (classification levels) assigned to both subjects and objects by a central authority. Common in government/military contexts (Top Secret, Secret, Classified, Unclassified). No individual can override the label policy.

**RBAC (Role-Based Access Control)** — access is granted based on a user's role within the organization. A user in the "Finance" role gets Finance data access; a user in "Engineering" gets Engineering data access. Easier to manage at scale.

**ABAC (Attribute-Based Access Control)** — access decisions are based on attributes of the user, resource, and environment. Example: "allow access if user.department = Finance AND resource.classification = Internal AND time.hour is between 8 and 18 AND user.location = Corporate." Very flexible; complex to manage.

---

### [SECTION 5 — EXAM TRAPS AND QUESTION ANALYSIS — 12:15]

#### Trap 1: OAuth 2.0 is Not Authentication

"A developer implements OAuth 2.0 so users can sign in with their Google account. What does OAuth 2.0 provide?"

Wrong answer: authentication.

Correct answer: **authorization** (the ability to access Google resources). OIDC is the layer that provides authentication (who the user is). OAuth 2.0 alone does not verify identity — it grants access.

#### Trap 2: SAML vs. OIDC

When to choose SAML: enterprise SSO, XML-based assertions, legacy SaaS integration, B2B federation, corporate VPN portals.

When to choose OIDC: modern consumer apps, mobile apps, APIs, any environment where JSON and JWT are preferred over XML.

The exam will present a scenario and ask which protocol is appropriate. Key discriminator: XML + enterprise = SAML; JSON/JWT + modern/mobile = OIDC.

#### Trap 3: MFA Factor Categories

"A user logs in with a password and answers a secret question. How many authentication factors are used?"

Wrong answer: two (two-factor authentication).

Correct answer: **one factor** — both are "something you know." MFA requires factors from different categories.

#### Trap 4: Kerberos vs. NTLM

"Which authentication protocol is used by default in modern Active Directory environments?"

Correct answer: **Kerberos**. NTLM is a legacy fallback.

"A penetration tester captures NTLM hashes on a Windows network. What attack is being set up?"

Answer: **Pass-the-Hash** — NTLM hashes can be used directly for authentication without knowing the plaintext password.

#### Trap 5: LDAP Port Numbers

LDAP uses port 389. LDAPS (LDAP over TLS) uses port 636. The exam tests port numbers for all directory and authentication protocols.

#### Trap 6: Least Privilege vs. Need to Know

These are related but distinct concepts:

- **Least privilege** — the minimum permissions needed to perform a function (access rights).

- **Need to know** — access to information is granted only to those with a demonstrated need for that specific information (information classification concept).

Both principles lead to restricted access but are applied in different contexts.

---

### [OUTRO — 15:00]

IAM is one of the most operationally relevant domains in security. The failures are universal: weak passwords, no MFA, over-privileged accounts, orphaned accounts, no access reviews.

Key review for the exam:

- MFA = different factor categories, not just two inputs.

- SAML = enterprise SSO, XML assertions.

- OAuth 2.0 = authorization only, not authentication.

- OIDC = authentication layer on OAuth 2.0, ID tokens.

- LDAP = protocol, port 389/636.

- Active Directory = uses Kerberos by default, NTLM as fallback.

- Least privilege, separation of duties, access reviews — core IAM best practices.

- PAM controls: JIT access, PAWs, password vaulting, session recording.

Complete the quiz and lab before moving to Module 07 — Network Security Architecture.

---

End of Part 2 — Module 06
