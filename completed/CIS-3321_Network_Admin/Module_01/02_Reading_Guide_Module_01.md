# Reading Guide: Module 01 – Networking Fundamentals and the OSI Model
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 01 establishes the conceptual foundation for every topic in this course. The OSI (Open Systems Interconnection) model is the most heavily tested architecture on the CompTIA Network+ exam. You must be able to identify which layer handles which function, which PDU exists at each layer, which devices operate at each layer, and which protocols map to which layer — all from a scenario description. Invest the time to master this module and every subsequent module becomes easier.

---

### 1. Core Vocabulary

The following terms are essential. Study each definition carefully and be able to apply it in a scenario context.

**OSI Model** — A seven-layer conceptual framework developed by the International Organization for Standardization (ISO) in 1984. It standardizes how data travels from one application to another across a network, allowing interoperability between devices from different vendors.

**Layer 7 – Application** — The layer closest to the end user where network-facing application protocols operate. Examples: HTTP (port 80), HTTPS (port 443), SMTP (port 25), FTP (ports 20/21), DNS (port 53), DHCP (ports 67/68). Note that this layer refers to the protocol interface, not the end-user application software itself.

**Layer 6 – Presentation** — Handles data formatting, translation, encryption/decryption, and compression. TLS/SSL encryption for HTTPS operates here. Character encoding standards such as ASCII and Unicode are a Presentation layer concern.

**Layer 5 – Session** — Manages the establishment, maintenance, and orderly termination of communication sessions between two hosts. Protocols: NetBIOS, RPC (Remote Procedure Call), SQL sessions.

**Layer 4 – Transport** — Provides end-to-end communication and reliability. TCP is connection-oriented, guarantees delivery through sequencing and acknowledgements, and initiates connections with the three-way handshake (SYN → SYN-ACK → ACK). UDP is connectionless, faster, with no delivery guarantee. PDU: segment (TCP) or datagram (UDP).

**Layer 3 – Network** — Handles logical addressing (IP addresses) and routing packets across networks. Routers and Layer 3 switches operate here. PDU: packet.

**Layer 2 – Data Link** — Handles physical (MAC) addressing and framing for node-to-node delivery on the same network segment. Switches and bridges operate here. Two sub-layers: LLC (Logical Link Control) and MAC (Media Access Control). PDU: frame.

**Layer 1 – Physical** — Transmits raw bits over the physical medium (copper wire, fiber optic, radio frequency). Devices: hubs, repeaters, cables, NICs (the physical aspect). PDU: bit.

**Encapsulation** — The process of wrapping data with protocol headers (and trailers) as it moves down the OSI stack toward transmission. Each layer adds its own header.

**Decapsulation** — The reverse process of stripping headers as data moves up the OSI stack at the receiving end.

**Protocol Data Unit (PDU)** — The name given to data at each OSI layer. The PDU names are: bit (Layer 1), frame (Layer 2), packet (Layer 3), segment or datagram (Layer 4), data (Layers 5–7).

**MAC Address** — A 48-bit hardware address burned into a Network Interface Card, expressed as six pairs of hexadecimal digits (e.g., 00:1A:2B:3C:4D:5E). The first 24 bits (OUI) identify the manufacturer. Used for Layer 2 delivery within a local segment.

**IP Address** — A logical Layer 3 address assigned to a network interface. IPv4 uses 32-bit dotted-decimal notation. IPv6 uses 128-bit hexadecimal notation. IP addresses identify both the network portion and the host portion.

**TCP (Transmission Control Protocol)** — A connection-oriented Layer 4 protocol that guarantees reliable, ordered delivery of data. Uses SYN/SYN-ACK/ACK handshake to establish connections. Provides flow control, error checking, and retransmission.

**UDP (User Datagram Protocol)** — A connectionless Layer 4 protocol optimized for speed over reliability. No handshake, no retransmission. Used for DNS queries, VoIP, video streaming, online gaming.

**Physical Topology** — The physical arrangement of network devices and cables.

**Logical Topology** — The path that data actually takes through the network, which may differ from the physical layout.

---

### 2. OSI Layer Reference Table

The following table summarizes the key attributes of each OSI layer. Memorize every column.

| Layer | Name         | PDU         | Key Devices              | Representative Protocols/Standards        |
|-------|--------------|-------------|--------------------------|-------------------------------------------|
| 7     | Application  | Data        | —                        | HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SNMP   |
| 6     | Presentation | Data        | —                        | TLS, SSL, JPEG, MPEG, ASCII, Unicode      |
| 5     | Session      | Data        | —                        | NetBIOS, RPC, SQL (session establishment) |
| 4     | Transport    | Segment/Datagram | —                   | TCP, UDP                                  |
| 3     | Network      | Packet      | Router, Layer 3 Switch   | IP, ICMP, ARP (some sources), OSPF, BGP   |
| 2     | Data Link    | Frame       | Switch, Bridge, NIC (L2) | Ethernet, Wi-Fi (802.11), ARP, PPP        |
| 1     | Physical     | Bit         | Hub, Repeater, Cable, NIC (physical) | 1000BASE-T, 802.3, DSL, T1  |

