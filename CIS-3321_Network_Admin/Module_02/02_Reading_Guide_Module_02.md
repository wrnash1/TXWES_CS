# Reading Guide: Module 02 – TCP/IP Model and Network Protocols
## CIS-3321 Network Administration | CompTIA Network+ (N10-008)
## Texas Wesleyan University | Professor Nash

---

### Introduction

Module 02 bridges the OSI model from Module 01 to the practical TCP/IP protocol suite that powers every modern network. The TCP/IP model is what actually runs on the internet. CompTIA Network+ N10-008 expects you to map protocols to their correct layers, know their port numbers, distinguish TCP from UDP, and understand how key protocols like DHCP and DNS operate. Port numbers are among the most directly tested facts on the entire exam. Invest the time to memorize every entry in the tables below.

---

### 1. Core Vocabulary

**TCP/IP Model** — A four-layer practical networking model describing how data is transmitted across the internet. Layers (bottom to top): Network Access, Internet, Transport, Application.

**TCP (Transmission Control Protocol)** — A connection-oriented, reliable Layer 4 protocol that guarantees delivery through acknowledgements, sequencing, and retransmission. Establishes connections with a three-way handshake: SYN → SYN-ACK → ACK.

**UDP (User Datagram Protocol)** — A connectionless, unreliable Layer 4 protocol with no handshake and no guaranteed delivery. Used where speed outweighs reliability (VoIP, DNS queries, DHCP, video streaming).

**ICMP (Internet Control Message Protocol)** — A Layer 3 Internet-layer protocol for error reporting and diagnostics. Used by ping (Echo Request/Reply) and traceroute (Time Exceeded). Has no port number.

**HTTP (HyperText Transfer Protocol)** — Application-layer protocol for web browsing over port 80, TCP. Transmits data in cleartext.

**HTTPS (HTTP Secure)** — HTTP encrypted with TLS/SSL over port 443, TCP. The standard for all modern web traffic.

**FTP (File Transfer Protocol)** — File transfer protocol using port 21 (control) and port 20 (active data transfer). Credentials are sent in cleartext; SFTP (port 22) or FTPS are secure replacements.

**SSH (Secure Shell)** — Encrypted remote terminal access over port 22, TCP. Replaces Telnet (port 23, cleartext).

**Telnet** — Unencrypted remote terminal access over port 23, TCP. Legacy only; replace with SSH in all modern environments.

**SMTP (Simple Mail Transfer Protocol)** — Email sending and relay protocol over port 25, TCP. Port 587 for authenticated client submission.

**POP3 (Post Office Protocol v3)** — Downloads email to client and deletes from server. Port 110, TCP. Secure version POP3S uses port 995.

**IMAP (Internet Message Access Protocol)** — Accesses email on the server without deleting it. Port 143, TCP. Enables multi-device access. Secure IMAP uses port 993.

**DNS (Domain Name System)** — Resolves hostnames to IP addresses. Port 53 — UDP for queries, TCP for zone transfers.

**DHCP (Dynamic Host Configuration Protocol)** — Automatically assigns IP address, subnet mask, gateway, and DNS to clients. Port 67 (server), port 68 (client), UDP. Process: DORA.

**SNMP (Simple Network Management Protocol)** — Monitors and manages network devices. Port 161 (queries), port 162 (traps), UDP. SNMPv3 adds authentication and encryption.

**RDP (Remote Desktop Protocol)** — Microsoft graphical remote desktop. Port 3389, TCP.

**NTP (Network Time Protocol)** — Clock synchronization across network devices. Port 123, UDP.

**LDAP (Lightweight Directory Access Protocol)** — Directory service queries. Port 389, TCP. Secure LDAPS uses port 636.

**TTYL (Time to Live)** — An IP header field specifying the maximum number of router hops a packet may traverse. Decremented by 1 at each router. When TTL reaches 0, the packet is discarded and an ICMP Time Exceeded message is returned.

**DORA** — The DHCP four-step process: Discover, Offer, Request, Acknowledge.

**Three-Way Handshake** — TCP connection establishment: SYN → SYN-ACK → ACK.

**Well-Known Ports** — Port numbers 0–1,023 reserved for standard services assigned by IANA.

**Ephemeral Ports** — Temporary high-numbered ports (1,024–65,535) assigned dynamically by the OS for client-side connections.

---

### 2. TCP/IP Model vs. OSI Model Mapping

