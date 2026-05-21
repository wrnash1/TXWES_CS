# Quiz: Module 04 - User, Group, and Computer Accounts in AD

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

An administrator shares a folder named `HR_Docs` on the network. The Share permissions grant the `HR_Group` Read access. The NTFS permissions on the same folder grant `HR_Group` Full Control. When a member of `HR_Group` accesses the folder over the network, what is their effective permission?

A) Full Control, because NTFS permissions take precedence over Share permissions.
B) Read, because when Share and NTFS permissions conflict, the most restrictive combination applies to network access.
C) Write only, because the two permission sets are averaged together when both apply.
D) No access, because conflicting Share and NTFS permissions cancel each other out.

* **Correct Answer:** B) Read, because when Share and NTFS permissions conflict, the most restrictive combination applies to network access.
* **Distractor Analysis:**
  * *Why A is incorrect:* Neither NTFS nor Share permissions unconditionally "win" over the other for network access. The effective network permission is the intersection — the most restrictive of the two. NTFS permissions do take sole precedence only for local (console) access, not network access.
  * *Why C is incorrect:* There is no averaging of permissions. Windows evaluates each permission set independently and then applies the most restrictive result for network connections.
  * *Why D is incorrect:* The user is granted Read by the Share permissions and Full Control by NTFS. These do not cancel out — the most restrictive (Read) is the effective network permission.

---

### Question 2

A company has two file servers: one in New York (`\\NY-FS01\Data`) and one in Los Angeles (`\\LA-FS01\Data`). Users currently must remember both server paths to access company files. Which Windows Server technology allows users to access all files through a single unified path such as `\\company.local\SharedData`?

A) DFS Replication (DFSR), which synchronizes folder contents and creates a unified access path automatically.
B) File Server Resource Manager (FSRM), which aggregates multiple shares under a single namespace for user access.
C) DFS Namespaces (DFSN), which creates a virtual folder hierarchy that maps a single path to shares on multiple underlying servers.
D) Storage Spaces Direct (S2D), which pools direct-attached storage across servers and presents it as a single share path.

* **Correct Answer:** C) DFS Namespaces (DFSN), which creates a virtual folder hierarchy that maps a single path to shares on multiple underlying servers.
* **Distractor Analysis:**
  * *Why A is incorrect:* DFSR replicates the contents of folders between servers to keep them synchronized but does not create a unified namespace path for users. You need DFSN for the unified path.
  * *Why B is incorrect:* FSRM is used for storage quota management and file screening (blocking specific file types); it has no capability to aggregate shares under a unified namespace path.
  * *Why D is incorrect:* Storage Spaces Direct is a hyper-converged infrastructure feature that pools physical disk storage across clustered nodes; it does not create a logical SMB namespace for abstracting share paths.

---

### Question 3

An organization follows the AGDLP best practice for assigning permissions. A new user joins the Sales department and needs access to the Sales file share. Arranging the steps in the correct AGDLP order, what is the proper sequence?

A) Add the user account to the Domain Local group, add the Domain Local group to the Global group, assign permissions to the Global group.
B) Add the user account to the Global group, add the Global group to the Domain Local group, assign permissions to the Domain Local group on the resource.
C) Assign permissions directly to the user account on the resource, then add the user to a Global group for reporting purposes.
D) Add the user account directly to the Domain Local group and assign permissions to the Domain Local group; Global groups are optional.

* **Correct Answer:** B) Add the user account to the Global group, add the Global group to the Domain Local group, assign permissions to the Domain Local group on the resource.
* **Distractor Analysis:**
  * *Why A is incorrect:* This reverses the AGDLP nesting order. Domain Local groups should contain Global groups, not the other way around. Reversing the nesting prevents proper cross-domain scalability.
  * *Why C is incorrect:* Assigning permissions directly to individual user accounts (rather than groups) is an anti-pattern that creates unmanageable permission sprawl as the organization grows.
  * *Why D is incorrect:* While technically functional for a single domain, skipping the Global group layer eliminates the scalability benefit of AGDLP. Global groups organize users by role and enable the same permission structure to extend across domains.

---

### Question 4

A workstation that was offline for 45 days is brought back online and a user attempts to log in with their domain credentials. The login fails with a message indicating the trust relationship between the workstation and the domain has failed. What is the most appropriate remediation?

A) Rejoin the computer to the domain by removing it and re-adding it, which resets the computer account password.
B) Delete the computer account from Active Directory Users and Computers, then create a new one with the same name.
C) Run `Test-ComputerSecureChannel -Repair` on the workstation with domain admin credentials to reset the secure channel without rejoining.
D) Reset the user's password in Active Directory, as the domain trust failure is caused by an expired user password.

* **Correct Answer:** C) Run `Test-ComputerSecureChannel -Repair` on the workstation with domain admin credentials to reset the secure channel without rejoining.
* **Distractor Analysis:**
  * *Why A is incorrect:* Rejoining the domain works but is disruptive — it changes the computer's SID, breaks local group memberships, and requires re-applying user profile settings. `Test-ComputerSecureChannel -Repair` achieves the same result non-destructively.
  * *Why B is incorrect:* Deleting and recreating the computer account also changes the SID, causing the same profile and permission disruption as a full rejoin, and is a more drastic action than necessary.
  * *Why D is incorrect:* The "trust relationship failed" error is caused by a mismatch between the computer account's stored password and the password hash on the Domain Controller — it is a machine account issue, completely unrelated to the user's password.

---

### Question 5

A service account used by a Windows service needs its password rotated automatically without requiring manual intervention or application reconfiguration. The service runs on a single server. Which account type best meets this requirement?

A) A standard domain user account with a complex password that is manually rotated every 90 days by a helpdesk administrator.
B) A Managed Service Account (MSA), which automatically rotates its password and can be used by services on a single designated server.
C) A local built-in account such as Network Service, which is managed entirely by the local operating system.
D) A universal security group used as a service principal, with its password synchronized via Azure AD Connect.

* **Correct Answer:** B) A Managed Service Account (MSA), which automatically rotates its password and can be used by services on a single designated server.
* **Distractor Analysis:**
  * *Why A is incorrect:* Standard user accounts require manual password rotation and application reconfiguration whenever the password changes, creating operational overhead and outage risk.
  * *Why C is incorrect:* Built-in local accounts like Network Service have limited domain permissions and are not suitable for services that need to access domain resources under a specific identity. They also cannot be audited with domain-level granularity.
  * *Why D is incorrect:* Security groups cannot be used as service accounts or service principals in the traditional Windows service model. A group is a container for members, not an authenticatable identity for a Windows service.
