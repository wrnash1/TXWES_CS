# Lab Activity: Module 07 — Active Directory User and Group Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will build a complete Active Directory user and group management
environment on DC1. You will create an OU hierarchy, provision individual and
bulk users from a CSV file, create Security groups with correct scopes, implement
AGDLP nesting, and practice account lifecycle operations.

**Estimated Time:** 75-90 minutes

**Prerequisites:**

- DC1 is running Windows Server 2022 and is a domain controller for txwes.edu

- You are logged in as a Domain Administrator

- PowerShell console is open with Administrator privileges

**Learning Objectives:**

- Create a multi-level OU structure using `New-ADOrganizationalUnit`

- Provision user accounts with `New-ADUser` including all required attributes

- Create Security groups with correct scopes using `New-ADGroup`

- Implement the AGDLP nesting pattern with `Add-ADGroupMember`

- Bulk-provision users from a CSV file using `Import-Csv`

- Perform account lifecycle operations: disable, unlock, reset password, move

---

## Part 1 — Build the OU Structure

### Step 1.1 — Create the Root and Department OUs

```powershell
# Create root OU with accidental deletion protection
New-ADOrganizationalUnit `
    -Name "TXWES" `
    -Path "DC=txwes,DC=edu" `
    -ProtectedFromAccidentalDeletion $true

# Create department OUs
$root = "OU=TXWES,DC=txwes,DC=edu"

foreach ($dept in @("IT","Faculty","Students","ServiceAccounts")) {
    New-ADOrganizationalUnit `
        -Name $dept `
        -Path $root `
        -ProtectedFromAccidentalDeletion $true
}

# Create sub-OUs under IT
$itPath = "OU=IT,OU=TXWES,DC=txwes,DC=edu"

foreach ($sub in @("Admins","Helpdesk")) {
    New-ADOrganizationalUnit `
        -Name $sub `
        -Path $itPath `
        -ProtectedFromAccidentalDeletion $true
}
```

### Step 1.2 — Verify the OU Structure

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" |
    Select-Object Name, DistinguishedName |
    Sort-Object DistinguishedName
```

The output should show all 7 OUs: TXWES root, IT, Admins, Helpdesk, Faculty,
Students, and ServiceAccounts.

Take **Screenshot 1** — `Get-ADOrganizationalUnit` output showing all 7 OUs.

---

## Part 2 — Create Individual User Accounts

### Step 2.1 — Create Three Individual Users

```powershell
# User 1 — IT Admin
New-ADUser `
    -Name               "Jane Smith" `
    -GivenName          "Jane" `
    -Surname            "Smith" `
    -SamAccountName     "jsmith" `
    -UserPrincipalName  "jsmith@txwes.edu" `
    -DisplayName        "Jane Smith" `
    -Department         "IT" `
    -Title              "Systems Administrator" `
    -Path               "OU=Admins,OU=IT,OU=TXWES,DC=txwes,DC=edu" `
    -AccountPassword    (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force) `
    -ChangePasswordAtLogon $true `
    -Enabled            $true

# User 2 — Helpdesk Technician
New-ADUser `
    -Name               "Tom Rivera" `
    -GivenName          "Tom" `
    -Surname            "Rivera" `
    -SamAccountName     "trivera" `
    -UserPrincipalName  "trivera@txwes.edu" `
    -DisplayName        "Tom Rivera" `
    -Department         "IT" `
    -Title              "Help Desk Technician" `
    -Path               "OU=Helpdesk,OU=IT,OU=TXWES,DC=txwes,DC=edu" `
    -AccountPassword    (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force) `
    -ChangePasswordAtLogon $true `
    -Enabled            $true

# User 3 — Faculty Member
New-ADUser `
    -Name               "Dr. Patricia Lee" `
    -GivenName          "Patricia" `
    -Surname            "Lee" `
    -SamAccountName     "plee" `
    -UserPrincipalName  "plee@txwes.edu" `
    -DisplayName        "Dr. Patricia Lee" `
    -Department         "Faculty" `
    -Title              "Associate Professor" `
    -Path               "OU=Faculty,OU=TXWES,DC=txwes,DC=edu" `
    -AccountPassword    (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force) `
    -ChangePasswordAtLogon $true `
    -Enabled            $true
```

### Step 2.2 — Verify the Users

