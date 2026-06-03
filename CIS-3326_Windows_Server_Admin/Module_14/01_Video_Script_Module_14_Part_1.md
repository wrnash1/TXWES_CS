# Video Script: Module 14 — Windows Server Security (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

### Introduction

Welcome to Module 14. I'm Professor Nash, and today we're covering Windows Server Security — one of the most critical and exam-heavy areas in Windows Server administration.

Security is not a single product or a single setting. It is a layered strategy. In this module we cover five major security capabilities: Windows Defender Antivirus, Windows Firewall with Advanced Security, Just Enough Administration (JEA), Credential Guard, and Local Administrator Password Solution (LAPS). In Part 1 we cover Windows Defender, Windows Firewall, and auditing. Part 2 covers JEA, Credential Guard, and LAPS.

---

### Section 1: Windows Defender Antivirus on Server

Windows Defender Antivirus is included with Windows Server 2016 and later and is enabled by default. It provides real-time protection against malware, ransomware, and other threats.

On Windows Server, Windows Defender runs as a background service. Server Core installations include Defender functionality without a GUI — you manage it through PowerShell.

```powershell
# Check Windows Defender status
Get-MpComputerStatus | Select-Object AMRunningMode, RealTimeProtectionEnabled,
    AntivirusEnabled, AntispywareEnabled, NISEnabled

# Update definitions manually
Update-MpSignature

# Run a quick scan
Start-MpScan -ScanType QuickScan

# Run a full scan
Start-MpScan -ScanType FullScan

# Check scan history and threats found
Get-MpThreatDetection | Select-Object ThreatName, ActionSuccess, DetectionTime
```

Important: when you install certain server roles, Windows Defender may exclude those role-specific directories automatically. You can add custom exclusions for performance-sensitive workloads (like Hyper-V VM storage directories), but exclusions should be minimal and carefully documented.

```powershell
# Add a folder exclusion
Add-MpPreference -ExclusionPath "D:\HyperV\VMs"

# View current exclusions
Get-MpPreference | Select-Object ExclusionPath, ExclusionProcess, ExclusionExtension
```

---

### Section 2: Windows Firewall with Advanced Security

Windows Firewall with Advanced Security (WFAS) is a host-based stateful firewall. It controls inbound and outbound network traffic at the server level, independent of any network firewall or security appliance.

There are three network profiles.

**Domain profile**: Active when the server can communicate with a domain controller. Applied automatically on domain-joined servers in the corporate network.

**Private profile**: Active when the network is marked as trusted (home or small office environments).

**Public profile**: Active on untrusted networks. Most restrictive by default.

On a domain-joined server, the Domain profile is almost always active. All three profiles can be active simultaneously on different network adapters.

```powershell
# View profile status
Get-NetFirewallProfile | Select-Object Name, Enabled,
    DefaultInboundAction, DefaultOutboundAction

# Create an inbound allow rule for a custom application
New-NetFirewallRule -DisplayName "Allow App TCP 8443" `
    -Direction Inbound `
    -Protocol TCP `
    -LocalPort 8443 `
    -Action Allow `
    -Profile Domain

# Block a specific outbound port
New-NetFirewallRule -DisplayName "Block Telnet Outbound" `
    -Direction Outbound `
    -Protocol TCP `
    -RemotePort 23 `
    -Action Block

# View all enabled inbound rules
Get-NetFirewallRule -Direction Inbound -Enabled True |
    Select-Object DisplayName, Action, Profile