| TCP/IP Layer   | OSI Layers     | Key Protocols and Technologies                         |
|----------------|----------------|--------------------------------------------------------|
| Application    | 5, 6, 7        | HTTP, HTTPS, FTP, SSH, Telnet, SMTP, POP3, IMAP, DNS, DHCP, SNMP, RDP, NTP, LDAP |
| Transport      | 4              | TCP, UDP                                               |
| Internet       | 3              | IP, ICMP, ARP (logical), OSPF, BGP                     |
| Network Access | 1, 2           | Ethernet (802.3), Wi-Fi (802.11), PPP, ARP (physical)  |

---

### 3. Comprehensive Port Number Reference Table

Memorize every row in this table. Port number questions appear frequently on the Network+ exam.

| Port  | Protocol     | Transport | Direction / Notes                              |
|-------|--------------|-----------|------------------------------------------------|
| 20    | FTP-Data     | TCP       | FTP data channel (active mode)                 |
| 21    | FTP-Control  | TCP       | FTP command/control channel                    |
| 22    | SSH / SFTP   | TCP       | Encrypted terminal and file transfer           |
| 23    | Telnet       | TCP       | Unencrypted terminal — legacy, replace with SSH|
| 25    | SMTP         | TCP       | Email sending (server-to-server relay)         |
| 53    | DNS          | UDP/TCP   | UDP for queries; TCP for zone transfers        |
| 67    | DHCP Server  | UDP       | Server listens on 67, receives client requests |
| 68    | DHCP Client  | UDP       | Client listens on 68, receives server responses|
| 80    | HTTP         | TCP       | Unencrypted web traffic                        |
| 110   | POP3         | TCP       | Email download (deletes from server)           |
| 123   | NTP          | UDP       | Clock synchronization                          |
| 143   | IMAP         | TCP       | Email access (keeps mail on server)            |
| 161   | SNMP         | UDP       | Network device polling/queries                 |
| 162   | SNMP Trap    | UDP       | Unsolicited alerts from managed devices        |
| 389   | LDAP         | TCP       | Directory service queries                      |
| 443   | HTTPS        | TCP       | Encrypted web traffic (HTTP over TLS)          |
| 636   | LDAPS        | TCP       | LDAP over TLS (encrypted directory service)    |
| 993   | IMAPS        | TCP       | IMAP over TLS (encrypted email access)         |
| 995   | POP3S        | TCP       | POP3 over TLS (encrypted email download)       |
| 3389  | RDP          | TCP       | Windows Remote Desktop Protocol                |

---

### 4. TCP vs. UDP Comparison Table

| Characteristic        | TCP                            | UDP                            |
|-----------------------|--------------------------------|--------------------------------|
| Connection model      | Connection-oriented            | Connectionless                 |
| Handshake             | Three-way (SYN/SYN-ACK/ACK)    | None                           |
| Delivery guarantee    | Yes (acknowledgements + retry) | No                             |
| Ordering              | Sequence numbers maintained    | Not guaranteed                 |
| Error correction      | Retransmission on loss         | None built in                  |
| Speed                 | Slower (overhead for reliability)| Faster (minimal overhead)    |
| Use cases             | HTTP, HTTPS, FTP, SMTP, SSH, RDP | DNS queries, DHCP, VoIP, streaming, gaming |

---

### 5. DHCP DORA Sequence Detail

| Step        | Message       | Source    | Destination          | Details                                          |
|-------------|---------------|-----------|----------------------|--------------------------------------------------|
| 1 Discover  | DHCPDISCOVER  | Client    | 255.255.255.255 (broadcast) | Client has no IP; broadcasts to find server  |
| 2 Offer     | DHCPOFFER     | Server    | Client (broadcast or unicast) | Server proposes IP, mask, gateway, DNS, lease |
| 3 Request   | DHCPREQUEST   | Client    | 255.255.255.255 (broadcast) | Client formally requests offered IP          |
| 4 Acknowledge | DHCPACK     | Server    | Client               | Server confirms lease; client configures IP      |

DHCP lease renewal: Client attempts renewal at 50% of lease duration, then again at 87.5%. If both fail, the lease expires and the DORA process restarts.

---

### 6. DNS Record Types Reference Table

