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
Which of the following most accurately describes **wildcard filtering** as used in Cisco ACLs?
*   A) A bit-mask where a 0 bit means the corresponding address bit must match and a 1 bit means any value is accepted, used in ACL and OSPF `network` commands to define address ranges.
*   B) A technique that compares a packet's destination IP address against all routing table entries and selects the route with the most specific (longest) prefix match for forwarding.
*   C) A subnet mask notation used on router interfaces to define the network boundary — calculated by subtracting the prefix length from 32 and allocating the remaining bits as host bits.
*   D) A Cisco IOS keyword that substitutes for `0.0.0.0 255.255.255.255` in an ACL, matching any IP address regardless of its network or host portion.
*   **Correct Answer:** A) A bit-mask where a 0 bit means the corresponding address bit must match and a 1 bit means any value is accepted, used in ACL and OSPF `network` commands to define address ranges.
*   **Distractor Analysis:**
    * *Why A is correct:* Wildcard masks are the inverse of subnet masks. 0 = must match, 1 = ignore. This is the fundamental definition used in both ACLs and OSPF `network` statements.
    * *Why B is incorrect:* This describes longest-prefix match (CIDR routing), not wildcard filtering.
    * *Why C is incorrect:* This describes a regular subnet mask and CIDR notation, not a wildcard mask.
    * *Why D is incorrect:* This describes the `any` keyword in ACLs, which is a shorthand for a full wildcard — not a definition of wildcard filtering itself.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) ping
A) traceroute
C) netstat -ano
D) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Access Control Lists (ACLs)** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When configuring **Access Control Lists (ACLs)**, you must mitigate the risk of **Attackers connecting rogue access points or unauthorized laptops directly to internal switch ports.**. Which of the following security configurations or controls represents the best practice to implement?
C) Apply an extended ACL on the router's LAN interface to block traffic from unrecognized source IP addresses before it enters the routed network.
D) Configure 802.1X port-based authentication on access switches to require valid credentials from any device before granting network access.
A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
B) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Correct Answer:** A) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Distractor Analysis:**
    * *Why A is correct:* Port Security directly prevents unauthorized devices from communicating by locking a switch port to specific MAC addresses, causing a violation action if an unknown device connects.
    * *Why C is incorrect:* An ACL on the router blocks traffic after it has already entered the network at Layer 2 — it cannot prevent a rogue device from physically connecting to a switch port.
    * *Why D is incorrect:* 802.1X is a strong preventive control, but the question scenario specifically concerns switch port-level MAC-based restriction, which Port Security directly addresses.
    * *Why B is incorrect:* SSH/HTTPS secures management sessions but does not prevent unauthorized physical device connections to switch ports.
