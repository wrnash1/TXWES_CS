# Quiz: Module 05 - Group Policy Objects: Creation and Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

An administrator links a GPO at the Domain level that disables the Run dialog box. A second GPO linked to the Executives OU re-enables it. The Domain-level GPO has the Enforced flag set. What is the result for users in the Executives OU?

A) The Run dialog box is enabled, because OU-linked GPOs always override Domain-level GPOs.

B) The Run dialog box is disabled, because the Enforced flag prevents lower-level OUs from overriding the Domain GPO.

C) Neither GPO applies, because conflicting Enforced and OU-level settings cancel each other.

D) The result depends on which GPO has the higher link order number in GPMC.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Under normal LSDOU processing, OU GPOs do win. However, the Enforced flag overrides the normal order and causes the Domain GPO to take precedence regardless of OU settings.
  - Why C is incorrect: Enforced and non-Enforced GPOs do not cancel each other. The Enforced GPO wins unconditionally.
  - Why D is incorrect: Link order determines precedence among GPOs at the same level. It does not override the Enforced flag set at a parent container.

---

### Question 2

You need to deploy a registry key via Group Policy only to computers running Windows 10, ignoring Windows 11 machines in the same OU. What is the most efficient and dynamically maintained method?

A) Create two separate OUs, manually move computers into each based on OS version, and link the GPO to the Windows 10 OU.

B) Configure Security Filtering on the GPO to include only a manually maintained Windows 10 Computers security group.

C) Configure a WMI Filter on the GPO that queries the OS version and returns TRUE only for Windows 10 machines.

D) Configure the GPO under User Configuration instead of Computer Configuration so it applies based on the logged-in user's OS.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Manually moving computers between OUs as they are upgraded is burdensome and error-prone. WMI filters evaluate dynamically at each refresh without any AD changes.
  - Why B is incorrect: A manually maintained security group requires updates every time a computer is upgraded. WMI queries the hardware and OS properties directly, requiring no ongoing maintenance.
  - Why D is incorrect: User Configuration policies apply based on where the user object lives in AD, not the OS version of the machine. This would not filter by OS version.

---

### Question 3

After running `gpresult /r`, an administrator sees a GPO listed under Denied GPOs with the reason "Inaccessible." What is the most likely cause?

A) The GPO link is disabled at the OU level.

B) The user's account does not have Read and Apply Group Policy permissions on the GPO's Security Filtering ACL.

C) The GPO contains a WMI Filter returning FALSE on this workstation.

D) The Domain Controller holding the PDC Emulator FSMO role is offline.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A disabled GPO link shows as "Disabled" in gpresult, not "Inaccessible." Inaccessible means the client cannot read the GPO — a permissions or SYSVOL issue.
  - Why C is incorrect: A WMI Filter returning FALSE shows as "Inaccessible WMI filter," a different reason code. Plain "Inaccessible" specifically indicates an ACL permission issue.
  - Why D is incorrect: PDC Emulator offline affects password changes and time sync. Clients that can still reach other DCs with SYSVOL copies can continue to process GPOs.

---

### Question 4

An administrator needs to run `gpupdate /force` on 200 domain-joined workstations simultaneously without logging into each one. Which PowerShell cmdlet accomplishes this most efficiently?

A) `Invoke-GPUpdate -Computer (Get-ADComputer -Filter *) -Force`

B) `Set-GPLink -All -Force` applied to every OU in the domain.

C) `Restart-Computer -ComputerName (Get-ADComputer -Filter *)` to trigger a policy refresh.

D) `gpupdate /force` must be run interactively on each workstation — there is no remote bulk method.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `Set-GPLink` manages link status (enabled/disabled/enforced) and does not trigger a client-side policy refresh.
  - Why C is incorrect: Restarting 200 computers simultaneously would cause significant service disruption. `Invoke-GPUpdate` refreshes policies without requiring a reboot.
  - Why D is incorrect: `Invoke-GPUpdate` was introduced specifically for remote policy refresh. Manual per-machine execution is never the correct enterprise-scale answer.

