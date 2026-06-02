# Lab Activity: Module 04 - User, Group, and Computer Accounts in AD

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Lab Overview

In this lab you will create the user and group infrastructure for the `corp.local` domain. You will create department user accounts, role-based Global groups, resource Domain Local groups, and nest them following the AGDLP pattern. You will also create a Managed Service Account. These objects will be used by Group Policy labs in Module 05.

**Estimated Time:** 60-75 minutes

**Prerequisites:**

- Module 03 lab complete: Two-DC `corp.local` domain with OU structure (Departments/HR/IT/Finance, Servers, Workstations)

**Learning Objectives:**

- Create user accounts using both ADUC and PowerShell
- Create Security groups with correct scope
- Nest groups following the AGDLP model
- Create and install a Managed Service Account
- Query and verify AD objects using Get-ADUser, Get-ADGroup, Get-ADGroupMember

---

### Part 1 — Create User Accounts

#### Step 1.1 — Create HR Department Users

Open PowerShell on DC1 (SRV-CORE-01) and run:

```powershell
$pwd = ConvertTo-SecureString "TempP@ss123!" -AsPlainText -Force

# HR Users
New-ADUser -Name "Sarah Connor" -GivenName "Sarah" -Surname "Connor" `
    -SamAccountName "sconnor" -UserPrincipalName "sconnor@corp.local" `
    -Path "OU=HR,OU=Departments,DC=corp,DC=local" `
    -AccountPassword $pwd -Enabled $true -ChangePasswordAtLogon $true

New-ADUser -Name "Michael Scott" -GivenName "Michael" -Surname "Scott" `
    -SamAccountName "mscott" -UserPrincipalName "mscott@corp.local" `
    -Path "OU=HR,OU=Departments,DC=corp,DC=local" `
    -AccountPassword $pwd -Enabled $true -ChangePasswordAtLogon $true
```

#### Step 1.2 — Create IT Department Users

```powershell
# IT Users
New-ADUser -Name "Diana Prince" -GivenName "Diana" -Surname "Prince" `
    -SamAccountName "dprince" -UserPrincipalName "dprince@corp.local" `
    -Path "OU=IT,OU=Departments,DC=corp,DC=local" `
    -AccountPassword $pwd -Enabled $true -ChangePasswordAtLogon $true

New-ADUser -Name "Bruce Wayne" -GivenName "Bruce" -Surname "Wayne" `
    -SamAccountName "bwayne" -UserPrincipalName "bwayne@corp.local" `
    -Path "OU=IT,OU=Departments,DC=corp,DC=local" `
    -AccountPassword $pwd -Enabled $true -ChangePasswordAtLogon $true
```

#### Step 1.3 — Create Finance Department Users

```powershell
# Finance Users
New-ADUser -Name "Tony Stark" -GivenName "Tony" -Surname "Stark" `
    -SamAccountName "tstark" -UserPrincipalName "tstark@corp.local" `
    -Path "OU=Finance,OU=Departments,DC=corp,DC=local" `
    -AccountPassword $pwd -Enabled $true -ChangePasswordAtLogon $true
```

#### Step 1.4 — Verify All Users

```powershell
Get-ADUser -Filter * -SearchBase "OU=Departments,DC=corp,DC=local" |
    Select-Object Name, SamAccountName, DistinguishedName, Enabled
```

Expected output: Five user accounts listed, all Enabled: True.

---

### Part 2 — Create Groups (AGDLP Pattern)

#### Step 2.1 — Create a Groups OU

```powershell
New-ADOrganizationalUnit -Name "Groups" -Path "DC=corp,DC=local" `
    -ProtectedFromAccidentalDeletion $true
```

#### Step 2.2 — Create Global Role Groups

```powershell
# Global groups (role-based)
New-ADGroup -Name "G_HRUsers" -GroupScope Global -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "HR Department Users"

New-ADGroup -Name "G_ITAdmins" -GroupScope Global -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "IT Department Administrators"

New-ADGroup -Name "G_FinanceUsers" -GroupScope Global -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "Finance Department Users"
```

#### Step 2.3 — Create Domain Local Resource Groups

```powershell
# Domain Local groups (resource-based)
New-ADGroup -Name "DL_HRShare_Read" -GroupScope DomainLocal -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "Read access to HR file share"

New-ADGroup -Name "DL_HRShare_Write" -GroupScope DomainLocal -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "Write access to HR file share"

New-ADGroup -Name "DL_FinanceShare_Read" -GroupScope DomainLocal -GroupCategory Security `
    -Path "OU=Groups,DC=corp,DC=local" `
    -Description "Read access to Finance file share"
```

#### Step 2.4 — Add Users to Global Groups

