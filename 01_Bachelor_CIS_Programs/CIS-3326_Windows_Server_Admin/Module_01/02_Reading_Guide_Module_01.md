# Reading Guide: Module 01 - Windows Server Installation and Editions

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

---

### Introduction

Welcome to Module 01. This reading guide covers the foundational knowledge you need before configuring any Windows Server role. Understanding edition differences, installation options, post-install configuration steps, and activation models is prerequisite knowledge for every topic in this course and is directly tested on the AZ-800 exam.

Work through each section in order, complete the study checklist at the end, and review the exam tips before attempting the quiz.

---

### 1. Windows Server Editions

#### 1.1 Edition Overview

Microsoft publishes Windows Server in three primary editions under the Long-Term Servicing Channel (LTSC):

| Edition | VM Licensing | Key Features | Typical Use Case |
|---|---|---|---|
| Standard | 2 VMs per license | Full role support | Physical servers, low virtualization |
| Datacenter | Unlimited VMs | Storage Spaces Direct, Shielded VMs, SDN | Hypervisor hosts, large deployments |
| Essentials | No Hyper-V hosting | Limited roles, up to 25 users | Small business, single server |

The Standard and Datacenter editions are the focus of this course and the AZ-800 exam. Essentials is out of scope for certification testing beyond awareness questions.

#### 1.2 Standard vs. Datacenter Decision

The cost per license is significantly higher for Datacenter, but the break-even point is typically around 8 to 10 VMs per physical host. A single Datacenter license covers all VMs on that host. Running 10 VMs on a Standard-licensed host requires 5 Standard licenses (2 VMs each), which at standard pricing often exceeds the Datacenter price.

Additional Datacenter-exclusive features include:

- Storage Spaces Direct (S2D) — software-defined storage using local drives
- Shielded Virtual Machines — VM encryption and attestation for Hyper-V fabric
- Host Guardian Service — attestation for shielded VM fabric
- Software Defined Networking (SDN) — network virtualization at scale

If a scenario question mentions any of these features, the correct edition is always Datacenter.

#### 1.3 In-Place Edition Upgrade

You can upgrade a Standard installation to Datacenter without a full OS reinstall using DISM:

```cmd
DISM /online /Set-Edition:ServerDatacenter /ProductKey:XXXXX-XXXXX-XXXXX-XXXXX-XXXXX /AcceptEula
```

Downgrade from Datacenter to Standard requires a full reinstall. This asymmetry is a recurring exam question.

---

### 2. Installation Options

#### 2.1 Desktop Experience

Desktop Experience is the full graphical installation. It includes:

- Windows graphical shell (Explorer, taskbar, Start menu)
- Server Manager console
- All MMC snap-ins (Active Directory Users and Computers, DNS Manager, etc.)
- Internet Explorer / Edge browser
- All graphical administrative tools

Use Desktop Experience when administrators are not yet fluent in PowerShell, when a server requires local GUI-based troubleshooting, or when a third-party application requires graphical components.

#### 2.2 Server Core

Server Core omits the graphical shell. After login, the administrator sees only a command prompt and optionally a PowerShell window. There is no Server Manager, no MMC, no taskbar.

Advantages of Server Core:

- Smaller attack surface — fewer installed binaries means fewer potential vulnerabilities
- Lower RAM consumption — typically 1 to 2 GB less than Desktop Experience
- Fewer monthly reboots — fewer components to patch
- Smaller disk footprint — relevant for VMs with thin-provisioned disks

Management options for Server Core:

| Tool | Method | Notes |
|---|---|---|
| sconfig | Local interactive menu | First-boot configuration |
| PowerShell | Local or remote (WinRM) | Primary ongoing management |
| Windows Admin Center | Browser-based remote GUI | Strategic MMC replacement |
| RSAT | Remote from admin workstation | Full MMC access remotely |
| Enter-PSSession | Remote PowerShell session | Scriptable remote management |

#### 2.3 Nano Server

Nano Server is a minimal container/cloud image. It does not support traditional server roles (AD DS, DNS, DHCP, File Services, etc.). It is not a valid answer for branch-office role deployment scenarios. Use Server Core for minimum-footprint role deployments; use Nano Server only for container host base images.

---

### 3. Post-Installation Configuration

#### 3.1 Required First-Boot Tasks

Every new Windows Server deployment requires these tasks before the server enters production:

1. Set a unique, descriptive hostname following your naming convention
2. Assign a static IP address (servers must not use DHCP)
3. Configure the DNS client to point to an internal DNS server
4. Set the default gateway
5. Configure the time zone and time synchronization source
6. Join the Active Directory domain (or workgroup)
7. Apply Windows Update to current patch level
8. Enable Remote Desktop or PowerShell remoting for ongoing management

#### 3.2 sconfig Reference

The `sconfig` utility on Server Core provides a numbered text menu:

