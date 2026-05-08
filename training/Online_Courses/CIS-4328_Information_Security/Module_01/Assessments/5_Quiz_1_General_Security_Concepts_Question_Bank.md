### 5. Quiz 1: General Security Concepts (Question Bank)
**Question 1**
An organization implements an automated system that checks the hash of system files every hour. If a hash mismatch is detected, an alert is sent to the security operations center. Which pillar of the CIA triad is this control primarily enforcing?
A) Confidentiality
B) Integrity
C) Availability
D) Non-repudiation
*   **Correct Answer:** B) Integrity
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Confidentiality is maintained by encryption (hiding data), not by hashing (checking if data changed).
    *   *Why C is incorrect:* Availability ensures systems are up (like clustering or backups), not checking for unauthorized alterations.
    *   *Why D is incorrect:* Non-repudiation proves *who* took an action (using digital signatures), while hashing only proves *if* the file changed.

**Question 2**
A company requires all employees to sign an Acceptable Use Policy (AUP) before being granted network access. How should this security control be classified?
A) Physical / Corrective
B) Logical / Detective
C) Administrative / Preventive
D) Technical / Corrective
*   **Correct Answer:** C) Administrative / Preventive
*   **Distractor Analysis:**
    *   *Why A is incorrect:* An AUP is a written document (Administrative), not a physical barrier (Physical), and it aims to set rules before bad things happen (Preventive), not fix them after (Corrective).
    *   *Why B is incorrect:* It does not use software to enforce rules automatically (Logical), nor does it alert after the fact (Detective).
    *   *Why D is incorrect:* Technical is synonymous with Logical. An AUP is a managerial policy.
