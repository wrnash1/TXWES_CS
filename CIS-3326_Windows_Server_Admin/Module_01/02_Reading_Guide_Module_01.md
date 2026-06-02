# Reading Guide: Module 01 - Windows Server Installation and Editions

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
