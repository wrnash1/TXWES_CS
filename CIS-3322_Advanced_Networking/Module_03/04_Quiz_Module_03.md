# Quiz: Module 03 - IPv6 Addressing and Configuration
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
What command enables a Cisco router to forward IPv6 traffic?
*   A) ip routing
*   B) ipv6 address autoconfig
*   C) ipv6 unicast-routing
*   D) ipv6 routing enable
*   **Correct Answer:** C) Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
*   **Distractor Analysis:**
    *   *Why correct:* Cisco routers require the global command `ipv6 unicast-routing` to act as an IPv6 router.
    *   ip routing is for IPv4. autoconfig sets up client address learning. routing enable is invalid syntax.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **EUI-64 configuration**?
C) An access control system where users are assigned to specific roles, and permissions are linked to those roles rather than individual users, simplifying permission management.
B) An algebraic restructuring operation on a binary tree that changes the parent-child relationships to restore balance without violating the search order.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) A deployment model that uses two identical production environments (Blue and Green) to minimize downtime and risk; updates are deployed to the idle environment before routing live traffic.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.
    * *Why A is correct:* This describes the exact role and function of **EUI-64 configuration**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **EUI-64 configuration**.


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
While working on **IPv6 Addressing and Configuration** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..


---

**Question 5**
When designing a system for **IPv6 Addressing and Configuration**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

