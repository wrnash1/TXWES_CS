# Quiz: Module 14 - AD FS and Single Sign-On

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A company wants to allow its employees to access a third-party SaaS application using their existing Active Directory credentials without creating separate accounts in the SaaS system. The SaaS vendor supports SAML 2.0. Which Windows Server technology provides this federated single sign-on capability?

A) Active Directory Lightweight Directory Services (AD LDS), which creates a separate LDAP directory partition for the SaaS application's user accounts.
B) Active Directory Federation Services (AD FS), which issues SAML security tokens based on claims from the internal AD so users authenticate once and the token is trusted by the SaaS application.
C) Active Directory Rights Management Services (AD RMS), which encrypts documents shared with the SaaS application so they can only be opened by authorized AD users.
D) Azure AD Application Proxy, which publishes the on-premises SaaS application through a secure reverse proxy so employees can access it from the internet.

* **Correct Answer:** B) Active Directory Federation Services (AD FS), which issues SAML security tokens based on claims from the internal AD so users authenticate once and the token is trusted by the SaaS application.
* **Distractor Analysis:**
  * *Why A is incorrect:* AD LDS provides a standalone LDAP directory for application-specific data. It does not issue SAML tokens or provide federated SSO; it would require the SaaS application to query the LDAP directory directly rather than consuming a federation token.
  * *Why C is incorrect:* AD RMS protects documents and emails with persistent encryption based on usage rights — it is a data protection technology, not an identity federation or SSO mechanism.
  * *Why D is incorrect:* Azure AD Application Proxy publishes internal web applications to the internet with pre-authentication via Azure AD. It applies to on-premises applications, not to third-party SaaS applications that already exist in the cloud.

---

### Question 2

An organization deploys AD FS with a Web Application Proxy (WAP) server to allow external users to access the federation service from the internet. In which network location should the WAP server be placed, and why?

A) On the internal corporate network alongside the AD FS server, because WAP requires direct LDAP access to the domain controllers to pre-authenticate users.
B) In the DMZ (perimeter network), because WAP acts as a reverse proxy that accepts external requests and forwards them to the internal AD FS server without exposing AD FS or domain controllers directly to the internet.
C) In a dedicated cloud VNET, because WAP only functions when deployed in Azure and cannot run on on-premises hardware.
D) On the same server as AD FS, because co-locating WAP and AD FS reduces the number of firewall rules required for external access.

* **Correct Answer:** B) In the DMZ (perimeter network), because WAP acts as a reverse proxy that accepts external requests and forwards them to the internal AD FS server without exposing AD FS or domain controllers directly to the internet.
* **Distractor Analysis:**
  * *Why A is incorrect:* Placing WAP on the internal network defeats its security purpose. WAP is specifically designed to sit in the DMZ to create a security boundary between external internet traffic and internal AD FS/DC infrastructure. WAP does not require direct LDAP access to domain controllers — it proxies authentication requests to AD FS.
  * *Why C is incorrect:* WAP is a Windows Server role (part of the Remote Access role) that runs on on-premises Windows Server hardware. It is not an Azure-only service and can be deployed in any network location, including on-premises DMZ segments.
  * *Why D is incorrect:* Co-locating WAP and AD FS on the same server violates the security isolation principle. AD FS servers should be on the internal network protected by the internal firewall; WAP servers are exposed to the internet and represent a higher-risk attack surface. They must be separated.

---

### Question 3

An organization's on-premises Active Directory needs to be synchronized with Azure AD so that users can sign in to Microsoft 365 with their existing AD passwords. The organization requires that authentication always happen on-premises against the on-premises AD DS, and the passwords must never be sent to or stored in Azure AD. Which Azure AD Connect sign-in method satisfies these requirements?

A) Password Hash Synchronization (PHS), which copies a hash of the user's password hash to Azure AD so authentication can occur in the cloud without on-premises involvement.
B) Pass-Through Authentication (PTA), which validates user passwords against on-premises AD DS using an on-premises agent, so authentication never leaves the local environment and no password material is stored in Azure AD.
C) AD FS Federation, which redirects authentication to AD FS so on-premises AD processes the password, but requires deploying AD FS and WAP servers for external access.
D) Active Directory Seamless SSO with PHS, which uses Kerberos tickets for domain-joined devices so passwords appear not to leave the network even though a hash is stored in Azure AD.

