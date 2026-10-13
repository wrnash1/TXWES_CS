# Video Script: Module 03 - Installing and Configuring AD DS (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 03 - Installing and Configuring AD DS

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 13 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide — Module 03]**

Welcome to Module 03. I am Professor Nash. In Module 02 we learned what Active Directory Domain Services is — the hierarchy, the FSMO roles, the Global Catalog, Kerberos. In this module we are going to actually build it.

Module 03 is one of the most hands-on modules in this course. By the end of Part 2, you will have installed AD DS, promoted a server to a Domain Controller, added a second DC for redundancy, verified replication, and explored the key configuration decisions you make during and after promotion.

This module maps to AZ-800 objective: "Deploy and manage Active Directory Domain Services in on-premises and hybrid environments."

---

### [SEGMENT 2 — AD DS Installation Overview]

**[SHOW SCREEN: Diagram showing three-step process: Install Role, Promote Server, Verify Health]**

[Alt-text: Three-step diagram showing Step 1 Install the AD DS Role, Step 2 Promote the Server via Configuration Wizard or PowerShell, Step 3 Verify with dcdiag and repadmin.]

Installing Active Directory Domain Services is a two-step process that many new administrators confuse into one. These two steps are distinct and required in sequence.

**Step 1: Install the AD DS role.** This installs the binaries — the Active Directory services, the PowerShell AD module, the management tools. After this step, the server is still just a member server or standalone server. It is not yet a Domain Controller. It cannot authenticate domain users. Nothing has changed about how it functions in the network.

**Step 2: Promote the server to a Domain Controller.** This is the configuration step. You run either the AD DS Configuration Wizard in Server Manager (which triggers automatically after role installation) or the appropriate PowerShell cmdlet. During promotion you make decisions about what kind of DC this will be, what domain and forest it joins, and what the DNS configuration will be. After promotion and reboot, the server is a Domain Controller.

A third step — **verification** — is not optional in a production environment. You must run `dcdiag` and `repadmin` to confirm the DC is healthy and replicating before placing it into production.

---

### [SEGMENT 3 — Promotion Scenarios]

**[SHOW SCREEN: Three promotion options — New Forest, New Child Domain, Additional DC in Existing Domain]**

[Alt-text: Three boxes showing promotion scenarios: New Forest Root Domain, New Child Domain in Existing Forest, and Additional Domain Controller in Existing Domain.]

When you promote a server to a Domain Controller, you choose from three scenarios.

**New Forest Root Domain:** You are creating AD DS from scratch. There is no existing forest. You specify the forest root domain name (e.g., `corp.local`), the NetBIOS name, the forest and domain functional levels, and a DSRM (Directory Services Restore Mode) password. The PowerShell cmdlet is `Install-ADDSForest`.

**New Child Domain or Domain Tree in Existing Forest:** You already have a forest and are adding a new domain. A child domain extends an existing domain's namespace (`east.corp.local` as a child of `corp.local`). A new domain tree starts a separate namespace within the same forest. The PowerShell cmdlet is `Install-ADDSDomain`.

**Additional Domain Controller in Existing Domain:** The most common scenario in production — adding a second or third DC for redundancy and load distribution. You join an existing domain and promote. The new DC receives a full replica of the existing domain database through initial replication. The PowerShell cmdlet is `Install-ADDSDomainController`.

---

### [SEGMENT 4 — Functional Levels]

**[SHOW SCREEN: Table of forest and domain functional levels and their minimum DC versions]**

[Alt-text: A table showing functional levels: Windows Server 2008, 2008 R2, 2012, 2012 R2, 2016, and 2019/2022, with the minimum DC operating system required for each level.]

Functional levels control which AD DS features are available based on the oldest Domain Controller in the environment. Raising the functional level enables newer features but requires that all DCs in the domain (or forest) run at least the specified operating system version.

The two functional levels you must know:

**Domain Functional Level (DFL):** Controls features available within a single domain. Determined by the oldest DC OS version in that domain. Raising the DFL enables features like Fine-Grained Password Policies (requires 2008 DFL) and Managed Service Account features.

**Forest Functional Level (FFL):** Controls features available across the entire forest. Must be equal to or lower than the lowest DFL. Raising the FFL enables features like Active Directory Recycle Bin (requires 2008 R2 FFL).

Key rule for the exam: **You cannot lower a functional level once raised.** This is a one-way operation. If you raise the DFL to Windows Server 2016 and then add an older DC, that older DC cannot join the domain — it will be rejected during promotion. Plan your functional level decisions carefully in a mixed-version environment.

For new deployments, use the highest available functional level. For the AZ-800 lab environment, we use `WinThreshold` which represents Windows Server 2016 and later.

---

### [SEGMENT 5 — Prerequisites for DC Promotion]

**[SHOW SCREEN: Checklist of prerequisites for DC promotion]**

[Alt-text: A bulleted checklist showing prerequisites: static IP, DNS pointing to existing DC, time synchronization, correct OS edition, minimum hardware.]

Before promoting a server to a Domain Controller, you must verify these prerequisites.

First, the server must have a **static IP address**. A DC with a DHCP address is an operational nightmare — its DNS SRV records must be stable. Every promotion wizard will warn you if the adapter is set to DHCP.

Second, the server's **DNS client must point to an existing DC** that hosts the domain's DNS zone (for joining an existing domain), or must be configured to point to itself after DNS is installed (for a new forest). For a new forest, the DNS Server role is installed as part of promotion and the adapter's DNS will be updated to `127.0.0.1` automatically.

