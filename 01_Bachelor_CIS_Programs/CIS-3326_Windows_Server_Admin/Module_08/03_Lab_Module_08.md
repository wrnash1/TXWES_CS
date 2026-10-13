# Lab Activity: Module 08 — Group Policy Objects (GPOs)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will create and link Group Policy Objects on DC1, configure
domain-level account policies, restrict user access for the Students OU, create
a loopback processing policy for a Kiosk OU, and verify all settings using
`gpresult` and PowerShell.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 07 lab complete: OU structure exists with TXWES root, IT, Faculty,
  Students OUs populated with user accounts

- DC1 is running Windows Server 2022 as a domain controller for txwes.edu

- PowerShell running as Domain Administrator

- Group Policy Management Console (GPMC) installed

**Learning Objectives:**

- Create and link GPOs using PowerShell and the Group Policy Management Console

- Configure domain-level Account Policies (password and lockout)

- Apply Administrative Template restrictions to the Students OU

- Configure Loopback Processing in Replace mode for a Kiosk OU

- Use `gpresult /h` and `Get-GPInheritance` to verify policy application

---

## Part 1 — Install Group Policy Management Tools

### Step 1.1 — Verify GPMC Is Installed

```powershell
# Install GPMC if not already present
Install-WindowsFeature -Name GPMC -IncludeManagementTools

# Verify
Get-WindowsFeature -Name GPMC | Select-Object Name, InstallState

# Import the GroupPolicy PowerShell module
Import-Module GroupPolicy
```

Take **Screenshot 1** — GPMC installed and module imported.

---

## Part 2 — Create and Link GPOs Using PowerShell

### Step 2.1 — Create Three GPOs

```powershell
# GPO 1 — Domain-wide security policy
New-GPO -Name "TXWES_Domain_Security" -Domain "txwes.edu" `
    -Comment "Password policy, account lockout — domain-wide"

# GPO 2 — Student restrictions
New-GPO -Name "TXWES_Students_Restrictions" -Domain "txwes.edu" `
    -Comment "Control Panel and command prompt restrictions for students"

# GPO 3 — Kiosk lockdown
New-GPO -Name "TXWES_Kiosk_Policy" -Domain "txwes.edu" `
    -Comment "Loopback Replace mode — locked-down kiosk policy"

# Verify all three GPOs exist
Get-GPO -All | Where-Object {$_.DisplayName -like "TXWES_*"} |
    Select-Object DisplayName, GPOStatus, CreationTime
```

### Step 2.2 — Link the GPOs to Appropriate Targets

```powershell
# Link TXWES_Domain_Security to the domain root
New-GPLink -Name "TXWES_Domain_Security" `
    -Target "DC=txwes,DC=edu" `
    -LinkEnabled Yes

# Link TXWES_Students_Restrictions to the Students OU
New-GPLink -Name "TXWES_Students_Restrictions" `
    -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu" `
    -LinkEnabled Yes

# Create the Kiosk OU and link the kiosk GPO
New-ADOrganizationalUnit -Name "Kiosks" `
    -Path "OU=TXWES,DC=txwes,DC=edu" `
    -ProtectedFromAccidentalDeletion $true

New-GPLink -Name "TXWES_Kiosk_Policy" `
    -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" `
    -LinkEnabled Yes
```

### Step 2.3 — Verify GPO Links

```powershell
# Check inheritance for the Students OU
Get-GPInheritance -Target "OU=Students,OU=TXWES,DC=txwes,DC=edu" |
    Select-Object -ExpandProperty GpoLinks
