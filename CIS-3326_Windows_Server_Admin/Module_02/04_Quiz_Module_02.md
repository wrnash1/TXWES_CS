# Quiz: Module 02 - Active Directory Domain Services Overview

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Instructions

Select the best answer for each question. Each question is worth 10 points. Review your Reading Guide and video notes before beginning.

---

### Question 1

In an Active Directory environment, what is the purpose of an Organizational Unit (OU)?

A) To create a security and replication boundary between groups of domain controllers.

B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.

C) To act as a standalone server that authenticates users when the primary Domain Controller fails.

D) To synchronize time across all computers in the domain.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Security and replication boundaries are created by domains and forests, not OUs. An OU is a logical container within a single domain and does not create a trust or replication boundary.
  - Why C is incorrect: A server that authenticates users when another DC fails is simply an additional Domain Controller. An OU is a directory container, not a server or role.
  - Why D is incorrect: Time synchronization in a domain is handled by the PDC Emulator FSMO role, not by an OU.

---

### Question 2

After installing the AD DS role via PowerShell, what critical step must be performed before the server can begin authenticating domain users?

A) The server must be promoted to a Domain Controller by running the AD DS Configuration Wizard or `Install-ADDSForest`.

B) The server must be removed from its current workgroup and joined to a domain as a member server.

C) The AD DS schema must be manually extended using ADSI Edit before any users can log in.

D) The Global Catalog service must be disabled on the new server to avoid replication conflicts.

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: A Domain Controller cannot belong to a workgroup or be a domain member — it defines and hosts the domain itself. Joining it as a member server is the opposite of promotion.
  - Why C is incorrect: The AD DS schema is automatically prepared during the promotion process. Manual schema extension with ADSI Edit is not required for basic domain creation.
  - Why D is incorrect: The first DC in a new forest is automatically a Global Catalog server. Disabling it would break forest-wide searches and Universal Group authentication.

---

### Question 3

Which of the following best describes the role of the PDC Emulator FSMO role?

A) It stores a partial read-only copy of all objects in the forest for cross-domain searches.

B) It allocates pools of relative identifiers (RIDs) to other Domain Controllers so they can create new security principals.

C) It acts as the authoritative time source for the domain, processes account lockouts, and handles password change replication with priority.

D) It controls all changes to the Active Directory schema, such as adding new object classes or attributes.

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: That description matches the Global Catalog server, which holds a partial read-only replica of all forest objects — not the PDC Emulator.
  - Why B is incorrect: Allocating RID pools to other DCs is the function of the RID Master FSMO role.
  - Why D is incorrect: Controlling schema changes is the function of the Schema Master FSMO role.

---

### Question 4

A domain has the structure `corp.local` with a child domain `eu.corp.local`. Users in `eu.corp.local` need to access a file share in `corp.local`. Which AD DS feature enables this without manual configuration?

A) An external trust, which must be manually created between the two domains before cross-domain resource access is possible.

B) The two-way transitive trust that is automatically created between parent and child domains during domain promotion.

C) A shortcut trust, which the administrator must create to improve authentication speed between sibling domains.

D) A realm trust, which connects Active Directory domains to non-Windows Kerberos realms.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: External trusts are manually created and are used to connect separate forests or legacy NT domains — not child domains within the same forest.
  - Why C is incorrect: Shortcut trusts are optional manual optimizations for authentication speed. They are not required for basic cross-domain access within the same forest.
  - Why D is incorrect: Realm trusts federate Active Directory with non-Windows Kerberos V5 realms such as MIT Kerberos on Linux — not for Windows domain-to-domain access.

---

### Question 5

An administrator runs `netdom query fsmo` and finds the Infrastructure Master is on a DC that is also a Global Catalog server. In a single-domain forest, why is this acceptable?

A) It is never acceptable; the Infrastructure Master must always be on a non-GC DC.

B) In a single-domain forest, all DCs are effectively GC servers, so the Infrastructure Master placement restriction does not apply.

C) The Infrastructure Master role is obsolete in Windows Server 2016 and later.

