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
Which of the following most accurately describes the difference between **LACP and PAgP**?
*   A) LACP is an open standard (IEEE 802.3ad) that works between any vendor's devices, while PAgP is Cisco-proprietary and only works between Cisco switches; both use negotiation modes but with different mode names.
*   B) LACP bundles up to 16 physical links into one logical channel, while PAgP is limited to a maximum of 4 physical links per bundle, regardless of platform.
*   C) LACP operates at Layer 3 and negotiates IP-based link bundles between routers, while PAgP operates at Layer 2 and only works between directly connected switches.
*   D) LACP requires that all member ports share the same VLAN ID, while PAgP allows member ports to belong to different VLANs as long as the port-channel is configured as a trunk.
*   **Correct Answer:** A) LACP is an open standard (IEEE 802.3ad) that works between any vendor's devices, while PAgP is Cisco-proprietary and only works between Cisco switches; both use negotiation modes but with different mode names.
*   **Distractor Analysis:**
    * *Why A is correct:* The primary distinction is vendor interoperability — LACP is the IEEE standard, PAgP is Cisco-only. Mode names differ: LACP uses active/passive; PAgP uses desirable/auto.
    * *Why B is incorrect:* While Cisco platforms often support up to 8 active links per channel, the 16-vs-4 comparison is not the defining difference between LACP and PAgP.
    * *Why C is incorrect:* Both LACP and PAgP operate at Layer 2 between directly connected switches — neither is a Layer 3 protocol.
    * *Why D is incorrect:* Both LACP and PAgP require matching VLAN/trunk configuration on all member ports; neither allows mixed VLAN membership within a bundle.


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
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.


---

**Question 5**
When configuring **EtherChannel Link Aggregation**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Configure SNMPv3 with `authPriv` security level to encrypt SNMP management polling traffic.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Use `service password-encryption` on Cisco IOS devices to obfuscate passwords stored in the running configuration.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS encrypt management session data in transit, preventing credential capture by a packet sniffer on the network.
    * *Why B is incorrect:* Port Security controls physical access by MAC address — it does not encrypt management traffic passing over the network.
    * *Why C is incorrect:* SNMPv3 authPriv encrypts SNMP traffic specifically, but does not address Telnet or HTTP credential exposure.
    * *Why D is incorrect:* `service password-encryption` applies a weak Vigenere cipher to stored passwords in the config — it does not encrypt credentials during transmission.
