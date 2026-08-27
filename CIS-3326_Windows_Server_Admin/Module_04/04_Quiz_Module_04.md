# Quiz: Module 04 - User, Group, and Computer Accounts in AD

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

An administrator shares a folder named `HR_Docs`. The Share permissions grant `HR_Group` Read access. The NTFS permissions grant `HR_Group` Full Control. What is the effective permission when an `HR_Group` member accesses the folder over the network?

A) Full Control, because NTFS permissions take precedence over Share permissions.

B) Read, because when Share and NTFS permissions conflict, the most restrictive combination applies to network access.

C) Write only, because the two permission sets are averaged together.

D) No access, because conflicting Share and NTFS permissions cancel each other.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Neither permission type unconditionally wins for network access. The effective network permission is the intersection — the most restrictive result.
  - Why C is incorrect: There is no averaging of permissions. Windows evaluates each permission set independently and applies the most restrictive for network connections.
  - Why D is incorrect: The user has Read from Share and Full Control from NTFS. These do not cancel — the most restrictive (Read) is the effective network permission.

---

### Question 2

A company follows AGDLP best practice for assigning file share permissions. A new user joins the Sales department and needs access to the Sales file share. What is the correct AGDLP sequence?

A) Add the user to the Domain Local group, add the Domain Local group to the Global group, assign permissions to the Global group.

B) Add the user to the Global group, add the Global group to the Domain Local group, assign permissions to the Domain Local group on the resource.

C) Assign permissions directly to the user account on the resource, then add the user to a Global group for reporting.

D) Add the user directly to the Domain Local group. Global groups are optional in single-domain environments.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This reverses the AGDLP nesting order. Domain Local groups contain Global groups, not the reverse.
  - Why C is incorrect: Assigning permissions directly to individual users creates unmanageable permission sprawl as the organization grows.
  - Why D is incorrect: Skipping the Global group layer works functionally but eliminates the scalability and management benefits of AGDLP.

---

### Question 3

A workstation was offline for 45 days and now fails domain logon with "trust relationship between this workstation and the primary domain failed." What is the most appropriate non-destructive fix?

A) Rejoin the computer to the domain by removing it and re-adding it to reset the computer account password.

B) Delete the computer account from ADUC and create a new one with the same name.

C) Run `Test-ComputerSecureChannel -Repair` on the workstation with domain admin credentials.

D) Reset the user's password in AD — the trust failure is caused by an expired user password.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Rejoining works but changes the computer's SID, breaking local profile associations and group memberships. `Test-ComputerSecureChannel -Repair` is non-destructive.
  - Why B is incorrect: Deleting and recreating also changes the SID, with the same disruptive consequences.
  - Why D is incorrect: The trust failure is a machine account issue — the computer and DC machine account passwords are out of sync. It has nothing to do with the user's password.

---

### Question 4

A service account runs on a single server and needs its password rotated automatically without any manual intervention. Which account type is most appropriate?

A) A standard domain user account with "Password never expires" set.

B) A Managed Service Account (MSA), which automatically rotates its password and is bound to a single designated server.

C) The local built-in Network Service account, managed entirely by the operating system.

D) A Universal security group used as a service principal.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Standard accounts require manual password rotation and application reconfiguration when the password changes.
  - Why C is incorrect: Network Service is a local account with limited domain permissions — it cannot access domain resources under a specific auditable domain identity.
  - Why D is incorrect: Security groups cannot be used as service accounts or authenticated service principals.

---

### Question 5

An administrator needs to create a service account that runs across five web servers in a load-balanced farm. The account must rotate its password automatically. Which account type is required?

A) Managed Service Account (MSA)

B) Group Managed Service Account (gMSA)

C) Standard user account with "Password never expires"

D) Domain Local group with service logon rights

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: MSAs are restricted to a single server. They cannot be used on multiple machines simultaneously.
  - Why C is incorrect: Standard accounts require manual password management and do not rotate automatically.
  - Why D is incorrect: Groups cannot be used as service accounts. Service logon rights must be granted to an account, not a group container.

---

### Question 6

An administrator needs to allow a user to log in only during business hours (Monday through Friday, 8 AM to 6 PM) and only from computers in the Finance department. Which two user account properties must be configured?

A) Account Expiration and Password Never Expires

B) Logon Hours and Logon Workstations

C) Account Is Disabled and Account Is Locked Out

