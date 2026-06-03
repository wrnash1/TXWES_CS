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
