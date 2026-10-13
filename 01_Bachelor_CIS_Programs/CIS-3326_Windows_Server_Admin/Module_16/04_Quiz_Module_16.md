# Quiz: Module 16 — Capstone Review

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

This capstone quiz covers all 15 modules. Select the best answer for each
question. Each question is worth 5 points (20 questions, 100 points total).

---

### Question 1

An organization requires that all RDP connections from external users use
port 443 because the perimeter firewall blocks all other ports. Which RDS
role service makes this possible?

A) RD Session Host, by changing the RDP listener port to 443

B) RD Gateway, which proxies RDP connections over HTTPS on port 443

C) RD Connection Broker, which redirects port 3389 traffic to port 443

D) RD Web Access, which tunnels RDP inside HTTP on port 80

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Changing the RDP listener port on the Session Host
    to 443 would conflict with HTTPS services and requires a firewall exception
    for 443 directly to the Session Host. RD Gateway is the correct perimeter
    component that accepts HTTPS on 443 and proxies RDP inside the tunnel.
  - Why C is incorrect: The Connection Broker handles session load balancing
    and reconnection — it does not proxy port traffic. It does not have a
    port-translation or tunneling function.
  - Why D is incorrect: RD Web Access provides a browser portal for launching
    RemoteApp programs and desktop connections. It does not tunnel RDP inside
    HTTP at the protocol level.

---

### Question 2

An administrator needs to run a script block on 30 servers simultaneously
and collect structured output. Which PowerShell approach is correct?

A) `Enter-PSSession` in a `foreach` loop, connecting to one server at a time

B) `Invoke-Command -ComputerName` with all 30 server names, which fans out
   execution to all servers in parallel

C) `New-PSSession` in a `foreach` loop, executing `Invoke-Command -Session`
   sequentially on each session

