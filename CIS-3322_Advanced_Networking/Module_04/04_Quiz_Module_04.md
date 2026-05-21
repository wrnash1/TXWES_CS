# Quiz: Module 04 - Switching Concepts & VLANs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
Which frame tagging standard is used to carry traffic for multiple VLANs over a single physical switchport connection?
*   A) ISL
*   B) 802.11
*   C) 802.1Q
*   D) LACP
*   **Correct Answer:** C) IEEE 802.1Q is the industry-standard frame-tagging protocol for VLAN trunks.
*   **Distractor Analysis:**
    *   *Why correct:* IEEE 802.1Q is the industry-standard frame-tagging protocol for VLAN trunks.
    *   ISL is Cisco legacy. 802.11 is Wi-Fi. LACP is for EtherChannel.

---

**Question 2**
Which of the following most accurately describes **DTP (Dynamic Trunking Protocol)**?
*   A) A Cisco-proprietary protocol that allows adjacent switch ports to automatically negotiate whether to form an 802.1Q trunk link, using modes such as dynamic auto and dynamic desirable.
*   B) An IEEE standard that allows a switch to forward frames based on destination MAC addresses, building a MAC address table by learning source MAC addresses from incoming frames.
*   C) A Cisco protocol that propagates VLAN configuration information from a VTP server to all VTP client switches in the same management domain across trunk links.
*   D) An IEEE spanning-tree enhancement that places switch ports connected to end hosts directly into a forwarding state, bypassing the normal listening and learning phases.
*   **Correct Answer:** A) A Cisco-proprietary protocol that allows adjacent switch ports to automatically negotiate whether to form an 802.1Q trunk link, using modes such as dynamic auto and dynamic desirable.
*   **Distractor Analysis:**
    * *Why A is correct:* DTP is Cisco-proprietary and handles trunk negotiation between directly connected Cisco switches — security best practice is to disable it on user-facing ports with `switchport nonegotiate`.
    * *Why C is incorrect:* This describes VTP (VLAN Trunking Protocol), which propagates VLAN database information — not trunk negotiation.
    * *Why B is incorrect:* This describes basic Layer 2 switching and MAC address learning, which is a switch forwarding mechanism, not a negotiation protocol.
    * *Why D is incorrect:* This describes PortFast (an STP enhancement), not DTP.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
B) nslookup
A) traceroute
D) ping
C) netstat -ano
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Switching Concepts & VLANs** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
D) Reboot the physical machine and wait for services to reload.
A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Correct Answer:** A) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why B is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why D is incorrect:* This action does not resolve the root cause of IP Address Conflict.
    * *Why A is correct:* Because Two devices on the same physical or logical network segment are configured with the identical IP address. The appropriate fix is to Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.


---

**Question 5**
When configuring **Switching Concepts & VLANs**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Disable DTP on all switch ports with `switchport nonegotiate` to prevent unauthorized trunk formation.
D) Enable VTP transparent mode on all switches to prevent unauthorized VLAN database updates from propagating.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH encrypts all data in the management session, preventing credential sniffing. On Cisco IOS, configure with `line vty 0 4` → `transport input ssh`.
    * *Why B is incorrect:* Port Security restricts physical access by MAC address but does not encrypt management credentials that may be sent in plaintext.
    * *Why C is incorrect:* Disabling DTP is a good hardening practice to prevent VLAN hopping, but it does not address plaintext credential capture.
    * *Why D is incorrect:* VTP transparent mode prevents VLAN propagation attacks but does not address the sniffing of management credentials.
