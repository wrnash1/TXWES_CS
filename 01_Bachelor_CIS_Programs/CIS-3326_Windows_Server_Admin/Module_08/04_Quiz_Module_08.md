# Quiz: Module 08 — Group Policy Objects (GPOs)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
Review your Reading Guide and video notes before beginning.

---

## Question 1

An administrator links a GPO to the domain root that sets the minimum password
length to 14 characters. A separate GPO linked to the `OU=IT` OU sets the minimum
password length to 8 characters. Users whose accounts are in the IT OU are able
to set passwords shorter than 14 characters. Which concept explains this behavior?

A) The IT OU GPO is processed first in the LSDOU chain and sets the password
length; the domain GPO cannot override OU-level policies.

B) Account Policies set in OU-level GPOs apply only to local computer accounts
on machines in that OU, not to domain user accounts. Domain accounts require
Account Policies at the domain-linked GPO level.

C) The IT OU GPO has a higher link order number than the domain GPO, giving the
domain GPO higher priority for password length settings.

D) Password length settings can only be configured in the Default Domain Policy
GPO; all other GPO names are ignored for Account Policy settings.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: LSDOU processes domain GPOs before OU GPOs, so domain GPOs are processed first and OU GPOs are processed last — the opposite of what this option states. However, Account Policies at the OU level apply only to local accounts, so the OU GPO's password setting does not affect domain accounts at all.
  - Why C is incorrect: Link order controls the priority among multiple GPOs linked to the same container. A lower link order number (higher in the GPMC list) means higher priority — but this scenario involves different containers (domain vs. OU), not multiple GPOs on the same container.
  - Why D is incorrect: Account Policies can be configured in any GPO — not only the Default Domain Policy. Any GPO linked at the domain level will apply domain Account Policies. The restriction is the link level (must be domain), not the GPO name.

---

## Question 2

A system administrator needs to prevent a specific OU from receiving any Group
Policy settings from the domain-level or parent OU GPOs. Which Group Policy
feature accomplishes this?

A) Setting all GPOs linked to parent containers to Disabled, which prevents them
from processing for any OU below the parent.

B) Applying Enforced to the OU's own GPOs, which causes the OU's policies to
take priority over all parent policies.

C) Enabling Block Inheritance on the OU, which prevents GPOs from parent
containers from flowing down to the OU.

D) Removing the computer and user objects from the Security Filtering of all
parent GPOs, which prevents those GPOs from applying to any objects in the OU.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Disabling a GPO link in a parent container prevents the GPO from applying to everything linked to that container, affecting all OUs — not just the target OU. This is a broad action that does not selectively protect one OU.
  - Why B is incorrect: Enforced is a property of a GPO link, not an OU setting. Setting a GPO as Enforced means it cannot be blocked — it does not block parent GPOs from applying. Enforced is the opposite of what Block Inheritance does.
  - Why D is incorrect: Removing objects from Security Filtering is a valid way to prevent specific GPOs from applying to specific users/computers, but it requires modifying every parent GPO individually. Block Inheritance is the per-OU setting that blocks all parent GPOs at once.

---

## Question 3

A university has a `PublicKiosks` OU containing 20 lab computers. Any student
who logs on to a kiosk should receive a heavily locked-down desktop — regardless
of which OU the student's user account is in. The student's home OU allows
access to all standard applications. Which Group Policy feature and mode
achieves this requirement?

A) Security Filtering on the kiosk GPO — add all student user accounts to the
Security Filtering group so the kiosk policy follows the user to any computer.

B) Loopback Processing in Merge mode linked to the Kiosks OU — the computer's
User Configuration settings are added to the user's settings.

C) Loopback Processing in Replace mode linked to the Kiosks OU — the computer's
User Configuration settings completely replace the user's normal User
Configuration, regardless of the user's own OU policy.

D) Block Inheritance on the student's OU — prevents the student's normal policy
from applying whenever they log on to a kiosk computer.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Security Filtering would cause the kiosk GPO to follow the user to any computer they log on to, which is the opposite requirement. The goal is for the computer's location to determine policy, not the user's location.
  - Why B is incorrect: Merge mode adds the computer's User Configuration to the user's existing User Configuration. The student's permissive home policy would still apply, supplemented by the kiosk policy. Conflicts go to the computer, but the student's allowed settings remain. Replace mode is required to completely discard the student's normal policy.
  - Why D is incorrect: Block Inheritance on the student's OU would prevent the student from receiving their normal policy everywhere, not just when logging on to a kiosk. This would be an overly broad action that breaks the student's policy in all contexts.