| Record Type | Purpose                                          | Example                                    |
|-------------|--------------------------------------------------|--------------------------------------------|
| A           | Maps hostname to IPv4 address                    | www.example.com → 93.184.216.34            |
| AAAA        | Maps hostname to IPv6 address                    | www.example.com → 2606:2800:220:1:248:1893:25c8:1946 |
| MX          | Identifies mail server for a domain              | example.com mail handled by mail.example.com |
| CNAME       | Canonical name — alias pointing to another hostname | shop.example.com → www.example.com      |
| PTR         | Reverse lookup — IP address to hostname          | 93.184.216.34 → www.example.com            |
| NS          | Identifies authoritative name servers for a zone | example.com → ns1.example.com             |
| SOA         | Start of Authority — zone admin information      | Serial, refresh, retry, expire parameters  |
| TXT         | Text records — used for SPF, DKIM, domain verification | "v=spf1 include:example.com ~all"     |

---

### 7. IP Header Key Fields

| Field            | Size    | Purpose                                                         |
|------------------|---------|-----------------------------------------------------------------|
| Version          | 4 bits  | IP version (4 for IPv4, 6 for IPv6)                             |
| IHL              | 4 bits  | Internet Header Length — number of 32-bit words in the header   |
| Total Length     | 16 bits | Total packet size including header and data                     |
| TTL              | 8 bits  | Maximum hops; decremented by 1 at each router; packet dropped at 0 |
| Protocol         | 8 bits  | Layer 4 protocol: 1=ICMP, 6=TCP, 17=UDP                        |
| Source Address   | 32 bits | Sender's IP address                                             |
| Destination Address | 32 bits | Receiver's IP address                                        |

---

### 8. Certification Exam Tips

**Tip 1:** Port numbers are tested constantly. The exam may give a scenario and ask which port is involved, or show a port number and ask you to identify the protocol. Both directions require memorization.

**Tip 2:** TCP vs. UDP decision rule: "reliability," "guaranteed delivery," "connection-oriented," and "acknowledgements" all point to TCP. "Speed," "real-time," "low overhead," and "streaming" point to UDP.

**Tip 3:** DNS is unique — it uses both UDP (queries) and TCP (zone transfers). The exam specifically tests this distinction.

**Tip 4:** The DHCP DORA sequence is a guaranteed exam topic. Remember that Discover and Request are broadcasts; Offer and Acknowledge can be unicast.

**Tip 5:** The exam describes Telnet as the cleartext management protocol on port 23. The correct secure replacement is always SSH on port 22.

**Tip 6:** The "secure" version rule: add TLS to the protocol name (HTTPS, FTPS, LDAPS, IMAPS, POP3S) and the port number shifts. HTTP 80 becomes HTTPS 443. IMAP 143 becomes IMAPS 993. POP3 110 becomes POP3S 995. LDAP 389 becomes LDAPS 636.

**Tip 7:** ICMP has no port number and is Protocol 1 in the IP header. The exam will never associate ping or traceroute with a port number.

**Tip 8:** TTL field exhaustion (TTL = 0) produces an ICMP Type 11 Time Exceeded message. This is the mechanism traceroute exploits to discover each hop.

---

### 9. Required Reading and Viewing

**Required Reading:** Computer Networking: Principles, Protocols and Practice — read the sections on Application Layer Protocols and the TCP/IP model. Focus on the TCP/UDP comparison and the DHCP exchange.

**Required Viewing:** Professor Messer's Network+ N10-008 video series — watch the segments on network protocols, TCP and UDP, DHCP, and DNS. Available free at professormesser.com.

**Supplemental Reference:** CompTIA official N10-008 exam objectives — available at comptia.org. Review Domain 1.0 Networking Concepts for the complete list of protocol and port objectives.

---

### 10. Study Checklist

- [ ] Memorize all port numbers in the reference table in Section 3 — both number and protocol name
- [ ] Be able to identify for each protocol whether it uses TCP, UDP, or both, and explain why
- [ ] Recite the DHCP DORA sequence from memory with source, destination, and purpose of each step
- [ ] Identify all DNS record types and their purposes from memory
- [ ] Explain the TCP three-way handshake in detail including what happens if the SYN-ACK is never received
- [ ] Explain why ICMP has no port number
- [ ] Watch Professor Messer's protocol and TCP/UDP videos at professormesser.com
- [ ] Read the application-layer protocols chapter in the OER textbook
- [ ] Complete the Lab 02 activity using nslookup and netstat
- [ ] Post your Module 02 Discussion initial response by Wednesday at 11:59 PM
- [ ] Complete the Module 02 Quiz

---

*CIS-3321 Network Administration | Texas Wesleyan University | Professor Nash*
