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
C) A security control that divides a critical transaction workflow among multiple users to prevent fraud and errors (e.g., one person approves a purchase order, another pays the vendor).
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) A data table stored in a router or network host that lists the paths and network destinations to determine where packets should be forwarded.
B) An efficient mapping technique for complete binary trees where parent-child indices can be computed using simple arithmetic (e.g., parent is (i-1)/2).
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.
    * *Why A is correct:* This describes the exact role and function of **link-state advertisement**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **link-state advertisement**.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
D) traceroute
A) netstat -ano
B) ping
C) nslookup
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **OSPFv2 Routing Concepts & Setup** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **OSPFv2 Routing Concepts & Setup**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable full disk encryption on all client endpoints.
C) Enable full disk encryption on all client endpoints.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..