```powershell
# Add HR users to HR Global group
Add-ADGroupMember -Identity "G_HRUsers" -Members "sconnor", "mscott"

# Add IT users to IT Global group
Add-ADGroupMember -Identity "G_ITAdmins" -Members "dprince", "bwayne"

# Add Finance users to Finance Global group
Add-ADGroupMember -Identity "G_FinanceUsers" -Members "tstark"
```

#### Step 2.5 — Nest Global Groups into Domain Local Groups (AGDLP)

```powershell
# HR Read: G_HRUsers gets Read on HR share
Add-ADGroupMember -Identity "DL_HRShare_Read" -Members "G_HRUsers"

# HR Write: only managers — nest G_ITAdmins as example for mixed access
Add-ADGroupMember -Identity "DL_HRShare_Write" -Members "G_ITAdmins"

# Finance Read: G_FinanceUsers
Add-ADGroupMember -Identity "DL_FinanceShare_Read" -Members "G_FinanceUsers"
```

#### Step 2.6 — Verify Group Membership

```powershell
# Verify Global group membership
Get-ADGroupMember -Identity "G_HRUsers" | Select-Object Name, SamAccountName

# Verify Domain Local group shows nested Global group
Get-ADGroupMember -Identity "DL_HRShare_Read" | Select-Object Name, ObjectClass

# Show all groups for a specific user (recursive)
Get-ADPrincipalGroupMembership -Identity "sconnor" |
    Select-Object Name, GroupScope, GroupCategory
```

---

### Part 3 — Account Lifecycle Operations

#### Step 3.1 — Set Account Expiration for a Contractor

```powershell
# Simulate a contractor account expiration
Set-ADAccountExpiration -Identity "tstark" -DateTime "2025-12-31"

# Verify expiration is set
Get-ADUser -Identity "tstark" -Properties AccountExpirationDate |
    Select-Object Name, AccountExpirationDate
```

#### Step 3.2 — Disable and Move a Departing User

```powershell
# Simulate employee departure — disable the account
Disable-ADAccount -Identity "mscott"

# Verify it is disabled
Get-ADUser -Identity "mscott" -Properties Enabled | Select-Object Name, Enabled

# Move to Disabled_Users OU (create OU first)
New-ADOrganizationalUnit -Name "Disabled_Users" -Path "DC=corp,DC=local" `
    -ProtectedFromAccidentalDeletion $false

Move-ADObject `
    -Identity "CN=Michael Scott,OU=HR,OU=Departments,DC=corp,DC=local" `
    -TargetPath "OU=Disabled_Users,DC=corp,DC=local"
```

---

### Part 4 — Managed Service Account

#### Step 4.1 — Create and Install an MSA

```powershell
# Create the MSA in AD
New-ADServiceAccount -Name "SVC_AppService" -RestrictToSingleComputer

# Install it on the local DC (simulating a target server)
Install-ADServiceAccount -Identity "SVC_AppService"

# Verify the MSA exists and is installed
Get-ADServiceAccount -Identity "SVC_AppService" -Properties *
Test-ADServiceAccount -Identity "SVC_AppService"
```

The `Test-ADServiceAccount` command should return `True` if the MSA is correctly installed.

---

### Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1 — All users created:** Output of `Get-ADUser -Filter * -SearchBase "OU=Departments,DC=corp,DC=local"` listing all 5 users.

**Screenshot 2 — AGDLP nesting:** Output of `Get-ADGroupMember -Identity "DL_HRShare_Read"` showing `G_HRUsers` as an ObjectClass: group member.

**Screenshot 3 — User group memberships:** Output of `Get-ADPrincipalGroupMembership -Identity "sconnor"` showing group memberships.

**Screenshot 4 — Disabled user moved:** Output of `Get-ADUser -SearchBase "OU=Disabled_Users,DC=corp,DC=local" -Filter *` showing mscott in the Disabled_Users OU.

**Screenshot 5 — MSA verification:** Output of `Test-ADServiceAccount -Identity "SVC_AppService"` returning True.

---

### Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| All 5 user accounts created in correct OUs | 20 | Get-ADUser output with correct DistinguishedNames |
| All Global and Domain Local groups created | 15 | Get-ADGroup output shows all 6 groups with correct scope |
| AGDLP nesting correct | 25 | DL groups show Global groups as members (ObjectClass: group) |
| Account lifecycle (disable + move) | 20 | mscott disabled and in Disabled_Users OU |
| MSA created and installed | 20 | Test-ADServiceAccount returns True |

---

### Troubleshooting Notes

If `New-ADUser` returns "Access Denied," verify you are logged in as `CORP\Administrator` and the session has the AD module loaded:

```powershell
Import-Module ActiveDirectory
```

If the OU path in `-Path` does not exist, the cmdlet returns "The directory path was not found." Use `Get-ADOrganizationalUnit -Filter *` to verify OU names and DNs before running user creation commands.
