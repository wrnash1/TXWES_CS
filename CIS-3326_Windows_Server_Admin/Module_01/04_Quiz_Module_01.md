# Quiz: Module 01 - Windows Server Installation and Editions

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

Which of the following is a primary advantage of installing Windows Server using the Server Core option instead of Desktop Experience?

A) It provides a larger selection of pre-installed graphical management tools.

B) It has a reduced attack surface and lower hardware footprint.

C) It allows for the installation of Microsoft Office applications directly on the server.

D) It forces the use of IPv6 for all network communications.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Server Core removes almost all graphical tools. Administrators must manage it remotely via Windows Admin Center, RSAT, or PowerShell remoting.
  - Why C is incorrect: Client productivity applications like Microsoft Office are not installed on servers, and Server Core lacks the GUI shell those applications require.
  - Why D is incorrect: Server Core supports both IPv4 and IPv6 identically to Desktop Experience. The installation option has no effect on network protocol selection.

---

### Question 2

You have just installed a new Windows Server Core machine. Which command-line utility provides a simple, text-based menu to configure the hostname, IP address, domain membership, and Windows Update settings?

A) `netsh`

B) `sysdm.cpl`

C) `sconfig`

D) `ServerManager.exe`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `netsh` is a scripting tool for specific network components but does not provide a numbered interactive menu for comprehensive first-boot tasks.
  - Why B is incorrect: `sysdm.cpl` opens the graphical System Properties dialog, which is unavailable on Server Core because the full graphical shell is not installed.
  - Why D is incorrect: `ServerManager.exe` launches the graphical Server Manager console, which is not present on Server Core installations.

---

### Question 3

A company is deploying 50 new Windows Server virtual machines in a data center. They need to activate all servers automatically without manually entering a product key on each machine, using an internal corporate activation server. Which activation method should they use?

A) Multiple Activation Key (MAK), because it works offline without any server infrastructure.

B) Key Management Service (KMS), because it activates domain-joined servers automatically by contacting an internal KMS host.

C) Retail activation, because it provides the most license flexibility per server.

D) Windows Activation Troubleshooter, because it auto-detects the correct key for each edition.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: MAK provides a fixed activation pool that contacts Microsoft's servers directly. It is designed for machines that cannot reach an internal KMS host, not for bulk automated activation.
  - Why C is incorrect: Retail licenses are intended for individual purchases and provide no automated activation infrastructure.
  - Why D is incorrect: The Windows Activation Troubleshooter is a diagnostic tool for resolving individual activation failures, not an activation infrastructure for multiple servers.

---

### Question 4

An administrator needs to upgrade a Windows Server Standard installation to Datacenter edition to unlock unlimited virtual machine licensing. Which approach accomplishes this without requiring a full OS reinstall?

A) Run `DISM /online /Set-Edition:ServerDatacenter /ProductKey:<key> /AcceptEula` from an elevated command prompt.

B) Use Programs and Features in Control Panel to upgrade the edition in place.

C) Boot from the Datacenter installation media and choose Upgrade to preserve installed roles and data.

D) Change the product edition in the Server Manager Local Server properties panel.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Programs and Features does not expose a Windows Server edition upgrade option.
  - Why C is incorrect: Booting from installation media runs a full Setup-based upgrade, which is more disruptive than the online DISM conversion and risks application compatibility issues.
  - Why D is incorrect: Server Manager Local Server properties does not include an edition change control. DISM is the supported in-place method.

---

### Question 5

A security-conscious organization wants to deploy a Windows Server that will run only as a DNS server in a branch office. They want to minimize installed components and reduce the attack surface. Which installation option best meets these requirements?

A) Desktop Experience, because it includes all GUI tools needed to troubleshoot DNS locally.

B) Server Core, because it omits the graphical shell, reduces installed components requiring patching, and lowers the attack surface.

C) Nano Server, because it is the smallest possible Windows Server footprint and supports all traditional server roles.

D) Hyper-V Server free edition, because it reduces licensing cost and supports the DNS role natively.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Desktop Experience installs additional graphical components that increase the patching surface without any functional benefit for a dedicated DNS server.
  - Why C is incorrect: Nano Server does not support traditional server roles such as DNS Server. It is a container base image only.
  - Why D is incorrect: Hyper-V Server free edition is a bare hypervisor. It cannot host the DNS Server role as a native Windows service.

