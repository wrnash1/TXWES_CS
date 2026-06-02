# Lab Activity: Module 05 - Group Policy Objects: Creation and Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will create and configure three Group Policy Objects in the `corp.local` domain: a domain-wide security baseline, an IT-department-specific GPO with Security Filtering, and a Loopback Processing GPO for a Kiosk scenario. You will verify each GPO using `gpresult` and the PowerShell GroupPolicy module.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- Module 04 lab complete: User accounts and OU structure exist in corp.local
- Group Policy Management Console accessible from DC1

**Learning Objectives:**

- Create and link GPOs using GPMC and PowerShell
- Configure Security Filtering to target a GPO to a specific group
- Enable Loopback Processing for a kiosk OU
- Use gpresult and gpupdate to verify and troubleshoot GPO application
- Generate an HTML RSoP report

---

### Part 1 — Domain-Wide Password Policy GPO

#### Step 1.1 — Open GPMC

**[SHOW SCREEN: Server Manager — Tools — Group Policy Management]**

On DC1, open Server Manager. Click Tools and select Group Policy Management.

#### Step 1.2 — Create the GPO

In the GPMC tree, right-click Group Policy Objects and select New. Name the GPO `CORP_Domain_Security`. Click OK.

#### Step 1.3 — Edit Password Policy Settings

Right-click `CORP_Domain_Security` and select Edit. Navigate to:

Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Password Policy

Configure:

- Enforce password history: 12 passwords
- Maximum password age: 90 days
- Minimum password age: 1 day
- Minimum password length: 12 characters
- Password must meet complexity requirements: Enabled

Navigate to Account Lockout Policy:

- Account lockout duration: 15 minutes
- Account lockout threshold: 5 invalid logon attempts
- Reset account lockout counter after: 15 minutes

Close the GPME.

#### Step 1.4 — Link to Domain

In the GPMC tree, right-click the domain name `corp.local` and select "Link an Existing GPO." Select `CORP_Domain_Security` and click OK.

#### Step 1.5 — Verify with PowerShell

```powershell
# Confirm the GPO exists
Get-GPO -Name "CORP_Domain_Security"

# Confirm the domain link
Get-GPLink -Target "DC=corp,DC=local" | Where-Object { $_.DisplayName -eq "CORP_Domain_Security" }
```

---

### Part 2 — IT Department Security Baseline GPO with Security Filtering

#### Step 2.1 — Create the GPO

In GPMC, right-click Group Policy Objects, select New, and name it `CORP_IT_Security_Baseline`.

#### Step 2.2 — Configure Settings

Edit the GPO and configure:

Computer Configuration > Policies > Administrative Templates > Control Panel > Personalization:

- Screen saver timeout: Enabled, 600 seconds
- Password protect the screen saver: Enabled

Computer Configuration > Policies > Administrative Templates > System:

- Prevent access to registry editing tools: Enabled (optional — used to demonstrate computer config)

Close the GPME.

#### Step 2.3 — Link to IT OU

Right-click the `IT` OU (under Departments) in the GPMC tree and select "Link an Existing GPO." Select `CORP_IT_Security_Baseline`.

#### Step 2.4 — Configure Security Filtering

Click the linked GPO in the IT OU. Go to the Scope tab. Under Security Filtering:

1. Select "Authenticated Users" and click Remove
2. Click Add. Search for `G_ITAdmins` and click OK

Click the Delegation tab. Click Add. Search for `Domain Computers`. Set permission to Read (do not check Apply Group Policy). Click OK.

This ensures IT Admins receive the policy, while the computer accounts can still read it for Computer Configuration processing.

#### Step 2.5 — Verify Security Filtering

```powershell
# View GPO security settings
Get-GPPermissions -Name "CORP_IT_Security_Baseline" -All
```

---

### Part 3 — Kiosk Loopback Processing GPO

#### Step 3.1 — Create a Kiosk OU

```powershell
New-ADOrganizationalUnit -Name "Kiosks" -Path "DC=corp,DC=local" `
    -ProtectedFromAccidentalDeletion $true