D) It is only acceptable if the DC is running Windows Server Datacenter edition.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The restriction applies only in multi-domain forests. In a single-domain forest, all objects are local and all DCs can be GC servers without issue.
  - Why C is incorrect: The Infrastructure Master FSMO role is still active and relevant for multi-domain forests in all current Windows Server versions.
  - Why D is incorrect: FSMO placement guidelines are based on forest topology, not server edition.

---

### Question 6

A branch office has 30 users and limited physical security — the server is in an unlocked storage room. Which Domain Controller type is most appropriate to deploy in this location?

A) A full writable Domain Controller to allow administrators to make directory changes locally.

B) A Read-Only Domain Controller (RODC) to limit the impact of a potential physical compromise.

C) An additional Global Catalog server without the DC role to improve search performance.

D) A Hyper-V host running a virtual DC, which automatically encrypts the AD database.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: A full writable DC in a physically insecure location means a stolen server exposes the entire domain credential database. RODCs are specifically designed for this scenario.
  - Why C is incorrect: A Global Catalog server without the DC role is not a valid configuration. The GC role is a designation on a Domain Controller.
  - Why D is incorrect: Virtualization does not automatically encrypt the AD database. Shielded VMs in Datacenter edition provide VM-level encryption but do not address physical server theft in the way an RODC does.

---

### Question 7

What is the maximum clock skew tolerance in Kerberos authentication before tickets are rejected?

A) 1 minute

B) 5 minutes

C) 10 minutes

D) 30 minutes

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: One minute is too strict. The Kerberos RFC and Windows implementation allow a 5-minute tolerance by default.
  - Why C is incorrect: Ten minutes is the default Kerberos ticket lifetime unit in some configurations, not the clock skew tolerance.
  - Why D is incorrect: Thirty minutes would be far too permissive and would undermine Kerberos replay attack protection.

---

### Question 8

An organization is upgrading its AD DS environment and wants to ensure the Active Directory schema can be extended for a new application. Which FSMO role holder must be online and reachable for this operation to succeed?

A) PDC Emulator

B) RID Master

C) Schema Master

D) Infrastructure Master

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The PDC Emulator handles time synchronization, password changes, and account lockouts — not schema modifications.
  - Why B is incorrect: The RID Master allocates Relative Identifier pools to Domain Controllers for security principal creation — not schema extensions.
  - Why D is incorrect: The Infrastructure Master maintains cross-domain object references — not schema modifications.

---

### Question 9

When a user in `corp.local` logs on to a domain-joined computer, Kerberos must resolve Universal Group memberships before completing the logon token. Which server type provides this information?

A) The PDC Emulator

B) The RID Master

C) The Global Catalog server

D) The Infrastructure Master

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The PDC Emulator provides time synchronization and password change processing — not Universal Group membership data for logon token construction.
  - Why B is incorrect: The RID Master allocates RID pools to Domain Controllers — it plays no role in logon token construction.
  - Why D is incorrect: The Infrastructure Master maintains cross-domain object references — it does not provide Universal Group membership lookups during logon.

---

### Question 10

An administrator needs to verify which Domain Controller holds the PDC Emulator role using a single PowerShell command. Which command returns this information along with all domain FSMO roles?

A) `Get-ADForest | Select-Object SchemaMaster, DomainNamingMaster`

B) `Get-ADDomain | Select-Object PDCEmulator, RIDMaster, InfrastructureMaster`

C) `Get-ADDomainController -Filter { IsPDCEmulator -eq $true }`

