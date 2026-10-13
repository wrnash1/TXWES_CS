# Lab Activity: Module 16 — Capstone Lab

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

This capstone lab integrates skills from the entire course. You will work
through scenarios covering Active Directory administration, Group Policy,
PowerShell remoting, Hyper-V virtual machine management, DSC compliance
verification, and security auditing. Each part simulates a real-world
administrative task you might encounter on the certification exam or in a
production environment.

---

## Lab Environment Requirements

- Windows Server 2022 domain controller (DC1) in the txwes.edu domain
- Windows Server 2022 member server (SERVER1) joined to txwes.edu
- Administrator credentials
- Hyper-V enabled on DC1 or SERVER1
- PowerShell 5.1 or later with Administrator privileges

---

## Part 1: Active Directory Administration

### Step 1.1 — Verify FSMO Role Holders

```powershell
# Display all five FSMO role holders
Get-ADDomain | Select-Object PDCEmulator, RIDMaster, InfrastructureMaster
Get-ADForest | Select-Object SchemaMaster, DomainNamingMaster
```

Record the server names holding each role in your lab report.

### Step 1.2 — Create Organizational Units and Users

```powershell
# Create OU structure
New-ADOrganizationalUnit -Name "CapstoneServers" `
    -Path "DC=txwes,DC=edu"

New-ADOrganizationalUnit -Name "CapstoneUsers" `
    -Path "DC=txwes,DC=edu"

# Create a test user account
New-ADUser -Name "CapstoneUser01" `
    -GivenName "Capstone" `
    -Surname "User01" `
    -SamAccountName "capstoneuser01" `
    -UserPrincipalName "capstoneuser01@txwes.edu" `
    -Path "OU=CapstoneUsers,DC=txwes,DC=edu" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force) `
    -Enabled $true

# Verify the user was created
Get-ADUser -Identity "capstoneuser01" | Select-Object Name, DistinguishedName, Enabled
```

### Step 1.3 — Simulate and Recover a Deleted Object

```powershell
# Verify AD Recycle Bin is enabled
Get-ADOptionalFeature -Filter {Name -like "Recycle Bin Feature"} |
    Select-Object Name, EnabledScopes

# Delete the test user
Remove-ADUser -Identity "capstoneuser01" -Confirm:$false

# Verify deletion
Get-ADUser -Identity "capstoneuser01" -ErrorAction SilentlyContinue

# Restore from Recycle Bin
Get-ADObject -Filter {isDeleted -eq $true -and SamAccountName -eq "capstoneuser01"} `
    -IncludeDeletedObjects | Restore-ADObject

# Verify restoration
Get-ADUser -Identity "capstoneuser01" | Select-Object Name, Enabled
```

Take Screenshot 1 — `Get-ADUser` output showing the restored user account.

---

## Part 2: Group Policy

### Step 2.1 — Create a GPO with a Password Policy

```powershell
# Create the GPO
New-GPO -Name "CapstonePasswordPolicy" -Domain "txwes.edu"

# Link the GPO to the CapstoneUsers OU
New-GPLink -Name "CapstonePasswordPolicy" `
    -Target "OU=CapstoneUsers,DC=txwes,DC=edu"

# Set minimum password length to 14 via registry-based GPO setting
# (Fine-grained password policies via PSO are an alternative; GPO is shown here)
Set-GPRegistryValue -Name "CapstonePasswordPolicy" `
    -Key "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" `
    -ValueName "PasswordExpiryWarning" `
    -Type DWord `
    -Value 14
```

### Step 2.2 — Generate a GPO Compliance Report

```powershell
# Run gpresult to see applied GPOs for the current user and computer
gpresult /r

# Generate an HTML report (opens in browser)
gpresult /h "C:\CapstoneReports\GPOReport.html" /f
Start-Process "C:\CapstoneReports\GPOReport.html"
```

Take Screenshot 2 — HTML GPO report showing applied GPOs.

---

## Part 3: PowerShell Remoting and Health Check

### Step 3.1 — Fan-Out Health Check

