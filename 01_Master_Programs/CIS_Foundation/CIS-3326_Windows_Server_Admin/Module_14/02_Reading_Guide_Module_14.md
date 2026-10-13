# Reading Guide: Module 14 — Windows Server Security

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3326 &BULL; WINDOWS SERVER ADMINISTRATION & ACTIVE DIRECTORY</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Microsoft Windows Server Administration

---

## Overview

This reading guide covers the five major security technologies in Module 14: Windows Defender Antivirus, Windows Firewall with Advanced Security, Just Enough Administration, Credential Guard, and LAPS. Security concepts appear heavily on all Microsoft certification exams — both the AZ-800 and AZ-801 tracks.

---

## Part 1: Windows Defender Antivirus

### 1.1 Defender on Server Core

Windows Server Core installations include Windows Defender but have no graphical interface. All Defender management on Server Core is done via PowerShell using the `Defender` module or via Group Policy.

```powershell
# Key Defender status and management commands
Get-MpComputerStatus            # Overall status
Get-MpPreference                # Current configuration
Get-MpThreatDetection           # Recent detected threats
Start-MpScan -ScanType QuickScan
Update-MpSignature              # Force definition update
Set-MpPreference -DisableRealtimeMonitoring $false   # Ensure RTP is on
```

### 1.2 Automatic Exclusions

When Windows Server roles are installed, Defender automatically adds exclusions for performance-critical paths associated with that role. For example, installing Hyper-V automatically excludes VM storage directories. These auto-exclusions are documented by Microsoft for each role.

Custom exclusions should be added only when there is a documented performance or compatibility need. Each exclusion increases risk by creating a potential blind spot.

### 1.3 Attack Surface Reduction Rules

ASR rules block specific behaviors rather than specific files or signatures. They are policy-driven and can be deployed via Group Policy or Intune. Key ASR rules tested on exams:

- Block Office applications from creating child processes
- Block credential stealing from LSASS
- Block executable content from email and webmail
- Block JavaScript/VBScript from launching downloaded executables
- Use advanced ransomware protection

---

## Part 2: Windows Firewall with Advanced Security

### 2.1 Rule Evaluation Order

Understanding how WFAS evaluates rules is critical for both troubleshooting and exam questions.

Rules are evaluated in this order:

1. Authenticated bypass rules (IPsec-authenticated exceptions — highest priority)
2. Block connection rules
3. Allow connection rules
4. Default profile behavior (block inbound, allow outbound)

Within each category, more specific rules take effect over less specific ones. If there is any ambiguity, a Block rule beats an Allow rule.

### 2.2 Exporting and Importing Firewall Policies

For consistent firewall configuration across many servers, export the policy from a reference server and import it on others.

```powershell
# Export all firewall rules to a file
netsh advfirewall export "C:\FirewallPolicy.wfw"

# Import firewall policy from a file
netsh advfirewall import "C:\FirewallPolicy.wfw"
```

Group Policy is the preferred method for maintaining consistent firewall policies across a fleet of servers — deploy via Computer Configuration > Windows Settings > Security Settings > Windows Firewall with Advanced Security.

### 2.3 Monitoring Firewall Activity

```powershell
# Enable firewall logging
Set-NetFirewallProfile -Profile Domain `
    -LogFileName "C:\Windows\System32\LogFiles\Firewall\domainfw.log" `
    -LogMaxSizeKilobytes 4096 `
    -LogAllowed True `
    -LogBlocked True

# View recently blocked connections
Get-Content "C:\Windows\System32\LogFiles\Firewall\domainfw.log" |
    Where-Object { $_ -like "*DROP*" } |
    Select-Object -Last 20
```

---

## Part 3: Just Enough Administration Deep Dive

### 3.1 NoLanguage Mode

JEA endpoints run in NoLanguage mode by default. This means users cannot use PowerShell language features like loops, variables, or script blocks. They can only call the specific commands defined in their Role Capability file. This is intentional — it prevents privilege escalation through creative scripting.

```powershell
# Check what language mode a session is running in
$ExecutionContext.SessionState.LanguageMode
```

Inside a standard PowerShell session, this returns `FullLanguage`. Inside a JEA session, it returns `NoLanguage`.

### 3.2 Virtual Accounts vs. Group Managed Service Accounts