---

### Question 6

An administrator is configuring a Server Core installation and needs to set a static IP address using PowerShell. Which cmdlet creates a new static IP address assignment on a named network adapter?

A) `Set-NetIPAddress`

B) `New-NetIPAddress`

C) `Add-NetIPAddress`

D) `Configure-NetAdapter`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Set-NetIPAddress` modifies an existing IP address assignment but cannot create one from scratch on an unconfigured adapter.
  - Why C is incorrect: `Add-NetIPAddress` is not a valid PowerShell cmdlet in the NetTCPIP module.
  - Why D is incorrect: `Configure-NetAdapter` is not a valid PowerShell cmdlet. Adapter configuration uses cmdlets from the NetTCPIP and NetAdapter modules.

---

### Question 7

Your organization has 12 Windows Server virtual machines running on a single Hyper-V host. Which Windows Server edition for the host minimizes total licensing cost while covering all 12 VMs?

A) Standard edition with 6 licenses (2 VMs per license × 6 = 12 VMs)

B) Datacenter edition with 1 license (covers unlimited VMs on one host)

C) Essentials edition with 1 license (supports up to 25 users)

D) Standard edition with 1 license (covers all VMs without limit)

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While technically valid, purchasing 6 Standard licenses typically costs more than one Datacenter license at enterprise pricing when running 10 or more VMs per host.
  - Why C is incorrect: Essentials edition cannot function as a Hyper-V host and does not support large VM deployments.
  - Why D is incorrect: Standard edition licenses only 2 VMs per physical license. Hosting 12 VMs requires 6 Standard licenses, not 1.

---

### Question 8

What is the minimum number of client computers or servers that must request activation from a Key Management Service (KMS) host before the host begins issuing activations for Windows Server?

A) 1

B) 5

C) 10

D) 25

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A single server cannot trigger KMS activation. The KMS host requires a threshold of requests before it activates any clients.
  - Why C is incorrect: 10 is the threshold for KMS to activate Windows client operating systems, not Windows Server.
  - Why D is incorrect: 25 is the threshold required for KMS to activate Windows client operating systems, not Windows Server. Windows Server requires 5.

---

### Question 9

An administrator needs to manage a remote Windows Server Core machine from a browser-based interface without installing any agent on the remote server. Which tool provides this capability?

A) Remote Desktop Services Manager

B) Windows Admin Center

C) Microsoft Management Console (MMC)

D) System Center Configuration Manager

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Remote Desktop Services Manager manages RDS session collections and is not a general-purpose server management console.
  - Why C is incorrect: MMC snap-ins require the graphical shell on the target or remote RSAT installation. MMC is not browser-based.
  - Why D is incorrect: System Center Configuration Manager (now Microsoft Endpoint Configuration Manager) is an enterprise management platform that requires an agent installed on managed machines.

---

### Question 10

A Windows Server administrator uses PowerShell to rename a server and immediately restarts it. Which cmdlet and parameter combination accomplishes both tasks in a single command?

A) `Set-ComputerName -Name "SRV-01" -Restart`

B) `Rename-Computer -NewName "SRV-01" -Restart`

C) `Set-Hostname "SRV-01" -ForceRestart`

D) `netdom renamecomputer localhost /newname:SRV-01 /restart`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Set-ComputerName` is not a valid PowerShell cmdlet. The correct cmdlet is `Rename-Computer`.
  - Why C is incorrect: `Set-Hostname` is not a valid PowerShell cmdlet for Windows Server. This syntax does not exist in the Windows PowerShell environment.
  - Why D is incorrect: While `netdom renamecomputer` works, it is a legacy command-line tool. The PowerShell equivalent `Rename-Computer -Restart` is the current best-practice method tested on AZ-800.

---

### Question 11 (5 points)

Which Windows Server edition includes the Host Guardian Service and Shielded Virtual Machines features that protect tenant VMs from compromised fabric administrators?

