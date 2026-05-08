### 5. Quiz 2: Active Directory (Question Bank)
**Question 1**
In an Active Directory environment, what is the purpose of an Organizational Unit (OU)?
A) To create a boundary for password policies across the entire forest.
B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
C) To act as a standalone server that authenticates users when the primary Domain Controller fails.
D) To synchronize time across all computers in the domain.
*   **Correct Answer:** B) To group users, computers, and other objects to delegate administrative control and apply Group Policy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Password policies are traditionally applied at the Domain level, not the OU level (though Fine-Grained Password Policies allow targeting specific groups, OUs are primarily for management delegation and GPO linking).
    *   *Why C is incorrect:* A standalone server that authenticates users is a Backup Domain Controller (or simply another DC in modern AD), not an OU. An OU is a logical container, not a physical server.
    *   *Why D is incorrect:* Time synchronization in a domain is handled by the PDC Emulator FSMO role, not an OU.

**Question 2**
After installing the Active Directory Domain Services (AD DS) role via Server Manager or PowerShell, what critical step must be performed before the server can begin authenticating users?
A) The server must be promoted to a Domain Controller.
B) The server must be joined to a workgroup.
C) The schema must be manually modified using ADSI Edit.
D) The Global Catalog service must be disabled.
*   **Correct Answer:** A) The server must be promoted to a Domain Controller.
*   **Distractor Analysis:**
    *   *Why B is incorrect:* Domain Controllers cannot belong to a workgroup; they define the domain.
    *   *Why C is incorrect:* The schema is automatically modified/prepared during the promotion process; manual modification is rarely required for initial setup.
    *   *Why D is incorrect:* The first Domain Controller in a new forest is automatically configured as a Global Catalog server, and disabling it would break functionality.
