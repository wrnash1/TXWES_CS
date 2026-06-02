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
