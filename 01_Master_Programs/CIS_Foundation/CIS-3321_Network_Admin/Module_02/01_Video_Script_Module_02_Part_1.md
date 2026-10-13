# Video Script: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Part 1 of 2 | Estimated Duration: 12–15 minutes
## Recorded by: Professor Nash | Texas Wesleyan University

---

### Pre-Roll Slide

[SHOW SLIDE: Course banner — "CIS-3321 Network Administration | Module 02: TCP/IP Model and Network Protocols | Texas Wesleyan University"]

---

### Section 1: Introduction

[00:00 – 01:15]

[SHOW SLIDE: Professor Nash on camera with module title card]

Welcome to Module 02. I'm Professor Nash. In Module 01, we learned the OSI model as a theoretical reference framework. In this module, we shift to the TCP/IP model — the protocol suite that actually runs the internet. While every network administrator knows the OSI model as a diagnostic and design tool, the TCP/IP model is what you work with every single day when you configure devices, troubleshoot protocols, and capture traffic.

Part 1 covers the TCP/IP model structure, how it compares to the OSI model, and the critical protocols at each layer — including IP, TCP, UDP, and ICMP. Part 2 covers application-layer protocols and their port numbers in depth, which is one of the highest-tested topic areas on the Network+ exam.

---

### Section 2: The TCP/IP Model — Four Layers

[01:15 – 04:00]

[SHOW DIAGRAM: A four-layer vertical stack for the TCP/IP model. From bottom to top: Network Access Layer, Internet Layer, Transport Layer, Application Layer. To the right, a seven-layer OSI model stack with dotted lines connecting: Network Access to Layers 1 and 2, Internet to Layer 3, Transport to Layer 4, Application to Layers 5 through 7.]

[Alt-text: Two vertical stacks shown side by side. Left stack is the TCP/IP model with four layers from bottom to top: Network Access, Internet, Transport, Application. Right stack is the OSI model with seven layers from bottom to top: Physical, Data Link, Network, Transport, Session, Presentation, Application. Dotted horizontal lines connect Network Access to Physical and Data Link, Internet to Network, Transport to Transport, and Application to Session through Application.]

The TCP/IP model was developed by the U.S. Department of Defense in the 1970s as the underlying framework for ARPANET — the precursor to the modern internet. Unlike the OSI model, TCP/IP is not just a reference framework. It is an actual working protocol suite used on every network device in existence today.

The TCP/IP model has four layers.

The Network Access Layer combines the functions of OSI Layers 1 and 2. This is where physical transmission and frame-level addressing happen. Ethernet, Wi-Fi (802.11), and ARP (Address Resolution Protocol) operate at this layer.

The Internet Layer corresponds to OSI Layer 3. This is where IP (Internet Protocol) operates. IP provides logical addressing and routing — it is responsible for getting packets from a source host to a destination host across multiple networks. ICMP (Internet Control Message Protocol) also lives at the Internet layer.

The Transport Layer corresponds to OSI Layer 4. TCP and UDP operate here.

The Application Layer encompasses OSI Layers 5, 6, and 7. All application-facing protocols live here — HTTP, HTTPS, FTP, SMTP, DNS, DHCP, SNMP, SSH, and more.

---

### Section 3: Internet Protocol — IP in Detail

[04:00 – 06:30]

[SHOW DIAGRAM: An IPv4 packet header diagram showing key fields: Version, IHL, Total Length, TTL, Protocol, Source IP Address, Destination IP Address, and Data payload.]

[Alt-text: A rectangular diagram representing an IPv4 packet header. The fields shown include Version (4 bits) and IHL (4 bits) in the top row, followed by Total Length (16 bits). Below that are TTL (8 bits), Protocol (8 bits), and Header Checksum (16 bits) on one row. The Source IP Address (32 bits) occupies the next row. The Destination IP Address (32 bits) occupies the row after. The data payload fills the remaining space below.]

IP is the core protocol of the internet. Every packet crossing a network carries an IP header with critical fields.

The Source IP Address (32 bits for IPv4) identifies where the packet came from.

The Destination IP Address (32 bits) identifies where the packet is going. Every router along the path reads this field to make its forwarding decision.

The TTL (Time to Live) field specifies how many router hops a packet can traverse before being discarded. Each router decrements the TTL by one. When TTL reaches zero, the router drops the packet and sends an ICMP "Time Exceeded" message back to the source. This prevents packets from looping through the network forever.

The Protocol field tells the receiving host what Layer 4 protocol is carried in the payload. Protocol 6 equals TCP. Protocol 17 equals UDP. Protocol 1 equals ICMP.

> **Network+ Exam Tip:** The TTL field is directly related to how traceroute works. The traceroute command sends packets with TTL values starting at 1, then 2, then 3, and so on. Each router that receives a packet with TTL equal to 1 drops it and returns an ICMP Time Exceeded message, revealing that router's IP address. This is how traceroute maps the path hop by hop.

---

