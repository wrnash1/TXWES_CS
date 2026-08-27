# Quiz: Module 03 - Installing and Configuring AD DS

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

An administrator runs `Install-WindowsFeature -Name AD-Domain-Services` on a new Windows Server and the server completes the installation without errors. A user then tries to log in with a domain account and fails. What is the most likely reason?

A) The server needs to be rebooted twice after role installation before AD DS activates.

B) The server was not promoted to a Domain Controller — role installation only copies binaries.

C) The administrator forgot to specify `-IncludeManagementTools`, which is required for the DC to function.

D) The DNS Server role must be installed separately before domain accounts can authenticate.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: AD DS promotion is not automatic after role installation regardless of how many reboots occur. An explicit promotion step is always required.
  - Why C is incorrect: `-IncludeManagementTools` installs management utilities and the AD PowerShell module but is not required for DC functionality. The server would still fail to authenticate users even with management tools installed, because promotion has not occurred.
  - Why D is incorrect: DNS is installed automatically when the `-InstallDns` switch is used during promotion. Pre-installing DNS separately is not required and does not enable domain authentication without promotion.

---

### Question 2

A company needs to deploy a new child domain `west.corp.local` in an existing forest. Which PowerShell cmdlet is used to promote the server as a Domain Controller for this new child domain?

A) `Install-ADDSForest`

B) `Install-ADDSDomainController`

C) `Install-ADDSDomain`

D) `Add-WindowsFeature -ChildDomain`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `Install-ADDSForest` creates a brand-new forest. Using it would create a separate forest named `west.corp.local` rather than a child domain in the existing `corp.local` forest.
  - Why B is incorrect: `Install-ADDSDomainController` adds an additional DC to an existing domain. It does not create a new domain.
  - Why D is incorrect: `Add-WindowsFeature` does not exist as a cmdlet for child domain creation. `Add-WindowsFeature` is also not the correct syntax for `Install-WindowsFeature`.

---

### Question 3

After promoting a new DC, an administrator runs `dcdiag` and receives a failure on the Replications test. What is the most likely root cause and best first diagnostic step?

A) The Domain Controller's IP address needs to be renewed with DHCP before replication can start.

B) DNS resolution is failing or the DC cannot locate replication partners — verify DNS records and check replication topology with `repadmin /showrepl`.

C) SYSVOL is not published — re-create the SYSVOL share manually using Server Manager.

D) The Domain Functional Level must be raised before replication between DCs can begin.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Domain Controllers require static IP addresses. DHCP renewal would change the IP, invalidating DNS SRV registrations, and would not resolve a replication failure.
  - Why C is incorrect: SYSVOL is published automatically by the DFSR service once AD replication is healthy. Manually re-creating it does not fix DNS or network-layer replication failures.
  - Why D is incorrect: Replication between DCs does not require a specific functional level to operate. Replication failures at initial setup are almost always DNS or network connectivity issues.

---

### Question 4

Which PowerShell command provides the most concise summary of replication health across all Domain Controllers in a domain, showing success and failure counts per DC?

A) `Get-ADReplicationFailure -Scope Domain`

B) `repadmin /showrepl * /errorsonly`

C) `repadmin /replsummary`

D) `dcdiag /test:Replications`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: While `Get-ADReplicationFailure` exists, it reports failures for a specific DC rather than providing a domain-wide summary table of success and failure counts per DC.
  - Why B is incorrect: `repadmin /showrepl * /errorsonly` shows only failed replication relationships — it does not display a summary count or show healthy DCs. It is a good follow-up tool but not the best first-look summary command.
  - Why D is incorrect: `dcdiag /test:Replications` runs a diagnostic test and shows pass/fail output. It is thorough but more verbose than the summary table provided by `repadmin /replsummary`.

---

### Question 5

An organization is adding a new server to an existing forest but the administrator forgets to configure a static IP. The promotion appears to succeed but clients cannot find the new DC. What specific failure would explain this?

A) The AD DS database was not created because NTDS.dit requires a static IP to initialize.

B) The DNS SRV records registered by the Netlogon service reference the DHCP-assigned IP, which may change, making the DC unreachable by name.

C) DHCP servers automatically block port 389 on Windows Server, preventing LDAP from functioning.

D) The Domain Functional Level is automatically lowered when a DHCP-configured DC joins the domain.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: NTDS.dit creation is not dependent on IP addressing. The promotion can complete with a DHCP address, which is why the administrator did not see an error.
  - Why C is incorrect: DHCP servers do not block LDAP ports. Port 389 availability is controlled by Windows Firewall, which allows it by default for AD DS.
  - Why D is incorrect: DHCP configuration on a DC has no effect on Domain Functional Level. DFL is determined by the OS versions of DCs in the domain.