D) `Connect-PSSession` with all 30 names listed in the `-ComputerName`
   parameter

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Enter-PSSession` is interactive and one-to-one.
    Using it in a loop processes one server at a time sequentially, which
    defeats the purpose of fleet administration.
  - Why C is incorrect: Running `Invoke-Command -Session` sequentially in a
    `foreach` loop processes each session in turn. `Invoke-Command -ComputerName`
    with multiple names executes on all targets simultaneously.
  - Why D is incorrect: `Connect-PSSession` reconnects to a disconnected
    session on a single computer. It does not accept a list of computer names
    and does not run script blocks.

---

### Question 3

A new Windows Server 2022 VM must boot from UEFI, support Secure Boot, and
use NVMe storage. Which VM generation provides these capabilities?

A) Generation 1, because it supports all legacy and modern firmware options

B) Generation 2, which uses UEFI firmware, supports Secure Boot, and uses
   synthetic NVMe storage controllers

C) Either generation, because Hyper-V abstracts the firmware from the
   guest operating system

D) Generation 1 with a UEFI firmware upgrade applied through Hyper-V Manager

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Generation 1 VMs use BIOS firmware only. They do not
    support UEFI, Secure Boot, or NVMe storage. BIOS and UEFI are fixed at
    VM creation time and cannot be changed after the VM is created.
  - Why C is incorrect: Hyper-V does not abstract firmware — Generation 1
    and Generation 2 VMs have fundamentally different firmware and device
    models. The firmware type is a permanent property set at VM creation.
  - Why D is incorrect: There is no UEFI firmware upgrade for Generation 1
    VMs in Hyper-V. Generation must be selected at creation time.

---

### Question 4

A Hyper-V administrator needs a checkpoint type that is safe to use for a
VM running a SQL Server database. Which checkpoint type is appropriate and why?

A) Standard checkpoint, because it captures memory state and is consistent
   with running transactions

B) Production checkpoint, which uses Volume Shadow Copy Service to create an
   application-consistent point without capturing uncommitted memory state

C) Either type is equivalent for database VMs because the database engine
   handles its own crash recovery

D) Standard checkpoint with the SQL Server service stopped before the snapshot
   to ensure consistency

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Standard checkpoints include the memory state, which
    can capture uncommitted transactions in flight. Restoring a standard
    checkpoint on a database VM can leave the database in an inconsistent
    state requiring recovery.
  - Why C is incorrect: While SQL Server handles crash recovery, the goal of
    a checkpoint is to create a consistent recovery point. Production
    checkpoints coordinate with VSS to quiesce the database before capturing
    state, which is the recommended approach.
  - Why D is incorrect: Stopping the SQL Server service before a Standard
    checkpoint defeats the purpose of online checkpointing. Production
    checkpoints achieve VSS-consistent state without requiring service
    interruption.

---

### Question 5

An organization needs a Storage Spaces virtual disk that can survive the
simultaneous failure of two disks. Which resiliency type and minimum disk
count is required?

A) Two-way mirror with four disks

B) Parity with five disks

C) Three-way mirror with five disks

D) Dual parity with seven disks

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: Two-way mirror stores two copies of each data stripe.
    It can survive the failure of one disk, not two.
  - Why B is incorrect: Single parity (similar to RAID 5) can survive one
    disk failure. A two-disk failure would result in data loss.
  - Why C is incorrect: Three-way mirror stores three copies and can survive
    two simultaneous disk failures, but it requires a minimum of five disks —
    however, the question can also be answered by dual parity, which is the
    more space-efficient option for two-disk fault tolerance at seven disks.
    When the scenario specifies minimizing disk count for two-failure tolerance,
    three-way mirror at five disks is the answer. Dual parity at seven disks
    provides two-disk fault tolerance with less space overhead than three-way
    mirror at larger scales.

---

### Question 6

A headless server in a locked data center must decrypt its BitLocker-protected
OS volume automatically when it boots on the corporate network, without
requiring an administrator to enter a PIN or connect a USB drive. Which
BitLocker protector achieves this?

A) TPM-only protector, which unlocks automatically based on hardware measurements

B) Network Unlock, which decrypts the drive when the server boots on the
   trusted corporate network using a WDS key

C) Recovery Key protector, which is entered automatically via a startup
   script

D) TPM + PIN, which automatically supplies the PIN from an AD-stored credential

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: TPM-only protectors also unlock automatically at boot,
    but they do not verify that the server is on the trusted corporate network.
    A stolen server with an intact TPM could decrypt the drive anywhere.
    Network Unlock adds the network location requirement.
  - Why C is incorrect: Recovery keys are 48-digit numeric keys for emergency
    access. They cannot be automatically supplied by a startup script — that
    would negate their security purpose entirely.
  - Why D is incorrect: TPM + PIN always requires an administrator to type the
    PIN at the console or via a remote management interface. There is no
    mechanism to automatically supply the PIN from Active Directory.

---

### Question 7

An administrator configures a GPO at the Domain level that sets a screen saver
timeout. A child OU has Block Inheritance enabled. The domain administrator
then enables the Enforced option on that GPO. What happens?

A) The Enforced GPO is still blocked because Block Inheritance takes
   precedence over Enforced.

B) The Enforced GPO applies to the child OU regardless of Block Inheritance,
   because Enforced overrides Block Inheritance.

C) Block Inheritance removes the GPO from the domain and it stops applying
   to all OUs.

D) The Enforced GPO applies to new users but not existing users in the
   blocked OU.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The GPO processing rule is that Enforced (No Override)
    beats Block Inheritance. Block Inheritance prevents normal higher-level
    GPOs from flowing down, but Enforced GPOs bypass this restriction and
    always apply.
  - Why C is incorrect: Block Inheritance does not remove a GPO from the
    domain — it only prevents GPOs from higher in the hierarchy from applying
    to that OU and its children. The GPO continues to exist and applies
    normally to other OUs that have not blocked inheritance.
  - Why D is incorrect: GPO processing does not distinguish between new and
    existing users in the OU. Group Policy applies based on the current OU
    membership and security filtering at policy refresh time.

---

### Question 8

An administrator deletes 30 user accounts accidentally. The AD Recycle Bin
is enabled and the deletion occurred 2 hours ago. Which PowerShell command
recovers all deleted user objects in a single operation?

A) `Get-ADUser -Filter {Enabled -eq $false} | Enable-ADAccount`

B) `Get-ADObject -Filter {isDeleted -eq $true -and ObjectClass -eq "user"} -IncludeDeletedObjects | Restore-ADObject`

C) `Restore-ADObject -Identity "CN=Deleted Objects,DC=contoso,DC=com"`

D) `ntdsutil "authoritative restore" "restore object CN=Users,DC=contoso,DC=com"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Disabled accounts are not deleted accounts. `Enable-ADAccount`
    re-enables an account that exists but is disabled. Deleted accounts are
    moved to the Deleted Objects container and are not returned by `Get-ADUser`
    without `-IncludeDeletedObjects`.
  - Why C is incorrect: `Restore-ADObject` with the container DN would attempt
    to restore the Deleted Objects container itself, not its contents. Individual
    deleted objects must be piped from `Get-ADObject -IncludeDeletedObjects`.
  - Why D is incorrect: `ntdsutil` authoritative restore is the recovery method
    when the Recycle Bin is not enabled or the tombstone period has expired. It
    requires DSRM and restoring from a system state backup. When Recycle Bin is
    enabled, `Restore-ADObject` is the correct and faster path.