```powershell
Get-ADUser -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" `
    -Properties Department, Title |
    Select-Object Name, SamAccountName, Department, Title, Enabled |
    Sort-Object Department
```

Take **Screenshot 2** — All three user accounts listed with correct Department
and Enabled status.

---

## Part 3 — Create Security Groups and Implement AGDLP

### Step 3.1 — Create the Groups

```powershell
$groupOU = "OU=IT,OU=TXWES,DC=txwes,DC=edu"

# Global group — role-based
New-ADGroup `
    -Name          "G_IT_Admins" `
    -GroupScope    Global `
    -GroupCategory Security `
    -Description   "IT Administrators — role-based global group" `
    -Path          $groupOU

# Global group — helpdesk role
New-ADGroup `
    -Name          "G_IT_Helpdesk" `
    -GroupScope    Global `
    -GroupCategory Security `
    -Description   "IT Helpdesk staff — role-based global group" `
    -Path          $groupOU

# Domain Local group — holds the file share permission
New-ADGroup `
    -Name          "DL_ITShare_FullControl" `
    -GroupScope    DomainLocal `
    -GroupCategory Security `
    -Description   "IT share — Full Control permission holder" `
    -Path          $groupOU
```

### Step 3.2 — Implement AGDLP Nesting

```powershell
# Add users to their role-based Global groups
Add-ADGroupMember -Identity "G_IT_Admins"   -Members "jsmith"
Add-ADGroupMember -Identity "G_IT_Helpdesk" -Members "trivera"

# Nest both Global groups into the Domain Local group
Add-ADGroupMember -Identity "DL_ITShare_FullControl" -Members "G_IT_Admins","G_IT_Helpdesk"
```

### Step 3.3 — Verify the AGDLP Chain

```powershell
Write-Host "=== G_IT_Admins members ===" -ForegroundColor Cyan
Get-ADGroupMember -Identity "G_IT_Admins" | Select-Object Name, objectClass

Write-Host "=== DL_ITShare_FullControl members (including nested) ===" -ForegroundColor Cyan
Get-ADGroupMember -Identity "DL_ITShare_FullControl" -Recursive |
    Select-Object Name, objectClass
```

Take **Screenshot 3** — Output showing jsmith inside G_IT_Admins, and both
jsmith and trivera appearing when DL_ITShare_FullControl is queried recursively.

---

## Part 4 — Bulk Provisioning from CSV

### Step 4.1 — Create the CSV File

```powershell
# Create a sample CSV file for bulk provisioning
$csvContent = @"
FirstName,LastName,Department,Title,OU
Alice,Johnson,Faculty,Professor,OU=Faculty,OU=TXWES,DC=txwes,DC=edu
Bob,Williams,IT,Help Desk Tech,OU=Helpdesk,OU=IT,OU=TXWES,DC=txwes,DC=edu
Carol,Brown,Students,Student,OU=Students,OU=TXWES,DC=txwes,DC=edu
David,Garcia,Faculty,Lecturer,OU=Faculty,OU=TXWES,DC=txwes,DC=edu
Emma,Davis,Students,Student,OU=Students,OU=TXWES,DC=txwes,DC=edu
"@

$csvContent | Out-File -FilePath "C:\Scripts\new_users.csv" -Encoding UTF8
```

### Step 4.2 — Run the Bulk Provisioning Script

```powershell
# Ensure the Scripts directory exists
New-Item -Path "C:\Scripts" -ItemType Directory -Force | Out-Null

# Import and provision
$users = Import-Csv -Path "C:\Scripts\new_users.csv"

foreach ($user in $users) {
    $sam = ($user.FirstName.Substring(0,1) + $user.LastName).ToLower()
    $upn = "$sam@txwes.edu"

    New-ADUser `
        -Name               "$($user.FirstName) $($user.LastName)" `
        -GivenName          $user.FirstName `
        -Surname            $user.LastName `
        -SamAccountName     $sam `
        -UserPrincipalName  $upn `
        -DisplayName        "$($user.FirstName) $($user.LastName)" `
        -Department         $user.Department `
        -Title              $user.Title `
        -Path               $user.OU `
        -AccountPassword    (ConvertTo-SecureString "Welcome1!" -AsPlainText -Force) `
        -ChangePasswordAtLogon $true `
        -Enabled            $true

    Write-Host "Created: $sam" -ForegroundColor Green
}

# Verify all users
Get-ADUser -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" `
    -Properties Department |
    Select-Object Name, SamAccountName, Department | Sort-Object Department
