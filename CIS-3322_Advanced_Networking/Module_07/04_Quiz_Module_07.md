# Quiz: Module 07 - Inter-VLAN Routing Solutions
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

**Question 1**
In a Router-on-a-stick topology, how are multiple VLANs terminated on a single physical router interface?
*   A) Using multiple IP addresses on the primary interface
*   B) Creating logical subinterfaces for each VLAN
*   C) Plugging in multiple network cables
*   D) Enabling PortFast on the router link
*   **Correct Answer:** B) Subinterfaces allow partition of a physical interface into multiple virtual interfaces, each handling a VLAN.
*   **Distractor Analysis:**
    *   *Why correct:* Subinterfaces allow partition of a physical interface into multiple virtual interfaces, each handling a VLAN.
    *   A is invalid (only one primary IP). C defeats the purpose of the single trunk link.

---

**Question 2**
Which of the following most accurately describes a **Layer 3 Switch SVI (Switched Virtual Interface)**?
*   A) A virtual Layer 3 interface on a multilayer switch that represents a VLAN, configured with an IP address to serve as the default gateway for hosts in that VLAN.
*   B) A physical router interface subdivided into logical virtual channels, each carrying 802.1Q-tagged frames for a separate VLAN over a single trunk link to a switch.
*   C) A loopback interface on a Cisco router used to represent the router's stable management address that stays up regardless of physical interface state.
*   D) A virtual port-channel interface that aggregates multiple physical switch ports into a single logical link for increased bandwidth and redundancy.
*   **Correct Answer:** A) A virtual Layer 3 interface on a multilayer switch that represents a VLAN, configured with an IP address to serve as the default gateway for hosts in that VLAN.
*   **Distractor Analysis:**
    * *Why A is correct:* SVIs (`interface vlan [id]`) are the primary method for inter-VLAN routing on multilayer switches. They require `ip routing` globally and must have at least one active port in the VLAN to come up.
    * *Why B is incorrect:* This describes a router subinterface used in router-on-a-stick configuration — not an SVI.
    * *Why C is incorrect:* This describes a loopback interface, which is a separate IOS construct used for management and routing protocol configuration.
    * *Why D is incorrect:* This describes a port-channel (EtherChannel) interface, which aggregates physical links — not a Layer 3 VLAN interface.


---

**Question 3**
A systems administrator or developer needs to **display all active network connections, listening ports, and corresponding process identifiers**. Which of the following commands is the most appropriate to execute?
C) traceroute
B) nslookup
A) netstat -ano
D) ping
*   **Correct Answer:** A) netstat -ano
*   **Distractor Analysis:**
    * *Why C is incorrect:* This command handles alternative administrative tasks.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why A is correct:* The `netstat -ano` command is directly designed to display all active network connections, listening ports, and corresponding process identifiers.
    * *Why D is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **Inter-VLAN Routing Solutions** in a production environment, you encounter a system alert indicating a **DNS Failure** error. Which of the following is the most effective troubleshooting action to resolve this issue?
C) Release and renew the DHCP lease, or configure a unique static IP address outside the DHCP pool range.
D) Reboot the physical machine and wait for services to reload.
B) Correct the subnet mask configuration on the interface to match the network segment parameters.
A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Correct Answer:** A) Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.
*   **Distractor Analysis:**
    * *Why C is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why D is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why B is incorrect:* This action does not resolve the root cause of DNS Failure.
    * *Why A is correct:* Because The configured DNS server is offline, misconfigured, or unreachable, preventing host name resolution. The appropriate fix is to Change the local network interface settings to use a public DNS resolver like 8.8.8.8 or 1.1.1.1.


---

**Question 5**
When configuring **Inter-VLAN Routing Solutions**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Apply ACLs on the SVI interfaces to restrict which VLANs can send traffic to the management VLAN.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
C) Configure a separate management VLAN (e.g., VLAN 99) and restrict SVI access to that VLAN using an ACL.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS encrypt management credentials in transit, preventing capture by a packet sniffer. Configure with `transport input ssh` on VTY lines and `ip http secure-server`.
    * *Why D is incorrect:* ACLs on SVI interfaces restrict which traffic can reach the management plane, but do not encrypt credentials if Telnet is still permitted.
    * *Why B is incorrect:* Port Security controls physical MAC-based access, not encryption of management traffic on the network.
    * *Why C is incorrect:* A management VLAN isolates management traffic but does not encrypt it — Telnet on a dedicated VLAN is still plaintext.