```

Key rule priority: **Block rules always take precedence over Allow rules** within the same profile. If you have both an Allow and a Block rule matching the same traffic, the Block wins.

---

### Section 3: Connection Security Rules and IPsec

Beyond filtering traffic, WFAS manages Connection Security Rules that use IPsec to authenticate and optionally encrypt traffic between specific computers. This is separate from allow/block rules — a Connection Security Rule defines the security requirements for a connection without itself allowing or blocking traffic.

Common use cases:

- Require Kerberos authentication for server-to-server communication on a sensitive segment
- Require encryption between specific application servers and database servers
- Isolate domain-joined computers from non-domain computers using domain isolation rules

---

### Section 4: Security Auditing and Event Logs

Auditing is the process of recording security-relevant events to the Windows Security event log. Auditing is essential for detecting security incidents, satisfying compliance requirements, and conducting forensic investigations.

Windows Server auditing is configured through Group Policy under:

Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration

Key audit categories:

- **Logon/Logoff** — records successful and failed interactive and network logons
- **Account Logon** — records credential validation attempts (on DCs: Kerberos tickets)
- **Object Access** — records access to audited files, folders, registry keys
- **Privilege Use** — records when privileged rights (like Act as OS) are exercised
- **Policy Change** — records changes to audit policy, trust relationships
- **Account Management** — records user/group creation, deletion, password changes
- **System** — records system startup, shutdown, security subsystem changes

```powershell
# View current audit policy settings
auditpol /get /category:*

# Enable logon auditing (success and failure)
auditpol /set /subcategory:"Logon" /success:enable /failure:enable

# Query recent failed logon events from the Security log
Get-WinEvent -FilterHashtable @{
    LogName   = "Security"
    Id        = 4625          # Event 4625 = Failed logon
    StartTime = (Get-Date).AddHours(-24)
} | Select-Object TimeCreated, Message -First 20
```

Key Security event IDs to know for certification exams:

- **4624** — Successful logon
- **4625** — Failed logon
- **4648** — Logon using explicit credentials (RunAs)
- **4720** — User account created
- **4740** — User account locked out
- **4776** — Domain controller validated credentials

---

### Section 5: Windows Event Forwarding

In large environments, reviewing security logs on each individual server is impractical. Windows Event Forwarding (WEF) allows servers to automatically forward events to a central collector server, where all events can be reviewed in one place.

```powershell
# On the collector server — configure as event collector
wecutil qc /q

# On source servers — configure to forward events
# (typically done via Group Policy)
# GPO path: Computer Configuration > Administrative Templates >
#            Windows Components > Event Forwarding
```

Windows Event Forwarding works over WinRM, so the infrastructure from Module 11 directly enables this security capability.

---

### Section 6: Microsoft Defender for Endpoint Integration

On enterprise Windows Server deployments, Windows Defender Antivirus integrates with Microsoft Defender for Endpoint (formerly Microsoft Defender ATP). This cloud-connected platform adds:

- Behavioral detection beyond signature-based scanning
- Endpoint Detection and Response (EDR) capabilities
- Automated investigation and remediation
- Threat intelligence from Microsoft's global security telemetry

For exam purposes, understand that Windows Defender on Windows Server is the local component; Microsoft Defender for Endpoint is the enterprise management and intelligence platform built on top of it.

---

### Section 7: Attack Surface Reduction Rules

Attack Surface Reduction (ASR) rules are a Windows Defender feature that blocks behaviors commonly used by malware, even before any malicious payload is detected. Examples include:

- Block Office applications from creating child processes
- Block executable content from email client and webmail
- Block JavaScript or VBScript from launching downloaded executable content
- Use advanced protection against ransomware

```powershell
# Enable an ASR rule (audit mode first, then enforce)
# Rule GUID for "Block Office apps from creating child processes"
Set-MpPreference -AttackSurfaceReductionRules_Ids `
    "D4F940AB-401B-4EFC-AADC-AD5F3C50688A" `
    -AttackSurfaceReductionRules_Actions AuditMode
```

Starting in audit mode lets you identify false positives before switching to block mode.

---

### Closing Part 1

In Part 1, we covered Windows Defender Antivirus, Windows Firewall with Advanced Security, security auditing, and the broader Windows Defender ecosystem. These form the detection and prevention layer of Windows Server security.

In Part 2, we cover the access control and privilege management layer: Just Enough Administration, Credential Guard, and LAPS. These three technologies are critical for preventing privilege escalation and lateral movement — the techniques attackers use after they have gained initial access to a network. See you in Part 2.
