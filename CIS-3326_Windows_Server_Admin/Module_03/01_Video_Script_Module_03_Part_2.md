# Video Script: Module 03 - Installing and Configuring AD DS (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 03 - Installing and Configuring AD DS

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 12 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 03. In Part 1 we covered the two-step install-then-promote process, the three promotion scenarios, functional levels, DNS integration, replication, and DSRM. In Part 2 I will walk you through the complete PowerShell workflow for installing and promoting a Domain Controller, adding a second DC, and verifying health with diagnostic tools.

---

### [SEGMENT 2 — Demo: Install the AD DS Role]

**[SHOW SCREEN: PowerShell console on Windows Server]**

[Alt-text: PowerShell console showing the Install-WindowsFeature command and feature installation progress output.]

```powershell
# Install the AD DS role with management tools
Install-WindowsFeature `
    -Name AD-Domain-Services `
    -IncludeManagementTools `
    -Verbose
```

This installs the AD-Domain-Services role and all dependent features including the AD PowerShell module (RSAT-AD-PowerShell) and the DNS Server role management tools. When complete you see `Success : True`. The server does not reboot automatically. We control when promotion and reboot happen.

---

### [SEGMENT 3 — Demo: Promote to New Forest Root DC]

**[SHOW SCREEN: PowerShell showing Install-ADDSForest command and output]**

[Alt-text: PowerShell console showing the Install-ADDSForest cmdlet with parameters and promotion progress output including NTDS directory creation, DNS zone creation, and reboot notification.]

```powershell
# Set DSRM password as a secure string
$dsrmPassword = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

# Promote to new forest root domain controller
Install-ADDSForest `
    -DomainName "corp.local" `
    -DomainNetBIOSName "CORP" `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPassword `
    -Force
```

Parameter notes: `-DomainName` is the FQDN. `-DomainNetBIOSName` is the legacy short name, 15 characters maximum. `-ForestMode` and `-DomainMode` set functional levels. `-InstallDns` creates an AD-integrated DNS zone automatically. `-Force` suppresses prompts.

After a few minutes the server reboots. When it returns, the logon prompt shows `CORP\Administrator`.

---

### [SEGMENT 4 — Demo: Add a Second DC to an Existing Domain]

**[SHOW SCREEN: PowerShell on a second server]**

[Alt-text: PowerShell console on a second server showing Install-WindowsFeature followed by Install-ADDSDomainController.]

On the second server, install the AD DS role first, then promote:

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

$credential = Get-Credential "CORP\Administrator"
$dsrmPassword = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

Install-ADDSDomainController `
    -DomainName "corp.local" `
    -Credential $credential `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPassword `
    -Force
```

The key difference is `-Credential` — domain admin credentials are required to join an existing domain. The new DC contacts the existing DC, authenticates, and replicates the AD database. After reboot, we have two DCs.

---

### [SEGMENT 5 — Demo: Verify Health with dcdiag]

**[SHOW SCREEN: PowerShell showing dcdiag output]**

[Alt-text: PowerShell console showing dcdiag output with multiple tests each ending in passed test.]

```powershell
# Run all DC diagnostic tests
dcdiag /v

# Run only replication tests
dcdiag /test:Replications /v

# Verify DNS SRV record registration
dcdiag /test:DNS /v
```

Key tests to check: `Advertising` confirms the DC is advertising in DNS. `Replications` confirms replication with all partners. `SysVolCheck` confirms SYSVOL is shared. `DNS` verifies SRV record registration. All should return `passed test`.

---

### [SEGMENT 6 — Demo: Verify Replication with repadmin]

**[SHOW SCREEN: PowerShell showing repadmin output]**

[Alt-text: PowerShell console showing repadmin /replsummary output with zero replication failures for both domain controllers.]

```powershell
# Show replication summary
repadmin /replsummary

# Show detailed replication status per partner
repadmin /showrepl

# Force immediate replication from all partners
repadmin /syncall /AdeP

# Show replication failures only
repadmin /showrepl * /errorsonly
```

In a healthy two-DC environment, `repadmin /replsummary` shows zero failures for both DCs. If failures appear, use `/showrepl * /errorsonly` to identify which partnerships are failing.