| Option | Function |
|---|---|
| 1 | Domain/Workgroup membership |
| 2 | Computer Name |
| 3 | Add Local Administrator |
| 4 | Configure Remote Management |
| 5 | Windows Update Settings |
| 6 | Download and Install Updates |
| 7 | Remote Desktop |
| 8 | Network Settings |
| 9 | Date and Time |
| 11 | Windows Activation |
| 13 | Restart Server |
| 14 | Shut Down Server |
| 15 | Exit to Command Line |

#### 3.3 PowerShell First-Boot Reference

```powershell
# Rename the computer
Rename-Computer -NewName "SRV-CORE-01" -Restart

# List network adapters
Get-NetAdapter

# Set a static IP address
New-NetIPAddress -InterfaceAlias "Ethernet" `
    -IPAddress "192.168.10.10" -PrefixLength 24 `
    -DefaultGateway "192.168.10.1"

# Set DNS server address
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" `
    -ServerAddresses "192.168.10.1"

# Join an Active Directory domain
Add-Computer -DomainName "corp.local" `
    -Credential (Get-Credential) `
    -OUPath "OU=Servers,DC=corp,DC=local" -Restart

# Enable PowerShell remoting
Enable-PSRemoting -Force

# Enable Remote Desktop via registry
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Terminal Server" `
    -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"

# Verify IP configuration
Get-NetIPAddress -InterfaceAlias "Ethernet"
Get-DnsClientServerAddress -InterfaceAlias "Ethernet"
```

---

### 4. Windows Admin Center

Windows Admin Center (WAC) is a browser-based, locally deployed management platform. Key facts:

- Installed on a Windows 10/11 workstation or Windows Server machine (not cloud-hosted)
- Communicates over WinRM: HTTP port 5985, HTTPS port 5986
- No agent required on managed nodes
- Provides GUI access to Server Core machines
- Covers: PowerShell, Event Viewer, Storage, Networking, Roles and Features, Hyper-V, Certificates, Firewall
- Strategic replacement for traditional MMC snap-ins (not a full replacement yet — some tasks still require MMC)

---

### 5. Licensing and Activation

#### 5.1 Key Management Service (KMS)

KMS is the standard activation method for enterprise environments:

- Requires a KMS host installed on the internal network
- Requires a minimum of 5 servers (25 for Windows clients) before the KMS host issues activations
- Servers renew activation automatically every 180 days by contacting the KMS host
- Domain-joined servers find the KMS host via a DNS SRV record: `_vlmcs._tcp`
- No manual intervention required after KMS host is configured

#### 5.2 Multiple Activation Key (MAK)

MAK is used for machines that cannot reach a KMS host:

- Fixed pool of activations (quantity defined at purchase)
- Each activation contacts Microsoft's activation servers (or Volume Activation Management Tool proxy)
- Appropriate for air-gapped networks, secure facilities, small deployments
- Once the activation pool is exhausted, additional machines cannot be activated with the same key

#### 5.3 Azure Hybrid Benefit

- Allows on-premises Windows Server licenses with Software Assurance to be used in Azure VMs
- Reduces per-VM licensing cost in Azure for organizations with existing SA coverage
- Relevant to AZ-800 hybrid scenario questions

---

### 6. Servicing Channels

| Channel | Description | Support Life |
|---|---|---|
| Long-Term Servicing Channel (LTSC) | Full role support, traditional deployments | 5 years mainstream + 5 years extended |
| Annual Channel (discontinued) | Semi-annual feature releases — containers/cloud | 18 months (now discontinued for on-premises) |

All new on-premises deployments use LTSC. Annual Channel releases are no longer issued for on-premises use.

---

### 7. Architecture Diagram: Installation Decision Flow

```text
Start: Deploy Windows Server
         |
         v
    Choose Edition
    /            \
Standard        Datacenter
(2 VMs/lic)   (Unlimited VMs,
               S2D, Shielded VMs)
         |
         v
  Choose Installation Option
  /                    \
Server Core         Desktop Experience
(No GUI,            (Full GUI,
 smaller footprint,  Server Manager,
 remote management)  MMC snap-ins)
         |
         v
  Post-Install Configuration
  - Hostname (sconfig option 2 / Rename-Computer)
  - Static IP (sconfig option 8 / New-NetIPAddress)
  - DNS (Set-DnsClientServerAddress)
  - Domain join (sconfig option 1 / Add-Computer)
  - Windows Update (sconfig option 5)
         |
         v
      Activation
      /        \
    KMS         MAK
(Enterprise,  (Isolated,
 auto-renews)  fixed pool)
