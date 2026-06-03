# Quiz: Module 07 — Active Directory User and Group Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
Review your Reading Guide and video notes before beginning.

---

## Question 1

An administrator runs the following PowerShell command to create a new user
account. After the command succeeds, the user reports they cannot log on.
What is the most likely reason?

```powershell
New-ADUser -Name "Kim Park" -SamAccountName "kpark" -UserPrincipalName "kpark@txwes.edu"
```

A) The `-UserPrincipalName` parameter is not required and causes an error when
included with `-SamAccountName`.

B) The account was created in a disabled state because the `-Enabled $true`
parameter was not included.

C) The `-Name` parameter format is invalid — it must match the `-SamAccountName`
value exactly.

D) The user account requires a computer object in the same OU before it can
authenticate to the domain.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Both `-SamAccountName` and `-UserPrincipalName` are valid and commonly used together. Including both is correct and does not cause an error.
  - Why C is incorrect: `-Name` is the display name (Common Name) and does not need to match `-SamAccountName`. They serve different purposes: CN is the display identifier and sAMAccountName is the logon name.
  - Why D is incorrect: User accounts authenticate independently of computer objects. There is no requirement for a computer object in the same OU for a user to log on.

---

## Question 2

A domain administrator needs to create a group that will contain users from
multiple departments within the same domain and will be added to Domain Local
groups in other domains in the same forest to grant file share permissions.
Which group scope is correct?

A) Domain Local, because it can contain members from any domain and is used
to assign permissions.

B) Universal, because it can span the forest and its membership is stored in
the Global Catalog for cross-domain reference.

C) Global, because it contains users from the same domain and can be nested
into Domain Local groups in any domain in the forest.

D) Distribution, because cross-domain access requires a distribution group
that is not bound to a single domain's security boundary.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Domain Local groups are used to hold permissions on resources within one domain. They are the destination for Global group nesting, not the container for same-domain users being granted access elsewhere.
  - Why B is incorrect: Universal groups can span the forest, but they are not the right choice here. All users are in the same domain, so a Global group satisfies the membership requirement. Universal groups carry the overhead of Global Catalog replication for their membership.
  - Why D is incorrect: Distribution groups cannot be assigned to NTFS or share permissions. They are email-only and have no role in the AGDLP access management model.

---

## Question 3

A company implements the AGDLP group nesting model. Which of the following
correctly describes the role of a Domain Local group in this model?

A) It holds the user accounts that share a common job role or department, so
that role changes require adding or removing users from only one group.

B) It is nested inside a Global group to extend the Global group's membership
to include users from other domains in the forest.

C) It holds the permission on the resource (the file share, printer, or folder)
and contains Global groups as its members.

D) It is created in the forest root domain so that its permissions automatically
flow down to all child domains via inheritance.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: This describes the role of a **Global** group — organizing users who share a role. The Domain Local group's role is to hold the permission on the resource, not to organize users by role.
  - Why B is incorrect: Domain Local groups are not nested inside Global groups. The nesting direction in AGDLP is: Global groups are nested **into** Domain Local groups, not the other way around.
  - Why D is incorrect: Group permissions do not flow down to child domains via inheritance. Each domain's resources are governed by the Domain Local groups in that domain. There is no automatic inheritance of permissions to child domains.

---

## Question 4

An IT manager wants to prevent junior administrators from accidentally deleting
the `OU=Faculty,OU=TXWES,DC=txwes,DC=edu` organizational unit. Which PowerShell
parameter accomplishes this when creating or modifying the OU?

A) `-PreventDeletion $true`

B) `-ProtectedFromAccidentalDeletion $true`

C) `-ReadOnly $true`

D) `-Immutable $true`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-PreventDeletion` is not a valid parameter for `New-ADOrganizationalUnit` or `Set-ADOrganizationalUnit`. This is a plausible-sounding but incorrect parameter name.
  - Why C is incorrect: `-ReadOnly` is not a valid Active Directory OU parameter. Making an OU read-only would also prevent administrators from creating objects inside it, which is not the intent.
  - Why D is incorrect: `-Immutable` is not a valid Active Directory OU parameter. The correct and tested parameter for accidental deletion protection is `-ProtectedFromAccidentalDeletion`.

---

## Question 5

A company has 50 new student employees starting on Monday. An administrator
receives a CSV file with columns: FirstName, LastName, Department, OU. Which
PowerShell approach is correct for bulk-provisioning all 50 accounts from
this file?

A) Use `Get-ADUser -Filter * | New-ADUser` to clone existing user accounts for
each row in the CSV.

B) Use `Import-Csv` to load the CSV into an array, then loop through each row
with `foreach` calling `New-ADUser` for each record.

C) Use `Set-ADUser` in a loop to update the 50 existing disabled accounts with
new names and UPNs from the CSV.

D) Use `Add-ADGroupMember -Members (Import-Csv "file.csv")` to import the
CSV rows directly as new group members.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-ADUser | New-ADUser` is not a valid pipeline pattern for creating new users. `New-ADUser` does not accept pipeline input from `Get-ADUser` to clone accounts en masse.
  - Why C is incorrect: `Set-ADUser` modifies existing accounts — it does not create new ones. If the 50 accounts do not already exist, `Set-ADUser` will throw "identity not found" errors for every row.
  - Why D is incorrect: `Add-ADGroupMember` adds existing objects to a group. It cannot create new user accounts from CSV data. Users must be created with `New-ADUser` before they can be added to groups.

---

## Question 6

A user account for a terminated employee has been disabled. The IT policy
requires waiting 60 days before permanently deleting the account. The employee's
manager requests that the user's group memberships be preserved during the
waiting period. Which of the following is true about a disabled Active Directory
account?

