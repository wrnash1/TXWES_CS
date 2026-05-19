# Quiz: Module 09 - Exploiting Linux Systems
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Question 1
Which file permission bit configuration allows an executable to run with the permissions of the file owner (often root)?

*   A) Write Permission
*   B) Sticky Bit
*   C) SUID (Set Owner User ID)
*   D) Execute Bit

---

### Answer Key
*   **Correct Option:** **C**

---

### Explanation
SUID allows binaries to execute using root privileges, creating potential escalation targets if misconfigured.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Sticky bit limits deletions. SGID sets group execution permissions.
