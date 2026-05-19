# Quiz: Module 06 - EtherChannel Link Aggregation
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which protocol is the open standard for dynamically negotiating EtherChannel links?
*   A) PAgP
*   B) LACP
*   C) RSTP
*   D) VTP
*   **Correct Answer:** B) Link Aggregation Control Protocol (LACP) is the open-standard (IEEE 802.3ad) link aggregation protocol.
*   **Distractor Analysis:**
    *   *Why correct:* Link Aggregation Control Protocol (LACP) is the open-standard (IEEE 802.3ad) link aggregation protocol.
    *   PAgP is Cisco-proprietary. RSTP is spanning tree. VTP propagates VLANs.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **LACP vs PAgP**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) The practice of dividing a single logical network into multiple smaller, manageable subnetwork segments to optimize traffic and enhance security.
D) The memory block allocated on the system stack for a single function call, storing parameters, local variables, and the return address.
B) A two-dimensional CSS layout system that allows developers to design complex grid-based user interfaces with rows and columns, offering precise control over alignment.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **LACP vs PAgP**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
A) netstat -ano
B) ping
D) traceroute
C) nslookup
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **EtherChannel Link Aggregation** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **EtherChannel Link Aggregation**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

