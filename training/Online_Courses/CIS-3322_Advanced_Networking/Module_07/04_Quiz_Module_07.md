# Quiz: Module 07 - Inter-VLAN Routing Solutions
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a Router-on-a-stick topology, how are multiple VLANs terminated on a single physical router interface?
*   A) Using multiple IP addresses on the primary interface
*   B) Creating logical subinterfaces for each VLAN
*   C) Plugging in multiple network cables
*   D) Enabling PortFast on the router link
*   **Correct Answer:** B) Subinterfaces allow partition of a physical interface into multiple virtual interfaces, each handling a VLAN.
*   **Distractor Analysis:**
    *   *Why correct:* Subinterfaces allow partition of a physical interface into multiple virtual interfaces, each handling a VLAN.
    *   A is invalid (only one primary IP). C defeats the purpose of the single trunk link.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Layer 3 Switch SVI configuration.**?
C) A binary search tree that automatically adjusts its height during insertions and deletions (e.g., AVL, Red-Black) to maintain logarithmic operations.
D) The final node in a linked list, whose next pointer typically references null (or the head node in a circular list), marking the end of the chain.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.
    * *Why A is correct:* This describes the exact role and function of **Layer 3 Switch SVI configuration.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
C) traceroute
D) netstat -ano
A) nslookup
B) ping
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Inter-VLAN Routing Solutions** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Inter-VLAN Routing Solutions**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