---

### Question 6

An organization is raising its domain functional level to Windows Server 2016. Before running `Set-ADDomainMode`, what must the administrator verify?

A) That the Schema Master is online and the schema version matches Windows Server 2016.

B) That all Domain Controllers in the domain are running Windows Server 2016 or later.

C) That the forest functional level is already at Windows Server 2016 before raising the domain level.

D) That the Active Directory Recycle Bin is disabled before the domain level change is applied.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Schema version and Schema Master availability are required for schema extensions, not for raising the functional level.
  - Why C is incorrect: The forest functional level cannot be higher than the lowest domain functional level — it is the domain level that must be raised first, then the forest level.
  - Why D is incorrect: The Recycle Bin has no dependency relationship with the domain functional level change operation.

---

### Question 7

A Domain Controller in a branch office fails completely and cannot be recovered. The administrator needs to remove its metadata from Active Directory. Which tool is used to perform metadata cleanup?

A) `dcdiag /fix`

B) `ntdsutil` with the metadata cleanup command

C) `repadmin /removelingeringobjects`

D) `Active Directory Sites and Services` — delete the server object

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `dcdiag /fix` performs minor automatic repairs for some diagnostic failures but does not remove DC metadata.
  - Why C is incorrect: `repadmin /removelingeringobjects` removes objects that exist on a DC but were deleted elsewhere — it does not remove DC server metadata.
  - Why D is incorrect: Deleting the server object in Active Directory Sites and Services is part of metadata cleanup but is not the complete process. `ntdsutil` performs the authoritative cleanup sequence including NTDS Settings object removal.

---

### Question 8

The Netlogon service is responsible for registering DNS SRV records when a DC starts. An administrator notices that a newly promoted DC's SRV records are missing from DNS. What is the fastest way to re-register them?

A) Promote a new DC — the existing DC cannot re-register SRV records without a full reinstall.

B) Restart the Netlogon service on the DC with missing records.

C) Delete the DNS zone and allow automatic recreation.

D) Run `ipconfig /registerdns` and then `dcdiag /fix`.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Repromoting is unnecessary. The Netlogon service registers SRV records every time it starts, so a service restart is sufficient.
  - Why C is incorrect: Deleting the DNS zone would remove all records for all DCs and cause a domain-wide authentication outage. This is never appropriate as a troubleshooting step for missing SRV records.
  - Why D is incorrect: `ipconfig /registerdns` registers the host A record but does not register AD DS SRV records. SRV record registration is performed exclusively by the Netlogon service.

---

### Question 9

An administrator is deploying a DC at a branch office with limited physical security. They want to allow caching of branch office user passwords but must ensure that no Domain Admin passwords are ever cached on the branch DC. Which DC type and configuration meets this requirement?

A) A standard writable DC with BitLocker enabled.

B) A Read-Only DC with Domain Admin accounts in the Denied RODC Password Replication Group.

C) A standard writable DC with the Password Replication Policy configured.

D) A Read-Only DC with no Password Replication Policy configured, which defaults to no caching.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A writable DC holds all password hashes regardless of BitLocker. BitLocker protects offline disk access but not runtime credential extraction.
  - Why C is incorrect: Standard writable DCs do not have a Password Replication Policy — that mechanism exists only on RODCs.
  - Why D is incorrect: The default RODC configuration with no PRP changes caches no passwords at all, including branch office users. The requirement is to allow branch user caching while blocking Domain Admins — this requires a configured PRP with an Allow list for branch users and a Deny list for privileged accounts.

---

### Question 10

An administrator wants to verify that SYSVOL is properly shared and replicated on a newly promoted DC. Which command confirms SYSVOL share availability?

A) `net share SYSVOL /verify`

B) `Get-SmbShare | Where-Object { $_.Name -eq "SYSVOL" }`

C) `repadmin /showsysvol`

D) `dcdiag /test:SYSVOLCheck /v`

- **Correct Answer:** D
- **Distractor Analysis:**
  - Why A is incorrect: `net share SYSVOL /verify` is not valid syntax. `net share` can list shares but does not accept `/verify` as a parameter.
  - Why B is incorrect: While this PowerShell command confirms the SYSVOL share exists, `dcdiag /test:SysVolCheck` is the comprehensive test that verifies SYSVOL is properly shared, published, and accessible — which is what the exam expects.
  - Why C is incorrect: `repadmin /showsysvol` is not a valid repadmin command. SYSVOL replication status is checked via DFSR event logs or `dfsrdiag`.

