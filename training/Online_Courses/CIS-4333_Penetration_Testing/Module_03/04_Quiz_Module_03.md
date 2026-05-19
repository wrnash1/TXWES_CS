# Quiz: Module 03 - Passive Reconnaissance (OSINT)
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Question 1
Which command-line tool is used for passive DNS gathering, specifically retrieving mail server configurations?

*   A) dig example.com MX
*   B) nmap example.com
*   C) ping example.com
*   D) traceroute example.com

---

### Answer Key
*   **Correct Option:** **A**

---

### Explanation
`dig` queries DNS name servers. Passing `MX` retrieves mail records passively without targeting the server directly.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Nmap is active scanning. Ping sends ICMP traffic. Traceroute routes packets.
