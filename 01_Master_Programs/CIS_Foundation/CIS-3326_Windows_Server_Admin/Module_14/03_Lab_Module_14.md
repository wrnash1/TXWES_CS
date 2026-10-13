# Lab Activity: Module 14 — Windows Server Security

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Time: 90 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

In this lab, you configure Windows Defender Antivirus, create and test Windows Firewall rules, build a basic JEA endpoint, configure LAPS, and review security audit events. These hands-on exercises cover the core security administration skills tested on Microsoft certification exams.

---

## Lab Environment Requirements

- Windows Server 2019 or 2022, domain-joined
- Administrator credentials
- Active Directory domain available (for LAPS schema extension)
- PowerShell 5.1 or later

---

## Part 1: Windows Defender Antivirus Management

### Step 1.1 — Check Defender Status

```powershell
# View overall Defender status
Get-MpComputerStatus | Select-Object `
    AMRunningMode,
    RealTimeProtectionEnabled,
    AntivirusEnabled,
    AntispywareEnabled,
    AntivirusSignatureAge,
    AntivirusSignatureLastUpdated
```

Record the signature age — if greater than 3 days, the definitions are outdated.

### Step 1.2 — Update Definitions

```powershell
Update-MpSignature -Verbose
```

After the update completes, re-check the signature age:

```powershell
(Get-MpComputerStatus).AntivirusSignatureAge
```

### Step 1.3 — Run a Quick Scan

```powershell
Start-MpScan -ScanType QuickScan
```

The scan runs in the background. Check results:

```powershell
Get-MpThreatDetection | Select-Object ThreatName, ActionSuccess, DetectionTime |
    Format-Table -AutoSize
```

If the system is clean, no output is returned.

### Step 1.4 — Add and Verify an Exclusion

```powershell
# Create a test directory and add it as an exclusion
New-Item -ItemType Directory -Path "C:\LabExclusion" -Force

Add-MpPreference -ExclusionPath "C:\LabExclusion"

# Verify the exclusion was added
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

### Step 1.5 — Remove the Exclusion

```powershell
Remove-MpPreference -ExclusionPath "C:\LabExclusion"

# Verify it was removed
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```

---

## Part 2: Windows Firewall Rules

### Step 2.1 — View Current Profile Settings

```powershell
Get-NetFirewallProfile | Select-Object Name, Enabled,
    DefaultInboundAction, DefaultOutboundAction
```

### Step 2.2 — Create an Inbound Allow Rule

```powershell
New-NetFirewallRule `
    -DisplayName "Lab14 Allow TCP 9000 Inbound" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 9000 `
    -Action Allow `
    -Profile Domain `
    -Description "Module 14 lab test rule"

# Verify
Get-NetFirewallRule -DisplayName "Lab14 Allow TCP 9000 Inbound" |
    Select-Object DisplayName, Direction, Action, Profile, Enabled
```

### Step 2.3 — Create a Conflicting Block Rule

```powershell
New-NetFirewallRule `
    -DisplayName "Lab14 Block TCP 9000 Inbound" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 9000 `
    -Action Block `
    -Profile Domain `
    -Description "Module 14 lab block rule — tests rule priority"
```

### Step 2.4 — Verify Block Takes Precedence

Both rules now target inbound TCP 9000 on the Domain profile. Review both rules and confirm your understanding of which one wins:

```powershell
Get-NetFirewallRule -DisplayName "Lab14*" |
    Select-Object DisplayName, Direction, Action, Enabled |
    Sort-Object Action
```

Document your answer: which rule takes precedence and why?

### Step 2.5 — Enable Firewall Logging

```powershell
Set-NetFirewallProfile -Profile Domain `
    -LogFileName "C:\Windows\System32\LogFiles\Firewall\domainfw.log" `
    -LogMaxSizeKilobytes 4096 `
    -LogAllowed True `
    -LogBlocked True

# Confirm logging is configured
Get-NetFirewallProfile -Profile Domain |
    Select-Object Name, LogFileName, LogAllowed, LogBlocked
```

### Step 2.6 — Clean Up Lab Rules

```powershell
Remove-NetFirewallRule -DisplayName "Lab14 Allow TCP 9000 Inbound" -Confirm:$false
Remove-NetFirewallRule -DisplayName "Lab14 Block TCP 9000 Inbound" -Confirm:$false
```

---

## Part 3: Just Enough Administration Endpoint

### Step 3.1 — Create the JEA Directory Structure

```powershell
New-Item -ItemType Directory -Path "C:\JEALab" -Force
New-Item -ItemType Directory -Path "C:\JEALab\RoleCapabilities" -Force
New-Item -ItemType Directory -Path "C:\JEALab\Transcripts" -Force
```