---

## Question 4

An administrator configures a GPO with Enforced on a link from the domain to
a specific OU. A junior administrator then enables Block Inheritance on a child
OU beneath that OU. What is the effective result?

A) The Block Inheritance completely prevents the Enforced GPO from applying
to users and computers in the child OU.

B) The Enforced GPO still applies to the child OU despite Block Inheritance.
Enforced links cannot be blocked by Block Inheritance at any level.

C) Block Inheritance cancels the Enforced flag and the GPO reverts to normal
priority processing through the child OU.

D) An administrative alert is generated and both settings are disabled until
a Domain Admin resolves the conflict in Group Policy Management Console.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This is the most common misconception about Block Inheritance. Block Inheritance stops non-Enforced GPOs only. Enforced GPOs are specifically designed to override Block Inheritance at any level below the Enforced link.
  - Why C is incorrect: Block Inheritance has no effect on Enforced links. The Enforced flag on a GPO link is not cancelled or altered by Block Inheritance settings on child OUs.
  - Why D is incorrect: Windows does not generate administrative alerts for the combination of Enforced and Block Inheritance. This is expected, well-defined behavior. Block Inheritance blocks normal GPOs; Enforced GPOs are exempt.

---

## Question 5

An administrator runs `gpresult /r` on a workstation and notices the GPO
`TXWES_Students_Restrictions` is listed under "The following GPOs were not
applied because they were filtered out." The reason given is "Denied (Security)."
What is the most likely cause?

A) The GPO has Block Inheritance enabled, which filters the GPO from applying
to the local workstation's OU.

B) The workstation's computer account or the logged-on user account is not
included in the GPO's Security Filtering group.

C) The GPO link is set to Disabled, which filters the GPO from processing at
startup or logon.

D) The GPO contains only Computer Configuration settings, and the user is
attempting to view User Configuration RSoP, causing a security filtering
mismatch.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Block Inheritance prevents GPOs from parent containers from applying — it does not show as "Denied (Security)" in gpresult. A Block Inheritance filter shows as "Blocked (SOM)" in the RSoP output.
  - Why C is incorrect: A disabled GPO link shows as "Disabled (Link)" in gpresult output, not "Denied (Security)." The "Denied (Security)" reason specifically indicates a Security Filtering issue.
  - Why D is incorrect: Having only Computer Configuration settings does not cause a "Denied (Security)" message. GPOs with only Computer Configuration simply do not write User Configuration to the RSoP. The security denial reason is about the principal not being in the Security Filtering ACL.

---

## Question 6

An administrator needs to create a GPO that configures a legal notice displayed
at every domain computer's logon screen, and backs up the GPO immediately after
creation. Which sequence of PowerShell commands is correct?

A) `Set-GPO "LegalNotice" -Target "DC=txwes,DC=edu"` then `Export-GPO -Name "LegalNotice" -Path "C:\Backup"`

B) `New-GPO -Name "LegalNotice"`, then `New-GPLink -Name "LegalNotice" -Target "DC=txwes,DC=edu" -LinkEnabled Yes`, then `Backup-GPO -Name "LegalNotice" -Path "C:\GPOBackups"`

C) `New-GPO -Name "LegalNotice"`, then `Set-GPLink -Enforced Yes`, then `Copy-GPO -SourceName "LegalNotice" -TargetName "LegalNotice_Backup"`

D) `Add-GPO -Name "LegalNotice" -Domain "txwes.edu"`, then `Link-GPO -Target "DC=txwes,DC=edu"`, then `Save-GPO -Name "LegalNotice" -Path "C:\Backup"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Set-GPO` modifies an existing GPO's metadata — it does not create a new GPO or link it. `Export-GPO` is not a valid GroupPolicy module cmdlet; the correct cmdlet is `Backup-GPO`.
  - Why C is incorrect: `Set-GPLink -Enforced Yes` requires both `-Name` and `-Target` parameters. `Copy-GPO` creates a copy of the GPO with a new name — it does not create a backup. Backups require `Backup-GPO`, which stores the GPO in a restorable format with `Restore-GPO`.
  - Why D is incorrect: `Add-GPO`, `Link-GPO`, and `Save-GPO` are not valid PowerShell GroupPolicy module cmdlets. The correct cmdlets are `New-GPO`, `New-GPLink`, and `Backup-GPO`.