### Section 4: TCP — Reliable Transport

[06:30 – 09:00]

[SHOW DIAGRAM: TCP three-way handshake sequence diagram. Three vertical elements labeled Client, Network (arrow line), and Server. Three horizontal arrows: SYN from Client to Server, SYN-ACK from Server to Client, ACK from Client to Server. Label at bottom: "TCP Connection Established."]

[Alt-text: A sequence diagram showing the TCP three-way handshake. On the left is a box labeled Client. On the right is a box labeled Server. Three horizontal arrows are shown: first arrow points from Client to Server and is labeled SYN. Second arrow points from Server to Client and is labeled SYN-ACK. Third arrow points from Client to Server and is labeled ACK. Below the third arrow, text reads "Connection Established — Data Transfer Begins."]

TCP is the protocol that makes the internet reliable. When you download a file, send an email, or load a web page, TCP ensures every byte arrives in the correct order and that any lost segments are retransmitted.

The TCP three-way handshake establishes a connection before data is transferred.

Step 1 — SYN. The client sends a TCP segment with the SYN (Synchronize) flag set to the server. This says "I want to open a connection, and here is my starting sequence number."

Step 2 — SYN-ACK. The server responds with a segment that has both the SYN and ACK flags set. This says "I received your SYN, here is my starting sequence number, and I acknowledge yours."

Step 3 — ACK. The client sends a final ACK to the server, confirming receipt of the server's SYN. The connection is now established and data transfer begins.

TCP uses sequence numbers and acknowledgements throughout the data transfer phase. If an ACK is not received within a timeout period, TCP retransmits the missing segment. This is why TCP is called "reliable" — not because the network is reliable, but because TCP adds the mechanisms to detect and recover from lost data.

---

### Section 5: UDP — Fast Connectionless Transport

[09:00 – 10:30]

[SHOW DIAGRAM: A two-column comparison table contrasting TCP and UDP across six rows: connection model, handshake, delivery guarantee, sequencing, overhead, and use cases.]

[Alt-text: A two-column comparison table. Column header on left reads TCP, column header on right reads UDP. Row 1: Connection-oriented versus Connectionless. Row 2: Three-way handshake required versus No handshake. Row 3: Guaranteed delivery versus No delivery guarantee. Row 4: Sequence numbers maintained versus No sequencing. Row 5: Higher per-packet overhead versus Lower overhead. Row 6: Use cases: HTTP, FTP, email versus Use cases: DNS queries, VoIP, video streaming, DHCP.]

UDP sacrifices reliability for speed. It sends data and does not wait for acknowledgements. There is no handshake and no retransmission mechanism.

Why would you use UDP? Because for real-time applications, a retransmitted packet is worse than a lost one. If you are on a VoIP call and a voice packet is delayed 300 milliseconds for retransmission, it creates an audible glitch. It is better to skip that packet and continue. The same logic applies to live video streaming, online gaming, and DNS queries.

UDP is also used for broadcast and multicast protocols like DHCP discovery, where establishing individual TCP connections to every potential client would be inefficient.

---

### Section 6: ICMP — Network Diagnostics

[10:30 – 12:30]

[SHOW SLIDE: ICMP message type table — Type 0: Echo Reply, Type 3: Destination Unreachable, Type 8: Echo Request, Type 11: Time Exceeded]

ICMP (Internet Control Message Protocol) operates at the Internet layer of the TCP/IP model, which corresponds to OSI Layer 3. It does not carry user data — it carries error messages and operational information between network devices.

The two ICMP messages you will use constantly are Echo Request (Type 8) and Echo Reply (Type 0). These are the messages sent and received by the ping command.

When ping sends an Echo Request and receives an Echo Reply, you have confirmed Layer 3 IP connectivity to that host. When ping returns "Destination Unreachable" (Type 3), it means no route exists to the destination or the destination host refused the connection. When ping returns "Time Exceeded" (Type 11), it means the TTL expired in transit — this is the foundation of how traceroute works.

> **Network+ Exam Tip:** ICMP is not TCP or UDP. It is a separate protocol carried directly within IP. Its Protocol field value in the IP header is 1. ICMP has no port number. On exam questions about ping and traceroute, the answer always involves ICMP.

---

### Section 7: Part 1 Summary

[12:30 – 14:00]

[SHOW SLIDE: Summary bullet list]

In Part 1, we covered the TCP/IP model's four layers and how they map to the OSI model. We examined IP header fields that govern routing and TTL behavior. We walked through the TCP three-way handshake and TCP's reliable delivery mechanism. We compared TCP and UDP and explained why both protocols exist. We covered ICMP and its role in diagnostic tools including ping and traceroute.

In Part 2, we go deep on application-layer protocols and their port numbers — the most directly tested area on the Network+ exam.

---

### Additional Resources

- Professor Messer's free CompTIA Network+ N10-008 Study Course: professormesser.com
- CompTIA official Network+ exam objectives: comptia.org

---

*End of Part 1*