D) `Test-ADServiceAccount -Identity PDCEmulator`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-ADForest` returns the two forest-wide FSMO roles (Schema Master and Domain Naming Master), not the domain-wide roles including PDC Emulator.
  - Why C is incorrect: While `Get-ADDomainController` can filter on properties, `IsPDCEmulator` is not a valid filter property for this cmdlet. The correct property is returned by `Get-ADDomain`.
  - Why D is incorrect: `Test-ADServiceAccount` tests a Managed Service Account, not an FSMO role holder.

---

### Question 11 (5 points)

An administrator needs to create a new child domain `west.corp.local` in an existing forest. Which FSMO role holder must be reachable for this operation to succeed?

- A) PDC Emulator of the parent domain
- B) Schema Master of the forest
- C) Domain Naming Master of the forest
- D) Infrastructure Master of the parent domain

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The PDC Emulator handles time synchronization, password changes, and account lockouts within its domain. It plays no role in adding new domains to the forest.
  - Why B is incorrect: The Schema Master controls schema extensions (new object classes and attributes). Creating a new child domain does not require a schema modification.
  - Why D is incorrect: The Infrastructure Master maintains cross-domain object references within its domain. It does not control whether new domains can be added to the forest.

---

### Question 12 (5 points)

A user in a multi-domain forest reports that their group memberships appear incomplete after being moved from one domain to another. Which FSMO role is responsible for maintaining these cross-domain object references?

- A) Schema Master
- B) RID Master
- C) Infrastructure Master
- D) Domain Naming Master

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: The Schema Master controls changes to the directory schema definition. It has no role in tracking cross-domain object references after objects move.
  - Why B is incorrect: The RID Master allocates Relative Identifier pools to Domain Controllers for creating new security principals. It does not track cross-domain references.
  - Why D is incorrect: The Domain Naming Master controls the addition and removal of domains from the forest. It does not resolve or maintain cross-domain group membership references.

---

### Question 13 (5 points)

Which PowerShell command correctly creates a new Organizational Unit named "Marketing" as a child of the "Departments" OU in the `corp.local` domain?

- A) `New-ADOrganizationalUnit -Name "Marketing" -Path "OU=Departments,DC=corp,DC=local"`
- B) `Add-ADOrganizationalUnit -Name "Marketing" -Parent "Departments"`
- C) `New-ADObject -Type OU -Name "Marketing" -Container "Departments"`
- D) `Set-ADOrganizationalUnit -Name "Marketing" -Path "Departments,corp.local"`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `Add-ADOrganizationalUnit` is not a valid PowerShell cmdlet in the Active Directory module. The correct cmdlet is `New-ADOrganizationalUnit`.
  - Why C is incorrect: While `New-ADObject` can technically create objects of any type, using it to create an OU without specifying the `-Path` in LDAP distinguished name format would fail. The dedicated `New-ADOrganizationalUnit` cmdlet with a proper `-Path` is the correct approach.
  - Why D is incorrect: `Set-ADOrganizationalUnit` modifies an existing OU; it does not create a new one. Additionally, the `-Path` value is not in valid LDAP distinguished name format.

---

### Question 14 (5 points)

What is the name and default file path of the Active Directory domain database on a Windows Server Domain Controller?

- A) `AD.mdb` located at `C:\Windows\System32\`
- B) `NTDS.dit` located at `C:\Windows\NTDS\`
- C) `ActiveDirectory.db` located at `C:\AD\Database\`
- D) `Domain.mdf` located at `C:\Program Files\AD DS\`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `AD.mdb` is not the name of the Active Directory database. The file is named `NTDS.dit` (NT Directory Services Directory Information Tree).
  - Why C is incorrect: `ActiveDirectory.db` is not the name or location of the AD database. The correct file is `NTDS.dit` in `C:\Windows\NTDS\`.
  - Why D is incorrect: The AD database is not stored in Program Files. The standard location is `C:\Windows\NTDS\`, and the file is not a SQL Server `.mdf` file.

---

### Question 15 (5 points)

A technician runs `dcdiag /test:replications` and finds replication errors between two Domain Controllers. Which tool should the administrator use next to view the detailed Active Directory replication topology and check the status of inbound replication partners?

- A) `repadmin /showrepl`
- B) `netdom query dc`
- C) `Get-ADDomainController -Filter *`
- D) `nltest /dsgetdc`

- **Correct Answer:** A
- **Distractor Analysis:**
  - Why B is incorrect: `netdom query dc` lists Domain Controllers in the domain but provides no replication topology or error detail.
  - Why C is incorrect: `Get-ADDomainController -Filter *` lists DC properties including site membership but does not display replication topology or partner replication status.
  - Why D is incorrect: `nltest /dsgetdc` locates a Domain Controller for a specified domain (like a DC locator tool) and does not display replication status or topology.

---

### Question 16 (5 points)

In Active Directory, which port does LDAP use by default for unencrypted directory queries?

- A) 443
- B) 636
- C) 389
- D) 3268

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Port 443 is HTTPS. It is not used by standard LDAP queries. Active Directory Web Services uses port 9389 for PowerShell remoting.
  - Why B is incorrect: Port 636 is LDAPS (LDAP over SSL/TLS) — the encrypted version of LDAP. The question asks for the unencrypted default.
  - Why D is incorrect: Port 3268 is the Global Catalog port for LDAP queries that span all domains in the forest. It is not the standard single-domain LDAP port.

---

### Question 17 (5 points)

An administrator runs `Install-ADDSForest` and is prompted for the Safe Mode Administrator Password. What is this password used for?

- A) It sets the initial password for the domain Administrator account used for normal domain logins
- B) It is the recovery password used to log into Directory Services Restore Mode (DSRM) when the AD database needs to be repaired
- C) It encrypts the NTDS.dit database at rest using BitLocker
- D) It authenticates the Schema Master before allowing the forest creation to proceed

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The DSRM password is separate from the domain Administrator account password. The domain Administrator password is set when the first user account is created or inherited from the local Administrator account during promotion.
  - Why C is incorrect: The DSRM password has no relationship to BitLocker encryption of the NTDS.dit database. BitLocker is configured separately if at-rest encryption is required.
  - Why D is incorrect: The Schema Master authentication is handled by Active Directory's own Kerberos/LDAP authentication, not by the DSRM password.

---

### Question 18 (5 points)

A user reports they cannot log on to the domain and receives a "time difference" error. Other users logging on through the same Domain Controller are unaffected. What is the most likely cause?

- A) The user's account has expired in Active Directory
- B) The user's workstation clock is more than 5 minutes out of sync with the domain time
- C) The Domain Controller's RID pool has been exhausted
- D) The user's account is in an OU with a GPO that blocks interactive logon

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: An expired account produces an "account has expired" error, not a "time difference" error. Kerberos clock skew errors are specifically tied to clock synchronization, not account expiration.
  - Why C is incorrect: An exhausted RID pool prevents new security principals from being created. It does not prevent existing user accounts from authenticating.
  - Why D is incorrect: A GPO blocking interactive logon would produce an access denied or policy restriction error, not a "time difference" message. Time difference errors are explicitly related to Kerberos clock skew.

---

### Question 19 (5 points)

Which of the following is the correct Distinguished Name (DN) format for a user account named "jsmith" in the IT OU under Departments in the `corp.local` domain?

- A) `corp.local/Departments/IT/jsmith`
- B) `CN=jsmith,OU=IT,OU=Departments,DC=corp,DC=local`
- C) `jsmith@IT.Departments.corp.local`
- D) `CORP\jsmith\OU=IT`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This format resembles a file system path and is not valid LDAP Distinguished Name syntax. DN uses attribute=value pairs separated by commas.
  - Why C is incorrect: This resembles a UPN (User Principal Name) format but is not a valid UPN or DN. UPNs use `@` with the domain suffix, not the OU path.
  - Why D is incorrect: `CORP\jsmith` is a down-level logon name (SAM account name format), not a Distinguished Name. DNs use the LDAP attribute=value format.

---

### Question 20 (5 points)

An administrator wants to delegate the ability to reset passwords for users in the `HR` OU to a help desk group, without granting them Domain Admin rights. Which AD DS feature enables this?

- A) Fine-Grained Password Policy applied to the HR OU
- B) Delegation of control on the OU using the Delegation of Control Wizard or `dsacls`
- C) Assigning the help desk group to the Account Operators built-in group
- D) Modifying the Default Domain Policy GPO to include the help desk group in the password reset permission

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Fine-Grained Password Policies define different password complexity or lockout rules for specific users or groups. They do not grant administrative permissions to other accounts.
  - Why C is incorrect: Account Operators is a built-in group with domain-wide permissions to manage most user accounts. Assigning the help desk to Account Operators gives broader permissions than the targeted OU-level delegation required here.
  - Why D is incorrect: The Default Domain Policy GPO controls password and account lockout policies for the domain. It does not contain permission settings that grant one group the ability to reset another group's passwords.
