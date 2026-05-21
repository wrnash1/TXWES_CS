# Reading Guide: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 03 – Installing and Configuring Active Directory Domain Services**! This week's study material covers the step-by-step process of deploying AD DS: adding the server role, promoting a server to a Domain Controller, and configuring the underlying DNS dependency. This is one of the most heavily tested operational sequences on the AZ-800 exam.

As a student, you will learn the difference between installing the AD DS role and promoting the server, how to perform a Read-Only Domain Controller (RODC) deployment, and how to clone or stage a Domain Controller in a virtualized environment. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Install-ADDSForest / Install-ADDSDomain**: PowerShell cmdlets used to promote a server to a Domain Controller. `Install-ADDSForest` creates a brand-new forest; `Install-ADDSDomain` adds a new child domain to an existing forest. Both require the server to already have the AD DS role installed.
* **AD DS Role vs. Domain Controller Promotion**: Installing the AD DS role via Server Manager or `Install-WindowsFeature AD-Domain-Services` copies the binaries but does not make the server a DC. A separate promotion step — either through the Server Manager wizard ("Promote this server to a domain controller") or PowerShell — is required.
* **Read-Only Domain Controller (RODC)**: A DC that holds a read-only copy of the AD DS database. RODCs are deployed in branch offices or locations with poor physical security because an attacker who steals the server cannot write changes back to the main directory.
* **SYSVOL and NETLOGON shares**: SYSVOL is a shared folder replicated to all DCs using DFSR; it stores Group Policy templates and logon scripts. NETLOGON is a subfolder of SYSVOL that clients use during the authentication process. Both must be healthy for GPOs and logon scripts to function.
* **Domain Functional Level (DFL) and Forest Functional Level (FFL)**: Settings that control which AD DS features are available. Raising the functional level requires all DCs in the domain or forest to run at least that version of Windows Server. Lower functional levels limit available features.
* **dcpromo (deprecated)**: The legacy command-line tool for promoting a DC, removed in Windows Server 2012. The current method is the Server Manager wizard or PowerShell cmdlets. Exam questions may reference it as a distractor.

---

### 2. Certification Exam Tips

* **Two-step deployment**: AZ-800 commonly asks about the AD DS deployment sequence. Step 1 is installing the role (`Install-WindowsFeature`). Step 2 is promoting the server (`Install-ADDSForest` or the Server Manager wizard). Answering with only one step is the most common exam mistake.
* **DNS is a prerequisite**: AD DS requires DNS to function. During promotion, the wizard offers to install DNS automatically. Know that AD-integrated DNS zones store zone data in AD DS itself, making them more secure and easier to replicate than file-based zones.
* **RODC credential caching**: RODCs use a Password Replication Policy (PRP) to control which accounts' credentials are cached locally. Sensitive accounts (Domain Admins) should be explicitly denied caching to limit exposure if the RODC is compromised.
* **Microsoft Learn Reference**: Review the step-by-step deployment guide at [Microsoft Learn – Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-) for installation options, prerequisites, and PowerShell syntax.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the AD DS installation documentation at [Microsoft Learn: Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-). Pay close attention to the PowerShell deployment examples and the RODC deployment section.
* **Required Video:** Watch the video lecture on **Installing and Configuring AD DS** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will install the AD DS role using PowerShell, promote a server to a Domain Controller to create a new forest, and verify successful deployment by checking SYSVOL replication status and DNS record creation using `dcdiag` and `nslookup`.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the AD DS installation guide at [Microsoft Learn: Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-).
* [ ] Watch the video lecture on **Installing and Configuring AD DS** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
