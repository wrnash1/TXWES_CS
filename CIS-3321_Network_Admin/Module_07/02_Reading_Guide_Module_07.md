# Reading Guide: Module 07 - WAN and Cloud Connectivity
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 07 – WAN and Cloud Connectivity**! Wide area network technologies and cloud service models are tested throughout the CompTIA Network+ N10-009 exam. You must understand the major WAN circuit types, how VPNs create secure tunnels across public networks, and the three primary cloud service and deployment models. This module bridges the gap between LAN knowledge and the internet-scale infrastructure that connects enterprise sites and cloud providers.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **WAN (Wide Area Network)**: A network that spans geographically separate locations — typically connecting branch offices, data centers, and the internet. WANs use carrier-provided circuits such as MPLS, metro Ethernet, leased lines, or broadband.
*   **MPLS (Multiprotocol Label Switching)**: A carrier WAN technology that forwards packets using short fixed-length labels rather than full IP routing at every hop. Provides predictable latency and quality of service, commonly used for enterprise site-to-site connectivity.
*   **Metro Ethernet**: A WAN service delivered over Ethernet standards at carrier scale, connecting sites within a metropolitan area. Offers scalable bandwidth and familiar Ethernet interfaces to customer equipment.
*   **Leased Line (T1/T3)**: A dedicated point-to-point circuit providing fixed bandwidth (T1 = 1.544 Mbps; T3 = 44.736 Mbps) leased from a carrier. Always available, not shared — used for predictable-latency WAN connections.
*   **DSL (Digital Subscriber Line)**: Broadband WAN technology over existing copper telephone lines. ADSL (Asymmetric DSL) provides higher download than upload speeds. Limited by distance from the central office.
*   **Cable (DOCSIS)**: Broadband WAN technology over coaxial cable television infrastructure. Uses DOCSIS (Data Over Cable Service Interface Specification) standards. Bandwidth is shared among neighborhood subscribers.
*   **Fiber WAN**: WAN connectivity delivered over fiber optic infrastructure. Includes services like Ethernet over Fiber and GPON. Offers the highest bandwidth and lowest latency among consumer and enterprise broadband options.
*   **SD-WAN (Software-Defined WAN)**: A WAN architecture that uses software to centrally manage and route traffic across multiple underlying links (MPLS, broadband, LTE) based on application policies rather than static routing. Reduces dependency on expensive MPLS circuits.
*   **VPN (Virtual Private Network)**: A technology that creates an encrypted tunnel over a public network (typically the internet) to connect remote users or sites securely. Provides confidentiality, integrity, and authentication for WAN traffic.
*   **IPsec (Internet Protocol Security)**: A suite of protocols that authenticates and encrypts IP packets. Operates in Tunnel mode (encrypts the entire original packet, used for site-to-site VPNs) or Transport mode (encrypts only the payload, used for host-to-host). Uses IKE (Internet Key Exchange) for key negotiation.
*   **SSL/TLS VPN**: A VPN that uses SSL/TLS encryption (port 443) to create a secure tunnel accessible through a web browser or lightweight client. Commonly used for remote-access VPNs because it traverses firewalls and NAT easily.
*   **GRE (Generic Routing Encapsulation)**: A tunneling protocol that encapsulates a wide variety of network layer protocols inside IP tunnels. GRE itself provides no encryption — it is often combined with IPsec for secure tunneling.
*   **IaaS (Infrastructure as a Service)**: A cloud model where the provider delivers virtualized compute, storage, and networking resources on demand. The customer manages the OS, middleware, and applications. Examples: AWS EC2, Azure Virtual Machines.
*   **PaaS (Platform as a Service)**: A cloud model where the provider manages the underlying infrastructure and OS; the customer deploys and manages applications. Examples: Google App Engine, Azure App Service.
*   **SaaS (Software as a Service)**: A cloud model where the provider delivers a fully managed application over the internet. The customer only configures and uses the application — no infrastructure or OS management. Examples: Microsoft 365, Salesforce.
*   **Public Cloud**: Cloud infrastructure owned and operated by a third-party provider, shared among multiple customers (multi-tenant). Resources are accessible over the internet.
*   **Private Cloud**: Cloud infrastructure operated exclusively for a single organization, either on-premises or hosted by a provider. Offers greater control and security.
*   **Hybrid Cloud**: A deployment model combining public and private cloud, with orchestration allowing workloads to move between them. Enables bursting to public cloud when on-premises capacity is exhausted.

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** WAN technologies fall under **Domain 2.0 – Network Implementations (20%)**. Cloud concepts appear in **Domain 1.0 – Networking Concepts (23%)**. Both are heavily scenario-tested.
*   **WAN technology selection scenarios**: The exam describes a business requirement and asks which WAN technology fits. MPLS = predictable latency, QoS, enterprise; DSL/Cable = cost-effective broadband for small sites; SD-WAN = policy-based multi-link management; leased line = guaranteed dedicated bandwidth.
*   **IPsec modes — common exam trap**: Tunnel mode encrypts the ENTIRE original packet (used in site-to-site VPNs where the gateway is the VPN endpoint). Transport mode encrypts only the payload (used between two hosts). Get these backwards and you'll fail the question.
*   **VPN protocol on port 443**: SSL/TLS VPN uses port 443 — the same as HTTPS. This allows it to pass through firewalls that block other VPN ports (like IPsec's UDP 500/4500). The exam may present a scenario where only port 443 is allowed outbound.
*   **Cloud service model responsibility matrix**: IaaS = you manage OS up. PaaS = you manage app up. SaaS = you manage nothing. The exam presents a scenario and asks which model applies. Focus on what the customer manages, not what the provider manages.
*   **Study Resource:** Professor Messer's free [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) covers WAN technologies, VPN types, and cloud models in the Network Implementations section.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters on **WAN Technologies and Cloud Computing** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Pay particular attention to the VPN tunneling mechanisms and the cloud service model comparison.
*   **Required Video:** Watch Professor Messer's **WAN Technologies**, **VPN Technologies**, and **Cloud Models** videos from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).

---

### Lab & Command Integration
In this week's hands-on lab, you will configure a basic IPsec site-to-site VPN tunnel between two virtual routers in Cisco Packet Tracer, verify the tunnel is established using `show crypto isakmp sa` and `show crypto ipsec sa`, and compare the encapsulated packet structure in Tunnel mode versus the unencrypted baseline traffic.

---

### 3. Study Checklist
*   [ ] Know the major WAN circuit types: MPLS, Metro Ethernet, T1/T3, DSL, Cable, Fiber, SD-WAN.
*   [ ] Understand IPsec Tunnel mode vs. Transport mode and when each is used.
*   [ ] Know SSL/TLS VPN (port 443) and why it traverses firewalls more easily than IPsec.
*   [ ] Memorize the three cloud service models (IaaS, PaaS, SaaS) and what the customer manages in each.
*   [ ] Know the three cloud deployment models: Public, Private, Hybrid.
*   [ ] Read the **WAN and Cloud** chapters in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
*   [ ] Watch Professor Messer's WAN and cloud videos from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
*   [ ] Proceed to the weekly hands-on lab activity.
