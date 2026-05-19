# Quiz: Module 05 - Spanning Tree Protocol (STP & RSTP)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which criteria is analyzed FIRST during the Root Bridge election process in Spanning Tree?
*   A) System MAC Address
*   B) Port Priority
*   C) Bridge Priority Value
*   D) Link Speed
*   **Correct Answer:** C) STP elects the bridge with the lowest Bridge ID (BID), which begins with the Bridge Priority.
*   **Distractor Analysis:**
    *   *Why correct:* STP elects the bridge with the lowest Bridge ID (BID), which begins with the Bridge Priority.
    *   MAC address is used as a tie-breaker if priorities are equal.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **802.1D vs 802.1w (RSTP).**?
C) A node in a tree structure that has no child nodes (its children point to null), representing the termination points of the branches.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
B) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **802.1D vs 802.1w (RSTP).**.
    * *Why A is correct:* This describes the exact role and function of **802.1D vs 802.1w (RSTP).**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **802.1D vs 802.1w (RSTP).**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **802.1D vs 802.1w (RSTP).**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
B) ping
A) nslookup
D) traceroute
C) netstat -ano
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Spanning Tree Protocol (STP & RSTP)** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Spanning Tree Protocol (STP & RSTP)**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

