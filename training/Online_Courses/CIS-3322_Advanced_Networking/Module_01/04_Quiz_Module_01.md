# Quiz: Module 01 - Network Architectures & Topologies
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a three-tier enterprise design, at which layer is routing and policy-based traffic control typically implemented?
*   A) Access Layer
*   B) Distribution Layer
*   C) Core Layer
*   D) Physical Layer
*   **Correct Answer:** B) The Distribution Layer aggregates access switches, enforces policies (ACLs), and handles routing.
*   **Distractor Analysis:**
    *   *Why correct:* The Distribution Layer aggregates access switches, enforces policies (ACLs), and handles routing.
    *   Access layer connects endpoints. Core layer is designed for high-speed packet forwarding.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **spine-leaf topologies.**?
C) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
B) The node or router interface on a network that serves as an access point to other logical networks or the internet.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) The process of adjusting node positions in a binary heap to restore the heap property (min-heap or max-heap) after an insertion or deletion.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **spine-leaf topologies.**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **spine-leaf topologies.**.
    * *Why A is correct:* This describes the exact role and function of **spine-leaf topologies.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **spine-leaf topologies.**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
D) traceroute
B) netstat -ano
A) nslookup
C) ping
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Architectures & Topologies** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Network Architectures & Topologies**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..