---

## Question 7

Three GPOs are linked to the `OU=Students` OU in the following order in GPMC
(top to bottom): GPO-A (link order 1), GPO-B (link order 2), GPO-C (link order 3).
All three GPOs configure the same registry setting. Which GPO's value for that
setting is effective?

A) GPO-C, because it has the highest link order number and is processed last.

B) GPO-A, because it has the lowest link order number (highest priority) and
is processed last within the OU.

C) GPO-B, because the middle link order represents the average and is the
compromise value applied.

D) All three GPO values are merged and the numeric average of the three values
is applied by the Group Policy client.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A higher link order number means lower priority, not higher. GPO-C (link order 3) is processed first among the three, meaning its setting will be overwritten by GPO-B, then GPO-A.
  - Why C is incorrect: Group Policy does not calculate averages or merge numeric settings. It applies settings sequentially and the last-processed GPO wins. Link order 1 (highest in the list) is processed last and wins.
  - Why D is incorrect: Group Policy does not blend or average registry values. For any given setting, exactly one GPO's value is applied — the last one processed in the chain.

---

## Question 8

An administrator wants to verify exactly which GPO configured the setting
that is preventing users in the Students OU from accessing Control Panel.
Which tool or command provides the most detailed information about the winning
GPO for each applied setting?

A) `Get-GPO -All` — lists all GPOs in the domain with their current status.

B) `gpresult /h C:\Report.html` — generates an HTML RSoP report showing each
applied setting and the source GPO that provided the winning value.

C) `Get-GPInheritance -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu"` — shows
the inheritance chain for the OU, identifying the winning GPO per setting.

D) `Get-EventLog -LogName System -Source UserEnv` — queries the Group Policy
operational event log to find the specific GPO that applied Control Panel settings.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-GPO -All` lists GPOs and their metadata. It does not show which settings are in each GPO or which GPO is the winner for a given setting on a specific computer.
  - Why C is incorrect: `Get-GPInheritance` shows which GPOs are linked to and inherited by an OU — the GPO list and link order. It does not show the individual settings within each GPO or which GPO won for a specific registry value.
  - Why D is incorrect: The UserEnv event log source records Group Policy processing events (applied, skipped, etc.) but does not provide the per-setting GPO winner information that `gpresult /h` presents in a structured, readable format.

---

## Question 9

A company's security policy requires that all Windows domain computers display
a legal notice before logon. The IT team configures this in a GPO and links it
to the domain root. Six months later, a new OU (`OU=Development`) is created
with Block Inheritance enabled. The legal notice no longer appears on computers
in the Development OU. What is the fastest fix that ensures the legal notice
applies everywhere without affecting any other existing GPO settings?

A) Re-link the legal notice GPO directly to the `OU=Development` OU as well.

B) Set the legal notice GPO link at the domain root to Enforced.

C) Disable Block Inheritance on the `OU=Development` OU.

D) Move all computer accounts from `OU=Development` to the default `CN=Computers`
container where Block Inheritance does not apply.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Re-linking the GPO to each new OU is a maintenance burden that must be repeated every time a new OU with Block Inheritance is created. Setting Enforced at the domain root handles all current and future OUs with Block Inheritance automatically.
  - Why C is incorrect: Disabling Block Inheritance on the Development OU would cause all domain-level GPOs to apply to it, potentially applying settings the Development team specifically wanted to block. The goal is a targeted fix for the legal notice, not broad policy re-application.
  - Why D is incorrect: Moving computer accounts to CN=Computers bypasses all OU-based Group Policy, including policies specifically designed for the Development environment. This is a disruptive action that breaks intentional OU-based policy management.

---

## Question 10

A new administrator runs the following command to apply a restriction preventing
students from accessing the command prompt. After a `gpupdate /force`, students
report they can still open the command prompt. What is missing?

```powershell
New-GPO -Name "TXWES_Students_NoCmd" -Domain "txwes.edu"
Set-GPRegistryValue -Name "TXWES_Students_NoCmd" `
    -Key "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" -Type DWord -Value 1
```

A) The registry key path is incorrect — the correct key for DisableCMD is
`HKLM\Software\Microsoft\Windows\System`.

