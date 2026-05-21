# Quiz: Module 01 - Windows Server Installation and Editions

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

Which of the following is a primary advantage of installing Windows Server using the Server Core option instead of Desktop Experience?

A) It provides a larger selection of pre-installed graphical management tools.
B) It has a reduced attack surface and lower hardware footprint.
C) It allows for the installation of Microsoft Office applications directly on the server.
D) It forces the use of IPv6 for all network communications.

* **Correct Answer:** B) It has a reduced attack surface and lower hardware footprint.
* **Distractor Analysis:**
  * *Why A is incorrect:* Server Core removes almost all graphical tools; administrators must manage it remotely via Windows Admin Center, RSAT, or PowerShell remoting.
  * *Why C is incorrect:* Client productivity applications like Microsoft Office are not installed on servers, and Server Core lacks the GUI dependencies those applications require.
  * *Why D is incorrect:* Server Core supports both IPv4 and IPv6 identically to Desktop Experience; the installation type has no effect on network protocol selection.

---

### Question 2

You have just installed a new Windows Server Core machine. Which command-line utility provides a simple, text-based menu to configure the hostname, IP address, domain membership, and Windows Update settings?

A) `netsh`
B) `sysdm.cpl`
C) `sconfig`
D) `ServerManager.exe`

* **Correct Answer:** C) `sconfig`
* **Distractor Analysis:**
  * *Why A is incorrect:* `netsh` is a command-line scripting tool for configuring specific network components but does not provide an interactive numbered menu for comprehensive first-boot configuration tasks.
  * *Why B is incorrect:* `sysdm.cpl` opens the graphical System Properties dialog, which is unavailable on Server Core because the full graphical shell is not installed.
  * *Why D is incorrect:* `ServerManager.exe` launches the graphical Server Manager console, which is not present on Server Core installations.

---

### Question 3

A company is deploying 50 new Windows Server virtual machines in a data center. They need to activate all servers automatically without manually entering a product key on each machine, using an internal corporate activation server. Which activation method should they use?

A) Multiple Activation Key (MAK), because it works offline without any server infrastructure.
B) Key Management Service (KMS), because it activates domain-joined servers automatically by contacting an internal KMS host.
C) Retail activation, because it provides the most license flexibility per server.
D) Windows Activation Troubleshooter, because it auto-detects the correct key for each edition.

* **Correct Answer:** B) Key Management Service (KMS), because it activates domain-joined servers automatically by contacting an internal KMS host.
* **Distractor Analysis:**
  * *Why A is incorrect:* MAK provides a fixed pool of activations that contact Microsoft's servers directly and is designed for machines that cannot reach an internal KMS host, not for bulk automated activation in a data center.
  * *Why C is incorrect:* Retail licenses are intended for individual purchases and provide no automated or volume activation infrastructure.
  * *Why D is incorrect:* The Windows Activation Troubleshooter is a diagnostic tool for resolving individual activation failures, not an activation infrastructure for multiple servers.

---

### Question 4

An administrator needs to upgrade a Windows Server Standard installation to Datacenter edition to unlock unlimited virtual machine licensing. Which approach accomplishes this without requiring a full OS reinstall?

A) Run `DISM /online /Set-Edition:ServerDatacenter /ProductKey:<key> /AcceptEula` from an elevated command prompt.
B) Use Programs and Features in Control Panel to upgrade the edition in place.
C) Boot from the Datacenter installation media and choose "Upgrade" to preserve installed roles and data.
D) Change the product edition in the Server Manager Local Server properties panel.

* **Correct Answer:** A) Run `DISM /online /Set-Edition:ServerDatacenter /ProductKey:<key> /AcceptEula` from an elevated command prompt.
* **Distractor Analysis:**
  * *Why B is incorrect:* Programs and Features does not expose a Windows Server edition upgrade option; edition changes are not managed through Control Panel.
  * *Why C is incorrect:* Booting from installation media runs a full Setup-based upgrade, which is more disruptive than the online DISM edition conversion and risks application compatibility issues.
  * *Why D is incorrect:* Server Manager Local Server properties does not include a control for changing the installed edition; DISM is the supported in-place conversion method.

---

### Question 5

A security-conscious organization wants to deploy a Windows Server that will run only as a DNS server in a branch office. They want to minimize installed components and reduce the attack surface. Which installation option best meets these requirements?

A) Desktop Experience, because it includes all GUI tools needed to troubleshoot DNS locally without a remote connection.
B) Server Core, because it omits the graphical shell, reduces installed components requiring patching, and lowers the attack surface.
C) Nano Server, because it is the smallest possible Windows Server footprint and supports all traditional server roles.
D) Hyper-V Server free edition, because it reduces licensing cost and supports the DNS role natively as a host service.

* **Correct Answer:** B) Server Core, because it omits the graphical shell, reduces installed components requiring patching, and lowers the attack surface.
* **Distractor Analysis:**
  * *Why A is incorrect:* Desktop Experience installs additional graphical components and shell services that increase the patching surface without providing any functional benefit for a dedicated single-role DNS server.
  * *Why C is incorrect:* Nano Server is an extremely minimal container/cloud-optimized image that does not support traditional server roles such as DNS Server; it is not appropriate for branch office role deployments.
  * *Why D is incorrect:* Hyper-V Server free edition is a bare hypervisor — it cannot host the DNS Server role as a native Windows service; all workloads must run inside virtual machines.
