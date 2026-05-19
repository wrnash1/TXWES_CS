# Quiz: Module 08 - OSPFv2 Routing Concepts & Setup
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
What wildcard mask corresponds to a standard subnet mask of `255.255.255.252`?
*   A) 0.0.0.3
*   B) 0.0.0.255
*   C) 255.255.255.255
*   D) 0.0.0.7
*   **Correct Answer:** A) Subtracting `255.255.255.252` from `255.255.255.255` yields wildcard `0.0.0.3`.
*   **Distractor Analysis:**
    *   *Why correct:* Subtracting `255.255.255.252` from `255.255.255.255` yields wildcard `0.0.0.3`.
    *   0.0.0.255 is for /24. 0.0.0.7 is for /29.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **link-state advertisement**?
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) A data table stored in a router or network host that lists the paths and network destinations to determine where packets should be forwarded.
D) A structured, seven-step process (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor) created by NIST to help organizations manage cybersecurity risk.
B) The defining rule of a BST: for any given node, all keys in its left subtree must be less than or equal to its key, and all keys in its right subtree must be greater.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why A is correct:* This describes the exact role and function of **link-state advertisement**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
D) traceroute
C) netstat -ano
B) nslookup
A) ping
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.


---

**Question 4**
While working on **OSPFv2 Routing Concepts & Setup** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
D) Reboot the physical machine and wait for services to reload.
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..


---

**Question 5**
When designing a system for **OSPFv2 Routing Concepts & Setup**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

