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
