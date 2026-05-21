# Reading Guide: Module 12 - Identity Threat Detection – IAM and Privileged Access
## Course: CIS-4332_Cyber_Analyst (CompTIA CySA+)

---

### Introduction
Welcome to **Module 12 - Identity Threat Detection – IAM and Privileged Access**! This module covers how analysts detect and respond to threats targeting identity and access management systems, including privileged account abuse, orphaned accounts, excessive permissions, and multi-factor authentication gaps. Identity-based attacks are the most common initial access vector in enterprise breaches. These topics are tested under **Domain 1: Security Operations (33%)** of the CompTIA CySA+ CS0-003 exam.

As a student, you will learn to detect privilege escalation, identify orphaned and over-privileged accounts, and interpret IAM audit log events. Complete the glossary review and study checklist before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Privileged Account Abuse**: The misuse of accounts with elevated permissions (local administrator, domain administrator, service accounts, root) to access systems, data, or functions beyond legitimate job requirements. Privileged account abuse is a high-impact threat because attackers who compromise a privileged account can perform lateral movement, disable security controls, and exfiltrate data at scale. Detecting it requires monitoring for privilege use outside normal patterns — after-hours logins, access to sensitive systems the account has never touched before, or bulk data access events.
*   **Orphaned Accounts**: User accounts that remain active in directory systems (Active Directory, LDAP, cloud IAM) after the associated employee has left the organization or changed roles. Orphaned accounts pose a persistent access risk because they are not monitored and their credentials may be known to former employees or accessible through password spraying. CySA+ tests orphaned account identification as part of access review and IAM hygiene questions.
*   **Multifactor Authentication (MFA) Gaps**: Conditions in which MFA is not enforced for high-risk access scenarios — such as remote VPN access, administrative console logins, privileged account usage, or cloud management plane access. MFA gaps allow attackers who have obtained valid credentials (through phishing or credential stuffing) to authenticate successfully without requiring the second factor. CySA+ scenario questions test whether you identify MFA enforcement as the primary control to recommend when credential-based attack risk is described.

---

### 2. Certification Exam Tips
*   **Focus Area – IAM Controls (Domain 1):** CySA+ CS0-003 tests IAM as a primary security operations skill. Know the principle of least privilege (accounts should have only the permissions needed for their job function), separation of duties (no single account should be able to perform a complete high-risk transaction without a second approver), and need to know (data access should be limited to what is required for the task).
*   **Scenario Trap – Orphaned Accounts vs. Dormant Accounts:** An orphaned account belongs to someone who has left the organization — it should be disabled immediately. A dormant account belongs to a current employee who has not logged in recently — it should be reviewed and potentially disabled pending investigation. CySA+ may test the distinction. The correct action for both is investigation followed by disablement, not deletion (for audit trail preservation).
*   **Privileged Access Management (PAM):** PAM solutions vault privileged credentials, require just-in-time access approval, record privileged sessions, and rotate passwords automatically after each use. CySA+ questions may ask which control prevents a compromised service account password from being reused by an attacker — the answer is PAM with automatic credential rotation.
*   **Study Resource:** The CertifyBreakfast CySA+ playlist covers IAM threat detection, privileged access abuse, and access review procedures mapped to CS0-003 objectives: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This free resource includes walkthroughs of directory audit log review and IAM anomaly identification.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **Identity and Access Management** in the OER Textbook: [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/). The official CompTIA reference details IAM risk concepts, privileged access controls, and identity-based threat detection techniques tested on the exam.
*   **Required Video:** Watch the video lecture on **Identity Threat Detection – IAM and Privileged Access** in the official course playlist: [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W). This playlist includes demonstrations of Active Directory audit log review and privileged account anomaly identification.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Audit user directories for accounts inactive for more than 90 days**: Using PowerShell (`Search-ADAccount -AccountInactive -TimeSpan 90`) or a Linux `lastlog` command, generate a list of inactive accounts; classify each as orphaned (departed user) or dormant (current user, inactive); and document the recommended disposition for each account with justification.
*   **Analyze logs for administrative privilege escalations**: Review a provided Windows Security Event Log export filtered to Event IDs 4672 (Special privileges assigned to new logon) and 4728/4732 (Member added to privileged group); identify any accounts that received administrative privileges outside of a documented change window and flag them for investigation.
*   **Review role-based permission mappings for over-privileged accounts**: Using a provided IAM role-to-permission matrix, identify any standard user accounts assigned roles with excessive permissions (e.g., a help desk account with `Domain Admins` membership); document the least-privilege alternative and the risk introduced by the over-assignment.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **Identity and Access Management** in the [CompTIA CySA+ CS0-003 Exam Reference Library](https://www.comptia.org/).
- [ ] Watch the video lecture on **Identity Threat Detection – IAM and Privileged Access** in the [CertifyBreakfast CompTIA CySA+ Complete Playlist](https://www.youtube.com/playlist?list=PL1Y3F-rCypPM3S7PjJvHjTqP684FwJd0W).
- [ ] Review the IAM audit commands and access review steps outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
