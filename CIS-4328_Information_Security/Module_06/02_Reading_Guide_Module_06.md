# Reading Guide: Module 06 — Identity and Access Management

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment

---

## Overview

This reading guide supports Module 06 of CIS-4328. It covers authentication factors, MFA, SSO, federation protocols (SAML, OAuth 2.0, OIDC), directory services, IAM best practices, access control models, and privileged access management.

All readings use zero-cost, openly licensed resources.

---

## Learning Objectives

By the end of this module, you will be able to:

- Classify authentication factors by type and explain the requirement for multi-factor authentication.

- Describe how SSO and federation work, identifying the roles of IdP and SP.

- Distinguish SAML, OAuth 2.0, and OIDC by use case, token type, and what each provides.

- Describe LDAP's role as a directory query protocol and explain its relationship to Active Directory.

- Explain Kerberos ticket-based authentication and contrast it with NTLM challenge-response.

- Apply least privilege, separation of duties, and access reviews as core IAM best practices.

- Describe the four access control models (DAC, MAC, RBAC, ABAC) and identify the defining characteristic of each.

- Explain privileged access management controls including JIT access, PAWs, and password vaulting.

---

## Primary Readings

### Reading 1 — NIST SP 800-63B: Digital Identity Guidelines — Authentication

Source: [https://pages.nist.gov/800-63-3/sp800-63b.html](https://pages.nist.gov/800-63-3/sp800-63b.html)

Read: Section 4 (Authenticator Assurance Levels) and Section 5 (Authenticator and Verifier Requirements).

Focus areas:

- The three Authenticator Assurance Levels (AAL1, AAL2, AAL3) and what each requires.

- Why phishing-resistant authenticators (hardware keys, PIV) are designated AAL3.

- The specific weaknesses of SMS-based OTP (in the context of SIM-swapping attacks).

### Reading 2 — NIST SP 800-162: Guide to Attribute-Based Access Control

Source: [https://csrc.nist.gov/publications/detail/sp/800-162/final](https://csrc.nist.gov/publications/detail/sp/800-162/final)

Read: Section 3 (ABAC Overview) and Section 4 (ABAC vs. RBAC).

Focus areas:

- The structural differences between RBAC and ABAC.

- When ABAC provides better security granularity than RBAC.

- Environmental attributes and their role in context-aware access decisions.

### Reading 3 — CISA Zero Trust Maturity Model

Source: [https://www.cisa.gov/zero-trust-maturity-model](https://www.cisa.gov/zero-trust-maturity-model)

Read: The Identity pillar section.

Focus areas:

- How IAM underpins the zero trust model.

- The role of continuous authentication and risk-based access decisions.

- MFA as a baseline zero-trust requirement.

---

## Supplemental Readings

### Reading 4 — OAuth 2.0 Overview (Auth0 Documentation)

Source: [https://auth0.com/intro-to-iam/what-is-oauth-2/](https://auth0.com/intro-to-iam/what-is-oauth-2/)

Read: The full article.

Focus areas:

- The distinction between OAuth 2.0 authorization and OIDC authentication.

- The Authorization Code flow and why it is more secure than the Implicit flow.

- The PKCE extension and when it is required.

### Reading 5 — Microsoft: How Kerberos Authentication Works

Source: [https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)

Read: The overview and the "Kerberos Authentication Process" section.

Focus areas:

- The three-party model: client, KDC, and service.

- The TGT and service ticket flow.

- Why Kerberos is preferred over NTLM for modern AD environments.

---

## Concept Reference Tables

### Table 1 — Authentication Factor Categories

| Factor Type | Examples | Exam Notes |
|---|---|---|
| Something you know | Password, PIN, security question | Most common; weakest alone |
| Something you have | Smart card, hardware token, OTP app, phone | TOTP and HOTP are both "have" factors |
| Something you are | Fingerprint, retina, facial recognition, voice | Biometrics |
| Somewhere you are | Geolocation, IP restriction | Less common on exam |
| Something you do | Typing rhythm, gait, behavioral biometrics | Emerging category |

### Table 2 — Federation Protocol Comparison

| Protocol | Standard | Token Format | Primary Use Case | Provides |
|---|---|---|---|---|
| SAML 2.0 | OASIS | XML | Enterprise web SSO, B2B | Authentication + Authorization |
| OAuth 2.0 | IETF RFC 6749 | Access Token (opaque or JWT) | API authorization, delegated access | Authorization only |
| OIDC | OpenID Foundation | ID Token (JWT) | Consumer authentication on OAuth 2.0 | Authentication |

### Table 3 — Access Control Models

| Model | Control Mechanism | Defining Characteristic |
|---|---|---|
| DAC | Resource owner discretion | Owner assigns permissions; flexible but hard to enforce policy |
| MAC | Central authority assigns labels | Labels on subjects and objects; cannot be overridden by owner |
| RBAC | Role assignment | Access tied to job role; scalable for enterprises |
| ABAC | Policy evaluated against attributes | Most flexible; considers user, resource, and environment attributes |

### Table 4 — PAM Control Summary

| Control | Mechanism | Risk Addressed |
|---|---|---|
| Just-in-Time Access | Temporary elevation; auto-expires | Persistent privileged credentials |
| Privileged Access Workstation | Dedicated hardened device | Credential theft from general-use workstations |
| Password Vaulting | Encrypted storage; auto-rotation | Password reuse; insider knowledge of credentials |
| Session Recording | Full keystroke/screen capture | Audit trail; insider threat detection |
| Break Glass Account | Emergency access; sealed | Unavailability of normal admin access |

---

## Key Terms and Definitions

**Authentication** — The process of verifying a claimed identity.

**Authorization** — The process of determining what an authenticated identity is permitted to do.

**MFA (Multi-Factor Authentication)** — Authentication using two or more factors from different categories.

**TOTP** — Time-based One-Time Password; OTP valid for a short time window.

**HOTP** — HMAC-based One-Time Password; OTP valid until used; counter-based.

**Biometrics** — Authentication using physical or behavioral characteristics.

**FAR** — False Acceptance Rate; rate of incorrectly accepting unauthorized users.

**FRR** — False Rejection Rate; rate of incorrectly rejecting authorized users.

**CER** — Crossover Error Rate; point where FAR equals FRR; lower is better.

**SSO** — Single Sign-On; one authentication grants access to multiple systems.

**Identity Provider (IdP)** — The system that authenticates users and issues identity assertions.

**Service Provider (SP)** — The system that relies on the IdP's assertion to grant access.

**SAML** — Security Assertion Markup Language; XML-based SSO standard.

**OAuth 2.0** — Authorization framework allowing delegated access to resources.

**OIDC** — OpenID Connect; identity authentication layer built on OAuth 2.0.

**JWT** — JSON Web Token; compact, signed token format used in OIDC.

**LDAP** — Lightweight Directory Access Protocol; protocol for querying directory services.

**Active Directory** — Microsoft's enterprise directory service; uses LDAP and Kerberos.

**Kerberos** — Ticket-based network authentication protocol used in AD environments.

**NTLM** — NT LAN Manager; legacy challenge-response authentication; fallback in AD.

**Least Privilege** — Users and systems receive only the permissions required for their function.

**Separation of Duties** — No single individual can complete a sensitive transaction alone.

**DAC** — Discretionary Access Control; owner determines access.

**MAC** — Mandatory Access Control; central authority assigns classification labels.

**RBAC** — Role-Based Access Control; access based on organizational role.

**ABAC** — Attribute-Based Access Control; access based on user, resource, and environment attributes.

**PAM** — Privileged Access Management; controls for high-privilege accounts.

**JIT Access** — Just-in-Time Access; temporary elevation of privilege.

**PAW** — Privileged Access Workstation; hardened device for administrative tasks only.

**Offboarding** — The process of revoking access when an employee departs.

---

## Security+ Exam Alignment

The following SY0-701 exam objectives are covered in this module:

- 4.1 — Given a scenario, apply common access control concepts.

- 4.2 — Given a scenario, manage identities and authentication.

- 4.3 — Given a scenario, implement and manage authorization.

- 4.4 — Explain the importance of wireless security protocols.

---

## Critical Thinking Questions

1. An employee in the accounting department is transferred to the IT department. After the transfer, their manager requests additional permissions for the new role. Three months later, a security audit finds the employee has accumulated permissions from both roles. What principle has been violated, what is the specific risk, and what process control would have prevented it?

2. A startup is building a consumer-facing mobile app and wants users to be able to log in with their existing Google or Apple accounts. The app will also need to read the user's Google Drive files. Which protocols should be implemented? Explain the role of each protocol and which specific security properties each provides.

3. A hospital uses a shared nursing station account that multiple nurses log in to throughout the day. The account has access to all patient records. Identify all the security and compliance problems this configuration creates. What IAM architecture would you recommend to replace it?

4. An attacker has obtained NTLM hashes from a Windows domain controller using a credential-dumping tool. The attacker does not crack the hashes but uses them directly to authenticate to other systems. What attack technique is this, and what specific controls in the PAM domain would have reduced the risk?

5. A company is evaluating whether to implement RBAC or ABAC for their cloud environment. They need to restrict access based on user department, time of day, geographic location, and the sensitivity classification of the data being accessed. Which model is better suited, and why?

---

## 9. Supplemental Resources

**1. NIST SP 800-63B — Digital Identity Guidelines: Authentication and Lifecycle Management**
<https://pages.nist.gov/800-63-3/sp800-63b.html>
NIST's authoritative guidance on authenticator assurance levels (AAL1/AAL2/AAL3), phishing-resistant MFA requirements, and password policy recommendations. Directly supports Module 06 coverage of MFA factor types, FIDO2 requirements, and the deprecation of SMS OTP for high-assurance use cases.

**2. CISA Zero Trust Maturity Model**
<https://www.cisa.gov/zero-trust-maturity-model>
CISA's five-pillar Zero Trust framework covering Identity, Devices, Networks, Applications, and Data. The Identity pillar directly maps to Module 06 content on continuous verification, least privilege enforcement, and PAM controls. Use this to understand how IAM principles connect to the broader Zero Trust architecture covered in Module 07.

**3. OWASP JSON Web Token (JWT) Security Cheat Sheet**
<https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html>
A practical reference for secure JWT implementation covering algorithm confusion attacks (RS256 vs HS256), token expiration enforcement, signature validation, and claim validation. Directly supports the Module 06 lab JWT analysis tasks and reinforces the connection between OAuth 2.0/OIDC token handling and secure IAM implementation.

---

## Review Checklist

Before taking the Module 06 quiz, verify you can do each of the following without notes:

- Name the five authentication factor types and give one example of each.

- Explain the difference between FAR and FRR and which is a security problem vs. a usability problem.

- Describe the SAML authentication flow in four steps.

- Explain what OAuth 2.0 provides and what it does NOT provide.

- State how OIDC extends OAuth 2.0 and what the ID token contains.

- Distinguish Kerberos from NTLM and explain why Kerberos is preferred.

- Name the four access control models and state the defining characteristic of each.

- List three PAM controls and explain what risk each addresses.

---

Module 06 Reading Guide — End
