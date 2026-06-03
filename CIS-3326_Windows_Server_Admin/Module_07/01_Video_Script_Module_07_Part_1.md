# Video Script: Module 07 — Active Directory User and Group Management (Part 1 of 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Microsoft Windows Server Administration

---

## Introduction

Welcome back to CIS-3326 Windows Server Administration.

I am Professor Nash, and in Module 07 we are covering one of the most essential
day-to-day skills for any Windows Server administrator: managing users and groups
inside Active Directory.

By the end of this two-part module, you will understand how Active Directory
organizes its objects, why group types and scopes matter, and how to automate
provisioning at scale using PowerShell.

Part 1 covers concepts, architecture, and planning. Part 2 puts those concepts
to work with hands-on GUI and PowerShell demonstrations.

Let us start with the big picture.

---

## Section 1: Active Directory Object Model

Active Directory is a hierarchical directory service built on the LDAP protocol.
Everything stored in Active Directory — users, computers, printers, groups — is
called an **object**.

Objects are organized inside containers. The most flexible and important container
type is the **Organizational Unit**, abbreviated OU.

Think of OUs as folders inside a filing cabinet. You can nest them to mirror your
company's geography, departments, or administrative boundaries. An OU named
**Sales** might contain a child OU named **Sales-East** and another named
**Sales-West**.

OUs serve two critical purposes:

- They give you a logical structure for delegation of administrative control.

- They are the attachment points for Group Policy Objects, which we cover in
  Module 08.

Containers also exist — the built-in **Users** and **Computers** containers you
see when you open Active Directory Users and Computers. But these built-in
containers cannot have Group Policy linked to them, and you cannot delegate
control as granularly. For any real environment, you should move objects into
proper OUs.

---

## Section 2: Designing an OU Structure

Before you create a single user account, you need a plan. A poorly designed OU
structure causes headaches for years. A well-designed one simplifies everything
from daily administration to disaster recovery.

There are two primary OU design strategies:

**Geography-based structure** — Top-level OUs represent locations: Dallas,
Chicago, New York. Sub-OUs represent departments within each location. This
works well when IT administration is decentralized and each location manages
its own users.

**Function-based structure** — Top-level OUs represent departments: IT, Finance,
HR, Operations. Sub-OUs represent object types or roles within each department.
This works well for centralized IT organizations.

Many enterprises use a hybrid. For our lab environment at Texas Wesleyan, we will
use a function-based structure under a root OU named **TXWES**.

A typical lab OU tree looks like this:

```
TXWES (root OU)
├── IT
│   ├── Admins
│   └── Helpdesk
├── Faculty
├── Students
└── ServiceAccounts
```

Pause here for a moment and think about your own organization or a hypothetical
company. What OU structure would make sense? There is no single correct answer,
but the design decision affects everything downstream.

---

## Section 3: User Account Fundamentals

A user account in Active Directory represents a person — or in the case of a
service account, an application or service — that needs to authenticate and
access resources.

Every user object has a **distinguished name** that encodes its exact location
in the directory hierarchy. For example:

```
CN=jsmith,OU=IT,OU=TXWES,DC=txwes,DC=edu
```

This tells you the user jsmith lives in the IT OU inside TXWES inside the
txwes.edu domain.

Key attributes on a user object include:

- **sAMAccountName** — the pre-Windows 2000 logon name, also called the
  "username." Must be unique in the domain. Maximum 20 characters.

- **userPrincipalName (UPN)** — the email-style logon name such as
  jsmith@txwes.edu. Preferred for modern authentication. Must be unique in
  the forest.

- **displayName** — the friendly name shown in address books.

- **employeeID** — useful for linking AD accounts to HR systems.

- **manager** — links to another user object, enabling org chart features.

When planning user accounts, you should establish a consistent naming convention.
Common conventions are:

- First initial plus last name: jsmith

- First name plus period plus last name: john.smith

- Last name plus first initial: smithj

Pick one convention and stick to it. Inconsistency causes confusion and breaks
automation scripts.

---

## Section 4: Group Types

Active Directory supports two types of groups, and understanding the difference
is critical for both the exam and real-world administration.

### Security Groups

Security groups are used to control access to resources. You add a security group
to an NTFS permission or a share permission, and every member of that group
inherits that access. Security groups can also be used as email distribution lists
in Exchange-integrated environments.

Security groups are the type you will use for the vast majority of administrative
tasks — assigning file permissions, controlling software deployment, managing
printer access.

### Distribution Groups

Distribution groups exist solely for email distribution. They cannot be used to
assign permissions to resources. If you have Exchange or Microsoft 365, you use
distribution groups to create mailing lists.

