# Reading Guide: Module 09 - Entra Authentication and MFA

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 09 - Entra Authentication and MFA**! This module covers Microsoft Entra ID's authentication capabilities as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. Strong authentication and context-aware access policies are cornerstones of cloud security — AZ-900 tests whether you understand the difference between authenticating a user (MFA) and controlling when and how that authentication is required (Conditional Access).

You will learn how Multi-Factor Authentication adds a second verification layer, how Conditional Access policies enforce context-based access rules, and how Single Sign-On simplifies the user experience across multiple applications. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Multi-Factor Authentication (MFA)**: An authentication method that requires users to verify their identity using two or more factors: something you know (password), something you have (authenticator app, SMS code, hardware token), or something you are (biometric). MFA dramatically reduces the risk of account compromise from stolen passwords. In Azure, MFA is enabled via Microsoft Entra ID and can be enforced through Conditional Access policies.

* **Conditional Access Policies**: Rule-based policies in Microsoft Entra ID that evaluate signals (user identity, device compliance, location, application being accessed, real-time risk score) and then enforce access decisions such as requiring MFA, blocking access, or requiring a compliant device. Conditional Access implements an "if-then" logic: if a user logs in from outside the corporate network, then require MFA.

* **Single Sign-On (SSO)**: An authentication capability that allows users to sign in once with a single set of credentials and access multiple applications without re-entering credentials. Azure SSO uses Entra ID as the identity provider, issuing tokens that are honored by integrated SaaS applications (e.g., Salesforce, ServiceNow) and Microsoft services. SSO reduces password fatigue and decreases the attack surface.

---

### 2. Certification Exam Tips

* **MFA vs. Conditional Access**: AZ-900 tests the relationship between these two. MFA is the authentication mechanism (the second factor). Conditional Access is the policy that decides when MFA is required. MFA can be always-on or triggered only by Conditional Access signals.
* **Zero Trust and Conditional Access**: AZ-900 may reference the Zero Trust security model. Conditional Access is the Azure implementation of Zero Trust's "verify explicitly" principle — it evaluates multiple signals rather than assuming a user inside the network is trusted.
* **Entra ID Free vs. P1 for MFA**: Per-user MFA (legacy) is available in the Free tier. Conditional Access-driven MFA (recommended) requires Entra ID P1. The exam may distinguish between these approaches — Conditional Access is always the modern best practice.
* **SSO Benefits**: AZ-900 may ask why SSO improves security. The answer: fewer passwords means less password reuse across services, fewer credentials to steal, and centralized revocation — revoking a user's Entra ID account revokes access to all SSO-integrated applications simultaneously.
* **Study Resource**: The Microsoft Learn security module covers MFA, Conditional Access, and SSO with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers MFA, Conditional Access, and SSO under the identity and security domain. Access it at [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Entra authentication concepts for AZ-900 — watch the identity security section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Configure a Conditional Access policy requiring MFA for administrators**: In the Entra ID portal, create a Conditional Access policy that targets the Global Administrator role and requires MFA as the access control. Set the policy to Report-only mode to observe impact without enforcing.
* **Verify authentication flow**: Using a test user account, sign in to the Azure portal and trace the authentication steps. Observe how Entra ID evaluates Conditional Access policies and prompts for MFA when the policy conditions are met.
* **Configure SSO settings**: In Entra ID Enterprise Applications, review how an existing application is configured for SSO. Observe the SSO mode (SAML or OIDC), the claim mappings, and how the application trusts Entra ID as the identity provider.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the authentication and MFA unit in [Microsoft Learn – AZ-900 Azure Security](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the identity security section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for Conditional Access policy creation and SSO configuration.
* [ ] Proceed to the weekly hands-on lab activity.