JEA sessions can run as either a **virtual account** or a **Group Managed Service Account (gMSA)**.

**Virtual account**: A temporary local administrator account created by Windows for the duration of the JEA session. It exists only on the local machine and only while the session is active. Easiest to configure, good for single-server scenarios.

**Group Managed Service Account (gMSA)**: An Active Directory service account with an automatically rotated password, managed by Active Directory. Required when the JEA session needs to access network resources (because virtual accounts have no domain identity).

```powershell
# Configure JEA to use a gMSA instead of a virtual account
New-PSSessionConfigurationFile `
    -Path "C:\JEA\Config.pssc" `
    -GroupManagedServiceAccount "CONTOSO\JEA_gMSA$" `
    -SessionType RestrictedRemoteServer `
    -RoleDefinitions @{
        "CONTOSO\Helpdesk" = @{ RoleCapabilityFiles = "C:\JEA\RC\Helpdesk.psrc" }
    }
```

### 3.3 JEA Audit Trail

Every command executed through a JEA endpoint is logged in two places:

- **PowerShell operational log**: Records session start/end
- **Transcript files**: If `TranscriptDirectory` is configured, a complete log of every command and its output is saved per session

This audit trail is a key security and compliance benefit of JEA — you know exactly what each user did during every administrative session.

---

## Part 4: Credential Guard

### 4.1 Virtualization-Based Security Architecture

Credential Guard requires Virtualization-Based Security (VBS). When VBS is enabled, the hypervisor creates two isolated environments:

- **Normal World (Ring 0 / Ring 3)**: The standard Windows kernel and user mode. Even with kernel-level access, attackers cannot read VSM memory.
- **Secure World (Virtual Secure Mode)**: A separate, isolated Hyper-V partition where sensitive data lives. Only signed, trusted code runs here.

The Windows credential manager stores NTLM hashes and Kerberos tickets in the Secure World. LSASS runs in the Normal World but offloads credential operations to the Isolated LSASS (IsoLSASS) process in the Secure World.

### 4.2 What Credential Guard Protects Against

Credential Guard specifically blocks:

- **Pass-the-Hash (PTH)**: Extracting NTLM hashes from LSASS and using them to authenticate without knowing the plaintext password
- **Pass-the-Ticket (PTT)**: Extracting Kerberos tickets from LSASS and using them to authenticate to other services
- **Overpass-the-Hash**: Converting an NTLM hash into a Kerberos ticket

Credential Guard does NOT protect against:

- Keyloggers that capture passwords as they are typed
- Social engineering attacks
- Compromised domain controllers (if the DC is compromised, all domain credentials are at risk)

### 4.3 Credential Guard Limitations

Some scenarios are incompatible with Credential Guard:

- Windows Digest authentication (disabled when Credential Guard is on)
- CredSSP credential delegation (disabled — relevant for double-hop remoting)
- NTLMv1 authentication (disabled)
- NTLM or Kerberos for authentication to specific services may require configuration changes

---

## Part 5: Local Administrator Password Solution

### 5.1 The Problem LAPS Solves

Consider an organization with 5,000 workstations all imaged with the same local Administrator password. An attacker compromises one machine and recovers the local admin password hash. They run a tool that tries this hash on all 5,000 machines simultaneously. Every machine accepts it — full lateral movement in seconds.

LAPS breaks this attack by ensuring every machine has a different local admin password.

### 5.2 LAPS AD Schema Extension

Before LAPS can store passwords in Active Directory, the AD schema must be extended to add the LAPS attributes to computer objects.

For Windows LAPS (built into Windows Server 2022):

```powershell
# Extend AD schema for Windows LAPS
Update-LapsADSchema

# Verify the new attributes were added
Get-LapsADSchema
```

For legacy LAPS (downloaded from Microsoft):

```powershell
# Import the LAPS PowerShell module
Import-Module AdmPwd.PS

# Update the AD schema
Update-AdmPwdADSchema

# Grant computers permission to update their own password attribute
Set-AdmPwdComputerSelfPermission -OrgUnit "OU=Workstations,DC=contoso,DC=com"
```

### 5.3 LAPS Password Policy

LAPS password complexity and rotation schedule are configured through Group Policy.

Key Group Policy settings:

- **Password Settings**: Complexity (uppercase, lowercase, digits, special), length, age
- **Account Managed**: Which account LAPS manages (default: built-in Administrator)
- **AD Backup Directory**: Whether to use AD DS or Azure AD
- **Post-Authentication Actions**: What happens after the password is used (reset immediately, reset after delay)

### 5.4 Reading LAPS Passwords

```powershell
# Windows LAPS — retrieve password for a specific computer
Get-LapsADPassword -Identity "DESKTOP-001" -AsPlainText

# Windows LAPS — retrieve password with expiration info
Get-LapsADPassword -Identity "DESKTOP-001" |
    Select-Object ComputerName, Password, PasswordExpirationTime

# Force a password reset on the next policy evaluation
Reset-LapsPassword -Identity "DESKTOP-001"
```

---

## Key Terms to Know

- **Windows Defender Antivirus** — built-in endpoint protection; managed via `Get-MpComputerStatus` and `Set-MpPreference`
- **ASR rules** — Attack Surface Reduction rules that block malicious behaviors
- **WFAS** — Windows Firewall with Advanced Security; host-based stateful firewall
- **Firewall profile** — Domain, Private, or Public — activated by network detection
- **Connection Security Rule** — IPsec rule for traffic authentication/encryption between computers
- **JEA** — Just Enough Administration; constrained PowerShell endpoints with role-based access
- **Session Configuration File (.pssc)** — defines who connects and which role capabilities apply
- **Role Capability File (.psrc)** — defines what commands a role can run
- **Virtual account** — temporary local admin account for JEA session execution
- **gMSA** — Group Managed Service Account; used when JEA needs network resource access
- **Credential Guard** — VBS-based isolation of NTLM hashes and Kerberos tickets
- **VSM** — Virtual Secure Mode; the isolated Hyper-V container protecting credentials
- **Pass-the-Hash** — attack using stolen NTLM hash to authenticate without the password
- **LAPS** — Local Administrator Password Solution; unique per-machine local admin passwords stored in AD
- **Windows LAPS** — built-in version in Windows Server 2022 / Windows 11 22H2+

---

## Review Questions

1. What is the difference between Attack Surface Reduction (ASR) rules and traditional antivirus signatures?

2. A Block firewall rule and an Allow firewall rule both match the same inbound traffic. Which takes precedence?

3. Explain what `-RunAsVirtualAccount` does in a JEA session configuration.

4. A JEA endpoint uses `NoLanguage` mode. What does this prevent a connected user from doing?

5. What attack does Credential Guard specifically prevent that standard NTFS permissions do not?

6. Why does Credential Guard require Virtualization-Based Security (VBS)?

7. An organization images 3,000 workstations with the same local Administrator password. How does LAPS solve the lateral movement risk this creates?

8. What AD schema change is required before Windows LAPS can function?

9. What event ID indicates a failed logon in the Windows Security event log?

10. What is the difference between a JEA Session Configuration file and a Role Capability file?

---

## Supplemental Resources

The following free, open-access resources go deeper on Module 14 topics:

**1. Microsoft Learn — Implement security in Windows Server**
<https://learn.microsoft.com/en-us/training/modules/implement-security-windows-server/>
Hands-on module covering Windows Defender Antivirus, Attack Surface Reduction rules, Just Enough Administration (JEA), Credential Guard, LAPS, and security event monitoring with sandbox exercises aligned to AZ-800.

**2. Microsoft Docs — Just Enough Administration (JEA) overview**
<https://learn.microsoft.com/en-us/powershell/scripting/learn/remoting/jea/overview>
Complete JEA documentation including session configuration files, role capability files, virtual accounts, constrained language mode, transcript logging, and step-by-step deployment guidance.

**3. Microsoft Docs — Windows Local Administrator Password Solution (Windows LAPS)**
<https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview>
Full reference for Windows LAPS including schema extension, GPO configuration, Azure AD support, password encryption at rest, and migration guidance from legacy LAPS to Windows LAPS.

**4. Microsoft Docs — Credential Guard overview**
<https://learn.microsoft.com/en-us/windows/security/identity-protection/credential-guard/credential-guard>
Technical deep-dive on Credential Guard including Virtualization-Based Security architecture, how LSAIso protects NTLM hashes and Kerberos tickets, hardware requirements, and Pass-the-Hash/Pass-the-Ticket attack prevention.
