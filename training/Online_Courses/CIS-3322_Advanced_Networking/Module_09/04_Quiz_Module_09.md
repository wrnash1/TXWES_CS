# Quiz: Module 09 - WAN Technologies & VPNs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which IPsec component provides data integrity and origin authentication without confidentiality (encryption)?
*   A) ESP
*   B) AH
*   C) IKE
*   D) Diffie-Hellman
*   **Correct Answer:** B) Authentication Header (AH) handles authentication and integrity. Encapsulating Security Payload (ESP) handles encryption.
*   **Distractor Analysis:**
    *   *Why correct:* Authentication Header (AH) handles authentication and integrity. Encapsulating Security Payload (ESP) handles encryption.
    *   ESP provides encryption. IKE negotiates keys.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **Site-to-Site VPNs**?
D) A binary tree in which every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
B) The absolute maximum time a business process can be disrupted before the organization suffers irreparable damage or failure.
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **Site-to-Site VPNs**.
    * *Why A is correct:* This describes the exact role and function of **Site-to-Site VPNs**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **Site-to-Site VPNs**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **Site-to-Site VPNs**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
D) netstat -ano
B) traceroute
A) ping
C) nslookup
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **WAN Technologies & VPNs** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **WAN Technologies & VPNs**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