```

---

### 8. Exam Tips for Module 01

The following tips address the most frequently tested concepts in this module area.

**Tip 1 — Server Core for attack surface:** Any scenario asking for minimum attack surface, fewest installed components, or lowest patch overhead means Server Core. Nano Server is only for container base images, not traditional role deployment.

**Tip 2 — sconfig vs. PowerShell:** The exam may ask which tool provides an interactive numbered menu for Server Core first-boot configuration. The answer is `sconfig`. If the question asks for the scriptable/automatable equivalent, list the PowerShell cmdlets.

**Tip 3 — Edition upgrade direction:** DISM `/Set-Edition` upgrades Standard to Datacenter in-place. Downgrade requires reinstall. This is tested as a distractor — choices that suggest downgrading via DISM are wrong.

**Tip 4 — KMS minimum count:** KMS requires at least 5 servers requesting activation before the host issues activations. This threshold is tested. MAK has no minimum — one machine can activate with MAK.

**Tip 5 — WAC port:** Windows Admin Center uses WinRM on ports 5985 (HTTP) and 5986 (HTTPS). It is not cloud-hosted. No agent is required on managed nodes.

**Tip 6 — Nano Server scope:** Nano Server cannot host DNS, DHCP, AD DS, File Services, or any traditional server role. It is a container/cloud base image only.

**Tip 7 — Standard VM count:** One Standard license = 2 VMs. Always calculate license count by dividing VM count by 2, rounding up.

**Tip 8 — Azure Hybrid Benefit:** If a scenario mentions using existing on-premises Windows Server licenses in Azure, the answer involves Azure Hybrid Benefit combined with Software Assurance.

---

### 9. Key Terms Glossary

| Term | Definition |
|---|---|
| LTSC | Long-Term Servicing Channel — 10-year support lifecycle for Windows Server |
| Server Core | Installation option with no graphical shell; managed via PowerShell, WAC, or RSAT |
| Desktop Experience | Full graphical installation including Server Manager and MMC snap-ins |
| sconfig | Text-based first-boot configuration menu for Server Core |
| Windows Admin Center | Browser-based, on-premises management platform for Windows Server |
| KMS | Key Management Service — internal activation server for enterprise deployments |
| MAK | Multiple Activation Key — fixed-pool key for isolated deployments |
| DISM | Deployment Image Servicing and Management — tool for in-place edition upgrades |
| WinRM | Windows Remote Management — protocol used by PowerShell remoting and WAC |
| Azure Hybrid Benefit | License portability from on-premises SA-covered Windows Server to Azure VMs |
| Nano Server | Minimal container base image — does not support traditional server roles |
| Storage Spaces Direct | Datacenter-exclusive software-defined storage using local drives |
| Shielded VMs | Datacenter-exclusive encrypted VMs protected by Host Guardian Service |

---

### 10. Study Checklist

Complete each item before attempting the quiz.

- Read Section 1 (Editions) and memorize the Standard vs. Datacenter feature table
- Read Section 2 (Installation Options) and understand the Server Core vs. Desktop Experience trade-offs
- Read Section 3 (Post-Installation Configuration) and review all sconfig options and PowerShell cmdlets
- Read Section 4 (Windows Admin Center) and note the port numbers and deployment model
- Read Section 5 (Activation) and distinguish KMS from MAK use cases
- Review the Architecture Diagram in Section 7
- Review all 8 Exam Tips in Section 8
- Review the Key Terms Glossary in Section 9
- Complete the Lab activity for Module 01
- Complete the Quiz for Module 01
- Post your initial Discussion response by Wednesday 11:59 PM

---

### Additional Reading

- [Windows Server Get Started documentation](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-windows-server)
- [Windows Server 2022 editions comparison](https://learn.microsoft.com/en-us/windows-server/get-started/editions-comparison-windows-server-2022)
- [Server Core administration guide](https://learn.microsoft.com/en-us/windows-server/administration/server-core/server-core-administration)
- [Windows Admin Center overview](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview)
- [Volume Activation overview](https://learn.microsoft.com/en-us/windows/deployment/volume-activation/volume-activation-windows-10)

---

## 9. Supplemental Resources

The following free, open-access resources go deeper on Module 01 topics:

**1. Microsoft Learn — Windows Server on-premises deployment**
<https://learn.microsoft.com/en-us/training/paths/windows-server-deployment-configuration-administration/>
A complete Microsoft Learn path covering Windows Server deployment, configuration, and administration aligned to AZ-800. Includes interactive exercises for Server Core setup, edition selection, and activation.

**2. Microsoft Learn — Administer Windows Server Core**
<https://learn.microsoft.com/en-us/training/modules/administer-windows-server-core/>
Module-level deep dive into Server Core management using sconfig, PowerShell, Windows Admin Center, and RSAT. Includes sandbox exercises you can complete in a browser.

**3. Microsoft Learn — Implement Windows Server hybrid infrastructure**
<https://learn.microsoft.com/en-us/training/paths/implement-windows-server-hybrid-infrastructure/>
Covers Azure Hybrid Benefit, hybrid activation, and connecting on-premises Windows Server to Azure services — directly relevant to AZ-800 hybrid scenario questions.

**4. Microsoft Tech Community — Windows Server Blog**
<https://techcommunity.microsoft.com/category/windows-server/blog/windowsserverblog>
Official Microsoft blog for Windows Server release announcements, edition changes, and servicing channel updates. Useful for staying current on LTSC lifecycle dates and new edition features.
