# Reading Guide: Module 02 - Active Directory Domain Services (AD DS) Overview

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 02 – Active Directory Domain Services (AD DS) Overview**! This week's study material introduces the architecture and core components of Active Directory, Microsoft's directory service for managing identities and access in Windows environments. AD DS is the central topic of the AZ-800 exam and the backbone of nearly every enterprise Windows network.

As a student, you will learn how domains, forests, and trusts are structured, what Domain Controllers do, and how the Global Catalog and FSMO roles keep the directory consistent. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Active Directory Domain**: A logical grouping of network objects (users, computers, groups) that share a common directory database, security policies, and trust relationships. All objects are stored in the AD DS database file (NTDS.dit) on every Domain Controller in that domain.
* **Domain Controller (DC)**: A Windows Server that hosts a writable copy of the AD DS database and handles authentication (Kerberos/NTLM), authorization, and directory replication. A minimum of two DCs per domain is recommended for fault tolerance.
* **Forest and Domain Tree**: A forest is the top-level AD DS container and security boundary, consisting of one or more domain trees that share a common schema and Global Catalog. A domain tree is a hierarchy of domains sharing a contiguous DNS namespace (e.g., corp.local and sales.corp.local).
* **Global Catalog (GC)**: A Domain Controller that stores a complete copy of all objects in its own domain and a partial, read-only copy of all objects in every other domain in the forest. It is required for universal group membership lookups and cross-domain searches.
* **FSMO Roles (Flexible Single Master Operations)**: Five specialized roles that prevent multi-master conflicts in AD DS. Forest-wide: Schema Master and Domain Naming Master. Domain-wide: PDC Emulator, RID Master, and Infrastructure Master. Each role can reside on a different DC.
* **Organizational Unit (OU)**: A container object within a domain used to organize users, computers, and other directory objects. OUs are the primary targets for Group Policy linking and administrative delegation — they do not create security boundaries.

---

### 2. Certification Exam Tips

* **Know all five FSMO roles and their functions**: AZ-800 scenario questions frequently describe a symptom (e.g., "users cannot change passwords after this server went offline") and ask you to identify which FSMO role is affected. The PDC Emulator is the most tested — it handles password changes, account lockout processing, and time synchronization.
* **OU vs. domain security boundary**: A common distractor is treating an OU as a security boundary. Only domains and forests create security boundaries. OUs exist purely for delegation and GPO application.
* **Global Catalog placement in multi-site environments**: Every AD site should have a GC server to prevent authentication failures during WAN outages. Know the symptoms of a missing GC — slow logon times and universal group membership errors.
* **Microsoft Learn Reference**: Study AD DS concepts at [Microsoft Learn – Active Directory Domain Services Overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) for authoritative definitions aligned with the exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the AD DS overview and architecture documentation at [Microsoft Learn: Active Directory Domain Services Overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview). Focus on the domain, forest, trust, and FSMO role sections.
* **Required Video:** Watch the video lecture on **AD DS Overview** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will explore the structure of an Active Directory domain using Active Directory Users and Computers (ADUC) and Active Directory Administrative Center (ADAC). You will identify Domain Controllers, locate FSMO role holders using `netdom query fsmo`, and examine the default OU structure created during domain promotion.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the AD DS overview at [Microsoft Learn: Active Directory Domain Services Overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).
* [ ] Watch the video lecture on **AD DS Overview** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.
