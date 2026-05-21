# Quiz: Module 06 - EtherChannel Link Aggregation
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which protocol is the open standard for dynamically negotiating EtherChannel links?
*   A) PAgP
*   B) LACP
*   C) RSTP
*   D) VTP
*   **Correct Answer:** B) Link Aggregation Control Protocol (LACP) is the open-standard (IEEE 802.3ad) link aggregation protocol.
*   **Distractor Analysis:**
    *   *Why correct:* Link Aggregation Control Protocol (LACP) is the open-standard (IEEE 802.3ad) link aggregation protocol.
    *   PAgP is Cisco-proprietary. RSTP is spanning tree. VTP propagates VLANs.

---

**Question 2**
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **LACP vs PAgP**?
C) The core operations of a queue: 'enqueue' appends an element to the back, and 'dequeue' removes and returns the front element.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
D) The operational principle of a stack, where the element added most recently is the first one to be removed, similar to a stack of trays.
B) The node or router interface on a network that serves as an access point to other logical networks or the internet.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.
    * *Why A is correct:* This describes the exact role and function of **LACP vs PAgP**.
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **LACP vs PAgP**.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
D) ping
A) traceroute
C) netstat -ano
B) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **EtherChannel Link Aggregation** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range..
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a system for **EtherChannel Link Aggregation**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Enable full disk encryption on all client endpoints.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Enable full disk encryption on all client endpoints.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.

