# Video Script: Module 16 — Capstone Review (Part 1)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 14–16 minutes

**Part 1 focus:** Capstone review of Modules 1–8 — Windows Server installation,
Active Directory, Group Policy, DNS, DHCP, certificates, Remote Desktop Services,
and Hyper-V. Exam-oriented summary of highest-yield topics, threshold values, and
PowerShell commands.

---

## Opening

Welcome to Module 16 — the capstone module for CIS-3326 Windows Server
Administration. This is the final module of the course.

Over fifteen modules you built a complete Windows Server administration skill set.
In Part 1 of this two-part review, we cover Modules 1 through 8. In Part 2, we
cover Modules 9 through 15 and work through exam strategy.

This is not a deep re-teach. It is a high-yield review of the concepts, thresholds,
PowerShell commands, and scenario patterns that appear most frequently on the
Microsoft Windows Server Administration exam.

---

## Module 1 — Windows Server Installation and Configuration

[SHOW SCREEN: Windows Server installation options comparison]
[Alt-text: Table showing Server Core, Desktop Experience, and Nano Server with columns for GUI, attack surface, and typical use case.]

Three installation options to know:

**Server Core** has no GUI shell. Smallest attack surface. Managed via PowerShell,
Server Manager remotely, or Windows Admin Center. Recommended for production
servers. GUI can be added or removed after installation.

**Desktop Experience** installs the full GUI. Requires more patching surface.
Appropriate for servers where GUI-dependent management tools are required.

**Nano Server** is a minimal container and cloud image with no local logon. It is
not used for traditional server roles. Know that Nano Server is the answer when
questions describe the smallest footprint for container workloads.

Key PowerShell: `Get-WindowsFeature`, `Install-WindowsFeature`, `Uninstall-WindowsFeature`.

---

## Modules 2 and 3 — Active Directory Domain Services and Group Policy

[SHOW SCREEN: FSMO roles table]
[Alt-text: Table with two columns: forest-wide roles (Schema Master, Domain Naming Master) and domain-wide roles (PDC Emulator, RID Master, Infrastructure Master).]

FSMO roles: know which are forest-wide vs. domain-wide.

- **Forest-wide:** Schema Master, Domain Naming Master (one per forest)
- **Domain-wide:** PDC Emulator, RID Master, Infrastructure Master (one per domain)

The PDC Emulator handles time synchronization and password change replication.
It is the most commonly queried FSMO on exam questions about authentication
failures and time skew.

AD object recovery: if **AD Recycle Bin** is enabled, use `Restore-ADObject`
to recover deleted objects within the tombstone lifetime without taking a DC
offline. If the Recycle Bin was not enabled before deletion, authoritative
restore with `ntdsutil` in Directory Services Restore Mode is required.

Group Policy processes in **LSDOU order**: Local, Site, Domain, OU. Later
policies overwrite earlier policies for the same setting. Three modifiers:

- **Enforced** (formerly No Override): higher-level GPO wins regardless of
  Block Inheritance below it.
- **Block Inheritance**: prevents higher-level policies from applying to an OU,
  except Enforced GPOs.
- **Security Filtering**: limits which accounts receive the GPO. Default is
  Authenticated Users; restrict to a group to scope the policy.

Key PowerShell: `Get-ADDomain`, `Get-ADForest`, `Move-ADDirectoryServerOperationMasterRole`,
`Get-GPO`, `New-GPO`, `Set-GPLink`.

---

## Modules 4 and 5 — DNS and DHCP

[SHOW SCREEN: DNS zone types comparison]
[Alt-text: Table with three rows: Primary (writable, AD-integrated option), Secondary (read-only copy), Stub (NS/SOA/glue only, for referral to another zone).]

DNS zone types for the exam:

- **Primary**: writable; can be AD-integrated for automatic replication via AD
- **Secondary**: read-only copy from a primary; good for read offloading
- **Stub**: contains only NS, SOA, and glue records; used to refer queries to
  another zone without hosting a full copy

For security: AD-integrated zones with **Secure Only** dynamic updates require
domain membership to register records, preventing spoofed DNS registrations.

DNSSEC signs zone records cryptographically. `Add-DnsServerResourceRecord`
and `Invoke-DnsServerSigningKeyRollover` are PowerShell cmdlets to know.

DHCP failover provides high availability without clustering.

- **Hot Standby**: one server active, one passive. Passive takes over when active
  is unreachable.