Third, **time synchronization** must be within 5 minutes of the existing domain (for joining an existing domain). If the clocks are out of sync by more than 5 minutes, Kerberos authentication fails and promotion will error.

Fourth, for adding a DC to an existing domain, the account performing promotion must have **Domain Admins** or **Enterprise Admins** group membership. For creating a new forest, local Administrator rights on the server are sufficient (there is no existing domain to authenticate against).

Fifth, the server must meet **minimum hardware requirements** — at minimum 2 GB RAM and 40 GB disk for a DC, though in production you would provision significantly more.

---

### [SEGMENT 6 — DNS and AD DS Integration]

**[SHOW SCREEN: Diagram showing DNS SRV records created by AD DS — _kerberos._tcp, _ldap._tcp, _gc._tcp]**

[Alt-text: A DNS zone diagram showing SRV record entries for _kerberos._tcp, _ldap._tcp, and _gc._tcp under the corp.local zone, each pointing to the Domain Controller's hostname.]

Active Directory is deeply integrated with DNS. Domain Controllers register Service Locator (SRV) records in DNS so that domain-joined computers can find services automatically. These records are in the format `_service._protocol.domain`.

The most important SRV records for AD DS:

- `_ldap._tcp.corp.local` — LDAP directory queries (port 389)
- `_kerberos._tcp.corp.local` — Kerberos authentication (port 88)
- `_gc._tcp.corp.local` — Global Catalog queries (port 3268)
- `_kpasswd._tcp.corp.local` — Kerberos password changes (port 464)

When a client computer joins the domain and a user logs in, their workstation queries DNS for `_ldap._tcp.corp.local` to find a Domain Controller to authenticate against. If these SRV records are missing or incorrect, domain logons fail.

This is why DNS is so critical to AD DS: without correct DNS SRV records, the domain effectively does not exist from the client's perspective.

Best practice: install the DNS Server role on every Domain Controller and configure DNS to use Active Directory-integrated zones. This automatically replicates DNS data to all DCs and eliminates single points of failure in DNS.

---

### [SEGMENT 7 — AD DS Replication]

**[SHOW SCREEN: Diagram showing replication between DC1 and DC2 within a site and DC1 to a remote site DC via a site link]**

[Alt-text: A diagram showing two Domain Controllers in Site A (DC1 and DC2) with arrows labeled Intra-site Replication, and another DC in Site B connected to DC1 with an arrow labeled Inter-site Replication via Site Link.]

When you have multiple Domain Controllers, changes made on any DC must propagate to all other DCs. This is AD DS replication.

**Intra-site replication** — between DCs in the same AD site — is triggered within 15 seconds of a change and uses the RPC over IP protocol. It is fast and designed for LAN-speed links.

**Inter-site replication** — between DCs in different AD sites — follows a schedule defined by site links. The default schedule replicates every 180 minutes but can be adjusted as low as 15 minutes. Inter-site replication uses either RPC over IP or SMTP (for very low-bandwidth or unreliable links).

The **KCC (Knowledge Consistency Checker)** automatically builds the replication topology based on site links you define. It creates connection objects between DCs to form a ring topology that ensures every DC can reach every other DC in at most two hops.

The **SYSVOL** folder — `C:\Windows\SYSVOL` — is also replicated between all DCs in the domain. SYSVOL holds Group Policy template files and logon scripts. Since Windows Server 2008, SYSVOL replication uses DFS-R (Distributed File System Replication), which is more efficient and reliable than the older FRS (File Replication Service) protocol.

---

### [SEGMENT 8 — DSRM and the AD DS Database]

**[SHOW SCREEN: Diagram showing the NTDS.dit database, transaction logs, and the DSRM boot option]**

[Alt-text: Diagram showing C:\Windows\NTDS containing NTDS.dit and log files, with an arrow to the DSRM boot option in Windows Boot Manager.]

During promotion, you are required to set a **Directory Services Restore Mode (DSRM) password**. This is the local Administrator password used when booting the DC into DSRM — a special recovery mode that loads the operating system without starting AD DS services.

DSRM is used for:

- Offline AD DS database maintenance and defragmentation using `ntdsutil`
- AD DS database restoration from backup
- Authoritative restore of objects deleted from Active Directory (restoring objects that have already replicated their deletion to all DCs)

DSRM is accessible by pressing F8 during boot and selecting Directory Services Restore Mode. In DSRM, the domain controller behaves like a standalone server — it does not authenticate domain accounts. You log in with the local Administrator account using the DSRM password you set during promotion.

**Critical warning:** The DSRM password is separate from the domain Administrator password. If you lose the DSRM password, you cannot perform AD DS recovery operations on that DC. Store DSRM passwords securely.

---

### [SEGMENT 9 — Certification Alignment Summary]

This module's content maps directly to AZ-800 objectives: deploying AD DS, adding DCs to existing domains, configuring functional levels, verifying domain health, and understanding DNS integration with AD DS.

In Part 2, we will walk through the PowerShell promotion commands, demonstrate `dcdiag` and `repadmin` verification, and preview the lab.

---

### Additional Resources

- [Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-)
- [AD DS deployment with PowerShell](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-200-)
- [Active Directory replication concepts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts)
- [dcdiag reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731968(v=ws.11))

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
