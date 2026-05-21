# Reading Guide: Module 01 - Networking Fundamentals and the OSI Model
## Course: CIS-3321 – Network Administration (CompTIA Network+ N10-009)

---

### Introduction
Welcome to **Module 01 – Networking Fundamentals and the OSI Model**! This module establishes the conceptual framework that every other networking topic builds upon. The OSI (Open Systems Interconnection) model is the most heavily tested architecture on the CompTIA Network+ exam. You must be able to identify which layer handles which function, which PDU (Protocol Data Unit) exists at each layer, and which devices and protocols map to each layer — all from a scenario description.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **OSI Model**: A seven-layer conceptual framework developed by ISO that standardizes how data travels from one application to another across a network. Each layer has a distinct function, and understanding which layer a device or protocol operates at is a core exam skill.
*   **Layer 7 – Application**: The layer closest to the end user where application protocols operate (HTTP port 80, HTTPS port 443, SMTP port 25, FTP ports 20/21, DNS port 53, DHCP port 67/68). This layer does not refer to the software application itself, but to the interface between the application and the network.
*   **Layer 6 – Presentation**: Responsible for data formatting, encryption/decryption (TLS/SSL), and character encoding (ASCII, Unicode). Think of it as the translator that makes data readable by the receiving application.
*   **Layer 5 – Session**: Manages the establishment, maintenance, and termination of communication sessions between two hosts. Protocols like NetBIOS and RPC operate here.
*   **Layer 4 – Transport**: Provides end-to-end communication and error recovery. **TCP** (port-based, connection-oriented, reliable, uses three-way handshake: SYN → SYN-ACK → ACK) and **UDP** (connectionless, faster, no guaranteed delivery) both operate here. The PDU at Layer 4 is a **segment** (TCP) or **datagram** (UDP).
*   **Layer 3 – Network**: Responsible for logical addressing (IP addresses) and routing packets across multiple networks. Routers and Layer 3 switches operate here. The PDU is a **packet**.
*   **Layer 2 – Data Link**: Handles physical addressing (MAC addresses) and framing for node-to-node delivery on the same network segment. Switches and bridges operate here. The PDU is a **frame**. Sub-layers: LLC (Logical Link Control) and MAC (Media Access Control).
*   **Layer 1 – Physical**: Transmits raw bits over the physical medium (cables, fiber, radio waves). Hubs, repeaters, and cables operate here. The PDU is a **bit**.
*   **Encapsulation**: The process of wrapping data with protocol headers (and trailers) as it moves **down** the OSI stack toward transmission. Each layer adds its own header.
*   **Decapsulation**: The reverse process — stripping headers as data moves **up** the OSI stack at the receiving end.
*   **MAC Address**: A 48-bit hardware address burned into a NIC (Network Interface Card), expressed as six pairs of hex digits (e.g., 00:1A:2B:3C:4D:5E). Used for Layer 2 delivery on a local segment. The first 24 bits identify the manufacturer (OUI).
*   **IP Address**: A logical Layer 3 address assigned to a network interface. IPv4 uses 32-bit dotted-decimal notation; IPv6 uses 128-bit hexadecimal notation. IP addresses identify both the network and the host.
*   **Network Topology – Star**: The most common topology in modern LANs. All devices connect to a central switch. Single point of failure is the central switch, but any single node failure does not affect others.
*   **Network Topology – Mesh**: Every node connects directly to every other node. Provides maximum redundancy. Full mesh connections formula: `n(n-1)/2`. Expensive to cable but used in WANs and critical backbone links.
*   **Network Topology – Bus**: All devices share a single coaxial backbone cable (legacy). A break in the cable disables the entire network.
*   **Network Topology – Ring**: Each device connects to exactly two neighbors, forming a circle. Used in legacy Token Ring and SONET/SDH fiber rings.
*   **Protocol Data Unit (PDU)**: The name given to the data at each OSI layer — bit (L1), frame (L2), packet (L3), segment/datagram (L4), data (L5–L7).

---

### 2. Certification Exam Tips
*   **Domain mapping (N10-009):** OSI model and network fundamentals fall under **Domain 1.0 – Networking Concepts (23%)**, the largest domain on the exam. Master it first.
*   **Layer identification trick**: Use the mnemonic "**All People Seem To Need Data Processing**" (Application, Presentation, Session, Transport, Network, Data Link, Physical) from top to bottom. For bottom-to-top: "**Please Do Not Throw Sausage Pizza Away**."
*   **Most commonly tested layer association**: Firewalls can operate at Layers 3, 4, or 7 — the exam will specify the type. A *stateful* firewall is Layer 4; a *next-generation/application firewall* is Layer 7.
*   **Trick question alert**: The exam often lists "Layer 2 switch" as a distractor for a question about routing. Remember: switches forward based on MAC addresses (Layer 2); routers forward based on IP addresses (Layer 3).
*   **PDU names must be exact**: The exam uses exact PDU terminology. "Segment" is TCP at Layer 4; "datagram" can refer to UDP at Layer 4 or an IP packet at Layer 3 in older usage — know context.
*   **TCP three-way handshake sequence**: SYN → SYN-ACK → ACK. The exam tests this in scenarios where a connection cannot be established.
*   **Memorize these key ports**: HTTP=80, HTTPS=443, FTP=20 (data) / 21 (control), SSH=22, Telnet=23, SMTP=25, DNS=53, DHCP=67/68, POP3=110, IMAP=143, SNMP=161, RDP=3389.
*   **Study Resource:** Professor Messer covers every OSI layer in depth in his free N10-009 study course. Start with his [CompTIA Network+ N10-009 video series](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/) — the OSI/TCP-IP model sections are typically in Section 1.

---

### Required Readings & Videos
*   **Required Reading:** Read the chapters covering **Network Models and the OSI Framework** in the OER Textbook: [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/). Focus on the sections explaining encapsulation, layer functions, and protocol mapping.
*   **Required Video:** Watch Professor Messer's free video on **The OSI Model** and **Network Topologies** from the [CompTIA Network+ N10-009 Course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/). These free videos align directly with exam domain 1.0 objectives.

---

### Lab & Command Integration
In this week's hands-on lab, you will use Cisco Packet Tracer or a VirtualBox network environment to observe Layer 2 vs. Layer 3 forwarding decisions. You will capture traffic with Wireshark to observe Ethernet frames (Layer 2 headers showing MAC addresses) and IP packets (Layer 3 headers showing IP addresses), demonstrating encapsulation directly.

---

### 3. Study Checklist
- [ ] Memorize all 7 OSI layers, their PDUs, their devices, and representative protocols for each.
- [ ] Be able to name the 4 TCP/IP model layers and map them to corresponding OSI layers.
- [ ] Read the **Network Models** section in [Computer Networking: Principles, Protocols and Practice](https://www.computer-networking.info/).
- [ ] Watch Professor Messer's OSI Model video from the [N10-009 course](https://www.professormesser.com/network-plus/n10-009/n10-009-video/n10-009-training-course/).
- [ ] Practice writing the PDU name for each OSI layer from memory.
- [ ] Proceed to the weekly hands-on lab activity.
