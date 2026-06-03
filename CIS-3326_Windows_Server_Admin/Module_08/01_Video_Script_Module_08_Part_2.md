# Video Script: Module 08 — Group Policy Objects (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back. I am Professor Nash.

In Part 1 we covered the GPO architecture, LSDOU processing order, Block
Inheritance, Enforcement, RSoP, Loopback Processing, and common security
policies.

In Part 2 we configure all of this hands-on. We will create GPOs in the Group
Policy Management Console, link them to OUs, configure password and lockout
policies, restrict Control Panel access for students, configure loopback
processing for a Kiosk OU, and use `gpresult` and PowerShell to verify the
results.

---

## Section 1: Creating and Linking a GPO with PowerShell

Before we open the GUI, let us see how to create and link GPOs with PowerShell,
because this is what the exam and the field both expect you to know.

```powershell
# Install the Group Policy Management module if not already present
Import-Module GroupPolicy

# Create a new GPO
New-GPO -Name "TXWES_Students_Restrictions" -Domain "txwes.edu" `
    -Comment "Restricts Control Panel and Command Prompt for students"

# Link the GPO to the Students OU
New-GPLink `
    -Name  "TXWES_Students_Restrictions" `
    -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu" `
    -LinkEnabled Yes

# Verify the link
Get-GPInheritance -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu"
```

The `New-GPO` cmdlet creates the GPO object. The `New-GPLink` cmdlet attaches it
to the OU. Without the link, the GPO exists but applies to nothing.

---

## Section 2: Configuring Password and Lockout Policy

Account Policies must be configured in a GPO linked at the **domain level** for
them to affect domain user accounts. OU-level GPOs that set Account Policies only
affect local account logons on computers in that OU.

```powershell
# Set password policy in the Default Domain Policy (or a new domain-linked GPO)
Set-GPRegistryValue -Name "Default Domain Policy" `
    -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows\System" `
    -ValueName "PasswordComplexity" `
    -Type DWord `
    -Value 1

# The preferred method for Account Policies is the GUI or ADMX templates
# but you can view current domain password policy with:
Get-ADDefaultDomainPasswordPolicy

# Set Account Policy via GUI path:
# Computer Configuration > Policies > Windows Settings >
# Security Settings > Account Policies > Password Policy
#   - Minimum password length: 12
#   - Password must meet complexity requirements: Enabled
#   - Maximum password age: 90 days
#   - Enforce password history: 10

# Set Account Lockout Policy:
#   - Account lockout threshold: 5 invalid attempts
#   - Account lockout duration: 30 minutes
#   - Reset account lockout counter after: 30 minutes
```

Let me walk through the GUI path now. In Group Policy Management Console,
right-click the Default Domain Policy and choose Edit. Navigate to Computer
Configuration > Policies > Windows Settings > Security Settings > Account
Policies > Password Policy. Set Minimum password length to 12. Enable complexity
requirements. Set Maximum password age to 90 days.

---

## Section 3: Configuring User Restrictions with Administrative Templates

Now let us restrict Control Panel access for students using the
TXWES_Students_Restrictions GPO we created.

In GPMC, right-click the TXWES_Students_Restrictions GPO and choose Edit.
Navigate to:

User Configuration > Policies > Administrative Templates > Control Panel

Set **Prohibit access to Control Panel and PC Settings** to **Enabled**.

Navigate to:

User Configuration > Policies > Administrative Templates > System

Set **Prevent access to the command prompt** to **Enabled**.

These settings are applied to any user who logs on whose user account is in
the Students OU — or any child OU that inherits this GPO.

```powershell
# You can also set Administrative Template values via PowerShell
# using Set-GPRegistryValue with the correct registry path.
# The ADMX template maps to a specific registry key:

# Prohibit Control Panel = HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
Set-GPRegistryValue `
    -Name "TXWES_Students_Restrictions" `
    -Key  "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "NoControlPanel" `
    -Type DWord `
    -Value 1

# Prevent command prompt = HKCU\Software\Policies\Microsoft\Windows\System
Set-GPRegistryValue `
    -Name "TXWES_Students_Restrictions" `
    -Key  "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" `
    -Type DWord `
    -Value 1
```

---

## Section 4: Configuring Loopback Processing for Kiosk Computers

Let us set up a Kiosk OU with loopback processing in Replace mode so that any
user logging on to a kiosk gets the kiosk policy regardless of where their user
account lives.

```powershell
# Create the Kiosk OU
New-ADOrganizationalUnit -Name "Kiosks" `
    -Path "OU=TXWES,DC=txwes,DC=edu" `
    -ProtectedFromAccidentalDeletion $true

# Create a kiosk-specific GPO
New-GPO -Name "TXWES_Kiosk_Policy" -Domain "txwes.edu" `
    -Comment "Loopback Replace mode — locked-down kiosk configuration"

# Link the GPO to the Kiosks OU
New-GPLink -Name "TXWES_Kiosk_Policy" `
    -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" `
    -LinkEnabled Yes
