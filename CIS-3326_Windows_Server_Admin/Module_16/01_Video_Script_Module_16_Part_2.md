# Video Script: Module 16 — Capstone Review (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

### Introduction

Welcome back. In Part 1 we reviewed Modules 11 through 15. In Part 2 we
cover the foundational topics from Modules 1 through 10, work through
hybrid cloud scenarios, present exam strategy, and close with career
pathways for Windows Server administrators.

---

### Section 1: Foundations Review — Modules 1 through 5

Windows Server installation offers three options: Server Core (no GUI,
smallest attack surface), Desktop Experience (full GUI), and Nano Server
(container/cloud workloads only, no remote management via traditional
tools). For certification exams, Server Core is the recommended deployment
for production servers. GUI can be removed after installation using
`Uninstall-WindowsFeature Server-Gui-Mgmt-Infra`.

Active Directory Domain Services requires at least one domain controller
per domain. The PDC Emulator FSMO role handles password changes and time
synchronization. The RID Master issues RID pools to domain controllers.
The Infrastructure Master updates cross-domain group membership references.
Know the forest-wide roles (Schema Master, Domain Naming Master) versus
domain-wide roles (PDC Emulator, RID Master, Infrastructure Master).

AD recoverability has two paths. If AD Recycle Bin is enabled, use
`Restore-ADObject` to recover deleted objects without taking a DC offline.
If the Recycle Bin was not enabled before deletion, use `ntdsutil` authoritative
restore in DSRM after restoring from a system state backup.

Group Policy processes in LSDOU order: Local, Site, Domain, OU. Later
policies overwrite earlier ones for the same setting. Enforced (`No Override`)
forces a higher-level GPO to win regardless of lower OU settings.
Block Inheritance prevents higher-level GPOs from applying to an OU,
except Enforced GPOs. Security Filtering limits which objects receive
a GPO — by default, Authenticated Users applies the GPO to all.
WMI Filters conditionally apply the GPO based on system properties.

---

### Section 2: Networking — Modules 6 through 8

DNS zones have two storage types. Primary zones are writable and can be
stored in AD for automatic replication. Secondary zones are read-only
copies from a primary. Stub zones contain only NS, SOA, and glue records
and are used to resolve names in another zone without a full secondary.

For dynamic DNS security, configure the zone as AD-integrated and set
dynamic updates to Secure Only. Only domain-joined computers can then
register records.

DHCP failover in Windows Server provides high availability without requiring
a cluster. In Hot Standby mode, one server is active and one is passive.
In Load Balance mode, both servers share the lease pool. DHCP failover uses
continuous replication between the two partners so either can service requests.

Always On VPN is the current standard for remote access VPN. It works on
all Windows 10/11 editions, IPv4 networks, and non-domain devices. It uses
IKEv2, SSTP, or L2TP tunnels. DirectAccess is the legacy technology —
it requires Windows Enterprise edition, domain membership, and IPv6.
For any new deployment question on the certification exam, Always On VPN
is the correct answer.

---

### Section 3: Hybrid Cloud Scenarios

Certification exams increasingly test hybrid identity and management scenarios.
Here are the three most common.

Password Hash Synchronization (PHS) synchronizes a transformed hash of each
user's on-premises password to Azure AD. Authentication happens in the
cloud. This works even when on-premises DCs are unavailable. It is the
simplest configuration and provides the best cloud availability.

Pass-Through Authentication (PTA) sends authentication requests to on-premises
DCs via a lightweight agent. Passwords never leave the on-premises environment.
If the on-premises domain controllers go offline, cloud authentication fails.
This is the key trade-off: security of never storing passwords in the cloud
versus the availability risk of on-premises dependency.

Azure AD Federation with AD FS provides the richest conditional access and
claims-based policies but requires the most infrastructure. Federation means
cloud authentication redirects to an on-premises STS (AD FS) for token
issuance. Any on-premises outage affects cloud sign-in.

