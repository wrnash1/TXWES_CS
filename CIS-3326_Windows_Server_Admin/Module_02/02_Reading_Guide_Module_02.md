# Reading Guide: Module 02 - Active Directory Domain Services Overview

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 02 introduces Active Directory Domain Services — the identity and access management backbone of every enterprise Windows environment. Understanding the AD DS logical hierarchy, the roles of Domain Controllers, FSMO roles, the Global Catalog, and Kerberos authentication is foundational knowledge for all remaining modules in this course and is central to the AZ-800 exam.

Work through each section carefully. The FSMO roles section in particular requires memorization — expect multiple scenario-based questions on the exam that require you to identify the correct role based on symptoms.

---

### 1. The AD DS Logical Hierarchy

#### 1.1 Four-Level Structure

Active Directory organizes objects in four logical levels. Each level has distinct characteristics, boundaries, and administrative implications.

| Level | Description | Boundary Type | Key Characteristic |
|---|---|---|---|
| Forest | Top-level container; shared schema and GC | Security boundary | One schema per forest |
| Tree | Hierarchy of domains with contiguous DNS namespace | None — part of forest | Parent-child DNS relationship |
| Domain | Core administrative unit; own database and DCs | Account boundary | Own administrators, own policies |
| Organizational Unit (OU) | Container within a domain | None — within domain | GPO and delegation target |

#### 1.2 Forest

The forest is the outermost container and the true security boundary in AD DS. All domains in a forest:

- Share a common schema (the definition of object types and attributes)
- Share a common Global Catalog
- Have automatic two-way transitive trusts between all domains
- Share a common Configuration partition in the directory

You cannot share schema or Global Catalog data across forest boundaries without establishing an explicit forest trust.

#### 1.3 Domain Trees

A domain tree is a group of domains sharing a contiguous DNS namespace. If the root is `corp.local`, children can be `east.corp.local`, `eu.corp.local`, etc. Parent-child trust relationships are created automatically during child domain promotion.

#### 1.4 Domains

The domain is the core unit of AD DS. Each domain has:

- Its own AD DS database partition (Domain NC)
- Its own set of Domain Controllers
- Its own Domain Admins group (which only has admin rights within that domain)
- Its own password and account lockout policies (at the domain level, or per OU with Fine-Grained Password Policies in 2008+)

#### 1.5 Organizational Units

OUs are the primary unit administrators interact with daily. They:

- Contain users, computers, groups, and other OUs
- Can have Group Policy Objects linked to them
- Can have administrative control delegated (e.g., Help Desk can reset passwords in a specific OU without domain admin rights)
- Do NOT create security boundaries — only domains/forests do

---

### 2. Domain Controllers

#### 2.1 Role of a Domain Controller

A Domain Controller (DC) is a Windows Server that hosts:

- The Active Directory Domain Services role
- The NTDS.dit database file (located in `C:\Windows\NTDS\`)
- The Kerberos Key Distribution Center (KDC)
- The LDAP directory service (port 389, or LDAPS port 636)
- DNS Server role (best practice — install DNS on every DC)

#### 2.2 Domain Controller Types

| DC Type | Description | Use Case |
|---|---|---|
| Full DC | Writable copy of all domain objects | Primary DCs in main sites |
| Read-Only DC (RODC) | Read-only copy; Password Replication Policy controls caching | Branch offices with limited physical security |
| Global Catalog DC | Holds partial read-only replicas of all forest objects | One per site minimum |

#### 2.3 Best Practices

- Deploy a minimum of two DCs per domain for fault tolerance
- Deploy a local DC at each site with more than 20 users to prevent WAN-dependent authentication
- Enable the Global Catalog on at least one DC per site
- Co-locate DNS with every DC

---

### 3. FSMO Roles

#### 3.1 Forest-Wide Roles (One Per Forest)

The **Schema Master** is the only DC that can make changes to the Active Directory schema — the blueprint defining object classes and attributes. Schema extensions (for Exchange, Lync/Teams, etc.) require the Schema Master to be online and reachable. There is one Schema Master per forest. After a schema change, changes replicate to all DCs.

The **Domain Naming Master** controls the addition and removal of domains in the forest. When running `Install-ADDSDomain` for a new child domain, the Domain Naming Master must be reachable. There is one Domain Naming Master per forest.

#### 3.2 Domain-Wide Roles (One Per Domain)

The **PDC Emulator** is the most operationally important FSMO role. It:

- Serves as the authoritative time source for all DCs in the domain
- Processes account lockouts — when a user is locked out on one DC, that DC contacts the PDC Emulator to check if the lockout should apply
- Prioritizes password change replication — when a user changes their password, the change is immediately replicated to the PDC Emulator before propagating to other DCs
- Handles legacy NT compatibility (NTLM, NT 4.0 BDC emulation)

The **RID Master** allocates pools of Relative Identifiers (RIDs) to other DCs. Every security principal (user, computer, group) gets a unique Security Identifier (SID) = Domain SID + RID. DCs request RID pools in advance. If the RID Master is offline, DCs exhaust their pools and cannot create new security principals.

The **Infrastructure Master** maintains cross-domain object references — for example, when a user from `eu.corp.local` is a member of a group in `corp.local`, the Infrastructure Master in `corp.local` tracks that reference. Important: in a multi-domain forest, the Infrastructure Master should NOT be placed on a DC that is also a Global Catalog server, because a GC already knows about all objects in all domains and the Infrastructure Master would never detect stale references. In a single-domain forest, this restriction does not apply.

#### 3.3 FSMO Role Summary Table

| Role | Scope | Function | Failure Impact |
|---|---|---|---|
| Schema Master | Forest | Controls schema modifications | Cannot extend schema |
| Domain Naming Master | Forest | Controls domain add/remove | Cannot add/remove domains |
| PDC Emulator | Domain | Time sync, password changes, lockouts | Auth issues, time skew |
| RID Master | Domain | Allocates RID pools to DCs | Cannot create new objects (when pools exhausted) |
| Infrastructure Master | Domain | Maintains cross-domain references | Stale cross-domain group memberships |

#### 3.4 Querying FSMO Roles

```powershell
# Domain-level FSMO roles
Get-ADDomain | Select-Object PDCEmulator, RIDMaster, InfrastructureMaster

# Forest-level FSMO roles
Get-ADForest | Select-Object SchemaMaster, DomainNamingMaster

# All five roles at once (legacy tool, still valid)
netdom query fsmo
```

---

### 4. Global Catalog

#### 4.1 What It Is

The Global Catalog (GC) is a designation applied to a Domain Controller that makes it store:

- A complete copy of all objects in its own domain (all attributes)
- A partial read-only copy of all objects in every other domain in the forest (a subset of commonly searched attributes)

#### 4.2 Why It Matters

The GC is required for:

- Universal Group membership resolution at logon
- Cross-domain and forest-wide object searches (e.g., searching the Global Address List in Exchange)
- Authentication of user principal names (UPNs) for logon

If no GC is available when a user logs on and the environment uses Universal Groups, the user may receive a "domain unavailable" error or log on with a cached profile only.

#### 4.3 Placement

- Every site should have at least one GC server
- The first DC in a new forest is automatically a GC server
- In small environments, all DCs are typically GC servers
- In a multi-domain forest, be selective about GC placement to control replication volume

```powershell
# Enable Global Catalog on a DC
Set-ADObject -Identity "CN=NTDS Settings,CN=DC2,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=corp,DC=local" `
    -Replace @{options='1'}

# Verify GC designation
Get-ADDomainController -Filter * | Select-Object Name, IsGlobalCatalog
```

---

### 5. Kerberos Authentication

#### 5.1 Overview

Windows domain authentication uses Kerberos v5 by default. Kerberos is defined in RFC 4120. NTLM is the fallback protocol used when Kerberos is unavailable (e.g., when accessing a server by IP address rather than hostname).

#### 5.2 Kerberos Authentication Flow

```text
Step 1: User logs in → Workstation sends AS-REQ to KDC
        KDC validates credential → Returns TGT (Ticket Granting Ticket)
        TGT lifetime: 10 hours by default

Step 2: User accesses a resource (file share, app) → Workstation sends TGS-REQ to KDC
        Workstation presents TGT → KDC returns Service Ticket for target resource

Step 3: Workstation presents Service Ticket to resource server
        Resource server validates ticket → Grants access
        Password never transmitted after Step 1
```

#### 5.3 Key Kerberos Parameters

| Parameter | Default Value | Significance |
|---|---|---|
| TGT Lifetime | 10 hours | Users must re-authenticate after 10 hours |
| Maximum Clock Skew | 5 minutes | DCs must be within 5 minutes of each other — PDC Emulator role |
| Service Ticket Lifetime | 10 hours | |
| Maximum Ticket Renewal | 7 days | |

The 5-minute clock skew tolerance is why the PDC Emulator's time synchronization function is so operationally critical. If a DC's clock drifts more than 5 minutes from the domain time, Kerberos authentication fails for clients authenticating through that DC.

---

### 6. Trust Relationships

#### 6.1 Trust Types

| Trust Type | Direction | Transitive | Created By |
|---|---|---|---|
| Parent-Child | Two-way | Yes | Automatically at promotion |
| Tree-Root | Two-way | Yes | Automatically at promotion |
| Forest Trust | Two-way (or one-way) | Yes (within forest) | Manual |
| External Trust | One-way or two-way | No | Manual |
| Shortcut Trust | One-way or two-way | No | Manual optimization |
| Realm Trust | One-way or two-way | Configurable | Manual (for MIT Kerberos) |

#### 6.2 Transitivity Rule

Transitive trusts mean: if A trusts B and B trusts C, then A trusts C. All intra-forest trusts are transitive. Inter-forest trusts are transitive within each forest but not across the forest boundary (forest trusts are needed for cross-forest access, and they are transitive within each participating forest).

---

### 7. AD DS Architecture Diagram

```text
FOREST: corp.local
  |
  +-- SCHEMA MASTER: DC1.corp.local
  +-- DOMAIN NAMING MASTER: DC1.corp.local
  |
  +-- TREE: corp.local
  |     |
  |     +-- DOMAIN: corp.local
  |     |     PDC Emulator: DC1.corp.local
  |     |     RID Master: DC1.corp.local
  |     |     Infrastructure Master: DC1.corp.local
  |     |     |
  |     |     +-- OU: Departments
  |     |     |     +-- OU: HR
  |     |     |     +-- OU: IT
  |     |     |     +-- OU: Finance
  |     |     |
  |     |     +-- OU: Domain Controllers
  |     |           DC1 (GC, Writable)
  |     |           DC2 (GC, Writable)
  |     |
  |     +-- DOMAIN: eu.corp.local
  |           (child domain, automatic 2-way transitive trust)
```

---

### 8. Exam Tips for Module 02

**Tip 1 — PDC Emulator symptoms:** Slow password change propagation, account lockout inconsistencies, time synchronization errors, and logon failures related to clock skew all point to the PDC Emulator. This is the most frequently tested FSMO role.

**Tip 2 — OU vs. domain boundary:** OUs are containers for organization and delegation, not security boundaries. The exam frequently uses "security boundary" in scenarios — the correct answer is always domain or forest.

**Tip 3 — Infrastructure Master and GC conflict:** In a multi-domain forest, place the Infrastructure Master on a DC that is NOT a Global Catalog server. In a single-domain forest, this restriction does not apply — all DCs can be GC servers regardless of which one holds the Infrastructure Master.

**Tip 4 — RODC use case:** Branch offices with limited physical security use RODCs. Password Replication Policy controls which accounts are cached. If compromised, only cached credentials are at risk.

**Tip 5 — Clock skew and Kerberos:** The maximum tolerated clock skew between domain members is 5 minutes. If this is exceeded, Kerberos tickets are rejected. The PDC Emulator is the authoritative time source — all DCs sync to it; clients sync to their authenticating DC.

**Tip 6 — Trust transitivity:** Trusts within a forest are automatic and transitive. Trusts between forests or between unrelated domains are manual. External trusts are non-transitive. Shortcut trusts are optional performance optimizations.

**Tip 7 — Global Catalog at every site:** A GC must be at each Active Directory site. Missing GC causes Universal Group membership lookup failures at logon, especially when WAN is unavailable.

**Tip 8 — netdom query fsmo:** Know this command. It is commonly used in troubleshooting steps described in exam scenarios and is a practical tool you will use in the field.

---

### 9. Key Terms Glossary

| Term | Definition |
|---|---|
| NTDS.dit | The Active Directory database file stored on every DC in `C:\Windows\NTDS\` |
| KDC | Key Distribution Center — the Kerberos service running on every DC |
| TGT | Ticket Granting Ticket — Kerberos proof-of-identity issued at logon |
| LDAP | Lightweight Directory Access Protocol — used to query and modify the AD directory (port 389) |
| GC | Global Catalog — DC role that stores forest-wide partial object replicas |
| FSMO | Flexible Single Master Operations — five roles preventing multi-master conflicts |
| PDC Emulator | Domain-wide FSMO handling time sync, password changes, account lockouts |
| RID Master | Domain-wide FSMO allocating Relative Identifier pools to DCs |
| Infrastructure Master | Domain-wide FSMO maintaining cross-domain object references |
| Schema Master | Forest-wide FSMO controlling schema modifications |
| Domain Naming Master | Forest-wide FSMO controlling domain additions and removals |
| RODC | Read-Only Domain Controller for physically insecure locations |
| OU | Organizational Unit — domain container for GPO linking and delegation |
| Trust | A configured relationship allowing authentication across domain or forest boundaries |

---

### 10. Study Checklist

- Read Section 1 (Hierarchy) and memorize the four levels and their boundary types
- Read Section 2 (Domain Controllers) and understand writable DC vs. RODC vs. GC
- Read Section 3 (FSMO Roles) and memorize all five roles, their scope, function, and failure impact
- Read Section 4 (Global Catalog) and understand GC placement rules
- Read Section 5 (Kerberos) and memorize the 5-minute clock skew tolerance
- Read Section 6 (Trusts) and understand the trust type table
- Review the Architecture Diagram in Section 7
- Review all 8 Exam Tips in Section 8
- Review the Key Terms Glossary in Section 9
- Complete the Lab activity for Module 02
- Complete the Quiz for Module 02
- Post your initial Discussion response by Wednesday 11:59 PM

---

### Additional Reading

- [Active Directory Domain Services overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Understanding AD DS design](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-ad-ds-design)
- [FSMO roles in Active Directory](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-roles)
- [Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)
- [Active Directory trusts](https://learn.microsoft.com/en-us/azure/active-directory-domain-services/concepts-forest-trust)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 02 topics:

**1. Microsoft Learn — Deploy and manage Active Directory Domain Services**
<https://learn.microsoft.com/en-us/training/modules/deploy-manage-active-directory-domain-services/>
Hands-on Microsoft Learn module covering AD DS installation, domain promotion, and FSMO role management with browser-based sandbox exercises.

**2. Microsoft Learn — Manage Active Directory objects**
<https://learn.microsoft.com/en-us/training/modules/manage-active-directory-objects/>
Covers creating and managing users, computers, groups, and OUs using PowerShell and the graphical tools — directly complementing the lab work in this module.

**3. Microsoft Docs — FSMO placement and optimization**
<https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-placement-and-optimization-on-active-directory-domain-controllers>
Deep-dive reference on FSMO role placement best practices, common failure scenarios, and how to seize or transfer roles. Essential reading before the midterm.

**4. Microsoft Learn — Understand Kerberos authentication in Active Directory**
<https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview>
Official Kerberos protocol overview including ticket lifecycle, clock skew tolerances, and troubleshooting authentication failures — covers the exact concepts tested in Questions 7 and 18.