---

### Question 9

A company deploys Pass-Through Authentication via Azure AD Connect. During
an unplanned on-premises domain controller outage lasting 4 hours, users
are unable to sign in to Microsoft 365. What configuration change would have
allowed cloud authentication to succeed during the outage?

A) Deploy a second Azure AD Connect server in Active mode for redundancy

B) Switch from Pass-Through Authentication to Password Hash Synchronization,
   which stores a hash of each user's password in Azure AD for cloud-only
   authentication

C) Enable Azure AD Seamless SSO, which caches credentials in Azure AD for
   offline use

D) Configure Hybrid Azure AD Join, which stores Microsoft 365 tokens on
   domain-joined devices

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Azure AD Connect supports only one Active server at a
    time. A second Active server would cause conflicts. More importantly, PTA
    always contacts on-premises DCs to validate passwords, so a second Azure
    AD Connect server does not resolve on-premises DC outages.
  - Why C is incorrect: Seamless SSO provides Kerberos-based SSO for
    domain-joined machines on the corporate network. It does not store passwords
    in Azure AD and does not enable cloud-only authentication during on-premises
    outages.
  - Why D is incorrect: Hybrid Azure AD Join enables devices to obtain Azure
    AD tokens. However, Microsoft 365 user authentication still depends on the
    PTA authentication method, which requires on-premises DC availability.

---

### Question 10

Which DSC ConfigurationMode setting applies the configuration once and then
monitors for drift but does not automatically correct it?

A) `ApplyOnly`

B) `ApplyAndMonitor`

C) `ApplyAndAutoCorrect`

D) `MonitorOnly`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `ApplyOnly` applies the configuration exactly once and
    performs no monitoring afterward. Drift is neither detected nor logged.
  - Why C is incorrect: `ApplyAndAutoCorrect` both monitors for drift and
    automatically corrects it. The question specifies monitoring without
    automatic correction.
  - Why D is incorrect: `MonitorOnly` is not a valid DSC ConfigurationMode
    value. The three valid modes are `ApplyOnly`, `ApplyAndMonitor`, and
    `ApplyAndAutoCorrect`.

---

### Question 11

An administrator needs to ensure that only domain-joined computers can
dynamically register DNS records in the corporate DNS zone. Which combination
of DNS settings achieves this?

A) Configure the zone as a primary zone with Nonsecure and Secure dynamic
   updates

B) Configure the zone as an AD-integrated zone with Secure Only dynamic updates

C) Configure the zone as a secondary zone — secondary zones prevent
   unauthorized registrations

D) Disable dynamic updates entirely and use static DNS records only

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Nonsecure and Secure dynamic updates allow any client,
    including non-domain-joined machines, to register DNS records. This
    defeats the requirement for authenticated registration.
  - Why C is incorrect: Secondary zones are read-only copies that receive zone
    transfers from a primary zone. They do not accept dynamic registrations
    at all — clients cannot register in a secondary zone.
  - Why D is incorrect: Disabling dynamic updates prevents all automated
    registration. Workstations and servers would fail to register their
    A records, causing DNS resolution failures across the environment.

---

### Question 12

An administrator uses JEA to restrict help desk operators to a limited set
of service management commands. Which two files must be created to define
a JEA endpoint?

A) A Role Capability File (`.psrc`) and a Session Configuration File (`.pssc`)

B) A Module Manifest (`.psd1`) and a Script Module (`.psm1`)

C) A Constrained Language Mode file and a firewall rule for WinRM