```powershell
# Save as C:\CapstoneReports\CapstoneHealthCheck.ps1

$servers = @("DC1", "SERVER1", "localhost")

$results = Invoke-Command -ComputerName $servers -ScriptBlock {
    [PSCustomObject]@{
        Computer        = $env:COMPUTERNAME
        OS              = (Get-CimInstance Win32_OperatingSystem).Caption
        Uptime          = [math]::Round(
                            (Get-Date - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
                            ).TotalHours, 1)
        RunningServices = (Get-Service | Where-Object { $_.Status -eq "Running" }).Count
        StoppedAuto     = (Get-Service | Where-Object {
                            $_.StartType -eq "Automatic" -and $_.Status -eq "Stopped"
                          }).Count
        DiskCFreeGB     = [math]::Round(
                            (Get-PSDrive C).Free / 1GB, 1)
    }
} -ErrorAction SilentlyContinue

$results | Select-Object Computer, OS, Uptime, RunningServices, StoppedAuto, DiskCFreeGB |
    Format-Table -AutoSize
```

### Step 3.2 — Export the Results

```powershell
New-Item -Path "C:\CapstoneReports" -ItemType Directory -Force | Out-Null

$results | Export-Csv -Path "C:\CapstoneReports\HealthCheck.csv" -NoTypeInformation

Import-Csv "C:\CapstoneReports\HealthCheck.csv" | Format-Table -AutoSize
```

Take Screenshot 3 — Health check results from all three targets.

---

## Part 4: Hyper-V Virtual Machine Management

### Step 4.1 — Create a Test Virtual Machine

```powershell
# Create an internal virtual switch if it does not exist
if (-not (Get-VMSwitch -Name "CapstoneInternal" -ErrorAction SilentlyContinue)) {
    New-VMSwitch -Name "CapstoneInternal" -SwitchType Internal
}

# Create a Generation 2 test VM
New-VM -Name "CapstoneTestVM" `
    -Generation 2 `
    -MemoryStartupBytes 1GB `
    -SwitchName "CapstoneInternal" `
    -Path "C:\VMs"

# Enable Dynamic Memory
Set-VMMemory -VMName "CapstoneTestVM" `
    -DynamicMemoryEnabled $true `
    -MinimumBytes 512MB `
    -MaximumBytes 2GB

# Verify the VM configuration
Get-VM -Name "CapstoneTestVM" | Select-Object Name, State, Generation
Get-VMMemory -VMName "CapstoneTestVM" | Select-Object DynamicMemoryEnabled, Minimum, Maximum
```

### Step 4.2 — Create and Restore a Checkpoint

```powershell
# Create a production checkpoint
Checkpoint-VM -Name "CapstoneTestVM" `
    -SnapshotName "CapstoneBaseline" `
    -CheckpointType Production

# Verify the checkpoint exists
Get-VMCheckpoint -VMName "CapstoneTestVM" | Select-Object Name, CreationTime, CheckpointType

# Restore to the checkpoint
Restore-VMCheckpoint -VMName "CapstoneTestVM" `
    -SnapshotName "CapstoneBaseline" `
    -Confirm:$false

# Remove the checkpoint
Remove-VMCheckpoint -VMName "CapstoneTestVM" -SnapshotName "CapstoneBaseline"
```

Take Screenshot 4 — `Get-VM` and `Get-VMMemory` output showing the test VM.

---

## Part 5: DSC Compliance Verification

### Step 5.1 — Write and Apply a DSC Configuration

```powershell
# Save as C:\CapstoneReports\DSC\CapstoneConfig.ps1

Configuration CapstoneBaseline {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node "localhost" {
        # Ensure Windows Time service is running
        Service W32Time {
            Name        = "W32Time"
            State       = "Running"
            StartupType = "Automatic"
        }

        # Ensure Print Spooler is stopped (security baseline)
        Service Spooler {
            Name        = "Spooler"
            State       = "Stopped"
            StartupType = "Disabled"
        }

        # Ensure the reports directory exists
        File CapstoneDir {
            DestinationPath = "C:\CapstoneReports\Configured"
            Type            = "Directory"
            Ensure          = "Present"
        }
    }
}
```

```powershell
# Compile and apply the configuration
. "C:\CapstoneReports\DSC\CapstoneConfig.ps1"
CapstoneBaseline -OutputPath "C:\CapstoneReports\DSC\MOF"

Start-DscConfiguration `
    -Path "C:\CapstoneReports\DSC\MOF" `
    -Wait `
    -Verbose `
    -Force
```

### Step 5.2 — Test Compliance

```powershell
$result = Test-DscConfiguration -Verbose
Write-Host "In Desired State: $result"
```

Take Screenshot 5 — `Test-DscConfiguration` output showing `True`.

### Step 5.3 — Simulate Drift

```powershell
# Simulate drift by starting Spooler
Set-Service -Name "Spooler" -StartupType Manual
Start-Service -Name "Spooler"