---

### Question 11 (5 points)

An administrator needs to add a DC to the `corp.local` domain. The promotion fails with: "The forest functional level is not compatible with the operating system of this computer." What is the most likely cause?

- A) The new DC's computer account has not yet been pre-staged in Active Directory
- B) The new server is running an older Windows Server version than the current forest functional level requires
- C) The DSRM password provided was too short
- D) The AD DS role was installed with `-IncludeManagementTools`, which conflicts with promotion

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Pre-staging a DC computer account is optional (used for delegated RODC deployments). A missing pre-staged account produces a different error, not a functional level compatibility message.
  - Why C is incorrect: DSRM password length requirements produce a password complexity error, not a functional level error.
  - Why D is incorrect: `-IncludeManagementTools` installs optional management utilities. It has no effect on DC promotion compatibility or functional level requirements.

---

### Question 12 (5 points)

An administrator wants to force immediate replication of all directory partitions from all replication partners to a specific DC named `SRV-CORE-02`. Which command accomplishes this?

- A) `repadmin /replicate SRV-CORE-02 * /force`
- B) `repadmin /syncall SRV-CORE-02 /AdeP`
- C) `Sync-ADObject -Destination SRV-CORE-02`
- D) `dcdiag /test:Replications /force /target:SRV-CORE-02`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `repadmin /replicate` triggers replication of a single naming context from a single source DC, not all partitions from all partners. The syntax shown is also not valid.
  - Why C is incorrect: `Sync-ADObject` synchronizes a single specific object to a target DC. It does not perform a full domain-wide partition sync.
  - Why D is incorrect: `dcdiag /test:Replications` is a diagnostic command that reports replication health. It does not force replication to occur.

---

### Question 13 (5 points)

Which DNS zone configuration should be used on Domain Controllers to ensure that DNS zone data is automatically replicated to all DCs in the forest without manual zone transfer configuration?

- A) Standard primary zone stored in a flat zone file
- B) Standard secondary zone pointing to DC1 as the primary
- C) Active Directory-integrated zone with replication scope set to Forest
- D) Stub zone referencing the authoritative nameserver

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: A standard primary zone stores data in a flat file on disk. It does not replicate automatically via AD replication and creates a single point of failure.
  - Why B is incorrect: A standard secondary zone is a read-only copy that receives zone transfers from a primary. It still requires manual zone transfer configuration and does not leverage AD replication.
  - Why D is incorrect: A stub zone contains only NS and SOA records pointing to authoritative nameservers. It does not store full zone data and cannot serve authoritative DNS responses for the domain.

---

### Question 14 (5 points)

What is the purpose of the `dcpromo.exe` tool in current Windows Server environments?

- A) It is the primary command-line tool for promoting servers to Domain Controllers in Windows Server 2022
- B) It was removed in Windows Server 2012; current deployments use Server Manager or PowerShell AD DS cmdlets
- C) It is a diagnostic tool for validating prerequisites before DC promotion
- D) It is used to demote a DC to a member server in Windows Server 2016 and later

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `dcpromo.exe` has not been the promotion tool since Windows Server 2008 R2. It was officially removed in Windows Server 2012. Using it in a current environment would fail.
  - Why C is incorrect: `dcpromo.exe` was a promotion tool, not a diagnostic validator. The current prerequisite check is built into `Install-ADDSForest` and the Server Manager wizard.
  - Why D is incorrect: DC demotion in Windows Server 2012 and later is performed using `Uninstall-ADDSDomainController`. `dcpromo.exe` is not available for this purpose.

---

### Question 15 (5 points)

After deploying a new DC in a branch office, the administrator notices that `dcdiag /test:Advertising` fails. What does this test check, and what is the most common cause of failure?

- A) It checks whether the DC's IP address is reachable; failure is caused by a firewall blocking ICMP
- B) It checks whether the DC is advertising itself in DNS as a DC; failure is most commonly caused by missing or incorrect DNS SRV records
- C) It checks whether the DC's security certificate is valid; failure is caused by an expired certificate
- D) It checks whether replication from all partners is current; failure is caused by a network outage

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The Advertising test does not check ICMP reachability. It verifies that the DC is advertising its role via DNS service records so clients can locate it as a Domain Controller.
  - Why C is incorrect: DC certificate validation is not what the Advertising test checks. Certificate issues are diagnosed through separate dcdiag tests or the PKI management tools.
  - Why D is incorrect: Replication currency between partners is what the Replications test checks. The Advertising test is specifically about DNS SRV record registration, not replication state.

---