```

#### Step 3.2 — Create the GPO

In GPMC, create a new GPO named `CORP_Kiosk_Restrictions`.

#### Step 3.3 — Enable Loopback Processing

Edit the GPO. Navigate to:

Computer Configuration > Policies > Administrative Templates > System > Group Policy

Double-click "Configure user Group Policy loopback processing mode." Select Enabled. Set Mode to Replace. Click OK.

#### Step 3.4 — Configure Kiosk User Restrictions

Still in the GPO editor, navigate to:

User Configuration > Policies > Administrative Templates > System:

- Don't run specified Windows applications: Enabled — add `taskmgr.exe`, `regedit.exe`

User Configuration > Policies > Administrative Templates > Start Menu and Taskbar:

- Remove Run menu from Start Menu: Enabled

Close the GPME.

#### Step 3.5 — Link to Kiosks OU

Right-click the `Kiosks` OU and link `CORP_Kiosk_Restrictions`. Set the link to Enforced.

---

### Part 4 — Verify GPO Application

#### Step 4.1 — Force Policy Refresh

On DC1 (simulating from the server side since lab VMs may not include joined workstations):

```powershell
gpupdate /force
```

#### Step 4.2 — Run gpresult

```powershell
gpresult /r
```

Review the Applied Group Policy Objects section. The `CORP_Domain_Security` GPO should appear (linked to the domain). Take a screenshot.

#### Step 4.3 — Generate HTML RSoP Report

```powershell
gpresult /h "C:\GPReport_Module05.html"
```

Open the HTML file in a browser. Review all applied policies and verify the password policy settings from Part 1 are visible.

#### Step 4.4 — PowerShell: List All GPOs and Links

```powershell
# List all GPOs with status
Get-GPO -All | Select-Object DisplayName, GpoStatus, ModificationTime | Sort-Object DisplayName

# List all GPO links in the domain
Get-GPInheritance -Target "DC=corp,DC=local" | Select-Object -ExpandProperty GpoLinks

# List GPO links for the IT OU
Get-GPInheritance -Target "OU=IT,OU=Departments,DC=corp,DC=local" |
    Select-Object -ExpandProperty GpoLinks
```

---

### Part 5 — Optional Challenge: Test Block Inheritance

Create a test OU named `TestNoInheritance` and apply Block Inheritance.

```powershell
New-ADOrganizationalUnit -Name "TestNoInheritance" -Path "DC=corp,DC=local"
```

In GPMC, right-click `TestNoInheritance` and select Block Inheritance. Verify in GPMC that the domain-level GPO no longer appears as inherited in that OU.

Then set the `CORP_Domain_Security` GPO link at the domain level to Enforced. Re-check the `TestNoInheritance` OU — the Enforced GPO should now appear despite Block Inheritance.

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — GPMC overview:** GPMC showing all three GPOs (CORP_Domain_Security, CORP_IT_Security_Baseline, CORP_Kiosk_Restrictions) in the Group Policy Objects container.

**Screenshot 2 — Domain GPO linked:** GPMC showing corp.local domain with CORP_Domain_Security linked.

**Screenshot 3 — IT GPO Security Filtering:** GPMC Scope tab showing G_ITAdmins in the Security Filtering section for CORP_IT_Security_Baseline.

**Screenshot 4 — gpresult /r output:** Output showing Applied Group Policy Objects including at least one of your created GPOs.

**Screenshot 5 — GPO PowerShell list:** Output of `Get-GPO -All` showing all three GPOs with status.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| CORP_Domain_Security created and linked to domain | 20 | GPMC screenshot shows domain link |
| Password Policy settings configured correctly | 15 | GPO report shows configured values |
| CORP_IT_Security_Baseline with Security Filtering | 25 | Scope tab shows G_ITAdmins in filtering |
| CORP_Kiosk_Restrictions with Loopback Replace | 20 | GPO editor shows Loopback: Replace setting |
| gpresult /r screenshot confirming application | 20 | Applied GPOs section includes created GPO |

---

### Troubleshooting Notes

If a GPO appears in "Denied GPOs" with reason "Inaccessible," verify that Domain Computers has Read permission in the GPO's Delegation tab.

If `Get-GPLink` returns no results, verify the GroupPolicy PowerShell module is loaded:

```powershell
Import-Module GroupPolicy
```

If `gpupdate /force` says "User Policy could not be updated successfully," verify the user account running the command has the AD module available and is domain-joined.