# Verify drift detected
$result = Test-DscConfiguration
Write-Host "In Desired State after drift: $result"

# Re-apply to correct drift
Start-DscConfiguration -Path "C:\CapstoneReports\DSC\MOF" -Wait -Force -Verbose

# Verify corrected
Get-Service -Name "Spooler" | Select-Object Name, Status, StartType
```

Take Screenshot 6 — Service status before and after re-applying DSC configuration.

---

## Part 6: Security Auditing

### Step 6.1 — Enable Logon Auditing

```powershell
# Enable auditing of successful and failed logon events
auditpol /set /subcategory:"Logon" /success:enable /failure:enable

# Verify the policy
auditpol /get /subcategory:"Logon"
```

### Step 6.2 — Query Security Events

```powershell
# Query for failed logon events in the past 24 hours
Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = 4625
    StartTime = (Get-Date).AddDays(-1)
} | Select-Object TimeCreated, Id, Message -First 10 |
    Format-List
```

### Step 6.3 — Export the Security Event Report

```powershell
$secEvents = Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = @(4624, 4625, 4720, 4740)
    StartTime = (Get-Date).AddDays(-1)
} | Select-Object TimeCreated, Id,
    @{n="EventType"; e={
        switch ($_.Id) {
            4624 { "Logon Success" }
            4625 { "Logon Failure" }
            4720 { "Account Created" }
            4740 { "Account Locked" }
        }
    }},
    Message

$secEvents | Export-Csv -Path "C:\CapstoneReports\SecurityEvents.csv" -NoTypeInformation
Write-Host "Exported $($secEvents.Count) security events."

$secEvents | Group-Object EventType | Select-Object Name, Count | Format-Table -AutoSize
```

Take Screenshot 7 — Security event summary grouped by event type.

---

## Lab Deliverables

Submit the following screenshots and answers to Canvas.

**Screenshot 1** — Restored AD user account from Recycle Bin.

**Screenshot 2** — HTML GPO report showing applied policies.

**Screenshot 3** — Invoke-Command health check results from three targets.

**Screenshot 4** — Hyper-V VM configuration showing Generation 2 and Dynamic Memory.

**Screenshot 5** — `Test-DscConfiguration` returning `True`.

**Screenshot 6** — Spooler service status showing drift and correction by DSC.

**Screenshot 7** — Security event summary grouped by event type.

**Written Answers:**

1. Which server holds the PDC Emulator FSMO role in your lab environment?
   Why is the PDC Emulator the most frequently contacted FSMO role in a
   production domain?

2. After applying the DSC configuration, `Test-DscConfiguration` returns `True`.
   After simulating drift by starting Spooler, it returns `False`. Explain what
   the LCM would do automatically if `ConfigurationMode` were set to
   `"ApplyAndAutoCorrect"` instead of requiring manual re-application.

3. You ran `Invoke-Command` against three targets simultaneously. Compare this
   to running the same commands in a `foreach` loop with `Enter-PSSession`.
   What is the operational advantage of `Invoke-Command` for fleet
   administration?

---

## Lab Rubric — 100 Points

| Item | Points | Criteria |
|---|---|---|
| AD recovery | 15 | Screenshot 1 shows user restored from Recycle Bin |
| GPO report | 10 | Screenshot 2 shows HTML report with applied GPOs |
| PowerShell remoting | 15 | Screenshot 3 shows results from three targets |
| Hyper-V management | 15 | Screenshot 4 shows correct VM configuration |
| DSC compliance | 20 | Screenshots 5 and 6 show compliance test and drift correction |
| Security auditing | 15 | Screenshot 7 shows grouped security event summary |
| Written answers | 10 | Answers demonstrate conceptual understanding |

---

## Cleanup

```powershell
# Remove the test VM
Remove-VM -Name "CapstoneTestVM" -Force

# Remove the test virtual switch
Remove-VMSwitch -Name "CapstoneInternal" -Force

# Remove test OUs and users (remove OU contents first)
Remove-ADUser -Identity "capstoneuser01" -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=CapstoneUsers,DC=txwes,DC=edu" `
    -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=CapstoneServers,DC=txwes,DC=edu" `
    -Recursive -Confirm:$false

# Remove the GPO
Remove-GPO -Name "CapstonePasswordPolicy" -Domain "txwes.edu"
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Build a Comprehensive Environment Health Dashboard

Integrate skills from all major course modules into a single script that audits
AD, DNS, DHCP, file services, and security event data in one execution.

