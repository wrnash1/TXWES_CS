# Video Script: Module 06 — Identity and Access Management (Part 1 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

### [INTRO — 0:00]

Welcome to Module 06, Part 1. I'm Professor Nash.

Identity and Access Management — IAM — is the set of processes and technologies that ensure the right people have the right access to the right resources at the right time. Every security breach ultimately involves either a compromised identity or an access control failure. IAM is the domain that prevents both.

Security+ Domain 4 — "Identity and Access Management" — covers authentication factors, federation, directory services, and privileged access. This module is also deeply interconnected with real-world zero-trust implementations.

Part 1 covers the foundational concepts: authentication factors, MFA, SSO, SAML, OAuth 2.0, and OIDC. Part 2 covers directory services, IAM best practices, privileged access management, and exam traps.

---

### [SECTION 1 — Authentication Fundamentals — 1:00]

Authentication is the process of verifying that a claimed identity is genuine.

The three traditional authentication factors are:

- **Something you know** — passwords, PINs, security questions.

- **Something you have** — hardware tokens, smart cards, one-time password (OTP) apps.

- **Something you are** — biometrics: fingerprint, retina, facial recognition, voice.

Two additional factors appear on the Security+ exam:

- **Somewhere you are** — geolocation; restricting access to specific IP ranges or geographic regions.

- **Something you do** — behavioral biometrics: typing rhythm, gait analysis, mouse movement patterns.

**Multi-Factor Authentication (MFA)** requires two or more factors from different categories. The key word is "different categories." A password plus a security question is two factors from the same category (both are something you know) — this is NOT MFA.

**Exam trap**: "Two-factor" means exactly two factors from two different categories. Using a password and a PIN is single-factor, not two-factor.

#### OTP Types

- **TOTP (Time-based OTP)** — generates a code using a shared secret and the current time; valid for 30–60 seconds. Used by Google Authenticator, Microsoft Authenticator. Algorithm: HOTP with a time step.

- **HOTP (HMAC-based OTP)** — generates a code using a shared secret and an incrementing counter. Each code is valid until used.

**Exam point**: TOTP expires after a time window; HOTP persists until used. Both require the shared secret to be established securely during enrollment.

#### Biometrics

Biometrics introduces two error metrics that the exam tests:

- **FAR (False Acceptance Rate)** — the rate at which the system incorrectly accepts an unauthorized user.

- **FRR (False Rejection Rate)** — the rate at which the system incorrectly rejects an authorized user.

These metrics trade off against each other. Increasing sensitivity reduces FAR but increases FRR. The **CER (Crossover Error Rate)** is the point where FAR = FRR, used to compare biometric systems. Lower CER = better system.

**Exam trap**: A high FAR is a security problem (unauthorized access). A high FRR is a usability problem (frustrated legitimate users).

---

### [SECTION 2 — Single Sign-On — 5:00]

**Single Sign-On (SSO)** allows a user to authenticate once and access multiple systems without re-authenticating for each one.

Benefits: improved user experience, reduced password fatigue, centralized authentication logging.

Risk: if the SSO credential is compromised, the attacker gains access to all connected systems. This is why SSO is almost always deployed with MFA.

SSO relies on **federation** — a trust relationship between an **Identity Provider (IdP)** and one or more **Service Providers (SPs)**. The IdP authenticates the user; the SPs trust the IdP's assertion.

---

### [SECTION 3 — SAML — 6:30]

**SAML (Security Assertion Markup Language)** is an XML-based open standard for exchanging authentication and authorization data between an IdP and an SP.

SAML is predominantly used for **enterprise web application SSO** — especially in B2B and SaaS contexts.

The SAML flow:

1. User attempts to access the SP (e.g., Salesforce).

2. SP redirects to the IdP.

3. User authenticates with the IdP (e.g., corporate Active Directory via ADFS).

4. IdP issues a **SAML assertion** — a signed XML token containing authentication information.

