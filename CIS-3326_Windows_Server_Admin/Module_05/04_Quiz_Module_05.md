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