1. Create the multi-domain health collection function. This script queries data
   from modules 02 (AD), 06 (DNS/DHCP), 10 (file services), and 14 (security events):

   ```powershell
   function Get-EnvironmentHealthReport {
       param([string]$DomainController = "DC1")

       $report = [ordered]@{}

       # --- Active Directory Health (Module 02/03) ---
       try {
           $fsmo = netdom query fsmo 2>&1
           $report.PDCEmulator     = ($fsmo | Where-Object {$_ -match "PDC"}) -replace ".*:\s*",""
           $report.SchemaOwner     = ($fsmo | Where-Object {$_ -match "Schema"}) -replace ".*:\s*",""
           $report.RIDOwner        = ($fsmo | Where-Object {$_ -match "RID"}) -replace ".*:\s*",""
       } catch {
           $report.FSMOError = $_.Exception.Message
       }

       # --- User Account Summary (Module 07) ---
       try {
           $report.TotalUsers          = (Get-ADUser -Filter *).Count
           $report.DisabledUsers       = (Search-ADAccount -AccountDisabled).Count
           $report.LockedUsers         = (Search-ADAccount -LockedOut).Count
       } catch {
           $report.ADUserError = $_.Exception.Message
       }

       # --- DNS Health (Module 09) ---
       try {
           $zones = Get-DnsServerZone -ComputerName $DomainController -ErrorAction Stop
           $report.TotalDNSZones       = $zones.Count
           $report.ADIntegratedZones   = ($zones | Where-Object {$_.ZoneType -eq "Primary" -and $_.IsDsIntegrated}).Count
       } catch {
           $report.DNSError = $_.Exception.Message
       }

       # --- DHCP Health (Module 09) ---
       try {
           $scopes = Get-DhcpServerv4Scope -ComputerName $DomainController -ErrorAction Stop
           $report.DHCPScopes          = $scopes.Count
           $stats  = Get-DhcpServerv4ScopeStatistics -ScopeId $scopes[0].ScopeId `
                         -ComputerName $DomainController -ErrorAction Stop
           $report.DHCPFirstScopeUsed  = "$($stats.PercentageInUse)%"
       } catch {
           $report.DHCPError = $_.Exception.Message
       }

       # --- Security Events (Module 14) ---
       try {
           $report.FailedLogons24h = (Get-WinEvent -ComputerName $DomainController -ErrorAction Stop `
               -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddDays(-1)}).Count
           $report.Lockouts24h     = (Get-WinEvent -ComputerName $DomainController -ErrorAction Stop `
               -FilterHashtable @{LogName='Security'; Id=4740; StartTime=(Get-Date).AddDays(-1)}).Count
       } catch {
           $report.SecurityError = $_.Exception.Message
       }

       $report.ReportTime = (Get-Date).ToString("yyyy-MM-dd HH:mm")
       [PSCustomObject]$report
   }
   ```

2. Run the health report and display results:

   ```powershell
   $health = Get-EnvironmentHealthReport -DomainController "DC1"
   $health | Format-List *
   ```

3. Export to CSV and generate a risk summary:

   ```powershell
   $health | Export-Csv "C:\CapstoneReports\EnvHealth_$(Get-Date -Format yyyyMMdd).csv" `
       -NoTypeInformation

   # Risk flags
   if ($health.LockedUsers -gt 5) {
       Write-Warning "HIGH: $($health.LockedUsers) locked accounts — possible brute force"
   }
   if ($health.FailedLogons24h -gt 100) {
       Write-Warning "HIGH: $($health.FailedLogons24h) failed logons in 24h — investigate"
   }
   if ([double]($health.DHCPFirstScopeUsed -replace '%','') -gt 90) {
       Write-Warning "HIGH: DHCP scope utilization at $($health.DHCPFirstScopeUsed)"
   }
   ```

4. Save a baseline and compare against a future run:

   ```powershell
   $baseline = $health
   # [Simulate time passing — re-run the health report]
   $current  = Get-EnvironmentHealthReport -DomainController "DC1"

   Write-Host "Baseline failed logons: $($baseline.FailedLogons24h)"
   Write-Host "Current failed logons:  $($current.FailedLogons24h)"
   $delta = [int]$current.FailedLogons24h - [int]$baseline.FailedLogons24h
   if ($delta -gt 50) {
       Write-Warning "Failed logon SPIKE: +$delta since last baseline"
   }
   ```

   In your lab notes, identify which module skills are represented by each section
   of this script, and describe how you would schedule this report to run hourly
   and email the security team when any risk flag triggers.

