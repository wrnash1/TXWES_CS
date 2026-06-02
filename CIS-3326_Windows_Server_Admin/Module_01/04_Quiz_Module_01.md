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
