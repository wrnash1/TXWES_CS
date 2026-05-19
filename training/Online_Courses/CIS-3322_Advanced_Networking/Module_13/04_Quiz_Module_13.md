# Quiz: Module 13 - Quality of Service (QoS) Fundamentals
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which Layer 3 marking field in the IP header is used for configuring Quality of Service (QoS)?
*   A) Class of Service (CoS)
*   B) Differentiated Services Code Point (DSCP)
*   C) MAC Priority
*   D) VLAN Tag
*   **Correct Answer:** B) DSCP uses 6 bits in the Type of Service (ToS) field of the IPv4 header (Layer 3) to mark packets.
*   **Distractor Analysis:**
    *   *Why correct:* DSCP uses 6 bits in the Type of Service (ToS) field of the IPv4 header (Layer 3) to mark packets.
    *   CoS is a Layer 2 marking found inside 802.1Q tags.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **WFQ)**?
C) The operational principle of a queue, where the first element added is the first one to be removed, mimicking a line at a checkout register.
D) The danger of exhausting the call stack memory allocation when recursive calls are made too deeply or without hitting a base case, crashing the program.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
B) The practice of dividing a single logical network into multiple smaller, manageable subnetwork segments to optimize traffic and enhance security.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **WFQ)**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **WFQ)**.
    * *Why A is correct:* This describes the exact role and function of **WFQ)**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **WFQ)**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
D) netstat -ano
C) nslookup
B) traceroute
A) ping
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.


---

**Question 4**
While working on **Quality of Service (QoS) Fundamentals** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **Quality of Service (QoS) Fundamentals**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Implementing Implement switch Port Security to restrict access to switch ports based on approved MAC addresses. mitigates the risk of Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports..
    * *Why B is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why C is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.
    * *Why D is incorrect:* This does not address the security vulnerability of Unauthorized Port Access.

