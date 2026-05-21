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
In the context of standard IT systems, which of the following is the most accurate definition of the concept or parameter **queuing mechanisms (FIFO**?
D) An operation in Red-Black trees where nodes are flipped between red and black to maintain structural invariants after insertions or deletions.
A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
C) Web Content Accessibility Guidelines; international standards ensuring web content is usable for people with disabilities (e.g., screen reader compatibility, color contrast).
B) The mathematical expectation of an algorithm's performance across all possible inputs of size N, representing typical real-world runtime behavior.
*   **Correct Answer:** A) A critical parameter and standard protocol utilized to enforce access rules, manage data flow, or verify integrity within networking operations.
*   **Distractor Analysis:**
    * *Why D is incorrect:* This option represents an alternative operational definition that does not apply to **queuing mechanisms (FIFO**.
    * *Why A is correct:* This describes the exact role and function of **queuing mechanisms (FIFO**.
    * *Why C is incorrect:* This option represents an alternative operational definition that does not apply to **queuing mechanisms (FIFO**.
    * *Why B is incorrect:* This option represents an alternative operational definition that does not apply to **queuing mechanisms (FIFO**.


---

**Question 3**
A systems administrator or developer needs to **verify basic network connectivity and latency to a remote host using ICMP Echo Requests**. Which of the following commands is the most appropriate to execute?
B) netstat -ano
A) ping
C) nslookup
D) traceroute
*   **Correct Answer:** A) ping
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `ping` command is directly designed to verify basic network connectivity and latency to a remote host using ICMP Echo Requests.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Quality of Service (QoS) Fundamentals** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
B) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
D) Reboot the physical machine and wait for services to reload.
C) Correct the subnet mask configuration on the interface to match the network segment parameters.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1..
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When designing a system for **Quality of Service (QoS) Fundamentals**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
C) Enable full disk encryption on all client endpoints.
D) Enable full disk encryption on all client endpoints.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why D is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why B is incorrect:* This does not address the security vulnerability of Unencrypted Traffic Exposure.
    * *Why A is correct:* Implementing Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP. mitigates the risk of Attackers capturing plaintext management passwords or session data using network sniffers..

