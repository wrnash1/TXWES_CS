# Video Script: Module 02 - Active Directory Domain Services Overview (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 02 - Active Directory Domain Services (AD DS) Overview

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 14 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 02]**

Welcome to Module 02. I am Professor Nash. Last module we installed and configured Windows Server. Now we turn to the most important role that Windows Server plays in enterprise environments: Active Directory Domain Services, or AD DS.

If Module 01 was about getting a server running, Module 02 is about understanding what that server is going to become — a Domain Controller that authenticates every user, every computer, and every service in your organization.

This module covers the conceptual architecture of AD DS: the logical hierarchy from forests down to objects, the role of Domain Controllers, the five FSMO roles, Kerberos authentication, and trust relationships between domains. Part 2 will walk through the demonstration in Active Directory Users and Computers and the PowerShell equivalents.

This content maps to AZ-800 objective area: "Plan and implement an on-premises Active Directory Domain Services infrastructure."

---

### [SEGMENT 2 — Why Active Directory Exists]

**[SHOW SCREEN: Diagram showing 500 computers each with a local SAM database vs. one DC serving all 500]**

[Alt-text: Two diagrams side by side. Left: 500 computer icons each with a small database icon labeled SAM, illustrating distributed local account management. Right: 500 computer icons all connected to a single server labeled Domain Controller with a central AD DS database.]

Before Active Directory, administrators managed user accounts locally on each machine. If your organization had 500 computers, you had 500 separate databases of usernames and passwords. Adding a new employee meant creating an account on every machine they might use. Password changes were a per-machine operation. Auditing who accessed what was nearly impossible.

Active Directory solves this with a centralized directory service. Every user has one account in the AD database. That account works on any computer joined to the domain. The administrator creates the account once. Password changes happen in one place. Access control, group membership, and policy enforcement all flow from one central store.

This is the fundamental value of AD DS: single-point identity management for an entire organization.

---

### [SEGMENT 3 — The AD DS Logical Hierarchy]

**[SHOW SCREEN: Pyramid diagram — Forest at top, Trees below, Domains below Trees, OUs inside Domains]**

[Alt-text: A hierarchical pyramid diagram. The top tier is labeled Forest. The second tier shows two tree shapes labeled Tree 1 and Tree 2. The third tier shows circles labeled Domains inside each tree. The bottom tier shows folder icons labeled Organizational Units inside each domain.]

AD DS organizes objects in a strict four-level logical hierarchy. Understanding each level is critical for both the AZ-800 exam and practical administration.

**The Forest** is the topmost container and the ultimate security boundary. All domains in a forest share a common schema — the blueprint that defines what types of objects exist and what attributes they have — and a common Global Catalog. A forest can contain one or many domain trees. An organization typically has one forest. A second forest means a separate organization or a separate security boundary.

**Domain Trees** are hierarchies of domains that share a contiguous DNS namespace. If your root domain is `corp.local`, a child domain for your European operations might be `eu.corp.local`. Together they form a single tree. The namespace is contiguous because every subdomain extends the parent name.

**Domains** are the core administrative unit. Each domain has its own domain database, its own Domain Controllers, and its own administrator account. Domains are the account boundary — a user account in `corp.local` is a different object than a user account in `eu.corp.local`. Domains are not security boundaries between each other within a forest; the forest is the security boundary.

**Organizational Units (OUs)** are containers within a domain used to organize objects — users, computers, groups, and other OUs. OUs are the primary targets for Group Policy Objects and administrative delegation. A common OU structure might have top-level OUs for Departments, Locations, or Object Types, with nested OUs underneath. OUs do not create security boundaries; they exist purely for organization and policy application.

This four-level structure — Forest, Tree, Domain, OU — determines how permissions, policies, and trust relationships work throughout your organization.

---

### [SEGMENT 4 — Domain Controllers]

**[SHOW SCREEN: Diagram showing two Domain Controllers with bidirectional replication arrows, and client computers authenticating to each]**

