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
Which of the following most accurately describes **GRE (Generic Routing Encapsulation) tunnels**?
*   A) A Cisco tunneling protocol that encapsulates any Layer 3 protocol within IP packets, enabling routing protocols and multicast traffic to traverse WAN links — but providing no native encryption.
*   B) An IPsec transport-mode framework that encrypts only the payload of IP packets between two hosts while preserving the original IP header for routing across the public internet.
*   C) A carrier WAN service that extends Ethernet frames over a metropolitan area network, offering point-to-point (E-Line) and multipoint (E-LAN) connectivity to enterprise customers.
*   D) A Cisco-proprietary VPN technology that uses NHRP and IPsec to create dynamic spoke-to-spoke tunnels in a hub-and-spoke VPN overlay architecture.
*   **Correct Answer:** A) A Cisco tunneling protocol that encapsulates any Layer 3 protocol within IP packets, enabling routing protocols and multicast traffic to traverse WAN links — but providing no native encryption.
*   **Distractor Analysis:**
    * *Why A is correct:* GRE is a versatile tunneling protocol that supports multicast (needed for OSPF/EIGRP), but is unencrypted on its own. It is commonly combined with IPsec for security.
    * *Why B is incorrect:* This describes IPsec in transport mode, not GRE. GRE does not provide encryption at all.
    * *Why C is incorrect:* This describes Metro Ethernet, a carrier WAN service type — not GRE.
    * *Why D is incorrect:* This describes DMVPN (Dynamic Multipoint VPN), which uses GRE as one component but is a distinct, more advanced technology.


---

**Question 3**
A systems administrator or developer needs to **map and trace the exact path of router hops packets travel to reach a target destination**. Which of the following commands is the most appropriate to execute?
A) traceroute
B) ping
D) netstat -ano
C) nslookup
*   **Correct Answer:** A) traceroute
*   **Distractor Analysis:**
    * *Why A is correct:* The `traceroute` command is directly designed to map and trace the exact path of router hops packets travel to reach a target destination.
    * *Why B is incorrect:* This command handles alternative administrative tasks.
    * *Why D is incorrect:* This command handles alternative administrative tasks.
    * *Why C is incorrect:* This command handles alternative administrative tasks.


---

**Question 4**
While working on **WAN Technologies & VPNs** in a production environment, you encounter a system alert indicating a **IP Address Conflict** error. Which of the following is the most effective troubleshooting action to resolve this issue?
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
When configuring **WAN Technologies & VPNs**, you must mitigate the risk of **Attackers capturing plaintext management passwords or session data using network sniffers.**. Which of the following security configurations or controls represents the best practice to implement?
C) Implement IPsec ESP tunnel mode between all branch sites to encrypt all inter-site traffic traversing the public WAN.
A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
D) Deploy DMVPN with IPsec to provide encrypted spoke-to-spoke connectivity without requiring full-mesh manual VPN configuration.
B) Implement switch Port Security to restrict access to switch ports based on approved MAC addresses.
*   **Correct Answer:** A) Configure SSH (port 22) for terminal access and HTTPS (port 443) for web interfaces, disabling Telnet and HTTP.
*   **Distractor Analysis:**
    * *Why A is correct:* SSH and HTTPS encrypt the interactive management session itself, preventing credential capture by a sniffer regardless of the network path.
    * *Why C is incorrect:* IPsec ESP encrypts inter-site traffic, but does not protect local management sessions where Telnet is used on the device console or VTY lines.
    * *Why D is incorrect:* DMVPN with IPsec is a scalable WAN solution, but does not address the risk of plaintext management credentials being sniffed during Telnet sessions.
    * *Why B is incorrect:* Port Security restricts physical port access by MAC address and has no effect on management session encryption.
