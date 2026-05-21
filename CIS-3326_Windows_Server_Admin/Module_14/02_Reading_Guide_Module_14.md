# Reading Guide: Module 14 - Active Directory Federation Services (AD FS) and SSO

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 14 – Active Directory Federation Services (AD FS) and Single Sign-On (SSO)**! This week's study material covers how AD FS extends identity beyond the on-premises domain, enabling users to authenticate to external web applications and cloud services using their existing Active Directory credentials. AD FS and SSO are tested on AZ-800 in the context of hybrid identity and claims-based authentication.

As a student, you will learn how AD FS federates identity between organizations, how Web Application Proxy (WAP) secures external access, and how Azure AD Connect bridges on-premises AD with Microsoft Entra ID (Azure AD) for seamless SSO to Microsoft 365 and SaaS applications. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Active Directory Federation Services (AD FS)**: A Windows Server role that implements claims-based authentication and federated identity. It issues security tokens (SAML, OAuth, WS-Federation) that allow users authenticated by one organization's AD to access resources in a trusting partner organization or cloud service without re-entering credentials.
* **Claims-Based Authentication**: An identity model where a trusted authority (the AD FS server) issues a token containing "claims" — assertions about the user such as name, email, group membership, or department. The relying party (the application) trusts these claims without querying AD directly.
* **Relying Party Trust**: A configuration on the AD FS server that defines the relationship with an application or partner organization that will consume tokens. Each web application or SaaS service added to AD FS is configured as a Relying Party Trust with its own claims issuance rules.
* **Web Application Proxy (WAP)**: A role service (part of Remote Access) deployed in the DMZ that acts as a reverse proxy and pre-authentication gateway for AD FS. External users authenticate with AD FS through WAP before their requests reach internal applications, keeping AD FS servers off the public internet.
* **Azure AD Connect (Microsoft Entra Connect)**: A tool that synchronizes on-premises AD DS objects (users, groups, contacts) to Microsoft Entra ID (Azure AD), enabling hybrid identity. It supports Password Hash Synchronization (PHS), Pass-Through Authentication (PTA), and Federation (with AD FS) as authentication methods.
* **Single Sign-On (SSO)**: The ability for a user to authenticate once (at domain logon or AD FS) and access multiple applications and services without re-entering credentials. In a hybrid environment, SSO spans on-premises AD applications and cloud services like Microsoft 365 and Salesforce.

---

### 2. Certification Exam Tips

* **AD FS authentication method comparison**: AZ-800 scenarios test when to choose Password Hash Synchronization vs. Pass-Through Authentication vs. Federation (AD FS). PHS is simplest and works even when on-premises infrastructure is unavailable. PTA requires on-premises agents to be online. Federation with AD FS provides the most control but is the most complex to maintain.
* **WAP placement in the DMZ**: The Web Application Proxy must be placed in the DMZ (perimeter network) — never on the internal network. It communicates inbound with external users and outbound to the internal AD FS server over specific ports (443 for HTTPS, 49443 for certificate authentication).
* **Claims rules and attribute stores**: AD FS claim rules can pull attributes from AD (the default attribute store), LDAP directories, or SQL databases. AZ-800 questions may ask how to pass a custom claim (e.g., department attribute) to a relying party — the answer involves an Issuance Transform Rule.
* **Microsoft Learn Reference**: Review AD FS and hybrid identity documentation at [Microsoft Learn – AD FS Overview](https://learn.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) and [Microsoft Learn – Azure AD Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect) for current deployment guidance.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the AD FS and hybrid identity documentation at [Microsoft Learn: Active Directory Federation Services](https://learn.microsoft.com/en-us/windows-server/identity/active-directory-federation-services) and [Microsoft Learn: What is Azure AD Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect). Focus on authentication method comparison, WAP deployment, and Relying Party Trust configuration.
* **Required Video:** Watch the video lecture on **AD FS and Single Sign-On** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will install and configure AD FS on a Windows Server, configure a test Relying Party Trust for a sample web application, and verify that a domain user can authenticate to the application using their AD credentials via the AD FS sign-in page.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the AD FS documentation at [Microsoft Learn: Active Directory Federation Services](https://learn.microsoft.com/en-us/windows-server/identity/active-directory-federation-services).
* [ ] Read the hybrid identity documentation at [Microsoft Learn: What is Azure AD Connect](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect).
* [ ] Watch the video lecture on **AD FS and Single Sign-On** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