D) UPN Suffix and SAM Account Name

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Account Expiration controls when the account deactivates permanently. Password Never Expires affects the password policy. Neither restricts logon hours or workstations.
  - Why C is incorrect: Disabled and Locked Out are account states, not configurable restriction settings. They block all logon, not scheduled/workstation-based restriction.
  - Why D is incorrect: UPN suffix and SAM Account Name are logon name identifiers, not access restriction settings.

---

### Question 7

A Global group named `G_Finance` is used to assign permissions to a file share in a multi-domain forest. Administrators find that users in a partner domain cannot be added to `G_Finance`. What is the reason?

A) Global groups can only be assigned permissions within their own domain.

B) Global groups can only contain members from the same domain where the group was created.

C) Global groups require the forest functional level to be at Windows Server 2016 before accepting cross-domain members.

D) Global groups must be converted to Universal groups before the file share permissions can take effect.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Global groups can be used to assign permissions in any domain in the forest. The restriction is on membership, not permission assignment.
  - Why C is incorrect: The cross-domain membership limitation is inherent to Global group scope and is not related to functional levels.
  - Why D is incorrect: Converting to Universal is one solution, but it is not required. A Domain Local group accepting a cross-domain Global group is the correct AGDLP approach.

---

### Question 8

Which PowerShell command displays all groups that a specific user account is a member of, including nested memberships?

A) `Get-ADGroup -Filter { Members -contains "jdoe" }`

B) `Get-ADGroupMember -Identity "jdoe" -Recursive`

C) `Get-ADPrincipalGroupMembership -Identity "jdoe"`

D) `Get-ADUser -Identity "jdoe" -Properties MemberOf`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: This syntax is not valid. `Get-ADGroup` filters by group properties; the `-Filter` expression used here is not a supported syntax.
  - Why B is incorrect: `Get-ADGroupMember` lists members of a group — it takes a group name as input, not a user name. It would list who is in a group, not which groups a user belongs to.
  - Why D is incorrect: While `Get-ADUser -Properties MemberOf` returns the `MemberOf` attribute, it only shows direct memberships and returns Distinguished Names rather than friendly group names. `Get-ADPrincipalGroupMembership` is the correct tool for this purpose.

---

### Question 9

What happens to a user's resource access permissions when their account is deleted from Active Directory?

A) Access permissions are preserved because the resource still has the group names recorded.

B) Access permissions become inaccessible because the SID is destroyed, and the group and ACL entries that referenced the SID become orphaned.

C) Access permissions are automatically reassigned to the user's manager based on the AD organizational hierarchy.

D) Access permissions remain intact for 30 days and then expire, allowing time for auditing.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Permissions are stored as SIDs in ACLs, not as names. When the SID is deleted, the ACL entry becomes an orphaned "Account Unknown" entry with no resolvable identity.
  - Why C is incorrect: AD does not have an automatic permission transfer mechanism based on reporting structure. Permissions must be managed manually.
  - Why D is incorrect: There is no 30-day grace period for deleted account permissions. SID deletion is immediate and permanent without the AD Recycle Bin.

---

### Question 10

An administrator creates a gMSA for a web application cluster. Before running `New-ADServiceAccount`, what must exist in the forest?

A) A Global Catalog server in each AD site

B) A KDS Root Key, created with `Add-KdsRootKey`

C) A Fine-Grained Password Policy applied to the service account OU

D) A Managed Service Account (MSA) with the same name already present

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: GC server placement affects logon performance but is not a prerequisite for gMSA creation.
  - Why C is incorrect: FGPPs are not required or related to gMSA creation. gMSAs manage their own passwords independently.
  - Why D is incorrect: There is no requirement to have an MSA before creating a gMSA. They are separate account types.

---

### Question 11 (5 points)

An administrator creates a new user and uses `Set-ADUser -Identity "jdoe" -LogonWorkstations "WS-FIN-01,WS-FIN-02"`. What is the effect of this configuration?

- A) The user can only log on to the domain from WS-FIN-01 and WS-FIN-02
- B) The user's profile is copied to WS-FIN-01 and WS-FIN-02 at next logon
- C) Group Policy from the workstations OU applies to the user only when logged on to those machines
- D) The user's password expiration is tied to the last logon date on either workstation

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Profile copying is not triggered by the `LogonWorkstations` attribute. Roaming profiles are configured separately through the user's Profile tab.
  - Why C is incorrect: Group Policy Computer Configuration applies based on the computer's OU placement, not on which user is logged on. The `LogonWorkstations` setting restricts logon access only.
  - Why D is incorrect: Password expiration is governed by domain password policy or Fine-Grained Password Policies. It has no relationship to the `LogonWorkstations` attribute.

