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
