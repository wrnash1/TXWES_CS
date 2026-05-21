# Quiz: Module 05 - Group Policy Objects (GPOs) - Creation and Management

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

An administrator links a GPO at the Domain level that disables the Run dialog box. A second GPO linked to the `Executives` OU re-enables the Run dialog box. The Domain-level GPO has the "Enforced" flag set. What is the result for users in the `Executives` OU?

A) The Run dialog box is enabled, because OU-linked GPOs always override Domain-level GPOs.
B) The Run dialog box is disabled, because the Enforced flag on the Domain GPO prevents lower-level OUs from overriding it.
C) Neither GPO applies, because conflicting Enforced and OU-level settings cancel each other out.
D) The result depends on which GPO has the higher link order number in the GPMC.

* **Correct Answer:** B) The Run dialog box is disabled, because the Enforced flag on the Domain GPO prevents lower-level OUs from overriding it.
* **Distractor Analysis:**
  * *Why A is incorrect:* Under normal LSDOU processing, OU GPOs do win over Domain GPOs. However, the Enforced flag overrides the normal inheritance order and causes the Domain GPO to take precedence regardless of what lower-level OUs configure.
  * *Why C is incorrect:* Enforced and non-Enforced GPOs do not cancel each other. The Enforced GPO wins unconditionally — no cancellation occurs.
  * *Why D is incorrect:* Link order within the same OU container determines precedence among multiple GPOs linked at the same level. It does not override the Enforced flag set at a parent container.

---

### Question 2

You need to deploy a specific registry key via Group Policy only to computers running Windows 10, ignoring all Windows 11 machines in the same OU. What is the most efficient and dynamically maintained method?

A) Create two separate OUs, manually move computers into each based on OS version, and link the GPO to the Windows 10 OU.
B) Add all Windows 10 computers to a manually maintained security group and configure Security Filtering on the GPO.
C) Configure a WMI Filter on the GPO that queries the operating system version and returns TRUE only for Windows 10 machines.
D) Configure the GPO under User Configuration instead of Computer Configuration so it applies based on the logged-in user's OS.

* **Correct Answer:** C) Configure a WMI Filter on the GPO that queries the operating system version and returns TRUE only for Windows 10 machines.
* **Distractor Analysis:**
  * *Why A is incorrect:* Manually moving computers between OUs as they are upgraded is operationally burdensome and error-prone. WMI filters evaluate the condition dynamically at each policy refresh with no administrative maintenance.
  * *Why B is incorrect:* A manually maintained security group requires ongoing updates as machines are upgraded, introducing the same administrative overhead. WMI queries the hardware and OS properties directly without requiring group membership changes.
  * *Why D is incorrect:* User Configuration policies apply based on where the user object lives in AD, not what OS version the machine is running. This change in configuration node would not filter by OS version at all.

---

### Question 3

A domain user reports that a new wallpaper policy is not applying to their workstation, even though the GPO is linked to their OU. After running `gpresult /r`, the administrator sees the GPO listed under "Denied GPOs" with the reason "Inaccessible." What is the most likely cause?

A) The GPO link is disabled at the OU level, preventing the policy from flowing to users.
B) The user's account does not have Read and Apply Group Policy permissions on the GPO's Security Filtering ACL.
C) The GPO contains a WMI Filter that is returning FALSE on this workstation.
D) The Domain Controller holding the PDC Emulator FSMO role is offline, blocking all GPO processing.

* **Correct Answer:** B) The user's account does not have Read and Apply Group Policy permissions on the GPO's Security Filtering ACL.
* **Distractor Analysis:**
  * *Why A is incorrect:* A disabled GPO link shows in `gpresult` as "Disabled" not "Inaccessible." Inaccessible specifically means the client cannot read the GPO — a permissions problem on the security descriptor.
  * *Why C is incorrect:* A WMI Filter returning FALSE causes the GPO to show as "Denied" with the reason "Inaccessible WMI filter" — a subtly different status. The plain "Inaccessible" reason points to an ACL/permissions issue on the GPO object itself.
  * *Why D is incorrect:* The PDC Emulator going offline degrades password change processing and time sync but does not block individual GPO reads for clients that can still reach other DCs with a copy of SYSVOL.

---

### Question 4

An administrator needs to run `gpupdate /force` on 200 domain-joined workstations simultaneously without logging into each one. Which PowerShell cmdlet accomplishes this most efficiently?

A) `Invoke-GPUpdate -Computer (Get-ADComputer -Filter *) -Force`
B) `Set-GPLink -All -Force` applied to every OU in the domain.
C) `Restart-Computer -ComputerName (Get-ADComputer -Filter *)` to trigger a policy refresh during reboot.
D) `gpupdate /force` must be run interactively on each workstation; there is no remote bulk method.

* **Correct Answer:** A) `Invoke-GPUpdate -Computer (Get-ADComputer -Filter *) -Force`
* **Distractor Analysis:**
  * *Why B is incorrect:* `Set-GPLink` manages the link status (enabled/disabled/enforced) of GPO links in the GPMC — it does not trigger a policy refresh on client machines.
  * *Why C is incorrect:* Restarting all 200 computers simultaneously to trigger a policy refresh would cause significant service disruption. Computer restart does process Computer Configuration GPOs, but `Invoke-GPUpdate` achieves the same result without downtime.
  * *Why D is incorrect:* The `Invoke-GPUpdate` cmdlet was introduced in Windows Server 2012 R2 specifically to enable remote policy refresh. Running `gpupdate` manually on each machine is never the correct enterprise-scale answer.

---

### Question 5

An administrator wants to apply a User Configuration GPO setting to all users who log into computers in the `Kiosks` OU, regardless of which OU the user accounts are located in. Which Group Policy feature enables this?

A) Security Filtering set to "All Users" scoped to the `Kiosks` OU link.
B) Loopback Processing in Replace mode, configured under Computer Configuration of a GPO linked to the `Kiosks` OU.
C) Block Inheritance on the `Kiosks` OU to prevent user OU policies from applying when users log into those computers.
D) A WMI Filter on the GPO that identifies the Kiosk computers by their IP subnet.

* **Correct Answer:** B) Loopback Processing in Replace mode, configured under Computer Configuration of a GPO linked to the `Kiosks` OU.
* **Distractor Analysis:**
  * *Why A is incorrect:* Security Filtering controls which security principals receive the GPO but does not change which OU determines the User Configuration settings that are applied. It does not make user settings follow the computer's OU location.
  * *Why C is incorrect:* Block Inheritance prevents higher-level GPOs from flowing down to the OU, but it does not cause user settings to be applied based on the computer's OU. It would actually remove policies rather than redirect which user policies apply.
  * *Why D is incorrect:* WMI Filters determine whether a GPO applies to a given machine based on a hardware or OS query. They do not redirect which OU is used to look up User Configuration settings when a user logs in to a machine.
