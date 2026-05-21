# Quiz: Module 01 - Network Architectures & Topologies
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a three-tier enterprise design, at which layer is routing and policy-based traffic control typically implemented?
*   A) Access Layer
*   B) Distribution Layer
*   C) Core Layer
*   D) Physical Layer
*   **Correct Answer:** B) The Distribution Layer aggregates access switches, enforces policies (ACLs), and handles routing.
*   **Distractor Analysis:**
    *   *Why correct:* The Distribution Layer aggregates access switches, enforces policies (ACLs), and handles routing.
    *   Access layer connects endpoints. Core layer is designed for high-speed packet forwarding.

---

**Question 2**
Which of the following is the most accurate description of a **spine-leaf topology**?
*   A) A two-tier data center design where every leaf switch connects to every spine switch, providing predictable equal-cost multipath paths with no Spanning Tree dependency.
*   B) A hierarchical campus design with three discrete layers — Core, Distribution, and Access — each performing a specific forwarding or policy role.
*   C) A WAN topology where all remote branch sites connect back to a single central hub router, with no direct branch-to-branch links.
*   D) A redundant design where two core switches are connected with a cross-link and each distribution switch dual-homes to both core switches.
*   **Correct Answer:** A) A two-tier data center design where every leaf switch connects to every spine switch, providing predictable equal-cost multipath paths with no Spanning Tree dependency.
*   **Distractor Analysis:**
    * *Why A is correct:* This accurately describes the spine-leaf (two-tier) topology used in modern data centers with full-mesh between leaf and spine tiers.
    * *Why B is incorrect:* This describes the traditional three-tier (Core/Distribution/Access) campus model, not spine-leaf.
    * *Why C is incorrect:* This describes a hub-and-spoke WAN topology, not a data center spine-leaf design.
    * *Why D is incorrect:* This describes a redundant collapsed-core or dual-core campus layout, not the spine-leaf architecture.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
C) ping
B) nslookup
A) netstat -ano
D) traceroute
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Network Architectures & Topologies** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When designing a network for **Network Architectures & Topologies**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
C) Deploy a syslog server and enable logging on all network devices to record connection events and configuration changes.
D) Configure 802.1X port-based authentication to require valid credentials before any device is allowed network access.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security restricts which MAC addresses can communicate on a switchport, directly preventing unauthorized devices from gaining network access.
    * *Why B is incorrect:* SSH/HTTPS encryption protects management sessions but does not prevent a rogue device from physically connecting to a switch port.
    * *Why C is incorrect:* Syslog logging improves visibility but is a detective control, not a preventive control against unauthorized port connections.
    * *Why D is incorrect:* 802.1X is also a valid preventive control, but Port Security is the more direct answer for MAC-based access restriction at the switch level.
