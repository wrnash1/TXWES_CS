# Lab Activity: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will add a second Domain Controller to the `corp.local` domain created in Module 02, verify replication between both DCs, and check domain health with diagnostic tools. A two-DC domain is the minimum recommended configuration for any production environment and is tested on the AZ-800 exam.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 02 lab complete: `SRV-CORE-01` is DC1 in `corp.local` with IP `192.168.10.10`
- A second VM ready: fresh Windows Server 2022 installation, named `SRV-CORE-02`, static IP `192.168.10.20/24`, DNS pointing to `192.168.10.10`

**Learning Objectives:**

- Install the AD DS role and promote a second DC using PowerShell
- Verify replication health between two DCs using repadmin
- Run dcdiag to confirm domain health
- Verify DNS SRV record registration
- Confirm SYSVOL and NETLOGON share availability

---

### Part 1 — Prepare the Second Server

#### Step 1.1 — Configure SRV-CORE-02

On the second VM, open PowerShell and verify the network configuration:

```powershell
# Verify hostname
hostname
# Expected: SRV-CORE-02

# Verify IP address
Get-NetIPAddress -InterfaceAlias "Ethernet" -AddressFamily IPv4
# Expected: 192.168.10.20

# Verify DNS points to DC1
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
# Expected: 192.168.10.10
```

If DNS is not pointing to DC1, set it now:

```powershell
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses "192.168.10.10"
```

#### Step 1.2 — Verify Connectivity to DC1

```powershell
# Test connectivity to DC1
Test-NetConnection -ComputerName 192.168.10.10 -Port 389

# Verify DC1 is reachable by name
nslookup SRV-CORE-01.corp.local
```

Both should succeed. If `Test-NetConnection` fails on port 389, check the Windows Firewall on SRV-CORE-01 — LDAP must be allowed.

---

### Part 2 — Install AD DS Role on SRV-CORE-02

#### Step 2.1 — Install the Role

```powershell
Install-WindowsFeature `
    -Name AD-Domain-Services `
    -IncludeManagementTools `
    -Verbose
```

Wait for installation to complete. Verify `Success : True` in the output.

```powershell
# Confirm installation
Get-WindowsFeature -Name AD-Domain-Services | Select-Object Name, InstallState
```

---

### Part 3 — Promote SRV-CORE-02 as Additional DC

#### Step 3.1 — Set Credentials and DSRM Password

```powershell
$credential = Get-Credential
# When prompted, enter: CORP\Administrator and the domain admin password

$dsrmPassword = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force
```

#### Step 3.2 — Run the Promotion

```powershell
Install-ADDSDomainController `
    -DomainName "corp.local" `
    -Credential $credential `
    -InstallDns `
    -SafeModeAdministratorPassword $dsrmPassword `
    -Force
```

**[SHOW SCREEN: Promotion progress output showing replication from DC1 and final reboot message]**

The promotion replicates the AD database from DC1. After the reboot, log in as `CORP\Administrator`.

---

### Part 4 — Verify Replication Health

Run all replication verification commands on DC2 (SRV-CORE-02) after login.

#### Step 4.1 — Check Both DCs Are Visible

```powershell
Get-ADDomainController -Filter * | Select-Object Name, IPv4Address, IsGlobalCatalog, Site
```

Expected: Two entries — SRV-CORE-01 and SRV-CORE-02, both with IsGlobalCatalog: True.

#### Step 4.2 — Run Replication Summary

```powershell
repadmin /replsummary
```

All failure counts should be zero. If any DC shows failures, proceed to Step 4.3.

#### Step 4.3 — Detailed Replication Status

```powershell
repadmin /showrepl
```

Each entry should say "Last attempt was successful." Note the time of last replication. In a healthy lab environment, initial replication completes within 5-10 minutes of promotion.

#### Step 4.4 — Force Replication

If replication has not yet completed, force it:

```powershell
repadmin /syncall /AdeP
```

Then re-run `repadmin /replsummary` to confirm zero failures.

---

### Part 5 — Run dcdiag Health Checks

#### Step 5.1 — Full Diagnostic Run

```powershell
dcdiag /v
```

This runs all tests. Review the output for any `failed test` entries. The following tests are most important:

- `Advertising` — must pass
- `Replications` — must pass
- `SysVolCheck` — must pass
- `DNS` — must pass

#### Step 5.2 — Targeted Replication Test

```powershell
dcdiag /test:Replications /v
```

#### Step 5.3 — DNS SRV Record Verification

```powershell
# From SRV-CORE-02, verify LDAP SRV records for both DCs
nslookup -type=SRV _ldap._tcp.corp.local

# Verify Kerberos SRV records
nslookup -type=SRV _kerberos._tcp.corp.local
```

Both DC1 and DC2 should appear as LDAP SRV record targets.

---

### Part 6 — Verify SYSVOL and NETLOGON Shares

```powershell
# List shares on DC2
Get-SmbShare | Select-Object Name, Path, Description

# Verify SYSVOL contents
Get-ChildItem -Path "C:\Windows\SYSVOL\sysvol\corp.local\"
```

You should see both `SYSVOL` and `NETLOGON` shares listed. The SYSVOL directory should contain a `Policies` folder (Group Policy templates) and a `scripts` folder.

---

### Part 7 — Verify Functional Levels

```powershell
# Check current functional levels on DC2
Get-ADDomain | Select-Object DomainMode, PDCEmulator, RIDMaster, InfrastructureMaster
Get-ADForest | Select-Object ForestMode, SchemaMaster, DomainNamingMaster
```

Confirm that functional levels show `Windows2016Domain` and `Windows2016Forest` (or the level you set during Module 02 promotion).

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — AD DS role installation on DC2:** Output of `Get-WindowsFeature AD-Domain-Services` showing `InstallState: Installed`.

**Screenshot 2 — Promotion completion:** PowerShell output showing `Install-ADDSDomainController` completing successfully.

**Screenshot 3 — Both DCs visible:** Output of `Get-ADDomainController -Filter *` showing SRV-CORE-01 and SRV-CORE-02.

**Screenshot 4 — Replication summary:** Output of `repadmin /replsummary` showing zero failures for both DCs.

**Screenshot 5 — dcdiag Replications test:** Output of `dcdiag /test:Replications /v` showing passed test on DC2.

**Screenshot 6 — SYSVOL and NETLOGON shares:** Output of `Get-SmbShare` showing both shares.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| AD DS role installed on DC2 | 10 | Feature install screenshot shows InstallState: Installed |
| DC2 promoted successfully | 20 | Both DCs visible in Get-ADDomainController |
| Replication working | 25 | repadmin /replsummary shows zero failures for both DCs |
| dcdiag Replications test passes on DC2 | 20 | dcdiag test screenshot shows passed |
| SYSVOL and NETLOGON shares present on DC2 | 15 | Get-SmbShare output |
| DNS SRV records for both DCs | 10 | nslookup SRV output shows both DC1 and DC2 |

---

### Troubleshooting Notes

If `Install-ADDSDomainController` fails with "The RPC server is unavailable," verify that Windows Firewall on DC1 allows inbound connections on TCP 135 and the AD DS firewall exception group.

```powershell
# Run on DC1 to verify AD DS firewall rules are enabled
Get-NetFirewallRule -DisplayGroup "Active Directory Domain Services" | Select-Object DisplayName, Enabled
```

If repadmin shows errors after promotion, check Event Viewer on both DCs under Windows Logs > Directory Service for replication error codes.

```powershell
Get-EventLog -LogName "Directory Service" -EntryType Error, Warning -Newest 20
```