- **Load Balance**: both servers share the scope, each handling a percentage of
  leases (default 50/50).

DHCP failover requires the same scope on both servers. Use
`Add-DhcpServerv4Failover` to configure. Authorized with
`Add-DhcpServerInDC`.

---

## Module 6 — Certificate Services

[SHOW SCREEN: PKI hierarchy diagram]
[Alt-text: Three-tier text diagram: Offline Root CA at top, Policy/Subordinate CA in middle, Issuing CA at bottom with arrows pointing to end entities (servers, workstations, users).]

A **standalone Root CA** is typically kept offline to protect the root key.
It signs the certificate of a **subordinate CA**, which is the online issuing CA.
This is the two-tier PKI hierarchy used in enterprise environments.

Key exam points:

- `certreq.exe` submits certificate requests from the command line.
- `certutil.exe -verify` checks a certificate chain.
- Auto-enrollment distributes certificates to domain members automatically via
  Group Policy (Computer or User Configuration, Windows Settings, Security
  Settings, Public Key Policies).
- The **CDP** (CRL Distribution Point) is where clients download the Certificate
  Revocation List to check whether a certificate has been revoked.

---

## Module 7 — Remote Desktop Services

[SHOW SCREEN: RDS role services table]
[Alt-text: Table listing RD Session Host (port 3389), RD Gateway (HTTPS 443), RD Web Access (443), RD Connection Broker (session reconnection), RD Licensing (CALs, 120-day grace).]

RDS role services: know each one's function and port.

**RD Session Host** — where user sessions and applications run. All users on
a farm connect to Session Hosts.

**RD Gateway** — proxies RDP connections over HTTPS on port 443. This is the
exam answer for "allow RDP through a firewall that blocks port 3389." The Gateway
terminates the HTTPS tunnel and forwards the RDP session internally.

**RD Connection Broker** — reconnects disconnected sessions to the original
Session Host. Provides load balancing across a Session Host farm.

**RD Licensing** — issues Client Access Licenses. The 120-day grace period starts
when the first Session Host is configured. After grace expires, connections are
refused without valid Per Device or Per User CALs.

**RemoteApp** — publishes a single application rather than a full desktop. The
application window appears local but executes on the Session Host.

Key PowerShell: `Get-RDSessionHost`, `Get-RDUserSession`, `Disconnect-RDUser`,
`New-RDSessionDeployment`.

---

## Module 8 — Hyper-V Virtualization

[SHOW SCREEN: Hyper-V virtual switch types comparison]
[Alt-text: Table with three rows: External (VM to physical network + host), Internal (VM to VM + host, no physical NIC), Private (VM to VM only, no host access).]

Hyper-V is a **Type 1 hypervisor** running directly on hardware. After installation,
the host OS runs inside a privileged management partition.

**VM Generations:**

- **Generation 1**: BIOS firmware, IDE controllers, broader OS compatibility.
- **Generation 2**: UEFI firmware, Secure Boot, NVMe, PXE boot. Use for all
  new Windows Server 2012 R2+ and Linux deployments. For Linux Gen 2, set the
  Secure Boot template to `MicrosoftUEFICertificateAuthority`.

**Virtual switch types:** External, Internal, Private.

**Checkpoint types:**

- **Standard**: captures memory state and disk. Not application-consistent.
  Suitable for test environments only.
- **Production**: uses VSS (Volume Shadow Copy Service) for application-consistent
  point. Required for SQL Server, Exchange, and any production database VM.

**Live Migration**: moves a running VM between Hyper-V hosts with zero downtime.
Requires compatible CPU generations, domain membership or Shared Nothing
configuration, and for clustered migration, shared storage.

**Hyper-V Replica**: asynchronous DR replication. Does **not** require shared
storage. Configurable RPO: 30 seconds, 5 minutes, or 15 minutes.

Key PowerShell: `New-VMSwitch`, `New-VM`, `Set-VMFirmware`, `Checkpoint-VM`,
`Enable-VMReplication`, `Move-VM`.

---

## Closing — Part 1

Modules 1 through 8 establish the core infrastructure stack: deployment,
identity, policy, name resolution, address assignment, certificates,
remote access, and virtualization.

In Part 2 we review Modules 9 through 15 — covering file and print services,
security, PowerShell, storage, advanced security, and monitoring — then close
with exam strategy.

---

Module 16 Part 1 — End of Script
