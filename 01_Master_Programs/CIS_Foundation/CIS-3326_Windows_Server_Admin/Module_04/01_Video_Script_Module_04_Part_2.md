# Video Script: Module 04 - User, Group, and Computer Accounts in AD (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University

---

**Recorded by:** Professor Nash | Texas Wesleyan University

**Module:** 04 - User, Group, and Computer Accounts in AD

**Part:** 2 of 2 — Demonstrations, PowerShell Commands, Exam Tips, and Lab Preview

**Estimated Duration:** 11 minutes

**Certification Alignment:** AZ-800 (Administering Windows Server Hybrid Core Infrastructure)

---

### [SEGMENT 1 — Recap and Demo Overview]

Welcome back to Module 04. In Part 1 we covered user account properties, the four group scopes, group types, AGDLP nesting, computer accounts and the secure channel, and service accounts. In Part 2 I am going to demonstrate creating users, groups, and computer accounts using both Active Directory Users and Computers and PowerShell.

---

### [SEGMENT 2 — Demo: Create User Accounts with PowerShell]

**[SHOW SCREEN: PowerShell console on the Domain Controller]**

[Alt-text: PowerShell console showing New-ADUser commands and output.]

```powershell
# Create a single user account
New-ADUser `
    -Name "Jane Smith" `
    -GivenName "Jane" `
    -Surname "Smith" `
    -SamAccountName "jsmith" `
    -UserPrincipalName "jsmith@corp.local" `
    -Path "OU=HR,OU=Departments,DC=corp,DC=local" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force) `
    -Enabled $true `
    -ChangePasswordAtLogon $true

# Verify account was created
Get-ADUser -Identity "jsmith" -Properties *
```

Key parameters: `-Name` is the display name. `-SamAccountName` is the legacy login name. `-UserPrincipalName` is the UPN (modern login format). `-Path` places the account in the correct OU. `-ChangePasswordAtLogon $true` forces a password change at first login — always use this for new accounts.

---

### [SEGMENT 3 — Demo: Bulk User Creation]

**[SHOW SCREEN: PowerShell showing an array-based bulk user creation loop]**

[Alt-text: PowerShell console showing a foreach loop creating multiple user accounts from an array.]

For large deployments, you would use a CSV file. Here is a simplified inline example:

```powershell
$users = @(
    @{Name="Alice Brown"; Sam="abrown"; OU="IT"},
    @{Name="Bob Davis";   Sam="bdavis"; OU="Finance"},
    @{Name="Carol Evans"; Sam="cevans"; OU="HR"}
)

$pwd = ConvertTo-SecureString "TempP@ss123!" -AsPlainText -Force

foreach ($u in $users) {
    New-ADUser `
        -Name $u.Name `
        -SamAccountName $u.Sam `
        -UserPrincipalName "$($u.Sam)@corp.local" `
        -Path "OU=$($u.OU),OU=Departments,DC=corp,DC=local" `
        -AccountPassword $pwd `
        -Enabled $true `
        -ChangePasswordAtLogon $true
    Write-Host "Created: $($u.Name)"
}

# Verify all three accounts
Get-ADUser -Filter * -SearchBase "OU=Departments,DC=corp,DC=local" |
    Select-Object Name, SamAccountName, Enabled
```

---

### [SEGMENT 4 — Demo: Create and Nest Groups]

**[SHOW SCREEN: PowerShell showing New-ADGroup and Add-ADGroupMember commands]**

[Alt-text: PowerShell console showing group creation and membership commands with output confirming groups are created.]

```powershell
# Create Global groups for roles
New-ADGroup -Name "G_HRUsers" -GroupScope Global -GroupCategory Security `
    -Path "OU=HR,OU=Departments,DC=corp,DC=local"

New-ADGroup -Name "G_ITAdmins" -GroupScope Global -GroupCategory Security `
    -Path "OU=IT,OU=Departments,DC=corp,DC=local"

# Create Domain Local groups for resource access
New-ADGroup -Name "DL_HR_FileShare_Read" -GroupScope DomainLocal `
    -GroupCategory Security -Path "OU=Groups,DC=corp,DC=local"

New-ADGroup -Name "DL_HR_FileShare_Write" -GroupScope DomainLocal `
    -GroupCategory Security -Path "OU=Groups,DC=corp,DC=local"

# Add user to Global group
Add-ADGroupMember -Identity "G_HRUsers" -Members "jsmith", "cevans"

# Nest Global group into Domain Local group (AGDLP)
Add-ADGroupMember -Identity "DL_HR_FileShare_Read" -Members "G_HRUsers"

# Verify membership
Get-ADGroupMember -Identity "G_HRUsers" | Select-Object Name, SamAccountName
Get-ADGroupMember -Identity "DL_HR_FileShare_Read" | Select-Object Name, ObjectClass
```

Notice the last command: `DL_HR_FileShare_Read` shows one member: the `G_HRUsers` group. That group in turn contains Jane Smith and Carol Evans. This is the AGDLP pattern — users flow through group nesting, not direct assignment.

---

### [SEGMENT 5 — Demo: Computer Accounts]

**[SHOW SCREEN: ADUC showing Computers container and computer properties]**

[Alt-text: Active Directory Users and Computers showing a computer object in the IT OU with properties panel showing Operating System and DNS Hostname fields.]

Computer accounts are created automatically when a computer joins the domain. But you can also pre-stage them.

```powershell
# Pre-stage a computer account in a specific OU
New-ADComputer -Name "WS-IT-001" `
    -Path "OU=Workstations,DC=corp,DC=local" `
    -Enabled $true