### Step 3.2 — Create a Role Capability File

```powershell
New-PSRoleCapabilityFile `
    -Path "C:\JEALab\RoleCapabilities\ServerMonitor.psrc" `
    -Description "Read-only server monitoring role for helpdesk" `
    -VisibleCmdlets @(
        "Get-Service",
        "Get-Process",
        "Get-EventLog",
        "Get-ComputerInfo",
        "Get-Volume",
        "Get-Disk"
    ) `
    -VisibleProviders "FileSystem"
```

### Step 3.3 — Create a Session Configuration File

```powershell
New-PSSessionConfigurationFile `
    -Path "C:\JEALab\LabJEA.pssc" `
    -SessionType RestrictedRemoteServer `
    -RunAsVirtualAccount `
    -TranscriptDirectory "C:\JEALab\Transcripts" `
    -RoleDefinitions @{
        "BUILTIN\Administrators" = @{
            RoleCapabilityFiles = "C:\JEALab\RoleCapabilities\ServerMonitor.psrc"
        }
    } `
    -Description "Lab 14 JEA endpoint for server monitoring"
```

### Step 3.4 — Validate the Session Configuration File

```powershell
Test-PSSessionConfigurationFile -Path "C:\JEALab\LabJEA.pssc"
```

The output should be `True`. If it returns `False`, review the file for syntax errors.

### Step 3.5 — Register the JEA Endpoint

```powershell
Register-PSSessionConfiguration `
    -Path "C:\JEALab\LabJEA.pssc" `
    -Name "Lab14_ServerMonitor" `
    -Force

# Verify the endpoint is registered
Get-PSSessionConfiguration | Where-Object Name -eq "Lab14_ServerMonitor" |
    Select-Object Name, Enabled, RunAsUser
```

### Step 3.6 — Connect to the JEA Endpoint and Test Constraints

```powershell
# Connect to the JEA endpoint on the local machine
$jeasession = New-PSSession -ComputerName "localhost" `
    -ConfigurationName "Lab14_ServerMonitor"

# Test an allowed command
Invoke-Command -Session $jeasession -ScriptBlock {
    Get-Service | Select-Object -First 5 Name, Status
}

# Test a blocked command (should fail)
Invoke-Command -Session $jeasession -ScriptBlock {
    Get-ADUser -Filter *
} -ErrorAction SilentlyContinue

# Check the language mode
Invoke-Command -Session $jeasession -ScriptBlock {
    $ExecutionContext.SessionState.LanguageMode
}
```

Document the language mode returned. Was `Get-ADUser` blocked? What error did you receive?

### Step 3.7 — Check the Transcript

```powershell
# View the transcript generated by the JEA session
$transcriptPath = "C:\JEALab\Transcripts"
Get-ChildItem $transcriptPath | Select-Object Name, LastWriteTime

# View the content of the most recent transcript
$latest = Get-ChildItem $transcriptPath | Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
Get-Content $latest.FullName | Select-Object -First 30
```

### Step 3.8 — Remove the JEA Endpoint

```powershell
Unregister-PSSessionConfiguration -Name "Lab14_ServerMonitor" -Force
```

---

## Part 4: LAPS Configuration

### Step 4.1 — Check for Windows LAPS

```powershell
# Check if Windows LAPS is available (Windows Server 2022+)
Get-Command Get-LapsADPassword -ErrorAction SilentlyContinue
```

If Windows LAPS is available, continue. If not, note this in your lab report — Windows LAPS requires Windows Server 2022 or a Windows Server 2019 with the LAPS update applied.

### Step 4.2 — Update AD Schema for Windows LAPS

```powershell
# Requires Domain Admin rights
Update-LapsADSchema -Verbose
```

### Step 4.3 — Grant Computer Self-Permission

```powershell
# Grant computers in the default Computers OU permission to update their LAPS attribute
Set-LapsADComputerSelfPermission -Identity "CN=Computers,DC=contoso,DC=local"
```

Replace `DC=contoso,DC=local` with your actual domain DN.

### Step 4.4 — View LAPS Policy Settings

```powershell
# Check current LAPS policy configuration on this machine
Get-LapsADPasswordExpirationTime -Identity $env:COMPUTERNAME -ErrorAction SilentlyContinue

# View LAPS Group Policy settings (if configured)
Get-ItemProperty `
    "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\LAPS" `
    -ErrorAction SilentlyContinue
```

---

## Part 5: Security Audit Events

### Step 5.1 — Enable Logon Auditing