- A) Standard edition with Software Assurance
- B) Essentials edition with the Hyper-V role enabled
- C) Datacenter edition
- D) Standard edition with the RSAT tools installed

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Software Assurance is a licensing benefit that provides upgrade rights and other perks, but it does not unlock Shielded VMs or Host Guardian Service on Standard edition. These remain Datacenter-exclusive features.
  - Why B is incorrect: Essentials edition does not support Hyper-V hosting at scale and does not include Host Guardian Service. Essentials is designed for small business single-server deployments.
  - Why D is incorrect: RSAT provides remote administration tools but does not unlock server features. Edition determines which roles and features are available, not the management tools installed.

---

### Question 12 (5 points)

An administrator wants to verify that Windows Server activation succeeded on a Server Core machine. Which command displays the current activation status?

- A) `slmgr /dli`
- B) `wscript /status`
- C) `netsh activation query`
- D) `Get-WindowsLicense`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `wscript /status` is not a valid activation query command. `wscript` is a Windows Script Host launcher, not a licensing tool.
  - Why C is incorrect: `netsh activation query` is not a valid netsh context. Netsh does not have an activation module.
  - Why D is incorrect: `Get-WindowsLicense` is not a valid PowerShell cmdlet in standard Windows Server installations. License status is queried with `slmgr` or the `Get-CimInstance SoftwareLicensingProduct` cmdlet.

---

### Question 13 (5 points)

A junior administrator accidentally set a static IP address on the wrong network adapter of a Server Core machine. Which PowerShell cmdlet removes the incorrect IP address assignment without requiring a reboot?