```

Take **Screenshot 4** — All 8 user accounts (3 from Part 2 + 5 from CSV) listed
with correct department assignments.

---

## Part 5 — Account Lifecycle Operations

### Step 5.1 — Disable and Re-Enable an Account

```powershell
# Disable trivera (simulating a leave of absence)
Disable-ADAccount -Identity "trivera"

# Verify
Get-ADUser -Identity "trivera" | Select-Object Name, Enabled

# Re-enable
Enable-ADAccount -Identity "trivera"
Get-ADUser -Identity "trivera" | Select-Object Name, Enabled
```

### Step 5.2 — Simulate and Unlock a Locked Account

```powershell
# Check lockout status before
Get-ADUser -Identity "jsmith" -Properties LockedOut, BadLogonCount |
    Select-Object Name, LockedOut, BadLogonCount

# Unlock the account (use this after a real lockout occurs in your lab)
Unlock-ADAccount -Identity "jsmith"

# Verify unlock
Get-ADUser -Identity "jsmith" -Properties LockedOut |
    Select-Object Name, LockedOut
```

### Step 5.3 — Reset a Password

```powershell
# Reset password and force change at next logon
Set-ADAccountPassword -Identity "plee" `
    -NewPassword (ConvertTo-SecureString "Faculty2024!" -AsPlainText -Force) `
    -Reset

Set-ADUser -Identity "plee" -ChangePasswordAtLogon $true

# Verify the flag is set
Get-ADUser -Identity "plee" -Properties PasswordExpired, PasswordLastSet |
    Select-Object Name, PasswordExpired, PasswordLastSet
```

### Step 5.4 — Move an Account to a Different OU

```powershell
# Move trivera from Helpdesk to Admins (simulating a promotion)
$triveraDN = (Get-ADUser -Identity "trivera").DistinguishedName

Move-ADObject `
    -Identity   $triveraDN `
    -TargetPath "OU=Admins,OU=IT,OU=TXWES,DC=txwes,DC=edu"

# Verify new location
Get-ADUser -Identity "trivera" | Select-Object Name, DistinguishedName
```

Take **Screenshot 5** — trivera's DistinguishedName showing the Admins OU path.

---

## Part 6 — Audit and Search Operations

```powershell
# Find all disabled accounts in the domain
Write-Host "=== Disabled Accounts ===" -ForegroundColor Cyan
Search-ADAccount -AccountDisabled -SearchBase "OU=TXWES,DC=txwes,DC=edu" |
    Select-Object Name, SamAccountName

# Find all locked accounts
Write-Host "=== Locked Accounts ===" -ForegroundColor Cyan
Search-ADAccount -LockedOut |
    Select-Object Name, SamAccountName

# List all groups a user belongs to
Write-Host "=== Groups for jsmith ===" -ForegroundColor Cyan
Get-ADPrincipalGroupMembership -Identity "jsmith" |
    Select-Object Name, GroupScope, GroupCategory
```

Take **Screenshot 6** — `Get-ADPrincipalGroupMembership` output for jsmith
showing G_IT_Admins and DL_ITShare_FullControl memberships.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — OU structure: `Get-ADOrganizationalUnit` showing all 7 OUs.

**Screenshot 2** — Individual users: three accounts with correct Department and
Enabled status.

**Screenshot 3** — AGDLP chain: G_IT_Admins and DL_ITShare_FullControl recursive
membership output.

**Screenshot 4** — Bulk provisioning: all 8 accounts listed with correct
departments.

**Screenshot 5** — Account move: trivera's DistinguishedName in the Admins OU.

**Screenshot 6** — Group audit: jsmith's group membership output.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| OU structure created | 15 | Screenshot 1 shows all 7 OUs |
| Individual users created | 15 | Screenshot 2 shows 3 users with correct attributes |
| AGDLP groups configured | 25 | Screenshot 3 shows correct nesting and recursive membership |
| Bulk provisioning completed | 20 | Screenshot 4 shows all 8 users in correct OUs |
| Account lifecycle operations | 15 | Screenshot 5 shows account move to correct OU |
| Audit and search | 10 | Screenshot 6 shows jsmith group membership |

---

## Troubleshooting Notes

If `New-ADOrganizationalUnit` fails with "An object with this name already
exists," the OU was created in a previous attempt. Use `Get-ADOrganizationalUnit
-Filter *` to verify and skip creating existing OUs.

If `New-ADUser` fails with "The object name is too long," the `-Name` parameter
is too long for the CN attribute. Use only First and Last name — do not include
titles or prefixes in the `-Name` parameter.

If `Move-ADObject` fails with "Access is denied," the target OU has
`ProtectedFromAccidentalDeletion` enabled and your account lacks the correct
delegation. Run the command as Domain Admin or check OU permissions in ADUC.

```powershell
# Check if an OU has deletion protection enabled
Get-ADOrganizationalUnit -Identity "OU=IT,OU=TXWES,DC=txwes,DC=edu" |
    Select-Object Name, ProtectedFromAccidentalDeletion
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Enable and Test the Active Directory Recycle Bin