For management at scale, Windows Admin Center provides a browser-based
console for managing Windows Servers and clusters without requiring
individual RDP sessions. It can be deployed as a gateway server, allowing
administrators to manage servers from any browser on the internal network.

---

### Section 4: PowerShell and DSC — Exam Synthesis

PowerShell questions on Microsoft certification exams test cmdlet knowledge,
pipeline efficiency, and remoting. Remember three principles.

Filter left — pipe right. Use the cmdlet's built-in filter parameters
(such as `-Filter` with Get-ADUser, or `-FilterHashtable` with Get-WinEvent)
rather than piping all objects to Where-Object. This reduces the number of
objects in memory and improves performance dramatically on large data sets.

For DSC, the exam tests the difference between `ApplyOnly`, `ApplyAndMonitor`,
and `ApplyAndAutoCorrect`. Know that `Test-DscConfiguration` is read-only —
it checks compliance but makes no changes. Know that `Start-DscConfiguration`
applies the MOF file to the node.

For JEA, the two file types are the Session Configuration File (`.pssc`,
registered with `Register-PSSessionConfiguration`) and the Role Capability
File (`.psrc`, placed in the `RoleCapabilities` folder of a module). The
`[DSCLocalConfigurationManager()]` decorator on a `Configuration` block marks
it as a meta-configuration for LCM settings rather than node configuration.

---

### Section 5: Exam Strategy

You have 150 minutes to answer approximately 40 to 60 questions on Microsoft
Server Administration certification exams. Most questions are multiple choice
or multiple select.

Read the last sentence of every scenario question first. That sentence
contains the constraint — "without additional cost," "must not require
a reboot," "must work when the WAN link is down." The constraint eliminates
multiple answer choices immediately.

For multi-select questions (select two or three), eliminate the obviously
wrong choices first. Do not overthink second-choice answers — if two choices
are both defensible, the correct pair satisfies the entire scenario constraint.

Know the PowerShell cmdlets precisely. Exam distractors use parameter names
that do not exist for the stated cmdlet. If you know that `Get-Service` does
not have a `-Filter` parameter and `Register-ScheduledTask` does not have
a direct `-Execute` parameter, you can eliminate incorrect choices immediately.

Use Microsoft Learn as your final review resource. The AZ-800 and AZ-801
study guides list every exam objective with links to the official documentation.
Any objective you cannot explain in one sentence is a gap to address.

---

### Section 6: Career Pathways

Completing CIS-3326 and the associated Microsoft certification opens several
career paths in IT infrastructure.

Windows Server Administrator roles exist in virtually every organization.
The skills in this course — AD, DNS, DHCP, GPO, virtualization, security,
and automation — are the daily toolkit of infrastructure teams.

Cloud Infrastructure Engineer is the modern evolution of the Windows Server
Administrator. Organizations moving to Azure bring their AD DS, DNS, and
DHCP knowledge to hybrid Azure environments. The AZ-800 and AZ-801
certifications align with Azure Administrator Associate (AZ-104), which
is the next natural step.

Security-focused roles such as Systems Security Administrator and Security
Operations Center Analyst draw on the Module 14 material — firewall policy,
auditing, JEA, Credential Guard, and LAPS. The SC-200 and SC-300 certifications
build on that foundation.

DevOps and Automation Engineer roles value the PowerShell and DSC skills
from Module 15. Combining PowerShell with tools like Azure DevOps, GitHub
Actions, and Terraform creates infrastructure-as-code workflows that are
in high demand.

---

### Closing

Sixteen modules. Server installation, Active Directory, Group Policy, DNS,
DHCP, certificates, RDS, Hyper-V, Storage Spaces, security, and PowerShell
DSC automation. That is the Windows Server administration stack.

The certification exam tests whether you can apply these concepts in realistic
scenarios, not whether you have memorized syntax. Trust the understanding you
have built in the labs. Approach exam questions by identifying the constraint
first, eliminating distractors, and selecting the most specific tool that
satisfies all requirements.

Best of luck on your exam. It has been a pleasure to teach CIS-3326.
