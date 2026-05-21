# Quiz: Module 02 - Active Directory Domain Services (AD DS) Overview

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

In an Active Directory environment, what is the purpose of an Organizational Unit (OU)?

A) To create a security and replication boundary between groups of domain controllers.
B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
C) To act as a standalone server that authenticates users when the primary Domain Controller fails.
D) To synchronize time across all computers in the domain.

* **Correct Answer:** B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
* **Distractor Analysis:**
  * *Why A is incorrect:* Security and replication boundaries are created by domains and forests, not OUs. An OU is a logical container within a single domain and does not create a trust or replication boundary.
  * *Why C is incorrect:* A server that authenticates users when another DC fails is simply an additional Domain Controller. An OU is a directory container object, not a server or role.
  * *Why D is incorrect:* Time synchronization in a domain is handled by the PDC Emulator FSMO role, not by an OU.

---

### Question 2

After installing the Active Directory Domain Services (AD DS) role via Server Manager or PowerShell, what critical step must be performed before the server can begin authenticating domain users?

A) The server must be promoted to a Domain Controller by running the AD DS Configuration Wizard or `Install-ADDSForest`.
B) The server must be removed from its current workgroup and joined to a domain as a member server.
C) The AD DS schema must be manually extended using ADSI Edit before any users can log in.
D) The Global Catalog service must be disabled on the new server to avoid replication conflicts.

* **Correct Answer:** A) The server must be promoted to a Domain Controller by running the AD DS Configuration Wizard or `Install-ADDSForest`.
* **Distractor Analysis:**
  * *Why B is incorrect:* A Domain Controller cannot belong to a workgroup or be a domain member — it defines and hosts the domain itself. Joining it as a member server is the opposite of promotion.
  * *Why C is incorrect:* The AD DS schema is automatically prepared during the promotion process using `adprep`; manual schema extension with ADSI Edit is not required and would be dangerous without proper planning.
  * *Why D is incorrect:* The first Domain Controller in a new forest is automatically designated as a Global Catalog server, and disabling the GC would break forest-wide searches and universal group authentication.

---

### Question 3

Which of the following best describes the role of the PDC Emulator FSMO role in an Active Directory domain?

A) It stores a partial read-only copy of all objects in the forest for cross-domain searches.
B) It allocates pools of relative identifiers (RIDs) to other Domain Controllers so they can create new security principals.
C) It acts as the authoritative time source for the domain, processes account lockouts, and handles password change replication with priority.
D) It controls all changes to the Active Directory schema, such as adding new object classes or attributes.

* **Correct Answer:** C) It acts as the authoritative time source for the domain, processes account lockouts, and handles password change replication with priority.
* **Distractor Analysis:**
  * *Why A is incorrect:* That description matches the Global Catalog server, which holds a partial read-only replica of all forest objects — not the PDC Emulator.
  * *Why B is incorrect:* Allocating RID pools to other DCs is the function of the RID Master FSMO role, not the PDC Emulator.
  * *Why D is incorrect:* Controlling schema changes is the function of the Schema Master FSMO role. Only the Schema Master can authorize modifications to the AD schema.

---

### Question 4

A Windows domain has the following structure: a forest root domain named `corp.local` with a child domain named `eu.corp.local`. Users in `eu.corp.local` need to access a file share hosted in `corp.local`. Which AD DS feature automatically enables this access without any manual configuration?

A) External trust, which must be manually created between the two domains before cross-domain resource access is possible.
B) The two-way transitive trust that is automatically created between parent and child domains during domain promotion.
C) A shortcut trust, which the administrator must create to improve authentication speed between sibling domains.
D) A realm trust, which connects Active Directory domains to non-Windows Kerberos realms for cross-domain access.

* **Correct Answer:** B) The two-way transitive trust that is automatically created between parent and child domains during domain promotion.
* **Distractor Analysis:**
  * *Why A is incorrect:* External trusts are manually created one-way, non-transitive trusts used to connect separate forests or legacy NT domains — not child domains within the same forest, which already have automatic transitive trusts.
  * *Why C is incorrect:* Shortcut trusts are optional manual optimizations that improve authentication speed between domains deep in a forest hierarchy, but they are not required for basic cross-domain access within the same forest.
  * *Why D is incorrect:* Realm trusts are used to federate Active Directory with non-Windows Kerberos V5 realms (such as MIT Kerberos on Linux), not for access between Windows domains in the same forest.

---

### Question 5

An administrator runs `netdom query fsmo` on a Domain Controller and finds that the Infrastructure Master role is held by a Domain Controller that is also a Global Catalog server. In a single-domain forest, why is this configuration acceptable?

A) It is never acceptable; the Infrastructure Master must always be on a DC that is not a Global Catalog server.
B) In a single-domain forest, every DC is effectively a Global Catalog server, so the Infrastructure Master placement restriction does not apply.
C) The Infrastructure Master role is obsolete in Windows Server 2016 and later and can be ignored regardless of placement.
D) It is only acceptable if the DC is running Windows Server Datacenter edition, which lifts FSMO placement restrictions.

* **Correct Answer:** B) In a single-domain forest, every DC is effectively a Global Catalog server, so the Infrastructure Master placement restriction does not apply.
* **Distractor Analysis:**
  * *Why A is incorrect:* The restriction that the Infrastructure Master should not be on a GC server applies only in multi-domain forests. In a single-domain forest, all objects are local and the GC contains all domain objects anyway, making the restriction irrelevant.
  * *Why C is incorrect:* The Infrastructure Master FSMO role is still active and relevant in Windows Server 2016 and later for multi-domain forests; it is not obsolete.
  * *Why D is incorrect:* FSMO placement guidelines are based on forest topology, not server edition. Datacenter vs. Standard edition has no bearing on which FSMO roles can be hosted on a given DC.
