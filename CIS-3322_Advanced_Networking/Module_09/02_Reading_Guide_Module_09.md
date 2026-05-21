# Reading Guide: Module 09 - WAN Technologies & VPNs
## Course: CIS-3322_Advanced_Networking (Cisco CCNA (200-301))

---

### Introduction
Welcome to **Module 09 - WAN Technologies & VPNs**! This week's study material focuses on the core foundations and configuration mechanics of **WAN Technologies & VPNs** as aligned with the **Cisco CCNA (200-301)** certification framework. Understanding these topics is essential not only for passing the certification exam but also for administering enterprise systems in real-world environments.

As a student, you will learn the primary operational roles, command syntaxes, and troubleshooting parameters needed to design, configure, and maintain these services. We will explore how different protocols establish connections, how configurations manage resource allocation, and how security controls prevent access breaches. Make sure to complete the checklists and review the glossary terms in detail before beginning the lab activity.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Metro Ethernet**: A WAN technology that extends Ethernet services over a carrier's metropolitan area network, offering E-Line (point-to-point), E-LAN (multipoint-to-multipoint), and E-Tree (hub-and-spoke) service types. Metro Ethernet allows organizations to use familiar Ethernet interfaces on their CPE (customer premises equipment) while the provider handles the underlying transport infrastructure.
*   **Site-to-Site VPNs**: A permanent encrypted tunnel between two network sites, typically established between two router or firewall endpoints over the public internet. IPsec is the most common framework used, providing authentication, data integrity, and encryption for all traffic traversing the tunnel. Unlike remote access VPNs, site-to-site VPNs are always on and connect entire networks (not individual users).
*   **GRE tunnels**: Generic Routing Encapsulation (GRE) is a Cisco tunneling protocol that encapsulates any Layer 3 protocol within IP packets, allowing routing protocols and multicast traffic to traverse WAN paths that would otherwise block them. GRE tunnels are configured with `interface tunnel [number]`, `tunnel source`, and `tunnel destination` commands. Note: GRE itself provides no encryption — it must be combined with IPsec for security.
*   **IPsec framework components**: IPsec is a suite of protocols providing secure IP communications. Key components include: **IKE (Internet Key Exchange)** for negotiating security associations and exchanging keys, **AH (Authentication Header)** for integrity and authentication without encryption, and **ESP (Encapsulating Security Payload)** for encryption, integrity, and authentication. IPsec operates in Transport mode (host-to-host) or Tunnel mode (network-to-network).

---

### 2. Certification Exam Tips
*   **CCNA Domain:** WAN and VPN concepts fall under **WAN Technologies (12.5%)** and **Security Fundamentals (15%)** of the CCNA 200-301 exam. Expect conceptual questions rather than detailed IPsec CLI configuration.
*   **AH vs ESP:** The CCNA exam frequently tests this distinction. **AH** provides authentication and integrity but **no encryption** — traffic is readable in plaintext. **ESP** provides authentication, integrity, **and encryption**. In practice, ESP is almost always used. Remember: AH = Authentication only, ESP = Encryption + Authentication.
*   **GRE key fact:** GRE encapsulates a wide range of protocols and supports multicast/broadcast (which IPsec tunnels do not natively support). This makes GRE ideal for running OSPF or EIGRP across a tunnel. GRE is unencrypted by default.
*   **DMVPN concept:** Dynamic Multipoint VPN (DMVPN) is a Cisco technology that combines GRE, NHRP (Next Hop Resolution Protocol), and IPsec to create scalable hub-and-spoke VPNs with spoke-to-spoke dynamic tunnel capability. The CCNA exam tests awareness of DMVPN concepts, not full configuration.
*   **Study Resource:** Watch the WAN technologies and VPN episodes in the Jeremy's IT Lab CCNA free playlist, which cover GRE tunnel configuration and IPsec conceptual review: [Jeremy's IT Lab CCNA Complete Course on YouTube](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ). Look for "WAN Architecture" and "VPN" episodes.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the section covering **WAN Technologies and VPNs** in the Cisco Skills for All CCNA course. The content covers WAN connectivity options, VPN types, and IPsec framework components with clear diagrams: [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/). Navigate to "CCNA: Enterprise Networking, Security, and Automation" — the WAN Concepts chapter.
*   **Required Video:** Watch the WAN and VPN episodes in the Jeremy's IT Lab CCNA complete playlist. The videos explain Metro Ethernet, GRE tunnel configuration, and the AH vs ESP distinction with Packet Tracer demonstrations: [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Configure a generic routing encapsulation (GRE) tunnel interface**: Create `interface tunnel 0` on both routers. Set the tunnel mode with `tunnel mode gre ip` (the default). Assign an IP address to the tunnel interface in a separate subnet from any physical interface.
*   **Set tunnel source and destination IPs**: Use `tunnel source [interface or IP]` to specify the local endpoint and `tunnel destination [remote router IP]` to specify the far end. The source and destination must be publicly reachable via the underlying WAN routing.
*   **Test routing protocols across the tunnel**: After configuring the GRE tunnel, run OSPF or a static route pointing to the remote network across the tunnel interface. Use `show interface tunnel 0` and `show ip route` to verify tunnel state and route installation.


---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the section covering **WAN Technologies and VPNs** in [Cisco Skills for All Portal - CCNA Guides](https://skillsforall.com/).
- [ ] Watch the WAN and VPN episodes in [Jeremy's IT Lab CCNA Complete Course](https://www.youtube.com/playlist?list=PLxbwE86jKRgMpuZuLBivzlM8s2Dk5lXBQ).
- [ ] Review the commands outlined in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.
