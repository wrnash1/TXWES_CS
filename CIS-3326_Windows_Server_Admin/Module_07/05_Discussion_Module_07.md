# Discussion Forum: Module 07 — Active Directory User and Group Management

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

This week's discussion applies Active Directory user and group management concepts
to real-world enterprise design and troubleshooting scenarios. Choose one scenario
below, answer all three sub-questions, and engage substantively with at least
two classmates.

---

## Scenario A — OU Structure and Group Policy Planning for a University

Texas Wesleyan University is migrating from a flat Active Directory structure
(all users in CN=Users) to a properly designed OU hierarchy. The university has
four main groups of users: Faculty, Students, IT Staff, and Service Accounts.
Each group requires different Group Policy settings — for example, Students
should not be able to access Control Panel, Faculty should receive mapped drives
to a research share, and IT Staff should have administrative tools available on
their desktops.

1. Design an OU hierarchy for this university. Describe the structure you would
   create, explain why you placed objects where you did, and identify whether you
   used a function-based, geography-based, or hybrid approach. Explain why your
   chosen approach fits this specific organization.

2. The current flat structure has all user accounts in CN=Users. You cannot link
   Group Policy directly to CN=Users. What steps must you take to migrate the
   existing accounts to your new OU structure, and what PowerShell cmdlet would
   you use to move accounts in bulk from CN=Users to the correct OUs?

3. A junior administrator asks why you used `-ProtectedFromAccidentalDeletion
   $true` on every OU. Explain what this property does, what happens if it is
   not set and an administrator accidentally runs `Remove-ADOrganizationalUnit`,
   and how an administrator would remove this protection before intentionally
   deleting an OU.

Write your initial post in 175-225 words, addressing all three sub-questions with
technical specificity.

---

## Scenario B — AGDLP Design for a Financial Services Firm

A financial services firm has three tiers of employees: Analysts, Senior Analysts,
and Portfolio Managers. The firm has two file shares: a read-only Research Data
share and a read-write Trading Desk share. Analysts should only read from Research
Data. Senior Analysts need read-write access to both shares. Portfolio Managers
need Full Control on the Trading Desk share and read-only access to Research Data.

1. Design a complete AGDLP group structure to satisfy these requirements. Name
   each group you would create, identify its scope and category, and describe
   exactly which groups are nested inside which other groups and which permissions
   are assigned at the resource level.

2. A new Senior Analyst joins the firm. Describe the single administrative action
   required to give this new user the correct access to both shares, and explain
   why AGDLP makes this a single-step operation rather than requiring the
   administrator to touch each share's permission list individually.

3. The firm later acquires a partner company with its own Active Directory domain
   in the same forest. The partner's analysts need the same read-only access to
   the Research Data share. Explain how you would extend your AGDLP design to
   accommodate users from the partner domain without rebuilding the permission
   structure, and which group scope modification or addition is required.

Write your initial post in 175-225 words, addressing all three sub-questions with
technical specificity.

---

## Scenario C — Bulk Provisioning and Account Lifecycle at Scale

A community college is preparing for a new semester. The registrar's office
provides a CSV file with 1,200 new student accounts, including FirstName,
LastName, StudentID, and the OU path where each student should be placed (based
on their program of study). The IT team has one business day to create all
accounts before registration opens.

1. Write a description (not necessarily working code) of the PowerShell approach
   you would use to process the CSV and create all 1,200 accounts. Identify the
   key cmdlets, explain how you would build the sAMAccountName from the CSV data,
   and describe how you would handle duplicate name collisions (for example, two
   students named John Smith).

2. After accounts are created, the IT team discovers that 47 accounts were placed
   in the wrong OU because of a data error in the CSV. Explain which PowerShell
   cmdlet moves accounts between OUs, what information you need to identify each
   account before moving it, and what risk you should be aware of when mass-moving
   accounts (hint: consider Group Policy).

3. At the end of the semester, all graduating student accounts should be disabled
   but not deleted until 90 days have passed. Describe a PowerShell approach that
   would disable all accounts in the `OU=Graduates,OU=Students,OU=TXWES` OU in
   a single operation, and explain why you would choose to disable rather than
   immediately delete.

Write your initial post in 175-225 words, addressing all three sub-questions with
technical specificity.

---

## Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions.

- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each.

- In peer replies: evaluate the accuracy of their group design or OU structure,
  and add one consideration or edge case they did not mention.

---

## Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

## Professor Nash's Note

The AGDLP model is one of those concepts that looks simple in a diagram but
becomes genuinely powerful when you see it working in a large environment.
I have seen organizations that manage permissions by adding individual users
directly to share ACLs — they call it "simple." Then a manager changes
departments and the IT team has to manually audit and update fifteen different
file shares. AGDLP makes that a one-line change. Scenario B is built around a
pattern I use in financial services environments where access tiers and compliance
requirements make clean group nesting essential. For Scenario C — bulk
provisioning duplicate name handling is a real problem in universities. Think
through how you would make sAMAccountNames unique before writing your post.