---

### 3. TCP/IP Model vs. OSI Model Mapping Table

| TCP/IP Layer   | OSI Layers Covered     | Protocols                              |
|----------------|------------------------|----------------------------------------|
| Application    | Layers 5, 6, 7         | HTTP, HTTPS, FTP, SMTP, DNS, DHCP      |
| Transport      | Layer 4                | TCP, UDP                               |
| Internet       | Layer 3                | IP, ICMP, OSPF, BGP                    |
| Network Access | Layers 1 and 2         | Ethernet, Wi-Fi, ARP, PPP              |

---

### 4. Network Topology Reference Table

| Topology | Physical Layout            | Key Advantage              | Key Disadvantage                        | Modern Use     |
|----------|---------------------------|----------------------------|-----------------------------------------|----------------|
| Bus      | Single shared backbone     | Low cost, simple           | One break kills entire network          | Legacy only     |
| Ring     | Circular daisy chain       | Equal access, predictable  | One break can disrupt ring              | SONET/SDH      |
| Star     | All devices to central hub/switch | Fault isolation, scalable | Central switch is single point of failure | Modern LANs |
| Mesh     | Every device connects to all others | Full redundancy      | Expensive, complex cabling              | WAN backbones  |
| Hybrid   | Combination of topologies  | Flexible                   | Complex to manage                       | Enterprise LANs |

**Full mesh connection formula:** n(n-1)/2, where n = number of nodes. For 5 nodes: 5(4)/2 = 10 connections required.

---

### 5. Well-Known Port Numbers

Memorizing these port numbers is mandatory for the Network+ exam.

| Port  | Protocol | Layer | Description                          |
|-------|----------|-------|--------------------------------------|
| 20    | FTP-Data | 7     | FTP data transfer                    |
| 21    | FTP-Control | 7  | FTP command channel                  |
| 22    | SSH      | 7     | Secure Shell encrypted terminal      |
| 23    | Telnet   | 7     | Unencrypted remote terminal (legacy) |
| 25    | SMTP     | 7     | Simple Mail Transfer Protocol (send) |
| 53    | DNS      | 7     | Domain Name System queries           |
| 67    | DHCP     | 7     | DHCP server (receives client request)|
| 68    | DHCP     | 7     | DHCP client (receives server reply)  |
| 80    | HTTP     | 7     | Web traffic unencrypted              |
| 110   | POP3     | 7     | Post Office Protocol v3 (receive)    |
| 123   | NTP      | 7     | Network Time Protocol                |
| 143   | IMAP     | 7     | Internet Message Access Protocol     |
| 161   | SNMP     | 7     | Simple Network Management Protocol  |
| 162   | SNMP Trap| 7     | SNMP trap notification               |
| 389   | LDAP     | 7     | Lightweight Directory Access Protocol|
| 443   | HTTPS    | 7     | HTTP over TLS (secure web)           |
| 3389  | RDP      | 7     | Remote Desktop Protocol              |

---

### 6. Encapsulation Process Detail

When a web browser sends an HTTP request, here is the layer-by-layer encapsulation sequence:

1. Layer 7 (Application): HTTP request created — "GET /index.html HTTP/1.1"
2. Layer 6 (Presentation): Data formatted; TLS encryption applied if HTTPS
3. Layer 5 (Session): Session established and tracked
4. Layer 4 (Transport): TCP header added — source port (random ephemeral), destination port 80 or 443, sequence number, ACK flag. PDU = Segment
5. Layer 3 (Network): IP header added — source IP address, destination IP address, TTL. PDU = Packet
6. Layer 2 (Data Link): Ethernet frame header added — source MAC, destination MAC. FCS trailer added. PDU = Frame
7. Layer 1 (Physical): Frame converted to electrical signals or light pulses and transmitted as bits

At the receiving end, decapsulation reverses this process layer by layer.

---

### 7. TCP Three-Way Handshake

The three-way handshake establishes a TCP connection before any data is sent.

1. SYN — Client sends a Synchronize packet to the server to initiate connection
2. SYN-ACK — Server responds with Synchronize-Acknowledge, confirming it received the SYN
3. ACK — Client sends a final Acknowledgement, completing the handshake. Data transfer begins.

Connection termination uses a four-way FIN/ACK process.

---

### 8. Certification Exam Tips

