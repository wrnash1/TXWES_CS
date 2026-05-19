# Quiz: Module 08 - Exploiting Windows & Active Directory
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Question 1
Which Active Directory attack involves requesting service tickets and attempting to crack the service account password hashes offline?

*   A) Pass-the-Hash
*   B) Kerberoasting
*   C) AS-REP Roasting
*   D) SMB Relay

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
Kerberoasting allows standard AD users to request tickets for service principal names (SPNs) and attempt offline brute-forcing.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Pass-the-hash uses existing hashes to authenticate without cracking them.