---

### [SEGMENT 7 — Demo: DNS SRV Record Verification]

**[SHOW SCREEN: PowerShell showing nslookup SRV record query]**

[Alt-text: PowerShell console showing nslookup querying for _ldap._tcp.corp.local SRV records and returning DC1.corp.local as the result.]

```powershell
# Verify Kerberos SRV record
nslookup -type=SRV _kerberos._tcp.corp.local

# Verify LDAP SRV record
nslookup -type=SRV _ldap._tcp.corp.local

# Verify Global Catalog SRV record
nslookup -type=SRV _gc._tcp.corp.local
```

Each query should return your DC's hostname and IP address. Missing SRV records mean clients cannot find the DC. If records are missing, restart the Netlogon service — it is responsible for registering SRV records:

```powershell
Restart-Service Netlogon
```

---

### [SEGMENT 8 — Demo: Functional Level Query and Raise]

**[SHOW SCREEN: PowerShell showing functional level commands]**

[Alt-text: PowerShell console showing Get-ADDomain output with DomainMode field and Set-ADDomainMode command.]

```powershell
# Check current functional levels
(Get-ADDomain).DomainMode
(Get-ADForest).ForestMode

# Verify all DCs meet the target OS version before raising
Get-ADDomainController -Filter * | Select-Object Name, OperatingSystem

# Raise domain functional level (one-way — cannot be undone)
Set-ADDomainMode -Identity "corp.local" -DomainMode Windows2016Domain

# Raise forest functional level
Set-ADForestMode -Identity "corp.local" -ForestMode Windows2016Forest
```

Always verify DC OS versions before raising. Once raised, the operation cannot be reversed.

---

### [SEGMENT 9 — Exam Tips]

**[SHOW SCREEN: Exam tips slide for Module 03]**

**Exam Tip 1:** Two separate steps — `Install-WindowsFeature` installs the role; `Install-ADDSForest` / `Install-ADDSDomainController` promotes the server. Role installation alone does not create a DC.

**Exam Tip 2:** `dcpromo.exe` was removed in Windows Server 2012. Any answer offering `dcpromo` for current Windows Server is incorrect.

**Exam Tip 3:** Functional level raising is irreversible. Verify all DC OS versions before raising. A lower-OS DC cannot join a domain whose DFL exceeds its OS version.

**Exam Tip 4:** The DSRM password is local to each DC. It is not the domain Administrator password. It is required for offline AD DS database maintenance and authoritative restore.

**Exam Tip 5:** Use `nslookup -type=SRV _ldap._tcp.corp.local` to verify DC discoverability. Missing SRV records are the first thing to check when clients cannot find the domain.

**Exam Tip 6:** `repadmin /replsummary` and `dcdiag /test:Replications` are the primary replication verification tools. Know both commands for the exam and for troubleshooting in the field.

---

### [SEGMENT 10 — Lab Preview]

**[SHOW SCREEN: Lab 03 instructions document]**

This week's lab builds on the Module 02 domain. You already have `SRV-CORE-01` as DC1 in `corp.local`. In this lab you will deploy a second VM, install AD DS, and promote it as an additional DC. Then you will run `dcdiag /test:Replications` on both DCs and `repadmin /replsummary` to verify replication.

Deliverables: screenshots of dcdiag Replications test passing on both DCs, repadmin replsummary showing zero failures, and `Get-ADDomainController -Filter *` showing both DCs.

---

### [SEGMENT 11 — Module 03 Summary]

**[SHOW SCREEN: Summary slide]**

AD DS deployment is a two-step process: install the role, then promote. Three promotion scenarios cover all cases: new forest, new domain in existing forest, and additional DC in existing domain. Functional levels are one-way operations. DNS SRV records are the mechanism clients use to find DCs. Replication keeps all DCs in sync. Use dcdiag and repadmin to verify everything is healthy.

Module 04 covers user, group, and computer account management in the domain we have now built. See you there.

---

### Additional Resources

- [Install Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-)
- [AD DS deployment with PowerShell](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-200-)
- [AD DS replication concepts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/replication/active-directory-replication-concepts)
- [repadmin tool reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc770963(v=ws.11))

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 03.*