B) The GPO was created and configured but never linked to the Students OU.
Without a `New-GPLink` command, the GPO exists but does not apply to any
users or computers.

C) The `Set-GPRegistryValue` cmdlet requires a `-Scope Computer` parameter
to apply settings to user accounts; without it, the setting is discarded.

D) The `gpupdate /force` command must be run on the client workstations where
students log on — running it only on DC1 does not push policy to client machines.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `HKCU\Software\Policies\Microsoft\Windows\System\DisableCMD` is the correct registry path for the "Prevent access to the command prompt" Administrative Template setting. The key path in the command is correct.
  - Why C is incorrect: `Set-GPRegistryValue` does not have a `-Scope Computer` parameter. The registry hive used (HKCU vs. HKLM) determines whether the setting goes into User Configuration or Computer Configuration. HKCU correctly places it in User Configuration.
  - Why D is incorrect: While `gpupdate /force` on clients is required to refresh policy immediately, the fundamental issue here is that the GPO has never been linked. A GPO that is not linked applies to nobody, regardless of how many times `gpupdate` is run.

---

## Question 11 (5 points)

An administrator needs to verify that a GPO named `TXWES_Students_Restrictions` is both linked to the Students OU and that the link is currently enabled. Which PowerShell command provides this information?

- A) `Get-GPO -Name "TXWES_Students_Restrictions" | Select-Object GpoStatus`
- B) `Get-GPInheritance -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu" | Select-Object -ExpandProperty GpoLinks`
- C) `Get-GPLink -Name "TXWES_Students_Restrictions" -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu"`
- D) `Show-GPOLinks -Name "TXWES_Students_Restrictions"`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-GPO -Name` returns the GPO object's metadata including status, but does not show which OUs it is linked to or whether each link is enabled. GPO status (All Settings Disabled, etc.) is different from link enabled/disabled state.
  - Why C is incorrect: `Get-GPLink` is not a valid PowerShell cmdlet in the GroupPolicy module. Link information is retrieved via `Get-GPInheritance`.
  - Why D is incorrect: `Show-GPOLinks` is not a valid cmdlet. The correct approach for viewing GPO links and their enabled state is `Get-GPInheritance`.

---

## Question 12 (5 points)

A GPO is linked at the domain level and configured to deploy a specific software package. Six months after deployment, the package is no longer needed. The administrator wants to remove the software from all domain computers. Which GPO configuration removes software that was deployed via Group Policy Software Installation?

- A) Delete the GPO entirely — deleting the GPO automatically removes the software from all computers at next startup
- B) Change the software package deployment action from "Assigned" to "Uninstall this application when it falls out of the scope of management" in the GPO
- C) Use `gpupdate /force` on each computer to push the uninstall command
- D) Remove the computer accounts from the Security Filtering of the GPO

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Deleting a GPO removes the policy configuration but does not instruct client computers to uninstall already-deployed software. The software remains installed on all affected machines.
  - Why C is incorrect: `gpupdate /force` triggers policy refresh but does not by itself uninstall software. The GPO must be configured to issue the uninstall instruction first.
  - Why D is incorrect: Removing computers from Security Filtering means the GPO no longer applies to them, but this does not cause the software to be uninstalled. Software deployed via "Assigned" stays installed even when it falls out of scope, unless the "Uninstall when out of scope" option is set.

---

## Question 13 (5 points)

An administrator wants to apply a GPO only to computers that are in a specific subnet `10.10.20.0/24`. Which Group Policy feature evaluates the client's network properties at refresh time to determine whether the GPO should apply?

- A) Security Filtering using an IP address-based security group
- B) A WMI Filter that queries `Win32_NetworkAdapterConfiguration` for the subnet address
- C) GPO link order targeting set to the site associated with that subnet
- D) Conditional Forwarder configured in DNS for the 10.10.20.0 network

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Security groups contain AD objects (users, computers), not IP address ranges. There is no IP address-based security group that dynamically includes all computers in a subnet. WMI Filters evaluate dynamic hardware properties.
  - Why C is incorrect: AD Sites can be mapped to subnets and GPO links can target sites. While this is a valid approach for site-based targeting, the question specifically asks about a feature that "evaluates at refresh time" — which is the WMI Filter mechanism.
  - Why D is incorrect: Conditional Forwarders are a DNS feature for routing queries for specific domains to designated DNS servers. They have no relationship to Group Policy targeting.

---

## Question 14 (5 points)

A GPO applies a screensaver timeout via User Configuration. After linking the GPO to the Students OU and running `gpupdate /force`, the screensaver setting is not active. The student's computer account is in the `Computers` OU, not the `Students` OU. What is the likely reason the policy is not applying?

- A) User Configuration settings in a GPO only apply when the user's computer account is in the same OU as the user account
- B) The GPO's screensaver setting is in User Configuration, which applies based on the user's OU location. Since the student user accounts are in the Students OU and the GPO is linked there, it should apply — but a reboot may be needed
- C) The screensaver timeout setting is in Computer Configuration only; it cannot be set via User Configuration
- D) The `gpupdate /force` command only refreshes Computer Configuration; User Configuration requires a logoff and logon

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: User Configuration policies apply based on the user account's OU location, not the computer's OU. The computer account's OU is irrelevant for User Configuration processing under standard (non-loopback) processing.
  - Why B is incorrect: This option correctly identifies that User Configuration applies based on the user's OU. However, the screensaver setting not being active after `gpupdate /force` is explained by the fact that `gpupdate /force` refreshes both sections but some User Configuration shell settings (like screensaver) only fully activate at logon.
  - Why C is incorrect: Screensaver settings (Control Panel > Personalization) can be configured in both Computer Configuration and User Configuration. The screensaver timeout under User Configuration is a valid and commonly used setting.

---

## Question 15 (5 points)

An administrator uses `Get-GPResultantSetOfPolicy -ReportType HTML -Path "C:\RSoP.html"`. When does this cmdlet collect data for the report?

- A) It reads the current local policy files on the DC where the command is run and reports those settings
- B) It simulates what would apply to the current user and computer by querying AD and generating the report without contacting the client
- C) It collects the actual applied RSoP data from the local machine where the cmdlet is run, representing what is currently applied
- D) It queries all DCs in the domain and generates an aggregate report combining settings from all SYSVOL copies

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The cmdlet queries the Group Policy client data on the local machine, not the DC's policy files. The DC stores GPO templates; the client applies and records them.
  - Why B is incorrect: RSoP simulation (planning mode) is performed using GPMC or the `Get-GPResultantSetOfPolicy -Mode Planning` variant. Without `-Mode Planning`, the default is logging mode — actual applied data from the current machine.
  - Why D is incorrect: RSoP reports are per-machine and per-user. The cmdlet collects data from the local machine where it is run. It does not aggregate data from all DCs.

---

## Question 16 (5 points)

A developer logs on to a computer in the `Development` OU, which has Block Inheritance enabled. The developer's user account is in the `OU=IT` OU, which has a GPO granting access to developer tools. Will the developer receive the developer tools policy?

- A) No — Block Inheritance on the Development OU prevents all GPOs from applying, including those from the user's own OU
- B) Yes — Block Inheritance only affects GPOs linked above the Development OU in the hierarchy. The developer's user account GPO is linked to the IT OU and applies based on the user's OU, not the computer's OU
- C) No — the developer's computer account is in the Development OU, so all policies apply based on the computer's OU
- D) Yes — Block Inheritance is automatically disabled for any user who logs on with a Domain Admin account

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Block Inheritance applies to Computer Configuration and to User Configuration that flows down from parent containers to the Development OU. User Configuration linked to the user's own OU (IT OU) applies normally regardless of the computer's OU, unless Loopback Processing is enabled.
  - Why C is incorrect: User Configuration policies apply based on the user account's OU, not the computer's OU. Without Loopback Processing, the computer's OU does not affect which User Configuration policies the logged-on user receives.
  - Why D is incorrect: Block Inheritance is not disabled for Domain Admins. All accounts, including Domain Admins, are subject to Block Inheritance on OUs their computer is in — unless the GPO is set to Enforced.

---

## Question 17 (5 points)

Which PowerShell command disables a specific GPO link on the `OU=Kiosks` OU without removing the link entirely, allowing it to be re-enabled later?

- A) `Remove-GPLink -Name "TXWES_Kiosk_Policy" -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu"`
- B) `Set-GPLink -Name "TXWES_Kiosk_Policy" -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" -LinkEnabled No`
- C) `Disable-GPO -Name "TXWES_Kiosk_Policy"`
- D) `Set-GPO -Name "TXWES_Kiosk_Policy" -GpoStatus AllSettingsDisabled`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Remove-GPLink` permanently removes the link between the GPO and the OU. If the administrator later wants the GPO to apply to Kiosks again, a new link must be created. The question asks to disable the link, not remove it.
  - Why C is incorrect: `Disable-GPO` is not a valid PowerShell cmdlet. GPO status is changed with `Set-GPO -GpoStatus`. However, disabling the GPO itself affects all its links everywhere — not just the one OU link.
  - Why D is incorrect: `Set-GPO -GpoStatus AllSettingsDisabled` disables all settings in the GPO (Computer and User Configuration), which affects all OU links of that GPO. To disable only one specific link, `Set-GPLink -LinkEnabled No` is the correct targeted approach.

---

## Question 18 (5 points)

An organization has a mandatory GPO linked at the domain root that all OU administrators must not be able to override. Which two GPO features must be configured to guarantee this?

- A) Set the GPO link to Enforced and ensure no OU in the domain has Block Inheritance enabled
- B) Set the GPO link to Enforced — this alone guarantees the GPO applies everywhere regardless of Block Inheritance
- C) Enable Block Inheritance on the domain root and set the GPO link order to 1
- D) Set the GPO as Read-Only in GPMC and link it to every OU individually

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Enforced alone is sufficient to guarantee the GPO applies everywhere. You do not need to audit or remove Block Inheritance from every OU — that is the point of Enforced. Block Inheritance cannot stop an Enforced GPO.
  - Why C is incorrect: Block Inheritance on the domain root would prevent any GPOs linked above (there are none above the domain root) from flowing in — it has no effect at the domain level and would not guarantee the GPO applies to all OUs below.
  - Why D is incorrect: Making a GPO Read-Only prevents administrators from editing it but does not affect whether it applies. Linking to every OU individually would work functionally but is maintenance-intensive and unnecessary when Enforced at the domain level is available.

---

## Question 19 (5 points)

An administrator needs to find all GPOs that currently have no links (unlinked GPOs) in the domain, as part of a GPO cleanup project. Which PowerShell approach identifies these orphaned GPOs?

- A) `Get-GPO -All | Where-Object { $_.GpoStatus -eq "Unlinked" }`
- B) `Get-GPO -All | Where-Object { $_.LinksCount -eq 0 }`
- C) `Get-GPO -All | ForEach-Object { if ((Get-GPInheritance -Target $_).GpoLinks.Count -eq 0) { $_ } }`
- D) `Get-GPO -All | Where-Object { $_.Links -eq $null }`

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: `GpoStatus` is a property that indicates whether Computer Configuration or User Configuration sections are enabled or disabled, not whether the GPO is linked to any container.
  - Why B is incorrect: `LinksCount` is not a property of GPO objects returned by `Get-GPO`. GPO link information is stored separately and must be queried via `Get-GPInheritance` or by examining the GPO's XML report.
  - Why C is incorrect: `Get-GPInheritance` takes an OU, domain, or site as the target — it queries what applies to a container, not what containers a GPO is linked to. This approach would not correctly identify unlinked GPOs.

---

## Question 20 (5 points)

A GPO applies a software restriction policy that blocks execution of `notepad.exe`. The policy is in User Configuration. A user complains that Notepad is still accessible. `gpresult /r` shows the GPO as "Applied." What is the most likely explanation?

- A) User Configuration software restriction policies require a reboot to take effect, not just a logoff/logon
- B) The software restriction policy may conflict with Windows Defender Application Control (WDAC), which overrides GPO software restrictions
- C) The GPO is applied but the user has not logged off and back on; User Configuration settings that affect process execution apply at logon, not mid-session after `gpupdate`
- D) The software restriction policy requires the Enforced flag to be set on the GPO link to block executable access

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: User Configuration software restriction policies apply at logon, not at reboot (reboot triggers Computer Configuration refresh). Logging off and back on is sufficient — a full reboot is not required.
  - Why B is incorrect: While WDAC can override or supplement software restriction policies, this would not explain why `gpresult` shows the GPO as applied. WDAC conflicts manifest differently and would not be the first explanation to test.
  - Why D is incorrect: The Enforced flag controls inheritance precedence in the LSDOU chain. It does not affect whether a correctly applied software restriction policy is enforced at the process execution level. The GPO is already shown as Applied.