### Question 16 (5 points)

An administrator is deploying an RODC and wants branch office users to be able to authenticate locally even when the WAN is down, but must prevent any Domain Admin credentials from being cached. What is the correct configuration?

- A) Add branch office user accounts to the Allowed RODC Password Replication Group; verify Domain Admins are in the Denied RODC Password Replication Group
- B) Add Domain Admins to the Allowed group and branch users to the Denied group, then reverse the policy after deployment
- C) Leave both groups empty; RODC caches all passwords by default and deletes privileged ones automatically
- D) Configure the RODC with a pre-populated password cache file using `repadmin /prp`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: Adding Domain Admins to the Allowed group would cache their credentials on the RODC, which is specifically what the question requires to be prevented. Reversing after deployment does not uncache already-replicated credentials.
  - Why C is incorrect: The default RODC configuration caches no passwords. Caching requires explicit Allow list entries. The RODC does not selectively delete privileged passwords on its own.
  - Why D is incorrect: `repadmin /prp` queries the password replication policy and reveals cached accounts, but it is not used to pre-populate a cache file. Password caching is controlled by the PRP group membership, not a file.

---

### Question 17 (5 points)

Which SYSVOL replication mechanism replaced the older File Replication Service (FRS) starting with Windows Server 2008?

- A) BranchCache
- B) DFS Replication (DFSR)
- C) Robocopy scheduled tasks
- D) Active Directory Sites and Services zone replication

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: BranchCache is a WAN optimization technology that caches file content locally for branch users. It is not a replication mechanism for SYSVOL or domain system files.
  - Why C is incorrect: Robocopy is a manual file copy utility and is not involved in SYSVOL replication. FRS and DFSR are the automated AD DS replication mechanisms.
  - Why D is incorrect: Active Directory Sites and Services manages AD DS replication topology for directory data. SYSVOL content (GPO templates, scripts) replicates via DFSR, not the AD directory replication engine.

---

### Question 18 (5 points)

An administrator wants to verify what functional level is required before enabling the Active Directory Recycle Bin. Which minimum forest functional level must be met?

- A) Windows Server 2003
- B) Windows Server 2008
- C) Windows Server 2008 R2
- D) Windows Server 2012

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Windows Server 2003 FFL predates the Active Directory Recycle Bin feature entirely. This functional level does not support it.
  - Why B is incorrect: Windows Server 2008 FFL introduced Fine-Grained Password Policies at the domain level and auditing improvements, but not the AD Recycle Bin. The Recycle Bin requires 2008 R2.
  - Why D is incorrect: Windows Server 2012 FFL added Dynamic Access Control and Kerberos armoring. The Recycle Bin was already available at 2008 R2 FFL. Waiting for 2012 is unnecessary.

---

### Question 19 (5 points)

A Domain Controller fails completely and permanently. The administrator must remove its metadata from Active Directory. Which tool performs a clean metadata cleanup?

- A) `repadmin /removelingeringobjects`
- B) `ntdsutil` using the metadata cleanup menu
- C) `adsi edit` — delete the computer account
- D) `Get-ADDomainController -Identity "failedDC" | Remove-ADObject`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `repadmin /removelingeringobjects` removes objects that exist on a replication partner but were deleted on the master. It does not clean up the server metadata of a failed DC.
  - Why C is incorrect: Deleting the computer account in ADSI Edit removes the computer object but not all of the DC's associated metadata objects (NTDS Settings, server objects in Sites and Services, etc.). `ntdsutil` performs the complete cleanup.
  - Why D is incorrect: `Remove-ADObject` removes an AD object but does not clean up all the associated server and NTDS Settings metadata that `ntdsutil` metadata cleanup handles systematically.

---

### Question 20 (5 points)

After promoting a new DC, an administrator wants to verify that it holds a copy of the AD DS database and that the database integrity is intact. Which command checks the database integrity of NTDS.dit on the local DC?

- A) `ntdsutil "activate instance ntds" "files" "integrity" quit quit`
- B) `dcdiag /test:NTDSIntegrity`
- C) `repadmin /checkDB`
- D) `Get-ADDatabase -IntegrityCheck`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `dcdiag /test:NTDSIntegrity` is not a valid dcdiag test name. The dcdiag tool does not include a dedicated NTDS database integrity test.
  - Why C is incorrect: `repadmin /checkDB` is not a valid repadmin command. Database integrity is checked using `ntdsutil`, not repadmin.
  - Why D is incorrect: `Get-ADDatabase` is not a valid PowerShell cmdlet in the Active Directory module. Database integrity checks require `ntdsutil`.
