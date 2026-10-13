# Video Script: Module 07 — Active Directory User and Group Management (Part 2 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back. I am Professor Nash.

In Part 1 we covered OU structure design, user account fundamentals, group types
and scopes, the AGDLP nesting strategy, and bulk provisioning concepts.

In Part 2 we put all of that to work. We will build an OU structure, create
users and groups using both the GUI and PowerShell, run a bulk provisioning
script from a CSV file, and practice account management tasks including disabling,
unlocking, and moving accounts.

Let us get started.

---

## Section 1: Building the OU Structure with PowerShell

The first step in any new AD environment is building the OU hierarchy. Open
PowerShell as a Domain Administrator.

```powershell
# Create the root OU
New-ADOrganizationalUnit -Name "TXWES" -Path "DC=txwes,DC=edu" `
    -ProtectedFromAccidentalDeletion $true

# Create department OUs under TXWES
$rootPath = "OU=TXWES,DC=txwes,DC=edu"

New-ADOrganizationalUnit -Name "IT"             -Path $rootPath -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "Faculty"        -Path $rootPath -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "Students"       -Path $rootPath -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "ServiceAccounts"-Path $rootPath -ProtectedFromAccidentalDeletion $true

# Create sub-OUs under IT
$itPath = "OU=IT,OU=TXWES,DC=txwes,DC=edu"
New-ADOrganizationalUnit -Name "Admins"   -Path $itPath -ProtectedFromAccidentalDeletion $true
New-ADOrganizationalUnit -Name "Helpdesk" -Path $itPath -ProtectedFromAccidentalDeletion $true

# Verify the OU structure
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName | Sort-Object DistinguishedName
```

The `-ProtectedFromAccidentalDeletion $true` flag prevents an administrator from
accidentally deleting an OU with a simple `Remove-ADOrganizationalUnit` call.
This is a best practice for any production OU.

---

## Section 2: Creating Individual Users with New-ADUser

Now let us create a user account with the attributes we discussed in Part 1.

```powershell
# Create a single user account
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

# Verify the user was created
Get-ADUser -Identity "jsmith" -Properties Department, Title, UserPrincipalName |
    Select-Object Name, SamAccountName, UserPrincipalName, Department, Title, Enabled
```

Notice `-ChangePasswordAtLogon $true`. This is a best practice for new accounts
— force users to set their own password on first login so IT never retains their
credentials.

---

## Section 3: Creating Groups with New-ADGroup

Next, create the security groups we need for AGDLP access management.

```powershell
$groupBase = "OU=IT,OU=TXWES,DC=txwes,DC=edu"

# Create a Global security group for IT Admins role
New-ADGroup `
    -Name          "G_IT_Admins" `
    -GroupScope    Global `
    -GroupCategory Security `
    -Description   "IT Administrators — role-based global group" `
    -Path          $groupBase

# Create a Domain Local security group for file share permissions
New-ADGroup `
    -Name          "DL_ITShare_FullControl" `
    -GroupScope    DomainLocal `
    -GroupCategory Security `
    -Description   "IT file share — Full Control permission holder" `
    -Path          $groupBase

# Add jsmith to the Global group
Add-ADGroupMember -Identity "G_IT_Admins" -Members "jsmith"

# Nest the Global group inside the Domain Local group (AGDLP pattern)
Add-ADGroupMember -Identity "DL_ITShare_FullControl" -Members "G_IT_Admins"

# Verify group membership
Get-ADGroupMember -Identity "G_IT_Admins"   | Select-Object Name, objectClass
Get-ADGroupMember -Identity "DL_ITShare_FullControl" | Select-Object Name, objectClass
```

Note the `-GroupScope` and `-GroupCategory` parameters. Missing either one
creates the wrong type of group. The exam tests these parameters specifically.

---

## Section 4: Bulk Provisioning from a CSV File

This is where PowerShell really shines. In a real environment you might receive
an HR export with 300 new employees. Here is how to handle it.

First, imagine a CSV file named `new_users.csv` with these columns:

```text
FirstName,LastName,Department,OU
Alice,Johnson,Faculty,OU=Faculty,OU=TXWES,DC=txwes,DC=edu
Bob,Williams,IT,OU=Helpdesk,OU=IT,OU=TXWES,DC=txwes,DC=edu
Carol,Brown,Students,OU=Students,OU=TXWES,DC=txwes,DC=edu
```

Now the PowerShell import loop:

```powershell
# Import users from CSV
$users = Import-Csv -Path "C:\Scripts\new_users.csv"