### Challenge 2: Design a Disaster Recovery Runbook Scenario

Apply knowledge from all modules to document and test a recovery procedure
for a simulated failure scenario.

1. Simulate an accidental GPO deletion and verify the impact:

   ```powershell
   # Create a test GPO to delete
   New-GPO -Name "DR_Test_Policy" -Domain "txwes.edu"
   New-GPLink -Name "DR_Test_Policy" -Target "DC=txwes,DC=edu" -LinkEnabled No

   # Record the GPO GUID before deletion
   $gpo = Get-GPO -Name "DR_Test_Policy"
   Write-Host "GPO GUID: $($gpo.Id)"

   # Delete the GPO (simulating an accident)
   Remove-GPO -Name "DR_Test_Policy" -Domain "txwes.edu" -Confirm:$false

   # Verify it is gone
   Get-GPO -Name "DR_Test_Policy" -ErrorAction SilentlyContinue
   ```

2. Restore the GPO from a backup (requires a prior backup to exist — create one
   first in a real scenario):

   ```powershell
   # Backup all GPOs first (should be done regularly)
   Backup-GPO -All -Path "C:\GPOBackups" -Domain "txwes.edu"

   # List available backups
   Get-ChildItem "C:\GPOBackups" | Select-Object Name, CreationTime

   # Restore the deleted GPO by name from the most recent backup
   Restore-GPO -Name "DR_Test_Policy" -Path "C:\GPOBackups" -Domain "txwes.edu"

   # Verify restoration
   Get-GPO -Name "DR_Test_Policy" | Select-Object DisplayName, GpoStatus, CreationTime
   ```

3. Simulate an AD user account recovery from the Recycle Bin:

   ```powershell
   # Create a test user to delete
   New-ADUser -Name "DR Test User" -SamAccountName "drtest" -Enabled $false

   # Delete the user
   Remove-ADUser -Identity "drtest" -Confirm:$false

   # Recover from Recycle Bin
   Get-ADObject -Filter {SamAccountName -eq "drtest"} -IncludeDeletedObjects |
       Restore-ADObject

   # Verify recovery
   Get-ADUser -Identity "drtest" | Select-Object Name, SamAccountName, DistinguishedName

   # Cleanup
   Remove-ADUser -Identity "drtest" -Confirm:$false
   ```

4. Document the recovery procedures as a runbook entry:

   ```powershell
   $runbook = @"
   TXWES Domain Recovery Runbook — Entry 001
   ==========================================
   Scenario:   Accidental GPO deletion
   Detection:  User reports policy no longer applying; Get-GPO returns empty
   RTO Target: 30 minutes
   Steps:
     1. Identify missing GPO name from ticket or audit log
     2. Run: Backup-GPO -All -Path C:\GPOBackups (if not done today)
     3. Run: Restore-GPO -Name "<GPOName>" -Path C:\GPOBackups
     4. Verify: Get-GPO -Name "<GPOName>" shows active status
     5. Force policy refresh on affected systems: Invoke-GPUpdate -Computer <targets>
   Prevention: Backup-GPO scheduled daily; GPO creation requires change ticket
   "@

   $runbook | Out-File "C:\CapstoneReports\Runbook_GPO_Recovery.txt"
   Get-Content "C:\CapstoneReports\Runbook_GPO_Recovery.txt"
   ```

   In your lab notes, add a second runbook entry for AD user recovery, following
   the same format. Include the detection method, RTO target, step-by-step recovery
   commands, and prevention controls.

### Reflection Questions

1. You have completed a Windows Server Administration course covering installation,
   Active Directory, DNS, DHCP, GPO, file services, security, PowerShell,
   storage, monitoring, and hybrid identity. A hiring manager asks you to describe
   the single most important operational practice that applies across all of these
   areas. Drawing on at least three specific module topics, construct a cohesive
   answer that demonstrates how the practice you choose connects the skills from
   this course into a unified professional competency.

2. A critical production domain controller fails completely and cannot be restarted.
   The organization has no hot standby DC, no recent AD backup, but they do have
   a second domain controller (DC2) that is a replica of DC1. Describe the complete
   recovery sequence — including which FSMO roles need to be seized (vs. transferred),
   how DNS service would be restored, which event log entries on DC2 would confirm
   successful AD replication before the failure, and what monitoring you would
   implement going forward to detect DC failure within 5 minutes rather than
   discovering it through user complaints.
