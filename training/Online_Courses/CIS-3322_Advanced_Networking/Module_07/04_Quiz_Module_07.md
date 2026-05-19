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
B) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
D) A complete binary tree where the key of any parent node is greater than or equal to the keys of its children, guaranteeing the root is always the maximum element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.
    * *Why A is correct:* This describes the exact role and function of **Layer 3 Switch SVI configuration.**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Layer 3 Switch SVI configuration.**.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
C) traceroute
B) nslookup
A) netstat -ano
D) ping
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Inter-VLAN Routing Solutions** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..


---

**Question 5**
When designing a system for **Inter-VLAN Routing Solutions**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