---

### Question 5

An administrator wants to apply a User Configuration GPO setting to all users who log into computers in the Kiosks OU, regardless of which OU the user accounts live in. Which feature enables this?

A) Security Filtering set to All Users scoped to the Kiosks OU link.

B) Loopback Processing in Replace mode, configured under Computer Configuration in a GPO linked to the Kiosks OU.

C) Block Inheritance on the Kiosks OU to prevent user OU policies from flowing in.

D) A WMI Filter that identifies kiosk computers by their IP subnet.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Security Filtering controls which principals receive the GPO but does not redirect which OU determines the User Configuration settings that apply.
  - Why C is incorrect: Block Inheritance prevents higher-level GPOs from flowing in but does not redirect user settings based on the computer's OU location. It would remove policies rather than apply computer-OU user policies.
  - Why D is incorrect: WMI Filters determine whether a GPO applies based on machine properties. They do not redirect which OU is used to look up User Configuration settings at logon.

---

### Question 6

A GPO linked to the Domain level sets "Interactive logon: Do not display last user name" to Enabled. A GPO linked to the Sales OU sets the same setting to Disabled. Block Inheritance is NOT set on the Sales OU. What is the result for computers in the Sales OU?

A) The Domain GPO applies because it was linked first.

B) The Sales OU GPO applies because it is processed last in the LSDOU order.

C) Both settings apply simultaneously, causing undefined behavior.

D) Neither setting applies because they conflict at different LSDOU levels.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The domain GPO is processed before the OU GPO in LSDOU order. The last-applied setting wins — that is the OU setting.
  - Why C is incorrect: For any individual setting, only one value can be active. The last-applied wins; there is no simultaneous conflict.
  - Why D is incorrect: Conflicting settings at different levels do not cancel each other. The LSDOU last-applied rule determines the winner.

---

### Question 7

Which component of a GPO is stored in SYSVOL and contains the actual policy setting files and scripts?

A) Group Policy Container (GPC)

B) Group Policy Template (GPT)

C) Group Policy Security Descriptor (GPSD)

D) Group Policy Object Link (GPOL)

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Group Policy Container is the AD portion of a GPO. It stores metadata, the GPO GUID, and version numbers — not the actual setting files.
  - Why C is incorrect: GPSD is not a GPO component term. Security descriptors are part of AD objects but are not a named GPO subcomponent.
  - Why D is incorrect: A GPO Link is the association between a GPO and a container (site, domain, OU). It is not a storage component of the GPO itself.

---

### Question 8

An administrator has multiple GPOs linked to the same OU with link order values of 1, 2, and 3. GPO with link order 1 and GPO with link order 3 both configure the same screensaver timeout setting. Which value applies?

A) Link order 3 applies, because higher numbers have higher precedence.

B) Link order 1 applies, because lower link order numbers are applied last and have the highest precedence.

C) Both apply simultaneously and the average of the two values is used.

D) Link order 2 applies, because the middle value always breaks ties.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Higher link order numbers are processed first, not last. Lower numbers are processed last and therefore win.
  - Why C is incorrect: Group Policy applies a single value — the last-applied wins. There is no averaging mechanism.
  - Why D is incorrect: The middle link order value has no special precedence role. Precedence is strictly determined by link order number — lower = higher precedence.

---

### Question 9

After removing "Authenticated Users" from a GPO's Security Filtering and adding only the `G_Executives` group, Computer Configuration settings stop applying to computers in the affected OU. What is the most likely cause?

A) Computer Configuration settings require the Enforced flag to be set when Security Filtering is modified.

B) The computer account objects no longer have Read permission to access the GPO, preventing Computer Configuration processing.

C) Computer Configuration settings only apply when User Configuration settings are also enabled in the same GPO.

