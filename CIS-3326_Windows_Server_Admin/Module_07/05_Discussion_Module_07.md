# Discussion Forum: Module 07 - File and Print Services

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies File and Print Services concepts to real-world enterprise design and troubleshooting scenarios. Choose one scenario below, answer all three sub-questions, and engage substantively with at least two classmates.

---

### Scenario A — Share and NTFS Permission Design for a Multi-Department Organization

A law firm has three departments: Attorneys, Paralegals, and Billing. Each department has its own shared folder on a Windows Server file server. The IT manager asks you to design the permissions model. Requirements: Attorneys need full access to all three folders. Paralegals need read-only access to the Attorneys folder and full access to the Paralegals folder. Billing needs full access only to the Billing folder.

1. Describe how you would configure Share and NTFS permissions to meet these requirements. Explain specifically which permission level you would set at the Share level and which level at the NTFS level, and why this is the recommended approach rather than enforcing restrictions at both layers simultaneously.

2. An attorney reports they cannot save a file to the Attorneys folder from their workstation, even though they have Full Control on both Share and NTFS. Walk through the three most likely causes you would investigate, in priority order, and describe the diagnostic step for each.

3. The IT manager wants to prevent any user from saving executable (.exe) files to any of the three department shares. Which FSRM feature and which screen type would you configure, and what is the difference between the two available screen types in terms of behavior when a user attempts to save a blocked file?

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario B — DFS Namespace and Replication Design

A healthcare company has two office locations — Dallas and Houston — each with its own file server. The company stores patient intake forms in a folder that both locations need to access and modify. The IT team wants users at both sites to access the data through the single path `\\health.local\PatientFiles`, and the data should be synchronized between the two servers so both sites always have a local copy.

1. Identify which two DFS components are required to satisfy the full requirement (unified path AND synchronized data). Explain what each component provides and why neither component alone is sufficient to meet the complete goal.

2. The company chooses a domain-based namespace. Explain the difference between a domain-based namespace and a stand-alone namespace in terms of how the namespace root is stored, how it is made fault-tolerant, and what the UNC path format looks like for each type.

3. A week after deployment, a paralegal in Dallas edits a patient intake form at the same time a paralegal in Houston edits the same file. Both save their changes. Explain how DFS Replication handles this conflict, where the losing version of the file is stored, and how an administrator would locate and recover the losing version if needed.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Scenario C — File Server Resource Manager and Shadow Copies

A university IT department manages a shared research drive for graduate students. The department is experiencing three problems: students are storing large video files that are consuming all available disk space; occasionally students accidentally delete their thesis drafts; and the IT staff wants to know which file types are most commonly stored on the drive without blocking any file types.

1. Address the disk space problem using FSRM. Explain which FSRM feature you would use, whether you would configure it as a hard or soft type, and justify why you chose that type given that students are working on research and may legitimately need large files temporarily.

2. Address the accidental deletion problem using Shadow Copies. Explain how Shadow Copies work, how students would recover their own deleted files without IT involvement, and what the limitations of Shadow Copies are in terms of what they do and do not protect against.

3. Address the file type auditing requirement. Which FSRM feature and screen type provides visibility into what file types are being stored without blocking any files? Describe specifically how this differs from the feature that would be used if the goal were to actively block file types.

Write your initial post in 175-225 words, addressing all three sub-questions with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario, answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates; minimum 60 words each
- In peer replies: evaluate the accuracy of their permission design or FSRM/DFS decision, and add one consideration they did not mention

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

The Share plus NTFS permission interaction is one of the most consistently misunderstood concepts I encounter in new administrators. The shortcut I use in the field: set Share to Full Control for Authenticated Users and never touch it again — then manage everything at the NTFS layer. This way you never have to mentally evaluate two permission layers simultaneously. The DFS Namespace vs. DFS Replication distinction comes up frequently in real environments because people deploy DFSN for the unified path and then wonder why each site's data is different — they needed DFSR too. Scenario B is designed to address exactly that gap. Looking forward to your posts.