A) Disabling an account automatically removes the user from all security groups
to prevent residual access during the waiting period.

B) Disabling an account prevents the user from authenticating while preserving
all group memberships, attributes, and the account's place in the OU structure.

C) Disabled accounts must be moved to a Quarantine OU or they retain full access
to all resources through cached Kerberos tickets indefinitely.

D) Disabling an account removes only the user's Domain Local group memberships;
Global and Universal group memberships are preserved.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Disabling an account does not remove group memberships. All group memberships, attributes, and the distinguished name are preserved exactly. This is one of the key reasons to disable rather than immediately delete.
  - Why C is incorrect: Kerberos tickets have a maximum lifetime (default 10 hours). After ticket expiration, the disabled account cannot obtain new tickets and all resource access is blocked. The account does not need to be moved for access to be denied.
  - Why D is incorrect: Disabling an account is not selective — it does not remove any group memberships of any scope. All memberships across all group types are fully preserved.

---

## Question 7

An organization operates a multi-domain forest. The network team needs a group
whose membership is sourced from users in multiple domains and that can be used
to assign permissions to resources in multiple domains. Which group scope is
the only one that supports both requirements simultaneously?

A) Global, because it can contain users from any domain and assign permissions
in any domain.

B) Domain Local, because it can contain users from any domain and assign
permissions in the domain where it resides.

C) Universal, because it can contain users from any domain in the forest and
assign permissions in any domain in the forest.

D) Security Distribution, because cross-forest access requires a hybrid group
type that combines both security and distribution properties.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Global groups can contain members only from the **same domain** where the group was created. They cannot contain users from multiple domains, so they cannot satisfy the first requirement.
  - Why B is incorrect: Domain Local groups can contain members from any domain (satisfying requirement 1), but they can only assign permissions in the **same domain** where they reside (violating requirement 2). They cannot assign permissions in multiple domains simultaneously.
  - Why D is incorrect: "Security Distribution" is not a valid Active Directory group type. The two group categories are Security and Distribution. There is no hybrid type combining both.

---

## Question 8

An administrator needs to find all user accounts in the `txwes.edu` domain that
are currently locked out so the help desk can contact affected users. Which
PowerShell command is correct?

A) `Get-ADUser -Filter {LockedOut -eq $true} -Properties LockedOut`

B) `Search-ADAccount -LockedOut | Select-Object Name, SamAccountName`

C) `Get-ADUser -Filter * | Where-Object {$_.AccountLockoutTime -gt 0}`

D) `Get-EventLog -LogName Security -InstanceId 4740`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: While this syntax resembles a valid AD filter, `LockedOut` is a computed property that is not directly filterable using the `-Filter` parameter in the same way as stored attributes. `Search-ADAccount -LockedOut` is the purpose-built cmdlet for this task.
  - Why C is incorrect: `AccountLockoutTime` is a DateTime property, not a numeric value. Comparing it to `0` would throw a type error. Additionally, this approach retrieves all users first and then filters, which is less efficient than `Search-ADAccount`.
  - Why D is incorrect: `Get-EventLog -InstanceId 4740` retrieves Security event log entries for lockout events — this shows **when** lockouts occurred historically. It does not show which accounts are **currently** locked out right now.

---

## Question 9

A new administrator creates a security group with the following command and then
attempts to add it to a Domain Local group in a partner domain to grant file share
access. The operation fails. What is the reason?

```powershell
New-ADGroup -Name "G_Finance_Readers" -GroupScope DomainLocal -GroupCategory Security
```

A) The group name prefix "G_" is reserved for Global groups; Domain Local groups
must use the prefix "DL_" or the command fails.

B) A Domain Local group cannot be nested inside another Domain Local group in a
different domain. To grant cross-domain permissions, a Global group must be used.

C) The `-GroupCategory Security` parameter is incompatible with `-GroupScope
DomainLocal` and creates a group with no permissions capability.

D) Domain Local groups require the `-Path` parameter to specify an OU; without it,
the group is not visible to other domains and cannot be used cross-domain.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Group name prefixes like "G_" and "DL_" are naming conventions only — they have no technical meaning to Active Directory. The `-GroupScope` parameter controls the scope, not the name prefix.
  - Why C is incorrect: Security and DomainLocal are a fully valid combination. Domain Local Security groups are one of the most common group configurations and are the standard holder for resource permissions.
  - Why D is incorrect: The `-Path` parameter controls which OU the group is placed in, not cross-domain visibility. The fundamental issue is that a Domain Local group cannot be nested into a group in another domain — that is a scope rule, not a path issue.

---

## Question 10

An administrator wants to verify that the user `agarcia` is a member of the
`DL_HR_FullControl` Domain Local group through nested group membership (not direct
membership). Which PowerShell command reveals all groups `agarcia` belongs to,
including memberships through nested groups?

A) `Get-ADUser -Identity "agarcia" -Properties MemberOf`

B) `Get-ADGroupMember -Identity "DL_HR_FullControl" -Recursive`

C) `Get-ADPrincipalGroupMembership -Identity "agarcia"`

D) `(Get-ADUser "agarcia" -Properties MemberOf).MemberOf`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-ADUser -Properties MemberOf` returns only the groups `agarcia` is a **direct** member of. It does not traverse nested memberships and will not show Domain Local groups that `agarcia` belongs to through a nested Global group.
  - Why C is incorrect: `Get-ADPrincipalGroupMembership` returns the groups the principal is directly a member of — it does not recursively enumerate nested memberships. The question specifically asks about nested membership.
  - Why D is incorrect: `.MemberOf` property access returns the same result as option A — direct group memberships only. This does not reveal nested memberships inherited through group nesting chains.