```

Take **Screenshot 2** — `Get-GPInheritance` showing TXWES_Students_Restrictions
linked to the Students OU.

---

## Part 3 — Configure Domain-Level Account Policy

Account Policies must be configured in a domain-linked GPO to affect domain user
accounts. We will edit the TXWES_Domain_Security GPO.

### Step 3.1 — Open Group Policy Management Console

1. Open **Group Policy Management** from Server Manager > Tools.

2. Expand Forest: txwes.edu > Domains > txwes.edu.

3. Right-click **TXWES_Domain_Security** and choose **Edit**.

### Step 3.2 — Configure Password Policy

In the Group Policy Management Editor navigate to:

Computer Configuration > Policies > Windows Settings > Security Settings >
Account Policies > Password Policy

Configure these settings:

- Minimum password length: **12 characters**

- Password must meet complexity requirements: **Enabled**

- Maximum password age: **90 days**

- Enforce password history: **10 passwords**

### Step 3.3 — Configure Account Lockout Policy

Navigate to:

Computer Configuration > Policies > Windows Settings > Security Settings >
Account Policies > Account Lockout Policy

Configure these settings:

- Account lockout threshold: **5 invalid logon attempts**

- Account lockout duration: **30 minutes**

- Reset account lockout counter after: **30 minutes**

### Step 3.4 — Verify Via PowerShell

```powershell
# Force a policy update to apply the new domain policy
gpupdate /force

# View the effective domain password policy
Get-ADDefaultDomainPasswordPolicy | Select-Object `
    MinPasswordLength, ComplexityEnabled, MaxPasswordAge, PasswordHistoryCount

# View lockout policy
Get-ADDefaultDomainPasswordPolicy | Select-Object `
    LockoutThreshold, LockoutDuration, LockoutObservationWindow
```

Take **Screenshot 3** — `Get-ADDefaultDomainPasswordPolicy` output showing
MinPasswordLength: 12 and LockoutThreshold: 5.

---

## Part 4 — Configure Student Restrictions via Administrative Templates

### Step 4.1 — Edit TXWES_Students_Restrictions in GPMC

1. In GPMC, right-click **TXWES_Students_Restrictions** and choose **Edit**.

2. Navigate to:
   User Configuration > Policies > Administrative Templates > Control Panel

3. Double-click **Prohibit access to Control Panel and PC Settings**.

4. Set to **Enabled** and click OK.

5. Navigate to:
   User Configuration > Policies > Administrative Templates > System

6. Double-click **Prevent access to the command prompt**.

7. Set to **Enabled**, set "Disable the command prompt script processing also"
   to **Yes**, and click OK.

### Step 4.2 — Set Registry Values via PowerShell

You can also set these values directly through PowerShell:

```powershell
# Prohibit Control Panel
Set-GPRegistryValue `
    -Name      "TXWES_Students_Restrictions" `
    -Key       "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" `
    -ValueName "NoControlPanel" `
    -Type      DWord `
    -Value     1

# Prevent command prompt access
Set-GPRegistryValue `
    -Name      "TXWES_Students_Restrictions" `
    -Key       "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" `
    -Type      DWord `
    -Value     1

# Verify the GPO report
Get-GPOReport -Name "TXWES_Students_Restrictions" `
    -ReportType Html `
    -Path "C:\GPOReport_Students.html"
```

Take **Screenshot 4** — HTML GPO report open in browser showing the NoControlPanel
and DisableCMD settings configured in TXWES_Students_Restrictions.

---

## Part 5 — Configure Loopback Processing for the Kiosk OU

### Step 5.1 — Edit TXWES_Kiosk_Policy

1. In GPMC, right-click **TXWES_Kiosk_Policy** and choose **Edit**.

2. Navigate to:
   Computer Configuration > Policies > Administrative Templates > System >
   Group Policy

3. Double-click **Configure user Group Policy loopback processing mode**.

4. Set to **Enabled**.

5. Set the Mode dropdown to **Replace**.

6. Click OK.

### Step 5.2 — Add a User Restriction Under Computer Configuration

Still in TXWES_Kiosk_Policy, navigate to:

User Configuration > Policies > Administrative Templates > Control Panel

Set **Prohibit access to Control Panel and PC Settings** to **Enabled**.