```powershell
# Enable both success and failure logon auditing
auditpol /set /subcategory:"Logon" /success:enable /failure:enable

# Verify
auditpol /get /subcategory:"Logon"
```

### Step 5.2 — Generate a Failed Logon Event

Intentionally attempt a logon with wrong credentials. Open a separate PowerShell window and run:

```powershell
# This will fail with wrong password — generates event 4625
$wrongCred = New-Object PSCredential(".\FakeUser",
    (ConvertTo-SecureString "WrongPassword!" -AsPlainText -Force))
Enter-PSSession -ComputerName localhost -Credential $wrongCred -ErrorAction SilentlyContinue
```

### Step 5.3 — Query the Security Event Log

```powershell
# Find recent failed logon events (Event ID 4625)
Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = 4625
    StartTime = (Get-Date).AddMinutes(-15)
} | Select-Object TimeCreated, Message -First 5 |
    Format-List
```

---

## Lab Deliverables

Answer the following in your lab report:

1. What was the Windows Defender signature age before you ran `Update-MpSignature`? What was it after?

2. Paste the output of `Get-NetFirewallRule -DisplayName "Lab14*"` showing both your Allow and Block rules before cleanup.

3. In your own words: when both an Allow and a Block rule target the same traffic, which wins and why?

4. Paste the output of `Test-PSSessionConfigurationFile` showing your JEA configuration is valid.

5. What language mode did the JEA session return in Step 3.6? Why is this mode used in JEA endpoints?

6. Was `Get-ADUser` blocked inside the JEA endpoint? What error message did you receive?

7. Paste the first 15 lines of your JEA transcript showing the commands you ran inside the session.

8. Paste the output of the failed logon event (Event ID 4625) from Step 5.3.

---

## Troubleshooting Tips

**JEA endpoint registration fails**: Ensure the `.pssc` file passed validation (`Test-PSSessionConfigurationFile` returns `True`). Common issues include typos in cmdlet names in the role capability file.

**LAPS schema update fails**: You must run `Update-LapsADSchema` as a Domain Admin. Enterprise Admin rights are required to extend the AD schema.

**Event 4625 not appearing**: Ensure logon auditing is enabled (`auditpol /get /subcategory:"Logon"` shows Success and Failure). The Security event log may require elevated rights to read.

---

## Part 9 — Challenge Exercise

### Challenge 1: Build a Multi-Role JEA Endpoint with Parameter Constraints

A well-designed JEA endpoint grants different capabilities to different teams.
Build a JEA endpoint that supports two roles: HelpDesk (service management) and
NetworkOps (DNS management), with parameter restrictions to prevent misuse.

1. Create the HelpDesk role capability file that allows service status queries
   and restarts, but restricts `Restart-Service` to only specific safe services:

   ```powershell
   $helpDeskDir = "C:\JEA\RoleCapabilities"
   New-Item -ItemType Directory -Path $helpDeskDir -Force

   New-PSRoleCapabilityFile -Path "$helpDeskDir\HelpDesk.psrc" `
       -VisibleCmdlets @(
           "Get-Service",
           "Get-Process",
           @{ Name = "Restart-Service"; Parameters = @{ Name = "Name"; ValidateSet = "Spooler","W32Time","DNS" } }
       ) `
       -VisibleExternalCommands @("C:\Windows\System32\ipconfig.exe")
   ```

2. Create the NetworkOps role capability file permitting DNS record management:

   ```powershell
   New-PSRoleCapabilityFile -Path "$helpDeskDir\NetworkOps.psrc" `
       -VisibleCmdlets @(
           "Get-DnsServerResourceRecord",
           "Add-DnsServerResourceRecordA",
           "Remove-DnsServerResourceRecord",
           "Resolve-DnsName"
       ) `
       -ModulesToImport @("DnsServer")
   ```

3. Create the session configuration file mapping AD groups to roles:

   ```powershell
   $sessionDir = "C:\Program Files\WindowsPowerShell\Modules\JEA_LabEndpoint"
   New-Item -ItemType Directory -Path $sessionDir -Force

   New-PSSessionConfigurationFile -Path "C:\JEA\LabEndpoint.pssc" `
       -SessionType RestrictedRemoteServer `
       -RunAsVirtualAccount `
       -RoleDefinitions @{
           "txwes\HelpDesk"    = @{ RoleCapabilityFiles = "$helpDeskDir\HelpDesk.psrc" }
           "txwes\NetworkOps"  = @{ RoleCapabilityFiles = "$helpDeskDir\NetworkOps.psrc" }
       } `
       -TranscriptDirectory "C:\JEA\Transcripts" `
       -LanguageMode NoLanguage

   Test-PSSessionConfigurationFile -Path "C:\JEA\LabEndpoint.pssc"
   ```

4. Register the endpoint and test that parameter validation works correctly:

   ```powershell
   Register-PSSessionConfiguration -Name "LabEndpoint" `
       -Path "C:\JEA\LabEndpoint.pssc" -Force

   # Test — attempt to restart an unauthorized service (should fail)
   $session = New-PSSession -ComputerName localhost -ConfigurationName LabEndpoint
   Invoke-Command -Session $session -ScriptBlock {
       Restart-Service -Name "EventLog"   # Should be blocked by ValidateSet
   }
   Remove-PSSession $session
   ```

   In your lab notes, record the exact error message when `Restart-Service -Name EventLog` is blocked, and explain the difference between blocking the cmdlet entirely versus restricting its parameters with `ValidateSet`.

