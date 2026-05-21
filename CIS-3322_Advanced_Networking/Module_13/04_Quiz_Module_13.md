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
Which of the following most accurately describes **queuing mechanisms** in a network QoS context?
*   A) Algorithms that manage which packets are transmitted next when a network interface is congested, ranging from simple first-in-first-out delivery to priority-based and weighted scheduling that protects delay-sensitive traffic.
*   B) The process of examining packet headers to identify traffic types and assign DSCP or CoS markings that downstream devices will use to apply appropriate forwarding treatment.
*   C) A proactive packet-drop mechanism that randomly discards lower-priority packets as a queue fills, triggering TCP senders to reduce their transmission rate before the queue overflows completely.
*   D) A three-step Cisco IOS policy framework consisting of class-maps, policy-maps, and service-policies used to classify, mark, queue, and police traffic on a per-interface basis.
*   **Correct Answer:** A) Algorithms that manage which packets are transmitted next when a network interface is congested, ranging from simple first-in-first-out delivery to priority-based and weighted scheduling that protects delay-sensitive traffic.
*   **Distractor Analysis:**
    * *Why A is correct:* Queuing mechanisms specifically address how packets are ordered and scheduled for transmission during congestion — FIFO, WFQ, PQ, CBWFQ, and LLQ are all queuing algorithms.
    * *Why B is incorrect:* This describes traffic classification and marking, which is a separate QoS function that occurs before queuing.
    * *Why C is incorrect:* This describes WRED (Weighted Random Early Detection), which is a congestion avoidance mechanism — distinct from queuing.
    * *Why D is incorrect:* This describes Cisco's MQC (Modular QoS CLI) framework, which is the configuration model for QoS — not queuing itself.


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
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.


---

**Question 5**
When configuring **Quality of Service (QoS)**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
C) Apply DSCP marking to management traffic and place it in a high-priority queue to ensure management sessions receive preferential treatment over user data flows.
D) Use a dedicated management VLAN with an SVI, applying QoS policies to limit bandwidth available to the management VLAN to reduce exposure.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS encrypt interactive management sessions, preventing plaintext credential capture regardless of network path or QoS configuration.
    * *Why C is incorrect:* Prioritizing management traffic with DSCP improves availability but does not encrypt session data — Telnet traffic in a high-priority queue is still readable in plaintext.
    * *Why D is incorrect:* A dedicated management VLAN adds isolation, but limiting bandwidth to that VLAN does not prevent credential sniffing if Telnet is still in use.
    * *Why B is incorrect:* Port Security restricts MAC-based physical access but has no effect on encrypting management session credentials transmitted over the network.
