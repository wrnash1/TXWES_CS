# Video Script: Module 01 - Windows Server Installation and Editions (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 01 - Windows Server Installation and Editions

**Part:** 1 of 2 — Concepts, Theory, and Architecture

**Estimated Duration:** 13 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Introduction]

**[SHOW SCREEN: Course title slide with module number and topic]**

Welcome to Module 01 of CIS-3326, Windows Server Administration. I am Professor Nash, and in this first module we are going to lay the foundation for everything that follows in this course. Before you can manage Active Directory, configure DNS, or deploy Hyper-V, you need to understand how Windows Server is installed, which edition you are running, and what deployment choices you made the moment you began setup.

This module aligns directly to the AZ-800 exam objective domain "Deploy and manage Active Directory Domain Services in on-premises and cloud environments," as well as the preliminary infrastructure tasks that every certified Windows Server administrator must master before domain configuration begins.

By the end of Part 1, you will understand the Windows Server edition model, the difference between Server Core and Desktop Experience, first-boot configuration requirements, and the licensing and activation models you will encounter on the exam and in the field.

---

### [SEGMENT 2 — Windows Server 2022 Overview and Edition Model]

**[SHOW SCREEN: Microsoft Learn documentation page for Windows Server editions]**

Windows Server 2022 is the current Long-Term Servicing Channel release. Microsoft follows two servicing models. The Long-Term Servicing Channel, or LTSC, is the traditional model with full role support, 10 years of support, and the editions you will work with in this course. The Annual Channel was for semi-annual feature releases that are now discontinued for on-premises; today all new on-premises deployments use LTSC.

There are three primary editions you must know for the exam.

**Standard Edition** is designed for physical servers with low or no virtualization. A single Standard license covers two Hyper-V virtual machine instances on the licensed physical host. If you need a third or fourth VM on the same host, you purchase another Standard license. Standard supports all the same server roles as Datacenter but has the two-VM cap and does not include certain storage features.

**Datacenter Edition** is for highly virtualized environments. One Datacenter license covers unlimited Hyper-V virtual machines on the licensed host. It also enables Storage Spaces Direct, Shielded Virtual Machines, and Software Defined Networking capabilities not available in Standard. Datacenter costs more, but in large hypervisor environments it is the economical choice when you run eight or more VMs per host.

**Essentials Edition** targets small businesses with up to 25 users and 50 devices. It cannot act as a Hyper-V host, cannot function as a second domain controller, and does not support most enterprise roles. You will not be tested heavily on Essentials, but you need to know it exists and when it is inappropriate.

**[SHOW SCREEN: Table comparing Standard vs. Datacenter — VM limits, features, scenarios]**

The exam will give you a scenario and ask which edition fits. Key rule: if the scenario mentions unlimited VMs, Storage Spaces Direct, Shielded VMs, or SDN — the answer is Datacenter. If it says "minimal virtualization" or "two VMs max," the answer is Standard.

---

### [SEGMENT 3 — Installation Options: Server Core vs. Desktop Experience]

**[SHOW SCREEN: Windows Server setup screen showing the four installation choices — Standard Core, Standard Desktop Experience, Datacenter Core, Datacenter Desktop Experience]**

When you run Windows Server setup, you see four choices. Two editions, each with two installation options. The installation option is arguably the most important architectural decision you make, because it is difficult to change after the fact.

**Desktop Experience** installs the full Windows graphical shell — Server Manager, the taskbar, File Explorer, all MMC snap-ins, and Windows Admin Center support. It is the familiar environment that most administrators start with. The cost is higher RAM consumption, more background services, a larger patch surface, and more reboots per month because more components require updates.

**Server Core** omits the graphical shell entirely. When you log in, you see a command prompt. No taskbar. No Start menu. No Explorer window. No MMC snap-ins. You manage Server Core entirely through PowerShell, through remote tools, or through Windows Admin Center running on a separate management machine.

**[SHOW SCREEN: Side-by-side screenshot — left: black command prompt of Server Core; right: Server Manager open in Desktop Experience]**

[Alt-text: Side-by-side comparison showing Windows Server Core on the left with only a command prompt visible, and Windows Server Desktop Experience on the right showing Server Manager and the Windows graphical interface.]

Why does Microsoft default to pushing Server Core? Three reasons.

First, **reduced attack surface**. Every graphical component that is not installed cannot be exploited. Fewer binaries on disk means a smaller vulnerability footprint.

Second, **lower resource overhead**. Server Core typically uses 1 to 2 GB less RAM than Desktop Experience on the same hardware. On a virtualization host with dozens of VMs, that difference compounds significantly.

Third, **fewer reboots**. Because fewer components require patching, Core servers reboot less frequently — a major operational benefit for production systems.

The trade-off is that Server Core requires administrators who are comfortable with PowerShell and remote management. Organizations still transitioning to PowerShell fluency often choose Desktop Experience for initial deployments, then migrate toward Core as skills mature.

---

### [SEGMENT 4 — Nano Server and Containers]

**[SHOW SCREEN: Diagram showing Nano Server as a container base image]**

You may encounter a third option called Nano Server on the AZ-800 exam. Nano Server is an extremely minimal image — smaller even than Server Core. It is optimized as a container base image and for cloud-native workloads. Critically, Nano Server does not support traditional server roles. You cannot install the DNS Server role, DHCP, Active Directory Domain Services, or most of the roles covered in this course on a Nano Server installation.

The exam distractor frequently lists Nano Server as the answer for "smallest footprint branch office DNS server." That answer is wrong. Server Core is the correct minimum-footprint option for traditional role deployments. Nano Server is for containers only.

---

### [SEGMENT 5 — Post-Installation Configuration Requirements]

**[SHOW SCREEN: sconfig menu on a Server Core console]**