# Query all computer accounts
Get-ADComputer -Filter * | Select-Object Name, DistinguishedName, Enabled

# Find stale computers (not logged in for 90+ days)
$staleDate = (Get-Date).AddDays(-90)
Get-ADComputer -Filter {LastLogonDate -lt $staleDate} `
    -Properties LastLogonDate | Select-Object Name, LastLogonDate

# Reset a stale computer secure channel (run on the affected machine)
Test-ComputerSecureChannel -Repair -Credential (Get-Credential "CORP\Administrator")
```

---

### [SEGMENT 6 — Demo: Account Properties and Lifecycle]

**[SHOW SCREEN: PowerShell showing Get-ADUser and Set-ADUser commands]**

[Alt-text: PowerShell console showing user property queries and modification commands.]

```powershell
# Query a specific user with all properties
Get-ADUser -Identity "jsmith" -Properties *

# Set account expiration date (for contractors)
Set-ADAccountExpiration -Identity "jsmith" -DateTime "2025-12-31"

# Disable an account (departing employee)
Disable-ADAccount -Identity "jsmith"

# Move disabled account to a holding OU
Move-ADObject -Identity "CN=Jane Smith,OU=HR,OU=Departments,DC=corp,DC=local" `
    -TargetPath "OU=Disabled_Users,DC=corp,DC=local"

# Unlock a locked-out account
Unlock-ADAccount -Identity "jsmith"

# Find all locked-out accounts
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName

# Find all disabled accounts
Search-ADAccount -AccountDisabled | Select-Object Name, SamAccountName
```

---

### [SEGMENT 7 — Demo: Group Management Queries]

**[SHOW SCREEN: PowerShell showing group membership queries]**

[Alt-text: PowerShell console showing Get-ADGroupMember and Get-ADPrincipalGroupMembership output.]

```powershell
# List all members of a group (recursive — includes nested members)
Get-ADGroupMember -Identity "G_HRUsers" -Recursive |
    Select-Object Name, SamAccountName, ObjectClass

# List all groups a user belongs to
Get-ADPrincipalGroupMembership -Identity "jsmith" |
    Select-Object Name, GroupScope, GroupCategory

# Find all empty groups
Get-ADGroup -Filter * | Where-Object {
    (Get-ADGroupMember -Identity $_.SamAccountName).Count -eq 0
} | Select-Object Name, GroupScope
```

---

### [SEGMENT 8 — Exam Tips]

**[SHOW SCREEN: Exam tips slide for Module 04]**

**Exam Tip 1:** Know all four group scopes and their membership and permission-assignment rules. Domain Local can receive members from any domain but can only assign permissions within its own domain. Global can only receive members from its own domain but can assign permissions anywhere. Universal can do both — at the cost of GC replication.

**Exam Tip 2:** AGDLP is the answer whenever a scenario asks for a scalable, maintainable permission assignment strategy. The key nesting order: Accounts inside Global groups, Global groups inside Domain Local groups, permissions assigned to Domain Local groups.

**Exam Tip 3:** The `Test-ComputerSecureChannel -Repair` command is the non-destructive fix for "trust relationship failed" errors. It does not change the computer's SID. Rejoining the domain does change the SID and is the disruptive alternative.

**Exam Tip 4:** MSA for single-server service accounts. gMSA for multi-server or load-balanced services. Both rotate passwords automatically. Neither requires a KDS root key for MSA; gMSA requires a KDS root key (`Add-KdsRootKey`).

**Exam Tip 5:** Disable, do not delete, departing employee accounts. Deletion is permanent (without Recycle Bin), loses the SID, and removes resource permission assignments. Disabling preserves everything.

**Exam Tip 6:** `Search-ADAccount -LockedOut` and `Search-ADAccount -AccountDisabled` are the quick commands for finding accounts in those states. Know these for exam troubleshooting scenarios.

---

### [SEGMENT 9 — Lab Preview]

**[SHOW SCREEN: Lab 04 instructions document]**

This week's lab has you creating a department user structure in the `corp.local` domain. You will create user accounts for HR, IT, and Finance departments using both ADUC and PowerShell, create Global and Domain Local groups following AGDLP, and nest the groups correctly. You will also create a Managed Service Account and verify it can be installed on the DC.

Deliverables include screenshots of `Get-ADUser -Filter *` listing your created accounts, `Get-ADGroupMember` showing nested group membership, and `Get-ADServiceAccount` confirming the MSA exists.

---

### [SEGMENT 10 — Module 04 Summary]

**[SHOW SCREEN: Summary slide]**

Module 04 covers the three foundational AD object types. User accounts have rich properties including expiration, logon hours, and lockout state. Groups have two dimensions — type and scope — with AGDLP as the best-practice nesting pattern. Computer accounts have machine passwords and can develop stale secure channels. Managed and Group Managed Service Accounts provide automatic password rotation for service identities.

Module 05 brings these objects together with Group Policy — the mechanism for enforcing settings across all of them. See you there.

---

### Additional Resources

- [ActiveDirectory PowerShell module reference](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)
- [Understanding AD security groups](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups)
- [Group Managed Service Accounts overview](https://learn.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/group-managed-service-accounts-overview)
- [Test-ComputerSecureChannel reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/test-computersecurechannel)

---

*End of Part 2. Proceed to the Reading Guide, Lab, Quiz, and Discussion for Module 04.*
