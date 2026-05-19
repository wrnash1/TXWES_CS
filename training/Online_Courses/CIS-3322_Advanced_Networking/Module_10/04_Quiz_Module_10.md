# Quiz: Module 10 - Access Control Lists (ACLs)
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Where should a standard access control list typically be applied?
*   A) As close to the source as possible
*   B) As close to the destination as possible
*   C) On the core router only
*   D) On the internet gateway
*   **Correct Answer:** B) Standard ACLs filter traffic based only on source IP, so applying them near the destination prevents blocking good traffic.
*   **Distractor Analysis:**
    *   *Why correct:* Standard ACLs filter traffic based only on source IP, so applying them near the destination prevents blocking good traffic.
    *   Extended ACLs should be applied as close to the source as possible.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **wildcard filtering**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) The maximum acceptable age of data that must be recovered from backup storage to restore operations, representing the limit of tolerable data loss.
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
C) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **wildcard filtering**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **wildcard filtering**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **wildcard filtering**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **wildcard filtering**.


---

**Question 3**
A systems administrator or developer needs to **query DNS servers to verify domain name resolution and retrieve resource records**. Which of the following commands is the most appropriate to execute?
D) traceroute
B) ping
C) netstat -ano
A) nslookup
*   **Correct Answer:** A) nslookup
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `nslookup` command is directly designed to query DNS servers to verify domain name resolution and retrieve resource records.


---

**Question 4**
While working on **Access Control Lists (ACLs)** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Access Control Lists (ACLs)**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..