---

### Question 12 (5 points)

Which PowerShell command creates a new user account named "John Doe" with the UPN `jdoe@corp.local` in the IT OU and requires a password change at first logon?

- A) `New-ADUser -Name "John Doe" -SamAccountName "jdoe" -UserPrincipalName "jdoe@corp.local" -Path "OU=IT,OU=Departments,DC=corp,DC=local" -Enabled $true -ChangePasswordAtLogon $true`
- B) `Add-ADUser -Name "John Doe" -UPN "jdoe@corp.local" -OU "OU=IT,OU=Departments" -ForcePasswordChange`
- C) `New-ADUser -Identity "jdoe" -UPN "jdoe@corp.local" -Container "IT" -MustChangePassword`
- D) `Set-ADUser -Name "John Doe" -Path "OU=IT" -NewPassword (Read-Host -AsSecureString) -Enabled`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `Add-ADUser` is not a valid PowerShell cmdlet. The correct cmdlet is `New-ADUser`. The parameter names `-UPN` and `-ForcePasswordChange` are also invalid.
  - Why C is incorrect: `-Identity` is used with existing objects, not during creation. `-Container` and `-MustChangePassword` are not valid `New-ADUser` parameter names. The correct parameters are `-Path` and `-ChangePasswordAtLogon`.
  - Why D is incorrect: `Set-ADUser` modifies an existing account. It cannot create a new user. `New-ADUser` is required for account creation.

---

### Question 13 (5 points)

A Universal security group named `U_AllSalesReps` has 5,000 members drawn from three domains in the forest. The membership changes frequently. Why might an administrator restructure this to use Global groups nested into the Universal group?

- A) Universal groups cannot contain more than 1,000 members
- B) Each change to Universal group membership triggers Global Catalog replication across the entire forest, creating unnecessary replication traffic; nesting Global groups means only role group membership changes replicate universally
- C) Universal groups cannot assign permissions to resources — only Domain Local groups can
- D) Universal groups are not stored in the AD database and rely on DNS for membership resolution

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: There is no 1,000-member limit on Universal groups. They can contain any number of members.
  - Why C is incorrect: Universal groups can assign permissions to resources in any domain in the forest. The restriction is that Domain Local groups assign permissions only within their own domain.
  - Why D is incorrect: Universal group membership is stored in the Global Catalog, which is a designation on a Domain Controller — not in DNS. Universal group data is part of the AD directory database.

---

### Question 14 (5 points)

An administrator uses `Search-ADAccount -PasswordNeverExpires | Select-Object Name, SamAccountName` to audit the domain. Which type of accounts would typically appear in this output, and why is this a security concern?