[Alt-text: The sconfig text-based configuration menu showing numbered options including Computer Name, Network Settings, Windows Update, and Remote Desktop.]

When Windows Server finishes installation, it boots with a randomly generated computer name and attempts to obtain an IP address from DHCP. For production servers, both of these defaults are unacceptable.

Servers require:

- A descriptive, unique hostname that follows your organization's naming convention
- A static IP address so DNS records and client connections remain stable
- Membership in the correct Active Directory domain or workgroup
- Windows Update configured to an appropriate policy
- Remote management enabled for ongoing administration

On Desktop Experience, you handle these through Server Manager and the graphical System Properties dialogs. On Server Core, you use either **sconfig** or PowerShell.

**sconfig** is a text-based numbered menu built directly into Server Core. You type `sconfig` and press Enter, and it presents options numbered 1 through 15. Option 2 changes the computer name. Option 8 configures network settings. Option 7 controls Remote Desktop. Option 5 manages Windows Update. sconfig is the quickest tool for interactive first-boot configuration when you do not yet have PowerShell remoting established.

The equivalent PowerShell approach uses these key cmdlets:

- `Rename-Computer -NewName "SRV-CORE-01" -Restart` to rename and reboot
- `New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.10.10 -PrefixLength 24 -DefaultGateway 192.168.10.1` to set a static IP
- `Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 192.168.10.1` to configure DNS
- `Add-Computer -DomainName "corp.local" -Credential (Get-Credential) -Restart` to join a domain

These four cmdlets cover 90 percent of first-boot configuration tasks. Memorize them for the exam and for the lab.

---

### [SEGMENT 6 — Windows Admin Center]

**[SHOW SCREEN: Windows Admin Center dashboard in a browser showing managed servers]**

[Alt-text: Windows Admin Center browser interface showing a dashboard listing managed servers with connection status, CPU, and memory metrics.]

Windows Admin Center, often abbreviated WAC, is the modern strategic replacement for traditional MMC snap-ins. It is a locally deployed, browser-based management platform that you install on a Windows 10/11 or Windows Server machine and then use to connect to and manage remote servers — including Server Core machines.

Through Windows Admin Center you can access PowerShell sessions, view Event Viewer logs, manage storage, configure networking, and install server roles — all from a browser, all pointed at a remote Server Core machine that has no GUI of its own.

For the AZ-800 exam, remember that Windows Admin Center is not a cloud service — it is installed on-premises. It communicates with managed nodes over WinRM (port 5985/5986). It does not require any agent installation on managed servers, only WinRM to be enabled, which is the default on domain-joined Windows Server systems.

---

### [SEGMENT 7 — Licensing and Activation Models]

**[SHOW SCREEN: Diagram comparing KMS and MAK activation flows]**

[Alt-text: Diagram showing two activation flows: KMS where servers contact an internal KMS host automatically, and MAK where each server contacts Microsoft activation servers individually using a fixed-pool key.]

Windows Server activation ensures that each deployed server is properly licensed. The exam tests two primary activation models.

**Key Management Service (KMS)** is the standard model for enterprise environments. You install a KMS host on your internal network — it requires a minimum of five servers before it begins activating them — and all domain-joined servers contact the KMS host automatically every 180 days to renew activation. KMS requires no manual intervention once configured, making it ideal for large deployments.

**Multiple Activation Key (MAK)** is a product key with a fixed number of activations. Each MAK activation contacts Microsoft's activation servers. Once the activation count is exhausted, the key cannot activate additional machines. MAK is appropriate for air-gapped networks, government facilities, or small deployments that never have network access to an internal KMS host.

**Azure Hybrid Benefit** is relevant when deploying Windows Server in Azure. If you have on-premises Software Assurance coverage, you can use your existing licenses in Azure virtual machines without paying additional VM licensing fees. The AZ-800 exam will test your awareness of this benefit in hybrid scenario questions.

---

### [SEGMENT 8 — Architecture Summary]

**[SHOW SCREEN: Architecture diagram showing edition selection, installation option, post-install config, and activation flow]**

Let us summarize the architectural decisions in this module as a decision flow.

First, choose an edition: Standard for low-virtualization environments, Datacenter for unlimited VMs and advanced storage features.

Second, choose an installation option: Desktop Experience for full GUI management, Server Core for minimum footprint and reduced attack surface.

Third, complete post-install configuration: hostname, static IP, DNS server address, domain or workgroup membership, and Windows Update policy.

Fourth, activate: KMS for enterprise domain-joined environments, MAK for isolated or small deployments.

Every subsequent module in this course assumes you have completed these four steps. Active Directory, DNS, DHCP, Group Policy — all of it is built on top of a properly installed, named, addressed, and activated Windows Server instance.

---

### [SEGMENT 9 — Certification Alignment Summary]

This segment's content maps to AZ-800 objective area: "Deploy and manage on-premises and hybrid infrastructure" and "Plan and implement an on-premises Active Directory Domain Services infrastructure." The AZ-800 expects you to know edition differences, installation options, and activation mechanics without needing to look them up.

In Part 2 of this module, we will walk through the hands-on demonstration — using sconfig on Server Core, setting a static IP with PowerShell, and previewing the lab activity you will complete this week.

---

### Additional Resources

- [Windows Server Get Started](https://learn.microsoft.com/en-us/windows-server/get-started/get-started-with-windows-server)
- [Windows Server 2022 editions comparison](https://learn.microsoft.com/en-us/windows-server/get-started/editions-comparison-windows-server-2022)
- [Windows Admin Center overview](https://learn.microsoft.com/en-us/windows-server/manage/windows-admin-center/overview)
- [AZ-800 exam objectives](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-800)

---

*End of Part 1. Continue to Part 2 for demonstrations, PowerShell commands, exam tips, and lab preview.*
