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