- A) Locked-out accounts; they should be reviewed for brute-force attack attempts
- B) Service accounts configured with non-expiring passwords; stale credentials that have never rotated are a persistent security risk if compromised
- C) Computer accounts; their passwords never expire by AD design
- D) Disabled accounts; they retain their last password indefinitely after being disabled

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Search-ADAccount -PasswordNeverExpires` returns accounts with the password-never-expires flag. Locked-out accounts are found with `-LockedOut`. These are separate searches.
  - Why C is incorrect: Computer account passwords rotate automatically every 30 days by default. They would not appear in a `PasswordNeverExpires` query unless the flag was explicitly set.
  - Why D is incorrect: Disabling an account does not set the `PasswordNeverExpires` flag. These are separate attributes. A disabled account with an expiring password would not appear in this output.

---

### Question 15 (5 points)

An administrator needs to find all users whose accounts have expired as of today. Which PowerShell command correctly retrieves these accounts?

- A) `Get-ADUser -Filter {AccountExpirationDate -lt (Get-Date)}`
- B) `Search-ADAccount -AccountExpired`
- C) `Get-ADUser -Filter * -Properties AccountExpirationDate | Where-Object { $_.AccountExpirationDate -eq "Expired" }`
- D) `Find-ADUser -Status Expired`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The `-Filter` syntax for `Get-ADUser` does not support comparison with `(Get-Date)` inline in the filter expression. This would produce an error or unexpected results.
  - Why C is incorrect: `AccountExpirationDate` is a `DateTime` object, not a string. Comparing it to the literal string `"Expired"` will never match. This command returns no results.
  - Why D is incorrect: `Find-ADUser` is not a valid PowerShell cmdlet in the Active Directory module. The `Search-ADAccount` cmdlet is the correct tool for state-based account queries.

---

### Question 16 (5 points)

An administrator converts a Distribution group to a Security group. What immediate practical capability does this enable?

- A) The group can now receive email, which Distribution groups cannot
- B) The group can now be assigned NTFS and Share permissions on resources
- C) The group can now contain members from other forests without a trust
- D) The group members are now subject to Fine-Grained Password Policies

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Distribution groups are already email-capable; that is their primary purpose. Security groups can also receive email. Converting to Security does not add email capability.
  - Why C is incorrect: Cross-forest membership is governed by group scope (Universal) and forest trust relationships, not by whether the group is Security or Distribution type.
  - Why D is incorrect: Fine-Grained Password Policies apply to users and groups regardless of whether the group is Security or Distribution type. Group type does not affect FGPP applicability.

---

### Question 17 (5 points)

A Fine-Grained Password Policy named `IT_Admin_Policy` has Precedence 10. A second FGPP named `Standard_Policy` has Precedence 50. A user is a member of both groups that have these policies applied. Which policy governs the user's password requirements?

- A) `Standard_Policy` because higher precedence numbers take priority
- B) `IT_Admin_Policy` because lower precedence numbers take priority
- C) Both policies merge — the most restrictive settings from each are applied
- D) The domain Default Domain Policy overrides all FGPPs when a conflict exists

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Precedence numbering is counterintuitive — lower numbers mean higher priority. Precedence 10 wins over Precedence 50.
  - Why C is incorrect: FGPPs do not merge. The single winning policy (lowest precedence number) applies entirely to the user. There is no mixing of settings between competing PSOs.
  - Why D is incorrect: FGPPs are specifically designed to override the Default Domain Policy for targeted users and groups. When an FGPP applies to a user, it takes priority over the domain-wide password policy.

---

### Question 18 (5 points)

Which of the following group scope conversions is valid in Active Directory without first adding or removing members?

- A) Domain Local → Global
- B) Global → Domain Local
- C) Universal → Domain Local
- D) Global → Universal

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: Converting Domain Local to Global is not allowed because a Domain Local group may contain members from other domains. Global groups can only contain members from the same domain.
  - Why B is incorrect: Global to Domain Local conversion is not a supported direct conversion path in Active Directory.
  - Why C is incorrect: Universal to Domain Local conversion requires that the Universal group not be a member of any other Universal group. While this conversion is technically possible under some conditions, Global to Universal is the standard supported path. Universal → Domain Local is not a standard scope upgrade path.

---

### Question 19 (5 points)

An administrator creates a gMSA named `SVC_WebFarm` and grants a security group named `WebServers` the right to retrieve the managed password. What cmdlet parameter controls which computers can retrieve the gMSA password?

- A) `-AllowedToRetrievePassword`
- B) `-PrincipalsAllowedToRetrieveManagedPassword`
- C) `-AuthorizedComputers`
- D) `-PasswordRetrievalGroup`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-AllowedToRetrievePassword` is not a valid parameter name for `New-ADServiceAccount`. The correct parameter name is `-PrincipalsAllowedToRetrieveManagedPassword`.
  - Why C is incorrect: `-AuthorizedComputers` is not a valid parameter for `New-ADServiceAccount`. Computer authorization for gMSA password retrieval is set through the `-PrincipalsAllowedToRetrieveManagedPassword` parameter.
  - Why D is incorrect: `-PasswordRetrievalGroup` is not a valid PowerShell parameter name for gMSA creation. This is a fabricated parameter name.

---

### Question 20 (5 points)

An administrator disables a departing employee's user account and removes them from all security groups. Two weeks later, the manager requests the employee's account be reactivated due to a compliance requirement. What is the benefit of having disabled the account rather than deleted it?

- A) Disabled accounts retain their password history, allowing the employee to log in with the same password
- B) The original SID, group memberships (if preserved before removal), and all associated permissions are still recoverable because the AD object was not deleted
- C) Disabled accounts are automatically re-enabled after 30 days if no deletion is requested
- D) Disabled accounts remain active in Exchange mailbox but not in AD, simplifying email restoration

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Password history (previously used passwords) is stored as a hashed list to prevent reuse. The ability to log in with the old password is not preserved or recoverable from the disabled state.
  - Why C is incorrect: There is no automatic re-enable timer on disabled accounts. Accounts remain disabled until an administrator explicitly enables them.
  - Why D is incorrect: Exchange mailbox status is separate from AD account enablement. Disabling an AD account disables Exchange logon as well. Mailbox access is not preserved in a separate active state.