A practical rule of thumb: if you are not sure which type to create, choose a
security group. It can do everything a distribution group does, plus permissions.

---

## Section 5: Group Scopes

Every security group and distribution group has a **scope** that controls where
the group can be used and who can be a member.

There are three scopes:

### Domain Local

A Domain Local group is used to assign permissions to resources within a single
domain. It can contain members from any domain in the forest, from trusted
forests, or from the same domain.

Think of Domain Local groups as the "permission holders" — they live near the
resource and hold the permissions.

### Global

A Global group is used to organize users with similar roles or job functions
within a single domain. It can only contain members from the same domain where
it was created. However, it can be added to Domain Local groups in any domain
in the forest.

Think of Global groups as the "role buckets" — they hold the users who share
a role.

### Universal

A Universal group can contain members from any domain in the forest and can be
assigned permissions in any domain in the forest. Universal group membership is
stored in the Global Catalog, so changes to Universal group membership trigger
Global Catalog replication across all domain controllers.

Use Universal groups sparingly in large forests. Excessive use causes replication
traffic spikes.

---

## Section 6: The AGDLP Strategy

Microsoft recommends a nesting strategy called **AGDLP** for managing access:

- **A** — Accounts (user accounts)

- **G** — Global groups (role-based)

- **DL** — Domain Local groups (resource-based)

- **P** — Permissions (on the actual resource)

The workflow looks like this:

1. You create a Global group called **G_FileShare_ReadOnly** and add user
   accounts to it.

2. You create a Domain Local group called **DL_FinanceShares_Read** and add the
   Global group to it.

3. You assign Read permission on the Finance file share to the Domain Local group.

This nesting model lets you manage access cleanly. When a new employee joins the
Finance team, you add them to the Global group, and they automatically get access
to all the resources that Domain Local group controls.

In forests with multiple domains, the pattern extends to **AGUDLP** — inserting
Universal groups between Global and Domain Local to bridge domain boundaries.

---

## Section 7: Account Management Concepts

Beyond creating accounts, administrators spend significant time managing the
lifecycle of accounts:

**Disabling accounts** — When an employee goes on extended leave or terminates,
you disable the account rather than deleting it immediately. A disabled account
cannot authenticate, but its group memberships and attributes are preserved. This
is important for audit trails and for re-enabling if the employee returns.

**Unlocking accounts** — Account lockout policies lock an account after a defined
number of failed password attempts. Administrators must unlock these accounts,
either manually or through self-service tools.

**Password resets** — One of the most common helpdesk tasks. In Active Directory
Users and Computers, right-click the user and choose Reset Password.

**Moving accounts** — When users change departments, you move their account to
the correct OU so they receive the right Group Policy settings.

**Deleting accounts** — Best practice is to wait 30-90 days after disabling before
deleting, in case the account needs to be restored for audit or access recovery
purposes.

---

## Section 8: Bulk Provisioning Overview

In enterprise environments, you rarely create user accounts one at a time. New
employee onboarding, semester starts at universities, or mergers and acquisitions
can require creating hundreds or thousands of accounts quickly.

The tools for bulk provisioning include:

- **CSV import with PowerShell** — The most flexible and common method. You
  maintain a CSV file with columns like FirstName, LastName, Department, OU,
  and a script loops through each row calling **New-ADUser**.

- **LDIF files** — A low-level import format used with **ldifde.exe**. Rarely
  used in modern environments but still appears on certification exams.

- **CSVDE** — A Microsoft tool for importing and exporting AD objects using CSV
  format. Limited compared to PowerShell.

- **Azure AD Connect / Entra Connect** — In hybrid environments, accounts may be
  sourced from on-premises HR systems and synchronized to the cloud.

In Part 2, we will walk through a complete PowerShell bulk provisioning script
that reads a CSV, creates users, assigns them to groups, and places them in the
correct OUs.

---

## Wrap-Up: Part 1 Summary

Let us review what we covered in Part 1:

- Active Directory uses a hierarchical object model with OUs as the primary
  organizational and administrative containers.

- OU design should be deliberate — function-based, geography-based, or hybrid
  — because it affects Group Policy application and delegation.

- User accounts have key attributes including sAMAccountName, UPN, and
  displayName. Naming conventions should be established before provisioning begins.

- Security groups control access to resources. Distribution groups are for email
  only.

- Group scopes — Domain Local, Global, and Universal — control membership rules
  and where the group can be used to assign permissions.

- The AGDLP strategy is Microsoft's recommended nesting model for scalable
  access management.

- Bulk provisioning using PowerShell and CSV files is the standard approach for
  large-scale account creation.

In Part 2, we move to the command line and GUI to build these structures,
create users, and run bulk provisioning scripts in our lab environment.

See you in Part 2.