This User Configuration setting, combined with Loopback Replace mode, will
apply to any user who logs on to a kiosk computer — replacing their normal
User Configuration with the kiosk policy.

```powershell
# Verify the kiosk GPO has loopback configured by generating a report
Get-GPOReport -Name "TXWES_Kiosk_Policy" `
    -ReportType Html `
    -Path "C:\GPOReport_Kiosk.html"
```

Take **Screenshot 5** — The TXWES_Kiosk_Policy GPO report showing Loopback
Processing Mode set to Replace.

---

## Part 6 — Test GPO Enforcement and Block Inheritance

### Step 6.1 — Set a GPO as Enforced

```powershell
# Set TXWES_Domain_Security as Enforced at the domain level
Set-GPLink `
    -Name     "TXWES_Domain_Security" `
    -Target   "DC=txwes,DC=edu" `
    -Enforced Yes

# Verify
Get-GPInheritance -Target "DC=txwes,DC=edu" |
    Select-Object -ExpandProperty GpoLinks |
    Select-Object DisplayName, Enabled, Enforced
```

### Step 6.2 — Test Block Inheritance

```powershell
# Block Inheritance on the Kiosks OU
Set-GPInheritance -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" -IsBlocked Yes

# Verify — notice Enforced GPO still appears
Get-GPInheritance -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu"
```

The output will show that even with Block Inheritance enabled on Kiosks,
the Enforced TXWES_Domain_Security still appears in the inherited GPOs list.

Take **Screenshot 6** — `Get-GPInheritance` output for the Kiosks OU showing
Block Inheritance is active AND the Enforced domain GPO is still shown.

---

## Part 7 — Verify with gpresult

### Step 7.1 — Force Policy Refresh and Generate Report

```powershell
# Force immediate policy refresh
gpupdate /force

# Generate RSoP text summary
gpresult /r

# Generate full HTML report
gpresult /h C:\RSoP_Report.html
Start-Process C:\RSoP_Report.html
```

### Step 7.2 — PowerShell RSoP Report

```powershell
Get-GPResultantSetOfPolicy -ReportType Html -Path "C:\RSoP_PS.html"
Start-Process "C:\RSoP_PS.html"
```

Take **Screenshot 7** — `gpresult /r` text output showing Applied GPOs including
TXWES_Domain_Security.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — GPMC installed and GroupPolicy module imported.

**Screenshot 2** — `Get-GPInheritance` showing TXWES_Students_Restrictions linked.

**Screenshot 3** — `Get-ADDefaultDomainPasswordPolicy` showing MinPasswordLength 12.

**Screenshot 4** — HTML GPO report showing student restriction settings.

**Screenshot 5** — TXWES_Kiosk_Policy report showing Loopback Replace mode.

**Screenshot 6** — Kiosks OU inheritance showing Block Inheritance and Enforced GPO.

**Screenshot 7** — `gpresult /r` showing Applied GPOs.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| GPOs created and linked | 15 | Screenshot 2 shows correct GPO links |
| Domain Account Policy | 20 | Screenshot 3 shows length 12 and lockout 5 |
| Student restrictions | 20 | Screenshot 4 shows NoControlPanel and DisableCMD |
| Loopback Replace configured | 20 | Screenshot 5 shows Replace mode in kiosk GPO |
| Enforcement and Block Inheritance | 15 | Screenshot 6 shows both features working |
| RSoP verification | 10 | Screenshot 7 shows applied GPOs |

---

## Troubleshooting Notes

If `New-GPLink` fails with "The specified domain either does not exist or could
not be contacted," verify DNS resolution and that the GroupPolicy module is
imported.

If policy settings do not appear to apply after `gpupdate /force`, check that
the user account being tested is in the correct OU:

```powershell
Get-ADUser -Identity "studentuser" | Select-Object DistinguishedName
```

If `Get-ADDefaultDomainPasswordPolicy` shows default values (length 7) after
setting the policy, verify the domain GPO link is enabled and Enforced:

```powershell
Get-GPInheritance -Target "DC=txwes,DC=edu" |
    Select-Object -ExpandProperty GpoLinks
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Configure and Verify Loopback Processing