D) The GPO must be re-linked to the OU after Security Filtering changes take effect.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Enforced flag controls inheritance override, not permission access for Computer Configuration processing.
  - Why C is incorrect: Computer Configuration and User Configuration sections are independent. Each can have settings without the other.
  - Why D is incorrect: Security Filtering changes take effect without relinking. The cause is that computer accounts lost their Read access when Authenticated Users was removed.

---

### Question 10

Which PowerShell command generates a full RSoP (Resultant Set of Policy) report for a specific user and computer combination in HTML format?

A) `gpresult /h C:\RSoP.html /user CORP\jdoe /scope:computer`

B) `Get-GPResultantSetOfPolicy -Computer "WS-IT-001" -User "CORP\jdoe" -ReportType HTML -Path "C:\RSoP.html"`

C) `New-GPRSoPReport -User "CORP\jdoe" -Computer "WS-IT-001" -OutputPath "C:\RSoP.html"`

D) `Get-GPOReport -All -ReportType HTML -Path "C:\RSoP.html" -User "CORP\jdoe"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While `gpresult /h` generates an HTML report, the `/scope:computer` parameter is not valid syntax. The `gpresult` command does accept `/user` but has different scoping flags.
  - Why C is incorrect: `New-GPRSoPReport` is not a valid PowerShell cmdlet. The correct cmdlet is `Get-GPResultantSetOfPolicy`.
  - Why D is incorrect: `Get-GPOReport` reports on a single GPO's configuration, not the resultant policy for a user/computer combination.

---

### Question 11 (5 points)

An administrator creates a GPO that maps a network drive for all users in the Finance OU. After testing, they realize the drive mapping also appears for the administrator account when logged into Finance computers. What is the most targeted way to prevent the drive mapping from applying to administrator accounts while leaving it in place for standard Finance users?

- A) Move the administrator accounts into a separate OU that blocks the Finance GPO from applying
- B) Add the administrator group to the GPO's Delegation tab with a Deny "Apply Group Policy" permission
- C) Set the GPO link to Enforced so it cannot be overridden
- D) Change the drive mapping from User Configuration to Computer Configuration

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Moving admin accounts to a different OU is disruptive and may affect other GPOs. The Delegation deny ACE achieves the same result without any OU restructuring.
  - Why C is incorrect: Setting Enforced makes the GPO apply more broadly, not less. It would guarantee the drive mapping applies to administrators as well.
  - Why D is incorrect: Moving a drive mapping to Computer Configuration would make it apply to all users logging into Finance computers regardless of account type — the opposite of the desired result.

---

### Question 12 (5 points)

A technician runs `gpupdate /force` on a workstation but reports that a screen saver policy is still not applying. The GPO is linked to the correct OU. What should the administrator check first?

- A) Whether the GPO link is Enforced at the domain level
- B) Whether the screen saver setting is in User Configuration (requires user logoff/logon) or Computer Configuration (applies at startup/gpupdate)
- C) Whether Block Inheritance is set on the forest root
- D) Whether SYSVOL has been deleted and needs to be rebuilt

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Enforced status determines inheritance precedence, not whether a setting requires logoff to take effect. Even Enforced settings require the appropriate refresh cycle.
  - Why C is incorrect: Block Inheritance is set on OUs and sites, not on the forest root. If a policy was never applying at all, Block Inheritance might be relevant, but the question states `gpupdate /force` ran without resolving the issue.
  - Why D is incorrect: If SYSVOL were deleted, no GPOs would apply to any user or computer, not just this one. A specific policy failing is more likely a User Configuration refresh issue.

---

### Question 13 (5 points)

An administrator runs `Get-GPInheritance -Target "OU=IT,OU=Departments,DC=corp,DC=local"` and observes a GPO with `Enforced: True` in the output that was linked at the domain level. What does this mean for the IT OU?

- A) The Enforced GPO was disabled for the IT OU specifically
- B) The Enforced domain-level GPO applies to the IT OU regardless of any Block Inheritance setting on the OU
- C) The Enforced flag causes the GPO to apply only to computers, not users, in the IT OU
- D) The GPO with Enforced status will only apply after the next full domain replication cycle

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Enforced flag on a GPO link cannot be selectively disabled per-OU. It applies to all OUs below the link point.
  - Why C is incorrect: The Enforced flag affects inheritance precedence, not whether Computer or User Configuration sections apply. Both sections of an Enforced GPO can contain settings.
  - Why D is incorrect: GPO settings replicate via SYSVOL and AD replication. An Enforced GPO applies at the next group policy refresh, not after a special domain replication event.

---

### Question 14 (5 points)

Which PowerShell command creates a new GPO named `HR_DriveMappings` and immediately links it to the HR OU in `corp.local`?

- A) `New-GPO -Name "HR_DriveMappings" | New-GPLink -Target "OU=HR,OU=Departments,DC=corp,DC=local"`
- B) `New-GPO -Name "HR_DriveMappings" -Domain "corp.local" -LinkTo "OU=HR,OU=Departments,DC=corp,DC=local"`
- C) `Add-GPOLink -Name "HR_DriveMappings" -Path "OU=HR,OU=Departments,DC=corp,DC=local" -CreateNew`
- D) `New-GPLink -GPO "HR_DriveMappings" -OU "HR" -CreateIfNotExists`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `New-GPO` does not have a `-LinkTo` parameter. GPO creation and linking are separate operations, but can be pipelined using `New-GPLink`.
  - Why C is incorrect: `Add-GPOLink` is not a valid PowerShell cmdlet in the GroupPolicy module. The correct linking cmdlet is `New-GPLink`.
  - Why D is incorrect: `New-GPLink` does not accept `-GPO`, `-OU`, or `-CreateIfNotExists` parameters with these names. The valid parameters are `-Name` (for the GPO name) and `-Target` (for the OU distinguished name).

---

### Question 15 (5 points)

A WMI Filter is attached to a GPO targeting only laptops. A desktop computer in the same OU that also has the GPO linked reports the policy not applying. The administrator confirms the WMI query is correct. What is the expected behavior and its reason?

- A) This is a misconfiguration — WMI filters should never be used with Security Filtering on the same GPO
- B) This is correct behavior — the WMI Filter evaluated to FALSE on the desktop (not a laptop), so the GPO is skipped for that machine
- C) The desktop needs `gpupdate /force /target:computer` to evaluate the WMI filter
- D) WMI filters only apply to User Configuration sections, so Computer Configuration still applies to the desktop

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: WMI filters and Security Filtering can be used together on the same GPO. They are independent mechanisms — both must pass for the GPO to apply.
  - Why C is incorrect: `gpupdate /force` triggers policy refresh but does not change the result of a correctly functioning WMI filter. If the query returns FALSE for desktops, forcing a refresh will continue to skip the GPO.
  - Why D is incorrect: WMI filters apply to the entire GPO — both Computer Configuration and User Configuration sections are skipped when a WMI filter returns FALSE.

---

### Question 16 (5 points)

An administrator notices that the Default Domain Policy has been modified by a previous administrator to include custom screensaver settings. What is the Microsoft best-practice recommendation for this situation?

- A) Leave it as-is because modifying the Default Domain Policy is standard practice and fully supported
- B) Create a new GPO for the screensaver settings, link it to the domain, and restore the Default Domain Policy to its original state using `dcgpofix`
- C) Delete the Default Domain Policy and recreate it manually in GPMC
- D) Use `Get-GPOReport` to export the customized Default Domain Policy and then reimport it as a new GPO

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Microsoft explicitly recommends against modifying the Default Domain Policy beyond password, lockout, and Kerberos settings. Custom settings in the Default Domain Policy make troubleshooting harder and increase the risk of breaking authentication.
  - Why C is incorrect: Deleting the Default Domain Policy entirely would remove the password and account lockout policies that control domain authentication. This is far more disruptive than using `dcgpofix` to restore it.
  - Why D is incorrect: Exporting and reimporting the customized policy as a new GPO would preserve the custom settings but would not restore the Default Domain Policy to its baseline state.

---

### Question 17 (5 points)

An administrator configures Loopback Processing in Merge mode on a GPO linked to the Lab OU. A student (whose user account is in the Students OU) logs into a computer in the Lab OU. How are the User Configuration settings determined?

- A) Only the Lab OU's GPO User Configuration applies — the student's OU policies are completely replaced
- B) Only the Students OU's GPO User Configuration applies — Merge mode gives the user's OU policies exclusive control
- C) Both the Students OU policies and the Lab OU policies apply; where they conflict, the Lab OU policy wins
- D) Neither policy applies because Merge mode requires identical settings in both OUs to function

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Complete replacement of the user's OU policies is the behavior of Replace mode, not Merge mode. Merge mode combines both sets of policies.
  - Why B is incorrect: If only the user's OU policies applied, Loopback Processing would serve no purpose. Merge mode is specifically designed to combine the computer-OU policies with the user-OU policies.
  - Why D is incorrect: Merge mode does not require matching settings. It applies both policy sets and resolves conflicts by giving precedence to the computer-OU (Lab OU) policies.

---

### Question 18 (5 points)

A Group Policy Object contains settings in both Computer Configuration and User Configuration. An administrator sets the GPO status to "User Configuration Settings Disabled." What is the effect?

- A) The entire GPO stops applying to all users and computers
- B) The Computer Configuration settings still apply; the User Configuration section is skipped during processing
- C) The User Configuration settings apply but require manual approval before taking effect
- D) The GPO becomes read-only and cannot be edited until the status is changed back

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Disabling one configuration section does not disable the entire GPO. Computer Configuration processing continues normally.
  - Why C is incorrect: Group Policy does not have a manual approval workflow. Settings are applied automatically when the GPO is applied at refresh or startup/logon.
  - Why D is incorrect: GPO status (All Settings Disabled, User Configuration Disabled, Computer Configuration Disabled) affects processing, not editability. Administrators can still edit the GPO regardless of its status.

---

### Question 19 (5 points)

An administrator needs to back up all GPOs in the domain to `C:\GPO_Backup` before making changes. Which PowerShell command accomplishes this?

- A) `Export-GPO -All -Path "C:\GPO_Backup"`
- B) `Backup-GPO -All -Path "C:\GPO_Backup"`
- C) `Copy-GPO -All -Destination "C:\GPO_Backup"`
- D) `Get-GPO -All | Save-GPO -Path "C:\GPO_Backup"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Export-GPO` is not a valid PowerShell cmdlet in the GroupPolicy module. The correct cmdlet for GPO backup is `Backup-GPO`.
  - Why C is incorrect: `Copy-GPO` copies a GPO to a different domain, not to a file system path. It is not a backup command.
  - Why D is incorrect: `Save-GPO` is not a valid PowerShell cmdlet. The pipeline approach described here does not exist in the GroupPolicy module.

---

### Question 20 (5 points)

After applying a new GPO that restricts access to the Control Panel, users report they can still access it immediately after `gpupdate /force` is run on their workstations. The GPO is confirmed as applied in `gpresult`. What is the most likely explanation?

- A) The GPO has a WMI Filter that is blocking the setting from taking effect
- B) The setting is in User Configuration and requires the user to log off and log back on for the restriction to take effect after the refresh
- C) The setting requires a reboot of the Domain Controller to propagate to clients
- D) Control Panel restrictions are only enforced during computer startup, not during an active user session

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: If a WMI filter were blocking the GPO, it would not appear as applied in `gpresult`. The question states it is confirmed as applied.
  - Why C is incorrect: Client-side Group Policy processing does not depend on DC reboots. The DC serves the SYSVOL data; the client processes it. A DC reboot is not required.
  - Why D is incorrect: User Configuration settings including Control Panel restrictions can enforce both at startup and during an active session, but some shell settings (like hiding Control Panel) take effect at the next logon shell refresh — meaning logoff and logon is required for them to visually appear restricted.