foreach ($user in $users) {
    # Build the sAMAccountName: first initial + last name, lowercase
    $sam = ($user.FirstName.Substring(0,1) + $user.LastName).ToLower()
    $upn = "$sam@txwes.edu"

    # Create the user
    New-ADUser `
        -Name              "$($user.FirstName) $($user.LastName)" `
        -GivenName         $user.FirstName `
        -Surname           $user.LastName `
        -SamAccountName    $sam `
        -UserPrincipalName $upn `
        -DisplayName       "$($user.FirstName) $($user.LastName)" `
        -Department        $user.Department `
        -Path              $user.OU `
        -AccountPassword   (ConvertTo-SecureString "Welcome1!" -AsPlainText -Force) `
        -ChangePasswordAtLogon $true `
        -Enabled           $true

    Write-Host "Created: $sam in $($user.OU)" -ForegroundColor Green
}

# Verify all users were created
Get-ADUser -Filter * -SearchBase "OU=TXWES,DC=txwes,DC=edu" |
    Select-Object Name, SamAccountName, Enabled
```

This loop creates every user in the CSV in seconds. In a real migration, the CSV
might come from your HR system with 2,000 rows — the same script handles it
without modification.

---

## Section 5: Account Management Operations

Let us walk through the most common account management tasks.

```powershell
# ── Disable an account ──────────────────────────────────────────────
Disable-ADAccount -Identity "jsmith"
# Verify
Get-ADUser -Identity "jsmith" | Select-Object Name, Enabled

# ── Re-enable an account ────────────────────────────────────────────
Enable-ADAccount -Identity "jsmith"

# ── Unlock a locked account ─────────────────────────────────────────
Unlock-ADAccount -Identity "jsmith"
# Check lockout status
Get-ADUser -Identity "jsmith" -Properties LockedOut, BadLogonCount |
    Select-Object Name, LockedOut, BadLogonCount

# ── Reset a password ────────────────────────────────────────────────
Set-ADAccountPassword -Identity "jsmith" `
    -NewPassword (ConvertTo-SecureString "NewP@ss456!" -AsPlainText -Force) `
    -Reset
Set-ADUser -Identity "jsmith" -ChangePasswordAtLogon $true

# ── Move a user to a different OU ───────────────────────────────────
Move-ADObject `
    -Identity "CN=Jane Smith,OU=Admins,OU=IT,OU=TXWES,DC=txwes,DC=edu" `
    -TargetPath "OU=Helpdesk,OU=IT,OU=TXWES,DC=txwes,DC=edu"

# ── Find all disabled accounts ──────────────────────────────────────
Search-ADAccount -AccountDisabled | Select-Object Name, SamAccountName

# ── Find all locked accounts ────────────────────────────────────────
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName
```

The `Search-ADAccount` cmdlet is extremely useful for helpdesk audits. You can
quickly find all locked or disabled accounts across the entire domain.

---

## Section 6: Verifying Group Membership and Effective Access

Before wrapping up, let us verify our AGDLP chain is correct.

```powershell
# Check which groups a user belongs to (direct membership)
Get-ADPrincipalGroupMembership -Identity "jsmith" |
    Select-Object Name, GroupScope, GroupCategory

# Check nested group membership (all groups, including inherited)
(Get-ADUser "jsmith" -Properties MemberOf).MemberOf

# List all members of a group
Get-ADGroupMember -Identity "G_IT_Admins" -Recursive |
    Select-Object Name, objectClass

# Check if a specific user is in a group
(Get-ADUser "jsmith" -Properties MemberOf).MemberOf -match "G_IT_Admins"
```

---

## Section 7: Exam Tips

Here are the certification exam tips for this module:

**Exam Tip 1** — `New-ADUser` requires the `-Path` parameter to place users in
the correct OU. Without it, users land in the default CN=Users container, which
cannot have Group Policy linked to it.

**Exam Tip 2** — Group scope rules. Global groups can only contain members from
the **same domain**. Domain Local groups can contain members from **any domain**.
Universal groups can contain members from **any domain in the forest**. This
appears on the exam in the form of a scenario asking which scope is appropriate
for a given cross-domain access situation.

**Exam Tip 3** — Security vs. Distribution. Only Security groups can be assigned
to NTFS or share permissions. Distribution groups are email-only. If a scenario
asks about assigning file permissions, the answer always involves a Security group.

**Exam Tip 4** — AGDLP order matters: Accounts into Global, Global into Domain
Local, Domain Local gets the Permission. Reversing this order does not work
— you cannot put a Domain Local group inside a Global group.

**Exam Tip 5** — `-ProtectedFromAccidentalDeletion $true` on OUs is a best
practice. The exam may ask what prevents an accidental `Remove-ADOrganizationalUnit`
— this property is the answer.

**Exam Tip 6** — `Search-ADAccount` is the PowerShell tool for finding disabled,
locked-out, expired, or inactive accounts. Know this cmdlet for troubleshooting
scenarios on the exam.

---

## Wrap-Up

In this two-part module we covered:

- Designing and creating an OU structure with `New-ADOrganizationalUnit`.

- Creating individual user accounts with `New-ADUser` and all key attributes.

- Creating security groups with `New-ADGroup` using correct scopes and categories.

- Implementing the AGDLP nesting pattern with `Add-ADGroupMember`.

- Bulk provisioning hundreds of users from a CSV file using `Import-Csv` and a
  `foreach` loop.

- Managing the account lifecycle: disable, enable, unlock, password reset, and
  move with the AD cmdlet set.

- Verifying membership with `Get-ADPrincipalGroupMembership` and
  `Get-ADGroupMember`.

Head to the Reading Guide for reference tables, then complete Lab 07 where you
will build this entire structure from scratch in your own lab environment.

See you in Module 08 — Group Policy Objects.
