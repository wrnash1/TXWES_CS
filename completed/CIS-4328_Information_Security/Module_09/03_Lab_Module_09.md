# Lab Activity: Module 09 - AppSec (OWASP)
## Course: CIS-4328_Information_Security (CompTIA Security+ (SY0-701))

---

**Lab 9:** Use a vulnerable web app (like DVWA) to execute a successful SQL injection attack.

---

## Part 9 — Challenge Exercise

### Challenge 1: Authentication Attack Analysis and MFA Deployment Design

A regional credit union with 800 members and 60 employees has experienced two security incidents in the past six months. In the first incident, an employee account was compromised after the employee clicked a phishing link and entered their credentials on a fake login page; the attacker then received the TOTP code through a real-time relay and accessed the core banking system. In the second incident, fifteen member online banking accounts were compromised through a credential stuffing attack using a list of email/password pairs from an unrelated data breach.

1. For each incident, identify: the specific authentication weakness that was exploited, the MITRE ATT&CK technique name that describes the attack, and the specific authentication control that would have prevented the compromise. For the employee incident, explain why TOTP did not prevent the attack and why FIDO2 would have.

2. The credit union wants to deploy phishing-resistant MFA for all 60 employees who access the core banking system. They are evaluating two options: FIDO2 hardware security keys (one per employee, approximately $50 each) versus certificate-based smart cards integrated with their existing Active Directory PKI. Compare the two options across the following dimensions: phishing resistance mechanism, deployment complexity, cost, recovery process if a device is lost, and whether each satisfies NIST SP 800-63B AAL3 requirements.

3. For the 800 member online banking accounts, the credit union cannot require hardware keys. Design a layered authentication strategy using controls available in a consumer banking context. Your strategy must address: the primary authentication method, a second factor that provides meaningful protection without requiring hardware, a risk-based authentication trigger that requires step-up authentication for high-risk transactions (define what "high-risk" means in this context), and a credential stuffing detection mechanism. For each control, specify how it is implemented and what attack it addresses.

4. The credit union's IT director argues that requiring employees to use hardware security keys is excessive because "we already have MFA." Write a two-paragraph response explaining why not all MFA is equal, using NIST SP 800-63B Authenticator Assurance Levels as the framework, and specifically addressing the AAL level achieved by TOTP versus FIDO2 and why the difference matters for a financial institution subject to FFIEC guidance.

### Challenge 2: SSO Federation Architecture and Token Security

A healthcare network is consolidating authentication across three acquired hospital systems. Each hospital currently has its own Active Directory domain and its own set of clinical applications. The network's goal is to implement federated SSO so that a clinician credentialed at one hospital can access clinical applications at any of the three hospitals without separate logins. The environment includes on-premises EHR systems, a cloud-based radiology PACS viewer (SaaS), and an internal patient portal web application.

1. Design a federated identity architecture for this healthcare network. Your design must specify: the identity federation protocol (SAML 2.0, OIDC, or a combination), which system(s) act as Identity Providers and which act as Service Providers, how trust is established between the three AD domains, and how the cloud SaaS PACS viewer is integrated. Draw a text-format architecture diagram showing the relationship between all components.

2. The EHR system supports SAML 2.0 federation. When a physician from Hospital A logs into the EHR at Hospital B, trace the complete SAML authentication flow in six steps, identifying at each step: what message is sent, between which parties, what cryptographic operation occurs, and what security property that operation provides.

3. A security audit finds that one of the hospital's SAML Service Providers is accepting assertions without validating the NotBefore and NotAfter time conditions in the assertion. Explain what attack this misconfiguration enables (name the specific SAML attack), describe the attack scenario step by step, and identify the two specific SAML assertion fields the SP must validate to prevent it.

4. The network's security team wants to ensure that clinicians who are accessing the EHR remotely (outside hospital networks) are required to re-authenticate with a stronger second factor than clinicians on the hospital network. Describe how this risk-based, context-aware authentication requirement can be implemented within the federated SSO architecture, identifying the specific protocol mechanism (SAML AuthnContext, OIDC acr claim, or similar) and the network-location signal that triggers the step-up requirement.

### Reflection Questions

1. After completing both challenges, explain the fundamental security tradeoff between SSO convenience and risk concentration. In Challenge 2, a single IdP compromise could grant an attacker access to all three hospital systems and the cloud SaaS application. Compare this risk profile to the pre-consolidation state where each hospital had separate authentication. Address both the risk reduction that SSO provides (fewer credential sets, centralized policy enforcement, unified audit logging) and the new risk it introduces (single point of failure, blast radius of IdP compromise), and identify two specific technical controls that mitigate the IdP compromise risk without abandoning federation.

2. In Challenge 1, you analyzed MFA fatigue (push bombing) as an attack against authenticator app push notifications. A security engineer proposes solving this by requiring users to enter a number shown on the login screen into the push notification (number matching). Explain why number matching reduces but does not eliminate the MFA fatigue attack surface, identify the residual attack scenario that number matching does not prevent, and explain why FIDO2 origin binding provides a fundamentally stronger guarantee than number matching against real-time phishing relay attacks.