[Alt-text: Two server icons labeled DC1 and DC2 with bidirectional arrows labeled Replication between them. Client computer icons point to both DCs with arrows labeled Authentication Request.]

A **Domain Controller** is a Windows Server that has been promoted to host the AD DS database. Specifically, it stores a file called NTDS.dit — the NT Directory Services database — and hosts the Kerberos authentication service, LDAP directory service, and AD DS replication.

Every DC in a domain holds a complete, writable copy of the domain's directory database. When you create a new user on DC1, that change replicates to DC2 within minutes. This multi-master replication model means any DC can process any directory change.

Best practice is a minimum of two Domain Controllers per domain. With only one DC, a hardware failure takes down authentication for the entire domain — no one can log in. Two DCs provide fault tolerance. For branch offices, deploying a local DC prevents authentication traffic from crossing the WAN and protects against WAN link failures.

**Read-Only Domain Controllers (RODCs)** are a specialized DC type for locations with limited physical security — such as branch offices where the server might be in an unlocked closet. An RODC holds a read-only copy of the directory. If the RODC is stolen, the attacker cannot extract writeable credentials for the entire domain. Administrators control which account passwords are cached on the RODC through a Password Replication Policy.

---

### [SEGMENT 5 — The Five FSMO Roles]

**[SHOW SCREEN: Diagram showing five FSMO role names divided into forest-wide and domain-wide categories]**

[Alt-text: A table diagram with two sections. The Forest-Wide section contains Schema Master and Domain Naming Master. The Domain-Wide section contains PDC Emulator, RID Master, and Infrastructure Master.]

Because AD DS uses multi-master replication — where any DC can process changes — certain operations require a single authoritative source to prevent conflicts. These are the Flexible Single Master Operations roles, or FSMO roles. There are five total: two forest-wide and three domain-wide.

**Forest-Wide FSMO Roles:**

The **Schema Master** controls all changes to the Active Directory schema. When you install an application like Exchange that extends the AD schema with new object classes and attributes, that extension must flow through the Schema Master. There is one Schema Master per forest.

The **Domain Naming Master** controls the addition and removal of domains in the forest. When you create a new child domain or remove one, the Domain Naming Master must be reachable. There is one Domain Naming Master per forest.

**Domain-Wide FSMO Roles:**

The **PDC Emulator** is the most operationally critical FSMO role. It handles: password changes (when a DC processes a bad password, it checks the PDC Emulator before locking the account), account lockout policy enforcement, time synchronization (all DCs in the domain synchronize their clocks to the PDC Emulator), and compatibility with legacy Windows NT clients. There is one PDC Emulator per domain.

The **RID Master** allocates pools of Relative Identifiers to other DCs. Every security principal — user, computer, group — gets a unique Security Identifier (SID) constructed from the domain SID plus a RID. DCs request pools of RIDs from the RID Master in advance to avoid SID conflicts. There is one RID Master per domain.

The **Infrastructure Master** maintains references to objects in other domains within the forest. It keeps cross-domain object references up to date. In a single-domain forest this role has nothing to do — there are no cross-domain references. Important note: the Infrastructure Master should not run on a DC that is also a Global Catalog server in a multi-domain forest, because the GC would never need to update cross-domain references (it already knows about all of them). There is one Infrastructure Master per domain.

---

### [SEGMENT 6 — Global Catalog]

**[SHOW SCREEN: Diagram showing a GC server with full local domain objects and partial replicas of other domain objects]**

[Alt-text: A server icon labeled Global Catalog showing a full database for Domain A and smaller partial database icons for Domain B and Domain C, representing partial read-only replicas.]

The **Global Catalog** is not an FSMO role — it is a designation applied to specific Domain Controllers. A Global Catalog server stores a complete copy of all objects in its own domain, plus a partial read-only copy of all objects in every other domain in the forest.

