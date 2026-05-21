# Quiz: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

An administrator configures a Group Policy Object (GPO) at the Domain level that sets the minimum password length to 12 characters. A separate GPO linked to the `IT_Department` OU sets the minimum password length to 15 characters. Assuming no Enforced flags are set, what minimum password length applies to users in the `IT_Department` OU?

A) 12 characters, because Domain-level policies always override OU-level policies.
B) 15 characters, because the OU-linked GPO is processed last and its settings override the Domain GPO.
C) 15 characters, because Group Policy always enforces the most restrictive setting across all linked GPOs.
D) Neither policy applies; conflicting GPOs at different levels cancel each other out.

* **Correct Answer:** B) 15 characters, because the OU-linked GPO is processed last and its settings override the Domain GPO.
* **Distractor Analysis:**
  * *Why A is incorrect:* GPOs follow the LSDOU processing order (Local, Site, Domain, OU). OU-linked policies are processed after Domain policies, so the OU setting wins when there is a conflict and no Enforced flag is set.
  * *Why C is incorrect:* Group Policy does not evaluate restrictiveness; it applies the last-processed value. The OU GPO wins simply because it is applied last, not because 15 is greater than 12.
  * *Why D is incorrect:* Conflicting GPO settings do not cancel each other; the last-applied value for each individual setting takes effect according to the LSDOU order.

---

### Question 2

You need to deploy a registry key via Group Policy only to computers running Windows 10, ignoring all Windows 11 machines in the same OU. What is the most efficient and dynamic method to accomplish this?

A) Create two separate OUs, move computers manually into each based on OS version, and link the GPO to the Windows 10 OU.
B) Configure Security Filtering on the GPO to include only a manually maintained "Windows 10 Computers" security group.
C) Configure a WMI Filter on the GPO that queries the operating system version property and returns TRUE only for Windows 10.
D) Change the GPO settings from Computer Configuration to User Configuration so they apply based on user login rather than machine OS.

* **Correct Answer:** C) Configure a WMI Filter on the GPO that queries the operating system version property and returns TRUE only for Windows 10.
* **Distractor Analysis:**
  * *Why A is incorrect:* Manually moving computers between OUs as they are upgraded is operationally burdensome and error-prone. WMI filters dynamically evaluate conditions at policy refresh without any manual object movement.
  * *Why B is incorrect:* A manually maintained security group requires the administrator to track and update group membership every time a computer is upgraded from Windows 10 to Windows 11, creating ongoing administrative overhead. WMI filters query the OS version directly and dynamically.
  * *Why D is incorrect:* Moving the registry key setting to User Configuration changes when and how the policy applies — it would apply based on who logs in, not which OS the machine is running, making it ineffective for OS-targeted deployments.

---

### Question 3

A technician is deploying a new Domain Controller in a branch office location that has poor physical security. The organization wants to allow local caching of branch office user credentials but must ensure that Domain Admin account credentials can never be cached on this DC. Which DC type and configuration satisfies these requirements?

A) A standard writable DC with the "Do not allow storage of credentials or .NET Passports" security policy enabled.
B) A Read-Only Domain Controller (RODC) with Domain Admin accounts explicitly listed in the Denied List of the Password Replication Policy.
C) A standard writable DC with BitLocker enabled on all volumes to prevent credential extraction if stolen.
D) A Read-Only Domain Controller (RODC) with the Password Replication Policy set to allow all accounts by default.

* **Correct Answer:** B) A Read-Only Domain Controller (RODC) with Domain Admin accounts explicitly listed in the Denied List of the Password Replication Policy.
* **Distractor Analysis:**
  * *Why A is incorrect:* A standard writable DC holds a full read/write copy of the AD database, including all password hashes. If stolen, an attacker could potentially extract all domain credentials regardless of the local security policy setting.
  * *Why C is incorrect:* BitLocker protects the drive from offline attacks on the physical disk but does not prevent a running RODC from caching and potentially exposing credentials of privileged accounts if the Password Replication Policy is misconfigured.
  * *Why D is incorrect:* Setting the PRP to allow all accounts would permit Domain Admin credentials to be cached on the RODC — exactly the risk the organization is trying to prevent. The Denied List must explicitly block sensitive accounts.

---

### Question 4

After promoting a new Domain Controller, an administrator runs `dcdiag` and receives a failure on the `Replications` test. Which of the following is the most likely root cause and first diagnostic step?

A) The Domain Controller's IP address is incorrect; run `ipconfig /renew` to obtain a new address from DHCP.
B) DNS resolution is failing or the DC cannot locate replication partners; verify DNS records using `nslookup` and check replication topology with `repadmin /showrepl`.
C) The SYSVOL share is not published; run `net share` and re-create the SYSVOL share manually using Server Manager.
D) The Domain Functional Level is too low; raise it immediately to Windows Server 2019 to resolve all replication errors.

* **Correct Answer:** B) DNS resolution is failing or the DC cannot locate replication partners; verify DNS records using `nslookup` and check replication topology with `repadmin /showrepl`.
* **Distractor Analysis:**
  * *Why A is incorrect:* Domain Controllers should have static IP addresses; obtaining a DHCP address is not appropriate for a DC. A DHCP address would also invalidate the DC's DNS SRV registrations.
  * *Why C is incorrect:* SYSVOL is published automatically by the DFS Replication service once AD DS replication is healthy; manually re-creating the share does not fix an underlying replication topology or DNS failure.
  * *Why D is incorrect:* Raising the Domain Functional Level does not resolve replication errors caused by DNS failures or network connectivity issues, and doing so irreversibly while errors are present is dangerous.

---

### Question 5

An organization is deploying a new child domain named `asia.corp.local` in an existing `corp.local` forest. A junior administrator is told to "install AD DS on the new server." They install the AD DS role but the server still does not appear as a Domain Controller. What step did they miss?

A) They need to install the DNS Server role separately, as AD DS does not include DNS functionality.
B) They need to run the AD DS Configuration Wizard or `Install-ADDSDomain` PowerShell cmdlet to promote the server to a Domain Controller.
C) They need to reboot the server twice after role installation before the Domain Controller functionality activates automatically.
D) They need to run `dcpromo.exe` to complete the promotion, as it is required for all child domain deployments.

* **Correct Answer:** B) They need to run the AD DS Configuration Wizard or `Install-ADDSDomain` PowerShell cmdlet to promote the server to a Domain Controller.
* **Distractor Analysis:**
  * *Why A is incorrect:* The DNS Server role can be installed automatically during AD DS promotion via the wizard; it does not need to be pre-installed separately, and its absence is not why the server is not yet a DC.
  * *Why C is incorrect:* AD DS promotion is not automatic after role installation. Installing the role only copies binaries — a separate, explicit promotion step is always required regardless of how many times the server is rebooted.
  * *Why D is incorrect:* `dcpromo.exe` was the legacy promotion tool removed in Windows Server 2012. It is not available in current versions of Windows Server and running it would fail. The current tools are the Server Manager wizard and PowerShell cmdlets.