### Challenge 2: Create an Automated Security Posture Report

Build a PowerShell script that collects key security indicators from a server
and generates a structured HTML report.

1. Create the security data collection function:

   ```powershell
   function Get-SecurityPosture {
       param([string]$ComputerName = "localhost")

       $avStatus  = Get-MpComputerStatus
       $fwDomain  = Get-NetFirewallProfile -Profile Domain
       $failedLogons = (Get-WinEvent -FilterHashtable @{
           LogName='Security'; Id=4625
           StartTime=(Get-Date).AddDays(-1)
       } -ErrorAction SilentlyContinue).Count
       $lockouts  = (Get-WinEvent -FilterHashtable @{
           LogName='Security'; Id=4740
           StartTime=(Get-Date).AddDays(-1)
       } -ErrorAction SilentlyContinue).Count

       [PSCustomObject]@{
           Computer           = $ComputerName
           AVEnabled          = $avStatus.AntivirusEnabled
           AVSignatureAge     = $avStatus.AntivirusSignatureAge
           FWDomainEnabled    = $fwDomain.Enabled
           FWDefaultInbound   = $fwDomain.DefaultInboundAction
           FailedLogons24h    = $failedLogons
           Lockouts24h        = $lockouts
           ReportTime         = (Get-Date).ToString("yyyy-MM-dd HH:mm")
       }
   }
   ```

2. Run the function and display the report:

   ```powershell
   $report = Get-SecurityPosture -ComputerName "DC1"
   $report | Format-List *
   ```

3. Export the report as both CSV and an HTML file for documentation:

   ```powershell
   $report | Export-Csv "C:\Reports\SecurityPosture_$(Get-Date -Format yyyyMMdd).csv" `
       -NoTypeInformation

   $report | ConvertTo-Html -Title "Security Posture Report" `
       -PreContent "<h1>DC1 Security Posture — $(Get-Date -Format 'yyyy-MM-dd')</h1>" |
       Out-File "C:\Reports\SecurityPosture_$(Get-Date -Format yyyyMMdd).html"

   # Open the HTML report
   Start-Process "C:\Reports\SecurityPosture_$(Get-Date -Format yyyyMMdd).html"
   ```

4. Add a risk flag that highlights servers with antivirus signatures older than
   3 days or more than 50 failed logons in 24 hours:

   ```powershell
   if ($report.AVSignatureAge -gt 3) {
       Write-Warning "AV signatures on $($report.Computer) are $($report.AVSignatureAge) days old — update required"
   }

   if ($report.FailedLogons24h -gt 50) {
       Write-Warning "$($report.FailedLogons24h) failed logons in 24h on $($report.Computer) — investigate brute force"
   }
   ```

   In your lab notes, record the values for `AVSignatureAge` and `FailedLogons24h`
   from your report, and describe how this script could be extended to run daily
   via a scheduled task and email alerts to the security team.

### Reflection Questions

1. Just Enough Administration reduces administrative attack surface by granting
   only the minimum required permissions. However, a JEA endpoint requires
   significant upfront design: defining roles, testing capabilities, and
   maintaining capability files as the environment changes. Describe the process
   you would follow to onboard a new "StorageOps" role to an existing JEA
   endpoint, including how you would determine the minimum necessary cmdlets,
   test the role without disrupting existing roles, and maintain the configuration
   over time as PowerShell modules are updated.

2. LAPS solves the lateral movement risk of shared local administrator passwords.
   However, a security auditor notes that LAPS passwords are stored in Active
   Directory and any user with Read permission on the `msLAPS-Password` attribute
   can retrieve them. Describe the access control model you would implement for
   LAPS password retrieval — including which groups need read access, how you
   would audit password retrievals, and what additional control Windows LAPS
   (built-in) provides over legacy LAPS to protect the stored password.