The Global Catalog enables two critical functions. First, it supports cross-domain object searches. When a user searches the entire forest for a colleague, the search hits the GC rather than querying every domain separately. Second, it provides Universal Group membership lookups during logon. When a user logs in, Kerberos needs to know all of the user's group memberships — including Universal Groups from other domains — to build an authorization token. This lookup requires a GC server.

In a multi-site environment, every Active Directory site should have at least one Global Catalog server. Without a local GC, client logons require a WAN query to a remote GC. If the WAN link is down, logon may fail or be delayed significantly.

---

### [SEGMENT 7 — Authentication: Kerberos]

**[SHOW SCREEN: Kerberos ticket exchange diagram — client, KDC, and resource server]**

[Alt-text: A three-step diagram showing 1) a client requesting a Ticket Granting Ticket from the KDC, 2) the client using the TGT to request a service ticket, and 3) the client presenting the service ticket to the resource server for access.]

Windows domain authentication uses the Kerberos protocol by default. Kerberos is a ticket-based authentication system that avoids sending passwords over the network after initial login.

The process works in three steps. When a user logs in to a domain, their workstation contacts the Key Distribution Center — which runs on every Domain Controller — and requests a Ticket Granting Ticket, or TGT. The TGT is encrypted with the user's password hash and serves as proof of identity. When the user accesses a network resource — a file share, a web app — their workstation uses the TGT to request a Service Ticket for that specific resource. The resource server validates the Service Ticket and grants access.

The key benefit of Kerberos is that passwords are never transmitted after the initial login. The exam will ask you about Kerberos ticket lifetimes (default 10 hours), maximum tolerance for synchronization errors (default 5 minutes — this is why the PDC Emulator time synchronization role matters), and the fact that NTLM is used as a fallback when Kerberos is unavailable.

---

### [SEGMENT 8 — Trust Relationships]

**[SHOW SCREEN: Diagram showing parent-child trusts within a forest and an external trust to a separate forest]**

[Alt-text: A forest diagram showing automatic two-way transitive trusts between parent and child domains, and a separate one-way external trust arrow pointing from the forest to an external domain outside the forest boundary.]

Trust relationships determine whether users in one domain can access resources in another.

Within a forest, all trusts are created automatically during domain promotion and are **two-way transitive**. If Domain A trusts Domain B, and Domain B trusts Domain C, then Domain A implicitly trusts Domain C. Users in any domain can access resources in any other domain within the same forest, subject to permissions.

Between forests, trusts must be manually created. A **forest trust** connects two entire forests and is transitive within each forest. An **external trust** connects one specific domain in one forest to one specific domain in another — it is non-transitive and one-directional unless explicitly configured as two-way.

A **shortcut trust** is a manual optimization within a large forest. If users in a domain deep in one tree frequently access resources in a domain deep in another tree, the authentication chain must walk up through all parent domains and back down. A shortcut trust creates a direct path, speeding up authentication.

---

### [SEGMENT 9 — Summary and Part 2 Preview]

**[SHOW SCREEN: Summary slide — AD DS hierarchy, DC roles, FSMO, GC, Kerberos, Trusts]**

To summarize Part 1: Active Directory Domain Services provides centralized identity management organized in a four-level hierarchy — Forest, Tree, Domain, OU. Domain Controllers host the AD database and replicate changes to each other. Five FSMO roles prevent multi-master conflicts. The Global Catalog enables cross-domain searches and universal group lookups. Kerberos provides ticket-based authentication without sending passwords over the network. Trusts enable cross-domain resource access.

In Part 2 we will open Active Directory Users and Computers, explore the default OU structure, create an OU, and query FSMO role holders using PowerShell.

---

### Additional Resources

- [Active Directory Domain Services overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Understanding AD DS design](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/understanding-ad-ds-design)
- [FSMO roles reference](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/fsmo-roles)
- [Kerberos authentication overview](https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview)

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