* **Correct Answer:** B) Pass-Through Authentication (PTA), which validates user passwords against on-premises AD DS using an on-premises agent, so authentication never leaves the local environment and no password material is stored in Azure AD.
* **Distractor Analysis:**
  * *Why A is incorrect:* Password Hash Synchronization does store a transformed hash of the password in Azure AD so that Azure AD can authenticate users even when on-premises infrastructure is unavailable. This violates the requirement that no password material be stored in Azure AD.
  * *Why C is incorrect:* AD FS Federation also satisfies the requirement that authentication happen on-premises, but it requires deploying and maintaining AD FS servers and WAP servers — significantly more infrastructure than PTA. The scenario does not mention a federation requirement, making PTA the simpler and more direct answer.
  * *Why D is incorrect:* Seamless SSO combined with PHS still results in a password hash being stored in Azure AD. The "seamless" aspect refers to the user experience on domain-joined devices (no repeated prompts), not to where authentication data is stored.

---

### Question 4

An AD FS administrator needs to configure a Relying Party Trust for a new business partner's web application. The partner's application sends claims requests and requires the user's email address and department to be included in the SAML token. Which AD FS component is configured to extract the email address and department from Active Directory and transform them into outgoing claims in the token?

A) The Relying Party Trust endpoint URL, which specifies where the SAML token will be sent after claims are automatically included.
B) Claims Provider Trust rules on the AD FS server, which extract claims from the internal Active Directory and pass them to the Relying Party Trust.
C) Issuance Transform Rules (Claims Rules) on the Relying Party Trust, which define which AD attributes are read and how they are mapped to claim types included in the outgoing SAML token.
D) The AD FS proxy (WAP) configuration, which reads user attributes from Active Directory and appends them to the HTTPS request before forwarding to the Relying Party.

* **Correct Answer:** C) Issuance Transform Rules (Claims Rules) on the Relying Party Trust, which define which AD attributes are read and how they are mapped to claim types included in the outgoing SAML token.
* **Distractor Analysis:**
  * *Why A is incorrect:* The Relying Party Trust endpoint URL specifies the destination where AD FS sends the issued token — it is a routing and transport setting, not a claims selection or transformation configuration.
  * *Why B is incorrect:* Claims Provider Trust rules govern which claims are accepted from an incoming identity source (such as a partner federation server). For internal Active Directory users, the AD DS claims provider is the source; the transformation of those claims into outgoing SAML token claims is done by Issuance Transform Rules on the Relying Party Trust, not by Claims Provider Trust rules.
  * *Why D is incorrect:* WAP (Web Application Proxy) is a reverse proxy for forwarding requests — it does not read AD attributes or construct claims. Claims are assembled and signed by the AD FS server, not by WAP.

---

### Question 5

A company currently uses AD FS for SSO to federated applications. The security team requires that all sign-in attempts from outside the corporate network use multi-factor authentication (MFA), while internal network sign-ins may use password-only authentication. Which AD FS feature enforces this conditional access behavior?

A) Relying Party Trust endpoint binding, which restricts the SAML token to only be accepted from known internal IP address ranges.
B) AD FS Issuance Authorization Rules, which can evaluate the client network location (inside vs. outside the corporate network) and issue or deny the token based on whether MFA has been satisfied.
C) WAP Pre-Authentication configured to challenge all users for MFA before any request reaches the AD FS server, regardless of network location.
D) Azure AD Conditional Access Policies, which override AD FS authentication requirements and apply MFA rules to all sign-ins automatically.

* **Correct Answer:** B) AD FS Issuance Authorization Rules, which can evaluate the client network location (inside vs. outside the corporate network) and issue or deny the token based on whether MFA has been satisfied.
* **Distractor Analysis:**
  * *Why A is incorrect:* Relying Party Trust endpoint binding specifies transport endpoints (URL, binding type) for the application — it is not a conditional access or MFA enforcement mechanism and does not evaluate client network location.
  * *Why C is incorrect:* Configuring WAP pre-authentication to challenge all users for MFA would apply MFA to internal users as well, violating the requirement that internal sign-ins use password-only authentication. WAP processes only external requests, but the MFA challenge should be conditional, not universal.
  * *Why D is incorrect:* Azure AD Conditional Access applies to Azure AD-authenticated sign-ins. In a pure on-premises AD FS deployment without Azure AD Connect or hybrid integration, Azure AD Conditional Access does not control AD FS authentication decisions. The on-premises AD FS Issuance Authorization Rules are the correct mechanism.
