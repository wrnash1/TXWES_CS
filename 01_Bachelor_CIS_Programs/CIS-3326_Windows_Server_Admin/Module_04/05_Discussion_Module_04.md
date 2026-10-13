# Discussion Forum: Module 04 - User, Group, and Computer Accounts in AD

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies user, group, and computer account management concepts to real-world enterprise scenarios. Choose one scenario below, answer all three sub-questions, and engage substantively with at least two classmates.

---

### Scenario A — Group Strategy for a Growing Organization

A regional healthcare company is deploying Active Directory for the first time. They have 400 employees across four departments: Clinical, Administration, IT, and Finance. Multiple file servers host department-specific data. The IT director has proposed giving every user account direct NTFS permission on the files they need, arguing that groups "add unnecessary complexity."

1. Explain why the IT director's direct-assignment approach will become unmanageable as the company grows. Use specific examples of what happens when an employee changes departments or when a new file server share is created.
2. Describe the AGDLP group structure you would design for the Clinical department. Include the specific group names, scopes, and how you would handle both Read and Write access to a Clinical data share.
3. The company plans to add a partner hospital to the forest in 18 months. Explain how the AGUDLP extension accommodates cross-domain access without restructuring the existing permission assignments.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — Service Account Security Audit

A security audit of a financial services company reveals that 12 Windows services are running under a single standard domain user account named `svc_apps`. This account has been given Domain Admin privileges because the developer said "it needs access to everything." The password was set to never expire and has not been changed in three years.

1. Identify at least three specific security risks created by this service account configuration, referencing AD account properties and privilege concepts from this module.
2. Propose a remediation plan using Managed Service Accounts or Group Managed Service Accounts. For services that run on a single server, specify which account type applies. For services that run across a three-node cluster, specify which type applies and what prerequisite must exist in the forest.
3. The account currently has Domain Admin rights. After deploying MSAs and gMSAs with the minimum necessary permissions, what PowerShell commands would you use to audit remaining accounts that still have Domain Admin group membership?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — Computer Account Lifecycle and Stale Object Cleanup

The IT team at a university inherits a domain with 2,000 computer accounts. Based on hardware inventory, only 1,200 machines are currently active. The remaining 800 accounts belong to computers that were retired, stolen, or replaced. Several active computers have users reporting "trust relationship failed" errors on Monday mornings after extended weekends.

1. Explain why stale computer accounts represent a security risk in an AD environment, and what steps should be taken to identify and clean them up safely (without accidentally disabling active machines).
2. The "trust relationship failed" error is occurring on machines that are online and were correctly joined to the domain. What specific condition causes this error, and what is the preferred PowerShell command to fix it without rejoining the domain?
3. A laptop was reported stolen two weeks ago. The security team asks whether the laptop's computer account in AD poses any ongoing security risk if the thief attempts to use it. Explain what access the computer account grants, what the impact of disabling or deleting it is, and what additional security steps should be taken.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each
- In peer replies: evaluate the technical accuracy of their AGDLP design or account type recommendation, and add one consideration they did not address

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

The scenario B situation — one service account with Domain Admin rights running a dozen different applications — is more common in the real world than it should be. I have audited environments where a single compromised service account gave attackers immediate Domain Admin access to 10,000 machines. Managed Service Accounts and Group Managed Service Accounts are one of the most underused security tools in Windows environments. Understanding when and how to use them separates administrators who maintain security posture from those who create vulnerabilities. I look forward to your posts.