D) A Session Configuration File (`.pssc`) and a Group Policy Object

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Module manifests and script modules define PowerShell
    modules with exportable functions. They are not JEA-specific files and do
    not by themselves create constrained administrative endpoints.
  - Why C is incorrect: Constrained Language Mode is configured inside the
    `.pssc` file — it is not a separate file. A WinRM firewall rule is a
    network prerequisite but is not part of the JEA configuration itself.
  - Why D is incorrect: Group Policy Objects are used for domain-wide
    configuration settings, not for defining JEA endpoints. JEA endpoints
    are registered on individual servers using `Register-PSSessionConfiguration`.

---

### Question 13

An administrator runs the following command on a domain controller.

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = 4740
    StartTime = (Get-Date).AddHours(-6)
}
```

What events does this return?

A) All security audit events from the past 6 hours

B) Account lockout events (Event ID 4740) from the past 6 hours

C) Failed logon events (Event ID 4625) from the past 6 hours

D) Successful logon events (Event ID 4624) from the past 6 hours

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The `Id = 4740` filter restricts results to Event ID
    4740 only. All security events would require removing the `Id` filter.
  - Why C is incorrect: Event ID 4625 is a failed logon event. The command
    specifies `Id = 4740`, which is the account lockout event.
  - Why D is incorrect: Event ID 4624 is a successful logon event. The command
    specifies `Id = 4740`, not `4624`.

---

### Question 14

An iSCSI initiator needs to authenticate to a target server before accessing
storage LUNs. Which iSCSI feature provides this mutual authentication?

A) MPIO (Multipath I/O)

B) IQN (iSCSI Qualified Name)

C) CHAP (Challenge Handshake Authentication Protocol)

D) iSNS (Internet Storage Name Service)

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: MPIO provides multiple paths between the initiator and
    target for redundancy and load balancing. It does not authenticate the
    initiator to the target.
  - Why B is incorrect: An IQN is a unique identifier for iSCSI targets and
    initiators. While IQN-based access control lists can restrict which
    initiators connect, CHAP is the authentication mechanism that verifies
    credentials.
  - Why D is incorrect: iSNS is a discovery service that allows iSCSI devices
    to find each other, similar to DNS for iSCSI. It facilitates discovery
    but does not perform authentication.

---

### Question 15

Which Windows Server security technology uses Virtualization-Based Security to
isolate LSASS in a separate process, preventing attackers with SYSTEM-level
access from extracting credential hashes?

A) Local Administrator Password Solution (LAPS)

B) Windows Defender Credential Guard

C) Just Enough Administration (JEA)

D) BitLocker with Network Unlock

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: LAPS rotates the local administrator password on
    domain-joined computers. It protects against lateral movement via shared
    local admin passwords but does not use VBS or protect LSASS from credential
    extraction.
  - Why C is incorrect: JEA constrains PowerShell remoting sessions to a
    defined set of commands. It is a delegation and least-privilege tool, not
    a credential isolation technology.
  - Why D is incorrect: BitLocker with Network Unlock protects data at rest on
    server volumes. It does not protect the running LSASS process from
    credential extraction by an attacker who is already on the system.

---

### Question 16

An administrator needs to filter `Get-WinEvent` output for Security log events
in the most efficient way. Which approach minimizes the number of events
retrieved into memory?

A) `Get-WinEvent -LogName Security | Where-Object { $_.Id -eq 4625 }`

B) `Get-EventLog -LogName Security -Newest 10000 | Where-Object { $_.InstanceId -eq 4625 }`

C) `Get-WinEvent -FilterHashtable @{ LogName = "Security"; Id = 4625; StartTime = (Get-Date).AddDays(-1) }`

D) `Get-WinEvent -LogName Security | Select-Object -First 1000 | Where-Object { $_.Id -eq 4625 }`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: This retrieves all Security log events into memory and
    then filters in PowerShell. The Security log on an active domain controller
    can contain millions of events.
  - Why B is incorrect: Retrieving 10,000 events into memory and then filtering
    is inefficient. `-FilterHashtable` filters at the event log subsystem level
    before objects reach PowerShell.
  - Why D is incorrect: Taking the first 1,000 events and filtering may miss
    the desired events if they occurred before the 1,000-event window. This
    approach is both inefficient and incomplete.

---

### Question 17

An administrator must ensure that a DSC-managed server's Spooler service
remains stopped and disabled, and that any manual restart of the service is
automatically reversed within 15 minutes. Which LCM configuration achieves this
without administrator intervention?

A) `ConfigurationMode = "ApplyOnly"` with a scheduled task to re-apply the
   configuration every 15 minutes

B) `ConfigurationMode = "ApplyAndMonitor"` — the LCM logs the drift to
   the event log and notifies an administrator

C) `ConfigurationMode = "ApplyAndAutoCorrect"` with
   `ConfigurationModeFrequencyMins = 15` — the LCM checks and corrects
   compliance every 15 minutes

D) `RefreshMode = "Pull"` — Pull mode automatically re-applies configurations
   on a schedule

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `ApplyOnly` makes no change to a drifted server after
    the initial application. A scheduled task could work, but it is a manual
    workaround that requires separate maintenance. `ApplyAndAutoCorrect` is the
    purpose-built DSC mechanism.
  - Why B is incorrect: `ApplyAndMonitor` detects drift and logs it, but it
    does not automatically correct it. An administrator must manually re-apply
    the configuration.
  - Why D is incorrect: `RefreshMode = "Pull"` controls how the LCM retrieves
    new configurations from a Pull Server. It does not by itself correct
    configuration drift — the `ConfigurationMode` setting controls drift
    correction.

---

### Question 18

An administrator uses Storage Replica to replicate a data volume from Server A
to Server B. They configure synchronous replication. What does synchronous
replication guarantee?

A) Data is written to Server B's replica within 5 minutes of the write to
   Server A

B) Data is written to both Server A and Server B before the write is
   acknowledged to the application — guaranteeing zero data loss

C) Server B takes over automatically if Server A fails, with no administrator
   action required

D) Data is compressed during replication to reduce WAN bandwidth

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A 5-minute window describes asynchronous replication
    with a lag, not synchronous replication. Synchronous replication requires
    both writes to complete before acknowledging the application.
  - Why C is incorrect: Storage Replica does not perform automatic failover.
    Failover requires manual administrator action or an additional cluster
    configuration. Storage Replica handles replication, not high-availability
    failover.
  - Why D is incorrect: Storage Replica does not provide built-in compression.
    Compression is a network-layer capability managed separately from the
    replication protocol.

---

### Question 19

A Windows Server administrator wants to query all stopped services that have
a startup type of Automatic, sorted alphabetically by service name. Which
PowerShell command is most efficient and correct?

A) `Get-Service -Status Stopped | Sort-Object Name`

B) `Get-Service | Where-Object { $_.StartType -eq "Automatic" -and $_.Status -eq "Stopped" } | Sort-Object Name`

C) `Get-Service -Filter "StartType=Automatic AND Status=Stopped" | Sort-Object Name`

D) `Get-Service | Sort-Object Name | Filter { $_.StartType -eq "Automatic" }`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-Service -Status Stopped` filters by status only
    — it returns all stopped services regardless of startup type. This would
    include Manually started services that are currently stopped.
  - Why C is incorrect: `Get-Service` does not support a `-Filter` parameter.
    The `-Filter` parameter is available on Active Directory cmdlets and some
    file system operations, not on `Get-Service`.
  - Why D is incorrect: `Filter` is not a valid pipeline cmdlet in PowerShell.
    The correct filtering cmdlet is `Where-Object`.