```

Now in Group Policy Management Editor for TXWES_Kiosk_Policy, navigate to:

Computer Configuration > Policies > Administrative Templates > System > Group Policy

Set **Configure user Group Policy loopback processing mode** to **Enabled** and
set the Mode to **Replace**.

In Replace mode, the User Configuration settings from this GPO completely
replace any User Configuration the user would normally receive from their own OU.

---

## Section 5: GPO Enforcement and Block Inheritance

```powershell
# Set a GPO link to Enforced (so Block Inheritance cannot block it)
Set-GPLink `
    -Name   "Default Domain Policy" `
    -Target "DC=txwes,DC=edu" `
    -Enforced Yes

# Block Inheritance on a specific OU
# (This prevents domain/parent GPOs from applying, except Enforced ones)
Set-GPInheritance `
    -Target      "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" `
    -IsBlocked   Yes

# View the effective inheritance for an OU
Get-GPInheritance -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu" |
    Select-Object -ExpandProperty GpoLinks
```

Remember: Enforced GPOs always win, even against Block Inheritance. Use Enforced
only for settings that must apply without exception — security baselines and
compliance requirements are the common use cases.

---

## Section 6: Verifying GPO Application with gpresult

After linking and configuring GPOs, you always want to verify they are applying
correctly.

```powershell
# Force an immediate Group Policy refresh on the local machine
gpupdate /force

# Generate an RSoP summary report for the current user and computer
gpresult /r

# Generate a detailed HTML report (open in browser for full details)
gpresult /h C:\GPOReport.html
Start-Process C:\GPOReport.html

# Generate RSoP for a specific user on a remote computer
gpresult /s DC1 /u txwes\jsmith /r

# PowerShell alternative — generate a full XML or HTML GPO report
Get-GPResultantSetOfPolicy -ReportType Html -Path C:\RSoP_Report.html
```

The HTML report from `gpresult /h` shows:

- Every GPO that applied (separated by Computer and User sections).

- Every GPO that was filtered or not applied (and why).

- The winning setting for every configured policy value.

This is the primary troubleshooting tool for Group Policy. When a user says
"my policy is not applying," your first step is `gpresult /h`.

---

## Section 7: Managing GPOs with PowerShell

Here is a quick reference of the most important GPO management cmdlets:

```powershell
# List all GPOs in the domain
Get-GPO -All | Select-Object DisplayName, GPOStatus, CreationTime

# Get details on a specific GPO
Get-GPO -Name "TXWES_Students_Restrictions"

# Back up a single GPO to a folder
Backup-GPO -Name "TXWES_Students_Restrictions" -Path "C:\GPOBackups"

# Back up all GPOs
Backup-GPO -All -Path "C:\GPOBackups"

# Restore a GPO from backup
Restore-GPO -Name "TXWES_Students_Restrictions" -Path "C:\GPOBackups"

# Generate an HTML report of a GPO's settings
Get-GPOReport -Name "TXWES_Students_Restrictions" `
    -ReportType Html `
    -Path "C:\GPOReport_Students.html"

# Copy a GPO (useful for creating a new GPO based on an existing one)
Copy-GPO -SourceName "TXWES_Students_Restrictions" `
         -TargetName "TXWES_Faculty_Restrictions"

# Remove a GPO link (does not delete the GPO, just unlinks it)
Remove-GPLink -Name "TXWES_Students_Restrictions" `
    -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu"

# Delete a GPO entirely
Remove-GPO -Name "TXWES_Students_Restrictions" -Domain "txwes.edu"
```

---

## Section 8: Exam Tips

**Exam Tip 1** — LSDOU order and last-writer-wins. The OU-level GPO always
overrides the Domain-level GPO when there is a conflict, because the OU is
processed last. This appears on almost every Group Policy exam question.

**Exam Tip 2** — Account Policies (password, lockout) must be set in a GPO
linked at the **domain level** to affect domain accounts. Setting them in an
OU-level GPO only affects local computer accounts on machines in that OU.

**Exam Tip 3** — Enforced GPOs override Block Inheritance. Block Inheritance
does not block Enforced. If the scenario has both Block Inheritance on an OU and
an Enforced GPO from the domain, the Enforced GPO still applies.

**Exam Tip 4** — Loopback Replace vs. Merge. Replace discards the user's own
User Configuration and applies only the computer's GPO User Configuration.
Merge applies both and the computer GPO wins on conflicts. The exam will describe
a kiosk or locked-down computer scenario — the answer is Loopback Replace mode.

**Exam Tip 5** — `gpresult /h` generates an HTML RSoP report. `gpupdate /force`
forces an immediate policy refresh. Both appear in troubleshooting scenarios.

**Exam Tip 6** — GPO backup and restore with `Backup-GPO` and `Restore-GPO`
is the correct approach for GPO disaster recovery, not manually copying SYSVOL
folders.

---

## Wrap-Up

In this two-part module we covered Group Policy from architecture through
hands-on configuration. You now understand how GPOs are created, linked,
processed in LSDOU order, inherited, blocked, enforced, and verified with
RSoP tools.

Head to the Reading Guide for reference tables and the complete PowerShell
command list, then complete Lab 08 where you will build a full GPO environment
for the TXWES lab domain.

See you in Module 09 — DNS and DHCP Services.