- A) `Delete-NetIPAddress`
- B) `Remove-NetIPAddress`
- C) `Clear-NetIPAddress`
- D) `Reset-NetAdapter`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Delete-NetIPAddress` is not a valid PowerShell cmdlet in the NetTCPIP module. The verb for removing IP configurations is `Remove`.
  - Why C is incorrect: `Clear-NetIPAddress` is not a valid cmdlet. The correct cmdlet is `Remove-NetIPAddress`.
  - Why D is incorrect: `Reset-NetAdapter` resets the adapter to a default state but is more disruptive than needed. `Remove-NetIPAddress` selectively removes the specific address configuration.

---

### Question 14 (5 points)

Which DNS SRV record must be resolvable on the internal network for Windows Server machines to automatically locate the KMS host during activation?

- A) `_kms._tcp`
- B) `_vlmcs._tcp`
- C) `_activation._udp`
- D) `_spooler._tcp`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `_kms._tcp` is not the correct SRV record name used by the Volume Activation client service. The correct record name is `_vlmcs._tcp`.
  - Why C is incorrect: `_activation._udp` is not a real DNS SRV record. Windows activation uses TCP, not UDP, and the record name is `_vlmcs._tcp`.
  - Why D is incorrect: `_spooler._tcp` is unrelated to activation; it is not even a standard Windows DNS record. This option tests recognition of the correct KMS discovery mechanism.

---

### Question 15 (5 points)

An organization needs to deploy Windows Server to 200 remote branch offices that have no network connectivity to the corporate data center. Activation must work at each site independently. Which activation method is most appropriate?

- A) KMS, because it requires no internal server infrastructure at each branch
- B) MAK, because each server can activate independently by contacting Microsoft's activation servers
- C) Azure AD join, because it provides cloud-based activation without on-premises infrastructure
- D) KMS proxy, because it routes activation requests through the corporate WAN

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: KMS requires an internal KMS host reachable on the network and a minimum activation threshold of 5 servers. Branch offices with no corporate connectivity cannot use a centralized KMS host.
  - Why C is incorrect: Azure AD join is an identity and management feature, not a Windows Server volume activation method. It does not replace KMS or MAK for Windows Server license activation.
  - Why D is incorrect: A KMS proxy requires WAN connectivity to the central KMS host, which the question explicitly states is unavailable at these branches.

---

### Question 16 (5 points)

After installing Windows Server 2022, an administrator runs `Get-WindowsFeature` and notices hundreds of features listed as "Available" rather than "Installed." What does the "Available" state indicate?

- A) The features have been downloaded and are ready to install without any additional media
- B) The features are listed in the manifest but their binaries have not yet been installed; installation requires the source media or Windows Update
- C) The features require a Datacenter edition license to install
- D) The features are installed but disabled pending a reboot

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: "Available" does not mean the binaries are present on the local disk. It means the feature is known to the system but requires source media or online access to obtain the binaries.
  - Why C is incorrect: Most features listed as Available are edition-neutral and do not require Datacenter. Edition restrictions apply to specific features like S2D and Shielded VMs, but "Available" simply reflects installation state.
  - Why D is incorrect: Features that are installed but pending a reboot show as "Installed" with a restart indicator, not as "Available." "Available" means the binaries are not on the system.

---

### Question 17 (5 points)

Which PowerShell cmdlet retrieves detailed hardware and OS information including the computer name, installed RAM, number of processors, and Windows edition from the local machine?

- A) `Get-SystemInfo`
- B) `Get-WmiObject Win32_OperatingSystem`
- C) `Get-ComputerInfo`
- D) `systeminfo /fo list`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `Get-SystemInfo` is not a valid PowerShell cmdlet. The correct cmdlet that aggregates comprehensive system information in PowerShell is `Get-ComputerInfo`.
  - Why B is incorrect: `Get-WmiObject Win32_OperatingSystem` returns OS-specific information but not the comprehensive hardware and configuration detail that `Get-ComputerInfo` provides in a single object.
  - Why D is incorrect: `systeminfo /fo list` is a valid command-line tool but it is not a PowerShell cmdlet and does not return structured PowerShell objects that can be piped or filtered.

---

### Question 18 (5 points)

Windows Admin Center is installed on a gateway server. An administrator attempts to manage a remote Server Core machine but cannot connect. The firewall on the remote server is enabled. Which firewall rule group must be enabled on the remote Server Core machine to allow Windows Admin Center management?

- A) File and Printer Sharing
- B) Windows Remote Management
- C) Remote Event Log Management
- D) Network Discovery

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: File and Printer Sharing allows SMB and network printing access but is not the protocol used by Windows Admin Center for management connectivity. WAC uses WinRM.
  - Why C is incorrect: Remote Event Log Management enables reading event logs remotely but is not required for general Windows Admin Center connectivity. WAC uses WinRM as its transport.
  - Why D is incorrect: Network Discovery enables the computer to see and be seen on the network but is a discovery protocol (SSDP/WSD), not the management transport. WinRM must be allowed for WAC to manage the remote node.

---

### Question 19 (5 points)

An administrator needs to convert a Windows Server 2022 Standard evaluation installation to a licensed Standard edition. Which tool and action accomplishes this conversion?

- A) Run `slmgr /ipk <Standard product key>` to install the retail product key over the evaluation key
- B) Run `DISM /online /Set-Edition:ServerStandard` with no product key to convert in place
- C) Use Server Manager to switch the license mode under Local Server properties
- D) Reinstall from ISO, selecting the non-evaluation edition during setup

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: DISM `/Set-Edition` requires a valid product key and is used to upgrade editions (e.g., Standard to Datacenter). Converting an evaluation to a licensed copy of the same edition uses `slmgr /ipk` with the appropriate product key.
  - Why C is incorrect: Server Manager does not expose a license mode switch. License conversion is performed via command-line tools (`slmgr`) or DISM.
  - Why D is incorrect: Reinstalling from ISO would require reconfiguring the entire server from scratch. The supported in-place conversion for evaluation-to-licensed uses `slmgr /ipk`, which avoids reinstallation.

---

### Question 20 (5 points)

An administrator runs `Enable-PSRemoting -Force` on a Server Core machine. Which underlying Windows service must be running for PowerShell remoting to function?

- A) Remote Procedure Call (RPC)
- B) Windows Remote Management (WinRM)
- C) Remote Registry
- D) Secondary Logon

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: RPC is a foundational communication protocol used by many Windows services, but PowerShell remoting specifically depends on WinRM, not raw RPC. `Enable-PSRemoting` starts and configures the WinRM service.
  - Why C is incorrect: Remote Registry enables remote access to the registry via the registry editor. It is independent of PowerShell remoting and uses a different transport.
  - Why D is incorrect: Secondary Logon (RunAs) allows starting processes under different credentials locally. It is not involved in PowerShell remoting connectivity.
