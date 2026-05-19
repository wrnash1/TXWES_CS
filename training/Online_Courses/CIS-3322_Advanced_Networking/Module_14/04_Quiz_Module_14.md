# Quiz: Module 14 - Network Automation & REST APIs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a Software-Defined Networking architecture, which API is used to communicate between the controller and the application layer?
*   A) Southbound API
*   B) Northbound API
*   C) Eastbound API
*   D) OpenFlow
*   **Correct Answer:** B) Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
*   **Distractor Analysis:**
    *   *Why correct:* Northbound APIs connect the controller to applications and orchestration tools. Southbound APIs connect to network devices.
    *   OpenFlow is a southbound protocol.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **JSON/XML data formats.**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) The scenario where an algorithm requires the absolute minimum number of steps to complete (e.g., searching for an element that happens to be at the very beginning of a list).
C) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
B) The difference in height between the left and right subtrees of a node in an AVL tree, which must be -1, 0, or 1 to remain balanced.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **JSON/XML data formats.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **JSON/XML data formats.**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
D) netstat -ano
A) nslookup
B) ping
C) traceroute
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Automation & REST APIs** in a production environment, you encounter a system alert indicating a **Subnet Mask Mismatch** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why B is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why C is incorrect:* This action does not resolve the root cause of Subnet Mask Mismatch.
    * *Why A is correct:* Because A host is configured with an incorrect subnet mask, preventing it from identifying local vs. remote addresses. The appropriate fix is to Correct the subnet mask configuration on the interface to match the network segment parameters..


---

**Question 5**
When designing a system for **Network Automation & REST APIs**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..