The following tips are based on the CompTIA Network+ N10-008 exam objectives and common question patterns.

**Tip 1:** OSI model questions fall under Domain 1.0 Networking Concepts, which accounts for 23% of the N10-008 exam — the largest domain. Prioritize this material above all others.

**Tip 2:** Use the mnemonic "Please Do Not Throw Sausage Pizza Away" (bottom to top) to recall layer order. Practice writing it from memory 10 times before test day.

**Tip 3:** When asked which layer a firewall operates at, the answer depends on the firewall type. A stateless packet-filtering firewall operates at Layer 3/4. A stateful inspection firewall operates at Layer 4. A next-generation or application-layer firewall operates at Layer 7.

**Tip 4:** The exam tests the distinction between PDU names. If the question involves a switch making forwarding decisions, the PDU is a frame (Layer 2). If the question involves a router making routing decisions, the PDU is a packet (Layer 3). Never confuse these.

**Tip 5:** The TCP/IP model question pattern: "An administrator is reviewing protocols at the TCP/IP Internet layer. Which OSI layer does this correspond to?" Answer: Layer 3 (Network). The TCP/IP Internet layer = OSI Network layer.

**Tip 6:** Know both physical and logical topology definitions. An exam scenario that physically looks like a star but data flows in a ring is logically a ring topology.

**Tip 7:** The three-way handshake sequence SYN → SYN-ACK → ACK is tested in connection troubleshooting scenarios. If you see that a TCP connection cannot complete, the exam will describe which step failed.

**Tip 8:** ARP (Address Resolution Protocol) is debated in OSI placement — it is commonly placed at Layer 2 or between Layers 2 and 3. For exam purposes, when asked about resolving an IP address to a MAC address on a local network, the answer involves ARP and Layer 2/3 boundary behavior.

---

### 9. Required Reading and Viewing

The following resources are free and directly aligned to this module.

**Required Reading:** Computer Networking: Principles, Protocols and Practice — Read the sections covering the OSI model, TCP/IP model, and network topologies. This open-access textbook is available at no cost.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the segments on the OSI model, network topologies, and the TCP/IP model. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives — available at comptia.org. Review Domain 1.0 Networking Concepts for the full list of testable objectives related to this module.

---

### 10. Study Checklist

Complete each item before moving to Module 02.

- [ ] Memorize all 7 OSI layers by name, number, and PDU — both top-to-bottom and bottom-to-top
- [ ] Write out the OSI layer table from memory with PDU, devices, and protocols for each layer
- [ ] Map all 4 TCP/IP model layers to their corresponding OSI layers
- [ ] Memorize all port numbers in Section 5 of this guide
- [ ] Explain encapsulation and decapsulation in your own words without notes
- [ ] Distinguish between physical topology and logical topology with an example
- [ ] Describe the TCP three-way handshake steps in order
- [ ] Watch Professor Messer's OSI model video at professormesser.com
- [ ] Read the network models chapter in the OER textbook
- [ ] Complete the Lab 01 Packet Tracer activity
- [ ] Post your Module 01 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 01 Quiz

---

## 9. Supplemental Resources

The following free, openly available resources provide additional depth and alternative explanations for Module 01 topics. No purchase or account is required.

**1. Professor Messer — CompTIA Network+ N10-008 Free Study Materials**
URL: https://www.professormesser.com/network-plus/n10-008/n10-008-video/
Relevance: Professor Messer's free video course covers the OSI model, network topologies, and TCP/IP in dedicated segments. His study notes and practice questions are also free. This is the single most aligned free resource for the Network+ exam.

**2. Computer Networking: Principles, Protocols and Practice (OER Textbook)**
URL: https://www.computer-networking.info/
Relevance: Open-access university-level textbook covering OSI/TCP-IP models, encapsulation, and protocol fundamentals at a depth appropriate for this module. Available as a free PDF download.

**3. Cisco Networking Academy — Introduction to Networks (Free)**
URL: https://www.netacad.com/
Relevance: Cisco NetAcad offers a free "Introduction to Networks" self-paced course that covers OSI layers, TCP/IP protocols, and Packet Tracer exercises — directly applicable to Module 01 and the lab activity.

**4. CompTIA Network+ Exam Objectives (N10-008) — Official PDF**
URL: https://www.comptia.org/certifications/network
Relevance: The official exam objectives document (free download from CompTIA) lists every testable concept. Domain 1.0 Networking Concepts, which covers OSI, is the largest domain at 23% of the exam.

**5. Wireshark — Free Packet Analyzer**
URL: https://www.wireshark.org/
Relevance: Wireshark is a free, open-source network protocol analyzer. Capturing live traffic and viewing real encapsulation headers at each OSI layer reinforces the theoretical concepts from this module with real-world observation.

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