The AD Recycle Bin is the safest recovery mechanism for accidentally deleted objects. Enable it and practice the restore workflow.

1. Enable the AD Recycle Bin for the forest (requires Windows Server 2008 R2 or higher forest functional level):

   ```powershell
   Enable-ADOptionalFeature -Identity "Recycle Bin Feature" `
       -Scope ForestOrConfigurationSet `
       -Target "txwes.edu" `
       -Confirm:$false
   ```

2. Verify the Recycle Bin is enabled:

   ```powershell
   Get-ADOptionalFeature -Filter {Name -like "*Recycle*"} |
       Select-Object Name, EnabledScopes
   ```

3. Create a test user, then delete them:

   ```powershell
   New-ADUser -Name "Temp DeleteMe" -SamAccountName "tdeleteme" `
       -UserPrincipalName "tdeleteme@txwes.edu" `
       -Path "OU=Students,OU=TXWES,DC=txwes,DC=edu" `
       -Enabled $true `
       -AccountPassword (ConvertTo-SecureString "Temp123!" -AsPlainText -Force)

   Remove-ADUser -Identity "tdeleteme" -Confirm:$false
   ```

4. Restore the deleted user from the Recycle Bin:

   ```powershell
   Get-ADObject -Filter {SamAccountName -eq "tdeleteme"} `
       -IncludeDeletedObjects |
       Restore-ADObject

   # Verify the account is back
   Get-ADUser -Identity "tdeleteme" | Select-Object Name, Enabled, DistinguishedName
   ```

   Take a screenshot showing the restored user's DistinguishedName in the original OU.

### Challenge 2: Audit Stale User Accounts and Generate a Report

Stale user accounts (never logged on, or inactive for over 90 days) are a security risk. Automate the identification and reporting process.

1. Find all user accounts in the TXWES OU that have never logged on (LastLogonDate is null):

   ```powershell
   Get-ADUser -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" `
       -Properties LastLogonDate, WhenCreated |
       Where-Object { -not $_.LastLogonDate } |
       Select-Object Name, SamAccountName, WhenCreated |
       Sort-Object WhenCreated |
       Format-Table -AutoSize
   ```

2. Find all user accounts that have not logged on in the last 90 days (accounts with a LastLogonDate older than 90 days):

   ```powershell
   $cutoff = (Get-Date).AddDays(-90)
   Get-ADUser -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" `
       -Properties LastLogonDate |
       Where-Object { $_.LastLogonDate -lt $cutoff -and $_.LastLogonDate -ne $null } |
       Select-Object Name, SamAccountName, LastLogonDate |
       Sort-Object LastLogonDate |
       Export-Csv -Path "C:\stale_accounts.csv" -NoTypeInformation
   ```

3. View the exported report:

   ```powershell
   Import-Csv -Path "C:\stale_accounts.csv" | Format-Table -AutoSize
   ```

4. In your lab notes, write a one-paragraph policy recommendation: at what inactivity threshold should accounts be automatically disabled versus deleted, and what approval process should be required before deletion?

### Reflection Questions

1. The Recycle Bin restore returned the account to its original OU. Explain what would have happened to the account's NTFS permissions and group memberships if the AD Recycle Bin had NOT been enabled at the time of deletion.
2. Your stale account report identified accounts that have never logged on. List two legitimate reasons a user account might exist in Active Directory but have a null `LastLogonDate`, and explain how an administrator would distinguish these accounts from genuinely abandoned ones before disabling them.