5. SP validates the assertion and grants access.

Key SAML concepts:

- **Assertion** — the signed statement of identity issued by the IdP.

- **Binding** — the transport mechanism (HTTP Redirect, HTTP POST, HTTP Artifact).

- **Metadata** — XML documents that describe IdP and SP capabilities, endpoints, and signing certificates.

**Exam point**: SAML assertions are XML documents signed with the IdP's private key. The SP validates the signature using the IdP's public key (from metadata). This provides integrity and authenticity for the identity claim.

**When the exam says SAML**: think enterprise web SSO, XML tokens, assertion, IdP, and SP.

---

### [SECTION 4 — OAuth 2.0 — 9:00]

**OAuth 2.0** is an authorization framework — not an authentication protocol. This distinction is critically tested on Security+.

OAuth 2.0 allows a user to grant a third-party application **limited access** to their resources without sharing their credentials.

Classic example: A user clicks "Sign in with Google" on a third-party app. The app wants to read the user's Google Calendar. OAuth 2.0 defines the flow for granting that access.

Key OAuth 2.0 roles:

- **Resource Owner** — the user who owns the data.

- **Client** — the third-party application requesting access.

- **Authorization Server** — the server that issues access tokens (e.g., Google's auth server).

- **Resource Server** — the server hosting the protected data (e.g., Google Calendar API).

The output of OAuth 2.0 is an **access token** — a credential the client uses to access the resource server.

**Exam trap**: OAuth 2.0 is authorization, not authentication. It answers "what can this application do?" not "who is this user?" OAuth 2.0 was extended by OpenID Connect to add authentication.

#### OAuth 2.0 Grant Types

- **Authorization Code** — the most secure flow; used for server-side web apps. The authorization code is exchanged server-side for a token.

- **PKCE (Proof Key for Code Exchange)** — extension of Authorization Code for public clients (mobile apps, SPAs) where a client secret cannot be safely stored.

- **Client Credentials** — machine-to-machine flows; no user interaction.

- **Implicit** — deprecated; previously used for browser-based apps; now replaced by Authorization Code + PKCE.

---

### [SECTION 5 — OpenID Connect (OIDC) — 12:00]

**OpenID Connect (OIDC)** is an identity layer built on top of OAuth 2.0. Where OAuth 2.0 handles authorization, OIDC adds authentication.

OIDC introduces the **ID token** — a JSON Web Token (JWT) containing verified claims about the authenticated user's identity (sub, email, name, etc.).

When you see "Sign in with Google" and the app knows who you are (not just that you granted access), OIDC is what provides that identity.

The relationship:

- **OAuth 2.0** — answers "what can this app access?"

- **OIDC** — answers "who is this user?" and provides a verified identity assertion.

**JWT (JSON Web Token)** structure: three Base64URL-encoded sections separated by dots.

- **Header** — algorithm and token type.

- **Payload** — claims (user ID, issuer, expiration, audience).

- **Signature** — HMAC-SHA256 or RSA signature over header.payload.

**Exam trap**: OIDC is built on OAuth 2.0 but is not the same thing. If a question asks about authentication using a modern protocol for consumer-facing apps, OIDC is likely the answer. If the question is enterprise web SSO with XML assertions, SAML is the answer.

---

### [OUTRO — 15:00]

Part 1 has covered the authentication and federation layer of IAM:

- Authentication factors and MFA.

- SSO and federation (IdP / SP trust).

- SAML — enterprise web SSO, XML assertions.

- OAuth 2.0 — authorization, access tokens, not authentication.

- OIDC — identity layer on OAuth 2.0, ID tokens, JWTs.

In Part 2 we cover directory services (LDAP, Active Directory), IAM best practices (least privilege, separation of duties, access reviews), and privileged access management — plus the exam traps specific to this domain.

See you in Part 2.

---

End of Part 1 — Module 06
