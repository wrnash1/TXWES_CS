# Quiz: Module 04 - Active Reconnaissance (Nmap)
## Course: CIS-4333_Penetration_Testing (CompTIA PenTest+)

---

### Question 1
Which Nmap scan type is known as 'stealth' or 'half-open' scanning because it does not complete the 3-way handshake?

*   A) TCP Connect Scan (-sT)
*   B) TCP SYN Scan (-sS)
*   C) UDP Scan (-sU)
*   D) Ping Sweep (-sn)

---

### Answer Key
*   **Correct Option:** **B**

---

### Explanation
SYN scans send SYN packets and listen for SYN-ACK, but respond with RST instead of ACK to keep connections half-open.

---

### Distractor Analysis
*   **Why the incorrect options are wrong:**
    Connect scans complete the handshake, leaving log footprints on target sockets.