---

### Question 20

An administrator needs to connect remote clients using VPN through a firewall
that blocks all ports except 443, and the clients are running Windows 11
Home edition (non-domain-joined). Which VPN technology is the correct choice?

A) DirectAccess, which uses IPv6 over HTTPS and works with all Windows
   editions

B) L2TP/IPsec VPN on RRAS, which uses port 443 when NAT-T is enabled

C) Always On VPN with SSTP, which tunnels over HTTPS on port 443 and
   supports non-domain and non-Enterprise clients

D) PPTP VPN, which uses port 443 for encapsulation

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: DirectAccess requires Windows Enterprise edition and
    domain membership. Windows 11 Home edition cannot use DirectAccess.
    Additionally, DirectAccess requires IPv6, which may not be available in
    all environments.
  - Why B is incorrect: L2TP/IPsec uses UDP ports 500 and 4500 (or 1701 without
    NAT-T). NAT-T encapsulates ESP inside UDP 4500, not TCP 443. L2TP/IPsec
    would be blocked by a port-443-only firewall.
  - Why D is incorrect: PPTP uses TCP port 1723 and GRE protocol 47. It does
    not use port 443 and would be blocked by the firewall. PPTP is also
    considered cryptographically weak and is not recommended for new deployments.

---

End of Quiz — Module 16