Loopback Processing is critical for kiosk and lab computer environments. Configure it and verify its effect on a user logging into a restricted machine.

1. Create a new GPO named `TXWES_Loopback_Test` and enable Loopback Processing in Replace mode:

   ```powershell
   New-GPO -Name "TXWES_Loopback_Test" -Domain "txwes.edu"

   Set-GPRegistryValue -Name "TXWES_Loopback_Test" `
       -Key "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" `
       -ValueName "UserPolicyMode" -Type DWord -Value 2
   ```

   Note: Value 2 = Replace mode, Value 1 = Merge mode. Confirm this by checking the Group Policy Administrative Template path: Computer Configuration > Policies > Administrative Templates > System > Group Policy > "Configure user Group Policy loopback processing mode."

2. Link the GPO to the Kiosks OU:

   ```powershell
   New-GPLink -Name "TXWES_Loopback_Test" `
       -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" `
       -LinkEnabled Yes
   ```

3. Verify the GPO is linked and the registry value is set correctly:

   ```powershell
   Get-GPInheritance -Target "OU=Kiosks,OU=TXWES,DC=txwes,DC=edu" |
       Select-Object -ExpandProperty GpoLinks

   Get-GPRegistryValue -Name "TXWES_Loopback_Test" `
       -Key "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" `
       -ValueName "UserPolicyMode"
   ```

4. In your lab notes, explain the difference between setting `UserPolicyMode = 1` (Merge) versus `UserPolicyMode = 2` (Replace). Describe a real-world scenario where Merge mode would be more appropriate than Replace mode.

### Challenge 2: Identify Unlinked and Empty GPOs

GPO sprawl (unused, unlinked, or empty GPOs) creates confusion and should be cleaned up regularly. Practice identifying them.

1. List all GPOs and check which ones have no links by examining each GPO's XML report:

   ```powershell
   $allGPOs = Get-GPO -All
   foreach ($gpo in $allGPOs) {
       $report = [xml](Get-GPOReport -Guid $gpo.Id -ReportType Xml)
       $links = $report.GPO.LinksTo
       if (-not $links) {
           Write-Host "UNLINKED: $($gpo.DisplayName)" -ForegroundColor Yellow
       }
   }
   ```

2. Identify GPOs that are linked but have "All Settings Disabled" status (they apply to OUs but contain no active settings):

   ```powershell
   Get-GPO -All | Where-Object { $_.GpoStatus -eq "AllSettingsDisabled" } |
       Select-Object DisplayName, GpoStatus, CreationTime
   ```

3. For any GPOs that are both unlinked and empty (no active settings), document in your lab notes: what would be the safe procedure for removing them? Include what verification steps should be performed before deletion, and whether a backup is needed.

4. Generate a complete GPO inventory report for all GPOs in the domain:

   ```powershell
   Get-GPO -All | Select-Object DisplayName, GpoStatus, CreationTime, ModificationTime |
       Sort-Object DisplayName |
       Export-Csv -Path "C:\GPO_Inventory.csv" -NoTypeInformation

   Import-Csv "C:\GPO_Inventory.csv" | Format-Table -AutoSize
   ```

### Reflection Questions

1. Loopback Processing Replace mode discards all of the user's OU policies and substitutes the computer's OU User Configuration. What specific risk does this create for a Domain Admin who logs on to a kiosk computer with Loopback Replace enabled, and how would you mitigate it without disabling Loopback Processing?
2. You discovered several unlinked GPOs in the domain. Before deleting them, what information would you collect, and who in the organization should be consulted? Describe the process for safely retiring an unused GPO in a production environment.
